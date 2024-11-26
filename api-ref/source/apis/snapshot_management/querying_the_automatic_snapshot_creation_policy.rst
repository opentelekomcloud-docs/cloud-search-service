:original_name: ShowAutoCreatePolicy.html

.. _ShowAutoCreatePolicy:

Querying the Automatic Snapshot Creation Policy
===============================================

Function
--------

This API is used to query the automatic snapshot creation policy.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster where snapshots are to be automatically created.                                                               |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                       |
   +=======================+=======================+===================================================================+
   | keepday               | Integer               | Customize the number of snapshots to be retained.                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | period                | String                | Time when a snapshot is created every day.                        |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | prefix                | String                | Snapshot name prefix, which needs to be manually entered.         |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | bucket                | String                | Name of the OBS bucket where snapshots are stored.                |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | basePath              | String                | Storage path of the snapshot in the OBS bucket.                   |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | agency                | String                | Agency used to access OBS buckets.                                |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | enable                | String                | Whether to enable the automatic snapshot creation policy.         |
   |                       |                       |                                                                   |
   |                       |                       | -  **true**: The automatic snapshot creation policy is enabled.   |
   |                       |                       |                                                                   |
   |                       |                       | -  **false**: The automatic snapshot creation policy is disabled. |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | frequency             | String                | Frequency of automatically creating snapshots.                    |
   +-----------------------+-----------------------+-------------------------------------------------------------------+

Example Requests
----------------

None

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "keepday" : 2,
     "frequency" : "DAY",
     "period" : "16:00 GMT+08:00",
     "prefix" : "snapshot",
     "bucket" : "es-backup",
     "basePath" : "css_repository/tests",
     "agency" : "usearch",
     "enable" : "true"
   }

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
