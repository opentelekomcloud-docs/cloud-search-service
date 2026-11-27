:original_name: RetryUpgradeTask.html

.. _RetryUpgradeTask:

Retrying or Terminating a Failed Upgrade or AZ Switchover Task
==============================================================

Function
--------

This API is used to retry the upgrade or AZ change of an Elasticsearch or OpenSearch cluster. The upgrade or AZ change may take a long time and may fail due to network issues. You can use this API to retry or stop a failed upgrade task.

Constraints
-----------

-  To call this API, the task status must be failed.

-  During a cross-version upgrade, if Task Status is Failed, you can terminate the upgrade task only if all nodes have not been upgraded.

-  During an AZ switchover, if Task Status is Failed, you can terminate the upgrade task only if none of the nodes has been switched.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/upgrade/{action_id}/retry

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                  |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                                           |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                                               |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | ID of the cluster for which you want to retry the failed task. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                                               |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | action_id       | Yes             | String          | **Definition**                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | ID of the task to be retried. For details, see :ref:`Obtaining Details About a Cluster Upgrade or AZ Switchover <upgradedetail>`.                                 |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | ID of the failed task, in UUID format.                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                                               |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                              |
   +=================+=================+=================+==========================================================================================================================================================+
   | retry_mode      | No              | String          | **Definition**                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | Retry mode. When **retry_mode** is set to **abort**, the upgrade task is terminated. When this parameter is not configured, the upgrade task is retried. |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | **Constraints**                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | Only **abort** is currently supported.                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | **Range**                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | **abort**: Terminate the upgrade task.                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | **Default Value**                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                          |
   |                 |                 |                 | If not configured, the upgrade task is retried by default.                                                                                               |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

-  Example request for retrying a cluster upgrade or AZ switchover task.

   .. code-block:: text

      PUT https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/bcdb711c-a7f0-4007-b8ee-9f13c05f8326/retry

-  Example request for terminating a cluster upgrade or AZ switchover task.

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
