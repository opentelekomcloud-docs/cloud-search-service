:original_name: en-us_topic_0000001583146906.html

.. _en-us_topic_0000001583146906:

Deleting a Snapshot
===================

If you no longer need a snapshot, delete it to release storage resources. If the automatic snapshot creation function is enabled, snapshots that are automatically created cannot be deleted manually, and the system automatically deletes these snapshots on the half hour after the time specified by **Retention Period (days)**. If you disable the automatic snapshot creation function while retaining the automated snapshots, then you can manually delete them later. If you do not manually delete the automatically created snapshots and enable the automatic snapshot creation function again, then all snapshots with **Snapshot Type** set to **Automated** in the snapshot list of the cluster can only be automatically deleted by the system.

.. note::

   After a snapshot is deleted, its data cannot be restored. Exercise caution when deleting a snapshot.

#. In the snapshot list, locate the snapshot that you want to delete.
#. Click **Delete** in the **Operation** column. In the dialog box that is displayed, confirm the snapshot information and click **OK**.
