:original_name: ShowLogBackup.html

.. _ShowLogBackup:

Searching for Logs
==================

Function
--------

This API is used to query log information.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/logs/search

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to query.                                                                                             |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +--------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------+
   | Parameter    | Mandatory | Type   | Description                                                                                                                |
   +==============+===========+========+============================================================================================================================+
   | instanceName | Yes       | String | Node name. Obtain the **name** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`. |
   +--------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------+
   | level        | Yes       | String | Log level. The levels of logs that can be queried are **INFO**, **ERROR**, **DEBUG**, and **WARN**.                        |
   +--------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------+
   | logType      | Yes       | String | Log type. The types of logs that can be queried are **deprecation**, **indexingSlow**, **searchSlow**, and **instance**.   |
   +--------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------+-------------------------------------------------------------------+-------------+
   | Parameter | Type                                                              | Description |
   +===========+===================================================================+=============+
   | logList   | Array of :ref:`logList <showlogbackup__response_loglist>` objects | Log list.   |
   +-----------+-------------------------------------------------------------------+-------------+

.. _showlogbackup__response_loglist:

.. table:: **Table 4** logList

   ========= ====== ============
   Parameter Type   Description
   ========= ====== ============
   content   String Log content.
   date      String Date.
   level     String Log level.
   ========= ====== ============

Example Requests
----------------

Query logs.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/logs/search

   {
     "instanceName" : "css-4312-ess-esn-1-1",
     "level" : "INFO",
     "logType" : "instance"
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

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

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
