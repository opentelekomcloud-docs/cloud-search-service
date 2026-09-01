:original_name: DeleteSnapshot.html

.. _DeleteSnapshot:

Deleting a Snapshot
===================

Function
--------

Delete snapshots that are no longer needed to reclaim storage spaces.

This API is used to delete a snapshot.

.. note::

   After a snapshot is deleted, its data cannot be restored. Exercise caution.

Constraints
-----------

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
   |                 |                 |                 | ID of the snapshot you want to delete. For details, see :ref:`Querying Snapshots <listsnapshots>`.                                                              |
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
