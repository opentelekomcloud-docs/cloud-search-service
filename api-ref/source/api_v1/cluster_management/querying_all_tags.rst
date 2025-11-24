:original_name: ListClustersTags.html

.. _ListClustersTags:

Querying All Tags
=================

Function
--------

This API is used to query all tags of a user in the current project, including the keys and values. This facilitates tag management by group.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/{resource_type}/tags

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID.                                                                                                                      |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | resource_type   | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Resource type. Currently, its value can only be **css-cluster**.                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | css-cluster: Indicates the cluster type.                                                                                         |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+----------------------------------------------------------------------------------------------+-----------------------+
   | Parameter             | Type                                                                                         | Description           |
   +=======================+==============================================================================================+=======================+
   | tags                  | Array of :ref:`ShowAllTagsTagsResp <listclusterstags__response_showalltagstagsresp>` objects | **Definition**:       |
   |                       |                                                                                              |                       |
   |                       |                                                                                              | List of cluster tags. |
   |                       |                                                                                              |                       |
   |                       |                                                                                              | **Value range**:      |
   |                       |                                                                                              |                       |
   |                       |                                                                                              | N/A                   |
   +-----------------------+----------------------------------------------------------------------------------------------+-----------------------+

.. _listclusterstags__response_showalltagstagsresp:

.. table:: **Table 3** ShowAllTagsTagsResp

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | key                   | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Tag key.              |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+
   | values                | Array of strings      | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Tag values.           |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+

Example Requests
----------------

Query all cluster tags in a project.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/css-cluster/tags

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "tags" : [ {
       "key" : "key1",
       "values" : [ "value1", "value2" ]
     }, {
       "key" : "key2",
       "values" : [ "value1", "value2" ]
     } ]
   }

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------+
| Status Code                       | Description                                                       |
+===================================+===================================================================+
| 200                               | Request succeeded.                                                |
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
