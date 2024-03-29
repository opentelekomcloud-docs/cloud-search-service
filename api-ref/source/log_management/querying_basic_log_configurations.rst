:original_name: css_03_0097.html

.. _css_03_0097:

Querying Basic Log Configurations
=================================

Function
--------

This API is used to query basic log configurations.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/logs/settings

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to query.                                               |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +------------------+-------------------------------------------------------------------------+----------------------------------+
   | Parameter        | Type                                                                    | Description                      |
   +==================+=========================================================================+==================================+
   | logConfiguration | :ref:`logConfiguration <css_03_0097__response_logconfiguration>` object | Log configuration entity object. |
   +------------------+-------------------------------------------------------------------------+----------------------------------+

.. _css_03_0097__response_logconfiguration:

.. table:: **Table 3** logConfiguration

   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                     |
   +=======================+=======================+=================================================================================================================================+
   | id                    | String                | Log backup ID, which is generated using the system UUID.                                                                        |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | clusterId             | String                | Cluster ID.                                                                                                                     |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | obsBucket             | String                | Name of the OBS bucket for storing logs.                                                                                        |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | agency                | String                | Agency name. You can create an agency to allow CSS to call other cloud services.                                                |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | updateAt              | Long                  | Update time. Format: Unix timestamp.                                                                                            |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | basePath              | String                | Storage path of backed up logs in the OBS bucket.                                                                               |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | autoEnable            | Boolean               | Whether the automatic backup is enabled.                                                                                        |
   |                       |                       |                                                                                                                                 |
   |                       |                       | -  **true**: Automatic backup is enabled.                                                                                       |
   |                       |                       | -  **false**: Automatic backup is disabled.                                                                                     |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | period                | String                | Start time of automatic log backup. If **autoEnable** is set to **false**, the value of this parameter is **null**. Format: GMT |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+
   | logSwitch             | Boolean               | Whether the log function is enabled.                                                                                            |
   |                       |                       |                                                                                                                                 |
   |                       |                       | -  **true**: The log function is enabled.                                                                                       |
   |                       |                       | -  **false**: The log function is disabled.                                                                                     |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

None

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "logConfiguration" : {
       "id" : "d455a541-597e-4846-a6be-baad0ea361b1",
       "clusterId" : "4213d908-f5dc-4633-8401-cfd7175fca0c",
       "obsBucket" : "css-auto-test",
       "agency" : "css_obs_agency",
       "updateAt" : 1633663681055,
       "basePath" : "css/log",
       "autoEnable" : false,
       "period" : "16:00 GMT+02:00",
       "logSwitch" : true
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
