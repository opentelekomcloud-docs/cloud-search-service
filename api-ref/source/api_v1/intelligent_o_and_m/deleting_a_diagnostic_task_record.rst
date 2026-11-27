:original_name: DeleteAiOps.html

.. _DeleteAiOps:

Deleting a Diagnostic Task Record
=================================

Function
--------

This API is used to delete a diagnostic task record.

It is available for Elasticsearch and OpenSearch.

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
   | project_id      | Yes             | String          | **Definition**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Range**                                                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                             |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default Value**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | ID of the cluster to be deleted. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Range**                                                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                       |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default Value**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | aiops_id        | Yes             | String          | **Definition**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Detection task ID. For details, see :ref:`Querying the List and Details of Intelligent O&M Diagnostic Tasks <listaiops>`.           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                       |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Range**                                                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default Value**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Delete a diagnostic task record.

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
