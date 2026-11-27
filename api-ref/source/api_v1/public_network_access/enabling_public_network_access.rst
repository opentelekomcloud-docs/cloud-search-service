:original_name: CreateBindPublic.html

.. _CreateBindPublic:

Enabling Public Network Access
==============================

Function
--------

When an Elasticsearch/OpenSearch cluster has security mode and HTTPS access enabled, you can choose whether to configure public access. After public access is configured, you can obtain a public IP address to access the security cluster from the public network. Additionally, access control can be configured to set the IP addresses or CIDR blocks allowed to access the cluster from the public network.

Public access of an Elasticsearch/OpenSearch cluster is implemented through a shared load balancer, which shares resources with other instances. If your workloads require quicker access, you are advised to use a dedicated load balancer to access the cluster. For configuration details, see "Configuring a Dedicated Load Balancer for an Elasticsearch Cluster."

.. note::

   When public access is enabled and no access control whitelist is configured, all IP addresses are allowed. You are advised to configure an appropriate access control whitelist.

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
   | project_id      | Yes             | String          | **Definition**                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Range**                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                                              |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default Value**                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | ID of the cluster whose public network access you want to enable. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Range**                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default Value**                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                        | Description                                                                                                                                                   |
   +=================+=================+=============================================================================+===============================================================================================================================================================+
   | eip             | Yes             | :ref:`BindPublicReqEip <createbindpublic__request_bindpublicreqeip>` object | **Definition**:                                                                                                                                               |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | EIP for public network access.                                                                                                                                |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | **Constraints**:                                                                                                                                              |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | N/A                                                                                                                                                           |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | **Value range**:                                                                                                                                              |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | N/A                                                                                                                                                           |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | **Default value**:                                                                                                                                            |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | white_list      | No              | String                                                                      | **Definition**                                                                                                                                                |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | Whitelist for public access control. The CIDR blocks or IP addresses to be whitelisted must be separated by commas (,). Example: **192.168.1.1,10.0.0.0/24**. |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | **Constraints**                                                                                                                                               |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | The following are not supported: 0.0.0.0,x.x.x.x/0,172.16.0.0-172.16.255.255, non-standard formats such as 192.168.1, or duplicate entries.                   |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | If no access whitelist is configured, all public IP addresses can access the cluster. This poses security risks and is not recommended.                       |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | **Range**                                                                                                                                                     |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | IP addresses or CIDR blocks, separated by commas (,). Duplicate entries are not allowed.                                                                      |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | **Default Value**                                                                                                                                             |
   |                 |                 |                                                                             |                                                                                                                                                               |
   |                 |                 |                                                                             | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
   |                 |                 |                 | 1-200                                |
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
     "white_list" : "127.0.0.1"
   }

Example Responses
-----------------

**Status code: 200**

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
