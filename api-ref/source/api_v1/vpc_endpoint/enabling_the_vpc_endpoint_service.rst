:original_name: StartVpecp.html

.. _StartVpecp:

Enabling the VPC Endpoint Service
=================================

Function
--------

This API is used to enable the VPCEP service for a cluster.

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

   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter              | Mandatory       | Type            | Description                                                                                                                                                                                    |
   +========================+=================+=================+================================================================================================================================================================================================+
   | endpoint_with_dns_name | No              | Boolean         | Enable the VPC endpoint.                                                                                                                                                                       |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | profession_vpcep       | No              | Boolean         | Create a professional VPC endpoint.                                                                                                                                                            |
   |                        |                 |                 |                                                                                                                                                                                                |
   |                        |                 |                 | -  **true**: This option will be enabled.                                                                                                                                                      |
   |                        |                 |                 |                                                                                                                                                                                                |
   |                        |                 |                 | -  **false**: This option will be disabled.                                                                                                                                                    |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | dualstack_enable       | No              | Boolean         | Whether to enable the IPv4/IPv6 dual-stack network. The IPv4/IPv6 dual-stack network can be enabled only when a professional VPC endpoint is created and the VPC of the cluster supports IPv6. |
   |                        |                 |                 |                                                                                                                                                                                                |
   |                        |                 |                 | -  **true**: This option will be enabled.                                                                                                                                                      |
   |                        |                 |                 |                                                                                                                                                                                                |
   |                        |                 |                 | -  **false**: This option will be disabled.                                                                                                                                                    |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                        |
   +=======================+=======================+====================================================================================================+
   | action                | String                | **Parameter description**:                                                                         |
   |                       |                       |                                                                                                    |
   |                       |                       | Operation. The fixed value is **createVpcepservice**, indicating that the VPC endpoint is enabled. |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------+

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
