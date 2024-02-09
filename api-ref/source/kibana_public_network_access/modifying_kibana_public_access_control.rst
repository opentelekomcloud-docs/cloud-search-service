:original_name: css_03_0123.html

.. _css_03_0123:

Modifying Kibana Public Access Control
======================================

Function
--------

This API is used to modify the Kibana access permission by modifying the Kibana whitelist.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/publickibana/whitelist/update

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose Kibana access permission you want to modify.               |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type   | Description                                                                                                                                                |
   +===========+===========+========+============================================================================================================================================================+
   | whiteList | Yes       | String | Whitelisted IP addresses or network segments that can access Kibana. Separate them with commas (,), and each IP address or network segment must be unique. |
   +-----------+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

The latest whitelist

.. code-block::

   {
     "whiteList" : "192.168.0.xx"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                        |
+===================================+====================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                   |
|                                   |                                                                                                                                    |
|                                   | Modify the request before retry.                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                       |
|                                   |                                                                                                                                    |
|                                   | The resource that the client attempts to create already exists, or the update request fails to be processed because of a conflict. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
