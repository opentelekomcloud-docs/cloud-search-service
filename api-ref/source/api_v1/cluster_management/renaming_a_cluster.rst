:original_name: UpdateClusterName.html

.. _UpdateClusterName:

Renaming a Cluster
==================

Function
--------

This API is used to change cluster names.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/changename

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                  |
   +=================+=================+=================+==============================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                              |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.             |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | **Constraints**:                                                                                                                             |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | **Value range**:                                                                                                                             |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | Project ID of the account.                                                                                                                   |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | **Default value**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                          |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                              |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | ID of the cluster that you want to rename For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | **Constraints**:                                                                                                                             |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | **Value range**:                                                                                                                             |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | Cluster ID.                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | **Default value**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                          |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                    |
   +=================+=================+=================+================================================================================================================================================================+
   | display_name    | Yes             | String          | **Definition**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | New name of a cluster                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Constraints**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | display_name and desc cannot be null at the same time.                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Value range**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | The cluster name must start with a letter and can contain 4 to 32 characters. Only letters, digits, periods (.), hyphens (-), and underscores (_) are allowed. |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Default value**:                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | N/A                                                                                                                                                            |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | desc            | No              | String          | **Definition**:                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | Cluster description.                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Constraints**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | The value can contain up to 128 characters. display_name and desc cannot be null at the same time.                                                             |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Value range**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | N/A                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Default value**:                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | N/A                                                                                                                                                            |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Change the display name of the current cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/changename

   {
     "display_name" : "ES-Test-new",
     "desc" : "test1"
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
