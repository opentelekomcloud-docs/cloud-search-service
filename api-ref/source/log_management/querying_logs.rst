:original_name: css_03_0102.html

.. _css_03_0102:

Querying Logs
=============

Function
--------

This API is used to query log information.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/logs/search

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be queried                                                    |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +--------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------+
   | Parameter    | Mandatory | Type   | Description                                                                                                                |
   +==============+===========+========+============================================================================================================================+
   | instanceName | Yes       | String | Node name. Obtain the **Name** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`. |
   +--------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------+
   | level        | Yes       | String | Log level. The log levels that can be queried are **INFO**, **ERROR**, **DEBUG**, and **WARN**.                            |
   +--------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------+
   | logType      | Yes       | String | Log type. The log types that can be queried are **deprecation**, **indexingSlow**, **searchSlow**, and **instance**.       |
   +--------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameter

   +-----------+-----------------------------------------------------------------+-------------+
   | Parameter | Type                                                            | Description |
   +===========+=================================================================+=============+
   | logList   | Array of :ref:`logList <css_03_0102__response_loglist>` objects | Log list    |
   +-----------+-----------------------------------------------------------------+-------------+

.. _css_03_0102__response_loglist:

.. table:: **Table 4** logList

   ========= ====== ===========
   Parameter Type   Description
   ========= ====== ===========
   content   String Log content
   date      String Date
   level     String Log level
   ========= ====== ===========

Request Example
---------------

.. code-block::

   {
     "instanceName" : "css-4312-ess-esn-1-1",
     "level" : "INFO",
     "logType" : "instance"
   }

Response Example
----------------

**Status code: 200**

The request is processed successfully.

.. code-block::

   {
     "logList" : [ {
       "content" : "xxxxxx",
       "date" : "2021-10-08T03:55:54,718",
       "level" : "INFO"
     } ]
   }

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
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
