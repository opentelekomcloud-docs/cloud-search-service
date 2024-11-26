:original_name: DeleteClustersTags.html

.. _DeleteClustersTags:

Deleting a Cluster Tag
======================

Function
--------

This API is used to delete a cluster tag.

URI
---

DELETE /v1.0/{project_id}/{resource_type}/{cluster_id}/tags/{key}

.. table:: **Table 1** Path Parameters

   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter     | Mandatory | Type   | Description                                                                                                                      |
   +===============+===========+========+==================================================================================================================================+
   | project_id    | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id    | Yes       | String | ID of the cluster that you want to delete tags from.                                                                             |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | resource_type | Yes       | String | Resource type. Currently, its value can only be **css-cluster**.                                                                 |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | key           | Yes       | String | Name of the tag you want to delete. If the tag name is in Chinese, encode the tag name using URL before calling the API.         |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Example Requests
----------------

None

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------+
| Status Code                       | Description                                                       |
+===================================+===================================================================+
| 204                               | Request succeeded.                                                |
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
