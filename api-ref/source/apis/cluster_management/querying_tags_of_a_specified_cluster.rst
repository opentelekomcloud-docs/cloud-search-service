:original_name: ShowClusterTag.html

.. _ShowClusterTag:

Querying Tags of a Specified Cluster
====================================

Function
--------

This API is used to query the tags of a specified cluster.

URI
---

GET /v1.0/{project_id}/{resource_type}/{cluster_id}/tags

.. table:: **Table 1** Path Parameters

   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter     | Mandatory | Type   | Description                                                                                                                      |
   +===============+===========+========+==================================================================================================================================+
   | project_id    | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id    | Yes       | String | ID of the cluster you want to query.                                                                                             |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | resource_type | Yes       | String | Resource type. Currently, its value can only be **css-cluster**.                                                                 |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------+--------------------------------------------------------------------------------------+----------------------+
   | Parameter | Type                                                                                 | Description          |
   +===========+======================================================================================+======================+
   | tags      | Array of :ref:`ShowTagsTagsResp <showclustertag__response_showtagstagsresp>` objects | List of cluster tags |
   +-----------+--------------------------------------------------------------------------------------+----------------------+

.. _showclustertag__response_showtagstagsresp:

.. table:: **Table 3** ShowTagsTagsResp

   ========= ====== ===========
   Parameter Type   Description
   ========= ====== ===========
   key       String Tag key
   value     String Tag value
   ========= ====== ===========

Example Requests
----------------

None

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "tags" : [ {
       "key" : "key1",
       "value" : "value1"
     }, {
       "key" : "key2",
       "value" : "value3"
     } ]
   }

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------+
| Status Code                       | Description                                                       |
+===================================+===================================================================+
| 200                               | Request succeeded.                                                |
+-----------------------------------+-------------------------------------------------------------------+
| 400                               | Invalid request.                                                  |
|                                   |                                                                   |
|                                   | The client should modify the request instead of re-initiating it. |
+-----------------------------------+-------------------------------------------------------------------+
| 404                               | The requested resource could not be found.                        |
|                                   |                                                                   |
|                                   | The client should not repeat the request without modifications.   |
+-----------------------------------+-------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
