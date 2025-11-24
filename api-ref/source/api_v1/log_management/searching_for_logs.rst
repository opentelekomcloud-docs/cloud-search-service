:original_name: ShowLogBackup.html

.. _ShowLogBackup:

Searching for Logs
==================

Function
--------

CSS supports log backup and query, helping you efficiently locate issues. You can periodically back up cluster logs to OBS buckets for long-term storage, from which you download log data for troubleshooting or auditing purposes. You can also query cluster logs through an API. You can search for specific run logs by specifying a time period, node names, and log levels. This helps you quickly locate faults or performance bottlenecks. This API is used to query cluster logs by specifying the node name, log level, and log type.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/logs/search

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

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                     |
   +=================+=================+=================+=================================================================================================================================================================+
   | instance_name   | Yes             | String          | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Node name. Obtain the **name** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`.                                      |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | level           | No              | String          | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Queried log level.                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  DEBUG: Queries DEBUG logs.                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  INFO: Queries INFO logs.                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  WARN: Queries WARN logs.                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  ERROR: Queries ERROR logs.                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  ALL: Queries logs of all levels.                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | .. note::                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 |    If multiple log levels are required, separate them with vertical bars (|), for example, WARN|ERROR.                                                          |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | ALL                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | log_type        | Yes             | String          | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Queried log type.                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  deprecation: Queries deprecation logs. (Deprecation operation logs can be queried only when all log levels are selected.)                                    |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  indexingSlow: Queries slow indexing logs.                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  searchSlow: Queries slow query logs.                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | -  instance: Queries run logs.                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Number of log records returned. By default, 100 log records are returned. A maximum of 10,000 log records can be returned, and the log size cannot exceed 1 MB. |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | 1-10000                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | 100                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | time_index      | No              | String          | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Returns logs generated before a specified time.                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | The time format is yyyy-MM-ddTHH:mm:ss,SSS.                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | keyword         | No              | String          | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Keyword used for filtering.                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Only letters, digits, underscores (_), hyphens (-), periods (.), spaces, and square brackets are allowed. Maximum length: 64 characters.                        |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-------------------------------------------------------------------+----------------------------------------------+
   | Parameter             | Type                                                              | Description                                  |
   +=======================+===================================================================+==============================================+
   | logList               | Array of :ref:`logList <showlogbackup__response_loglist>` objects | **Parameter description**:                   |
   |                       |                                                                   |                                              |
   |                       |                                                                   | Log list.                                    |
   |                       |                                                                   |                                              |
   |                       |                                                                   | **Options**:                                 |
   |                       |                                                                   |                                              |
   |                       |                                                                   | N/A                                          |
   +-----------------------+-------------------------------------------------------------------+----------------------------------------------+
   | type                  | String                                                            | **Definition**:                              |
   |                       |                                                                   |                                              |
   |                       |                                                                   | Queried log type.                            |
   |                       |                                                                   |                                              |
   |                       |                                                                   | **Value range**:                             |
   |                       |                                                                   |                                              |
   |                       |                                                                   | -  deprecation: Queries deprecation logs.    |
   |                       |                                                                   |                                              |
   |                       |                                                                   | -  indexingSlow: Queries slow indexing logs. |
   |                       |                                                                   |                                              |
   |                       |                                                                   | -  searchSlow: Queries slow query logs.      |
   |                       |                                                                   |                                              |
   |                       |                                                                   | -  instance: Queries run logs.               |
   +-----------------------+-------------------------------------------------------------------+----------------------------------------------+

.. _showlogbackup__response_loglist:

.. table:: **Table 4** logList

   +-----------------------+-----------------------+-------------------------------+
   | Parameter             | Type                  | Description                   |
   +=======================+=======================+===============================+
   | content               | String                | **Parameter description**:    |
   |                       |                       |                               |
   |                       |                       | Log content.                  |
   |                       |                       |                               |
   |                       |                       | **Options**:                  |
   |                       |                       |                               |
   |                       |                       | N/A                           |
   +-----------------------+-----------------------+-------------------------------+
   | date                  | String                | **Definition**:               |
   |                       |                       |                               |
   |                       |                       | Date                          |
   |                       |                       |                               |
   |                       |                       | **Value range**:              |
   |                       |                       |                               |
   |                       |                       | N/A                           |
   +-----------------------+-----------------------+-------------------------------+
   | level                 | String                | **Definition**:               |
   |                       |                       |                               |
   |                       |                       | Queried log level.            |
   |                       |                       |                               |
   |                       |                       | **Value range**:              |
   |                       |                       |                               |
   |                       |                       | -  DEBUG: Queries DEBUG logs. |
   |                       |                       |                               |
   |                       |                       | -  INFO: Queries INFO logs.   |
   |                       |                       |                               |
   |                       |                       | -  WARN: Queries WARN logs.   |
   |                       |                       |                               |
   |                       |                       | -  ERROR: Queries ERROR logs. |
   +-----------------------+-----------------------+-------------------------------+

Example Requests
----------------

Query logs by node name, log level, and log type.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/logs/search

   {
     "instance_name" : "css-4312-ess-esn-1-1",
     "level" : "INFO",
     "log_type" : "instance",
     "limit" : 10,
     "time_index" : "2025-08-25T01:07:19,082",
     "keyword" : "received"
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "logList" : [ {
       "content" : "xxxxxx",
       "date" : "2021-10-08T03:55:54,718",
       "level" : "INFO"
     } ],
     "type" : "instance"
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
