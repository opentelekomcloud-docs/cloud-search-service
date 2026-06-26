:original_name: UpdateESListener.html

.. _UpdateESListener:

Updating Load Balancing Listeners for a Cluster
===============================================

Function
--------

CSS can interconnect with ELB. This API is used to update the configuration of load balancer listeners for clusters.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/es-listeners/{listener_id}

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID of the account.                                                                                                       |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | ID of the target cluster. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.     |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Cluster ID.                                                                                                                      |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | listener_id     | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | ID of the target listener.                                                                                                       |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                          | Description                                                                      |
   +=================+=================+===============================================================================+==================================================================================+
   | listener        | Yes             | :ref:`EsListenerRequest <updateeslistener__request_eslistenerrequest>` object | **Definition**:                                                                  |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | Listener information.                                                            |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | **Constraints**:                                                                 |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | N/A.                                                                             |
   +-----------------+-----------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------+
   | type            | No              | String                                                                        | **Definition**                                                                   |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | Configuration type.                                                              |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | **Constraints**                                                                  |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | N/A                                                                              |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | **Range**                                                                        |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | **searchTool**: Modifies the Elasticsearch or OpenSearch listener configuration. |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | **Default Value**                                                                |
   |                 |                 |                                                                               |                                                                                  |
   |                 |                 |                                                                               | **searchTool**                                                                   |
   +-----------------+-----------------+-------------------------------------------------------------------------------+----------------------------------------------------------------------------------+

.. _updateeslistener__request_eslistenerrequest:

.. table:: **Table 3** EsListenerRequest

   +-----------------------------+-----------------+-----------------+-----------------------------------------------------+
   | Parameter                   | Mandatory       | Type            | Description                                         |
   +=============================+=================+=================+=====================================================+
   | default_tls_container_ref   | Yes             | String          | **Definition**                                      |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | ID of the server certificate used by the listener.  |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | **Constraints**                                     |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | This is mandatory for HTTPS authentication.         |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | **Range**                                           |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | N/A                                                 |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | **Default Value**                                   |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | N/A                                                 |
   +-----------------------------+-----------------+-----------------+-----------------------------------------------------+
   | client_ca_tls_container_ref | No              | String          | **Definition**                                      |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | ID of the CA certificate used by the listener.      |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | **Constraints**                                     |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | This is mandatory for HTTPS two-way authentication. |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | **Range**                                           |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | N/A                                                 |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | **Default Value**                                   |
   |                             |                 |                 |                                                     |
   |                             |                 |                 | N/A                                                 |
   +-----------------------------+-----------------+-----------------+-----------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 4** Response body parameters

   +-----------------------+----------------------------------------------------------------------------------+-----------------------+
   | Parameter             | Type                                                                             | Description           |
   +=======================+==================================================================================+=======================+
   | listener              | :ref:`EsListenerResponse <updateeslistener__response_eslistenerresponse>` object | **Definition**:       |
   |                       |                                                                                  |                       |
   |                       |                                                                                  | Listener object.      |
   +-----------------------+----------------------------------------------------------------------------------+-----------------------+

.. _updateeslistener__response_eslistenerresponse:

.. table:: **Table 5** EsListenerResponse

   +-----------------------------+--------------------------------------------------------------------------------+----------------------------------------------------+
   | Parameter                   | Type                                                                           | Description                                        |
   +=============================+================================================================================+====================================================+
   | protocol                    | String                                                                         | **Definition**:                                    |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | Protocol used by the listener.                     |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | **Value range**:                                   |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | N/A.                                               |
   +-----------------------------+--------------------------------------------------------------------------------+----------------------------------------------------+
   | id                          | String                                                                         | **Definition**:                                    |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | Listener ID.                                       |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | **Value range**:                                   |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | N/A.                                               |
   +-----------------------------+--------------------------------------------------------------------------------+----------------------------------------------------+
   | name                        | String                                                                         | **Definition**:                                    |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | Listener name.                                     |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | **Value range**:                                   |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | N/A.                                               |
   +-----------------------------+--------------------------------------------------------------------------------+----------------------------------------------------+
   | protocol_port               | String                                                                         | **Definition**:                                    |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | Port used by the listener.                         |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | **Value range**:                                   |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | N/A.                                               |
   +-----------------------------+--------------------------------------------------------------------------------+----------------------------------------------------+
   | default_tls_container_ref   | String                                                                         | **Definition**                                     |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | ID of the server certificate used by the listener. |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | **Range**                                          |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | N/A                                                |
   +-----------------------------+--------------------------------------------------------------------------------+----------------------------------------------------+
   | client_ca_tls_container_ref | String                                                                         | **Definition**                                     |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | ID of the CA certificate used by the listener.     |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | **Range**                                          |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | N/A                                                |
   +-----------------------------+--------------------------------------------------------------------------------+----------------------------------------------------+
   | ipgroup                     | :ref:`EsIpgroupResource <updateeslistener__response_esipgroupresource>` object | **Definition**:                                    |
   |                             |                                                                                |                                                    |
   |                             |                                                                                | Access control information of the listener object. |
   +-----------------------------+--------------------------------------------------------------------------------+----------------------------------------------------+

.. _updateeslistener__response_esipgroupresource:

.. table:: **Table 6** EsIpgroupResource

   +-----------------------+-----------------------+------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                              |
   +=======================+=======================+==========================================================================================+
   | ipgroup_id            | String                | **Definition**:                                                                          |
   |                       |                       |                                                                                          |
   |                       |                       | ID of the access control group associated with the listener.                             |
   |                       |                       |                                                                                          |
   |                       |                       | **Value range**:                                                                         |
   |                       |                       |                                                                                          |
   |                       |                       | N/A                                                                                      |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------+
   | enable_ipgroup        | Boolean               | **Definition**:                                                                          |
   |                       |                       |                                                                                          |
   |                       |                       | Status of an access control group.                                                       |
   |                       |                       |                                                                                          |
   |                       |                       | **Value range**:                                                                         |
   |                       |                       |                                                                                          |
   |                       |                       | -  true: Enable the access control listener (which can be deleted directly).             |
   |                       |                       |                                                                                          |
   |                       |                       | -  false: Disable the access control listener.                                           |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------+
   | type                  | String                | **Definition**:                                                                          |
   |                       |                       |                                                                                          |
   |                       |                       | Type of an access control group.                                                         |
   |                       |                       |                                                                                          |
   |                       |                       | **Value range**:                                                                         |
   |                       |                       |                                                                                          |
   |                       |                       | -  **white**: Configure a whitelist. Only IP addresses on the whitelist can have access. |
   |                       |                       |                                                                                          |
   |                       |                       | -  **black**: Configure a blacklist. IP addresses on the blacklist are blocked access.   |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------+

Example Requests
----------------

Update ELB listeners for a cluster.

.. code-block:: text

   PUT https://{Endpoint}/v1.0/{project_id}/clusters/58ee0f27-70b3-47e0-ac72-9e3df6cd15cd/es-listeners/4425eb63-78ce-4c63-b60e-492befdac0e7

   {
     "listener" : {
       "default_tls_container_ref" : "9c82320a8dd049eba49b28e70a2c0c3e"
     }
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "listener" : {
       "id" : "a21b50ec-9cd5-4495-9398-b24a7e9afe5b",
       "name" : "css-55b6-searchServer",
       "protocol" : "HTTPS",
       "ipgroup" : {
         "ipgroup_id" : "4f3deec3-efa8-4598-bf91-560aad1377a3",
         "enable_ipgroup" : true,
         "type" : "white"
       },
       "protocol_port" : 9200,
       "default_tls_container_ref" : "b5c45f342bcd435abc18760a13976a1d",
       "client_ca_tls_container_ref" : "4a2053a825a0471ba85a60468afa80cf"
     }
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
