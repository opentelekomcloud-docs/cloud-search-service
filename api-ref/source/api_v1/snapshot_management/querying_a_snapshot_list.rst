:original_name: ListSnapshots.html

.. _ListSnapshots:

Querying a Snapshot List
========================

Function
--------

This API is used to query all snapshots of a cluster, including the snapshot creation time, data engine, snapshot ID, and snapshot status, helping you manage the lifecycle of cluster snapshots. This API enables you to quickly obtain the details of a specified snapshot, verify snapshot availability, and help you restore data, roll back versions, or analyze storage costs. This API also provides structured data support required for automatic monitoring and warning for the O&M team, significantly improving cluster O&M efficiency and stability.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | Project ID of the account.                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | ID of the cluster whose snapshots you want to query. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | Cluster ID.                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+---------------------------------------------------------------------------------------------------+-----------------------+
   | Parameter             | Type                                                                                              | Description           |
   +=======================+===================================================================================================+=======================+
   | backups               | Array of :ref:`ListSnapshotBackupsResp <listsnapshots__response_listsnapshotbackupsresp>` objects | **Definition**:       |
   |                       |                                                                                                   |                       |
   |                       |                                                                                                   | Snapshot list.        |
   |                       |                                                                                                   |                       |
   |                       |                                                                                                   | **Value range**:      |
   |                       |                                                                                                   |                       |
   |                       |                                                                                                   | N/A                   |
   +-----------------------+---------------------------------------------------------------------------------------------------+-----------------------+

.. _listsnapshots__response_listsnapshotbackupsresp:

.. table:: **Table 3** ListSnapshotBackupsResp

   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | Parameter             | Type                                                                                                      | Description                                              |
   +=======================+===========================================================================================================+==========================================================+
   | created               | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot creation time.                                  |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | The format is CCYY-MM-DDThh:mm:ss (ISO 8601).            |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | datastore             | :ref:`ListSnapshotBackupsDatastoreResp <listsnapshots__response_listsnapshotbackupsdatastoreresp>` object | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Search engine.                                           |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | description           | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot description.                                    |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | id                    | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot ID.                                             |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | clusterId             | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Cluster ID.                                              |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | clusterName           | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Cluster name.                                            |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | name                  | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot name.                                           |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | status                | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot status.                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  \**BUILDING": creating.                               |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **COMPLETED**: available.                             |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **FAILED**: unavailable.                              |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **PART_FAILED**: partially available.                 |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | backupType            | String                                                                                                    | **Parameter description**:                               |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot type.                                           |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Options**:                                             |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **0**: Automatic creation.                            |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **1**: Manual creation.                               |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | backupMethod          | String                                                                                                    | **Parameter description**:                               |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot creation mode.                                  |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Options**:                                             |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **auto**: automatic creation.                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **manual**: manual creation.                          |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | backupFrequency       | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Cluster snapshot creation frequency.                     |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **HOUR**                                              |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **DAY**                                               |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | indices               | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Index you want to back up.                               |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | totalShards           | Integer                                                                                                   | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Total number of shards of the index you want to back up. |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | failedShards          | Integer                                                                                                   | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Number of shards that fail to be backed up.              |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | restoreStatus         | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot restoration status.                             |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **restoring**: restoration in progress.               |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **success**: successful restoration.                  |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | -  **failed**: restoration failed.                       |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | startTime             | Long                                                                                                      | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot start timestamp.                                |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | endTime               | Long                                                                                                      | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Snapshot end timestamp.                                  |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+
   | bucketName            | String                                                                                                    | **Definition**:                                          |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | Name of the bucket that stores snapshot data.            |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | **Value range**:                                         |
   |                       |                                                                                                           |                                                          |
   |                       |                                                                                                           | N/A                                                      |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+----------------------------------------------------------+

.. _listsnapshots__response_listsnapshotbackupsdatastoreresp:

.. table:: **Table 4** ListSnapshotBackupsDatastoreResp

   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                     |
   +=======================+=======================+=================================================================================================================+
   | type                  | String                | **Definition**:                                                                                                 |
   |                       |                       |                                                                                                                 |
   |                       |                       | Cluster engine type.                                                                                            |
   |                       |                       |                                                                                                                 |
   |                       |                       | **Value range**:                                                                                                |
   |                       |                       |                                                                                                                 |
   |                       |                       | -  elasticsearch: Elasticsearch cluster.                                                                        |
   |                       |                       |                                                                                                                 |
   |                       |                       | -  openSearch: OpenSearch cluster.                                                                              |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------+
   | version               | String                | **Definition**:                                                                                                 |
   |                       |                       |                                                                                                                 |
   |                       |                       | Elasticsearch engine version. For details, see the supported versions in :ref:`Before You Start <css_03_0001>`. |
   |                       |                       |                                                                                                                 |
   |                       |                       | **Value range**:                                                                                                |
   |                       |                       |                                                                                                                 |
   |                       |                       | N/A                                                                                                             |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

Query the cluster snapshot list.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/37cb1075-c38e-4cd8-81df-442d52df3786/index_snapshots

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
       "backupFrequency" : "HOUR",
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
