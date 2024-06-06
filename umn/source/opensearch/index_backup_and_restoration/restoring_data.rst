:original_name: en-us_topic_0000001591285456.html

.. _en-us_topic_0000001591285456:

Restoring Data
==============

You can use existing snapshots to restore the backup index data to a specified cluster.

Prerequisites
-------------

To use the function of creating or restoring snapshots, the account or IAM user logging in to the CSS management console must have both of the following permissions:

-  **Tenant Administrator** for project **OBS** in region **Global service**
-  **CSS Administrator** in the current region

Precautions
-----------

-  Cluster snapshots will increase the CPU usage and disk I/O. You are advised to take cluster snapshots during off-peak hours.
-  If snapshots have been stored in the OBS bucket, the OBS bucket cannot be changed. You can disable the snapshot function, then enable the snapshot function, and specify a new OBS bucket. After you disable the snapshot function, you cannot use previously created snapshots to restore the cluster.
-  If a cluster is in the **Unavailable** status, you can use the cluster snapshot function only to restore clusters and view existing snapshot information.
-  During backup and restoration of a cluster, you can perform only certain operations, including scaling out, accessing Kibana, viewing metric, and deleting other snapshots of clusters. However, you cannot perform the following operations: restarting or deleting the cluster, deleting a snapshot that is in the **Creating** or **Restoring** status, and creating or restoring another snapshot. If a snapshot is being created or restored for a cluster, any automatic snapshot creation task initiated for the cluster will be canceled.
-  Cluster data cannot be queried during snapshot restoration.
-  If you restore a CSS cluster snapshot to another cluster, indexes with the same name in the destination cluster will be overwritten. If the snapshot and the destination cluster use different shards, the indexes with the same name will not be overwritten.
-  The version of the destination cluster used for restoration must be the same as or higher than that of the source cluster.


Restoring Data
--------------

You can use snapshots whose **Snapshot Status** is **Available** to restore cluster data. The stored snapshot data can be restored to other clusters.

Restoring data will overwrite current data in clusters. Therefore, exercise caution when restoring data.

#. In the **Snapshots** area, locate the row that contains the snapshot you want to restore and click **Restore** in the **Operation** column.

#. On the **Restore** page, set restoration parameters.

   **Index**: Enter the name of the index you want to restore. If you do not specify any index name, data of all indexes will be restored. The value can contain 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?)`` are not allowed. You can use the asterisk (``*``) to match multiple indexes. For example, **index\*** indicates that all indexes with the prefix **index** in snapshots are restored.

   **Rename Pattern**: Enter a regular expression. Indexes that match the regular expression are restored. The default value **index_(.+)** indicates restoring data of all indexes. The value contains 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?,)`` are not allowed.

   **Rename Replacement**: Enter the index renaming rule. The default value **restored_index_$1** indicates that **restored\_** is added in front of the names of all restored indexes. The value contains 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?,)`` are not allowed.

   .. note::

      The **Rename Pattern** and **Rename Replacement** take effect only when they are configured at the same time.

   **Cluster**: Select the name of the cluster to be restored. You can select the cluster of the current version. However, you can only restore the snapshot to clusters whose status is **Available**. If the status of the current cluster is **Unavailable**, you cannot restore the snapshot to the current cluster. If the target cluster you selected has an index with the same name as the original cluster, data in the index will be overwritten after the restoration. Exercise caution when performing this operation.


   .. figure:: /_static/images/en-us_image_0000001655964997.png
      :alt: **Figure 1** Restoring a snapshot

      **Figure 1** Restoring a snapshot

#. Click **OK**. If restoration succeeds, **Task Status** of the snapshot in the snapshot list will change to **Restoration succeeded**, and the index data is generated again according to the snapshot information.


   .. figure:: /_static/images/en-us_image_0000001607164742.png
      :alt: **Figure 2** Successful restoration

      **Figure 2** Successful restoration
