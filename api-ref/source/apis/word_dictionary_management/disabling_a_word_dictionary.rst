:original_name: DeleteIkThesaurus.html

.. _DeleteIkThesaurus:

Disabling a Word Dictionary
===========================

Function
--------

This API is used to clear custom word dictionaries (main word dictionary, stop word dictionary, and synonym dictionary).

URI
---

DELETE /v1.0/{project_id}/clusters/{cluster_id}/thesaurus

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose custom word dictionary you want to delete.                                                               |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

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

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                           |
+=============+=======================================================================================================================================================================+
| 200         | Request succeeded.                                                                                                                                                    |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403         | Request rejected.The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 500         | The server is able to receive but unable to understand the request.                                                                                                   |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
