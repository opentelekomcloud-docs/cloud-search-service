:original_name: ShowClusterTag.html

.. _ShowClusterTag:

Querying Tags of a Specified Cluster
====================================

Function
--------

This API is used to query the tags of a specified cluster.

URI
---

GET /v1.0/{project_id}/{resource_type}/{cluster_id}/tags

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | ID of the cluster you want to query.                                                                                                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | resource_type   | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Resource type. Currently, its value can only be **css-cluster**.                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | css-cluster                                                                                                                          |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+--------------------------------------------------------------------------------------+----------------------------+
   | Parameter             | Type                                                                                 | Description                |
   +=======================+======================================================================================+============================+
   | tags                  | Array of :ref:`ShowTagsTagsResp <showclustertag__response_showtagstagsresp>` objects | **Parameter description**: |
   |                       |                                                                                      |                            |
   |                       |                                                                                      | List of cluster tags       |
   +-----------------------+--------------------------------------------------------------------------------------+----------------------------+

.. _showclustertag__response_showtagstagsresp:

.. table:: **Table 3** ShowTagsTagsResp

   +-----------------------+-----------------------+----------------------------+
   | Parameter             | Type                  | Description                |
   +=======================+=======================+============================+
   | key                   | String                | **Parameter description**: |
   |                       |                       |                            |
   |                       |                       | Tag key.                   |
   +-----------------------+-----------------------+----------------------------+
   | value                 | String                | **Parameter description**: |
   |                       |                       |                            |
   |                       |                       | Tag value.                 |
   +-----------------------+-----------------------+----------------------------+

Example Requests
----------------

Query the tags of a cluster.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/{resource_type}/{resource_id}/tags

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "tags" : [ {
       "key" : "key1",
       "value" : "value1"
     }, {
       "key" : "key2",
       "value" : "value3"
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
