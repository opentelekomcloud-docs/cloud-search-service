:original_name: UpgradeDetail.html

.. _UpgradeDetail:

Obtaining Upgrade Details
=========================

Function
--------

The upgrade takes a long time. You can call this API to check the upgrade progress on a node.

Calling Method
--------------

For details, see :ref:`Calling APIs <iam_01_0023>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/upgrade/detail

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                         |
   +============+===========+========+=====================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be upgraded.                                                                                   |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================================+
   | start           | No              | Integer         | Offset. All VPC endpoint services after this offset will be queried. The offset must be an integer greater than 0 but less than the number of VPC endpoint services. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | Maximum number of connections displayed on each page.                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | action_mode     | No              | String          | Upgrade querying behavior.                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | -  If you need to query the cluster version upgrade details, leave this parameter blank.                                                                             |
   |                 |                 |                 | -  If you need to query the details about AZ switchover, set this parameter to **AZ_MIGRATION**.                                                                     |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +------------+---------------------------------------------------------------------------------------------+--------------------------------------------------------------+
   | Parameter  | Type                                                                                        | Description                                                  |
   +============+=============================================================================================+==============================================================+
   | totalSize  | Integer                                                                                     | Number of times a request is delivered to the execution API. |
   +------------+---------------------------------------------------------------------------------------------+--------------------------------------------------------------+
   | detailList | Array of :ref:`GetUpgradeDetailInfo <upgradedetail__response_getupgradedetailinfo>` objects | Upgrade task details.                                        |
   +------------+---------------------------------------------------------------------------------------------+--------------------------------------------------------------+

.. _upgradedetail__response_getupgradedetailinfo:

.. table:: **Table 4** GetUpgradeDetailInfo

   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | Parameter             | Type                                                                                  | Description                                                                                        |
   +=======================+=======================================================================================+====================================================================================================+
   | id                    | String                                                                                | Task ID                                                                                            |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | startTime             | String                                                                                | Start time of the upgrade.                                                                         |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | endTime               | String                                                                                | End time of the upgrade.                                                                           |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | status                | String                                                                                | Task status. The value can be:                                                                     |
   |                       |                                                                                       |                                                                                                    |
   |                       |                                                                                       | -  **RUNNING**: The upgrade is in progress.                                                        |
   |                       |                                                                                       | -  **SUCCESS**: The upgrade is successful.                                                         |
   |                       |                                                                                       | -  **FAILED**: The upgrade failed.                                                                 |
   |                       |                                                                                       | -  **PARTIAL_FAILED**: The upgrade partially failed.                                               |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | agencyName            | String                                                                                | Agency name. You can create an agency to allow CSS to call other cloud services.                   |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | imageInfo             | :ref:`GetTargetImageIdDetail <upgradedetail__response_gettargetimageiddetail>` object | Image details.                                                                                     |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | totalNodes            | String                                                                                | Names of the nodes to be upgraded.                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | completedNodes        | String                                                                                | Names of the nodes that have been upgraded.                                                        |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | currentNodeName       | String                                                                                | Names of the nodes that are being upgraded.                                                        |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | executeTimes          | String                                                                                | Retried times                                                                                      |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | migrateParam          | String                                                                                | Current upgrade behavior of the cluster. The value is displayed if the **query** parameter exists. |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | finalAzInfoMap        | String                                                                                | Expected result of the cluster upgrade. The value is displayed if the **query** parameter exists.  |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+
   | currentNodeDetail     | Array of :ref:`CurrentNodeDetail <upgradedetail__response_currentnodedetail>` objects | Task details of the node that is being upgraded.                                                   |
   +-----------------------+---------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------+

.. _upgradedetail__response_gettargetimageiddetail:

.. table:: **Table 5** GetTargetImageIdDetail

   ================ ======= ======================================
   Parameter        Type    Description
   ================ ======= ======================================
   id               String  ID of an image that can be upgraded.
   displayName      String  Name of an image that can be upgraded.
   imageDesc        String  Image description.
   datastoreType    String  Image engine type.
   datastoreVersion String  Image engine version.
   priority         Integer Priority
   ================ ======= ======================================

.. _upgradedetail__response_currentnodedetail:

.. table:: **Table 6** CurrentNodeDetail

   ========= ======= ===================================
   Parameter Type    Description
   ========= ======= ===================================
   order     Integer Sequence number of an upgrade task.
   name      String  Upgrade task name.
   status    String  Status of the current task.
   desc      String  Description of the current task.
   beginTime String  Start time of the current task.
   endTime   String  End time of the current task.
   ========= ======= ===================================

Request Example
---------------

-  Example request for upgrading a cluster.

   .. code-block:: text

      GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/detail

-  Example request for upgrading a cluster.

   .. code-block:: text

      GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/detail?action_mode=AZ_MIGRATION

Response Example
----------------

**Status code: 200**

The request is processed.

-  Example response for upgrading a cluster image.

   .. code-block::

      {
        "totalSize" : 1,
        "detailList" : [ {
          "id" : "b7ac4c5b-3bda-4feb-a303-eb80f4bce986",
          "startTime" : "2023-01-05T02:23:39",
          "endTime" : "",
          "status" : "RUNNING",
          "agencyName" : "css_test_agency",
          "imageInfo" : {
            "id" : "439b5d30-5968-45df-b088-d030a858522d",
            "displayName" : "7.10.2_22.5.1_1230",
            "imageDesc" : "The latest image of version 7.10.2 will be officially released on December 30, 2022. the stability of the cluster has been optimized. It is recommended that you upgrade to this version.",
            "datastoreType" : "elasticsearch",
            "datastoreVersion" : "7.10.2",
            "priority" : 16
          },
          "totalNodes" : "css-test-ess-esn-1-1,css-test-ess-esn-2-1,css-test-ess-esn-3-1",
          "completedNodes" : "",
          "currentNodeName" : "css-test-ess-esn-1-1",
          "executeTimes" : "1",
          "currentNodeDetail" : [ {
            "order" : 0,
            "name" : "Data migration",
            "status" : "SUCCESS",
            "desc" : "Data is migrated from a node to other nodes in the cluster by running the exclude command.",
            "beginTime" : "2023-01-05T02:23:42",
            "endTime" : "2023-01-05T02:29:51"
          }, {
            "order" : 12,
            "name" : "Task status update",
            "status" : "WAITING",
            "desc" : "The cluster task status is refreshed. If there are no nodes to be replaced, the task is marked as completed. Otherwise, another node starts to be replaced.",
            "beginTime" : "",
            "endTime" : ""
          } ]
        } ]
      }

-  Example response for switching the AZ.

   .. code-block::

      {
        "totalSize" : 1,
        "detailList" : [ {
          "id" : "8ebe958b-b8c6-4939-b5a7-85aee9468888",
          "startTime" : "2022-12-29T08:32:29",
          "endTime" : "",
          "status" : "RUNNING",
          "agencyName" : "css_test_agency",
          "totalNodes" : "css-test-ess-esn-2-1,css-test-ess-esn-1-1,css-test-ess-esn-3-1",
          "completedNodes" : "css-test-ess-esn-2-1",
          "currentNodeName" : "css-test-ess-esn-1-1",
          "executeTimes" : "1",
          "migrateParam" : "{\"instType\":\"ess\",\"migrateType\":\"az_migrate\",\"sourceAz\":\"cn-north-4a\",\"targetAz\":\"cn-north-4c\"}",
          "finalAzInfoMap" : "{\"cn-north-4c\":\"css-test-ess-esn-2-1,css-test-ess-esn-1-1,css-test-ess-esn-3-1\"}",
          "currentNodeDetail" : [ {
            "order" : 0,
            "name" : "Data migration",
            "status" : "SUCCESS",
            "desc" : "Data is migrated from a node to other nodes in the cluster by running the exclude command.",
            "beginTime" : "2022-12-29T08:41:05",
            "endTime" : "2022-12-29T08:41:23"
          }, {
            "order" : 12,
            "name" : "Task status update",
            "status" : "RUNNING",
            "desc" : "The cluster task status is refreshed. If there are no nodes to be replaced, the task is marked as completed. Otherwise, another node starts to be replaced.",
            "beginTime" : "2023-01-04T06:53:42",
            "endTime" : ""
          } ]
        } ]
      }

Status Codes
------------

+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                            |
+=============+========================================================================================================================================================================+
| 200         | The request is processed.                                                                                                                                              |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400         | Invalid request. Modify the request directly and do not attempt to retry it.                                                                                           |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403         | The request is rejected. The server has received and understood the request, but refused to respond to it. Modify the request directly and do not attempt to retry it. |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

For details, see :ref:`Error Code <css_03_0076>`.
