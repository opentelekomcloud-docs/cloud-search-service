:original_name: UpdatePublicKibanaWhitelist.html

.. _UpdatePublicKibanaWhitelist:

Modifying Kibana Public Access Control
======================================

Function
--------

This API is used to modify the Kibana access permission by modifying the Kibana whitelist.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/publickibana/whitelist/update

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                        |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | Project ID of the account.                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                     |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | ID of the cluster whose Kibana access permission you want to modify. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | Cluster ID.                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                                     |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                                                |
   +============+===========+========+============================================================================================================================================================+
   | white_list | Yes       | String | Whitelisted IP addresses or network segments that can access Kibana. Separate them with commas (,), and each IP address or network segment must be unique. |
   +------------+-----------+--------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

The latest whitelist.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/publickibana/whitelist/update

   {
     "white_list" : "192.168.0.21"
   }

Example Responses
-----------------

None

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
