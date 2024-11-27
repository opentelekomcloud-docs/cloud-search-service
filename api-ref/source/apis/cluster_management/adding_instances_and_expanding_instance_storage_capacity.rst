:original_name: UpdateExtendInstanceStorage.html

.. _UpdateExtendInstanceStorage:

Adding Instances and Expanding Instance Storage Capacity
========================================================

Function
--------

This API is used to add instances of different types and expand instance storage capacity in a cluster. This API is available for clusters with master, client, or cold data nodes.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/role_extend

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

   +-----------+-----------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
   | Parameter | Mandatory | Type                                                                                               | Description                                               |
   +===========+===========+====================================================================================================+===========================================================+
   | grow      | Yes       | Array of :ref:`RoleExtendGrowReq <updateextendinstancestorage__request_roleextendgrowreq>` objects | Detailed description about the cluster scale-out request. |
   +-----------+-----------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

.. _updateextendinstancestorage__request_roleextendgrowreq:

.. table:: **Table 3** RoleExtendGrowReq

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================================================================================================================================================================================================================================================+
   | type            | Yes             | String          | Type of the instance to be scaled out. Select at least one from **ess**, **ess-master**, and **ess-client**. A type can be selected once only.                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | You can only add instances, rather than increase storage capacity, on nodes of the **ess-master** and **ess-client** types.                                                                                                                                                                                                                                                                            |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | nodesize        | Yes             | Integer         | Number of instances you want to add. The total number of existing instances and newly added instances in a cluster cannot exceed 32.                                                                                                                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | disksize        | Yes             | Integer         | Storage capacity of the instance you want to add. The sum of the original instance storage capacity plus the expanded instance storage capacity cannot exceed the default upper limit of storage capacity set during cluster creation. If scale-out is not required, set this parameter to 0. With a yearly/monthly cluster, you cannot change the number of nodes and disk capacity at the same time. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | Unit: GB.                                                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  The scale-out step of ESS and ESS-cold nodes is 20.                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  Storage capacity of ess-master and ess-client nodes cannot be expanded.                                                                                                                                                                                                                                                                                                                             |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 4** Response body parameters

   ========= ====== ===========
   Parameter Type   Description
   ========= ====== ===========
   id        String Cluster ID.
   ========= ====== ===========

Example Requests
----------------

Change the number of instances and storage capacity of the current cluster.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/role_extend

   {
     "grow" : [ {
       "type" : "ess-master",
       "nodesize" : 2,
       "disksize" : 0
     }, {
       "type" : "ess",
       "nodesize" : 0,
       "disksize" : 40
     }, {
       "type" : "ess-client",
       "nodesize" : 1,
       "disksize" : 0
     } ],
     "isAutoPay" : 1
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "id" : "4f3deec3-efa8-4598-bf91-560aad1377a3"
   }

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
