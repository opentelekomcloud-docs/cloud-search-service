:original_name: css_03_0108.html

.. _css_03_0108:

Disabling the Public Network Access Control Whitelist
=====================================================

Function
--------

This API is used to disable the public network access control whitelist.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/public/whitelist/close

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+--------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                          |
   +============+===========+========+======================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`.   |
   +------------+-----------+--------+--------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose public network access control whitelist you want to disable. |
   +------------+-----------+--------+--------------------------------------------------------------------------------------+

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
