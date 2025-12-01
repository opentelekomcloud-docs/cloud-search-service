:original_name: DeleteAiOps.html

.. _DeleteAiOps:

Deleting a Detection Task
=========================

Function
--------

This API is used to delete a detection task.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

DELETE /v1.0/{project_id}/clusters/{cluster_id}/ai-ops/{aiops_id}

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                         |
   +=================+=================+=================+=====================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Value range**:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Project ID of the account.                                                                                                          |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default value**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | ID of the cluster to be deleted. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Value range**:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Cluster ID.                                                                                                                         |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default value**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | aiops_id        | Yes             | String          | ID of a detection task                                                                                                              |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Delete a detection task.

.. code-block:: text

   DELETE https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops/e19c9298-465e-42ad-a0ae-b6b552222925

Example Responses
-----------------

None

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
