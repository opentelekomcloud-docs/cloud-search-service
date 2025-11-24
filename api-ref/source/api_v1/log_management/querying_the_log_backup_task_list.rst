:original_name: ListLogsJob.html

.. _ListLogsJob:

Querying the Log Backup Task List
=================================

Function
--------

This API is used to query the log backup task list of a cluster. To be able to use this API, the target cluster must have log backup enabled, and log backup tasks were triggered earlier. This allows you to keep track of operations that were performed on the cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/logs/records

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Project ID of the account.                                                                                                              |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | ID of the cluster you want to query. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Cluster ID.                                                                                                                             |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================+
   | offset          | No              | Integer         | **Definition**:                                                                                                             |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | Start value for log query. The default value is 1, indicating that the query starts from the first log record.              |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                            |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                         |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                            |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | 1-1000                                                                                                                      |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                          |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | 1                                                                                                                           |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | **Definition**:                                                                                                             |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | Number of log records to be queried. The default value is 10, indicating that 10 log records are queried at a time.         |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                            |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                         |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                            |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | 1-1000                                                                                                                      |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                          |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | 10                                                                                                                          |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------+
   | status          | No              | String          | **Definition**:                                                                                                             |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | Status of the log tasks to be queried. If this parameter is not specified, all log task records of the cluster are queried. |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                            |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                         |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                            |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | -  **FAIL**: failed log tasks.                                                                                              |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | -  **NOT_FAIL**: ongoing or successful log tasks.                                                                           |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | -  If this parameter is not specified, all tasks are queried.                                                               |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                          |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | Empty string: Tasks of all states are queried.                                                                              |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------------------------------------------------------------------+-----------------------------------+
   | Parameter             | Type                                                                              | Description                       |
   +=======================+===================================================================================+===================================+
   | clusterLogRecord      | Array of :ref:`clusterLogRecord <listlogsjob__response_clusterlogrecord>` objects | **Parameter description**:        |
   |                       |                                                                                   |                                   |
   |                       |                                                                                   | List of cluster log backup tasks. |
   |                       |                                                                                   |                                   |
   |                       |                                                                                   | **Options**:                      |
   |                       |                                                                                   |                                   |
   |                       |                                                                                   | N/A                               |
   +-----------------------+-----------------------------------------------------------------------------------+-----------------------------------+

.. _listlogsjob__response_clusterlogrecord:

.. table:: **Table 4** clusterLogRecord

   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                |
   +=======================+=======================+============================================================================================+
   | id                    | String                | **Definition**:                                                                            |
   |                       |                       |                                                                                            |
   |                       |                       | Cluster log task ID, which is generated based on the system UUID.                          |
   |                       |                       |                                                                                            |
   |                       |                       | **Value range**:                                                                           |
   |                       |                       |                                                                                            |
   |                       |                       | N/A                                                                                        |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | clusterId             | String                | **Parameter description**:                                                                 |
   |                       |                       |                                                                                            |
   |                       |                       | Cluster ID.                                                                                |
   |                       |                       |                                                                                            |
   |                       |                       | **Options**:                                                                               |
   |                       |                       |                                                                                            |
   |                       |                       | N/A                                                                                        |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | createAt              | String                | **Definition**:                                                                            |
   |                       |                       |                                                                                            |
   |                       |                       | Cluster log creation time.                                                                 |
   |                       |                       |                                                                                            |
   |                       |                       | **Value range**:                                                                           |
   |                       |                       |                                                                                            |
   |                       |                       | Format: Unix timestamp.                                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | logPath               | String                | **Parameter description**:                                                                 |
   |                       |                       |                                                                                            |
   |                       |                       | Storage path of backed up logs in the OBS bucket.                                          |
   |                       |                       |                                                                                            |
   |                       |                       | **Options**:                                                                               |
   |                       |                       |                                                                                            |
   |                       |                       | N/A                                                                                        |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | status                | String                | **Definition**:                                                                            |
   |                       |                       |                                                                                            |
   |                       |                       | Cluster log task status.                                                                   |
   |                       |                       |                                                                                            |
   |                       |                       | **Value range**:                                                                           |
   |                       |                       |                                                                                            |
   |                       |                       | -  **RUNNING**: The backup is ongoing.                                                     |
   |                       |                       |                                                                                            |
   |                       |                       | -  **SUCCESS**: The backup is successful.                                                  |
   |                       |                       |                                                                                            |
   |                       |                       | -  **FAIL**: The backup failed.                                                            |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | finishedAt            | Long                  | **Definition**:                                                                            |
   |                       |                       |                                                                                            |
   |                       |                       | End time of cluster log creation. If it is still ongoing, the value is null.               |
   |                       |                       |                                                                                            |
   |                       |                       | **Value range**:                                                                           |
   |                       |                       |                                                                                            |
   |                       |                       | Format: Unix timestamp.                                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | jobTypes              | String                | **Definition**:                                                                            |
   |                       |                       |                                                                                            |
   |                       |                       | Type of a log creation task.                                                               |
   |                       |                       |                                                                                            |
   |                       |                       | **Value range**:                                                                           |
   |                       |                       |                                                                                            |
   |                       |                       | -  Manual: Manual backup.                                                                  |
   |                       |                       |                                                                                            |
   |                       |                       | -  Auto: Automatic backup.                                                                 |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | failedMsg             | String                | **Definition**:                                                                            |
   |                       |                       |                                                                                            |
   |                       |                       | Error returned for log creation. If the task status is not failed, this parameter is null. |
   |                       |                       |                                                                                            |
   |                       |                       | **Value range**:                                                                           |
   |                       |                       |                                                                                            |
   |                       |                       | N/A                                                                                        |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | jobId                 | String                | **Definition**:                                                                            |
   |                       |                       |                                                                                            |
   |                       |                       | ID of a log creation task.                                                                 |
   |                       |                       |                                                                                            |
   |                       |                       | **Value range**:                                                                           |
   |                       |                       |                                                                                            |
   |                       |                       | N/A                                                                                        |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------+

Example Requests
----------------

Querying the First 10 Log Backup Tasks

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/logs/records

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "clusterLogRecord" : [ {
       "id" : "d455a541-597e-4846-a6be-baad0ea361b1",
       "clusterId" : "4213d908-f5dc-4633-8401-cfd7175fca0c",
       "createAt" : 1656042837000,
       "logPath" : "css-backup-1610678043608/css/log",
       "status" : "RUNNING",
       "finishedAt" : null,
       "jobTypes" : "Manual",
       "failedMsg" : null,
       "jobId" : "2c9080df7c171342017c5e0884f8011c"
     } ]
   }

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
