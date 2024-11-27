:original_name: UpdateInstance.html

.. _UpdateInstance:

Replacing a Node
================

Function
--------

This API is used to replace a failed node.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/instance/{instance_id}/replace

.. table:: **Table 1** Path Parameters

   +-------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter   | Mandatory | Type   | Description                                                                                                                      |
   +=============+===========+========+==================================================================================================================================+
   | project_id  | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +-------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id  | Yes       | String | ID of the cluster where nodes are to be replaced                                                                                 |
   +-------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | instance_id | Yes       | String | ID of the node to be replaced                                                                                                    |
   +-------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                   |
   +=================+=================+=================+===============================================================+
   | migrateData     | No              | String          | Indicates whether to migrate data. The default value is true. |
   |                 |                 |                 |                                                               |
   |                 |                 |                 | -  "true": Migrate data.                                      |
   |                 |                 |                 |                                                               |
   |                 |                 |                 | -  "false": Do not migrate data.                              |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------+
   | agency          | No              | String          | Agency name, which is delegated to CSS.                       |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Example Requests
----------------

.. code-block:: text

   PUT /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/instance/43e63449-339c-4280-a6e9-da36b0685995/replace?migrateData=true

Example Responses
-----------------

None

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
|                                   | The client should modify the request instead of re-initiating it. |
+-----------------------------------+-------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
