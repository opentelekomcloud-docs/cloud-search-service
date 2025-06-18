:original_name: StopAutoCreateSnapshots.html

.. _StopAutoCreateSnapshots:

Disabling Automatic Snapshot Creation
=====================================

Function
--------

This API is used to disable the automatic snapshot creation function.

URI
---

PUT /v2.0/{project_id}/clusters/{cluster_id}/snapshots/policy/close

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that the snapshot belongs to.                                                                                  |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Example Requests
----------------

Disable the automatic backup function.

.. code-block:: text

   PUT /v2.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/snapshots/policy/close

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                           |
+===================================+=======================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                      |
|                                   |                                                                                                                                                                       |
|                                   | Modify the request before retry.                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
