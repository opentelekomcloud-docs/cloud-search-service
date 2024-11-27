:original_name: AddIndependentNode.html

.. _AddIndependentNode:

Adding Independent Masters and Clients
======================================

Function
--------

If you have not enabled the master or client node when creating a cluster, you can call this API to add one.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/type/{type}/independent

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | ID of the cluster that needs an independent master or client.                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | Node type. Its value can be:                                                                                                     |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                   |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+-----------------------------------------------------------------------------------+--------------------------------------+
   | Parameter | Mandatory | Type                                                                              | Description                          |
   +===========+===========+===================================================================================+======================================+
   | type      | Yes       | :ref:`IndependentTypeReq <addindependentnode__request_independenttypereq>` object | Master/Client request body parameter |
   +-----------+-----------+-----------------------------------------------------------------------------------+--------------------------------------+

.. _addindependentnode__request_independenttypereq:

.. table:: **Table 3** IndependentTypeReq

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================================================================+
   | flavor_ref      | Yes             | String          | Flavor ID. You can obtain the value of this parameter by calling the API for [Obtaining the Instance Specifications List] (ListFlavors.xml). Select the flavor ID suitable for your cluster version. |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | node_size       | Yes             | Integer         | Number of nodes.                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                      |
   |                 |                 |                 | -  If the node type is ess-master, the number of nodes must be an odd number in the range 3 to 10.                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                      |
   |                 |                 |                 | -  If the node type is ess-client, the number of nodes must be in the range 1 to 32.                                                                                                                 |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | volume_type     | Yes             | String          | Node storage type. Its value can be ULTRAHIGH, COMMON, or HIGH.                                                                                                                                      |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

Add independent master and client nodes.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/type/ess-client/independent

   {
     "type" : {
       "flavor_ref" : "d9dc06ae-b9c4-4ef4-acd8-953ef4205e27",
       "node_size" : 3,
       "volume_type" : "COMMON"
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

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                           |
+=============+=======================================================================================================================================================================+
| 200         | Request succeeded.                                                                                                                                                    |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403         | Request rejected.The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 500         | The server has received the request but could not understand it.                                                                                                      |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
