:original_name: css_02_0081.html

.. _css_02_0081:

Can I Expand the Subnet for an Elasticsearch or OpenSearch Cluster?
===================================================================

If the current subnet of an existing Elasticsearch or OpenSearch cluster cannot meet your requirements, you can switch to another subnet.

**Constraints**

-  After switching the subnet, the new subnet is used for adding nodes, including scaling, adding dedicated master/client nodes, and enabling VPC Endpoint. IP addresses will be allocated to newly added nodes from the new subnet.
-  A cluster can be associated with a maximum of two subnets.
-  Subnet switching does not affect the network settings of existing nodes.

**Procedure**

#. Log in to the CSS management console.
#. In the navigation pane on the left, expand **Clusters**. Select a cluster type based on the target cluster. The cluster list is displayed.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Click the **Overview** tab.
#. In the **Network Information** area, click **Change Subnet** under **Current Subnet**. In the displayed dialog box, select a new subnet. If there are no subnets that meet your requirements, click **Create Subnet** to go to the networking service console to create a new subnet.
#. Click **OK** after you change the subnet.
