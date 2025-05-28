:original_name: ListLogsJob.html

.. _ListLogsJob:

Querying the Log Backup Task List
=================================

Function
--------

This API is used to query the log backup task list of a cluster.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/logs/records

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | ID of the cluster you want to query.                                                                                                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================+
   | start           | No              | Integer         | **Parameter description**:                                                                                                  |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | The start value of the query. The default value is 1, indicating that the query starts from the first task.                 |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                            |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                         |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Options**:                                                                                                                |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | 1-1000                                                                                                                      |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                          |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | 1                                                                                                                           |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | **Parameter description**:                                                                                                  |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | Number of tasks to be queried. The default value is **10**, indicating that 10 tasks are queried at a time.                 |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                            |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                         |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Options**:                                                                                                                |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | 1-1000                                                                                                                      |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                          |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | 10                                                                                                                          |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------+
   | status          | No              | String          | **Parameter description**:                                                                                                  |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | Status of the log tasks to be queried. If this parameter is not specified, all log task records of the cluster are queried. |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | **Options**:                                                                                                                |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | -  **FAIL**: failed log tasks.                                                                                              |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | -  **NOT_FAIL**: ongoing or successful log tasks.                                                                           |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 | -  If this parameter is not specified, all tasks are queried.                                                               |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 |    **Default value**:                                                                                                       |
   |                 |                 |                 |                                                                                                                             |
   |                 |                 |                 |    Empty string: Tasks of all states are queried.                                                                           |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------------------------------------------------------------------+----------------------------+
   | Parameter             | Type                                                                              | Description                |
   +=======================+===================================================================================+============================+
   | clusterLogRecord      | Array of :ref:`clusterLogRecord <listlogsjob__response_clusterlogrecord>` objects | **Parameter description**: |
   |                       |                                                                                   |                            |
   |                       |                                                                                   | Cluster log entity object. |
   +-----------------------+-----------------------------------------------------------------------------------+----------------------------+

.. _listlogsjob__response_clusterlogrecord:

.. table:: **Table 4** clusterLogRecord

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                     |
   +=======================+=======================+=================================================================================================+
   | id                    | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Log task ID, which is generated based on the system UUID.                                       |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | clusterId             | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Cluster ID.                                                                                     |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | createAt              | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Creation time. Format: Unix timestamp.                                                          |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | logPath               | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Storage path of backed up logs in the OBS bucket.                                               |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | status                | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Task status.                                                                                    |
   |                       |                       |                                                                                                 |
   |                       |                       | **Options**:                                                                                    |
   |                       |                       |                                                                                                 |
   |                       |                       | -  **RUNNING**: The backup is ongoing.                                                          |
   |                       |                       |                                                                                                 |
   |                       |                       | -  **SUCCESS**: The backup is successful.                                                       |
   |                       |                       |                                                                                                 |
   |                       |                       | -  **FAIL**: The backup failed.                                                                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | finishedAt            | Long                  | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | End time. If the creation has not been completed, the end time is null. Format: Unix timestamp. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | jobTypes              | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Task type.                                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | **Options**:                                                                                    |
   |                       |                       |                                                                                                 |
   |                       |                       | -  **Manual**: Manual backup.                                                                   |
   |                       |                       |                                                                                                 |
   |                       |                       | -  **Auto**: Automatic backup.                                                                  |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | failedMsg             | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Error message. If the task is not failed, the value of this parameter is **null**.              |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | jobId                 | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Task ID.                                                                                        |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+

Example Requests
----------------

Querying the First 10 Log Backup Tasks

.. code-block:: text

   GET /v1.0/{project_id}/clusters/{cluster_id}/logs/records

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
