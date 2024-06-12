:original_name: css_03_0136.html

.. _css_03_0136:

Obtaining SMN Topics Available for Intelligent O&M Alarms
=========================================================

Function
--------

This API is used to obtain SMN topics available for intelligent O&M alarms.

URI
---

GET /v1.0/{project_id}/domains/{domain_id}/ai-ops/smn-topics

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                         |
   +============+===========+========+=====================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | domain_id  | Yes       | String | ID of the cluster to be queried                                                                                     |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameter

   ========== ================ ===================
   Parameter  Type             Description
   ========== ================ ===================
   topicsName Array of strings SMN topic name list
   ========== ================ ===================

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
         "riskType" : "Check whether the cluster has snapshot backup failures or no snapshot backup records in the last seven days.",
         "level" : "suggestion",
         "desc" : "The cluster has no snapshot backup records in the last seven days.",
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
