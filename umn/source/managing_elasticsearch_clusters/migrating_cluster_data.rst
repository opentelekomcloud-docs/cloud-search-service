:original_name: css_01_0040.html

.. _css_01_0040:

Migrating Cluster Data
======================

You can migrate data from one cluster to another. In certain scenarios, for example, if you cannot get sufficient capacity by changing the specifications of the current cluster, you can create a cluster of higher specifications and migrate all data of the current cluster to the new one. Alternatively, you can merge indices in two clusters to one cluster to meet your business needs. CSS enables you to migrate cluster data by using the index backup and restoration function, specifically, by restoring the snapshot of a cluster to the target cluster.

Prerequisites
-------------

-  The source and target clusters are in the same region.
-  The version of the target cluster is the same as or later than that of the source cluster.
-  The number of nodes in the target cluster must be greater than half of the number of nodes in the source cluster.

Suggestions
-----------

-  The number of nodes in the target cluster should be no less than the number of replicas in the source cluster.
-  The CPU, memory, and disk configurations of the target cluster should be no less than those of the source cluster. This will minimize service loss after migration.

In this section, assume that data of cluster **Es-1** is migrated to cluster **Es-2**. Cluster **Es-2** runs a version later than that of cluster **Es-1** and the number of nodes in cluster **Es-2** is greater than half of that in cluster **Es-1**.

Procedure
---------

#. On the **Clusters** page, click **Es-1**. On the displayed page, click **Cluster Snapshots**.

#. Click **Create Snapshot** to manually create a snapshot. In the displayed dialog box, enter the snapshot name and click **OK**.

   If you use the index backup and restoration function for the first time, you need to perform basic configurations first. For more details, see :ref:`Manually Creating a Snapshot <css_01_0033__section43906502025>`.


   .. figure:: /_static/images/en-us_image_0000001286596238.png
      :alt: **Figure 1** Creating a snapshot


      **Figure 1** Creating a snapshot

#. In the snapshot list, locate the row that contains the target snapshot and click **Restore** in the **Operation** column to restore data to cluster **Es-2**.

   -  Leave the **Index** option blank (default setting), indicating that you want to restore data of all indices in cluster **Es-1**.
   -  From the **Cluster** drop-down list, select **Es-2**.

   Click **OK**. You can also rename the restored index.


   .. figure:: /_static/images/en-us_image_0000001286436626.png
      :alt: **Figure 2** Restoring a snapshot


      **Figure 2** Restoring a snapshot

#. After restoration is complete, data in cluster **Es-1** will be migrated to cluster **Es-2**.
