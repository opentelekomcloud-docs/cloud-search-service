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

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | domain_id  | Yes       | String | ID of the cluster you want to query.                                                                                             |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   ========== ================ ===================
   Parameter  Type             Description
   ========== ================ ===================
   topicsName Array of strings SMN topic name list
   ========== ================ ===================

Example Requests
----------------

Obtain the intelligent O&M task list and details.

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
         "suggestion" : "You are advised to change the cluster to a multi-AZ cluster. Procedure: On the CSS cluster console, choose **Clusters** > **Elasticsearch**. In the **Operation** column of a cluster, choose **More** > **Modify Configuration**. Click the **Change AZ** tab and add AZs. Click the **Scale Cluster** tab and change the number of nodes."
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
