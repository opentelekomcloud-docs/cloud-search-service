:original_name: UpdateExtendCluster.html

.. _UpdateExtendCluster:

Scaling Out a Cluster
=====================

Function
--------

This API is used to add instances to a cluster (only Elasticsearch instances can be added). This API can only scale out clusters that only have common nodes. Clusters with master, client, or cold data nodes cannot use this API.For details about how to configure the number and storage capacity of instances in a cluster, see the API for :ref:`Adding Instances and Expanding Instance Storage Capacity <updateextendinstancestorage>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/extend

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to scale out.                                                                                         |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+
   | Parameter | Mandatory | Type                                                                                   | Description                                               |
   +===========+===========+========================================================================================+===========================================================+
   | grow      | Yes       | :ref:`ExtendClusterGrowReq <updateextendcluster__request_extendclustergrowreq>` object | Detailed description about the cluster scale-out request. |
   +-----------+-----------+----------------------------------------------------------------------------------------+-----------------------------------------------------------+

.. _updateextendcluster__request_extendclustergrowreq:

.. table:: **Table 3** ExtendClusterGrowReq

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                     |
   +=================+=================+=================+=================================================================================================+
   | modifySize      | Yes             | Integer         | Number of instances you want to add.                                                            |
   |                 |                 |                 |                                                                                                 |
   |                 |                 |                 | The total number of existing instances and newly added instances in a cluster cannot exceed 32. |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Change the number of instances in the current cluster.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/extend

   {
     "grow" : {
       "modifySize" : 4
     },
     "isAutoPay" : 1
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+--------------------------------------------+
| Status Code                       | Description                                |
+===================================+============================================+
| 200                               | Request succeeded.                         |
+-----------------------------------+--------------------------------------------+
| 400                               | Invalid request.                           |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+
| 404                               | The requested resource could not be found. |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
