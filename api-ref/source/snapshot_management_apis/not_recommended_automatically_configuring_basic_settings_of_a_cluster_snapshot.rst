:original_name: css_03_0037.html

.. _css_03_0037:

(Not Recommended) Automatically Configuring Basic Settings of a Cluster Snapshot
================================================================================

.. note::

   The API for automatically configuring a cluster snapshot can automatically create OBS buckets and agencies for storing snapthos. If you have multiple clusters, an OBS bucket will be created for each cluster via this API during automatic configuration and consume your OBS quota. Too many OBS buckets will be difficult to manage. You are advised to perform operations in :ref:`Modifying Basic Configurations of a Cluster Snapshot <css_03_0030>`.

Function
--------

This API is used to automatically set basic configurations for a cluster snapshot, including configuring OBS buckets and IAM agency.

-  **OBS Bucket**: Enter the location of the OBS bucket used for storing snapshots.
-  **IAM Agency**: Authorize you to use OBS in IAM so that snapshots must be stored in OBS.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/auto_setting

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+--------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                            |
   +============+===========+========+========================================================+
   | project_id | Yes       | String | Project ID.                                            |
   +------------+-----------+--------+--------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster where snapshots are to be backed up. |
   +------------+-----------+--------+--------------------------------------------------------+

Request
-------

None

Response
--------

None

Examples
--------

Example request

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/auto_setting

Status Code
-----------

:ref:`Table 2 <css_03_0037__table209491933101317>` describes the status code.

.. _css_03_0037__table209491933101317:

.. table:: **Table 2** Status code

   +-------------+----------------+------------------------------------------------------------------------------------------------+
   | Status Code | Code           | Status Code Description                                                                        |
   +=============+================+================================================================================================+
   | 200         | OK             | The request is processed successfully.                                                         |
   +-------------+----------------+------------------------------------------------------------------------------------------------+
   | 406         | Not Acceptable | The server cannot fulfill the request according to the content characteristics of the request. |
   +-------------+----------------+------------------------------------------------------------------------------------------------+
