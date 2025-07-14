:original_name: UpdateShrinkCluster.html

.. _UpdateShrinkCluster:

Scaling In Nodes of a Specific Type
===================================

Function
--------

This API is used to remove instances of specific types and reduce instance storage capacity in a cluster. Yearly/Monthly clusters do not support the removal of specified node types by calling this API.

.. note::

   All mission-critical data has been backed up before a cluster scale-in. This is to prevent data loss.

URI
---

POST /v1.0/extend/{project_id}/clusters/{cluster_id}/role/shrink

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Specifies the ID of the cluster to be scaled in. For details, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                               | Description                                                                                                                      |
   +=================+=================+====================================================================================+==================================================================================================================================+
   | shrink          | Yes             | Array of :ref:`ShrinkNodeReq <updateshrinkcluster__request_shrinknodereq>` objects | **Parameter description**:                                                                                                       |
   |                 |                 |                                                                                    |                                                                                                                                  |
   |                 |                 |                                                                                    | Type and quantity of nodes you want to scale in.                                                                                 |
   +-----------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | agency_name     | No              | String                                                                             | **Parameter description**:                                                                                                       |
   |                 |                 |                                                                                    |                                                                                                                                  |
   |                 |                 |                                                                                    | Agency name. You can create an agency to allow CSS to call other cloud services.                                                 |
   |                 |                 |                                                                                    |                                                                                                                                  |
   |                 |                 |                                                                                    | **Constraints**:                                                                                                                 |
   |                 |                 |                                                                                    |                                                                                                                                  |
   |                 |                 |                                                                                    | This parameter is mandatory when the new IAM plane is connected. This parameter is optional when the old IAM plane is connected. |
   |                 |                 |                                                                                    |                                                                                                                                  |
   |                 |                 |                                                                                    | **Options**:                                                                                                                     |
   |                 |                 |                                                                                    |                                                                                                                                  |
   |                 |                 |                                                                                    | VPC permissions required by the agency: "``vpc:subnets:get``","``vpc:ports:*``".                                                 |
   |                 |                 |                                                                                    |                                                                                                                                  |
   |                 |                 |                                                                                    | **Default value**:                                                                                                               |
   |                 |                 |                                                                                    |                                                                                                                                  |
   |                 |                 |                                                                                    | N/A                                                                                                                              |
   +-----------------+-----------------+------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _updateshrinkcluster__request_shrinknodereq:

.. table:: **Table 3** ShrinkNodeReq

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                     |
   +=================+=================+=================+=================================================================================================================================================================================================================================================================================================================================+
   | reducedNodeNum  | Yes             | Integer         | **Parameter description**:                                                                                                                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Number of nodes you want to reduce.                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  After the scale-in, there has to be at least one node in each AZ under each node type.                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  In a cross-AZ cluster, the difference between the numbers of same-type nodes in different AZs cannot exceed 1.                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  For a cluster with no Master nodes, the number of removed data nodes (including cold data nodes and other types of nodes) in a scale-in must be fewer than half of the number of the original data nodes, and the number of remaining data nodes after a scale-in must be greater than the maximum number of index replicas. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | For a cluster with master nodes, the number of removed master nodes in a scale-in must be fewer than half of the number of the original master nodes. After scale-in, there has to be an odd number of master nodes, and there has to be at least three of them.                                                                |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | **Parameter description**:                                                                                                                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Node type.                                                                                                                                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Options**:                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ess**: data node                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                                                                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Scale in a cluster by scaling in specified type of nodes.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/role/shrink

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
