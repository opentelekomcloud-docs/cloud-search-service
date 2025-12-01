:original_name: StopLogs.html

.. _StopLogs:

Disabling the Log Backup or Collection Function
===============================================

Function
--------

This API is used to disable log backup or log ingestion for a cluster. Log backup and log ingestion can be disabled separately. After log backup is disabled, any automatic log backup policy configured earlier becomes invalid, and cluster logs cannot be manually back up to OBS either. Disabling log collection for a cluster stops the logs of that cluster from being collected and saved to a specified cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/logs/close

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                               |
   +=================+=================+=================+===========================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                          |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | **Constraints**:                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | **Value range**:                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | Project ID of the account.                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | **Default value**:                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                                       |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | ID of the cluster for which log backup or ingestion is to be disabled. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | **Constraints**:                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | **Value range**:                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | Cluster ID.                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | **Default value**:                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                                       |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================================================================================+
   | action          | No              | String          | **Definition**:                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                  |
   |                 |                 |                 | Disables log backup or log collection.                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                  |
   |                 |                 |                 | You can disable log backup or log ingestion only when they have been enabled for the cluster. For details about how to enable log backup or log ingestion, see :ref:`Enabling Logs <startlogs>`. |
   |                 |                 |                 |                                                                                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                  |
   |                 |                 |                 | -  base_log_collect: Disables log backup.                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                  |
   |                 |                 |                 | -  real_time_log_collect: Stops log collection.                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                  |
   |                 |                 |                 | base_log_collect                                                                                                                                                                                 |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

-  Disable log backup or log ingestion.

   .. code-block:: text

      PUT https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/logs/close?action=base_log_collect

-  .. code-block:: text

      PUT https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/logs/close?action=real_time_log_collect

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

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
