:original_name: ListAiOps.html

.. _ListAiOps:

Querying the List and Details of Intelligent O&M Diagnostic Tasks
=================================================================

Function
--------

CSS provides intelligent O&M, where you can run intelligent cluster diagnostics to check potential risks in clusters. After a diagnostic task is completed, you can view the details of the identified risks and handle them promptly based on the recommendations. This API is used to obtain the list and details of intelligent O&M diagnostic tasks.

Applicable to Elasticsearch and OpenSearch engines.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ai-ops

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                         |
   +=================+=================+=================+=====================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Range**                                                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                             |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default Value**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | ID of the cluster to be queried. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Range**                                                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                       |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default Value**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================+
   | limit           | No              | Integer         | **Definition**                                                                                                                    |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | Maximum number of records displayed on a page. The default value is **10**, indicating that 10 tasks are queried at a time.       |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                               |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                         |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | 1-1000                                                                                                                            |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                 |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **10**                                                                                                                            |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | offset          | No              | Integer         | **Definition**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | Offset, which specifies the start value of the query. The default value is 0, indicating that the query starts from the 0th task. |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Constraints**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                               |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Value range**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | Greater than or equal to 0.                                                                                                       |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Default value**:                                                                                                                |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | 0                                                                                                                                 |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | report          | No              | String          | **Definition**                                                                                                                    |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | Obtain the latest report or a historical report.                                                                                  |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                               |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                         |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | -  **current**: Obtain only the latest diagnostic report.                                                                         |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | -  **history**: Obtain only historical diagnostic reports.                                                                        |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                 |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                               |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------------------------------------------+-------------------------------------------------------+
   | Parameter             | Type                                                      | Description                                           |
   +=======================+===========================================================+=======================================================+
   | total_size            | Integer                                                   | **Definition**                                        |
   |                       |                                                           |                                                       |
   |                       |                                                           | Total number of intelligent cluster diagnostic tasks. |
   |                       |                                                           |                                                       |
   |                       |                                                           | **Range**                                             |
   |                       |                                                           |                                                       |
   |                       |                                                           | N/A                                                   |
   +-----------------------+-----------------------------------------------------------+-------------------------------------------------------+
   | aiops_list            | Array of :ref:`AiOps <listaiops__response_aiops>` objects | **Definition**                                        |
   |                       |                                                           |                                                       |
   |                       |                                                           | Details of intelligent cluster diagnostic tasks.      |
   |                       |                                                           |                                                       |
   |                       |                                                           | **Range**                                             |
   |                       |                                                           |                                                       |
   |                       |                                                           | N/A                                                   |
   +-----------------------+-----------------------------------------------------------+-------------------------------------------------------+

.. _listaiops__response_aiops:

.. table:: **Table 4** AiOps

   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                                                                      | Description                                                                                                                  |
   +=======================+===========================================================================+==============================================================================================================================+
   | id                    | String                                                                    | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | ID of an intelligent cluster diagnostic task.                                                                                |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | N/A                                                                                                                          |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | check_type            | String                                                                    | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | Diagnosis type.                                                                                                              |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | -  **full_detection**: Full detection.                                                                                       |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | -  **unavailability_detection**: Cluster unavailability detection.                                                           |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | -  **partial_detection**: Partial detection.                                                                                 |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | trigger_type          | String                                                                    | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | Trigger type.                                                                                                                |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | -  **manual**                                                                                                                |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | -  **auto**                                                                                                                  |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | name                  | String                                                                    | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | Name of an intelligent cluster diagnostic task.                                                                              |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | N/A                                                                                                                          |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | desc                  | String                                                                    | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | Description of an intelligent cluster diagnostic task.                                                                       |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | N/A                                                                                                                          |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | status                | Integer                                                                   | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | Task execution status.                                                                                                       |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | -  **150**: disabled                                                                                                         |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | -  **200**: enabled                                                                                                          |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | -  **300**: sent                                                                                                             |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | summary               | :ref:`SummaryInfo <listaiops__response_summaryinfo>` object               | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | Cluster risk overview.                                                                                                       |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | N/A                                                                                                                          |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | create_time           | Integer                                                                   | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | Time when an intelligent cluster diagnostic task was created. The value is a Unix timestamp, for example, **1765457366399**. |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | N/A                                                                                                                          |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+
   | task_risks            | Array of :ref:`AIOpsRiskInfo <listaiops__response_aiopsriskinfo>` objects | **Definition**                                                                                                               |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | Cluster risk details.                                                                                                        |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | **Range**                                                                                                                    |
   |                       |                                                                           |                                                                                                                              |
   |                       |                                                                           | N/A                                                                                                                          |
   +-----------------------+---------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------+

.. _listaiops__response_summaryinfo:

.. table:: **Table 5** SummaryInfo

   +-----------------------+-----------------------+------------------------------+
   | Parameter             | Type                  | Description                  |
   +=======================+=======================+==============================+
   | highRisk              | Integer               | **Definition**               |
   |                       |                       |                              |
   |                       |                       | Number of high-risk items.   |
   |                       |                       |                              |
   |                       |                       | **Range**                    |
   |                       |                       |                              |
   |                       |                       | 0-100                        |
   +-----------------------+-----------------------+------------------------------+
   | mediumRisk            | Integer               | **Definition**               |
   |                       |                       |                              |
   |                       |                       | Number of medium-risk items. |
   |                       |                       |                              |
   |                       |                       | **Range**                    |
   |                       |                       |                              |
   |                       |                       | 0-100                        |
   +-----------------------+-----------------------+------------------------------+
   | normal                | Integer               | **Definition**               |
   |                       |                       |                              |
   |                       |                       | Number of normal items.      |
   |                       |                       |                              |
   |                       |                       | **Range**                    |
   |                       |                       |                              |
   |                       |                       | 0-100                        |
   +-----------------------+-----------------------+------------------------------+
   | suggestion            | Integer               | **Definition**               |
   |                       |                       |                              |
   |                       |                       | Number of warning items.     |
   |                       |                       |                              |
   |                       |                       | **Range**                    |
   |                       |                       |                              |
   |                       |                       | 0-100                        |
   +-----------------------+-----------------------+------------------------------+

.. _listaiops__response_aiopsriskinfo:

.. table:: **Table 6** AIOpsRiskInfo

   +-----------------------+-----------------------+--------------------------------+
   | Parameter             | Type                  | Description                    |
   +=======================+=======================+================================+
   | id                    | String                | **Definition**                 |
   |                       |                       |                                |
   |                       |                       | Check item ID                  |
   |                       |                       |                                |
   |                       |                       | **Range**                      |
   |                       |                       |                                |
   |                       |                       | N/A                            |
   +-----------------------+-----------------------+--------------------------------+
   | name                  | String                | **Definition**                 |
   |                       |                       |                                |
   |                       |                       | Check item name                |
   |                       |                       |                                |
   |                       |                       | **Range**                      |
   |                       |                       |                                |
   |                       |                       | N/A                            |
   +-----------------------+-----------------------+--------------------------------+
   | desc                  | String                | **Definition**                 |
   |                       |                       |                                |
   |                       |                       | Check item description         |
   |                       |                       |                                |
   |                       |                       | **Range**                      |
   |                       |                       |                                |
   |                       |                       | N/A                            |
   +-----------------------+-----------------------+--------------------------------+
   | level                 | String                | **Definition**                 |
   |                       |                       |                                |
   |                       |                       | Risk level of the check result |
   |                       |                       |                                |
   |                       |                       | **Range**                      |
   |                       |                       |                                |
   |                       |                       | -  **highRisk**                |
   |                       |                       |                                |
   |                       |                       | -  **mediumRisk**              |
   |                       |                       |                                |
   |                       |                       | -  **normal**                  |
   |                       |                       |                                |
   |                       |                       | -  **suggestion**              |
   +-----------------------+-----------------------+--------------------------------+
   | result                | String                | **Definition**                 |
   |                       |                       |                                |
   |                       |                       | Check result                   |
   |                       |                       |                                |
   |                       |                       | **Range**                      |
   |                       |                       |                                |
   |                       |                       | N/A                            |
   +-----------------------+-----------------------+--------------------------------+
   | suggestion            | String                | **Definition**                 |
   |                       |                       |                                |
   |                       |                       | Check suggestion               |
   |                       |                       |                                |
   |                       |                       | **Range**                      |
   |                       |                       |                                |
   |                       |                       | N/A                            |
   +-----------------------+-----------------------+--------------------------------+

Example Requests
----------------

This API is used to obtain the intelligent O&M task list and details.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops

Example Responses
-----------------

**Status code: 200**

.. code-block::

   {
     "total_size" : 1,
     "aiops_list" : [ {
       "id" : "id-id-id",
       "name" : "aiops-1765457366399",
       "desc" : null,
       "status" : 200,
       "summary" : {
         "highRisk" : 1,
         "mediumRisk" : 0,
         "normal" : 0,
         "suggestion" : 0
       },
       "trigger_type" : "manual",
       "check_type" : "partial_detection",
       "create_time" : 1765457366399,
       "task_risks" : [ {
         "id" : "nodeLeftCheck",
         "name" : "name",
         "desc" : "Check the connectivity of cluster nodes. Node disconnection will severely compromise cluster performance and therefore needs to be handled immediately.",
         "level" : "highRisk",
         "result" : "Check the connectivity of cluster nodes. Node disconnection will severely compromise cluster performance and therefore needs to be handled immediately.",
         "suggestion" : "Check the cluster's parameter settings.\nCheck and repair custom plug-ins.\nScale up data node specs or quantity"
       } ]
     } ]
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
