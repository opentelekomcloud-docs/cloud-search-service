:original_name: RestartCluster.html

.. _RestartCluster:

Restarting a Cluster
====================

Function
--------

This API is used to restart a cluster. Services will be interrupted during the restart.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/restart

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to restart.                                                                                           |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Example Requests
----------------

None

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
