:original_name: CreateSnapshot.html

.. _CreateSnapshot:

Manually Creating a Snapshot
============================

Function
--------

This API is used to manually create a snapshot.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster for which you want to create a snapshot.                                                                       |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter   | Mandatory | Type   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   +=============+===========+========+=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | name        | Yes       | String | Snapshot name. Enter 4 to 64 characters. Lowercase letters, digits, hyphens (-), and underscores (_) are allowed. The value must start with a letter.                                                                                                                                                                                                                                                                                                                                 |
   +-------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | description | No        | String | Snapshot description. The value can contain up to 256 characters and cannot contain the following characters: !<>=&"'                                                                                                                                                                                                                                                                                                                                                                 |
   +-------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | indices     | No        | String | Name of an index to be backed up. Multiple indexes are separated by commas (,). By default, all indexes are backed up. You can use the combination of a backslash and an asterisk (``*``) to back up data of certain indexes. For example, if you specify 2018-06*, then the data of the indexes with the prefix **2018-06** will be backed up.The value can contain 0 to 1,024 characters. Uppercase letters, spaces, and the following special characters are not allowed: "\\<|>/? |
   +-------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 201**

.. table:: **Table 3** Response body parameters

   +-----------+--------------------------------------------------------------+-----------------------+
   | Parameter | Type                                                         | Description           |
   +===========+==============================================================+=======================+
   | backup    | :ref:`backupRsp <createsnapshot__response_backuprsp>` object | Snapshot information. |
   +-----------+--------------------------------------------------------------+-----------------------+

.. _createsnapshot__response_backuprsp:

.. table:: **Table 4** backupRsp

   ========= ====== =============
   Parameter Type   Description
   ========= ====== =============
   id        String Snapshot ID
   name      String Snapshot name
   ========= ====== =============

Example Requests
----------------

Create a snapshot.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/index_snapshot

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

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                           |
+===================================+=======================================================================================================================================================================+
| 201                               | Resource created.                                                                                                                                                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                      |
|                                   |                                                                                                                                                                       |
|                                   | Modify the request before retry.                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 406                               | The server could not fulfill the request according to the content characteristics of the request.                                                                     |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 500                               | The server has received the request but could not understand it.                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 501                               | The server does not support the function required to fulfill the request.                                                                                             |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
