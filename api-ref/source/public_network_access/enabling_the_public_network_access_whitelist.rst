:original_name: css_03_0107.html

.. _css_03_0107:

Enabling the Public Network Access Whitelist
============================================

Function
--------

This API is used to enable the public network access whitelist.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/public/whitelist/update

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to enable the public network access whitelist      |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------+-----------+--------+---------------------------------------------------------------------+
   | Parameter | Mandatory | Type   | Description                                                         |
   +===========+===========+========+=====================================================================+
   | whiteList | Yes       | String | IP address of the user that enabled public network access whitelist |
   +-----------+-----------+--------+---------------------------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

.. code-block::

   {
     "whiteList" : "192.168.0.xx"
   }

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                         |
+===================================+=====================================================================================================================================================================================+
| 200                               | The request is processed successfully.                                                                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                    |
|                                   |                                                                                                                                                                                     |
|                                   | Modify the request instead of retrying.                                                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                                                                  |
|                                   |                                                                                                                                                                                     |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request fails to be processed because of the update of the conflict request. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the preconditions that the requester puts on the request.                                                                                           |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
