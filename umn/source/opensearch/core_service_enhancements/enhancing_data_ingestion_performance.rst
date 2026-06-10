:original_name: css_01_0090.html

.. _css_01_0090:

Enhancing Data Ingestion Performance
====================================

In large-scale data ingestion scenarios, such as log analytics and real-time monitoring, the traditional OpenSearch routing mechanism can generate excessive internal forwarding requests as the number of index shards and the write throughput increase. This can lead to write rejections and increased long-tail latency. To address this issue, CSS provides several ways to enhance ingestion performance: bulk routing, bulk aggregation, text indexing acceleration, and merge optimization. They can help reduce performance overhead and significantly improve write stability and throughput in heavy-load scenarios.

How the Feature Works
---------------------

To balance performance and functionality, CSS provides four ingestion performance enhancement solutions. The core idea is to eliminate or mitigate performance bottlenecks by reducing cross-node communication and accelerating index building.

.. table:: **Table 1** Ways to enhance data ingestion performance

   +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Solution                   | Description                                                                                                                                                                                                                          | When to Use                                                                                                                                                                                                                                    | Details                                                                                                                          |
   +============================+======================================================================================================================================================================================================================================+================================================================================================================================================================================================================================================+==================================================================================================================================+
   | Bulk routing               | Bulk routing reduces cross-node communication and request forwarding by the coordinator node, helping to prevent write rejections.                                                                                                   | Enable this feature for large-scale clusters with a high number of shards. It is particularly effective when bulk request throughput is so intense that it exhausts the coordinator node's network I/O or CPU resources.                       | :ref:`Configuring Bulk Routing <en-us_topic_0000001955726482__en-us_topic_0000001938377700_section9414161115511>`                |
   |                            |                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                |                                                                                                                                  |
   |                            | How it works: Rather than routing each document individually based on its ID (the default behavior), this optimization forces multiple documents within the same bulk request to be routed together to the same shard or local node. |                                                                                                                                                                                                                                                |                                                                                                                                  |
   +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Bulk aggregation           | Bulk aggregation reduces system overhead and improves single-node capacity by minimizing resource lock contention during write operations.                                                                                           | Enable this feature for ultra-high concurrency write scenarios where throughput is critical. We recommend enabling it when monitoring indicates high system CPU usage or significant memory allocation pressure.                               | :ref:`Configuring Bulk Aggregation <en-us_topic_0000001955726482__en-us_topic_0000001938377700_section1443152195614>`            |
   |                            |                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                |                                                                                                                                  |
   |                            | How it works: Instead of processing documents individually within the same bulk request, the system processes them as a unified batch, reducing memory allocations and lock contention.                                              |                                                                                                                                                                                                                                                |                                                                                                                                  |
   +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Text indexing acceleration | Text indexing acceleration significantly speeds up the indexing of text and keyword fields.                                                                                                                                          | Enable this feature when you need high-speed index building with relatively simple tokenization logic. Examples of such scenarios include log auditing and full-text search, where large-volume text and numerous keyword fields are involved. | :ref:`Configuring Text Indexing Acceleration <en-us_topic_0000001955726482__en-us_topic_0000001938377700_section15513121414583>` |
   |                            |                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                |                                                                                                                                  |
   |                            | How it works: Through an optimized indexing process, improved memory utilization, and accelerated tokenization, this feature improves the overall efficiency of text processing.                                                     |                                                                                                                                                                                                                                                |                                                                                                                                  |
   +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Merge optimization         | Merge optimization ensures write stability by preventing write throttling caused by slow segment merging.                                                                                                                            | Enable this feature in high-frequency write scenarios, particularly when the write throughput increases drastically after enabling the three optimizations above and writes become unstable due to merge throttling.                           | :ref:`Configuring Merge Optimization <en-us_topic_0000001955726482__en-us_topic_0000001938377700_section124450517595>`           |
   |                            |                                                                                                                                                                                                                                      |                                                                                                                                                                                                                                                |                                                                                                                                  |
   |                            | How it works: By dynamically increasing merging threads for index shards, this feature accelerates the merging of small segments and reclaims write cache space in a timely manner.                                                  |                                                                                                                                                                                                                                                |                                                                                                                                  |
   +----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

Constraints
-----------

Only OpenSearch 1.3.6 and 2.19.0 clusters support data ingestion performance enhancement.

Logging In to OpenSearch Dashboards
-----------------------------------

Log in to OpenSearch Dashboards and go to the command execution page. OpenSearch clusters support multiple access methods. This topic uses OpenSearch Dashboards as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

.. _en-us_topic_0000001955726482__en-us_topic_0000001938377700_section9414161115511:

Configuring Bulk Routing
------------------------

.. caution::

   After bulk routing is enabled (that is, **index.bulk_routing** is set to **pack** or **local_pack**), documents are no longer routed by ID. This may affect routing-related functionality. For example, ID-based GET requests may fail because the shards cannot be located.

Enable bulk routing to alleviate request forwarding pressure for the node that receives requests.

.. code-block:: text

   PUT /{index_name}/_settings
   {
     "index.bulk_routing": "local_pack"
   }

.. table:: **Table 2** Parameters for bulk routing

   +--------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter          | Type            | Default Value   | Description                                                                                                                                                                                                                                                                                                                                  |
   +====================+=================+=================+==============================================================================================================================================================================================================================================================================================================================================+
   | index_name         | String          | N/A             | Specifies one or more indexes.                                                                                                                                                                                                                                                                                                               |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                                              |
   |                    |                 |                 | -  Single index: Enter the index name, for example, **my_index**.                                                                                                                                                                                                                                                                            |
   |                    |                 |                 | -  Multiple indexes: Enter multiple index names and use a comma (,) to separate them, for example, **my_index1,my_index2**.                                                                                                                                                                                                                  |
   |                    |                 |                 | -  Wildcard: Use the wildcard (*) to match multiple indexes. For example, **myindex\*** indicates all indexes whose name starts with **myindex**.                                                                                                                                                                                            |
   +--------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index.bulk_routing | String          | default         | Specifies the internal routing policy for processing documents within bulk write requests.                                                                                                                                                                                                                                                   |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                                              |
   |                    |                 |                 | -  **default**: Uses the default routing behavior. Each document within the same bulk request is hashed and routed separately based on its **\_id**. This ensures even data distribution across all shards but can generate significant cross-node forwarding overhead during large-scale bulk writes.                                       |
   |                    |                 |                 | -  **pack**: Routes all documents within the same bulk request to a single, randomly selected shard. This eliminates per-document hash calculations and cross-node forwarding, reducing request forwarding pressure on the coordinator node.                                                                                                 |
   |                    |                 |                 | -  **local_pack** (recommended): First attempts to route all documents within the same bulk request to a local shard on the data node that received the bulk request. If that node does not host a shard of the target index, it falls back to the **pack** mode. This option is recommended because it achieves zero cross-node forwarding. |
   +--------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001955726482__en-us_topic_0000001938377700_section1443152195614:

Configuring Bulk Aggregation
----------------------------

Enable bulk aggregation to enable the system to process documents within each bulk request as a unified batch, instead of processing each document individually. This significantly reduces CPU overhead and lock contention during ultra-high concurrency write operations.

.. code-block:: text

   PUT /{index_name}/_settings
   {
     "index.aggr_perf_batch_size": "128"
   }

.. table:: **Table 3** Parameters for bulk aggregation

   +----------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                  | Type            | Default Value   | Description                                                                                                                                                                                                                                                                                              |
   +============================+=================+=================+==========================================================================================================================================================================================================================================================================================================+
   | index.aggr_perf_batch_size | Integer         | 1               | Specifies the maximum number of documents to process as a single batch.                                                                                                                                                                                                                                  |
   |                            |                 |                 |                                                                                                                                                                                                                                                                                                          |
   |                            |                 |                 | Minimum value: **1** (disables bulk aggregation so that documents will be processed individually)                                                                                                                                                                                                        |
   |                            |                 |                 |                                                                                                                                                                                                                                                                                                          |
   |                            |                 |                 | Recommended value: **128**                                                                                                                                                                                                                                                                               |
   |                            |                 |                 |                                                                                                                                                                                                                                                                                                          |
   |                            |                 |                 | Any value greater than 1 enables bulk aggregation. The system will internally reaggregate documents from bulk requests into batches up to this size. Larger batch sizes increase memory consumption per batch. Adjust this parameter based on your workload requirements and available system resources. |
   |                            |                 |                 |                                                                                                                                                                                                                                                                                                          |
   |                            |                 |                 | The actual number of documents per batch is calculated as: MIN(Number of documents within the bulk request, aggr_perf_batch_size)                                                                                                                                                                        |
   +----------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001955726482__en-us_topic_0000001938377700_section15513121414583:

Configuring Text Indexing Acceleration
--------------------------------------

.. caution::

   Text indexing acceleration cannot be enabled for indexes whose mapping contains nested fields. The system will not be able to start acceleration due to compatibility issues.

Enable text indexing acceleration to speed up the indexing of text and keyword fields.

.. code-block:: text

   PUT /{index_name}/_settings
   {
     "index.native_speed_up": true,
     "index.native_analyzer": true
   }

.. table:: **Table 4** Parameters for text indexing acceleration

   +-----------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type            | Default Value   | Description                                                                                                                                                                                                                                               |
   +=======================+=================+=================+===========================================================================================================================================================================================================================================================+
   | index.native_speed_up | Boolean         | false           | Whether to enable text indexing acceleration.                                                                                                                                                                                                             |
   |                       |                 |                 |                                                                                                                                                                                                                                                           |
   |                       |                 |                 | The value can be:                                                                                                                                                                                                                                         |
   |                       |                 |                 |                                                                                                                                                                                                                                                           |
   |                       |                 |                 | -  **true**: Enables text indexing acceleration. This will significantly accelerate the indexing of text and keyword fields, optimize memory usage during indexing, and reduces the frequency of garbage collection (GC) caused by high-frequency writes. |
   |                       |                 |                 | -  **false**: Disables text indexing acceleration.                                                                                                                                                                                                        |
   +-----------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index.native_analyzer | Boolean         | false           | Whether to enable tokenization acceleration.                                                                                                                                                                                                              |
   |                       |                 |                 |                                                                                                                                                                                                                                                           |
   |                       |                 |                 | This parameter is available only when **index.native_speed_up** is set to **true**, and it applies to text fields only.                                                                                                                                   |
   |                       |                 |                 |                                                                                                                                                                                                                                                           |
   |                       |                 |                 | The value can be:                                                                                                                                                                                                                                         |
   |                       |                 |                 |                                                                                                                                                                                                                                                           |
   |                       |                 |                 | -  **true**: Enables tokenization acceleration. This will significantly reduce CPU time for tokenization.                                                                                                                                                 |
   |                       |                 |                 | -  **false**: Disables tokenization acceleration.                                                                                                                                                                                                         |
   +-----------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001955726482__en-us_topic_0000001938377700_section124450517595:

Configuring Merge Optimization
------------------------------

Increase the number of threads used for segment merging for index shards. This helps prevent write throttling caused by slow segment merging.

.. code-block:: text

   PUT /{index_name}/_settings
   {
     "index.merge.scheduler.max_thread_count": 8
   }

.. table:: **Table 5** Parameters for segment merging

   +----------------------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                              | Type            | Default Value   | Description                                                                                                                                                                                                                                                                              |
   +========================================+=================+=================+==========================================================================================================================================================================================================================================================================================+
   | index.merge.scheduler.max_thread_count | Integer         | 4               | Specifies the maximum number of threads used for segment merging in a single shard.                                                                                                                                                                                                      |
   |                                        |                 |                 |                                                                                                                                                                                                                                                                                          |
   |                                        |                 |                 | Value range: 1 to (Number of CPU cores on the node/2)                                                                                                                                                                                                                                    |
   |                                        |                 |                 |                                                                                                                                                                                                                                                                                          |
   |                                        |                 |                 | The recommended value is 8. It allows you to accelerate segment merging by leveraging the multi-core architecture of CPUs, eliminating write throttling caused by slow segment merging. However, you must ensure that your cluster nodes have sufficient CPU cores to run these threads. |
   +----------------------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
