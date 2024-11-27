:original_name: StopSnapshot.html

.. _StopSnapshot:

Disabling the Snapshot Function
===============================

Function
--------

This API is used to disable the snapshot function.

URI
---

DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose snapshot function you want to disable.                                                                   |
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

+-------------+---------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                       |
+=============+===================================================================================================+
| 200         | Request succeeded.                                                                                |
+-------------+---------------------------------------------------------------------------------------------------+
| 406         | The server could not fulfill the request according to the content characteristics of the request. |
+-------------+---------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
