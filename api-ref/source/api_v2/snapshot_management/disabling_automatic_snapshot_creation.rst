:original_name: StopAutoCreateSnapshots.html

.. _StopAutoCreateSnapshots:

Disabling Automatic Snapshot Creation
=====================================

Function
--------

CSS allows you to use snapshots to back up and restore the data of an OpenSearch cluster. By storing a snapshot in an OBS bucket, you save a point-in-time copy of the cluster's data. By restoring this snapshot, you can restore the cluster to a previous state. There are two ways to create snapshots to back up a CSS cluster: automatic and manual.

-  Automatic snapshot creation: Snapshots are created periodically based on a preset time policy, for example, daily or weekly, to ensure continuous data protection. This reduces manual effort and improves backup reliability and efficiency.

-  Manual snapshot creation: You create snapshots manually for special occasions, for example, prior to a high-risk operation (such as a cluster upgrade). This ensures you can restore data using snapshots in case anything should go wrong. Manual snapshots provide additional flexibility.

This API is used to disable automatic snapshot creation.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v2.0/{project_id}/clusters/{cluster_id}/snapshots/policy/close

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                        |
   +=================+=================+=================+====================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Project ID of the account.                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | ID of the cluster that the snapshot belongs to. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Cluster ID.                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

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

Disable the automatic backup function.

.. code-block:: text

   PUT https://{Endpoint}/v2.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/snapshots/policy/close

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                           |
+===================================+=======================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                      |
|                                   |                                                                                                                                                                       |
|                                   | Modify the request before retry.                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
