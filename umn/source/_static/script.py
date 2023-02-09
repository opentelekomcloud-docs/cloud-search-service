#!/usr/bin/env python3

import argparse
import logging

import openstack
from otcextensions import sdk
import sys


conn = openstack.connect()

sdk.register_otc_extensions(conn)


logging.basicConfig(filename="debug.log", filemode="w", level=logging.DEBUG)
logger = logging.getLogger(__name__)


__author__ = "Vineet Pruthi<Vineet.Pruthi@t-systems.com>"


def print_table(table):

    # Get the maximum length of elements in each column
    longest_cols = [
        (max([len(str(row[i])) for row in table]) + 2)
        for i in range(len(table[0]))
    ]
    seperator = " +-" + "-+-".join(
        ["-" * col_length for col_length in longest_cols]
    ) + "-+ "
    # Create the format string for the rows
    row_format = " | " + " | ".join(
        ["{: <" + str(col_length) + "}" for col_length in longest_cols]
    ) + " | "

    for i, row in enumerate(table):
        # Print the header row
        if i == 0:
            # Print the top separator
            print(seperator)

            print(row_format.format(*row))
            # Print the separator after header
            print(seperator)
        else:
            print(row_format.format(*row))
    # Print the bottom separator
    print(seperator)


def print_elb_flavors(print_all=False):
    # elb_flavors = ConfigureELBv3().get_elb_flavors()
    rows = [
        "Flavor ID",
        "Name",
        "Max Connections",
        "Type",
        "Bandwidth (Mbit/s)"
    ]
    if print_all:
        flavors = conn.vlb.flavors()
    else:
        flavors = conn.vlb.flavors(type='L7')

    table = [
        (
            flavor.id,
            flavor.name,
            flavor.info["connection"],
            flavor.type,
            int(flavor.info["bandwidth"] / 1000)
        ) for flavor in flavors
    ]

    table = sorted(table, key=lambda x: (x[3], x[4]))
    table.insert(0, rows)
    print_table(table)


class ConfigureELBv3:
    """Configure Loadbalancer To access CSS Kibana Dashboard"""

    def __init__(self,
                 cluster_id,
                 certificate_id=None,
                 flavor_id=None,
                 name=None):

        self.cluster = self.get_css_cluster(cluster_id)
        self.certificate_id = certificate_id
        self.flavor_id = flavor_id or self.get_smallest_flavor_id()
        self.name = name

        self.cluster = conn.css.get_cluster(cluster_id)

        self.loadbalancer_id = None
        self.listener_id = None
        self.pool_id = None

    def get_css_cluster(self, cluster_id):
        return conn.css.find_cluster(
            cluster_id).to_dict(computed=False, original_names=True)

    def get_subnet(self):
        # cluster subnetId is network Id in neutron
        return next(
            conn.network.subnets(network_id=self.cluster["subnetId"]),
            None
        )

    def add_securitygroup_rule(self):
        subnet = self.get_subnet()
        params = {
            "security_group_id": self.cluster["securityGroupId"],
            "direction": "ingress",
            "protocol": "tcp",
            "port_range_min": 5601,
            "port_range_max": 5601
        }
        for rule in conn.network.security_group_rules(**params):
            if rule.remote_ip_prefix == subnet.cidr:
                print("Security Group Rule already added to allow ELB Access")
                return

        attrs = {
            "security_group_id": self.cluster["securityGroupId"],
            "direction": "ingress",
            "protocol": "tcp",
            "port_range_min": 5601,
            "port_range_max": 5601,
            "remote_ip_prefix": subnet.cidr
        }
        conn.network.create_security_group_rule(**attrs)

    def get_smallest_flavor_id(self):
        flavors_data = [[flavor.id, flavor.info["bandwidth"]]
                        for flavor in conn.vlb.flavors(type="L7")]
        flavors_data = sorted(flavors_data, key=lambda x: x[1])
        return flavors_data[0][0]

    def create_loadbalancer(self):
        name = self.name or "elb-" + self.cluster["name"]

        if conn.vlb.find_load_balancer(name, ignore_missing=True):
            print("Loadbalancer already exists with name: " + name)
            print("Specify a custom name.")
            sys.exit(1)

        availability_zones = [az.code for az in conn.vlb.availability_zones()
                              if az.state == "ACTIVE"]

        attrs = {
            "vpc_id": self.cluster["vpcId"],
            "availability_zone_list": availability_zones,
            "elb_virsubnet_ids": [self.cluster["subnetId"]],
            "l7_flavor_id": self.flavor_id,
            "name": name,
            "publicip": {
                "network_type": "5_gray",
                "bandwidth": {
                    "size": 10,
                    "share_type": "PER",
                    "charge_mode": "traffic",
                    "name": "elb_eip_traffic"
                }
            }
        }
        loadbalancer = conn.vlb.create_load_balancer(**attrs)
        self.loadbalancer_id = loadbalancer.id
        return loadbalancer

    def create_listener(self):
        attrs = {
            "protocol_port": 443,
            "protocol": "HTTPS",
            "loadbalancer_id": self.loadbalancer_id,
            "name": "listener-" + (self.name or self.cluster["name"]),
            "default_tls_container_ref": self.certificate_id
        }
        if not self.certificate_id:
            attrs["protocol_port"] = 80
            attrs["protocol"] = "HTTP"
        listener = conn.vlb.create_listener(**attrs)
        self.listener_id = listener.id

    def create_pool(self):
        attrs = {
            "name": "pool-" + (self.name or self.cluster["name"]),
            "lb_algorithm": "ROUND_ROBIN",
            "listener_id": self.listener_id,
            "protocol": "HTTP"
        }
        pool = conn.vlb.create_pool(**attrs)
        self.pool_id = pool.id

    def add_pool_members(self):
        subnet = self.get_subnet()
        node_ips = []
        for instance in self.cluster["instances"]:
            if instance["type"] == "ess":
                node_ips.append(instance["ip"])
        if node_ips == []:
            raise RuntimeError("No instance type ess")
        for node_ip in node_ips:
            attrs = {
                "subnet_cidr_id": subnet.id,
                "protocol_port": 5601,
                "address": node_ip
            }
            conn.vlb.create_member(self.pool_id, **attrs)


def create_elb(cluster_id, certificate_id=None, flavor_id=None, name=None):
    obj = ConfigureELBv3(cluster_id, certificate_id, flavor_id, name)

    print("\nCreating Loadbalancer...")
    loadbalancer = obj.create_loadbalancer()

    print("\nCreating Listener...")
    obj.create_listener()

    print("\nCreating Server Group (Pool)...")
    obj.create_pool()

    print("\nAdding CSS Cluster Nodes to Server Group (Pool)...")
    obj.add_pool_members()

    print("\nAdding Security Group Rule to allow access from ELB...")
    obj.add_securitygroup_rule()

    public_ip = next(iter(loadbalancer.floating_ips), None)["publicip_address"]
    url = "http://" + public_ip
    if certificate_id:
        url = "https://" + public_ip
    print("\nYour LoadBalancer %s is ready. You can access "
          "Kibana Dashboard using %s\n" % (loadbalancer.name, url))


def delete_elb(name_or_id, release_public_ip=False):
    """Delete a LoadBalancer"""

    print("\nGetting Details of the Loadbalancer:  %s" % name_or_id)
    loadbalancer = conn.vlb.find_load_balancer(name_or_id, False)

    for pool in loadbalancer.pools:
        print("\nRemoving members from Server Group (Pool):  %s" % pool["id"])
        for member in conn.vlb.get_pool(pool["id"]).members:
            conn.vlb.delete_member(member["id"], pool["id"])

        print("\nDeleting Server Group (Pool):  %s" % pool["id"])
        conn.vlb.delete_pool(pool["id"])

    for listener in loadbalancer.listeners:
        print("\nDeleting Listener:  %s" % listener["id"])
        conn.vlb.delete_listener(listener["id"])

    print("\nDeleting Loadbalancer:  %s" % name_or_id)
    conn.vlb.delete_load_balancer(loadbalancer.id)

    if release_public_ip:
        public_ip = next(iter(loadbalancer.floating_ips), None)
        if not public_ip:
            print("\nThere's no Public IP bound.")
            sys.exit(0)
        print("\nReleasing The Public IP:  %s" % public_ip["publicip_address"])
        conn.network.delete_ip(public_ip["publicip_id"])
    print("")


def main():
    parser = argparse.ArgumentParser(prog="Script to Configure LoadBalancer.")
    subparsers = parser.add_subparsers(dest="command")

    # Subparser for the "elb-flavors" subcommand
    elb_flavors = subparsers.add_parser(
        "elb-flavors",
        help="List Dedicated Loadbalancer Flavors."
    )
    elb_flavors.add_argument(
        "--all",
        action="store_true",
        help=("List All the Flavors.")
    )

    # Subparser for the "elb-configure" subcommand
    elb_configure = subparsers.add_parser(
        "elb-configure",
        help=("Create and configure a Dedicated LoadBalancer to Access "
              "CSS Kibana Dashboard.")
    )
    elb_configure.add_argument(
        "--cluster-id",
        required=True,
        help=("CSS Cluster ID.")
    )
    elb_configure.add_argument(
        "--certificate-id",
        help=("Tls Certificate ID to configure your Loadbalancer with "
              "HTTPS listener.")
    )
    elb_configure.add_argument(
        "--flavor-id",
        help=("Dedicated Loadbalancer Flavor ID.")
    )
    elb_configure.add_argument(
        "--name",
        help=("Specify the name of loadbalancer.")
    )

    # Subparser for the "elb-delete" subcommand
    elb_delete = subparsers.add_parser(
        "elb-delete",
        help=("Delete a Dedicated Loadbalancer Configured "
              "for CSS Kibana Access.")
    )
    elb_delete.add_argument(
        "loadbalancer",
        help=("Loadbalancer Name or ID.")
    )
    elb_delete.add_argument(
        "--release-public-ip",
        action="store_true",
        help=("Release EIP Bound to Loadbalancer.")
    )

    # Parse the arguments
    args = parser.parse_args()

    if args.command == "elb-flavors":
        print_elb_flavors(args.all)
    elif args.command == "elb-configure":
        create_elb(
            args.cluster_id,
            args.certificate_id,
            args.flavor_id,
            args.name
        )
    elif args.command == "elb-delete":
        delete_elb(args.loadbalancer, args.release_public_ip)


if __name__ == "__main__":
    main()
