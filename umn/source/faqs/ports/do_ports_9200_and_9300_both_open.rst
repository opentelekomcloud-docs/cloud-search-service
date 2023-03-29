:original_name: css_02_0083.html

.. _css_02_0083:

Do Ports 9200 and 9300 Both Open?
=================================

Yes. Port 9200 is used by external systems to access CSS clusters, and port 9300 is used for communication between nodes.

The methods for accessing port 9300 are as follows:

-  If your client is in the same VPC and subnet with the CSS cluster, you can access it directly.
-  If your client is in the same VPC with but different subnet from the CSS cluster, apply for a route separately.
-  If your client is in the different VPCs and subnets from the CSS cluster, create a VPC peering connection to enable communication between the two VPCs, and then apply for routes to connect the two subnets.
