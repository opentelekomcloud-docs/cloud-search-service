:original_name: StartAutoSetting.html

.. _StartAutoSetting:

(Not Recommended) Automatically Setting Basic Configurations of a Cluster Snapshot
==================================================================================

Function
--------

This API is used to automatically set basic configurations for a cluster snapshot, including configuring OBS buckets and IAM agency.

-  **OBS Bucket**: Enter the location of the OBS bucket used for storing snapshots.

-  **Backup Path**: Enter the storage path of the snapshot in the OBS bucket.

-  **IAM Agency**: Authorize you to use OBS in IAM so that snapshots must be stored in OBS.

This API automatically creates an OBS bucket and an agency for the snapshot. If there are multiple clusters, an OBS bucket will be created for each cluster via this API. As a result, the OBS quota may be insufficient, and many OBS buckets are difficult to maintain. You are advised to perform the operations in :ref:`Modifying Basic Configurations of a Cluster Snapshot <updatesnapshotsetting>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/auto_setting

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster where snapshots you want to back up.                                                                           |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Example Requests
----------------

None

Example Responses
-----------------

None

Status Codes
------------

+-------------+---------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                       |
+=============+===================================================================================================+
| 200         | Request succeeded.                                                                                |
+-------------+---------------------------------------------------------------------------------------------------+
| 406         | The server could not fulfill the request according to the content characteristics of the request. |
+-------------+---------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
