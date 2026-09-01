:original_name: AddIndependentNode.html

.. _AddIndependentNode:

Adding a Node Type
==================

Function
--------

This API is used to add dedicated master or client nodes or cold data nodes to an existing cluster that previously does not have such nodes. (When planning a cluster, you cannot always accurately predict future changes in data volumes. Add dedicated master or client nodes or cold data nodes is an effective way to scale up a cluster.)

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/type/{type}/independent

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                                        |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | Project ID of the account.                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | ID of the cluster that requires dedicated master or client nodes or cold data nodes. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | Cluster ID.                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | **Definition**:                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | Types of dedicated nodes to add.                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                              | Description                                                               |
   +=================+=================+===================================================================================+===========================================================================+
   | type            | Yes             | :ref:`IndependentTypeReq <addindependentnode__request_independenttypereq>` object | **Definition**:                                                           |
   |                 |                 |                                                                                   |                                                                           |
   |                 |                 |                                                                                   | Request body parameters for dedicated master, client, or cold data nodes. |
   |                 |                 |                                                                                   |                                                                           |
   |                 |                 |                                                                                   | **Constraints**:                                                          |
   |                 |                 |                                                                                   |                                                                           |
   |                 |                 |                                                                                   | N/A                                                                       |
   |                 |                 |                                                                                   |                                                                           |
   |                 |                 |                                                                                   | **Value range**:                                                          |
   |                 |                 |                                                                                   |                                                                           |
   |                 |                 |                                                                                   | N/A                                                                       |
   |                 |                 |                                                                                   |                                                                           |
   |                 |                 |                                                                                   | **Default value**:                                                        |
   |                 |                 |                                                                                   |                                                                           |
   |                 |                 |                                                                                   | N/A                                                                       |
   +-----------------+-----------------+-----------------------------------------------------------------------------------+---------------------------------------------------------------------------+

.. _addindependentnode__request_independenttypereq:

.. table:: **Table 3** IndependentTypeReq

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                              |
   +=================+=================+=================+==========================================================================================================================================================================================================================+
   | flavor_ref      | Yes             | String          | **Definition**:                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | Flavor ID.                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | You can obtain the value of this parameter by calling the API for :ref:`Obtaining the Instance Specifications List <listflavors>`. Select the flavor ID suitable for your cluster version.                               |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                                                                                                      |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | node_size       | Yes             | Integer         | **Definition**                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | Number of dedicated nodes.                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Constraints**                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  If the path parameter **type** is **ess-master**, which means dedicated master nodes are added, the number of nodes must be an odd number greater than or equal to 3 and less than or equal to 9.                     |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  If the path parameter **type** is **ess-client**, which means dedicated client nodes are added, the number of nodes must range from 1 to 64.                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  If the path parameter **type** is **ess-cold**, which means dedicated cold data nodes are added, the number of nodes must range from 1 to 32. For two-AZ clusters, each AZ must contain at least two cold data nodes. |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                                                                                                      |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | volume_type     | No              | String          | **Definition**:                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | Node storage type.                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | This parameter cannot be set when **flavor_ref** is set to a local disk flavor.                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **HIGH**: high I/O                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **ULTRAHIGH**: ultra-high I/O                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **ESSD**: ultra-fast SSD                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | If **flavor_ref** is not set to a local disk flavor, the default value is ULTRAHIGH.                                                                                                                                     |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | volume_size     | No              | Integer         | **Definition**:                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | Node storage capacity.                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  This parameter cannot be set when **flavor_ref** is set to a local disk flavor.                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  The value must be greater than 0 and a common multiple of 4 and 10, in GB.                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  Adding dedicated cold data nodes: 100 GB or the minimum disk capacity supported by the selected node flavor, whichever is larger.                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | -  Adding dedicated master or client nodes: The default size is 40 GB and cannot be changed.                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | You can obtain the disk size from the **diskrange** attribute in :ref:`Obtaining the Instance Specifications List <listflavors>`.                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | If **flavor_ref** is not set to a local disk flavor:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                          |
   |                 |                 |                 |    Adding dedicated cold data nodes: The disk size should be greater than 100 GB.                                                                                                                                        |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

Add dedicated master or client nodes or cold data nodes.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/type/ess-client/independent

   {
     "type" : {
       "flavor_ref" : "d9dc06ae-b9c4-4ef4-acd8-953ef4205e27",
       "node_size" : 3,
       "volume_type" : "COMMON",
       "volume_size" : 40
     }
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "id" : "320afa24-ff2a-4f44-8460-6ba95e512ad4"
   }

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                          |
+===================================+======================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.                                                                                                                                    |
|                                   |                                                                                                                                                      |
|                                   | The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 500                               | The server has received the request but could not understand it.                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
