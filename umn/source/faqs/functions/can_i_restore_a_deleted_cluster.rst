:original_name: en-us_topic_0000001476817914.html

.. _en-us_topic_0000001476817914:

Can I Restore a Deleted Cluster?
================================

Yes. You can use a snapshot stored in OBS to restore a cluster. A deleted cluster that has no snapshots in OBS cannot be restored. Exercise caution when deleting a cluster.

To restore a deleted cluster, perform the following steps:

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters**. On the displayed **Clusters** page, click **Create Cluster** in the upper right corner to create a cluster and enable the snapshot function. Set the OBS bucket and backup path to those of the cluster to be restored.

   To restore a deleted cluster to an existing cluster, set the OBS bucket and backup path to those of the deleted cluster.

   .. important::

      To restore a deleted cluster to a new cluster, ensure they are in the same region. The new cluster version must be the same as or later than that of the deleted cluster. The number of nodes in the new cluster must be greater than half of that in the deleted cluster. Otherwise, the cluster may fail to be restored.

#. If the status of the new cluster changes to **Available**, click the cluster name to go to the **Cluster Information** page.

#. In the navigation pane on the left, choose **Cluster Snapshots**.

   In the snapshot management list, you can view the snapshot information of the deleted cluster. If no information is displayed, wait for several minutes and refresh the page.

#. Locate the target snapshot and click **Restore** in the **Operation** column. The **Restore** page is displayed.

#. On the **Restore** page, set restoration parameters.

   **Index**: Enter the name of the index you want to restore. If you do not specify any index name, data of all indexes will be restored. The value can contain 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?)`` are not allowed.

   **Rename Pattern**: Enter a regular expression. Indexes that match the regular expression are restored. The default value **index_(.+)** indicates restoring data of all indices. The value contains 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?,)`` are not allowed.

   **Rename Replacement**: Enter the index renaming rule. The default value **restored_index_$1** indicates that **restored\_** is added in front of the names of all restored indexes. The value can contain 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?,)`` are not allowed. You can set **Rename Replacement** only if you have specified **Rename Pattern**.

   **Cluster**: Select the cluster that you want to restore. You can select the current cluster or others. However, you can only restore the snapshot to clusters whose status is **Available**. If the status of the current cluster is **Unavailable**, you cannot restore the snapshot to the current cluster. If you select another cluster and two or more indexes in the cluster have the same name, data of all indices with the same name as the name you specify will be overwritten. Therefore, exercise caution when you set the parameters.


   .. figure:: /_static/images/en-us_image_0000001477137558.png
      :alt: **Figure 1** Restoring a snapshot

      **Figure 1** Restoring a snapshot

#. Click **OK**. If restoration succeeds, **Task Status** of the snapshot in the snapshot list will change to **Restoration succeeded**, and the index data is generated again according to the snapshot information.
