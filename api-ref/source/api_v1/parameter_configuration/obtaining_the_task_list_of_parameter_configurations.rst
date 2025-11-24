:original_name: ListYmlsJob.html

.. _ListYmlsJob:

Obtaining the Task List of Parameter Configurations
===================================================

Function
--------

This API is used to obtain the parameter configuration task list of a cluster. It can obtain the parameter configuration list ID, cluster ID, and parameter modification records. After a cluster is created, you can call this API to check the cluster parameter settings.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ymls/joblists

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

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                 |
   +=================+=================+=================+=============================================================================================================+
   | offset          | No              | Integer         | **Definition**:                                                                                             |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | The start value of the query. The default value is 1, indicating that the query starts from the first task. |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                            |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | N/A                                                                                                         |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                            |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | 1-1000                                                                                                      |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                          |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | 1                                                                                                           |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | **Parameter description**:                                                                                  |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | Number of tasks to be queried. The default value is **10**, indicating that 10 tasks are queried at a time. |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                            |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | N/A                                                                                                         |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | **Options**:                                                                                                |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | 1-1000                                                                                                      |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                          |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | 10                                                                                                          |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------------------------------------------------------------+-------------------------------------------+
   | Parameter             | Type                                                                        | Description                               |
   +=======================+=============================================================================+===========================================+
   | configList            | Array of :ref:`configListRsp <listymlsjob__response_configlistrsp>` objects | **Definition**:                           |
   |                       |                                                                             |                                           |
   |                       |                                                                             | List of historical configuration changes. |
   |                       |                                                                             |                                           |
   |                       |                                                                             | **Value range**:                          |
   |                       |                                                                             |                                           |
   |                       |                                                                             | N/A                                       |
   +-----------------------+-----------------------------------------------------------------------------+-------------------------------------------+

.. _listymlsjob__response_configlistrsp:

.. table:: **Table 4** configListRsp

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                            |
   +=======================+=======================+========================================================================================+
   | id                    | String                | **Definition**:                                                                        |
   |                       |                       |                                                                                        |
   |                       |                       | Configuration list ID.                                                                 |
   |                       |                       |                                                                                        |
   |                       |                       | **Value range**:                                                                       |
   |                       |                       |                                                                                        |
   |                       |                       | N/A                                                                                    |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------+
   | clusterId             | String                | **Definition**:                                                                        |
   |                       |                       |                                                                                        |
   |                       |                       | Cluster ID.                                                                            |
   |                       |                       |                                                                                        |
   |                       |                       | **Value range**:                                                                       |
   |                       |                       |                                                                                        |
   |                       |                       | N/A                                                                                    |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------+
   | createAt              | String                | **Definition**:                                                                        |
   |                       |                       |                                                                                        |
   |                       |                       | Configuration list creation time                                                       |
   |                       |                       |                                                                                        |
   |                       |                       | **Value range**:                                                                       |
   |                       |                       |                                                                                        |
   |                       |                       | Format: Unix timestamp.                                                                |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------+
   | status                | String                | **Definition**:                                                                        |
   |                       |                       |                                                                                        |
   |                       |                       | Cluster task execution status.                                                         |
   |                       |                       |                                                                                        |
   |                       |                       | **Value range**:                                                                       |
   |                       |                       |                                                                                        |
   |                       |                       | -  **success**: The task is successful.                                                |
   |                       |                       |                                                                                        |
   |                       |                       | -  **failed**: The task failed.                                                        |
   |                       |                       |                                                                                        |
   |                       |                       | -  **running**: The task is being executed.                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------+
   | finishedAt            | String                | **Definition**:                                                                        |
   |                       |                       |                                                                                        |
   |                       |                       | End time. If the creation has not been completed, the end time is null.                |
   |                       |                       |                                                                                        |
   |                       |                       | **Value range**:                                                                       |
   |                       |                       |                                                                                        |
   |                       |                       | Format: Unix timestamp.                                                                |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------+
   | modifyDeleteReset     | String                | **Definition**:                                                                        |
   |                       |                       |                                                                                        |
   |                       |                       | History of parameter setting modifications.                                            |
   |                       |                       |                                                                                        |
   |                       |                       | **Value range**:                                                                       |
   |                       |                       |                                                                                        |
   |                       |                       | N/A                                                                                    |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------+
   | failedMsg             | String                | **Definition**:                                                                        |
   |                       |                       |                                                                                        |
   |                       |                       | Returned error message. If the status is success, the value of this parameter is null. |
   |                       |                       |                                                                                        |
   |                       |                       | **Value range**:                                                                       |
   |                       |                       |                                                                                        |
   |                       |                       | N/A                                                                                    |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------+

Example Requests
----------------

Obtaining the Parameter Configuration Task List of a Cluster

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/ymls/joblists

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "configList" : [ {
       "id" : "7ed7258a-60a8-46fe-8814-52819d491b80",
       "clusterId" : "4213d908-f5dc-4633-8401-cfd7175fca0c",
       "createAt" : "1755745344000,",
       "status" : "success",
       "finishedAt" : "1755745355000,",
       "modifyDeleteReset" : "{\"modify\":{\"elasticsearch.yml\":{\"thread_pool.force_merge.size\":\"1\"}}}",
       "failedMsg" : ""
     } ]
   }

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                        |
+===================================+====================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                   |
|                                   |                                                                                                                                    |
|                                   | Modify the request before retry.                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                       |
|                                   |                                                                                                                                    |
|                                   | The resource that the client attempts to create already exists, or the update request fails to be processed because of a conflict. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
