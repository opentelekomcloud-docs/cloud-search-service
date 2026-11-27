:original_name: UpdateShrinkCluster.html

.. _UpdateShrinkCluster:

Scaling In Nodes of a Specific Type
===================================

Function
--------

This API is used to scale in instances of different types and reduce the storage capacity of a cluster.

.. note::

   Before scaling in, back up all key data to prevent data loss.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/extend/{project_id}/clusters/{cluster_id}/role/shrink

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                           |
   +=================+=================+=================+=======================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.      |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Constraints**                                                                                                                       |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Range**                                                                                                                             |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                               |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Default Value**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | ID of the cluster to be scaled in. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Constraints**                                                                                                                       |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Range**                                                                                                                             |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                         |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Default Value**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | Parameter          | Mandatory       | Type                                                                               | Description                                                                                                          |
   +====================+=================+====================================================================================+======================================================================================================================+
   | shrink             | Yes             | Array of :ref:`ShrinkNodeReq <updateshrinkcluster__request_shrinknodereq>` objects | **Definition**                                                                                                       |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | Type and quantity of nodes you want to scale in.                                                                     |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Constraints**                                                                                                      |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | N/A                                                                                                                  |
   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | agency_name        | No              | String                                                                             | **Definition**                                                                                                       |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | Agency name, which is delegated to CSS to allow CSS to call your other cloud services.                               |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Constraints**                                                                                                      |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | -  The agency must have VPC operation permissions: "``vpc:subnets:get``","``vpc:ports:*``".                          |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | This parameter is mandatory when connected to the new IAM plane, and optional when connected to the old IAM plane.   |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Range**                                                                                                            |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | The agency name can contain up to 64 characters. Only letters, digits, underscores (_), and hyphens (-) are allowed. |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Default Value**                                                                                                    |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | N/A                                                                                                                  |
   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | operation_type     | No              | String                                                                             | **Definition**                                                                                                       |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | Scale-in type.                                                                                                       |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Constraints**                                                                                                      |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | N/A                                                                                                                  |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Range**                                                                                                            |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **vm**: Reduce nodes.                                                                                                |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Default Value**                                                                                                    |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **vm**                                                                                                               |
   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | cluster_load_check | No              | Boolean                                                                            | **Definition**:                                                                                                      |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | Whether to check the cluster load.                                                                                   |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Constraints**:                                                                                                     |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | N/A                                                                                                                  |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Value range**:                                                                                                     |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | -  **true**: enable cluster load check.                                                                              |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | -  **true**: skip cluster load check.                                                                                |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | **Default value**:                                                                                                   |
   |                    |                 |                                                                                    |                                                                                                                      |
   |                    |                 |                                                                                    | true                                                                                                                 |
   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

.. _updateshrinkcluster__request_shrinknodereq:

.. table:: **Table 3** ShrinkNodeReq

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                               |
   +=================+=================+=================+===========================================================================================================================================================================================================================================================================================================================================+
   | reducedNodeNum  | Yes             | Integer         | **Definition**                                                                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | Number of nodes to be scaled in.                                                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | **Constraints**                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  After the scale-in, there must be at least one instance for each node type in each AZ. For cross-AZ clusters, the number of same-type nodes in different AZs must not differ by more than 1. For clusters with two AZs, at least two data nodes (**ess**) or cold data nodes (**ess-cold**) must be deployed in each AZ.               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  For a cluster with no Master nodes, the number of removed data nodes (including cold data nodes and other types of nodes) in a scale-in must be fewer than half of the number of the original data nodes, and the number of remaining data nodes after a scale-in must be greater than the maximum number of index replicas.           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  For a cluster with master nodes, the number of removed master nodes in a scale-in must be fewer than half of the number of the original master nodes. After scale-in, there has to be an odd number of master nodes, and there has to be at least three of them.                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                                       |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | **Definition**                                                                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | Node type.                                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | **Constraints**                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  After scale-in, at least one instance of each node type must be retained in each AZ. For cross-AZ clusters, the difference in the number of nodes of the same type across different AZs must not exceed 1. For clusters with two AZs, at least two data nodes (**ess**) or cold data nodes (**ess-cold**) must be deployed in each AZ. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  For clusters without a master node, the number of data nodes (including cold data nodes and other node types) scaled in each time must be less than half of the total number of current data nodes, and the number of data nodes after scaling in must be greater than the maximum number of index replicas.                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  For clusters with a master node, the number of master nodes scaled in each time must be less than half of the total number of current master nodes, and the number of master nodes after scaling in must be an odd number not less than 3.                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  **ess**: Data node.                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  **ess-cold**: Cold data node.                                                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  **ess-client**: Client node.                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  **ess-master**: Master node.                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  **lgs**: Logstash node.                                                                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                                       |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Scale in a cluster by specifying the node type and the number of nodes to be removed.

.. code-block:: text

   POST https://{Endpoint}/v1.0/extend/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/role/shrink

   {
     "shrink" : [ {
       "type" : "ess",
       "reducedNodeNum" : 1
     } ]
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                        |
+===================================+====================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                   |
|                                   |                                                                                                                                    |
|                                   | Modify the request before retry.                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                       |
|                                   |                                                                                                                                    |
|                                   | The resource that the client attempts to create already exists, or the update request fails to be processed because of a conflict. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
