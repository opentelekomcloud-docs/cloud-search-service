:original_name: css_03_0088.html

.. _css_03_0088:

Scaling In a Cluster by Removing a Specific Node
================================================

Function
--------

This API is used to scale in a cluster by removing a specified node.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/node/offline

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to scale in.                                            |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-------------+-----------+------------------+---------------------------------------------------+
   | Parameter   | Mandatory | Type             | Description                                       |
   +=============+===========+==================+===================================================+
   | shrinkNodes | Yes       | Array of strings | ID of the node you want to remove from a cluster. |
   +-------------+-----------+------------------+---------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

.. code-block::

   {
     "shrinkNodes" : [ "2077bdf3-b90d-412e-b460-635b9b159c11" ]
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                        |
+===================================+====================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                   |
|                                   |                                                                                                                                    |
|                                   | Modify the request before retry.                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                       |
|                                   |                                                                                                                                    |
|                                   | The resource that the client attempts to create already exists, or the update request fails to be processed because of a conflict. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
