:original_name: ListSnapshots.html

.. _ListSnapshots:

Querying a Snapshot List
========================

Function
--------

This API is used to query all the snapshots of a cluster.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose snapshots you want to query.                                                                             |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------+---------------------------------------------------------------------------------------------------+---------------+
   | Parameter | Type                                                                                              | Description   |
   +===========+===================================================================================================+===============+
   | backups   | Array of :ref:`ListSnapshotBackupsResp <listsnapshots__response_listsnapshotbackupsresp>` objects | Snapshot list |
   +-----------+---------------------------------------------------------------------------------------------------+---------------+

.. _listsnapshots__response_listsnapshotbackupsresp:

.. table:: **Table 3** ListSnapshotBackupsResp

   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | Parameter               | Type                                                                                                      | Description                                                                         |
   +=========================+===========================================================================================================+=====================================================================================+
   | created                 | String                                                                                                    | Snapshot creation time                                                              |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | datastore               | :ref:`ListSnapshotBackupsDatastoreResp <listsnapshots__response_listsnapshotbackupsdatastoreresp>` object | Search engine                                                                       |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | description             | String                                                                                                    | Snapshot description                                                                |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | id                      | String                                                                                                    | Snapshot ID                                                                         |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | clusterId               | String                                                                                                    | Cluster ID                                                                          |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | clusterName             | String                                                                                                    | Cluster name                                                                        |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | name                    | String                                                                                                    | Snapshot name                                                                       |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | status                  | String                                                                                                    | Snapshot status                                                                     |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | updated                 | String                                                                                                    | Time when the snapshot was updated. The format is **ISO8601: CCYY-MM-DDThh:mm:ss**. |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | backupType              | String                                                                                                    | Snapshot creation type. The options are as follows:                                 |
   |                         |                                                                                                           |                                                                                     |
   |                         |                                                                                                           | -  **0**: Automatic creation.                                                       |
   |                         |                                                                                                           |                                                                                     |
   |                         |                                                                                                           | -  **1**: Manual creation.                                                          |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | backupMethod            | String                                                                                                    | Snapshot creation mode                                                              |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | backupExpectedStartTime | String                                                                                                    | Snapshot start time                                                                 |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | backupKeepDay           | Integer                                                                                                   | Snapshot retention period                                                           |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | backupPeriod            | String                                                                                                    | Time when a snapshot is created every day                                           |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | indices                 | String                                                                                                    | Index you want to back up                                                           |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | totalShards             | Integer                                                                                                   | Total number of shards of the index you want to back up                             |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | failedShards            | Integer                                                                                                   | Number of shards that fail to be backed up                                          |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | version                 | String                                                                                                    | Snapshot version                                                                    |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | restoreStatus           | String                                                                                                    | Snapshot restoration status                                                         |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | startTime               | Long                                                                                                      | Snapshot start timestamp                                                            |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | endTime                 | Long                                                                                                      | Snapshot end timestamp                                                              |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+
   | bucketName              | String                                                                                                    | Name of the bucket that stores snapshot data                                        |
   +-------------------------+-----------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------+

.. _listsnapshots__response_listsnapshotbackupsdatastoreresp:

.. table:: **Table 4** ListSnapshotBackupsDatastoreResp

   +-----------+--------+-----------------------------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                                     |
   +===========+========+=================================================================================================================+
   | type      | String | Engine type. Currently, only Elasticsearch is supported.                                                        |
   +-----------+--------+-----------------------------------------------------------------------------------------------------------------+
   | version   | String | Elasticsearch engine version. For details, see the supported versions in :ref:`Before You Start <css_03_0001>`. |
   +-----------+--------+-----------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

None

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "backups" : [ {
       "created" : "2018-03-07T07:34:47",
       "datastore" : {
         "type" : "elasticsearch",
         "version" : "x.x.x"
       },
       "description" : "",
       "id" : "e29d99c1-3d19-4ea4-ae8d-f252df76cbe9",
       "clusterId" : "37cb1075-c38e-4cd8-81df-442d52df3786",
       "clusterName" : "Es-xfx",
       "name" : "snapshot-002",
       "status" : "COMPLETED",
       "updated" : "2018-03-07T07:40:12",
       "backupType" : "1",
       "backupMethod" : "manual",
       "backupExpectedStartTime" : null,
       "backupKeepDay" : null,
       "backupPeriod" : null,
       "indices" : ".kibanawebsite2",
       "totalShards" : 6,
       "failedShards" : 0,
       "version" : "x.x.x",
       "restoreStatus" : "success",
       "startTime" : 1520408087099,
       "endTime" : 1520408412219,
       "bucketName" : "obs-b8ed"
     }, {
       "created" : "2018-03-06T15:42:37",
       "datastore" : {
         "type" : "elasticsearch",
         "version" : "x.x.x"
       },
       "description" : "",
       "id" : "29a2254e-947f-4463-b65a-5f0b17515fae",
       "clusterId" : "37cb1075-c38e-4cd8-81df-442d52df3786",
       "clusterName" : "Es-xfx",
       "name" : "snapshot-001",
       "status" : "COMPLETED",
       "updated" : "2018-03-06T15:48:04",
       "backupType" : "1",
       "backupMethod" : "manual",
       "backupExpectedStartTime" : null,
       "backupKeepDay" : null,
       "backupPeriod" : null,
       "indices" : ".kibana",
       "totalShards" : 1,
       "failedShards" : 0,
       "version" : "x.x.x",
       "restoreStatus" : "none",
       "startTime" : 1520350957275,
       "endTime" : 1520351284357,
       "bucketName" : "obs-b8ed"
     } ]
   }

Status Codes
------------

+-------------+---------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                       |
+=============+===================================================================================================+
| 200         | Request succeeded.                                                                                |
+-------------+---------------------------------------------------------------------------------------------------+
| 406         | The server could not fulfill the request according to the content characteristics of the request. |
+-------------+---------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
