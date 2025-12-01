:original_name: DeleteClustersTags.html

.. _DeleteClustersTags:

Deleting a Cluster Tag
======================

Function
--------

Tags are cluster identifiers. You can add tags to clusters to identify and manage cluster resources.

You can add tags to a cluster when creating a cluster or add them on the details page of a created cluster.

This API is used to delete cluster tags. You can delete unnecessary cluster tags to facilitate cluster management.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

DELETE /v1.0/{project_id}/{resource_type}/{cluster_id}/tags/{key}

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
   |                 |                 |                 | ID of the cluster that you want to delete tags from. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
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
   | resource_type   | Yes             | String          | **Definition**:                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | Resource type. Currently, its value can only be **css-cluster**.                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | css-cluster: Indicates the cluster type.                                                                                                                |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+
   | key             | Yes             | String          | **Definition**:                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | Name of the tag you want to delete                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | If the tag name is in Chinese, encode the tag name using URL before calling the API.                                                                    |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 204**

Request succeeded.

None

Example Requests
----------------

Delete the tags of a cluster.

.. code-block:: text

   DELETE https://{Endpoint}/v1.0/{project_id}/css-cluster/2a197c4d-5467-4003-931d-83ec49939cf/tags/K1

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------+
| Status Code                       | Description                                                       |
+===================================+===================================================================+
| 204                               | Request succeeded.                                                |
+-----------------------------------+-------------------------------------------------------------------+
| 400                               | Invalid request.                                                  |
|                                   |                                                                   |
|                                   | The client should modify the request instead of re-initiating it. |
+-----------------------------------+-------------------------------------------------------------------+
| 404                               | The requested resource could not be found.                        |
|                                   |                                                                   |
|                                   | The client should not repeat the request without modifications.   |
+-----------------------------------+-------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
