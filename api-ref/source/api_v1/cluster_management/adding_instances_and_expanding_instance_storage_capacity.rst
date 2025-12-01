:original_name: UpdateExtendInstanceStorage.html

.. _UpdateExtendInstanceStorage:

Adding Instances and Expanding Instance Storage Capacity
========================================================

Function
--------

This API is used to add instances of different types and expand instance storage capacity in a cluster. This API is available for clusters with master, client, or cold data nodes.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/role_extend

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                             |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.            |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | Project ID of the account.                                                                                                                  |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                          |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                         |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                             |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | ID of the cluster you want to scale out. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | Cluster ID.                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                          |
   |                 |                 |                 |                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                         |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                                               | Description                                               |
   +=================+=================+====================================================================================================+===========================================================+
   | grow            | Yes             | Array of :ref:`RoleExtendGrowReq <updateextendinstancestorage__request_roleextendgrowreq>` objects | **Definition**:                                           |
   |                 |                 |                                                                                                    |                                                           |
   |                 |                 |                                                                                                    | Detailed description about the cluster scale-out request. |
   |                 |                 |                                                                                                    |                                                           |
   |                 |                 |                                                                                                    | **Constraints**:                                          |
   |                 |                 |                                                                                                    |                                                           |
   |                 |                 |                                                                                                    | N/A                                                       |
   |                 |                 |                                                                                                    |                                                           |
   |                 |                 |                                                                                                    | **Value range**:                                          |
   |                 |                 |                                                                                                    |                                                           |
   |                 |                 |                                                                                                    | N/A                                                       |
   |                 |                 |                                                                                                    |                                                           |
   |                 |                 |                                                                                                    | **Default value**:                                        |
   |                 |                 |                                                                                                    |                                                           |
   |                 |                 |                                                                                                    | N/A                                                       |
   +-----------------+-----------------+----------------------------------------------------------------------------------------------------+-----------------------------------------------------------+

.. _updateextendinstancestorage__request_roleextendgrowreq:

.. table:: **Table 3** RoleExtendGrowReq

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                              |
   +=================+=================+=================+==========================================================================================================================================================================================================================================================+
   | type            | Yes             | String          | **Definition**:                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | Type of the instance to be scaled out.                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | You can only add instances, rather than increase storage capacity, on nodes of the **ess-master** and **ess-client** types.                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **ess**: data node                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | You can select multiple node types, but cannot select the same node for different roles.                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                      |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | nodesize        | Yes             | Integer         | **Definition**:                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | Number of instances you want to add.                                                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | After scaling, the number of nodes of each type must meet the following requirements:                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  Data nodes: If the cluster does not have master nodes, the value ranges from 1 to 32. Otherwise, the value ranges from 1 to 200.                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  Master nodes: 3, 5, 7, or 9 (must be an odd number from 3 to 9)                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  Client nodes: 1 to 32.                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  Cold data nodes: 1 to 32.                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | See Constraints.                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                      |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | disksize        | Yes             | Integer         | **Definition**:                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | Storage capacity to be added, in GB                                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | The sum of the original instance storage capacity plus the expanded instance storage capacity cannot exceed the default upper limit of storage capacity set during cluster creation. If there is no need to add more instances, set this parameter to 0. |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  The scale-out step of ESS and ESS-cold nodes is 20.                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  Storage capacity of ess-master and ess-client nodes cannot be expanded.                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                      |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 4** Response body parameters

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | id                    | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Cluster ID.           |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+

Example Requests
----------------

Change the number of instances and storage capacity of the current cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/role_extend

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
     }, {
       "type" : "ess-cold",
       "nodesize" : 1,
       "disksize" : 0
     } ],
     "is_auto_pay" : 1
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
