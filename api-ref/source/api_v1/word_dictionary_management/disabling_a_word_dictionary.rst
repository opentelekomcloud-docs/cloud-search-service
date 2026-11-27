:original_name: DeleteIkThesaurus.html

.. _DeleteIkThesaurus:

Disabling a Word Dictionary
===========================

Function
--------

The word dictionaries of an Elasticsearch/OpenSearch cluster in CSS is used for word segmentation of text, enabling special words to be recognized during segmentation and facilitating text data search by keywords. For example, you can search by trending terms such as **xidapuben**. It also supports searching text data using synonyms based on a synonym dictionary.

This API is used to clear a custom word dictionary (main word dictionary, stop word dictionary, and synonym dictionary).

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

DELETE /v1.0/{project_id}/clusters/{cluster_id}/thesaurus

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                           |
   +=================+=================+=================+=======================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                      |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Constraints**                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Range**                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                                               |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Default Value**                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | ID of the cluster whose custom word dictionary you want to delete. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Constraints**                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Range**                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Default Value**                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Delete a custom word dictionary.

.. code-block:: text

   DELETE https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/thesaurus

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                          |
+===================================+======================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.                                                                                                                                    |
|                                   |                                                                                                                                                      |
|                                   | The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 500                               | The server is able to receive but unable to understand the request.                                                                                  |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
