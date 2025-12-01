:original_name: UpdateFlavorByType.html

.. _UpdateFlavorByType:

Change the specifications of a specified node type.
===================================================

Function
--------

If the workloads on a cluster's data plane change, you can scale the cluster vertically by changing its node specifications or node storage type.

-  Cluster types that support node specifications change: Elasticsearch, OpenSearch, and Logstash.

-  Cluster types that support node storage type (disk type) change: Elasticsearch and OpenSearch. All mission-critical data must be backed up before a node storage type (disk type) change. This helps to prevent data loss.

You can specify the following node types when calling this API:

-  ess: data node (only for Elasticsearch and OpenSearch).

-  ess-cold: cold data node (only for Elasticsearch and OpenSearch).

-  ess-client: client node (only for Elasticsearch and OpenSearch).

-  ess-master: master node (only for Elasticsearch and OpenSearch).

-  lgs: Logstash node (only for Logstash).

Constraints
-----------

-  Make sure the cluster status is Available and there are no ongoing tasks.

-  The node specifications and storage type cannot be changed for nodes that use local disks.

-  The node specifications and storage type cannot be changed at the same time.

-  The node storage type can be changed only for data nodes and cold data nodes.

-  When you change the node storage type, data needs to be migrated between different nodes. The timeout for data migration per node is 48 hours. Upgrade will fail if this timeout expires. When the cluster has large quantities of data, you are advised to manually adjust the data migration rate and avoid performing the migration during peak hours.

-  For a cluster without master nodes, the node storage type can be changed only if the number of data nodes plus cold data nodes is at least three.

-  For a cluster with master nodes, this operation is allowed only if the cluster has at least two data nodes.

-  During a node storage type change, there is always one node that is unavailable. To ensure service continuity, there has to be at least two nodes of each type for the cluster in each of its AZs, and the total number of data nodes and cold data nodes is greater than the maximum number of index replicas plus 1.

-  During a node specifications changes, nodes are brought offline in order to make the changes. To ensure service continuity, make sure all shards have replicas.

-  Make sure the disk usage is always less than 80/ %during the change.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/{types}/flavor

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                   |
   +=================+=================+=================+===============================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Project ID of the account.                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | ID of the cluster whose specifications you want to change. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Cluster ID.                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | types           | Yes             | String          | **Definition**:                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | Type of the cluster node you want to modify.                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | -  **ess**: data node                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | -  lgs: Logstash node.                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                               |
   |                 |                 |                 | N/A                                                                                                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +---------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                 | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                   |
   +===========================+=================+=================+===============================================================================================================================================================================================================================================================================================+
   | new_flavor_id             | Yes             | String          | **Definition**:                                                                                                                                                                                                                                                                               |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | ID of the new node flavor or node storage type (disk type). It is determined by **operation_type**.                                                                                                                                                                                           |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | The value range depends on **operation_type**.                                                                                                                                                                                                                                                |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Value range**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | #. When **operation_type** is set to vm, newFlavorId indicates the node flavor ID after the change. This parameter is obtained by calling the :ref:`Obtaining the Instance Specifications List <listflavors>` API. The API selects a flavor_id based on the values of the **name** attribute. |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | #. When **operation_type** is set to volume, new_flavor_id indicates the node storage type (disk type). The options are as follows:                                                                                                                                                           |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  **COMMON**: common I/O                                                                                                                                                                                                                                                                     |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  **HIGH**: high I/O                                                                                                                                                                                                                                                                         |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  **ULTRAHIGH**: ultra-high I/O                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  **ESSD**: ultra-fast SSD                                                                                                                                                                                                                                                                   |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Default value**:                                                                                                                                                                                                                                                                            |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | N/A                                                                                                                                                                                                                                                                                           |
   +---------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | operation_type            | No              | String          | **Definition**:                                                                                                                                                                                                                                                                               |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | Operation type.                                                                                                                                                                                                                                                                               |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | N/A                                                                                                                                                                                                                                                                                           |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Value range**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  vm: Change the node flavor.                                                                                                                                                                                                                                                                |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  volume: Change the disk type.                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Default value**:                                                                                                                                                                                                                                                                            |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | vm                                                                                                                                                                                                                                                                                            |
   +---------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | need_check_replica        | No              | Boolean         | **Definition**:                                                                                                                                                                                                                                                                               |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | Whether to verify replicas.                                                                                                                                                                                                                                                                   |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | N/A                                                                                                                                                                                                                                                                                           |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Value range**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  \*\ *true*: Enable replica verification.                                                                                                                                                                                                                                                   |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  **false**: Disable replica verification.                                                                                                                                                                                                                                                   |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Default value**:                                                                                                                                                                                                                                                                            |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | true                                                                                                                                                                                                                                                                                          |
   +---------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | need_check_cluster_status | No              | Boolean         | **Definition**:                                                                                                                                                                                                                                                                               |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | Whether to check the cluster status. The value can be true or false. The default value is **true**.                                                                                                                                                                                           |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | N/A                                                                                                                                                                                                                                                                                           |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Value range**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  **true**: Enable cluster load check.                                                                                                                                                                                                                                                       |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  false: Cluster status verification is ignored.                                                                                                                                                                                                                                             |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Default value**:                                                                                                                                                                                                                                                                            |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | true                                                                                                                                                                                                                                                                                          |
   +---------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_load_check        | No              | Boolean         | **Definition**:                                                                                                                                                                                                                                                                               |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | Whether to check the cluster load. The value can be **true** or **false**. The default value is **true**.                                                                                                                                                                                     |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Constraints**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | N/A                                                                                                                                                                                                                                                                                           |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Value range**:                                                                                                                                                                                                                                                                              |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  **true**: enable cluster load check.                                                                                                                                                                                                                                                       |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | -  false: Skip cluster load check.                                                                                                                                                                                                                                                            |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | **Default value**:                                                                                                                                                                                                                                                                            |
   |                           |                 |                 |                                                                                                                                                                                                                                                                                               |
   |                           |                 |                 | true                                                                                                                                                                                                                                                                                          |
   +---------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ess/flavor

   {
     "need_check_replica" : false,
     "new_flavor_id" : "HIGH",

     "need_check_cluster_status" : true,
     "operation_type" : "volume",
     "cluster_load_check" : true
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
