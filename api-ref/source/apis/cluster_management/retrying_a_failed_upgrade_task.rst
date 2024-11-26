:original_name: RetryUpgradeTask.html

.. _RetryUpgradeTask:

Retrying a Failed Upgrade Task
==============================

Function
--------

The upgrade may fail due to network problems. In this case, you can call this API to retry.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/upgrade/{action_id}/retry

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to retry upgrade.                                                                                              |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | action_id  | Yes       | String | ID of the task to be retried.                                                                                                    |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +------------+-----------+--------+-----------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                 |
   +============+===========+========+=============================================================================+
   | retry_mode | No        | String | Impact of terminating the task. Currently, its value can only be **abort**. |
   +------------+-----------+--------+-----------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Example Requests
----------------

-  Example of an upgrade task retry request.

   .. code-block:: text

      PUT /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/bcdb711c-a7f0-4007-b8ee-9f13c05f8326/retry

-  Example of an upgrade task termination request.

   .. code-block:: text

      PUT /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/bcdb711c-a7f0-4007-b8ee-9f13c05f8326/retry?retry_mode=abort

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                     |
+===================================+=================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                |
|                                   |                                                                                                                                                                 |
|                                   | The client should not repeat the request without modifications.                                                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.                                                                                                                                               |
|                                   |                                                                                                                                                                 |
|                                   | The server has received the request and understood it, but the server refuses to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
