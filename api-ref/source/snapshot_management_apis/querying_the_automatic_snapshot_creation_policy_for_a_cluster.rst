:original_name: css_03_0032.html

.. _css_03_0032:

Querying the Automatic Snapshot Creation Policy for a Cluster
=============================================================

Function
--------

This API is used to query the automatic snapshot creation policy for a cluster.

URI
---

.. code-block:: text

   GET /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+---------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                           |
   +============+===========+========+=======================================================================================+
   | project_id | Yes       | String | Project ID.                                                                           |
   +------------+-----------+--------+---------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster, for which the automatic snapshot creation policy is to be queried. |
   +------------+-----------+--------+---------------------------------------------------------------------------------------+

Request
-------

None

Response
--------

:ref:`Table 2 <css_03_0032__table2282125191510>` describes the response parameters.

.. _css_03_0032__table2282125191510:

.. table:: **Table 2** Parameter description

   +---------------+---------+---------------------------------------------------------------------------------------+
   | Parameter     | Type    | Description                                                                           |
   +===============+=========+=======================================================================================+
   | keepday       | Integer | Retention days for a snapshot.                                                        |
   +---------------+---------+---------------------------------------------------------------------------------------+
   | period        | String  | Time when a snapshot is created every day.                                            |
   +---------------+---------+---------------------------------------------------------------------------------------+
   | prefix        | String  | Snapshot name prefix.                                                                 |
   +---------------+---------+---------------------------------------------------------------------------------------+
   | bucket        | String  | OBS bucket for storing snapshots.                                                     |
   +---------------+---------+---------------------------------------------------------------------------------------+
   | basePath      | String  | Storage path of the snapshot in the OBS bucket.                                       |
   +---------------+---------+---------------------------------------------------------------------------------------+
   | agency        | String  | Agency used to access OBS buckets.                                                    |
   +---------------+---------+---------------------------------------------------------------------------------------+
   | enable        | String  | Whether to enable the automatic snapshot creation policy.                             |
   +---------------+---------+---------------------------------------------------------------------------------------+
   | snapshotCmkId | String  | Snapshot encryption ID. If the snapshot is not encrypted, value **null** is returned. |
   +---------------+---------+---------------------------------------------------------------------------------------+

Examples
--------

Example request

.. code-block:: text

   GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/policy

Example response

.. code-block::

.. code-block::

   {
       "keepday":2,
       "period":"16:00 GMT+08:00",
       "prefix":"snapshot",
       "bucket":"es-backup",
       "basePath": "css_repository/tests",
       "agency":"usearch",
       "enable":"true",
       "snapshotCmkId" : "a7d5d58c-0330-4d25-860d-c488a4cb4ba7"
   }

Status Code
-----------

:ref:`Table 3 <css_03_0032__table18620659263>` describes the status code.

.. _css_03_0032__table18620659263:

.. table:: **Table 3** Status code

   +-------------+----------------+------------------------------------------------------------------------------------------------+
   | Status Code | Code           | Status Code Description                                                                        |
   +=============+================+================================================================================================+
   | 200         | OK             | The request is processed successfully.                                                         |
   +-------------+----------------+------------------------------------------------------------------------------------------------+
   | 406         | Not Acceptable | The server cannot fulfill the request according to the content characteristics of the request. |
   +-------------+----------------+------------------------------------------------------------------------------------------------+
