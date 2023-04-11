:original_name: css_03_0106.html

.. _css_03_0106:

Modifying Public Network Access Bandwidth
=========================================

Function
--------

This API is used to modify the public network access bandwidth.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/public/bandwidth

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose public network access bandwidth you want to modify.        |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+------------------------------------------------------------------------------------------+---------------------------+
   | Parameter | Mandatory | Type                                                                                     | Description               |
   +===========+===========+==========================================================================================+===========================+
   | bandWidth | Yes       | :ref:`BindPublicReqEipBandWidth <css_03_0106__request_bindpublicreqeipbandwidth>` object | Public network bandwidth. |
   +-----------+-----------+------------------------------------------------------------------------------------------+---------------------------+

.. _css_03_0106__request_bindpublicreqeipbandwidth:

.. table:: **Table 3** BindPublicReqEipBandWidth

   ========= ========= ======= =============================
   Parameter Mandatory Type    Description
   ========= ========= ======= =============================
   size      Yes       Integer Bandwidth range. Unit: Mbit/s
   ========= ========= ======= =============================

Response Parameters
-------------------

None

Example Requests
----------------

.. code-block::

   {
     "bandWidth" : {
       "size" : 5
     }
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
