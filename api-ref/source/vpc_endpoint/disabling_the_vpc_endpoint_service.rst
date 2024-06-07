:original_name: css_03_0111.html

.. _css_03_0111:

Disabling the VPC Endpoint Service
==================================

Function
--------

This API is used to disable the VPC endpoint service.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/close

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to disable the VPC endpoint service                |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameter

   +-----------+--------+-----------------------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                               |
   +===========+========+===========================================================================================================+
   | action    | String | Operation. The fixed value is **deleteVpcepservice**, indicating that the VPC endpoint has been disabled. |
   +-----------+--------+-----------------------------------------------------------------------------------------------------------+

Request Example
---------------

None

Response Example
----------------

**Status code: 200**

The request is processed successfully.

.. code-block::

   {
     "action" : "deleteVpcepservice"
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
