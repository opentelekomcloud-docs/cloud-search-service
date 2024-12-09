:original_name: css_03_0090.html

.. _css_03_0090:

Replacing a Node
================

Function
--------

This API is used to replace a failed node.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/instance/{instance_id}/replace

.. table:: **Table 1** Path parameters

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

Request Example
---------------

.. code-block:: text

   PUT /v1.0/{project_id}/clusters/{cluster_id}/instance/{instance_id}/replace

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-----------------------------------------+
| Status Code                       | Description                             |
+===================================+=========================================+
| 200                               | The request is processed successfully.  |
+-----------------------------------+-----------------------------------------+
| 400                               | Invalid request.                        |
|                                   |                                         |
|                                   | Modify the request instead of retrying. |
+-----------------------------------+-----------------------------------------+
| 404                               | The requested resource cannot be found. |
|                                   |                                         |
|                                   | Modify the request instead of retrying. |
+-----------------------------------+-----------------------------------------+
