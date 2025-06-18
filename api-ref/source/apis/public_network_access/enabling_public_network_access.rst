:original_name: CreateBindPublic.html

.. _CreateBindPublic:

Enabling Public Network Access
==============================

Function
--------

This API is used to enable public network access.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/public/open

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose public network access you want to enable.                                                                |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+-----------------------------------------------------------------------------+------------------+
   | Parameter | Mandatory | Type                                                                        | Description      |
   +===========+===========+=============================================================================+==================+
   | eip       | Yes       | :ref:`BindPublicReqEip <createbindpublic__request_bindpublicreqeip>` object | EIP information. |
   +-----------+-----------+-----------------------------------------------------------------------------+------------------+

.. _createbindpublic__request_bindpublicreqeip:

.. table:: **Table 3** BindPublicReqEip

   +-----------+-----------+-----------------------------------------------------------------------------------------------+---------------------------+
   | Parameter | Mandatory | Type                                                                                          | Description               |
   +===========+===========+===============================================================================================+===========================+
   | bandWidth | Yes       | :ref:`BindPublicReqEipBandWidth <createbindpublic__request_bindpublicreqeipbandwidth>` object | Public network bandwidth. |
   +-----------+-----------+-----------------------------------------------------------------------------------------------+---------------------------+

.. _createbindpublic__request_bindpublicreqeipbandwidth:

.. table:: **Table 4** BindPublicReqEipBandWidth

   ========= ========= ======= =============================
   Parameter Mandatory Type    Description
   ========= ========= ======= =============================
   size      Yes       Integer Bandwidth range. Unit: Mbit/s
   ========= ========= ======= =============================

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 5** Response body parameters

   +-----------+--------+-----------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                             |
   +===========+========+=========================================================================================+
   | action    | String | Operations. The fixed value is **bindZone**, indicating that the binding is successful. |
   +-----------+--------+-----------------------------------------------------------------------------------------+

Example Requests
----------------

.. code-block::

   {
     "eip" : {
       "bandWidth" : {
         "size" : 5
       }
     }
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "action" : "bindZone"
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
