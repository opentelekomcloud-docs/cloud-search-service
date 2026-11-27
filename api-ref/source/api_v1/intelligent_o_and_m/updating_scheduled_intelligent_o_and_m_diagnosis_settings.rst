:original_name: UpdateAiOpsSetting.html

.. _UpdateAiOpsSetting:

Updating Scheduled Intelligent O&M Diagnosis Settings
=====================================================

Function
--------

CSS provides scheduled diagnostic capabilities as part of intelligent O&M and supports daily diagnosis of potential cluster risks. This API is used to configure scheduled intelligent O&M diagnosis.

Applicable to Elasticsearch and OpenSearch engines.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/ai-ops/setting

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                  |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                           |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | Specifies the ID of the cluster to be updated. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | UUID format, 36 characters.                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                                                                                    |
   +=================+=================+==================+================================================================================================================+
   | check_type      | Yes             | String           | **Definition**:                                                                                                |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | Check type.                                                                                                    |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | **Constraints**:                                                                                               |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | N/A                                                                                                            |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | **Value range**:                                                                                               |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  full_detection: all check items.                                                                            |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  unavailability_detection: cluster unavailability check items.                                               |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  partial_detection: partial check items, select by setting check_items.                                      |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | **Default value**:                                                                                             |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | N/A                                                                                                            |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------+
   | check_items     | No              | Array of strings | **Definition**                                                                                                 |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | Select some detection items from all detection items for detection and input the detection item list.          |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **nodeDiskCheck**: Data node disk usage detection.                                                          |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **dataNodeDiskBalanceCheck**: Data node disk balance detection.                                             |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **largeShardBalanceCheck**: Large shard allocation balance detection.                                       |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **clusterNodeNumCheck**: Cluster node configuration detection.                                              |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **clusterHealthCheck**: Cluster health status detection.                                                    |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **maxShardPerNodeCheck**: Maximum shards per node detection.                                                |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **largeShardSizeCheck**: Oversized shard detection.                                                         |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **hotIndexCheck**: Hot index read/write detection (at 1-minute intervals).                                  |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **nodeLeftCheck**: Disconnected node detection.                                                             |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **httpConnectBalanceCheck**: Cluster node connection balance detection.                                     |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **sourceIPCheck**: Client connection detection (source IP analysis).                                        |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **cpuUsageCheck**: Node CPU usage detection (at 1-minute intervals).                                        |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **heapUsageCheck**: JVM heap memory usage detection (at 1-minute intervals).                                |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | -  **localDiskReplicasCheck**: Local disk cluster replica detection.                                           |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | **Constraints**                                                                                                |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | This parameter takes effect only when **check_type** is **partial_detection**.                                 |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------+
   | period          | Yes             | String           | **Definition**:                                                                                                |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | Intelligent O&M automatic check time, in the form of time followed by time zone, for example, 00:00 GMT+08:00. |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | **Constraints**:                                                                                               |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | N/A                                                                                                            |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | **Value range**:                                                                                               |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | N/A                                                                                                            |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | **Default value**:                                                                                             |
   |                 |                 |                  |                                                                                                                |
   |                 |                 |                  | N/A                                                                                                            |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Updating Scheduled Check Settings for Intelligent O&M

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops/setting

   {
     "check_type" : "full_detection",
     "check_items" : [ ],
     "period" : "11:30 GMT+08:00"
   }

Example Responses
-----------------

None

Status Codes
------------

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                                                                                             |
+=============+=========================================================================================================================================================================================================================================+
| 200         | Request succeeded.                                                                                                                                                                                                                      |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400         | Invalid request. Modify the request directly and do not attempt to retry it.                                                                                                                                                            |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409         | The request cannot be processed due to a conflict. This status code indicates that the resource that the client attempts to create already exists, or the request failed to be processed because of the update of the conflict request. |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412         | The server does not meet one of the preconditions that the client puts on the request.                                                                                                                                                  |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
