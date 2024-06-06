:original_name: en-us_topic_0000001528097309.html

.. _en-us_topic_0000001528097309:

How Do I Migrate a CSS Cluster Across Regions?
==============================================

CSS clusters cannot be directly migrated. You can back up a cluster to an OBS bucket and restore it to a new region.

-  If the OBS bucket is in the same region as your CSS cluster, migrate the cluster by following the instructions in Index Backup and Restoration.
-  If the OBS bucket is not in the same region as your CSS cluster, configure cross-region replication to back up the cluster to the bucket, and migrate the cluster by following the instructions in Index Backup and Restoration.

.. note::

   -  Before cross-region replication, ensure the snapshot folder of the destination cluster is empty. Otherwise, the snapshot information cannot be updated to the snapshot list of the destination cluster.
   -  Before every migration, ensure the folder is empty.
