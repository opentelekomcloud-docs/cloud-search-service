:original_name: StartVpecp.html

.. _StartVpecp:

Enabling the VPC Endpoint Service
=================================

Function
--------

The VPC endpoint service enables secure and reliable access across VPCs through a dedicated gateway, without exposing the network information of servers. This API is used to enable VPC endpoints for the cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/open

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Project ID of the account.                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                         |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | ID of the cluster whose VPC endpoint you want to enable. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Cluster ID.                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                         |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter              | Mandatory       | Type            | Description                                                                                                                                |
   +========================+=================+=================+============================================================================================================================================+
   | endpoint_with_dns_name | No              | Boolean         | **Definition**:                                                                                                                            |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | Whether to enable private domain names.                                                                                                    |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Constraints**:                                                                                                                           |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | N/A                                                                                                                                        |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Value range**:                                                                                                                           |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | -  **true**: enabled.                                                                                                                      |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | -  **false**: disabled.                                                                                                                    |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Default value**:                                                                                                                         |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | false                                                                                                                                      |
   +------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | profession_vpcep       | No              | Boolean         | **Definition**:                                                                                                                            |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | Whether to create professional VPC endpoints.                                                                                              |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Constraints**:                                                                                                                           |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | N/A                                                                                                                                        |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Value range**:                                                                                                                           |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | -  **true**: enabled.                                                                                                                      |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | -  **false**: disabled.                                                                                                                    |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Default value**:                                                                                                                         |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | false                                                                                                                                      |
   +------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | dualstack_enable       | No              | Boolean         | **Definition**:                                                                                                                            |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | Whether to enable IPv4/IPv6 dual-stack networking.                                                                                         |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Constraints**:                                                                                                                           |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | The IPv4/IPv6 dual-stack network can be enabled only when a professional VPC endpoint is created and the VPC of the cluster supports IPv6. |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Value range**:                                                                                                                           |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | -  **true**: enabled.                                                                                                                      |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | -  **false**: disabled.                                                                                                                    |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | **Default value**:                                                                                                                         |
   |                        |                 |                 |                                                                                                                                            |
   |                        |                 |                 | false                                                                                                                                      |
   +------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------+----------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                    |
   +=======================+=======================+================================================================+
   | action                | String                | **Definition**:                                                |
   |                       |                       |                                                                |
   |                       |                       | Whether to enable VPC endpoints.                               |
   |                       |                       |                                                                |
   |                       |                       | **Value range**:                                               |
   |                       |                       |                                                                |
   |                       |                       | **createVpcepservice** indicates that the endpoint is enabled. |
   +-----------------------+-----------------------+----------------------------------------------------------------+

Example Requests
----------------

Enable the VPC endpoint service.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/vpcepservice/open

   {
     "endpoint_with_dns_name" : true
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
