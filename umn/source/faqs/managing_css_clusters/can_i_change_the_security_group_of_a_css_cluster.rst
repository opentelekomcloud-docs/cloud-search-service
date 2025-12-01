:original_name: css_02_0123.html

.. _css_02_0123:

Can I Change the Security Group of a CSS Cluster?
=================================================

You can change the security group of an existing CSS cluster.

Constraints
-----------

-  It is advisable to perform this operation during off-peak hours.
-  The security group cannot be changed for clusters created before February 2023. To do that, create a new cluster by selecting the desired security group, then perform Migrating Data Between Elasticsearch Clusters Using Backup and Restoration to migrate its data to that new cluster.
-  Make sure the inbound rules of the new security group allow all the ports required for service access. For Elasticsearch and OpenSearch clusters, port 9200 must be allowed. For Logstash clusters, port 9600 must be allowed.

Changing the Security Group
---------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, expand **Clusters**. Select a cluster type based on the target cluster. The cluster list is displayed.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Click the **Overview** tab. In the **Configuration** area, click **Change Security Group** on the right of **Security Group**.
#. In the **Change Security Group** dialog box, select a new security group and click **OK**.
