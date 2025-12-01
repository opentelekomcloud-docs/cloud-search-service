:original_name: css_01_0086.html

.. _css_01_0086:

Planning Node Types and Specifications
======================================

This topic describes the application scenarios and configuration suggestions for each type of cluster nodes, including data nodes, master nodes, client nodes, and cold data nodes. The aim is to help you properly select and configure nodes for your cluster based on service requirements. It also provides suggestions on selecting node specifications and configuring the node storage type, storage capacity, and node quantity, helping you properly plan the capacities of your cluster.

Planning Node Types
-------------------

Before creating a cluster, determine the types of nodes to use based on service requirements, query load, data growth patterns, and performance goals.

For each cluster, data nodes are mandatory, while master, client, and cold data nodes are optional. Choose whether to enable the latter three based on your service needs and performance requirements.

.. table:: **Table 1** Introduction to different node types

   +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Node Type                         | Suggestions on Node Selection                                                                                                                                                                                                                                                                                                           |
   +===================================+=========================================================================================================================================================================================================================================================================================================================================+
   | Data node (ESS)                   | Data nodes are primarily used to store the cluster's data. The functions of the data nodes vary depending on the node types enabled for the cluster.                                                                                                                                                                                    |
   |                                   |                                                                                                                                                                                                                                                                                                                                         |
   |                                   | -  If **Master node** and **Client node** are both selected, data nodes will be used for data storage only.                                                                                                                                                                                                                             |
   |                                   | -  If **Master node** and **Client node** are both unselected, data nodes will be used for all of the following purposes: cluster management, data storage, cluster access, and data analysis. To ensure reliability, a cluster should have a least three nodes.                                                                        |
   |                                   | -  If **Master node** is selected but **Client node** is not, data nodes will be used for data storage, cluster access, and data analysis.                                                                                                                                                                                              |
   |                                   | -  If **Master node** is unselected but **Client node** is selected, data nodes will be used for data storage and cluster management.                                                                                                                                                                                                   |
   +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Master node (ess-master)          | Master nodes manage cluster-wide operations, including metadata, indexes, and shard allocation. For large-scale deployments, using dedicated master nodes enhances cluster stability, service availability, and centralized control.                                                                                                    |
   |                                   |                                                                                                                                                                                                                                                                                                                                         |
   |                                   | -  Large-scale cluster: For a cluster that has more than 10 nodes, you are advised to add dedicated master nodes to effectively manage the cluster status and metadata.                                                                                                                                                                 |
   |                                   | -  Large quantities of indexes and index shards: If the number of indexes or shards exceeds 10,000, master nodes will have better performance handling complex cluster management tasks, avoiding impact on the performance of data nodes.                                                                                              |
   |                                   | -  Better management of cluster nodes: Master nodes maintain the cluster metadata, including index mapping, settings, and aliases. For a complex cluster structure, dedicated master nodes offer better management, including node joining, exiting, and fault detection. Master nodes play a critical role in cluster node management. |
   |                                   | -  Improved cluster stability and reliability: Dedicated master nodes improve cluster stability and reliability by taking over cluster management responsibilities from data storage and query nodes.                                                                                                                                   |
   |                                   | -  Optimized performance for data nodes: By offloading cluster management tasks from data nodes to master nodes, you can allow data nodes to focus on data processing, which leads to improved performance.                                                                                                                             |
   +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Client node (ess-client)          | Client nodes route and coordinate search and index requests, offloading processing from data nodes for enhanced query performance and cluster scalability when there are heavy loads.                                                                                                                                                   |
   |                                   |                                                                                                                                                                                                                                                                                                                                         |
   |                                   | -  High queries per second (QPS): In the face of a high QPS, a dedicated client node can evenly distribute query requests, reducing the load of data nodes and improving the overall query performance.                                                                                                                                 |
   |                                   | -  Complex aggregation queries: For complex, compute-intensive aggregation queries, a client node can dedicate to the handling of aggregation results, thus improving the efficiency and response speed of such queries.                                                                                                                |
   |                                   | -  Large number of shards: In a cluster with a large number of shards, a client node can effectively coordinate and manage query requests to each shard, improving efficiency in request forwarding and processing.                                                                                                                     |
   |                                   | -  Reducing the load of data nodes: A client node parses search requests, determines the locations of index shards, and coordinates different nodes to execute searches. This reduces the load of data nodes by allowing them to focus on data storage and indexing.                                                                    |
   |                                   | -  Improved cluster scalability: The use of client nodes allows for better cluster scalability and flexibility, enabling support for large datasets and more complex query requirements.                                                                                                                                                |
   +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Cold data node (ess-cold)         | Cold data nodes are used to store and query latency-insensitive data in large quantities. They offer an effective way to manage large datasets while cutting storage costs.                                                                                                                                                             |
   |                                   |                                                                                                                                                                                                                                                                                                                                         |
   |                                   | -  Storage of historical data in large quantities: Cold data nodes offer a more cost-effective solution for storing large quantities of historical data that are infrequently accessed but useful for analytical purposes.                                                                                                              |
   |                                   | -  Optimizing hot data performance: By migrating cold data to cold data nodes, you reduce the storage load of hot data nodes, thereby optimizing their query and write performance.                                                                                                                                                     |
   |                                   | -  Insensitivity to query latency: Cold data nodes are a better option for storing data that is insensitive to a high query latency.                                                                                                                                                                                                    |
   |                                   | -  Cost-effectiveness: Cold data nodes usually use large-capacity disks that offer inexpensive storage.                                                                                                                                                                                                                                 |
   |                                   |                                                                                                                                                                                                                                                                                                                                         |
   |                                   | .. caution::                                                                                                                                                                                                                                                                                                                            |
   |                                   |                                                                                                                                                                                                                                                                                                                                         |
   |                                   |    CAUTION:                                                                                                                                                                                                                                                                                                                             |
   |                                   |    If no cold data nodes were enabled during cluster creation, they cannot be added later, so you have to determine whether to use cold data nodes while creating a cluster.                                                                                                                                                            |
   +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   -  If no master or client nodes were enabled when a cluster was created, you can add them if data nodes become overloaded later at some point. For details, see :ref:`Adding New Node Types <en-us_topic_0000001938218180__section1195734814511>`.
   -  When cold data nodes are enabled, you can switch between cold and hot data storage. For details, see :ref:`Switching Between Hot and Cold Storage for an Elasticsearch Cluster <css_01_0079>`. If there are no cold data nodes, we recommend that you use decoupled storage and compute, which can also cut storage costs. For details, see :ref:`Configuring Decoupled Storage and Compute for an Elasticsearch Cluster <css_01_0113>`.

Suggestions on Data Node Configuration
--------------------------------------

.. table:: **Table 2** Data node configuration

   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Configuration Suggestions                                                                                                                                                                                                                                                                                                                                   |
   +===================================+=============================================================================================================================================================================================================================================================================================================================================================+
   | Node Specifications               | In the node flavor list, **vCPUs \| Memory** indicate the number of vCPUs and memory capacity available for each flavor, and **Recommended Storage** indicates the supported storage capacity range. We recommend that you select node specifications based on service needs, such as the data volumes, performance requirements, and your spending budget. |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | :ref:`Node Specifications <en-us_topic_0000002351306217__section53901541481>` describes the application scenarios and core features of different node specifications. It can help you properly plan your cluster.                                                                                                                                           |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | For more information about different node specifications, see section "ECS Types" in *Elastic Cloud Server User Guide*.                                                                                                                                                                                                                                     |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Node Storage Type and Capacity    | -  If the selected node flavor uses EVS disks, you need to further select **Node Storage Type** and **Capacity** based on service requirements.                                                                                                                                                                                                             |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   |    -  For more on EVS disk performance, see section "Disk Types and Performance" in *Elastic Volume Service User Guide*.                                                                                                                                                                                                                                    |
   |                                   |    -  The value range of node storage capacity is determined by the node flavor you select. The value must be divisible by 20. For how to calculate the required node storage capacity, see :ref:`Recommended Node Storage Capacity for Data Nodes/Cold Data Nodes <en-us_topic_0000002351306217__section6913184705418>`.                                   |
   |                                   |    -  Node storage capacity cannot be reduced once the cluster is created. Evaluate your long-term data needs and select an appropriate size.                                                                                                                                                                                                               |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | -  If the selected node flavor uses local disks, there is no need to select the node storage type, and the node storage capacity is a fixed value. Both of them are determined by the local disk specifications.                                                                                                                                            |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Nodes                             | -  If master nodes are configured, the number of data nodes ranges from 1 to 200.                                                                                                                                                                                                                                                                           |
   |                                   | -  If no master nodes are configured, the number of data nodes ranges from 1 to 32.                                                                                                                                                                                                                                                                         |
   |                                   | -  To ensure cluster availability, you should configure at least three data nodes. For how to calculate the number of nodes needed, see :ref:`Recommended Node Quantity for Data Nodes/Cold Data Nodes <en-us_topic_0000002351306217__section9769202175713>`.                                                                                               |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | If the number of data nodes in your cluster is not evenly divisible by the number of AZs, data distribution may become unbalanced across nodes. This will negatively impact both query and write performance.                                                                                                                                               |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002351306217__section53901541481:

Node Specifications
-------------------

The choice of node specifications affects disk deployment. There are two types of disks: local disks and EVS disks. For example, high-performance nodes may use local disks, while standard nodes may use cost-effective EVS disks.

-  Local disks refer to physical storage directly attached to the host machines running your ECSs. They deliver high I/O performance, low latency, and high throughput, making them ideal for performance-sensitive workloads that do not require long-term storage.
-  EVS disks are a virtual block storage service that is independent of ECSs. They provide high reliability and fast elasticity, making them ideal for workloads that require high data reliability and highly scalable storage capacity.

.. warning::

   -  Local disks are less reliable than EVS disks—if the underlying host fails, data stored on local disks may be permanently lost. For this reason, avoid using local disks to store mission-critical data. Instead, use EVS disks.
   -  If you do use local disks, you are advised to enable automatic snapshot creation when creating the cluster, and also enable replicas when creating indexes. This helps lower the risk of data loss.

.. _en-us_topic_0000002351306217__section6913184705418:

Recommended Node Storage Capacity for Data Nodes/Cold Data Nodes
----------------------------------------------------------------

If you select EVS disks, you can select a node storage capacity within the range supported by the selected node flavor.

When planning the storage capacity of a cluster, consider the following factors: the original data size, number of data replicas, data bloat rate, and disk usage. The following is a recommended formula for determining the needed cluster storage capacity:

**Storage capacity = Original data size x (1 + Number of replicas) x (1 + Data bloat rate) x (1 + Ratio of reserved space)**

where,

-  Original data size: Determine the size of original data that needs to be stored.
-  Number of replicas: The default value is 1.
-  Data bloat rate: Extra data may be generated due to data indexing. Generally, you are advised to use a 25% data bloat rate.
-  Disk usage: Considering the space occupied by the operating system and file system and the space reserved for optimized disk performance and redundancy, you are advised to keep the disk usage under 70%. That is, you need to reserve 30% of the total disk capacity.

Using the recommended values above, the formula should be: Storage capacity = Original data size x 2 x 1.25 x 1.3 = Original data size x 3.25

This formula is for quick reference only. You still need to adjust it based on the actual applications and projected data growth rate. Moreover, the storage capacity must be divisible by 20.

.. _en-us_topic_0000002351306217__section9769202175713:

Recommended Node Quantity for Data Nodes/Cold Data Nodes
--------------------------------------------------------

Data nodes and cold data nodes are used to store data. Their quantities largely determine the cluster performance baseline. The following formulas can be used to estimate the number of data nodes and cold data nodes needed:

**Number of data nodes + Number of cold data nodes = Number of write nodes + Number of query nodes**

**Number of write nodes = Traffic during peak hours (MB/s)/Number of vCPUs per node/Per-vCPU write performance baseline (MB/s) x Number of index replicas**

**Number of query nodes = Query QPS/(Number of vCPUs per node x 3/2/Average query latency (s)) x Number of index shards**

where,

-  The number of vCPUs per node is determined by the selected node flavor.
-  The per-vCPU write performance baseline is determined by the selected disk type. For a node that uses EVS disks, the per-vCPU write performance baseline is 1 MB/s. For a node that uses local disks, this baseline is 1.5 MB/s.
-  QPS indicates the number of queries that can be processed per second.
-  The average query latency is used as the query performance baseline.
-  Where a high write performance is desired, we recommend setting the number of index shards to equal the total number of data nodes plus cold data nodes, thus evenly distributing the write load across all nodes.
-  Where a high QPS is desired, we recommend setting the number of index shards to equal the total number of data nodes plus cold data nodes **minus 1**, thus evenly distributing the query load across all nodes.

Example:

If the peak traffic is 100 MB/s; the node specifications are 16 vCPUs and 64 GB RAM, with EVS disks; the query throughput is 1,000 QPS; the average query latency is 100 ms; and each index has three shards and two replicas, then:

Number of write nodes = 100/16/1 x 2 = 12

Number of query nodes = 1000/(16 x 3/2/0.1) x 3 = 12

Number of data nodes + Number of cold data nodes = Number of write nodes + Number of query nodes = 12 + 12 = 24

Suggestions on Master Node Configuration
----------------------------------------

.. table:: **Table 3** Master node configuration

   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Configuration Suggestions                                                                                                                                                                                                 |
   +===================================+===========================================================================================================================================================================================================================+
   | Node Specifications               | In the node flavor list, **vCPUs \| Memory** indicate the number of vCPUs and memory capacity available for each flavor, and **Recommended Storage** indicates the supported storage capacity range.                      |
   |                                   |                                                                                                                                                                                                                           |
   |                                   | For a large-scale cluster with a large number of index shards, use large-capacity nodes as master nodes.                                                                                                                  |
   |                                   |                                                                                                                                                                                                                           |
   |                                   | Master nodes support EVS disks only. For more information about different node specifications, see section "ECS Types" in *Elastic Cloud Server User Guide*.                                                              |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Node Storage Type and Capacity    | Select an appropriate storage type and capacity for master nodes.                                                                                                                                                         |
   |                                   |                                                                                                                                                                                                                           |
   |                                   | -  For more on EVS disk performance, see section "Disk Types and Performance" in *Elastic Volume Service User Guide*.                                                                                                     |
   |                                   | -  The node storage capacity is fixed at 40 GB.                                                                                                                                                                           |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Nodes                             | The number of master nodes can be 3, 5, 7, or 9.                                                                                                                                                                          |
   |                                   |                                                                                                                                                                                                                           |
   |                                   | For split-brain protection, the number of master nodes must be an odd number. For the recommended master node quantity, see :ref:`Recommended Master Node Quantity <en-us_topic_0000002351306217__section1156653324311>`. |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002351306217__section1156653324311:

Recommended Master Node Quantity
--------------------------------

Increasing the number of master nodes can improve the cluster's fault tolerance performance, but it can also lead to issues like increased communication overhead, longer election time, and low resource utilization. You are advised to select an appropriate number of master nodes based on service requirements.

The following table provides the recommended number of master nodes based on the cluster size.

.. table:: **Table 4** Recommended number of master nodes

   +-------------------------------------+------------------------------------+----------------------------------------------------+
   | Cluster Size                        | Recommended Number of Master Nodes | Performance Expectation                            |
   +=====================================+====================================+====================================================+
   | Small (< 10 nodes)                  | 3                                  | Basic high availability                            |
   +-------------------------------------+------------------------------------+----------------------------------------------------+
   | Medium (50 > number of nodes >= 10) | 3 or 5                             | Balanced performance and high availability         |
   +-------------------------------------+------------------------------------+----------------------------------------------------+
   | Large (<= 50 nodes)                 | 5 or 7                             | Enhanced fault tolerance and stability             |
   +-------------------------------------+------------------------------------+----------------------------------------------------+
   | Extra-large (>= 100 nodes)          | 5 or 7                             | Pay attention to excessive communication overhead. |
   +-------------------------------------+------------------------------------+----------------------------------------------------+

Suggestions on Client Node Configuration
----------------------------------------

.. table:: **Table 5** Client node configuration

   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Configuration Suggestions                                                                                                                                                                            |
   +===================================+======================================================================================================================================================================================================+
   | Node Specifications               | In the node flavor list, **vCPUs \| Memory** indicate the number of vCPUs and memory capacity available for each flavor, and **Recommended Storage** indicates the supported storage capacity range. |
   |                                   |                                                                                                                                                                                                      |
   |                                   | For a cluster with heavy read and write traffic, use large-capacity nodes as client nodes.                                                                                                           |
   |                                   |                                                                                                                                                                                                      |
   |                                   | Client nodes support EVS disks only. For more information about different node specifications, see section "ECS Types" in *Elastic Cloud Server User Guide*.                                         |
   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Node Storage Type and Capacity    | Select an appropriate storage type and capacity for client nodes.                                                                                                                                    |
   |                                   |                                                                                                                                                                                                      |
   |                                   | -  For more on EVS disk performance, see section "Disk Types and Performance" in *Elastic Volume Service User Guide*.                                                                                |
   |                                   | -  The node storage capacity is fixed at 40 GB.                                                                                                                                                      |
   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Nodes                             | The number of client nodes ranges from 1 to 32.                                                                                                                                                      |
   |                                   |                                                                                                                                                                                                      |
   |                                   | For the recommended client node quantity, see :ref:`Recommended Client Node Quantity <en-us_topic_0000002351306217__section479411819168>`.                                                           |
   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002351306217__section479411819168:

Recommended Client Node Quantity
--------------------------------

Client nodes route and coordinate search and index requests. Its quantity should be determined based on the cluster traffic. For your reference, the following table provides the recommended number of client nodes based on the number of data nodes.

.. table:: **Table 6** Recommended number of client nodes

   ==================== =================================================
   Number of Data Nodes Recommended Number of Client Nodes
   ==================== =================================================
   < 5                  Do not use client nodes.
   >= 5 and < 10        2
   >= 10                Number of client nodes/Number of data nodes = 1:5
   ==================== =================================================

Suggestions on Cold Data Node Configuration
-------------------------------------------

.. table:: **Table 7** Cold data node configuration

   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Configuration Suggestions                                                                                                                                                                                                                                                                                                                                   |
   +===================================+=============================================================================================================================================================================================================================================================================================================================================================+
   | Node Specifications               | In the node flavor list, **vCPUs \| Memory** indicate the number of vCPUs and memory capacity available for each flavor, and **Recommended Storage** indicates the supported storage capacity range. We recommend that you select node specifications based on service needs, such as the data volumes, performance requirements, and your spending budget. |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | :ref:`Node Specifications <en-us_topic_0000002351306217__section53901541481>` describes the application scenarios and core features of different node specifications. It can help you properly plan your cluster.                                                                                                                                           |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | For more information about different node specifications, see section "ECS Types" in *Elastic Cloud Server User Guide*.                                                                                                                                                                                                                                     |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Node Storage Type and Capacity    | -  If the selected node flavor uses EVS disks, you need to further select **Node Storage Type** and **Capacity** based on service requirements.                                                                                                                                                                                                             |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   |    -  For more on EVS disk performance, see section "Disk Types and Performance" in *Elastic Volume Service User Guide*.                                                                                                                                                                                                                                    |
   |                                   |    -  The value range of node storage capacity is determined by the node flavor you select. The value must be divisible by 20. For how to calculate the required node storage capacity, see :ref:`Recommended Node Storage Capacity for Data Nodes/Cold Data Nodes <en-us_topic_0000002351306217__section6913184705418>`.                                   |
   |                                   |    -  Node storage capacity cannot be reduced once the cluster is created. Evaluate your long-term data needs and select an appropriate size.                                                                                                                                                                                                               |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | -  If the selected node flavor uses local disks, there is no need to select the node storage type, and the node storage capacity is a fixed value. Both of them are determined by the local disk specifications.                                                                                                                                            |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Nodes                             | The value range for cold data nodes is 1 to 32.                                                                                                                                                                                                                                                                                                             |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | For how to calculate the number of nodes needed, see :ref:`Recommended Node Quantity for Data Nodes/Cold Data Nodes <en-us_topic_0000002351306217__section9769202175713>`.                                                                                                                                                                                  |
   |                                   |                                                                                                                                                                                                                                                                                                                                                             |
   |                                   | If the number of cold data nodes in your cluster is not evenly divisible by the number of AZs, data distribution may become unbalanced across nodes. This will negatively impact both query and write performance.                                                                                                                                          |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
