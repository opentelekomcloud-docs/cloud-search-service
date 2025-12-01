:original_name: css_01_0280.html

.. _css_01_0280:

Configuring Routes for an OpenSearch Cluster
============================================

By default, a CSS OpenSearch cluster cannot access a target service—such as a client program or a Lightweight Directory Access Protocol (LDAP) service—that is located in a different VPC. To enable it, you need to configure a route for the cluster.

#. Establish a VPC peering connection to connect two VPCs.
#. On CSS, configure a route for the OpenSearch cluster that points to the client.
#. Verify network connectivity after starting services.

Configuring routes to enable cluster communication offers the following advantages:

-  Improved cross-VPC communication performance: A route table specifies the traffic forwarding paths, so that traffic does not have to pass through the public network.
-  Secure communication: Private networks can communicate through VPC peering connections, which is more secure than transmitting data over the public network.
-  Flexible access control policies: You can customize access permissions for specific subnets.
-  Support for a hybrid cloud architecture: Services can communicate across VPCs in different environments.

Constraints
-----------

-  By default, routes can be configured only for OpenSearch clusters whose image version is no earlier than x.x.x_25.3.0_x.x.x.
-  Adding cluster routes will alter network connections, possibly causing disruptions in the network. Exercise caution.

Prerequisites
-------------

-  The OpenSearch cluster is Available, and port 9200 is allowed in the inbound direction by the cluster's security group.
-  The client is running properly, and the server's security group allows port 9200 in the outbound direction.

Establishing a VPC Peering Connection
-------------------------------------

Before configuring routes for a CSS cluster, establish a connection between the CSS cluster's VPC and that of the client, that is, a VPC peering connection.

-  If the CSS cluster and the client belong to the same account, see section "Creating a VPC Peering Connection to Connect Two VPCs in the Same Account" in *Virtual Private Cloud User Guide*.
-  If the CSS cluster and the client belong to different accounts, see section "Creating a VPC Peering Connection to Connect Two VPCs in Different Accounts" in *Virtual Private Cloud User Guide*.

Set the peer VPC to the VPC where the CSS cluster is located and the local VPC to the VPC where the client is located.

When adding routes for a VPC peering connection, configure the destination addresses based on service requirements.

If the CSS cluster and the client share the same security group, there is no need to configure security group rules for the instances in the VPC at either end of the VPC peering connection.

Configuring a Route for an OpenSearch Cluster
---------------------------------------------

Configure a route for the OpenSearch cluster that points to the client, enabling the cluster to access the client.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Click the **Overview** tab. In the **Configuration** area, click **Add Route** next to **Cluster Route**.


   .. figure:: /_static/images/en-us_image_0000002272416338.png
      :alt: **Figure 1** Adding a route

      **Figure 1** Adding a route

#. In the displayed dialog box, configure the route information.

   .. table:: **Table 1** Adding a route

      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                  |
      +===================================+==============================================================================================================================================================================================================================+
      | IP Address                        | Enter the IP address (or a CIDR block) of the client or server that the cluster needs to access, for example, **10.10.1.0**.                                                                                                 |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Subnet Mask                       | Enter the subnet mask used with the IP address.                                                                                                                                                                              |
      |                                   |                                                                                                                                                                                                                              |
      |                                   | The subnet mask must align with the network part of the IP address. That is:                                                                                                                                                 |
      |                                   |                                                                                                                                                                                                                              |
      |                                   | -  The network bits (the 1s) of the subnet mask must encompass those of the IP address.                                                                                                                                      |
      |                                   | -  The host bits (the 0s) of the subnet mask must accommodate the IP address's host bits.                                                                                                                                    |
      |                                   |                                                                                                                                                                                                                              |
      |                                   | The subnet mask should not cover too wide a range, avoiding unnecessary IP address exposure or waste of the address space. 255.255.255.0 (that is, /24) is recommended, which applies to most internal networking scenarios. |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **OK** to add the route.

   After the route is added, click **View Route** to check the route information. You can click **Add Route** to add another route; or click **Delete Route** to delete one—In the **Delete Route** dialog box, select a route, enter **DELETE** manually, and then click **OK**.

Testing Connectivity
--------------------

Connectivity between the OpenSearch cluster and client cannot be verified right away. After the route is configured, start services. If the search service can be accessed, the route is configured successfully.
