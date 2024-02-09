:original_name: css_03_0090.html

.. _css_03_0090:

Replacing a Node
================

Function
--------

This API is used to replace a failed node.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/instance/{instance_id}/replace

.. table:: **Table 1** Path Parameters

   +-------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter   | Mandatory | Type   | Description                                                                        |
   +=============+===========+========+====================================================================================+
   | project_id  | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +-------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id  | Yes       | String | ID of the cluster where nodes are to be replaced                                   |
   +-------------+-----------+--------+------------------------------------------------------------------------------------+
   | instance_id | Yes       | String | ID of the node to be replaced                                                      |
   +-------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Example Requests
----------------

.. code-block:: text

   PUT /v1.0/{project_id}/clusters/{cluster_id}/instance/{instance_id}/replace

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
