:original_name: css_01_0033.html

.. _css_01_0033:

Backup and Restoration Overview
===============================

You can back up index data in clusters. If data loss occurs or you want to retrieve data of a specified duration, you can restore the index data. Index backup is implemented by creating cluster snapshots. When creating a backup for the first time, you are advised to back up data of all indexes.

-  :ref:`Managing Automatic Snapshot Creation <css_01_0267>`: Snapshots are automatically created at a specified time each day according to the rules you create. You can enable or disable the automatic snapshot creation function and set the automatic snapshot creation policy.
-  :ref:`Manually Creating a Snapshot <css_01_0268>`: You can manually create a snapshot at any time to back up all data or data of specified indexes.
-  :ref:`Restoring Data <css_01_0266>`: You can use existing snapshots to restore the backup index data to a specified cluster.
-  :ref:`Deleting a Snapshot <css_01_0271>`: Delete snapshots you do not require and release resources.
