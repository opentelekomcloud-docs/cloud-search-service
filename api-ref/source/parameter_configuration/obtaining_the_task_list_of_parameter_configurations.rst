:original_name: css_03_0117.html

.. _css_03_0117:

Obtaining the Task List of Parameter Configurations
===================================================

Function
--------

This API is used to obtain the parameter configuration task list of a cluster.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ymls/joblists

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to query.                                                                                             |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +------------+-----------------------------------------------------------------------------+------------------------------------------+
   | Parameter  | Type                                                                        | Description                              |
   +============+=============================================================================+==========================================+
   | configList | Array of :ref:`configListRsp <css_03_0117__response_configlistrsp>` objects | List of historical configuration changes |
   +------------+-----------------------------------------------------------------------------+------------------------------------------+

.. _css_03_0117__response_configlistrsp:

.. table:: **Table 3** configListRsp

   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                         |
   +=======================+=======================+=====================================================================================================+
   | id                    | String                | Operation ID.                                                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | clusterId             | String                | Cluster ID.                                                                                         |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | createAt              | String                | Creation time. Format: Unix timestamp.                                                              |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | status                | String                | Task execution status.                                                                              |
   |                       |                       |                                                                                                     |
   |                       |                       | -  **true**: The operation is successful.                                                           |
   |                       |                       | -  **false**: The execution failed.                                                                 |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | finishedAt            | String                | End time. If the creation has not been completed, the end time is **null**. Format: Unix timestamp. |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | modifyDeleteReset     | String                | History of parameter setting modifications.                                                         |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+
   | failedMsg             | String                | Returned error message. If the status is **success**, the value of this parameter is **null**.      |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------+

Example Requests
----------------

None

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "configList" : [ {
       "id" : "7ed7258a-60a8-46fe-8814-52819d491b80",
       "clusterId" : "4213d908-f5dc-4633-8401-cfd7175fca0c",
       "createAt" : 1633658735000,
       "status" : "success",
       "finishedAt" : null,
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
