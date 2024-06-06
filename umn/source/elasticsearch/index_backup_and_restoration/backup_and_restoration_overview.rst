:original_name: en-us_topic_0000001633303977.html

.. _en-us_topic_0000001633303977:

Backup and Restoration Overview
===============================

You can back up index data in clusters. If data loss occurs or you want to retrieve data of a specified duration, you can restore the index data. Index backup is implemented by creating cluster snapshots. When creating a backup for the first time, you are advised to back up data of all indexes.

-  :ref:`Managing Automatic Snapshot Creation <en-us_topic_0000001583460750>`: Snapshots are automatically created at a specified time each day according to the rules you create. You can enable or disable the automatic snapshot creation function and set the automatic snapshot creation policy.
-  :ref:`Manually Creating a Snapshot <en-us_topic_0000001633220693>`: You can manually create a snapshot at any time to back up all data or data of specified indexes.
-  :ref:`Restoring Data <en-us_topic_0000001583300810>`: You can use existing snapshots to restore the backup index data to a specified cluster.
-  :ref:`Deleting a Snapshot <en-us_topic_0000001583146906>`: Delete snapshots you do not require and release resources.
