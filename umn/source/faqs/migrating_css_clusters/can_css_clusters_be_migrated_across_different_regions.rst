:original_name: css_02_0094.html

.. _css_02_0094:

Can CSS Clusters Be Migrated Across Different Regions?
======================================================

In CSS, perform the following to migrate Elasticsearch clusters across different regions:

-  If the OBS bucket is in the same region as your CSS cluster, migrate the cluster by following the instructions in Index Backup and Restoration.
-  If the OBS bucket is not in the same region as your CSS cluster, configure cross-region replication to back up the cluster to the bucket, and migrate the cluster by following the instructions in Index Backup and Restoration.

.. note::

   -  Before cross-region replication, ensure the snapshot folder of the destination cluster is empty. Otherwise, the snapshot information cannot be updated to the snapshot list of the destination cluster.
   -  Before every migration, ensure the folder is empty.
