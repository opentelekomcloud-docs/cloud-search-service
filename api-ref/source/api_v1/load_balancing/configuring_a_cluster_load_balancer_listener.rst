:original_name: CreateElbListener.html

.. _CreateElbListener:

Configuring a Cluster Load Balancer Listener
============================================

Function
--------

CSS can interconnect with ELB. This API automatically creates listeners, backend server groups, and health check tasks for Elasticsearch or OpenSearch clusters, and interconnects the dedicated load balancers.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/es-listeners

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                   |
   +=================+=================+=================+===============================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                               |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.              |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                                                              |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                                                              |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | Project ID of the account.                                                                                                                    |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                           |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                               |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | ID of the cluster that you want to rename. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                                                              |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                                                              |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | Cluster ID.                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                           |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                             |
   +=================+=================+=================+=========================================================================================================+
   | protocol        | Yes             | String          | **Definition**:                                                                                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | Protocol type.                                                                                          |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | -  **HTTP**: HTTP protocol                                                                              |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | -  **HTTPS**: HTTPS protocol                                                                            |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                      |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+
   | protocol_port   | Yes             | Integer         | **Definition**:                                                                                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | Specifies the port used by the listener.                                                                |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | The port cannot be the same as that of another load balancer listener.                                  |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | 0-65535                                                                                                 |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                      |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+
   | server_cert_id  | No              | String          | **Definition**:                                                                                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | ID of the server certificate used by the listener                                                       |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | This parameter is mandatory when protocol is set to **HTTPS**.                                          |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                      |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+
   | ca_cert_id      | No              | String          | **Definition**:                                                                                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | ID of the CA certificate used by the listener.                                                          |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | This parameter is mandatory when protocol is set to **HTTPS** and bidirectional authentication is used. |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                      |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+
   | type            | No              | String          | **Definition**                                                                                          |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | Configuration type.                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Constraints**                                                                                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Range**                                                                                               |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **searchTool**: Configures listeners for Elasticsearch or OpenSearch.                                   |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Default Value**                                                                                       |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **searchTool**                                                                                          |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | elb_id                | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Load balancer ID.     |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A.                  |
   +-----------------------+-----------------------+-----------------------+

Example Requests
----------------

Configure ELB listeners for a cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/es-listeners

   {
     "protocol" : "HTTPS",
     "protocol_port" : 9200,
     "server_cert_id" : "1b74ae4afad741e6bc9497429d3d0838",
     "ca_cert_id" : "2a7b050f598e4ea8a61cffbe2bdb312f"
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "elb_id" : "56a83547-a55a-407a-8245-7f9b3a0606c0"
   }

Status Codes
------------

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                      |
+===================================+==================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | Modify the request instead of retrying.                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | This status code indicates that the resource that the client attempts to create already exits, or the requested update failed due to a conflict. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
