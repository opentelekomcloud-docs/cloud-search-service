:original_name: css_03_0110.html

.. _css_03_0110:

Enabling the VPC Endpoint Service
=================================

Function
--------

This API is used to enable the VPC endpoint service.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/open

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to enable the VPC endpoint                         |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +---------------------+-----------------+-----------------+------------------------------------------------------+
   | Parameter           | Mandatory       | Type            | Description                                          |
   +=====================+=================+=================+======================================================+
   | endpointWithDnsName | No              | Boolean         | Indicates whether to enable the private domain name. |
   |                     |                 |                 |                                                      |
   |                     |                 |                 | -  **true**: enabled                                 |
   |                     |                 |                 | -  **false**: disabled                               |
   +---------------------+-----------------+-----------------+------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameter

   +-----------+--------+----------------------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                                        |
   +===========+========+====================================================================================================+
   | action    | String | Operation. The fixed value is **createVpcepservice**, indicating that the VPC endpoint is enabled. |
   +-----------+--------+----------------------------------------------------------------------------------------------------+

Request Example
---------------

.. code-block::

   {
     "endpointWithDnsName" : true
   }

Response Example
----------------

**Status code: 200**

The request is processed successfully.

.. code-block::

   {
     "action" : "createVpcepservice"
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
