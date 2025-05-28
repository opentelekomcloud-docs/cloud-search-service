:original_name: UpdateUnbindPublic.html

.. _UpdateUnbindPublic:

Disabling Public Network Access
===============================

Function
--------

This API is used to disable public network access. Public network access cannot be disabled for yearly/monthly clusters by calling this API.

.. note::

   After public network access is disabled, users can no longer access the cluster via a public IP address. If you disable public network access and then re-enable it, the public IP address of the cluster may change. Exercise caution.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/public/close

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose public network access you want to disable.                                                               |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+-----------------------------------------------------------------------------------------+------------------+
   | Parameter | Mandatory | Type                                                                                    | Description      |
   +===========+===========+=========================================================================================+==================+
   | eip       | No        | :ref:`UnBindPublicReqEipReq <updateunbindpublic__request_unbindpublicreqeipreq>` object | EIP information. |
   +-----------+-----------+-----------------------------------------------------------------------------------------+------------------+

.. _updateunbindpublic__request_unbindpublicreqeipreq:

.. table:: **Table 3** UnBindPublicReqEipReq

   +-----------+-----------+-------------------------------------------------------------------------------------------------+---------------------------+
   | Parameter | Mandatory | Type                                                                                            | Description               |
   +===========+===========+=================================================================================================+===========================+
   | bandWidth | No        | :ref:`BindPublicReqEipBandWidth <updateunbindpublic__request_bindpublicreqeipbandwidth>` object | Public network bandwidth. |
   +-----------+-----------+-------------------------------------------------------------------------------------------------+---------------------------+

.. _updateunbindpublic__request_bindpublicreqeipbandwidth:

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

   +-----------+--------+---------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                 |
   +===========+========+=============================================================================================+
   | action    | String | Operations. The fixed value is **unbindZone**, indicating that the unbinding is successful. |
   +-----------+--------+---------------------------------------------------------------------------------------------+

Example Requests
----------------

Disable public network access.

.. code-block:: text

   PUT /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/public/close

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
     "action" : "unbindZone"
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
