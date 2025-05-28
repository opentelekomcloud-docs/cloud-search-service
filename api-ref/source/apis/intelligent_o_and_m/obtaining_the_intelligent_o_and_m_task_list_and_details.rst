:original_name: ListAiOps.html

.. _ListAiOps:

Obtaining the Intelligent O&M Task List and Details
===================================================

Function
--------

This API is used to obtain the intelligent O&M task list and details.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ai-ops

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to query                                                                                              |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type    | Description                                                                                                                                                          |
   +===========+===========+=========+======================================================================================================================================================================+
   | limit     | No        | Integer | Pagination parameter, indicating the maximum number of records on a page.                                                                                            |
   +-----------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | start     | No        | Integer | Offset. All VPC endpoint services after this offset will be queried. The offset must be an integer greater than 0 but less than the number of VPC endpoint services. |
   +-----------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +------------+---------------------------------------------------------------------+-----------------------------+
   | Parameter  | Type                                                                | Description                 |
   +============+=====================================================================+=============================+
   | total_size | Integer                                                             | Number of detection tasks   |
   +------------+---------------------------------------------------------------------+-----------------------------+
   | aiops_list | Array of :ref:`aiops_list <listaiops__response_aiops_list>` objects | Detection task details list |
   +------------+---------------------------------------------------------------------+-----------------------------+

.. _listaiops__response_aiops_list:

.. table:: **Table 4** aiops_list

   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | Parameter             | Type                                                                      | Description                                   |
   +=======================+===========================================================================+===============================================+
   | id                    | String                                                                    | Detection task ID                             |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | name                  | String                                                                    | Detection task name                           |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | desc                  | String                                                                    | Detection task description                    |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | status                | Integer                                                                   | Task execution status.                        |
   |                       |                                                                           |                                               |
   |                       |                                                                           | -  **150**: The function is disabled.         |
   |                       |                                                                           |                                               |
   |                       |                                                                           | -  **200**: The function is enabled.          |
   |                       |                                                                           |                                               |
   |                       |                                                                           | -  **300**: A message has been sent.          |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | summary               | :ref:`summary <listaiops__response_summary>` object                       | Risk summary                                  |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | create_time           | String                                                                    | Timestamp when a detection task is created    |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | smn_status            | String                                                                    | Status of the SMN alarm message sending task. |
   |                       |                                                                           |                                               |
   |                       |                                                                           | -  **not_open**                               |
   |                       |                                                                           |                                               |
   |                       |                                                                           | -  **not_trigger**                            |
   |                       |                                                                           |                                               |
   |                       |                                                                           | -  **sent**                                   |
   |                       |                                                                           |                                               |
   |                       |                                                                           | -  **send_fail**                              |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | smn_fail_reason       | String                                                                    | Cause of the message sending failure          |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+
   | task_risks            | Array of :ref:`AIOpsRiskInfo <listaiops__response_aiopsriskinfo>` objects | Risk item details                             |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------+

.. _listaiops__response_summary:

.. table:: **Table 5** summary

   ========== ======= =====================================
   Parameter  Type    Description
   ========== ======= =====================================
   high       Integer Number of high-risk detection items
   medium     Integer Number of medium-risk detection items
   suggestion Integer Number of suggestion detection items
   ========== ======= =====================================

.. _listaiops__response_aiopsriskinfo:

.. table:: **Table 6** AIOpsRiskInfo

   +-----------------------+-----------------------+------------------------+
   | Parameter             | Type                  | Description            |
   +=======================+=======================+========================+
   | riskType              | String                | Check item description |
   +-----------------------+-----------------------+------------------------+
   | level                 | String                | Risk level.            |
   |                       |                       |                        |
   |                       |                       | -  **high**            |
   |                       |                       |                        |
   |                       |                       | -  **medium**          |
   |                       |                       |                        |
   |                       |                       | -  **suggestion**      |
   +-----------------------+-----------------------+------------------------+
   | desc                  | String                | Risk description       |
   +-----------------------+-----------------------+------------------------+
   | suggestion            | String                | Risk suggestion        |
   +-----------------------+-----------------------+------------------------+

Example Requests
----------------

This API is used to obtain the intelligent O&M task list and details.

.. code-block:: text

   GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "aiops_list" : [ {
       "id" : "7381a80b-68cb-4b9e-8226-37d686b18b1d",
       "name" : "aiops-test",
       "desc" : "",
       "status" : 200,
       "summary" : {
         "high" : 1,
         "medium" : 0,
         "suggestion" : 1
       },
       "create_time" : 1687944156750,
       "smn_status" : "not_open",
       "smn_fail_reason" : null,
       "task_risks" : [ {
         "riskType" : "Check for snapshot creation failures and snapshot records in the cluster in the last seven days.",
         "level" : "suggestion",
         "desc" : "There are no snapshot records in the cluster in the last seven days.",
         "suggestion" : "You are advised to enable cluster snapshot and ensure that snapshots are successfully created within seven days. If snapshot creation fails, click the cluster name, and check the failure details on the Cluster Snapshots and Logs pages."
       }, {
         "riskType" : "Check the number of nodes in the cluster and the number of AZs to evaluate the high availability status of the distributed Elasticsearch cluster.",
         "level" : "high",
         "desc" : "The current cluster has one or two nodes. If a node is faulty, the entire cluster may become unavailable. The service availability risk is high.",
         "suggestion" : "You are advised to change the cluster to a multi-AZ cluster. Procedure: On the CSS cluster console, choose Clusters > Elasticsearch. In the Operation column of a cluster, choose More > Modify Configuration. Click the Change AZ tab and add AZs. Click the Scale Cluster tab and change the number of nodes."
       } ]
     } ],
     "total_size" : 1
   }

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
