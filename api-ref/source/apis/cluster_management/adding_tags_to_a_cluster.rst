:original_name: CreateClustersTags.html

.. _CreateClustersTags:

Adding Tags to a Cluster
========================

Function
--------

This API is used to add tags to a cluster.

URI
---

POST /v1.0/{project_id}/{resource_type}/{cluster_id}/tags

.. table:: **Table 1** Path Parameters

   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter     | Mandatory | Type   | Description                                                                                                                      |
   +===============+===========+========+==================================================================================================================================+
   | project_id    | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id    | Yes       | String | ID of the cluster that you want to add tags to.                                                                                  |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | resource_type | Yes       | String | Resource type. Currently, its value can only be **css-cluster**.                                                                 |
   +---------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+-----------------------------------------------------+-----------------------------+
   | Parameter | Mandatory | Type                                                | Description                 |
   +===========+===========+=====================================================+=============================+
   | tag       | Yes       | :ref:`Tag <createclusterstags__request_tag>` object | Tag object you want to add. |
   +-----------+-----------+-----------------------------------------------------+-----------------------------+

.. _createclusterstags__request_tag:

.. table:: **Table 3** Tag

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

Create a cluster tag.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/css-cluster/4f3deec3-efa8-4598-bf91-560aad1377a3/tags

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
