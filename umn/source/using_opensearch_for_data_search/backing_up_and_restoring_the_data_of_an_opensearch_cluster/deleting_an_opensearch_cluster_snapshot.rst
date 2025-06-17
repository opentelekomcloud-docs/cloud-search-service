:original_name: css_01_0482.html

.. _css_01_0482:

Deleting an OpenSearch Cluster Snapshot
=======================================

If you no longer need a snapshot, delete it to reclaim storage space.

If automatic snapshot creation is enabled, snapshots that are automatically created cannot be deleted manually. Instead, the system automatically deletes these snapshots on the half hour after the time specified by **Retention Period (days)** elapses.

If you disable automatic snapshot creation while retaining the automatically created snapshots, then you can manually delete these snapshots later. If you do not manually delete the automatically created snapshots but later enable automatic snapshot creation again, then all these snapshots (with **Snapshot Type** set to **Automated** in the snapshot list of the cluster) can only be automatically deleted by the system.

.. note::

   After a snapshot is deleted, its data cannot be restored. Exercise caution.

Manually Deleting a Snapshot
----------------------------

#. Log in to the CSS management console.
#. On the **Clusters** page, click the name of the target cluster. In the navigation pane on the left, choose **Cluster Snapshots**.
#. In the snapshot list, locate the snapshot you want to delete.
#. Click **Delete** in the **Operation** column. In the displayed dialog box, confirm the snapshot information, manually type in **DELETE**, and click **OK**.
