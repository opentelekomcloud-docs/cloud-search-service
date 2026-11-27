:original_name: UpdateClusterName.html

.. _UpdateClusterName:

Modifying the Name or Description of a Cluster
==============================================

Function
--------

This API is used to change the cluster name or description.

Constraints
-----------

The name change here does not affect the cluster's underlying name.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/changename

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Range**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                          |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default Value**                                                                                                                |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Cluster ID. It can be obtained by calling the :ref:`Obtaining the Cluster ID <css_03_0101>` API.                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Modifying the cluster name or description is independent of the cluster status.                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Range**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | UUID format, 36 characters.                                                                                                      |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default Value**                                                                                                                |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                |
   +=================+=================+=================+============================================================================================================================+
   | display_name    | Yes             | String          | **Definition**                                                                                                             |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | Modified cluster name.                                                                                                     |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | **Constraints**                                                                                                            |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                        |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | **Range**                                                                                                                  |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | 4 to 64 characters. Only digits, letters, hyphens (-), and underscores (_) are allowed. The name must start with a letter. |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | **Default Value**                                                                                                          |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                        |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+
   | desc            | No              | String          | **Definition**                                                                                                             |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | Cluster description.                                                                                                       |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | **Constraints**                                                                                                            |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                        |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | **Range**                                                                                                                  |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | Up to 128 characters. Only letters, hyphens (-), underscores (_), punctuation marks, and brackets are allowed.             |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | **Default Value**                                                                                                          |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                        |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

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
