:original_name: StartVpecp.html

.. _StartVpecp:

Enabling the VPC Endpoint Service
=================================

Function
--------

This API is used to enable the VPCEP service for a cluster.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/open

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose VPC endpoint you want to enable.                                                                         |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter           | Mandatory       | Type            | Description                                                                                                                                                                                    |
   +=====================+=================+=================+================================================================================================================================================================================================+
   | endpointWithDnsName | No              | Boolean         | Enable the VPC endpoint.                                                                                                                                                                       |
   +---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | professionVpcep     | No              | Boolean         | Create a professional VPC endpoint.                                                                                                                                                            |
   |                     |                 |                 |                                                                                                                                                                                                |
   |                     |                 |                 | -  **true**: enabled.                                                                                                                                                                          |
   |                     |                 |                 |                                                                                                                                                                                                |
   |                     |                 |                 | -  **false**: disabled.                                                                                                                                                                        |
   +---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | dualstackEnable     | No              | Boolean         | Whether to enable the IPv4/IPv6 dual-stack network. The IPv4/IPv6 dual-stack network can be enabled only when a professional VPC endpoint is created and the VPC of the cluster supports IPv6. |
   |                     |                 |                 |                                                                                                                                                                                                |
   |                     |                 |                 | -  **true**: enabled.                                                                                                                                                                          |
   |                     |                 |                 |                                                                                                                                                                                                |
   |                     |                 |                 | -  **false**: disabled.                                                                                                                                                                        |
   +---------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                     |
   +=======================+=======================+=================================================================================================+
   | action                | String                | **Parameter description**:                                                                      |
   |                       |                       |                                                                                                 |
   |                       |                       | Action. The fixed value is **createVpcepservice**, indicating that the VPC endpoint is enabled. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+

Example Requests
----------------

Enable the VPC endpoint service.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/vpcepservice/open

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

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
