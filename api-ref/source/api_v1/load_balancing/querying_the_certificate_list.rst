:original_name: ListElbCerts.html

.. _ListElbCerts:

Querying the Certificate List
=============================

Function
--------

This API is used to query the certificate list.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/elb/certificates

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Project ID of the account.                                                                                                              |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | ID of the cluster you want to query. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Cluster ID.                                                                                                                             |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+--------------------------------------------------------------------------------------------+-------------------------------+
   | Parameter             | Type                                                                                       | Description                   |
   +=======================+============================================================================================+===============================+
   | certificates          | Array of :ref:`CertificatesResource <listelbcerts__response_certificatesresource>` objects | **Definition**:               |
   |                       |                                                                                            |                               |
   |                       |                                                                                            | Certificate list information. |
   |                       |                                                                                            |                               |
   |                       |                                                                                            | **Value range**:              |
   |                       |                                                                                            |                               |
   |                       |                                                                                            | N/A                           |
   +-----------------------+--------------------------------------------------------------------------------------------+-------------------------------+

.. _listelbcerts__response_certificatesresource:

.. table:: **Table 3** CertificatesResource

   +-----------------------+-----------------------+------------------------------------+
   | Parameter             | Type                  | Description                        |
   +=======================+=======================+====================================+
   | id                    | String                | **Definition**:                    |
   |                       |                       |                                    |
   |                       |                       | Certificate ID.                    |
   |                       |                       |                                    |
   |                       |                       | **Value range**:                   |
   |                       |                       |                                    |
   |                       |                       | N/A                                |
   +-----------------------+-----------------------+------------------------------------+
   | name                  | String                | **Definition**:                    |
   |                       |                       |                                    |
   |                       |                       | Certificate name.                  |
   |                       |                       |                                    |
   |                       |                       | **Value range**:                   |
   |                       |                       |                                    |
   |                       |                       | N/A                                |
   +-----------------------+-----------------------+------------------------------------+
   | type                  | String                | **Definition**:                    |
   |                       |                       |                                    |
   |                       |                       | Type of the SL certificate.        |
   |                       |                       |                                    |
   |                       |                       | **Value range**:                   |
   |                       |                       |                                    |
   |                       |                       | -  **server**: server certificates |
   |                       |                       |                                    |
   |                       |                       | -  **client**: CA certificates     |
   +-----------------------+-----------------------+------------------------------------+

Example Requests
----------------

This API is used to query the certificate list.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/58ee0f27-70b3-47e0-ac72-9e3df6cd15cd/elb/certificates

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "certificates" : [ {
       "id" : "8c415d2e2f4c4fdbbfc9c21c98d7832b",
       "name" : "server1",
       "type" : "server"
     }, {
       "id" : "8c415d2e2f4c4fdbbfc9c21c98d7832b",
       "name" : "ca1",
       "type" : "client"
     }, {
       "id" : "8c415d2e2f4c4fdbbfc9c21c98d7832b",
       "name" : "server-css",
       "type" : "server"
     } ]
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
