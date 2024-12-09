:original_name: css_03_0089.html

.. _css_03_0089:

Removing Nodes of a Specific Type
=================================

Function
--------

This API is used to remove instances of specific types and reduce instance storage capacity in a cluster.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/extend/{project_id}/clusters/{cluster_id}/role/shrink

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to scale in                                             |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------+-----------+----------------------------------------------------------------------------+-----------------------------------------------+
   | Parameter | Mandatory | Type                                                                       | Description                                   |
   +===========+===========+============================================================================+===============================================+
   | shrink    | Yes       | Array of :ref:`ShrinkNodeReq <css_03_0089__request_shrinknodereq>` objects | Type and quantity of nodes you want to remove |
   +-----------+-----------+----------------------------------------------------------------------------+-----------------------------------------------+

.. _css_03_0089__request_shrinknodereq:

.. table:: **Table 3** ShrinkNodeReq

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================================================================================================================================================================+
   | reducedNodeNum  | Yes             | Integer         | Number of nodes you want to remove.                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | - After the scale-in, there has to be at least one node in each AZ under each node type.                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | - In a cross-AZ cluster, the difference between the numbers of the same type nodes in different AZs cannot exceed 1.                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | - For a cluster with no Master nodes, the number of removed data nodes (including cold data nodes and other types of nodes) in a scale-in must be fewer than half of the original data node number, and the number of remaining data nodes after a scale-in must be greater than the maximum number of index replicas. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | - For a cluster with Master nodes, the number of removed master nodes in a scale-in must be fewer than half of the original master node number. After scale-in, there has to be an odd number of master nodes, and there has to be at least three of them.                                                             |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | Node type.                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  **ess**: data node                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  **ess-client**: Client node                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | -  **ess-master**: Master node                                                                                                                                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

.. code-block::

   {
     "shrink" : [ {
       "type" : "ess",
       "reducedNodeNum" : 1
     } ]
   }

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                         |
+===================================+=====================================================================================================================================================================================+
| 200                               | The request is processed.                                                                                                                                                           |
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
