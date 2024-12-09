:original_name: css_03_0105.html

.. _css_03_0105:

Disabling Public Network Access
===============================

Function
--------

This API is used to disable public network access.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/public/close

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to disable public network access                   |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------+-----------+----------------------------------------------------------------------------------+-----------------+
   | Parameter | Mandatory | Type                                                                             | Description     |
   +===========+===========+==================================================================================+=================+
   | eip       | No        | :ref:`UnBindPublicReqEipReq <css_03_0105__request_unbindpublicreqeipreq>` object | EIP information |
   +-----------+-----------+----------------------------------------------------------------------------------+-----------------+

.. _css_03_0105__request_unbindpublicreqeipreq:

.. table:: **Table 3** UnBindPublicReqEipReq

   +-----------+-----------+------------------------------------------------------------------------------------------+---------------------------+
   | Parameter | Mandatory | Type                                                                                     | Description               |
   +===========+===========+==========================================================================================+===========================+
   | bandWidth | No        | :ref:`BindPublicReqEipBandWidth <css_03_0105__request_bindpublicreqeipbandwidth>` object | EIP bandwidth information |
   +-----------+-----------+------------------------------------------------------------------------------------------+---------------------------+

.. _css_03_0105__request_bindpublicreqeipbandwidth:

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

   +-----------+--------+--------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                |
   +===========+========+============================================================================================+
   | action    | String | Operation. The fixed value is **unbindZone**, indicating that the unbinding is successful. |
   +-----------+--------+--------------------------------------------------------------------------------------------+

Request Example
---------------

.. code-block::

   {
     "eip" : {
       "bandWidth" : {
         "size" : 5
       }
     }
   }

Response Example
----------------

**Status code: 200**

The request is processed successfully.

.. code-block::

   {
     "action" : "unbindZone"
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
