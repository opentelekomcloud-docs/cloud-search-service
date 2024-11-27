:original_name: UpdateSnapshotSetting.html

.. _UpdateSnapshotSetting:

Modifying Basic Configurations of a Cluster Snapshot
====================================================

Function
--------

This API is used to modify the basic configurations for a cluster snapshot, including OBS buckets and IAM agency.

You can also use this API to enable the snapshot function.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/setting

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose snapshot basic configuration you want to modify.                                                         |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+--------+-------------------------------------------------+
   | Parameter | Mandatory | Type   | Description                                     |
   +===========+===========+========+=================================================+
   | bucket    | Yes       | String | Name of the OBS bucket used for backup.         |
   +-----------+-----------+--------+-------------------------------------------------+
   | agency    | Yes       | String | IAM agency used to access OBS.                  |
   +-----------+-----------+--------+-------------------------------------------------+
   | basePath  | No        | String | Storage path of the snapshot in the OBS bucket. |
   +-----------+-----------+--------+-------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Enable the snapshot function.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/index_snapshot/setting

   {
     "bucket" : "test-bucket",
     "agency" : "usearch",
     "basePath" : "css_repository/Es-name"
   }

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
| 412         | The server did not meet one of the preconditions contained in the request.                        |
+-------------+---------------------------------------------------------------------------------------------------+
| 504         | A gateway timeout error occurred.                                                                 |
+-------------+---------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
