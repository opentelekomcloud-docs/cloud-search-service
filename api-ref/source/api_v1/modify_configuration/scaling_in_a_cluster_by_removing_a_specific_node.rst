:original_name: UpdateShrinkNodes.html

.. _UpdateShrinkNodes:

Scaling In a Cluster by Removing a Specific Node
================================================

Function
--------

If a cluster has excess capacity due to off-peak traffic or reduced data volume, you can reduce its nodes to cut costs.

Constraints
-----------

-  Data migration is involved during scale-in. The timeout threshold for data migration of a single node is 48 hours. If the timeout occurs, the scale-in fails. When the cluster data volume is large, manually adjust the data migration rate and avoid operations during peak hours.

-  Before scaling in, back up all key data to prevent data loss.

-  Only Elasticsearch/OpenSearch clusters are supported.

-  Data migration is involved during scale-in. The timeout threshold for data migration of a single node is 48 hours. If the timeout occurs, the scale-in fails. When the cluster data volume is large, manually adjust the data migration rate and avoid operations during peak hours.

-  For clusters without master nodes: scale-in is supported only when the total number of data nodes and cold data nodes is greater than or equal to 3. In a single scale-in operation, the total number of data nodes and cold data nodes to be removed must be less than half of the total number before scale-in. After scale-in, the total number of data nodes and cold data nodes must be greater than the maximum number of index replicas.

-  For clusters with master nodes: scale-in is supported only when the number of data nodes is greater than or equal to 2. In a single scale-in operation, the number of master nodes to be removed must be less than half of the number of master nodes before scale-in.

-  After scale-in, the disk usage must be less than 80%.

-  After scale-in, at least one instance of each node type must be retained in each AZ. For cross-AZ clusters, the difference in the number of nodes of the same type across different AZs must not exceed 1. For clusters with two AZs, at least two data nodes (**ess**) or cold data nodes (**ess-cold**) must be deployed in each AZ.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/node/offline

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

   +-----------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                                                                                                                                                                                                             |
   +=================+=================+==================+=========================================================================================================================================================================================================================================+
   | migrate_data    | No              | String           | **Definition**                                                                                                                                                                                                                          |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | Whether to migrate data from the node.                                                                                                                                                                                                  |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | **Constraints**                                                                                                                                                                                                                         |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | N/A                                                                                                                                                                                                                                     |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | **Range**                                                                                                                                                                                                                               |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | -  **true**: Migrate data. During data migration, the system moves all data shards from the node to be removed to the remaining nodes. The node is removed only after data migration is complete.                                       |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | -  **false**: Do not migrate data. When the data on the node to be removed has replicas on the remaining nodes, data migration can be skipped to shorten the cluster change time and reduce the load pressure caused by data migration. |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | **Default Value**                                                                                                                                                                                                                       |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | true                                                                                                                                                                                                                                    |
   +-----------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | shrink_nodes    | Yes             | Array of strings | **Definition**                                                                                                                                                                                                                          |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | ID of the node to be removed. Obtain the **ID** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`.                                                                                             |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | **Constraints**                                                                                                                                                                                                                         |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | N/A                                                                                                                                                                                                                                     |
   +-----------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | agency_name     | No              | String           | **Definition**                                                                                                                                                                                                                          |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | Agency name, which authorizes the current account to access and use OBS. OBS operation permissions are required to store snapshot data in the OBS bucket.                                                                               |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | **Constraints**                                                                                                                                                                                                                         |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | The agency must have VPC operation permissions: "``vpc:subnets:get``","``vpc:ports:*``".                                                                                                                                                |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | This parameter is mandatory when connected to the new IAM plane, and optional when connected to the old IAM plane.                                                                                                                      |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | **Range**                                                                                                                                                                                                                               |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | The agency name can contain up to 64 characters. Only letters, digits, underscores (_), and hyphens (-) are allowed.                                                                                                                    |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | **Default Value**                                                                                                                                                                                                                       |
   |                 |                 |                  |                                                                                                                                                                                                                                         |
   |                 |                 |                  | N/A                                                                                                                                                                                                                                     |
   +-----------------+-----------------+------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Scale in a cluster by removing specified nodes.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/{cluster_id}/node/offline

   {
     "shrink_nodes" : [ "2077bdf3-b90d-412e-b460-635b9b159c11" ],
     "migrate_data" : "true"
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
