:original_name: css_03_0092.html

.. _css_03_0092:

Changing the Security Group
===========================

Function
--------

This API is used to change the security group after a cluster is created.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/sg/change

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to change the security group                       |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   ================== ========= ====== =================
   Parameter          Mandatory Type   Description
   ================== ========= ====== =================
   security_group_ids Yes       String Security group ID
   ================== ========= ====== =================

Response Parameters
-------------------

None

Request Example
---------------

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/sg/change

   {
     "security_group_ids" : "b1038649-1f77-4ae9-b64d-9af56e42xxxx"
   }

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                            |
+===================================+========================================================================================================================================================================+
| 200                               | The request is processed successfully.                                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                       |
|                                   |                                                                                                                                                                        |
|                                   | Modify the request instead of retrying.                                                                                                                                |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | The request is rejected. The server has received and understood the request, but refused to respond to it. Modify the request directly and do not attempt to retry it. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
