:original_name: ResetPassword.html

.. _ResetPassword:

Changing the Password of a Cluster
==================================

Function
--------

This API is used to change cluster passwords to enhance cluster security.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/password/reset

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | Project ID of the account.                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | ID of the cluster whose password you want to change. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | Cluster ID.                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                |
   +=================+=================+=================+============================================================================================================================================+
   | newpassword     | Yes             | String          | **Definition**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | Password of the administrator admin for a security-mode cluster.                                                                           |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Constraints**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | This API is available only when **authorityEnable** is set to **true** during cluster creation.                                            |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Value range**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | -  Must contain 8 to 32 characters.                                                                                                        |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | -  Must contain at least three of the following character types: letters, digits, and special characters ``~!@#$%^&*()-_=+\|[{}];:,<.>/?`` |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | -  Do not use the administrator name, or the administrator name spelled backwards, as the password.                                        |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Default value**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                        |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Change the administrator password of the current cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/password/reset

   {
     "newpassword" : "xxxxxx"
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
