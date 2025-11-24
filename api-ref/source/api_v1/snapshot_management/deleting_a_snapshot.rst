:original_name: DeleteSnapshot.html

.. _DeleteSnapshot:

Deleting a Snapshot
===================

Function
--------

CSS allows you to use snapshots to back up and restore Elasticsearch cluster data. By storing a snapshot in an OBS bucket, you save a point-in-time copy of the cluster's data. By restoring this snapshot, you can restore the cluster to a previous state. There are two ways to create snapshots to back up a CSS cluster: automatic and manual.

-  Automatic snapshot creation: Snapshots are created periodically based on a preset time policy, for example, daily or weekly, to ensure continuous data protection. This reduces manual effort and improves backup reliability and efficiency.

-  Manual snapshot creation: You can manually create snapshots when necessary, for example, before performing a mission-critical operation (such as a cluster upgrade), so you can use these snapshots to quickly restore the cluster to a previous state in case anything goes wrong. Manual snapshots provide more flexibility.

This API is used to delete a snapshot.

.. note::

   After a snapshot is deleted, its data cannot be restored. Exercise caution.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                     |
   +=================+=================+=================+=================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Project ID of the account.                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | ID of the cluster to which the to-be-deleted snapshot belongs. For details about how to obtain the cluster ID, see :ref:`Obtaining a Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | Cluster ID.                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | snapshot_id     | Yes             | String          | **Definition**:                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | ID of the snapshot you want to delete.                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Delete a snapshot.

.. code-block:: text

   DELETE https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/29a2254e-947f-4463-b65a-5f0b17515fae

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                          |
+===================================+======================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                     |
|                                   |                                                                                                                                                      |
|                                   | Modify the request before retry.                                                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.                                                                                                                                    |
|                                   |                                                                                                                                                      |
|                                   | The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
