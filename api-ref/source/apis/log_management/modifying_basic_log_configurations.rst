:original_name: UpdateLogSetting.html

.. _UpdateLogSetting:

Modifying Basic Log Configurations
==================================

Function
--------

This API is used to modify basic log configurations.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/logs/settings

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose basic log configurations you want to modify.                                                             |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type   | Description                                                                                                                                                                                                                                                                |
   +===========+===========+========+============================================================================================================================================================================================================================================================================+
   | action    | No        | String | The action can be base_log_collect or real_time_log_collect. base indicates the historical capability, and real_time indicates the real-time collection capability. If this parameter is not passed, base is used by default, which is compatible with the previous logic. |
   +-----------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 3** Request body parameters

   +-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter         | Mandatory | Type    | Description                                                                                                                                                   |
   +===================+===========+=========+===============================================================================================================================================================+
   | agency            | Yes       | String  | Agency name. You can create an agency to allow CSS to call other cloud services. This parameter is mandatory when action is not set to real_time_log_collect. |
   +-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | logBasePath       | Yes       | String  | Storage path of backed up logs in the OBS bucket. This parameter is mandatory when action is not set to real_time_log_collect.                                |
   +-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | logBucket         | Yes       | String  | Name of the OBS bucket for storing logs. This parameter is mandatory when action is not set to real_time_log_collect.                                         |
   +-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index_prefix      | No        | String  | Index prefix for storing logs. This parameter is mandatory when action is set to real_time_log_collect.                                                       |
   +-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | keep_days         | No        | Integer | Log retention duration. This parameter is mandatory when action is set to real_time_log_collect.                                                              |
   +-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | target_cluster_id | No        | String  | Specifies the target cluster for saving logs. This parameter is mandatory when action is set to real_time_log_collect.                                        |
   +-------------------+-----------+---------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

-  Modify basic log configurations.

   .. code-block:: text

      POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/logs/settings

      {
        "agency" : "css_obs_agency",
        "logBasePath" : "css/log",
        "logBucket" : "000-words"
      }

-  Updating the Real-Time Log Collection Configuration

   .. code-block:: text

      POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/logs/settings?action=real_time_log_collect

      {
        "index_prefix" : "css_log",
        "keep_days" : 30,
        "target_cluster_id" : "4f3deec3-efa8-4598-bf91-560aad1377a3",
      }

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
