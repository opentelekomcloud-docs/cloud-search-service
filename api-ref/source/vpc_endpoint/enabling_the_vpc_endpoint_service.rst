:original_name: css_03_0110.html

.. _css_03_0110:

Enabling the VPC Endpoint Service
=================================

Function
--------

This API is used to enable the VPC endpoint service.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/open

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose VPC endpoint you want to enable.                           |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   =================== ========= ======= ========================
   Parameter           Mandatory Type    Description
   =================== ========= ======= ========================
   endpointWithDnsName No        Boolean Enable the VPC endpoint.
   =================== ========= ======= ========================

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------+--------+-----------------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                         |
   +===========+========+=====================================================================================================+
   | action    | String | Operations. The fixed value is **createVpcepservice**, indicating that the VPC endpoint is enabled. |
   +-----------+--------+-----------------------------------------------------------------------------------------------------+

Example Requests
----------------

.. code-block::

   {
     "endpointWithDnsName" : true
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "action" : "createVpcepservice"
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
