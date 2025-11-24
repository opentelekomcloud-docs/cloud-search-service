:original_name: RetryUpgradeTask.html

.. _RetryUpgradeTask:

Retrying a Failed Upgrade Task
==============================

Function
--------

The upgrade may fail due to network problems. In this case, you can call this API to retry.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/upgrade/{action_id}/retry

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.       |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Constraints**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Value range**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | Project ID of the account.                                                                                                             |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Default value**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | ID of the cluster to retry upgrade. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Constraints**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Value range**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | Cluster ID.                                                                                                                            |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Default value**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | action_id       | Yes             | String          | **Definition**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | ID of the task to be retried.                                                                                                          |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Constraints**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Value range**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Default value**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                       |
   +=================+=================+=================+===================================================================+
   | retry_mode      | No              | String          | **Definition**:                                                   |
   |                 |                 |                 |                                                                   |
   |                 |                 |                 | If this parameter is not left blank, the task will be terminated. |
   |                 |                 |                 |                                                                   |
   |                 |                 |                 | **Constraints**:                                                  |
   |                 |                 |                 |                                                                   |
   |                 |                 |                 | Currently, its value can only be **abort**.                       |
   |                 |                 |                 |                                                                   |
   |                 |                 |                 | **Value range**:                                                  |
   |                 |                 |                 |                                                                   |
   |                 |                 |                 | abort: Abort the task.                                            |
   |                 |                 |                 |                                                                   |
   |                 |                 |                 | **Default value**:                                                |
   |                 |                 |                 |                                                                   |
   |                 |                 |                 | N/A                                                               |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

-  Example of an upgrade task retry request.

   .. code-block:: text

      PUT https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/bcdb711c-a7f0-4007-b8ee-9f13c05f8326/retry

-  Example of an upgrade task termination request.

   .. code-block:: text

      PUT https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/bcdb711c-a7f0-4007-b8ee-9f13c05f8326/retry?retry_mode=abort

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
