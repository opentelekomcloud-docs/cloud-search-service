:original_name: ChangeMode.html

.. _ChangeMode:

Configuring the Security Mode.
==============================

Function
--------

This API is used to configure the security mode of a cluster. The security mode settings for clusters include:

-  Security mode + HTTP: strikes a balance between performance and security. Make sure the cluster is deployed in a secure environment. Do not expose the cluster's network interface to the public network.

-  Security mode + HTTPS: prioritizes security and in-transit data encryption, and allows public network access.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/mode/change

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
   |                 |                 |                 | ID of the target cluster For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.      |
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

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter        | Mandatory       | Type            | Description                                                                                                                                                               |
   +==================+=================+=================+===========================================================================================================================================================================+
   | authority_enable | Yes             | Boolean         | **Definition**:                                                                                                                                                           |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | Whether to enable the security mode for the cluster.                                                                                                                      |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Constraints**:                                                                                                                                                          |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | Only Elasticsearch 6.5.4 security-mode clusters and later support this parameter.                                                                                         |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Value range**:                                                                                                                                                          |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | -  true: enable.                                                                                                                                                          |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | -  false: disable.                                                                                                                                                        |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Default value**:                                                                                                                                                        |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | true                                                                                                                                                                      |
   +------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | admin_pwd        | No              | String          | **Definition**:                                                                                                                                                           |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | Cluster password in security mode.                                                                                                                                        |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Constraints**:                                                                                                                                                          |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | Only Elasticsearch 6.5.4 security-mode clusters and later support this parameter.                                                                                         |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Value range**:                                                                                                                                                          |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | N/A                                                                                                                                                                       |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Default value**:                                                                                                                                                        |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | N/A                                                                                                                                                                       |
   +------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | https_enable     | Yes             | Boolean         | **Definition**:                                                                                                                                                           |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | Whether to enable HTTPS for the cluster.                                                                                                                                  |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Constraints**:                                                                                                                                                          |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | -  Elasticsearch: Only Elasticsearch 6.5.4 and later versions support security-mode clusters.                                                                             |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | -  HTTPS access can be disabled only for OpenSearch 1.3.6 and 2.19.0 security-mode clusters. For other versions, HTTPS access is forcibly enabled and cannot be disabled. |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | -  true: Enable HTTPS.                                                                                                                                                    |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | -  false: Disable HTTPS.                                                                                                                                                  |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Value range**:                                                                                                                                                          |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | **Default value**:                                                                                                                                                        |
   |                  |                 |                 |                                                                                                                                                                           |
   |                  |                 |                 | true                                                                                                                                                                      |
   +------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Change the security mode of the current cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/mode/change

   {
     "authority_enable" : true,
     "admin_pwd" : "admin@1234",
     "https_enable" : true
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+--------------------------------------------+
| Status Code                       | Description                                |
+===================================+============================================+
| 200                               | Request succeeded.                         |
+-----------------------------------+--------------------------------------------+
| 400                               | Invalid request.                           |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+
| 404                               | The requested resource could not be found. |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
