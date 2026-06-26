:original_name: UpdateShrinkNodes.html

.. _UpdateShrinkNodes:

Scaling In a Cluster by Removing a Specific Node
================================================

Function
--------

If a cluster has excess capacity due to off-peak traffic or reduced data volume, you can reduce its nodes to cut costs.

Constraints
-----------

-  Scale-in involves data migration. The timeout threshold for data migration on a single node is 48 hours. If this threshold is exceeded, the scale-in operation fails. If the cluster contains a large amount of data, it is recommended that you manually adjust the data migration rate and avoid performing the operation during peak service hours.

-  Before performing scale-in, it is recommended that you back up all critical data to avoid data loss.

-  Supported only for Elasticsearch and OpenSearch clusters.

-  Scale-in involves data migration. The timeout threshold for data migration on a single node is 48 hours. If this threshold is exceeded, the scale-in operation fails. If the cluster contains a large amount of data, it is recommended that you manually adjust the data migration rate and avoid performing the operation during peak service hours.

-  For clusters without master nodes: scale-in is supported only when the total number of data nodes and cold data nodes is greater than or equal to 3. In a single scale-in operation, the total number of data nodes and cold data nodes to be removed must be less than half of the total number before scale-in. After scale-in, the total number of data nodes and cold data nodes must be greater than the maximum number of index replicas.

-  For clusters with master nodes: scale-in is supported only when the number of data nodes is greater than or equal to 2. In a single scale-in operation, the number of master nodes to be removed must be less than half of the number of master nodes before scale-in.

-  After scale-in, disk usage must be less than 80%.

-  After scale-in, at least one instance of each node type must remain in each AZ. For cross-AZ clusters, the number of same-type nodes in different AZs must not differ by more than 1. For clusters with two AZs, at least two data nodes (**ess**) or cold data nodes (**ess-cold**) must be deployed in each AZ.

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

   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                                                                                                                                                                        |
   +=================+=================+==================+====================================================================================================================================================================================================+
   | migrate_data    | No              | String           | **Definition**:                                                                                                                                                                                    |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | Whether to migrate data.                                                                                                                                                                           |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | **Value range**:                                                                                                                                                                                   |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | -  **true**: Migrate data. During data migration, the system migrates all data from the to-be-removed nodes to the remaining nodes, and removes these nodes upon completion of the data migration. |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | -  **false**: Do not migrate data. If the data on the to-be-removed nodes has replicas on other nodes, data migration can be skipped and the cluster change can be completed faster.               |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | **Default value**:                                                                                                                                                                                 |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | true                                                                                                                                                                                               |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | shrink_nodes    | Yes             | Array of strings | **Definition**:                                                                                                                                                                                    |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | ID of the node to be removed.                                                                                                                                                                      |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | **Constraints**:                                                                                                                                                                                   |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | N/A                                                                                                                                                                                                |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | **Value range**:                                                                                                                                                                                   |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | Obtain the **ID** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`.                                                                                      |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | **Default value**:                                                                                                                                                                                 |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | N/A                                                                                                                                                                                                |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | agency_name     | No              | String           | **Definition**:                                                                                                                                                                                    |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | Agency name that grants the current account the permission to access and use OBS. To store snapshots to an OBS bucket, you must have the required OBS access permissions.                          |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | **Constraints**:                                                                                                                                                                                   |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | VPC permissions required by the agency: "``vpc:subnets:get``","``vpc:ports:*``".                                                                                                                   |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | This parameter is mandatory when the new IAM plane is connected. This parameter is optional when the old IAM plane is connected.                                                                   |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | **Value range**:                                                                                                                                                                                   |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | N/A                                                                                                                                                                                                |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | **Default value**:                                                                                                                                                                                 |
   |                 |                 |                  |                                                                                                                                                                                                    |
   |                 |                 |                  | N/A                                                                                                                                                                                                |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Scale in a cluster by removing specified nodes.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/node/offline

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
