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
   |                 |                 |                 | ID of the cluster where snapshots are to be automatically created.                                                                   |
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
   | keepday               | Integer               | **Parameter description**:                                        |
   |                       |                       |                                                                   |
   |                       |                       | Customize the number of snapshots to be retained.                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | period                | String                | **Parameter description**:                                        |
   |                       |                       |                                                                   |
   |                       |                       | Time when a snapshot is created every day.                        |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | prefix                | String                | **Parameter description**:                                        |
   |                       |                       |                                                                   |
   |                       |                       | Snapshot name prefix, which needs to be manually entered.         |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | bucket                | String                | **Parameter description**:                                        |
   |                       |                       |                                                                   |
   |                       |                       | Name of the OBS bucket where snapshots are stored.                |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | basePath              | String                | **Parameter description**:                                        |
   |                       |                       |                                                                   |
   |                       |                       | Storage path of the snapshot in the OBS bucket.                   |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | agency                | String                | **Parameter description**:                                        |
   |                       |                       |                                                                   |
   |                       |                       | Agency used to access OBS buckets.                                |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | enable                | String                | **Parameter description**:                                        |
   |                       |                       |                                                                   |
   |                       |                       | Whether to enable the automatic snapshot creation policy.         |
   |                       |                       |                                                                   |
   |                       |                       | **Options**:                                                      |
   |                       |                       |                                                                   |
   |                       |                       | -  **true**: The automatic snapshot creation policy is enabled.   |
   |                       |                       |                                                                   |
   |                       |                       | -  **false**: The automatic snapshot creation policy is disabled. |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | frequency             | String                | **Parameter description**:                                        |
   |                       |                       |                                                                   |
   |                       |                       | Frequency of automatically creating snapshots.                    |
   |                       |                       |                                                                   |
   |                       |                       | **Options**:                                                      |
   |                       |                       |                                                                   |
   |                       |                       | -  **DAY**: days.                                                 |
   |                       |                       |                                                                   |
   |                       |                       | -  **HOUR**: hours.                                               |
   |                       |                       |                                                                   |
   |                       |                       | -  **MON**: Monday.                                               |
   |                       |                       |                                                                   |
   |                       |                       | -  **TUE**: Tuesday.                                              |
   |                       |                       |                                                                   |
   |                       |                       | -  **WED**: Wednesday.                                            |
   |                       |                       |                                                                   |
   |                       |                       | -  **THU**: Thursday.                                             |
   |                       |                       |                                                                   |
   |                       |                       | -  **FRI**: Friday.                                               |
   |                       |                       |                                                                   |
   |                       |                       | -  **SAT**: Saturday.                                             |
   |                       |                       |                                                                   |
   |                       |                       | -  **SUN**: Sunday.                                               |
   +-----------------------+-----------------------+-------------------------------------------------------------------+

Example Requests
----------------

Query the automatic snapshot creation policy.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy

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
