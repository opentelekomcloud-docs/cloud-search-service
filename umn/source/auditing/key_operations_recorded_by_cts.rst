:original_name: en-us_topic_0000001528299573.html

.. _en-us_topic_0000001528299573:

Key Operations Recorded by CTS
==============================

Cloud Trace Service (CTS) is available on the public cloud platform. With CTS, you can record operations associated with CSS for later query, audit, and backtrack operations.

Prerequisites
-------------

CTS has been enabled. For details, see `Enabling CTS <https://docs.otc.t-systems.com/en-us/usermanual/cts/en-us_topic_0030598498.html>`__.


Key Operations Recorded by CTS
------------------------------

.. table:: **Table 1** Key operations recorded by CTS

   +--------------------------------------------------------+---------------+--------------------------+
   | Operation                                              | Resource Type | Event Name               |
   +========================================================+===============+==========================+
   | Creating a cluster                                     | cluster       | createCluster            |
   +--------------------------------------------------------+---------------+--------------------------+
   | Deleting a cluster                                     | cluster       | deleteCluster            |
   +--------------------------------------------------------+---------------+--------------------------+
   | Expanding the cluster capacity                         | cluster       | roleExtendCluster        |
   +--------------------------------------------------------+---------------+--------------------------+
   | Restarting a cluster                                   | cluster       | rebootCluster            |
   +--------------------------------------------------------+---------------+--------------------------+
   | Performing basic configurations for a cluster snapshot | cluster       | updateSnapshotPolicy     |
   +--------------------------------------------------------+---------------+--------------------------+
   | Setting the automatic snapshot creation policy         | cluster       | updateAutoSnapshotPolicy |
   +--------------------------------------------------------+---------------+--------------------------+
   | Upgrading a cluster                                    | cluster       | upgradeCluster           |
   +--------------------------------------------------------+---------------+--------------------------+
   | Retrying the upgrade                                   | cluster       | retryAction              |
   +--------------------------------------------------------+---------------+--------------------------+
   | Manually creating a snapshot                           | snapshot      | createSnapshot           |
   +--------------------------------------------------------+---------------+--------------------------+
   | Restoring a snapshot                                   | snapshot      | restoreSnapshot          |
   +--------------------------------------------------------+---------------+--------------------------+
   | Deleting a snapshot                                    | snapshot      | deleteSnapshot           |
   +--------------------------------------------------------+---------------+--------------------------+
