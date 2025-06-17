:original_name: css_02_0123.html

.. _css_02_0123:

Can I Modify the Security Group for Elasticsearch and OpenSearch Clusters in CSS?
=================================================================================

After a cluster is created, you can modify its security group.

.. important::

   -  Before changing the security group, ensure that the port 9200 required for service access has been enabled. Incorrect security group configuration may cause service access failures. Exercise caution when performing this operation.
   -  You are advised to perform this operation during off-peak hours.
   -  The security group of a cluster created before February 2023 cannot be modified. To do that, perform Migrating Data Between Elasticsearch Clusters Using Backup and Restoration to migrate its data to a new cluster, and then modify the security group of the new cluster.

#. Log in to the CSS management console.

#. In the navigation pane, choose **Clusters**. The cluster list is displayed.

#. Click the name of a cluster to go to the cluster details page.

#. On the right of **Security Group**, click **Change Security Group**.


   .. figure:: /_static/images/en-us_image_0000001960517889.png
      :alt: **Figure 1** Changing a security group

      **Figure 1** Changing a security group

#. In the **Change Security Group** dialog box, select a new security group and click **OK**.
