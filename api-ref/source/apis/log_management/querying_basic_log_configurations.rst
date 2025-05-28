:original_name: ShowGetLogSetting.html

.. _ShowGetLogSetting:

Querying Basic Log Configurations
=================================

Function
--------

This API is used to query basic cluster log configurations.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/logs/settings

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

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                   |
   +=================+=================+=================+===============================================================================================================================================================================================+
   | action          | No              | String          | **Parameter description**:                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                               |
   |                 |                 |                 | action can be **base_log_collect** or **real_time_log_collect**. **base_log_collect** indicates non-real-time log ingestion, and **real_time_log_collect** indicates real-time log ingestion. |
   |                 |                 |                 |                                                                                                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                               |
   |                 |                 |                 | **Options**:                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                               |
   |                 |                 |                 | -  **base_log_collect**: non-real-time log ingestion.                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                               |
   |                 |                 |                 | -  **real_time_log_collect**: real-time log ingestion.                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                               |
   |                 |                 |                 | base_log_collect                                                                                                                                                                              |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +--------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
   | Parameter                | Type                                                                              | Description                         |
   +==========================+===================================================================================+=====================================+
   | logConfiguration         | :ref:`logConfiguration <showgetlogsetting__response_logconfiguration>` object     | **Parameter description**:          |
   |                          |                                                                                   |                                     |
   |                          |                                                                                   | Log configuration entity object.    |
   +--------------------------+-----------------------------------------------------------------------------------+-------------------------------------+
   | realTimeLogCollectRecord | :ref:`realTimeLogCollect <showgetlogsetting__response_realtimelogcollect>` object | **Parameter description**:          |
   |                          |                                                                                   |                                     |
   |                          |                                                                                   | Configure real-time log collection. |
   +--------------------------+-----------------------------------------------------------------------------------+-------------------------------------+

.. _showgetlogsetting__response_logconfiguration:

.. table:: **Table 4** logConfiguration

   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                       |
   +=======================+=======================+===================================================================================================================================+
   | id                    | String                | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Log backup ID, which is generated using the system UUID.                                                                          |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | clusterId             | String                | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Cluster ID.                                                                                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | obsBucket             | String                | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Name of the OBS bucket for storing logs.                                                                                          |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | agency                | String                | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Agency name. You can create an agency to allow CSS to call other cloud services.                                                  |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | updateAt              | Long                  | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Update time. Format: Unix timestamp.                                                                                              |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | basePath              | String                | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Storage path of backed up logs in the OBS bucket.                                                                                 |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | autoEnable            | Boolean               | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Whether to enable automatic backup.                                                                                               |
   |                       |                       |                                                                                                                                   |
   |                       |                       | **Options**:                                                                                                                      |
   |                       |                       |                                                                                                                                   |
   |                       |                       | -  **true**: Automatic backup is enabled.                                                                                         |
   |                       |                       |                                                                                                                                   |
   |                       |                       | -  **false**: Automatic backup is disabled.                                                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | period                | String                | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Start time of automatic log backup. When **autoEnable** is set to **false**, the value of this parameter is **null**. Format: GMT |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | logSwitch             | Boolean               | **Parameter description**:                                                                                                        |
   |                       |                       |                                                                                                                                   |
   |                       |                       | Whether to enable the log function.                                                                                               |
   |                       |                       |                                                                                                                                   |
   |                       |                       | **Options**:                                                                                                                      |
   |                       |                       |                                                                                                                                   |
   |                       |                       | -  **true**: The log function is enabled.                                                                                         |
   |                       |                       |                                                                                                                                   |
   |                       |                       | -  **false**: The log function is disabled.                                                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------+

.. _showgetlogsetting__response_realtimelogcollect:

.. table:: **Table 5** realTimeLogCollect

   +-----------------------+-----------------------+--------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                  |
   +=======================+=======================+==============================================================+
   | id                    | String                | **Parameter description**:                                   |
   |                       |                       |                                                              |
   |                       |                       | Log collection ID, which is generated using the system UUID. |
   +-----------------------+-----------------------+--------------------------------------------------------------+
   | clusterId             | String                | **Parameter description**:                                   |
   |                       |                       |                                                              |
   |                       |                       | Cluster ID.                                                  |
   +-----------------------+-----------------------+--------------------------------------------------------------+
   | indexPrefix           | String                | **Parameter description**:                                   |
   |                       |                       |                                                              |
   |                       |                       | Prefix of the index for saving logs.                         |
   +-----------------------+-----------------------+--------------------------------------------------------------+
   | keepDays              | Integer               | **Parameter description**:                                   |
   |                       |                       |                                                              |
   |                       |                       | Log retention duration.                                      |
   +-----------------------+-----------------------+--------------------------------------------------------------+
   | targetClusterId       | String                | **Parameter description**:                                   |
   |                       |                       |                                                              |
   |                       |                       | ID of the target cluster where logs are saved.               |
   +-----------------------+-----------------------+--------------------------------------------------------------+
   | status                | String                | **Parameter description**:                                   |
   |                       |                       |                                                              |
   |                       |                       | Status of a real-time log collection task.                   |
   +-----------------------+-----------------------+--------------------------------------------------------------+
   | createAt              | Long                  | **Parameter description**:                                   |
   |                       |                       |                                                              |
   |                       |                       | Start time of a real-time log collection task.               |
   +-----------------------+-----------------------+--------------------------------------------------------------+
   | updateAt              | Long                  | **Parameter description**:                                   |
   |                       |                       |                                                              |
   |                       |                       | Update time of a real-time log collection task.              |
   +-----------------------+-----------------------+--------------------------------------------------------------+

Example Requests
----------------

Query basic cluster log configurations.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/{cluster_id}/logs/settings

Example Responses
-----------------

**Status code: 200**

Request succeeded.

-  Example response to a real-time log collection request.

   .. code-block::

      {
        "logConfiguration" : null,
        "realTimeLogCollectRecord" : {
          "id" : "17939b7b-5a93-4ca5-8d3c-b9f2d0e715b4",
          "clusterId" : "e3201ceb-1a3e-49f3-bb2f-23a816440b20",
          "keepDays" : 30,
          "updateAt" : 1717666418870,
          "createAt" : 1717666405897,
          "targetClusterId" : "8c19644b-f2ef-44fc-abef-230a4c578ce7",
          "indexPrefix" : "aaa",
          "status" : "200"
        }
      }

-  Example response to a log backup request.

   .. code-block::

      {
        "logConfiguration" : {
          "id" : "00032118-aff5-40e8-b19a-dd4bb576e572",
          "clusterId" : "e3201ceb-1a3e-49f3-bb2f-23a816440b20",
          "obsBucket" : "css-autobk-notdel-cn-north-7",
          "agency" : "css_obs_agency",
          "updateAt" : 1639624882000,
          "basePath" : "css/log",
          "autoEnable" : false,
          "period" : null,
          "logSwitch" : false
        },
        "realTimeLogCollectRecord" : null
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
