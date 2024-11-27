:original_name: UpdateBatchClustersTags.html

.. _UpdateBatchClustersTags:

Adding or Deleting Cluster Tags in Batches
==========================================

Function
--------

This API is used to add tags to or delete tags from a cluster in batches.

URI
---

POST /v1.0/{project_id}/{resource_type}/{cluster_id}/tags/action

.. table:: **Table 1** Path Parameters

   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter     | Mandatory | Type   | Description                                                                                                                      |
   +===============+===========+========+==================================================================================================================================+
   | project_id    | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id    | Yes       | String | ID of the cluster that you want to add tags to or delete tags from in batches.                                                   |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | resource_type | Yes       | String | Resource type. Currently, its value can only be **css-cluster**.                                                                 |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                       | Description                                                                        |
   +=================+=================+============================================================================+====================================================================================+
   | action          | Yes             | String                                                                     | Action type. This attribute is used to identify the required operation type.       |
   |                 |                 |                                                                            |                                                                                    |
   |                 |                 |                                                                            | -  **create**: Tags are added in batches.                                          |
   |                 |                 |                                                                            |                                                                                    |
   |                 |                 |                                                                            | -  **delete**: Tags are deleted in batches.                                        |
   +-----------------+-----------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------+
   | tags            | Yes             | Array of :ref:`Tag <updatebatchclusterstags__request_tag>` objects         | Tag list.                                                                          |
   +-----------------+-----------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------+
   | sysTags         | No              | Array of :ref:`SysTags <updatebatchclusterstags__request_systags>` objects | System tag list.                                                                   |
   |                 |                 |                                                                            |                                                                                    |
   |                 |                 |                                                                            | -  The value of **key** is fixed to **\_sys_enterprise_project_id**.               |
   |                 |                 |                                                                            |                                                                                    |
   |                 |                 |                                                                            | -  The value is **UUID** or **0**. **0** indicates the default enterprise project. |
   +-----------------+-----------------+----------------------------------------------------------------------------+------------------------------------------------------------------------------------+

.. _updatebatchclusterstags__request_tag:

.. table:: **Table 3** Tag

   ========= ========= ====== ===========
   Parameter Mandatory Type   Description
   ========= ========= ====== ===========
   key       Yes       String Tag name.
   value     Yes       String Tag value.
   ========= ========= ====== ===========

.. _updatebatchclusterstags__request_systags:

.. table:: **Table 4** SysTags

   ========= ========= ====== ===========
   Parameter Mandatory Type   Description
   ========= ========= ====== ===========
   key       Yes       String Tag name.
   value     Yes       String Tag value.
   ========= ========= ====== ===========

Response Parameters
-------------------

None

Example Requests
----------------

Create or delete cluster tags in batches.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/css-cluster/4f3deec3-efa8-4598-bf91-560aad1377a3/tags/action

   {
     "action" : "create",
     "tags" : [ {
       "key" : "K1",
       "value" : "V1"
     }, {
       "key" : "K2",
       "value" : "V2"
     } ]
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                         |
+===================================+=====================================================================================================================================================================================+
| 204                               | Request succeeded.                                                                                                                                                                  |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                    |
|                                   |                                                                                                                                                                                     |
|                                   | Do not retry the request before modification.                                                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                                                                        |
|                                   |                                                                                                                                                                                     |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request fails to be processed because of the update of the conflict request. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                                                                          |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
