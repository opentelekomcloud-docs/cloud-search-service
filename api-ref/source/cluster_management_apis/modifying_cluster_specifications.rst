:original_name: css_03_0086.html

.. _css_03_0086:

Modifying Cluster Specifications
================================

Function
--------

This API is used to modify the specifications of a cluster. Only the specifications of ESS nodes can be modified.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/flavor

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to modify specifications                           |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter        | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                       |
   +==================+=================+=================+===================================================================================================================================================================================================================================================================================================================================================+
   | needCheckReplica | No              | Boolean         | Indicates whether to verify replicas. Its value can be **true** or **false**. Replica verification is enabled by default.                                                                                                                                                                                                                         |
   |                  |                 |                 |                                                                                                                                                                                                                                                                                                                                                   |
   |                  |                 |                 | -  **true**: Replica verification is enabled.                                                                                                                                                                                                                                                                                                     |
   |                  |                 |                 | -  **false**: Replica verification is disabled.                                                                                                                                                                                                                                                                                                   |
   +------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | newFlavorId      | Yes             | String          | ID of the new flavor. This parameter is obtained by calling the :ref:`Obtaining the Instance Specifications List <listflavors>` API. The API compares the values of the **name** attribute and obtains the ID of the flavor higher than the current flavor. Only the node specifications of the same Elasticsearch engine version can be changed. |
   +------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

-  .. code-block::

      {
        "needCheckReplica" : false,
        "newFlavorId" : "35b060a4-f152-48ce-8773-36559ceb81f2",
        "isAutoPay" : 1
      }

-  .. code-block::

      {
        "needCheckReplica" : false,
        "newFlavorId" : "35b060a4-f152-48ce-8773-36559ceb81f2"
      }

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                         |
+===================================+=====================================================================================================================================================================================+
| 200                               | The request is processed successfully.                                                                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                    |
|                                   |                                                                                                                                                                                     |
|                                   | Modify the request instead of retrying.                                                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                                                                  |
|                                   |                                                                                                                                                                                     |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request fails to be processed because of the update of the conflict request. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
