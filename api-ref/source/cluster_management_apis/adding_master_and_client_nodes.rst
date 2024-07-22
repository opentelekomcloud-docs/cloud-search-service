:original_name: AddIndependentNode.html

.. _AddIndependentNode:

Adding Master and Client Nodes
==============================

Function
--------

This API is used to add master and client nodes to a cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0137>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/type/{type}/independent

.. table:: **Table 1** Path parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                         |
   +=================+=================+=================+=====================================================================================================================+
   | project_id      | Yes             | String          | Project ID. For details about how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | ID of the cluster that needs an independent master or client.                                                       |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | Node type. The value can be:                                                                                        |
   |                 |                 |                 |                                                                                                                     |
   |                 |                 |                 | -  **ess-master**: Master node                                                                                      |
   |                 |                 |                 | -  **ess-client**: Client node                                                                                      |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+-----------------------------------------------------------------------------------+--------------------------------------+
   | Parameter | Mandatory | Type                                                                              | Description                          |
   +===========+===========+===================================================================================+======================================+
   | type      | Yes       | :ref:`IndependentBodyReq <addindependentnode__request_independentbodyreq>` object | Master/Client request body parameter |
   +-----------+-----------+-----------------------------------------------------------------------------------+--------------------------------------+

.. _addindependentnode__request_independentbodyreq:

.. table:: **Table 3** IndependentBodyReq

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================================================================================+
   | flavor_ref      | Yes             | String          | Flavor ID. You can obtain the value of this parameter by calling the API :ref:`Obtaining the Instance Specifications List <listflavors>`. Select the flavor ID suitable for your cluster version. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | node_size       | Yes             | Integer         | Number of nodes.                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                   |
   |                 |                 |                 | -  If the node type is **ess-master**, the number of nodes must be an odd number in the range 3 to 10.                                                                                            |
   |                 |                 |                 | -  If the node type is **ess-client**, the number of nodes must be in the range 1 to 32.                                                                                                          |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | volume_type     | Yes             | String          | Node storage type. Its value can be **ULTRAHIGH**, **COMMON**, or **HIGH**.                                                                                                                       |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 4** Response body parameters

   ========= ====== ===========
   Parameter Type   Description
   ========= ====== ===========
   id        String Cluster ID.
   ========= ====== ===========

Request Example
---------------

Add the master and client nodes.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/type/ess-client/independent

   {
     "type" : {
       "flavor_ref" : "d9dc06ae-b9c4-4ef4-acd8-953ef4205e27",
       "node_size" : 3,
       "volume_type" : "COMMON"
     }
   }

Response Example
----------------

**Status code: 200**

The request is processed.

.. code-block::

   {
     "id" : "320afa24-ff2a-4f44-8460-6ba95e512ad4"
   }

Status Codes
------------

+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                            |
+=============+========================================================================================================================================================================+
| 200         | The request is processed.                                                                                                                                              |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403         | The request is rejected. The server has received and understood the request, but refused to respond to it. Modify the request directly and do not attempt to retry it. |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 500         | The server can be accessed by the request, but it cannot understand the user's request.                                                                                |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

For details, see :ref:`Error Code <css_03_0076>`.
