:original_name: ListAiOps.html

.. _ListAiOps:

Obtaining the Intelligent O&M Task List and Details
===================================================

Function
--------

CSS provides intelligent O&M to check potential risks in clusters. After a scan task is completed, check the risks identified by the task, confirm and handle these risks in a timely manner based on risk handling suggestions. This API is used to obtain the intelligent O&M task list and details.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ai-ops

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Project ID of the account.                                                                                                              |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | ID of the cluster you want to query. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Cluster ID.                                                                                                                             |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================================+
   | limit           | No              | Integer         | **Definition**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Pagination parameter, indicating the maximum number of records on a page. The default value is 10, indicating that 10 tasks are queried at a time.                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | 1-1000                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | 10                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | offset          | No              | Integer         | **Definition**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Offset. All VPC endpoint services after this offset will be queried. The offset must be an integer greater than 0 but less than the number of VPC endpoint services. |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | 0-1000                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | 0                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+---------------------------------------------------------------------+-----------------------------------------+
   | Parameter             | Type                                                                | Description                             |
   +=======================+=====================================================================+=========================================+
   | total_size            | Integer                                                             | **Definition**:                         |
   |                       |                                                                     |                                         |
   |                       |                                                                     | Number of cluster risk detection tasks. |
   |                       |                                                                     |                                         |
   |                       |                                                                     | **Value range**:                        |
   |                       |                                                                     |                                         |
   |                       |                                                                     | 1-1000                                  |
   +-----------------------+---------------------------------------------------------------------+-----------------------------------------+
   | aiops_list            | Array of :ref:`aiops_list <listaiops__response_aiops_list>` objects | **Definition**:                         |
   |                       |                                                                     |                                         |
   |                       |                                                                     | Cluster risk detection task details.    |
   |                       |                                                                     |                                         |
   |                       |                                                                     | **Value range**:                        |
   |                       |                                                                     |                                         |
   |                       |                                                                     | N/A                                     |
   +-----------------------+---------------------------------------------------------------------+-----------------------------------------+

.. _listaiops__response_aiops_list:

.. table:: **Table 4** aiops_list

   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | Parameter             | Type                                                                      | Description                                                     |
   +=======================+===========================================================================+=================================================================+
   | id                    | String                                                                    | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | ID of a cluster risk detection task.                            |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | N/A                                                             |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | name                  | String                                                                    | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Name of a cluster risk detection task.                          |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | N/A                                                             |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | desc                  | String                                                                    | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Description of a cluster risk detection task.                   |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | N/A                                                             |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | status                | Integer                                                                   | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Task execution status.                                          |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | -  **150**: The function is disabled.                           |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | -  **200**: The function is enabled.                            |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | -  **300**: A message has been sent.                            |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | summary               | :ref:`summary <listaiops__response_summary>` object                       | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Cluster risk overview.                                          |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | N/A                                                             |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | create_time           | String                                                                    | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Time when a cluster risk detection task was created.            |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Format: Unix timestamp.                                         |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | smn_status            | String                                                                    | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Status of the task that sends cluster risk information via SMN. |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | -  **not_open**                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | -  **not_trigger**                                              |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | -  **sent**                                                     |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | -  **send_fail**                                                |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | smn_fail_reason       | String                                                                    | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Reason why cluster risk information failed to be sent via SMN.  |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | N/A                                                             |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+
   | task_risks            | Array of :ref:`AIOpsRiskInfo <listaiops__response_aiopsriskinfo>` objects | **Definition**:                                                 |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | Cluster risk details.                                           |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | **Value range**:                                                |
   |                       |                                                                           |                                                                 |
   |                       |                                                                           | N/A                                                             |
   +-----------------------+---------------------------------------------------------------------------+-----------------------------------------------------------------+

.. _listaiops__response_summary:

.. table:: **Table 5** summary

   +-----------------------+-----------------------+----------------------------------------------+
   | Parameter             | Type                  | Description                                  |
   +=======================+=======================+==============================================+
   | high                  | Integer               | **Definition**:                              |
   |                       |                       |                                              |
   |                       |                       | Number of high-risk items.                   |
   |                       |                       |                                              |
   |                       |                       | **Value range**:                             |
   |                       |                       |                                              |
   |                       |                       | 0-100                                        |
   +-----------------------+-----------------------+----------------------------------------------+
   | medium                | Integer               | **Definition**:                              |
   |                       |                       |                                              |
   |                       |                       | Number of medium-risk items.                 |
   |                       |                       |                                              |
   |                       |                       | **Value range**:                             |
   |                       |                       |                                              |
   |                       |                       | 0-100                                        |
   +-----------------------+-----------------------+----------------------------------------------+
   | suggestion            | Integer               | **Definition**:                              |
   |                       |                       |                                              |
   |                       |                       | Number of items that are just informational. |
   |                       |                       |                                              |
   |                       |                       | **Value range**:                             |
   |                       |                       |                                              |
   |                       |                       | 0-100                                        |
   +-----------------------+-----------------------+----------------------------------------------+

.. _listaiops__response_aiopsriskinfo:

.. table:: **Table 6** AIOpsRiskInfo

   +-----------------------+-----------------------+-----------------------------------------+
   | Parameter             | Type                  | Description                             |
   +=======================+=======================+=========================================+
   | riskType              | String                | **Definition**:                         |
   |                       |                       |                                         |
   |                       |                       | Cluster risk detection items.           |
   |                       |                       |                                         |
   |                       |                       | **Value range**:                        |
   |                       |                       |                                         |
   |                       |                       | N/A                                     |
   +-----------------------+-----------------------+-----------------------------------------+
   | level                 | String                | **Definition**:                         |
   |                       |                       |                                         |
   |                       |                       | Cluster risk level.                     |
   |                       |                       |                                         |
   |                       |                       | **Value range**:                        |
   |                       |                       |                                         |
   |                       |                       | -  high: high risk for the cluster.     |
   |                       |                       |                                         |
   |                       |                       | -  medium: medium risk for the cluster. |
   |                       |                       |                                         |
   |                       |                       | -  suggestion: suggestion.              |
   +-----------------------+-----------------------+-----------------------------------------+
   | desc                  | String                | **Definition**:                         |
   |                       |                       |                                         |
   |                       |                       | Cluster risk description.               |
   |                       |                       |                                         |
   |                       |                       | **Value range**:                        |
   |                       |                       |                                         |
   |                       |                       | N/A                                     |
   +-----------------------+-----------------------+-----------------------------------------+
   | suggestion            | String                | **Definition**:                         |
   |                       |                       |                                         |
   |                       |                       | Cluster risk handling suggestions.      |
   |                       |                       |                                         |
   |                       |                       | **Value range**:                        |
   |                       |                       |                                         |
   |                       |                       | N/A                                     |
   +-----------------------+-----------------------+-----------------------------------------+

Example Requests
----------------

This API is used to obtain the intelligent O&M task list and details.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops

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
       "task_risks" : [ {
         "riskType" : "Check for snapshot creation failures and snapshot records in the cluster in the last seven days.",
         "level" : "suggestion",
         "desc" : "There are no snapshot records in the cluster in the last seven days.",
         "suggestion" : "You are advised to enable cluster snapshot and ensure that snapshots are successfully created within seven days. If snapshot creation fails, click the cluster name, and check the failure details on the Cluster Snapshots and Logs pages."
       }, {
         "riskType" : "Check the number of nodes in a cluster and the number of AZs to evaluate the high availability status of a distributed Elasticsearch cluster.",
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
