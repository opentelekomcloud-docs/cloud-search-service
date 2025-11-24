:original_name: css_01_0271.html

.. _css_01_0271:

Deleting an Elasticsearch Cluster Snapshot
==========================================

Delete snapshots that are no longer needed to reclaim storage spaces.

Constraints
-----------

-  Deleting a snapshot will permanently delete its data.
-  The deletion of automatically generated snapshots is subject to the following constraints:

   -  While automatic snapshot creation is enabled, the system automatically deletes snapshots on the nearest half hour after their retention period expires.
   -  After automatic snapshot creation is disabled, existing auto-created snapshots will not be deleted automatically, but they can be deleted manually.
   -  If automatic snapshot creation is re-enabled, the system resumes automatic deletion of all auto-created snapshots upon expiration, including these created before automatic snapshot creation was previously disabled.

Manually Deleting a Snapshot
----------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Click the **Cluster Snapshots** tab.
#. In the cluster snapshot task list, select the snapshot you want to delete, and click **Delete** in the **Operation** column. In the displayed dialog box, enter **DELETE** and click **OK**.
