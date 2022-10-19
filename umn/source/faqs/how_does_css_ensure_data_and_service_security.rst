:original_name: css_02_0006.html

.. _css_02_0006:

How Does CSS Ensure Data and Service Security?
==============================================

CSS uses network isolation, in addition to various host and data security measures.

-  Network isolation

   The entire network is divided into two planes: service plane and management plane. The two planes are deployed and isolated physically to ensure the security of the service and management networks.

   -  Service plane: This is the network plane of the cluster. It provides service channels for users and delivers data definitions, indexing, and search capabilities.
   -  Management plane: This is the management console, where you manage CSS.

-  Host security

   CSS provides the following security measures:

   -  The VPC security group ensures the security of the hosts in a VPC.
   -  Network access control lists (ACLs) allow you to control what data can enter or exit your network.
   -  The internal security infrastructure (including the network firewall, intrusion detection system, and protection system) monitors all network traffic that enters or exits the VPC through an IPsec VPN.

-  Data security

   Multiple replicas, cross-AZ deployment of clusters, and third-party (OBS) backup of index data ensure the security of user data.
