:original_name: CreateAiOps.html

.. _CreateAiOps:

Creating a Cluster Diagnostic Task
==================================

Function
--------

This API is used to create a cluster diagnostic task.

It is available for Elasticsearch and OpenSearch.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/ai-ops

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Range**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                          |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default Value**                                                                                                                |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | ID of the target cluster. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.     |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Range**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                    |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default Value**                                                                                                                |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                             | Description                                                                                                                                                        |
   +=================+=================+==================================================+====================================================================================================================================================================+
   | check_type      | No              | String                                           | **Definition**                                                                                                                                                     |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | Detection scope for cluster diagnosis. Different diagnosis types apply to different fault troubleshooting scenarios.                                               |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Constraints**                                                                                                                                                    |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | When **check_type** is **partial_detection**, it must be used together with **check_items**.                                                                       |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Range**                                                                                                                                                          |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **full_detection**: All detection items.                                                                                                                        |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **unavailability_detection**: Cluster unavailable detection items for quick diagnosis of cluster unavailable scenarios.                                         |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **partial_detection**: Select some detection items from the full detection items for detection. The specific detection items need to be set in **check_items**. |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Default Value**                                                                                                                                                  |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | full_detection                                                                                                                                                     |
   +-----------------+-----------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | check_items     | No              | Array of strings                                 | **Definition**                                                                                                                                                     |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | Select some detection items from all detection items for detection, and input the detection item list. Each element in the array is a detection item:              |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **nodeDiskCheck**: Data node disk usage detection.                                                                                                              |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **dataNodeDiskBalanceCheck**: Data node disk balance detection.                                                                                                 |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **largeShardBalanceCheck**: Large shard allocation balance detection.                                                                                           |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **clusterNodeNumCheck**: Cluster node configuration detection.                                                                                                  |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **clusterHealthCheck**: Cluster health status detection.                                                                                                        |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **maxShardPerNodeCheck**: Maximum shards per node detection.                                                                                                    |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **largeShardSizeCheck**: Oversized shard detection.                                                                                                             |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **hotIndexCheck**: Hot index read/write detection (at 1-minute intervals).                                                                                      |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **nodeLeftCheck**: Disconnected node detection.                                                                                                                 |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **httpConnectBalanceCheck**: Cluster node connection balance detection.                                                                                         |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **sourceIPCheck**: Client connection detection (source IP analysis).                                                                                            |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **cpuUsageCheck**: Node CPU usage detection (at 1-minute intervals).                                                                                            |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **heapUsageCheck**: JVM heap memory usage detection (at 1-minute intervals).                                                                                    |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | -  **localDiskReplicasCheck**: Local disk cluster replica detection.                                                                                               |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Constraints**                                                                                                                                                    |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | This parameter takes effect only when **check_type** is **partial_detection**.                                                                                     |
   +-----------------+-----------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | name            | No              | String                                           | **Definition**                                                                                                                                                     |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | A custom detection report name.                                                                                                                                    |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Constraints**                                                                                                                                                    |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | N/A                                                                                                                                                                |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Range**                                                                                                                                                          |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | 4 to 64 characters. Only digits, letters, hyphens (-), and underscores (_) are allowed. The name must start with a letter.                                         |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Default Value**                                                                                                                                                  |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | N/A                                                                                                                                                                |
   +-----------------+-----------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | description     | No              | String                                           | **Definition**                                                                                                                                                     |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | A custom detection report description.                                                                                                                             |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Constraints**                                                                                                                                                    |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | N/A                                                                                                                                                                |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Range**                                                                                                                                                          |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | 0 to 255 characters.                                                                                                                                               |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Default Value**                                                                                                                                                  |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | N/A                                                                                                                                                                |
   +-----------------+-----------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | alarm           | No              | :ref:`alarm <createaiops__request_alarm>` object | **Definition**:                                                                                                                                                    |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | Check report sending. This function has been deprecated.                                                                                                           |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Constraints**:                                                                                                                                                   |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | N/A                                                                                                                                                                |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Value range**:                                                                                                                                                   |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | N/A                                                                                                                                                                |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | **Default value**:                                                                                                                                                 |
   |                 |                 |                                                  |                                                                                                                                                                    |
   |                 |                 |                                                  | N/A                                                                                                                                                                |
   +-----------------+-----------------+--------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _createaiops__request_alarm:

.. table:: **Table 3** alarm

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                |
   +=================+=================+=================+============================================================================+
   | level           | No              | String          | **Definition**:                                                            |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | Risk category of the report to be sent. This function has been deprecated. |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | **Constraints**:                                                           |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | N/A                                                                        |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | **Value range**:                                                           |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | N/A                                                                        |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | **Default value**:                                                         |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | N/A                                                                        |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------+
   | smn_topic       | No              | String          | **Definition**                                                             |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | Subject of the report to be sent. This function has been deprecated.       |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | **Constraints**                                                            |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | N/A                                                                        |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | **Range**                                                                  |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | N/A                                                                        |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | **Default Value**                                                          |
   |                 |                 |                 |                                                                            |
   |                 |                 |                 | N/A                                                                        |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

-  Create a cluster detection task.

   .. code-block:: text

      POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops

      {
        "check_type" : "partial_detection",
        "check_items" : [ "nodeDiskCheck" ]
      }

-  .. code-block:: text

      POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops

      {
        "check_type" : "full_detection",
        "check_items" : [ ]
      }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                      |
+===================================+==================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | Modify the request instead of retrying.                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | This status code indicates that the resource that the client attempts to create already exits, or the requested update failed due to a conflict. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
