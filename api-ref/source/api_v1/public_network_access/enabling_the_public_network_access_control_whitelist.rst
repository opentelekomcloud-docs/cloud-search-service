:original_name: StartPublicWhitelist.html

.. _StartPublicWhitelist:

Enabling the Public Network Access Control Whitelist
====================================================

Function
--------

If public network access is enabled for a cluster, you can use this API to configure a whitelist for public network access control.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/public/whitelist/update

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Value range**:                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | Project ID of the account.                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Default value**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | ID of the cluster whose public network access control whitelist you want to enable. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Value range**:                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | Cluster ID.                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | **Default value**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                   |
   +=================+=================+=================+===============================================================================================================================================================+
   | white_list      | Yes             | String          | **Definition**                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Public access control whitelist. Add the IP addresses or CIDR blocks to be whitelisted, separated by commas (,). Valid examples: **192.168.1.1,10.0.0.0/24**. |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Constraints**                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | The following are not supported: 0.0.0.0,x.x.x.x/0, non-standard formats such as 192.168.1, or duplicate entries.                                             |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Range**                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Valid CIDR blocks or IP addresses.                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Default Value**                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Enable the public network access control whitelist.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/public/whitelist/update

   {
     "white_list" : "192.168.0.1"
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
