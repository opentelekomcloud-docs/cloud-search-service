:original_name: ChangeClusterSubnet.html

.. _ChangeClusterSubnet:

Changing the Subnet of a Cluster
================================

Function
--------

If the subnet where the cluster resides does not have insufficient IP addresses and nodes cannot be added as a result, for example, during a cluster scale-out, you can use this API to switch to another subnet. After subnet switching, the new subnet will be used to create new nodes, but the subnet of existing nodes will remain unchanged.

.. note::

   By default, subnets with the same VPC are connected. Ensure that the new subnet can reach your service system. Note that a cluster with automatic IPv6 address creation enabled can only be switched to a new subnet that uses IPv6 addresses.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/subnet/change

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                         |
   +=================+=================+=================+=====================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                    |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | **Constraints**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | **Value range**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | Project ID of the account.                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | **Default value**:                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                                 |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | ID of the cluster whose subnet is to be changed. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | **Constraints**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | **Value range**:                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | Cluster ID.                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | **Default value**:                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                                 |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | subnet_id       | Yes             | String          | **Definition**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Subnet ID.                                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | If automatic IPv6 address assignment is enabled for the cluster, the cluster can only be switched to a new subnet with IPv6 enabled. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The subnet must be within the same VPC as the current cluster.                                                                       |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Change the subnet of a cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/subnet/change

   {
     "subnet_id" : "b1234567-1f77-4ae9-b64d-9af56e123456"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                          |
+===================================+======================================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                     |
|                                   |                                                                                                                                                                                      |
|                                   | Modify the request and then retry.                                                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be processed due to a conflict.                                                                                                                                |
|                                   |                                                                                                                                                                                      |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request failed to be processed because of the update of the conflict request. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the preconditions that the requester puts on the request.                                                                                            |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
