:original_name: ShowGetLogSetting.html

.. _ShowGetLogSetting:

Querying Basic Log Configurations
=================================

Function
--------

This API is used to query the basic configuration of cluster log backup or real-time log collection. If the log backup or log collection function has been enabled in the cluster, you can use this API to query the basic configurations of log backup and log collection.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/logs/settings

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

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                        |
   +=================+=================+=================+====================================================================+
   | action          | No              | String          | **Parameter description**:                                         |
   |                 |                 |                 |                                                                    |
   |                 |                 |                 | Queries the log backup or log collection settings of a cluster.    |
   |                 |                 |                 |                                                                    |
   |                 |                 |                 | **Constraints**:                                                   |
   |                 |                 |                 |                                                                    |
   |                 |                 |                 | N/A                                                                |
   |                 |                 |                 |                                                                    |
   |                 |                 |                 | **Options**:                                                       |
   |                 |                 |                 |                                                                    |
   |                 |                 |                 | -  base_log_collect: Queries cluster log backup settings.          |
   |                 |                 |                 |                                                                    |
   |                 |                 |                 | -  real_time_log_collect: Queries cluster log collection settings. |
   |                 |                 |                 |                                                                    |
   |                 |                 |                 | **Default value**:                                                 |
   |                 |                 |                 |                                                                    |
   |                 |                 |                 | base_log_collect                                                   |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +--------------------------+-----------------------------------------------------------------------------------+----------------------------------------+
   | Parameter                | Type                                                                              | Description                            |
   +==========================+===================================================================================+========================================+
   | logConfiguration         | :ref:`logConfiguration <showgetlogsetting__response_logconfiguration>` object     | **Parameter description**:             |
   |                          |                                                                                   |                                        |
   |                          |                                                                                   | Log backup configuration.              |
   |                          |                                                                                   |                                        |
   |                          |                                                                                   | **Options**:                           |
   |                          |                                                                                   |                                        |
   |                          |                                                                                   | N/A                                    |
   +--------------------------+-----------------------------------------------------------------------------------+----------------------------------------+
   | realTimeLogCollectRecord | :ref:`realTimeLogCollect <showgetlogsetting__response_realtimelogcollect>` object | **Parameter description**:             |
   |                          |                                                                                   |                                        |
   |                          |                                                                                   | Real-time log ingestion configuration. |
   |                          |                                                                                   |                                        |
   |                          |                                                                                   | **Options**:                           |
   |                          |                                                                                   |                                        |
   |                          |                                                                                   | N/A                                    |
   +--------------------------+-----------------------------------------------------------------------------------+----------------------------------------+

.. _showgetlogsetting__response_logconfiguration:

.. table:: **Table 4** logConfiguration

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                              |
   +=======================+=======================+==========================================================================================================================================================+
   | id                    | String                | **Parameter description**:                                                                                                                               |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Log backup ID, which is generated using the system UUID.                                                                                                 |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Options**:                                                                                                                                             |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | N/A                                                                                                                                                      |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | clusterId             | String                | **Parameter description**:                                                                                                                               |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Cluster ID.                                                                                                                                              |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Options**:                                                                                                                                             |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | N/A                                                                                                                                                      |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | obsBucket             | String                | **Parameter description**:                                                                                                                               |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Name of the OBS bucket for storing logs.                                                                                                                 |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Options**:                                                                                                                                             |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | N/A                                                                                                                                                      |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | agency                | String                | **Definition**:                                                                                                                                          |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Agency name. You can create an agency to allow CSS to call other cloud services. An agency name cannot contain special characters or Chinese characters. |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Value range**:                                                                                                                                         |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Only a-z, A-Z, 0-9, hyphens (-) and underscores (_) are allowed.                                                                                         |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | updateAt              | Long                  | **Definition**:                                                                                                                                          |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Update time.                                                                                                                                             |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Value range**:                                                                                                                                         |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | The format is CCYY-MM-DDThh:mm:ss (ISO 8601).                                                                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | basePath              | String                | **Parameter description**:                                                                                                                               |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Storage path of backed up logs in the OBS bucket.                                                                                                        |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Options**:                                                                                                                                             |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | N/A                                                                                                                                                      |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | autoEnable            | Boolean               | **Definition**:                                                                                                                                          |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Whether to enable automatic backup.                                                                                                                      |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Value range**:                                                                                                                                         |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | -  true: Enable automatic backup.                                                                                                                        |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | -  false: Disable automatic backup.                                                                                                                      |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | period                | String                | **Definition**:                                                                                                                                          |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Start time of automatic log backup.                                                                                                                      |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Value range**:                                                                                                                                         |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Format: Greenwich Mean Time (GMT). When **autoEnable** is set to **false**, the value of this parameter is **null**.                                     |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | logSwitch             | Boolean               | **Definition**:                                                                                                                                          |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | Whether to enable logging.                                                                                                                               |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | **Value range**:                                                                                                                                         |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | -  true: Enable logging.                                                                                                                                 |
   |                       |                       |                                                                                                                                                          |
   |                       |                       | -  false: Disable logging.                                                                                                                               |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _showgetlogsetting__response_realtimelogcollect:

.. table:: **Table 5** realTimeLogCollect

   +-----------------------+-----------------------+----------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                    |
   +=======================+=======================+================================================================+
   | id                    | String                | **Parameter description**:                                     |
   |                       |                       |                                                                |
   |                       |                       | Log collection ID, which is generated using the system UUID.   |
   |                       |                       |                                                                |
   |                       |                       | **Options**:                                                   |
   |                       |                       |                                                                |
   |                       |                       | N/A                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | clusterId             | String                | **Definition**:                                                |
   |                       |                       |                                                                |
   |                       |                       | Cluster ID                                                     |
   |                       |                       |                                                                |
   |                       |                       | **Value range**:                                               |
   |                       |                       |                                                                |
   |                       |                       | N/A                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | indexPrefix           | String                | **Parameter description**:                                     |
   |                       |                       |                                                                |
   |                       |                       | Prefix of the index for saving logs.                           |
   |                       |                       |                                                                |
   |                       |                       | **Options**:                                                   |
   |                       |                       |                                                                |
   |                       |                       | N/A                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | keepDays              | Integer               | **Parameter description**:                                     |
   |                       |                       |                                                                |
   |                       |                       | Log retention duration.                                        |
   |                       |                       |                                                                |
   |                       |                       | **Options**:                                                   |
   |                       |                       |                                                                |
   |                       |                       | N/A                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | targetClusterId       | String                | **Parameter description**:                                     |
   |                       |                       |                                                                |
   |                       |                       | ID of the target cluster where logs are saved.                 |
   |                       |                       |                                                                |
   |                       |                       | **Options**:                                                   |
   |                       |                       |                                                                |
   |                       |                       | N/A                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | status                | String                | **Definition**:                                                |
   |                       |                       |                                                                |
   |                       |                       | Status of a real-time log ingestion task.                      |
   |                       |                       |                                                                |
   |                       |                       | **Value range**:                                               |
   |                       |                       |                                                                |
   |                       |                       | -  100: A real-time log ingestion task is being created.       |
   |                       |                       |                                                                |
   |                       |                       | -  150: Real-time log ingestion is available.                  |
   |                       |                       |                                                                |
   |                       |                       | -  200: The real-time log ingestion task is activated.         |
   |                       |                       |                                                                |
   |                       |                       | -  300: Real-time log ingestion failed.                        |
   |                       |                       |                                                                |
   |                       |                       | -  302: The real-time log ingestion task failed to be deleted. |
   |                       |                       |                                                                |
   |                       |                       | -  303: The real-time log ingestion task failed to be created. |
   |                       |                       |                                                                |
   |                       |                       | -  304: The real-time log ingestion task is being disabled.    |
   |                       |                       |                                                                |
   |                       |                       | -  400: The real-time log ingestion task is disabled.          |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | createAt              | Long                  | **Parameter description**:                                     |
   |                       |                       |                                                                |
   |                       |                       | Start time of a real-time log collection task.                 |
   |                       |                       |                                                                |
   |                       |                       | **Options**:                                                   |
   |                       |                       |                                                                |
   |                       |                       | N/A                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | updateAt              | Long                  | **Parameter description**:                                     |
   |                       |                       |                                                                |
   |                       |                       | Update time of a real-time log collection task.                |
   |                       |                       |                                                                |
   |                       |                       | **Options**:                                                   |
   |                       |                       |                                                                |
   |                       |                       | N/A                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------+

Example Requests
----------------

-  Query the cluster's log backup settings.

   .. code-block:: text

      GET https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/logs/settings?action=base_log_collect

-  Query the cluster's log ingestion settings.

   .. code-block:: text

      GET https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/logs/settings?action=real_time_log_collect

Example Responses
-----------------

**Status code: 200**

Request succeeded.

-  Example response to a request to query the cluster's log backup settings.

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

-  Example response to a request to query the cluster's log ingestion settings.

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
