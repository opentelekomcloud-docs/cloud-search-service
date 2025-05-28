:original_name: StopVpecp.html

.. _StopVpecp:

Disabling the VPC Endpoint Service
==================================

Function
--------

This API is used to disable the VPCEP service for a cluster.

.. note::

   After the VPCEP service is disabled, users can no longer access the cluster via the VPCEP IP address or a private domain name. If you disable the VPCEP service and then re-enable it, the VPCEP IP address or private domain name may change. Exercise caution.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/close

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose VPC endpoint you want to disable.                                                                        |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                      |
   +=======================+=======================+==================================================================================================+
   | action                | String                | **Parameter description**:                                                                       |
   |                       |                       |                                                                                                  |
   |                       |                       | Action. The fixed value is **deleteVpcepservice**, indicating that the VPC endpoint is disabled. |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------+

Example Requests
----------------

None

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "action" : "deleteVpcepservice"
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
