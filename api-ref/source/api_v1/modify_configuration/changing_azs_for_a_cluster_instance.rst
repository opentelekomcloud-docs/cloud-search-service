:original_name: UpdateAzByInstanceType.html

.. _UpdateAzByInstanceType:

Changing AZs for a Cluster Instance
===================================

Function
--------

An availability zone (AZ) is a physical region where resources use independent power supplies and networks. AZs in the same region can communicate with each other through internal networks but are physically isolated.

Multi-AZ deployment is a high-availability solution provided by CSS. You can deploy a cluster across two or three AZs in the same region. This helps prevent data loss and lower the risk of downtime.

This API is used to change AZs for an Elasticsearch or OpenSearch cluster by specifying node types.

Constraints
-----------

-  To ensure service continuity, the total number of data nodes and cold data nodes in the cluster must be greater than or equal to 3.

-  To ensure that all index shards in the cluster can be allocated to the remaining data nodes or cold data nodes, and to prevent replicas from becoming unassignable when nodes go offline during switchover, the total number of data nodes and cold data nodes must be greater than the maximum number of index replicas plus 1.

-  In AZ high-availability reconstruction scenarios, when converting from a single-AZ deployment to a dual-AZ deployment, the final number of data nodes or cold data nodes in each AZ must be no fewer than 2.

-  During the switchover process, nodes are taken offline and rebuilt one by one. You must ensure that after any single node goes offline, the remaining nodes have enough disk capacity to accommodate all data from that node, and that disk usage remains below 80%.

-  While the cluster is switching AZs, the AZ attribute of some nodes may already have changed. In this case, the displayed AZ of the nodes may show an intermediate state. After the task is complete, the cluster AZ display returns to normal.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/inst-type/{inst_type}/azmigrate

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                  |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                           |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | ID of the cluster whose AZs are to be changed. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                                     |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | inst_type       | Yes             | String          | **Definition**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | Types of nodes whose AZs are to be changed.                                                                                                       |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Constraints**                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | The value must be a valid node type. Before changing AZs, you are advised to back up all critical data to prevent data loss.                      |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Range**                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | -  **all**: All node types.                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | -  **ess**: Data node.                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | -  **ess-cold**: Cold data node.                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | -  **ess-client**: Client node.                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | -  **ess-master**: Master node.                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | **Default Value**                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                                               |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +----------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter            | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                     |
   +======================+=================+=================+=================================================================================================================================================================================================================================================================================+
   | source_az            | Yes             | String          | **Definition**                                                                                                                                                                                                                                                                  |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | Current AZ of the node, obtained from :ref:`Querying Cluster Details <showclusterdetail>`.                                                                                                                                                                                      |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Constraints**                                                                                                                                                                                                                                                                 |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Range**                                                                                                                                                                                                                                                                       |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Default Value**                                                                                                                                                                                                                                                               |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   +----------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | target_az            | Yes             | String          | **Definition**                                                                                                                                                                                                                                                                  |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | Target AZ of the node, obtained from :ref:`Regions and Endpoints <css_03_0001>` in "Before You Start".                                                                                                                                                                          |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Constraints**                                                                                                                                                                                                                                                                 |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Range**                                                                                                                                                                                                                                                                       |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Default Value**                                                                                                                                                                                                                                                               |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   +----------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | migrate_type         | Yes             | String          | **Definition**:                                                                                                                                                                                                                                                                 |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | AZ migration method.                                                                                                                                                                                                                                                            |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | -  To complete this AZ change, the system will try to move as few nodes as possible to rebuild the cluster. During this process, the YML configuration file of the nodes that are not modified is also updated. You need to restart the cluster to make the change take effect. |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | -  If you migrate from one AZ to another, there is no need to restart the cluster. If multiple AZs are migrated, you must restart the cluster to make the change take effect.                                                                                                   |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Value range**:                                                                                                                                                                                                                                                                |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | -  **multi_az_change**: Add one or two AZs for a single-AZ cluster, or add one AZ for a dual-AZ cluster.                                                                                                                                                                        |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | -  **az_migrate**: Migrate data from one AZ to another.                                                                                                                                                                                                                         |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Default value**:                                                                                                                                                                                                                                                              |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   +----------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | agency               | Yes             | String          | **Definition**                                                                                                                                                                                                                                                                  |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | Agency name. After a node is rebuilt, NICs need to be reattached to the new node. This requires you to have VPC permissions. Select an IAM agency to grant the current account the permission to access and use VPC.                                                            |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Constraints**                                                                                                                                                                                                                                                                 |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | The agency name can contain at most 64 characters. Only letters, digits, underscores (_), and hyphens (-) are allowed.                                                                                                                                                          |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Range**                                                                                                                                                                                                                                                                       |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Default Value**                                                                                                                                                                                                                                                               |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   +----------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | indices_backup_check | No              | Boolean         | **Definition**:                                                                                                                                                                                                                                                                 |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | Whether to check full index snapshots. You are advised to select Check full index snapshot. This ensures that all data has been backed up, so that in case the task fails, the data can be restored using this snapshot.                                                        |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | N/A                                                                                                                                                                                                                                                                             |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Value range**:                                                                                                                                                                                                                                                                |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | -  **true**: Check for full index snapshots.                                                                                                                                                                                                                                    |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | -  **false**: Do not check for full index snapshots.                                                                                                                                                                                                                            |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | **Default value**:                                                                                                                                                                                                                                                              |
   |                      |                 |                 |                                                                                                                                                                                                                                                                                 |
   |                      |                 |                 | true                                                                                                                                                                                                                                                                            |
   +----------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Change AZs for the current cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/inst-type/all/azmigrate

   {
     "source_az" : "az_code_c",
     "target_az" : "az_code_a",
     "migrate_type" : "az_migrate",
     "agency" : "css-test-agency"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                                  |
+===================================+==============================================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                             |
|                                   |                                                                                                                                                                                              |
|                                   | The client should not repeat the request without modifications.                                                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | The request is rejected. The server has received the request and understood it, but the server is refusing to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
