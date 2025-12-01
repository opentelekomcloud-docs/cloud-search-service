:original_name: CreateSnapshot.html

.. _CreateSnapshot:

Manually Creating a Snapshot
============================

Function
--------

CSS allows you to use snapshots to back up and restore Elasticsearch cluster data. By storing a snapshot in an OBS bucket, you save a point-in-time copy of the cluster's data. By restoring this snapshot, you can restore the cluster to a previous state. There are two ways to create snapshots to back up a CSS cluster: automatic and manual.

-  Automatic snapshot creation: Snapshots are created periodically based on a preset time policy, for example, daily or weekly, to ensure continuous data protection. This reduces manual effort and improves backup reliability and efficiency.

-  Manual snapshot creation: You can manually create snapshots when necessary, for example, before performing a mission-critical operation (such as a cluster upgrade), so you can use these snapshots to quickly restore the cluster to a previous state in case anything goes wrong. Manual snapshots provide more flexibility.

This API is used to manually create a snapshot.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                   |
   +=================+=================+=================+===============================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Project ID of the account.                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | ID of the cluster for which you want to create a snapshot. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Cluster ID.                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                     |
   +=================+=================+=================+=================================================================================================================================================================================================================================================================================================================================================+
   | name            | Yes             | String          | **Definition**:                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Snapshot name.                                                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Snapshot name. Enter 4 to 64 characters. Only lowercase letters, digits, hyphens (-), and underscores (_) are allowed. The value must start with a letter.                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | description     | No              | String          | **Definition**:                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Snapshot description.                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | The value contains 0 to 256 characters and cannot contain !<>=&"'                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | indices         | No              | String          | **Definition**:                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Name of an index to be backed up. Multiple indexes are separated by commas (,). By default, all indexes are backed up. You can use the combination of a backslash and an asterisk (``*``) to back up data of certain indexes. For example, if you specify 2018-06*, then the data of the indexes with the prefix **2018-06** will be backed up. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | The value can contain 0 to 1,024 characters. Uppercase letters, spaces, and the following special characters are not allowed: "\\<|>/?                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | \*, indicating all indexes.                                                                                                                                                                                                                                                                                                                     |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 201**

.. table:: **Table 3** Response body parameters

   +-----------------------+--------------------------------------------------------------+---------------------------+
   | Parameter             | Type                                                         | Description               |
   +=======================+==============================================================+===========================+
   | backup                | :ref:`backupRsp <createsnapshot__response_backuprsp>` object | **Definition**:           |
   |                       |                                                              |                           |
   |                       |                                                              | The snapshot information. |
   |                       |                                                              |                           |
   |                       |                                                              | **Value range**:          |
   |                       |                                                              |                           |
   |                       |                                                              | N/A                       |
   +-----------------------+--------------------------------------------------------------+---------------------------+

.. _createsnapshot__response_backuprsp:

.. table:: **Table 4** backupRsp

   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                |
   +=======================+=======================+============================================================================================================================================================+
   | id                    | String                | **Definition**:                                                                                                                                            |
   |                       |                       |                                                                                                                                                            |
   |                       |                       | Snapshot ID.                                                                                                                                               |
   |                       |                       |                                                                                                                                                            |
   |                       |                       | **Value range**:                                                                                                                                           |
   |                       |                       |                                                                                                                                                            |
   |                       |                       | N/A                                                                                                                                                        |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | name                  | String                | **Definition**:                                                                                                                                            |
   |                       |                       |                                                                                                                                                            |
   |                       |                       | Snapshot name.                                                                                                                                             |
   |                       |                       |                                                                                                                                                            |
   |                       |                       | **Value range**:                                                                                                                                           |
   |                       |                       |                                                                                                                                                            |
   |                       |                       | Snapshot name. Enter 4 to 64 characters. Only lowercase letters, digits, hyphens (-), and underscores (_) are allowed. The value must start with a letter. |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

Create a snapshot.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/index_snapshot

   {
     "name" : "snapshot_001",
     "indices" : "myindex1myindex2"
   }

Example Responses
-----------------

**Status code: 201**

Resource created.

.. code-block::

   {
     "backup" : {
       "id" : "9dc4f5c9-33c0-45c7-9378-ae35ae350682",
       "name" : "snapshot_101"
     }
   }

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                          |
+===================================+======================================================================================================================================================+
| 201                               | Resource created.                                                                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                     |
|                                   |                                                                                                                                                      |
|                                   | Modify the request before retry.                                                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.                                                                                                                                    |
|                                   |                                                                                                                                                      |
|                                   | The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 406                               | The server could not fulfill the request according to the content characteristics of the request.                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 500                               | The server has received the request but could not understand it.                                                                                     |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 501                               | The server does not support the function required to fulfill the request.                                                                            |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
