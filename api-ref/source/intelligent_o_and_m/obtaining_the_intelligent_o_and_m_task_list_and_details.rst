:original_name: css_03_0134.html

.. _css_03_0134:

Obtaining the Intelligent O&M Task List and Details
===================================================

Function
--------

This API is used to obtain the intelligent O&M task list and details.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ai-ops

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                         |
   +============+===========+========+=====================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be queried                                                                                     |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query parameter

   +-----------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type    | Description                                                                                                                                                          |
   +===========+===========+=========+======================================================================================================================================================================+
   | limit     | No        | Integer | Maximum number of records displayed on a page                                                                                                                        |
   +-----------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | start     | No        | Integer | Offset. All VPC endpoint services after this offset will be queried. The offset must be an integer greater than 0 but less than the number of VPC endpoint services. |
   +-----------+-----------+---------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameter

   +------------+-----------------------------------------------------------------------+-----------------------------------+
   | Parameter  | Type                                                                  | Description                       |
   +============+=======================================================================+===================================+
   | total_size | Integer                                                               | Number of cluster detection tasks |
   +------------+-----------------------------------------------------------------------+-----------------------------------+
   | aiops_list | Array of :ref:`aiops_list <css_03_0134__response_aiops_list>` objects | Detection task list               |
   +------------+-----------------------------------------------------------------------+-----------------------------------+

.. _css_03_0134__response_aiops_list:

.. table:: **Table 4** aiops_list

   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | Parameter             | Type                                                                        | Description                                |
   +=======================+=============================================================================+============================================+
   | id                    | String                                                                      | Detection task ID                          |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | name                  | String                                                                      | Detection task name                        |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | desc                  | String                                                                      | Detection task description                 |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | status                | Integer                                                                     | Task execution status.                     |
   |                       |                                                                             |                                            |
   |                       |                                                                             | -  **150**: The task is not executed.      |
   |                       |                                                                             | -  **200**: The task has been executed.    |
   |                       |                                                                             | -  **300**: The task has been sent.        |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | summary               | :ref:`summary <css_03_0134__response_summary>` object                       | Risk summary                               |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | create_time           | String                                                                      | Timestamp when a detection task is created |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | smn_status            | String                                                                      | Status of SMN alarm messages.              |
   |                       |                                                                             |                                            |
   |                       |                                                                             | -  **not_open**                            |
   |                       |                                                                             | -  **not_trigger**                         |
   |                       |                                                                             | -  **sent**                                |
   |                       |                                                                             | -  **send_fail**                           |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | smn_fail_reason       | String                                                                      | Cause of the message sending failure       |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+
   | task_risks            | Array of :ref:`AIOpsRiskInfo <css_03_0134__response_aiopsriskinfo>` objects | Risk item details                          |
   +-----------------------+-----------------------------------------------------------------------------+--------------------------------------------+

.. _css_03_0134__response_summary:

.. table:: **Table 5** summary

   ========== ======= ===========================
   Parameter  Type    Description
   ========== ======= ===========================
   high       Integer Number of high-risk items
   medium     Integer Number of medium-risk items
   suggestion Integer Number of suggestion items
   ========== ======= ===========================

.. _css_03_0134__response_aiopsriskinfo:

.. table:: **Table 6** AIOpsRiskInfo

   +-----------------------+-----------------------+---------------------------+
   | Parameter             | Type                  | Description               |
   +=======================+=======================+===========================+
   | riskType              | String                | Check item description    |
   +-----------------------+-----------------------+---------------------------+
   | level                 | String                | Severity.                 |
   |                       |                       |                           |
   |                       |                       | -  high                   |
   |                       |                       | -  medium                 |
   |                       |                       | -  suggestion             |
   +-----------------------+-----------------------+---------------------------+
   | desc                  | String                | Risk description          |
   +-----------------------+-----------------------+---------------------------+
   | suggestion            | String                | Suggestions for the risks |
   +-----------------------+-----------------------+---------------------------+

Request Example
---------------

Obtain the intelligent O&M task list and details.

.. code-block:: text

   GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops

Response Example
----------------

**Status code: 200**

Request sent.

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
         "riskType" : "Check whether the cluster has snapshot backup failures or no snapshot backup records in the last seven days."
         "level" : "suggestion",
         "desc" : "The cluster has no snapshot backup records in the last seven days."
         "suggestion" : "You are advised to enable the cluster snapshot function and ensure that snapshots generated in the last seven days are successfully backed up. If snapshot creation fails, click the cluster name, and check the failure details on the Cluster Snapshots and Logs pages."
       }, {
         "riskType" : "Check the number of nodes in the cluster and the number of AZs to evaluate the high availability of the distributed Elasticsearch cluster."
         "level" : "high",
         "desc" : "The current cluster has one or two nodes. If a node is faulty, the entire cluster may become unavailable. The service availability risk is high."
         "suggestion" : "You are advised to change the cluster to a multi-AZ cluster. Procedure: On the CSS cluster console, choose Clusters > Elasticsearch. In the Operation column of a cluster, choose More > Modify Configuration. Click the Change AZ tab and add AZs. Click the Scale Cluster tab and change the number of nodes.
       } ]
     } ],
     "total_size" : 1
   }

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                         |
+===================================+=====================================================================================================================================================================================+
| 200                               | Request sent.                                                                                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                    |
|                                   |                                                                                                                                                                                     |
|                                   | Modify the request instead of retrying.                                                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                                                                  |
|                                   |                                                                                                                                                                                     |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request fails to be processed because of the update of the conflict request. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

For details, see :ref:`Error Code <css_03_0076>`.
