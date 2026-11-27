:original_name: CreateSnapshot.html

.. _CreateSnapshot:

Manually Creating a Snapshot
============================

Function
--------

The snapshot backup function of CSS provides data protection and restoration capabilities for Elasticsearch/OpenSearch clusters. Through snapshot backup, the data status of a cluster can be saved to an OBS bucket for restoration when needed. CSS cluster snapshots are classified into two types: automatic snapshots and manual snapshots.

-  Automatic snapshot: Automatically executes snapshot backup operations based on preset time policies, suitable for periodic backup scenarios, such as daily or weekly backups, to ensure continuous data protection. By configuring automatic snapshot policies, you can reduce manual operations and improve backup reliability and efficiency.

-  Manual snapshot: Manually triggers snapshot backup operations based on user requirements, suitable for temporary backups or specific scenarios, such as backing up before major operations (for example, cluster upgrade) so that you can quickly restore to the previous state if a problem occurs. Manual snapshots provide higher flexibility, allowing you to create snapshots at any time as needed.

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
   | project_id      | Yes             | String          | **Definition**                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Constraints**                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Range**                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                                       |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Default Value**                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | ID of the cluster for which you want to create a snapshot. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Constraints**                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Range**                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Default Value**                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                |
   +=================+=================+=================+============================================================================================================================================================+
   | name            | Yes             | String          | **Definition**                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | Snapshot name.                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Constraints**                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Range**                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | Snapshot name. Enter 4 to 64 characters. Only lowercase letters, digits, hyphens (-), and underscores (_) are allowed. The value must start with a letter. |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Default Value**                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                                        |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | description     | No              | String          | **Definition**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | Snapshot description.                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Constraints**:                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Value range**:                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | The value contains 0 to 256 characters and cannot contain !<>=&"'                                                                                          |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Default value**:                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                                        |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | indices         | No              | String          | **Definition**                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | Names of the indexes to be backed up.                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | -  You can specify indexes, separated by commas (,), for example, **index1,index2,index3**.                                                                |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | -  You can use an asterisk (*) to match multiple indexes. For example, index* matches all indexes whose names start with **index**.                        |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Constraints**                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Range**                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | 0 to 1,024 characters. Uppercase letters, spaces, or the following special characters are not allowed: "<|>/?                                              |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | **Default Value**                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                            |
   |                 |                 |                 | Empty by default, indicating that all indexes are backed up.                                                                                               |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 201**

.. table:: **Table 3** Response body parameters

   +-----------------------+--------------------------------------------------------------+-----------------------+
   | Parameter             | Type                                                         | Description           |
   +=======================+==============================================================+=======================+
   | backup                | :ref:`backupRsp <createsnapshot__response_backuprsp>` object | **Definition**        |
   |                       |                                                              |                       |
   |                       |                                                              | Snapshot information. |
   +-----------------------+--------------------------------------------------------------+-----------------------+

.. _createsnapshot__response_backuprsp:

.. table:: **Table 4** backupRsp

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | id                    | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Snapshot ID.          |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+
   | name                  | String                | **Definition**        |
   |                       |                       |                       |
   |                       |                       | Snapshot name.        |
   |                       |                       |                       |
   |                       |                       | **Range**             |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+

Example Requests
----------------

Create a snapshot.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/index_snapshot

   {
     "name" : "snapshot_001",
     "indices" : "myindex1,myindex2"
   }

Example Responses
-----------------

**Status code: 201**

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
