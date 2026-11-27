:original_name: ListSmnTopics.html

.. _ListSmnTopics:

Obtaining Available SMN Topics (Deprecated)
===========================================

Function
--------

This API is used to obtain available SMN topics.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/domains/{domain_id}/ai-ops/smn-topics

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                               |
   +=================+=================+=================+===========================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                            |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | Project ID. For details about how to obtain it, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | **Constraints**                                                                                           |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | N/A                                                                                                       |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | **Range**                                                                                                 |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.   |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | **Default Value**                                                                                         |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | N/A                                                                                                       |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------+
   | domain_id       | Yes             | String          | **Definition**                                                                                            |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | Account ID. For details about how to obtain it, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | **Constraints**                                                                                           |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | N/A                                                                                                       |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | **Range**                                                                                                 |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | N/A                                                                                                       |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | **Default Value**                                                                                         |
   |                 |                 |                 |                                                                                                           |
   |                 |                 |                 | N/A                                                                                                       |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | topicsName            | Array of strings      | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Topic name.           |
   +-----------------------+-----------------------+-----------------------+

Example Requests
----------------

Obtain available SMN topics.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/domains/{domain_id}/ai-ops/smn-topics

Example Responses
-----------------

**Status code: 200**

.. code-block::

   {
     "topicsName" : [ "aiops-test" ]
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
