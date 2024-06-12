:original_name: css_03_0104.html

.. _css_03_0104:

Enabling Public Network Access
==============================

Function
--------

This API is used to enable public network access.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/public/open

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to enable public network access                    |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------+-----------+------------------------------------------------------------------------+-----------------+
   | Parameter | Mandatory | Type                                                                   | Description     |
   +===========+===========+========================================================================+=================+
   | eip       | Yes       | :ref:`BindPublicReqEip <css_03_0104__request_bindpublicreqeip>` object | EIP information |
   +-----------+-----------+------------------------------------------------------------------------+-----------------+

.. _css_03_0104__request_bindpublicreqeip:

.. table:: **Table 3** BindPublicReqEip

   +-----------+-----------+------------------------------------------------------------------------------------------+---------------------------+
   | Parameter | Mandatory | Type                                                                                     | Description               |
   +===========+===========+==========================================================================================+===========================+
   | bandWidth | Yes       | :ref:`BindPublicReqEipBandWidth <css_03_0104__request_bindpublicreqeipbandwidth>` object | EIP bandwidth information |
   +-----------+-----------+------------------------------------------------------------------------------------------+---------------------------+

.. _css_03_0104__request_bindpublicreqeipbandwidth:

.. table:: **Table 4** BindPublicReqEipBandWidth

   ========= ========= ======= =======================
   Parameter Mandatory Type    Description
   ========= ========= ======= =======================
   size      Yes       Integer Bandwidth. Unit: Mbit/s
   ========= ========= ======= =======================

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 5** Response body parameter

   +-----------+--------+----------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                            |
   +===========+========+========================================================================================+
   | action    | String | Operation. The fixed value is **bindZone**, indicating that the binding is successful. |
   +-----------+--------+----------------------------------------------------------------------------------------+

Request Example
---------------

.. code-block::

   {
     "eip" : {
       "bandWidth" : {
         "size" : 5
       }
     },
     "isAutoPay" : 1
   }

Response Example
----------------

**Status code: 200**

The request is processed successfully.

.. code-block::

   {
     "action" : "bindZone"
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
