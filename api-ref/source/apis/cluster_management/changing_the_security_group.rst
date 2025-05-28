:original_name: ChangeSecurityGroup.html

.. _ChangeSecurityGroup:

Changing the Security Group
===========================

Function
--------

This API is used to change the security group after a cluster is created.

.. note::

   Before changing the security group, ensure that port 9200 has been enabled. Incorrect security group configuration may cause service access failures. Exercise caution when performing this operation.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/sg/change

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | Cluster ID.                                                                                                                      |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   ================== ========= ====== ==================
   Parameter          Mandatory Type   Description
   ================== ========= ====== ==================
   security_group_ids Yes       String Security group ID.
   ================== ========= ====== ==================

Response Parameters
-------------------

None

Example Requests
----------------

Change the security group that the current cluster belongs to.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/sg/change

   {
     "security_group_ids" : "b1038649-1f77-4ae9-b64d-9af56e422652"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                           |
+===================================+=======================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                      |
|                                   |                                                                                                                                                                       |
|                                   | The client should not repeat the request without modifications.                                                                                                       |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
