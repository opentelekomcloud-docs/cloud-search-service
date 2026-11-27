:original_name: AddIndependentNode.html

.. _AddIndependentNode:

Adding a Node Type
==================

Function
--------

This API is used to add dedicated master or client nodes or cold data nodes to an Elasticsearch or OpenSearch cluster that previously does not have such nodes. (When planning a cluster, you cannot always accurately predict future changes in data volumes. Add dedicated master or client nodes or cold data nodes is an effective way to scale up a cluster.)

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/type/{type}/independent

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Constraints**                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Range**                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                                                                |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Default Value**                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | ID of the cluster that requires dedicated master, client nodes, or cold data nodes. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Constraints**                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Range**                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Default Value**                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | **Definition**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | Types of dedicated nodes to add.                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Value range**:                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Default value**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================================================================================================================================================================+
   | flavor_ref      | Yes             | String          | **Definition**:                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | Flavor ID.                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | You can obtain the value of this parameter by calling the API for :ref:`Obtaining the Instance Specifications List <listflavors>`. Select the flavor ID suitable for your cluster version.                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | node_size       | Yes             | Integer         | **Definition**                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | Number of dedicated nodes.                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Constraints**                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  If the path parameter **type** is **ess-master**, dedicated master nodes are added. The number of nodes must be an odd number ranging from 3 to 9.                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  If the path parameter **type** is **ess-client**, dedicated client nodes are added. The number of nodes must range from 1 to 64.                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  If the path parameter **type** is **ess-cold**, dedicated cold data nodes are added. The number of nodes must range from 1 to 32. For two-AZ clusters, each AZ must contain at least two cold data nodes.                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | volume_type     | No              | String          | **Definition**:                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | Node storage type.                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | This parameter cannot be set when **flavor_ref** is set to a local disk flavor.                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  **HIGH**: high I/O                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  **ULTRAHIGH**: ultra-high I/O                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  **ESSD**: ultra-fast SSD                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | If **flavor_ref** is not set to a local disk flavor, the default value is ULTRAHIGH.                                                                                                                                                                                                        |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | volume_size     | No              | Integer         | **Definition**                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | Node storage size, in GB.                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |    For a new dedicated cold data node, a value greater than 100 GB is recommended.                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |    **Constraints**                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  This parameter cannot be set if **flavor_ref** specifies a local disk flavor.                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  The value must be greater than 0 and must be a multiple of both 4 and 10. Unit: GB.                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | The disk size can be obtained from the **diskrange** attribute in :ref:`Obtaining the Instance Specifications List <listflavors>`.                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | If **flavor_ref** does not specify a local disk flavor, for a new dedicated cold data node, the default value is the greater of 100 and the minimum disk capacity supported by the node flavor. For a new dedicated master or client node, the default size is 40 GB and cannot be changed. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
