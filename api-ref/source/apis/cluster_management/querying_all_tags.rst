:original_name: ListClustersTags.html

.. _ListClustersTags:

Querying All Tags
=================

Function
--------

This API is used to query all tags in a specified region.

URI
---

GET /v1.0/{project_id}/{resource_type}/tags

.. table:: **Table 1** Path Parameters

   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter     | Mandatory | Type   | Description                                                                                                                      |
   +===============+===========+========+==================================================================================================================================+
   | project_id    | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
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

   +-----------+----------------------------------------------------------------------------------------------+----------------------+
   | Parameter | Type                                                                                         | Description          |
   +===========+==============================================================================================+======================+
   | tags      | Array of :ref:`ShowAllTagsTagsResp <listclusterstags__response_showalltagstagsresp>` objects | List of cluster tags |
   +-----------+----------------------------------------------------------------------------------------------+----------------------+

.. _listclusterstags__response_showalltagstagsresp:

.. table:: **Table 3** ShowAllTagsTagsResp

   ========= ================ ===========
   Parameter Type             Description
   ========= ================ ===========
   key       String           Tag key
   values    Array of strings Tag value
   ========= ================ ===========

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
       "values" : [ "value1", "value2" ]
     }, {
       "key" : "key2",
       "values" : [ "value1", "value2" ]
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
