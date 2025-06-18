:original_name: css_01_0050.html

.. _css_01_0050:

Viewing Elasticsearch Cluster Audit Logs
========================================

Cloud Trace Service (CTS) is available on the public cloud platform. With CTS, you can record operations associated with CSS for later query, audit, and backtrack operations.

Prerequisites
-------------

CTS has been enabled. For details, see `Enabling CTS <https://docs.otc.t-systems.com/en-us/usermanual/cts/en-us_topic_0030598498.html>`__.

Key Operations Recorded by CTS
------------------------------

.. table:: **Table 1** Key operations recorded by CTS

   +------------------------------------------------------------------+---------------+-----------------------------+
   | Operation                                                        | Resource Type | Event Name                  |
   +==================================================================+===============+=============================+
   | Creating a cluster                                               | cluster       | createCluster               |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying cluster details                                         | cluster       | showClusterDetail           |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Deleting a cluster                                               | cluster       | deleteCluster               |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Changing a cluster name                                          | cluster       | updateClusterName           |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying the cluster list                                        | cluster       | listClusters                |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Changing the password of a cluster                               | cluster       | resetPassword               |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Restarting a cluster                                             | cluster       | restartCluster              |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Expanding cluster capacity                                       | cluster       | updateExtendCluster         |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Adding instances and expanding storage                           | cluster       | updateExtendInstanceStorage |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Changing specifications                                          | cluster       | updateFlavor                |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining the instance specifications list                       | cluster       | listFlavors                 |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Removing specified nodes                                         | cluster       | updateShrinkNodes           |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Changing the specifications of a specified node type             | cluster       | updateFlavorByType          |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Scaling in nodes of a specific type                              | cluster       | updateShrinkCluster         |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Downloading a security certificate                               | cluster       | downloadCert                |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Replacing a node                                                 | cluster       | updateInstance              |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Changing the security mode                                       | cluster       | changeMode                  |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Adding a dedicated Master or Client node                         | cluster       | addIndependentNode          |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Upgrading the cluster kernel                                     | cluster       | upgradeCore                 |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining a target image ID                                      | cluster       | listImages                  |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining upgrade details                                        | cluster       | upgradeDetail               |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Retrying a failed upgrade task                                   | cluster       | retryUpgradeTask            |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Changing the security group                                      | cluster       | changeSecurityGroup         |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Creating a V2 cluster                                            | cluster       | createClusterV2             |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Restarting a V2 cluster                                          | cluster       | restartCluster              |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Rolling restart                                                  | cluster       | rollingRestart              |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Enabling Kibana public access                                    | cluster       | startKibanaPublic           |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling Kibana public access                                   | cluster       | updateCloseKibana           |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Modifying the Kibana public network bandwidth                    | cluster       | updateAlterKibana           |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Modifying Kibana public network access control                   | cluster       | updatePublicKibanaWhitelist |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling Kibana public network access control                   | cluster       | stopPublicKibanaWhitelist   |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Enabling logging                                                 | cluster       | startLogs                   |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling logging                                                | cluster       | stopLogs                    |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying the job list                                            | cluster       | listLogsJob                 |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying basic log configurations                                | cluster       | showGetLogSetting           |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Modifying basic log configurations                               | cluster       | updateLogSetting            |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Enabling automatic log backup                                    | cluster       | startLogAutoBackupPolicy    |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling automatic log backup                                   | cluster       | stopLogAutoBackupPolicy     |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Backing up logs                                                  | cluster       | createLogBackup             |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying logs                                                    | cluster       | showLogBackup               |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Enabling public network access                                   | cluster       | createBindPublic            |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling public access                                          | cluster       | updateUnbindPublic          |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Modifying public network access bandwidth                        | cluster       | updatePublicBandWidth       |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Enabling the public network access whitelist                     | cluster       | startPublicWhitelist        |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling the public network access whitelist                    | cluster       | stopPublicWhitelist         |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Automatically setting basic configurations of a cluster snapshot | cluster       | startAutoSetting            |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Modifying basic configurations of a cluster snapshot             | cluster       | updateSnapshotSetting       |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Manually creating a snapshot                                     | snapshot      | createSnapshot              |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Restoring a snapshot                                             | snapshot      | restoreSnapshot             |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Deleting a specified snapshot                                    | snapshot      | deleteSnapshot              |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Setting an automatic snapshot creation policy                    | cluster       | createAutoCreatePolicy      |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying automatic snapshot creation policies                    | cluster       | showAutoCreatePolicy        |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying the snapshot list                                       | cluster       | listSnapshots               |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling snapshot function                                      | cluster       | stopSnapshot                |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Enabling automatic snapshot creation                             | cluster       | startAutoCreateSnapshots    |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling automatic snapshot creation                            | cluster       | stopAutoCreateSnapshots     |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Enabling VPC Endpoint Service                                    | cluster       | startVpecp                  |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Disabling VPC Endpoint Service                                   | cluster       | stopVpecp                   |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining a VPCEP connection                                     | cluster       | showVpcepConnection         |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Updating a VPCEP connection                                      | cluster       | updateVpcepConnection       |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Modifying the VPCEP whitelist                                    | cluster       | updateVpcepWhitelist        |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Modifying parameter settings                                     | cluster       | listYmls                    |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining the task list of parameter settings                    | cluster       | listYmlsJob                 |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining the parameter settings list                            | cluster       | updateYmls                  |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying ELB V3 load balancers supported by a cluster            | cluster       | listElbs                    |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Enabling or disabling the Elasticsearch Load Balancer            | cluster       | enableOrDisableElb          |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Configuring an Elasticsearch listener                            | cluster       | createElbListener           |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining information about an Elasticsearch ELB                 | cluster       | showElbDetail               |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Updating an Elasticsearch listener                               | cluster       | updateEsListener            |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Querying the certificate list                                    | cluster       | listElbCerts                |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining the intelligent O&M task list and details              | cluster       | listAiOps                   |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Creating a cluster detection task                                | cluster       | createAiOps                 |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Deleting a detection task record                                 | cluster       | deleteAiOps                 |
   +------------------------------------------------------------------+---------------+-----------------------------+
   | Obtaining SMN topics available for intelligent O&M alarms        | cluster       | listSmnTopics               |
   +------------------------------------------------------------------+---------------+-----------------------------+

Querying Real-Time Traces
-------------------------

After a management tracker is created on the CTS console, the system starts recording operations performed on cloud service resources. After a data tracker is created, the system starts recording operations performed on data in OBS buckets. CTS retains operation records generated in the latest seven days.
