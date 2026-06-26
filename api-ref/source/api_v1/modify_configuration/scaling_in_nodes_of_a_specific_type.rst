:original_name: UpdateShrinkCluster.html

.. _UpdateShrinkCluster:

Scaling In Nodes of a Specific Type
===================================

Function
--------

This API is used to remove instances of specific types and reduce instance storage capacity in a cluster.

.. note::

   All mission-critical data has been backed up before a cluster scale-in. This is to prevent data loss.

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
   | project_id      | Yes             | String          | **Definition**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.      |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Constraints**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Value range**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | Project ID of the account.                                                                                                            |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Default value**:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | ID of the cluster to be scaled in. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Constraints**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Value range**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | Cluster ID.                                                                                                                           |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Default value**:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter          | Mandatory       | Type                                                                               | Description                                                                                                                      |
   +====================+=================+====================================================================================+==================================================================================================================================+
   | shrink             | Yes             | Array of :ref:`ShrinkNodeReq <updateshrinkcluster__request_shrinknodereq>` objects | **Parameter description**:                                                                                                       |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | Type and quantity of nodes you want to scale in.                                                                                 |
   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | agency_name        | No              | String                                                                             | **Definition**:                                                                                                                  |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | Agency name. You can create an agency to allow CSS to call other cloud services.                                                 |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Constraints**:                                                                                                                 |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | VPC permissions required by the agency: "``vpc:subnets:get``","``vpc:ports:*``".                                                 |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | This parameter is mandatory when the new IAM plane is connected. This parameter is optional when the old IAM plane is connected. |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Value range**:                                                                                                                 |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | N/A                                                                                                                              |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Default value**:                                                                                                               |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | N/A                                                                                                                              |
   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | operation_type     | No              | String                                                                             | **Definition**:                                                                                                                  |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | Operation type.                                                                                                                  |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Constraints**:                                                                                                                 |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | N/A                                                                                                                              |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Value range**:                                                                                                                 |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | -  vm: Reduce nodes.                                                                                                             |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | - volume: Reduce the disk size.                                                                                                  |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Default value**:                                                                                                               |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | vm                                                                                                                               |
   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_load_check | No              | Boolean                                                                            | **Definition**:                                                                                                                  |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | Whether to check the cluster load.                                                                                               |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Constraints**:                                                                                                                 |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | N/A                                                                                                                              |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Value range**:                                                                                                                 |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | -  **true**: enable cluster load check.                                                                                          |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | -  **true**: skip cluster load check.                                                                                            |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | **Default value**:                                                                                                               |
   |                    |                 |                                                                                    |                                                                                                                                  |
   |                    |                 |                                                                                    | true                                                                                                                             |
   +--------------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _updateshrinkcluster__request_shrinknodereq:

.. table:: **Table 3** ShrinkNodeReq

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                  |
   +=================+=================+=================+==============================================================================================================================================================================================================================================================================================================================+
   | reducedNodeNum  | Yes             | Integer         | **Definition**                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | Number of nodes to be scaled in.                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | **Constraints**                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  After scale-in, at least one instance of each node type must remain in each AZ. For cross-AZ clusters, the number of same-type nodes in different AZs must not differ by more than 1. For clusters with two AZs, at least two data nodes (**ess**) or cold data nodes (**ess-cold**) must be deployed in each AZ.         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  For clusters without master nodes, the number of data nodes removed in a single scale-in operation (including cold data nodes and other node types) must be less than half of the current total number of data nodes. After scale-in, the number of data nodes must be greater than the maximum number of index replicas. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  For clusters with master nodes, the number of master nodes removed in a single scale-in operation must be less than half of the current total number of master nodes. After scale-in, the number of master nodes must be an odd number and must not be less than 3.                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | See **Constraints**.                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                          |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | **Definition**:                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | Node type.                                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | [If **operation_type** is set to **volume**, this parameter cannot be set to **ess-client** or **ess-master**.] (tag:non_helpcenter)                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  **ess**: data node                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | -  **lgs**: Logstash node                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                                                                          |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

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
