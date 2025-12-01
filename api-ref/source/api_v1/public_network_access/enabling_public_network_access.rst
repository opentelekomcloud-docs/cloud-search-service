:original_name: CreateBindPublic.html

.. _CreateBindPublic:

Enabling Public Network Access
==============================

Function
--------

Public network access is supported only when Security Mode and HTTPS Access are enabled for a cluster. When Public IP Address is enabled, a public IP address is automatically assigned, which will enable access to the security cluster from the public network. Additionally, you can configure access control from the public network by IP addresses or IP address ranges.

To enable public network access for Elasticsearch or OpenSearch clusters, a shared load balancer is typically used for load balancing. If your workloads require quicker access, you are advised to use a dedicated load balancer to connect to your clusters. For details about its configuration, see section "Configuring a Dedicated Load Balancer for an Elasticsearch Cluster."

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/public/open

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Project ID of the account.                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | ID of the cluster whose public network access you want to enable. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Cluster ID.                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                        | Description                                                                                                 |
   +=================+=================+=============================================================================+=============================================================================================================+
   | eip             | Yes             | :ref:`BindPublicReqEip <createbindpublic__request_bindpublicreqeip>` object | **Definition**:                                                                                             |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | EIP for public network access.                                                                              |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | **Constraints**:                                                                                            |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | N/A                                                                                                         |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | **Value range**:                                                                                            |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | N/A                                                                                                         |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | **Default value**:                                                                                          |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | N/A                                                                                                         |
   +-----------------+-----------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+
   | white_list      | No              | String                                                                      | **Definition**:                                                                                             |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | Public network access control whitelist.                                                                    |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | **Constraints**:                                                                                            |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | Separate the whitelisted CIDR blocks or IP addresses with commas (,), and make sure each of them is unique. |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | **Value range**:                                                                                            |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | N/A                                                                                                         |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | **Default value**:                                                                                          |
   |                 |                 |                                                                             |                                                                                                             |
   |                 |                 |                                                                             | N/A                                                                                                         |
   +-----------------+-----------------+-----------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------+

.. _createbindpublic__request_bindpublicreqeip:

.. table:: **Table 3** BindPublicReqEip

   +-----------------+-----------------+-----------------------------------------------------------------------------------------------+---------------------------+
   | Parameter       | Mandatory       | Type                                                                                          | Description               |
   +=================+=================+===============================================================================================+===========================+
   | band_width      | Yes             | :ref:`BindPublicReqEipBandWidth <createbindpublic__request_bindpublicreqeipbandwidth>` object | **Definition**:           |
   |                 |                 |                                                                                               |                           |
   |                 |                 |                                                                                               | Public network bandwidth. |
   |                 |                 |                                                                                               |                           |
   |                 |                 |                                                                                               | **Constraints**:          |
   |                 |                 |                                                                                               |                           |
   |                 |                 |                                                                                               | N/A                       |
   |                 |                 |                                                                                               |                           |
   |                 |                 |                                                                                               | **Value range**:          |
   |                 |                 |                                                                                               |                           |
   |                 |                 |                                                                                               | N/A                       |
   |                 |                 |                                                                                               |                           |
   |                 |                 |                                                                                               | **Default value**:        |
   |                 |                 |                                                                                               |                           |
   |                 |                 |                                                                                               | N/A                       |
   +-----------------+-----------------+-----------------------------------------------------------------------------------------------+---------------------------+

.. _createbindpublic__request_bindpublicreqeipbandwidth:

.. table:: **Table 4** BindPublicReqEipBandWidth

   +-----------------+-----------------+-----------------+--------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                          |
   +=================+=================+=================+======================================+
   | size            | Yes             | Integer         | **Definition**:                      |
   |                 |                 |                 |                                      |
   |                 |                 |                 | Public network bandwidth, in Mbit/s. |
   |                 |                 |                 |                                      |
   |                 |                 |                 | **Constraints**:                     |
   |                 |                 |                 |                                      |
   |                 |                 |                 | N/A                                  |
   |                 |                 |                 |                                      |
   |                 |                 |                 | **Value range**:                     |
   |                 |                 |                 |                                      |
   |                 |                 |                 | N/A                                  |
   |                 |                 |                 |                                      |
   |                 |                 |                 | **Default value**:                   |
   |                 |                 |                 |                                      |
   |                 |                 |                 | N/A                                  |
   +-----------------+-----------------+-----------------+--------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 5** Response body parameters

   +-----------------------+-----------------------+-----------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                 |
   +=======================+=======================+=============================================================================+
   | action                | String                | **Definition**:                                                             |
   |                       |                       |                                                                             |
   |                       |                       | A setting required to enable public network access.                         |
   |                       |                       |                                                                             |
   |                       |                       | **Value range**:                                                            |
   |                       |                       |                                                                             |
   |                       |                       | The fixed value is **bindZone**, indicating that the binding is successful. |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------+

Example Requests
----------------

Enable public network access.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/public/open

   {
     "eip" : {
       "band_width" : {
         "size" : 5
       }
     },
     "white_list" : "127.0.0.1",
     "is_auto_pay" : 1
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "action" : "bindZone"
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
