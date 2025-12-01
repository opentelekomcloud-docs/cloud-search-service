:original_name: CreateClustersTags.html

.. _CreateClustersTags:

Adding Tags to a Cluster
========================

Function
--------

Tags are cluster identifiers. You can add tags to clusters to identify and manage cluster resources.

You can add tags to a cluster when creating a cluster or add them on the details page of a created cluster.

This API is used to add tags to a cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/{resource_type}/{cluster_id}/tags

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                        |
   +=================+=================+=================+====================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Project ID of the account.                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | ID of the cluster that you want to add tags to. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Cluster ID.                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | resource_type   | Yes             | String          | **Definition**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Resource type. Currently, its value can only be **css-cluster**.                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | css-cluster: Indicates the cluster type.                                                                                                           |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------------------------------------------+-----------------------------+
   | Parameter       | Mandatory       | Type                                                | Description                 |
   +=================+=================+=====================================================+=============================+
   | tag             | Yes             | :ref:`Tag <createclusterstags__request_tag>` object | **Definition**:             |
   |                 |                 |                                                     |                             |
   |                 |                 |                                                     | Tag object you want to add. |
   |                 |                 |                                                     |                             |
   |                 |                 |                                                     | **Constraints**:            |
   |                 |                 |                                                     |                             |
   |                 |                 |                                                     | N/A                         |
   |                 |                 |                                                     |                             |
   |                 |                 |                                                     | **Value range**:            |
   |                 |                 |                                                     |                             |
   |                 |                 |                                                     | N/A                         |
   |                 |                 |                                                     |                             |
   |                 |                 |                                                     | **Default value**:          |
   |                 |                 |                                                     |                             |
   |                 |                 |                                                     | N/A                         |
   +-----------------+-----------------+-----------------------------------------------------+-----------------------------+

.. _createclusterstags__request_tag:

.. table:: **Table 3** Tag

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                    |
   +=================+=================+=================+================================================================================================+
   | key             | Yes             | String          | **Definition**:                                                                                |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | Tag key.                                                                                       |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | **Constraints**:                                                                               |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | -  The key cannot be empty. Its length is 1 to 128 characters.                                 |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | -  The value can contain UTF-8 letters, digits, spaces, and special characters \_ . : = + - @. |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | -  Tags starting with *sys* are system tags and cannot be used by tenants.                     |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | -  Do not use spaces to start or end the key.                                                  |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | **Value range**:                                                                               |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | N/A                                                                                            |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | **Default value**:                                                                             |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | N/A                                                                                            |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------+
   | value           | Yes             | String          | **Definition**:                                                                                |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | Tag value.                                                                                     |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | **Constraints**:                                                                               |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | -  The value contains 0 to 255 characters.                                                     |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | -  The value can contain UTF-8 letters, digits, spaces, and special characters ``_.://=+-@``   |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | **Value range**:                                                                               |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | N/A                                                                                            |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | **Default value**:                                                                             |
   |                 |                 |                 |                                                                                                |
   |                 |                 |                 | N/A                                                                                            |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 204**

Request succeeded.

None

Example Requests
----------------

Add tags to a cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/css-cluster/4f3deec3-efa8-4598-bf91-560aad1377a3/tags

   {
     "tag" : {
       "key" : "K1",
       "value" : "V1"
     }
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                      |
+===================================+==================================================================================================================================================+
| 204                               | Request succeeded.                                                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | The client should modify the request instead of re-initiating it.                                                                                |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                                     |
|                                   |                                                                                                                                                  |
|                                   | This status code indicates that the resource that the client attempts to create already exits, or the requested update failed due to a conflict. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
