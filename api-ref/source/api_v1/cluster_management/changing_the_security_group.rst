:original_name: ChangeSecurityGroup.html

.. _ChangeSecurityGroup:

Changing the Security Group
===========================

Function
--------

This API is used to change the security group after a cluster is created.

Constraints
-----------

Make sure the security group allows port 9200 in the inbound direction. Incorrect security group configuration may make the cluster inaccessible. Exercise caution when performing this operation.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/sg/change

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                    |
   +=================+=================+=================+================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                               |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Constraints**                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | N/A                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Range**                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                                        |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Default Value**                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | N/A                                                                                                                                                            |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | ID of the cluster whose security group you want to change. It can be obtained by calling the :ref:`Obtaining the Cluster ID <css_03_0101>` API.                |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Constraints**                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | The cluster must be in the available state. Security group change is not supported when the cluster is in states such as creating, scaling out, or restarting. |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Range**                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | UUID format, 36 characters.                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | **Default Value**                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                |
   |                 |                 |                 | N/A                                                                                                                                                            |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +--------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter          | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                         |
   +====================+=================+=================+=====================================================================================================================================================================================================================================================================================+
   | security_group_ids | Yes             | String          | **Definition**                                                                                                                                                                                                                                                                      |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | Target security group ID. It can be obtained by calling the API. After the switch, the cluster will use the new security group rules, and the original security group rules will no longer take effect. Ensure that the new security group is configured with correct access rules. |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | **Constraints**                                                                                                                                                                                                                                                                     |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | -  Only one security group ID is supported.                                                                                                                                                                                                                                         |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | -  The target security group must be in the same VPC as the cluster, and necessary ports such as 9200 must be opened. Otherwise, the cluster may not be accessible after the switch.                                                                                                |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | **Range**                                                                                                                                                                                                                                                                           |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | UUID format, 36 characters.                                                                                                                                                                                                                                                         |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | **Default Value**                                                                                                                                                                                                                                                                   |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | N/A                                                                                                                                                                                                                                                                                 |
   +--------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Change the security group of a cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/sg/change

   {
     "security_group_ids" : "b1038649-1f77-4ae9-b64d-9af56e422652"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                          |
+===================================+======================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                     |
|                                   |                                                                                                                                                      |
|                                   | The client should not repeat the request without modifications.                                                                                      |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.                                                                                                                                    |
|                                   |                                                                                                                                                      |
|                                   | The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
