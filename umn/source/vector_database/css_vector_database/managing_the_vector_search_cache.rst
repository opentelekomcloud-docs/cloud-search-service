:original_name: css_01_0130.html

.. _css_01_0130:

Managing the Vector Search Cache
================================

For vector search systems processing hundreds of millions of vectors, maintaining millisecond-level latency requires storing a large number of high-dimensional vector indexes in memory. Unlike traditional Elasticsearch or OpenSearch implementations that rely heavily on JVM heap memory, the CSS vector search engine is built on C++ and uses off-heap memory, which delivers superior performance. Without effective lifecycle management, large-scale deployments may experience: out of memory (OOM) if inactive (or cold) indexes accumulate and occupy too much memory; or unstable query latency due to frequent "swap-in and swap-out" of cached index segments. To address this problem, the CSS vector database implements a comprehensive set of off-heap memory management policies to ensure stable search performance under heavy loads. These policies include: real-time monitoring of memory usage watermarks; index preloading to mitigate high first-query latency; and dynamic cache reclamation through automatic cache clearing based on predefined idle timeout periods or usage thresholds.

How the Feature Works
---------------------

The CSS vector database divides cluster physical memory into JVM heap memory and off-heap memory. The management policies for off-heap memory are as follows:

-  Upon first hits, vector segments are loaded from the disk into off-heap memory. In this case, queries may experience high latency.
-  Once the data is resident in off-heap memory, all subsequent queries are served directly from the cache, enabling millisecond-level response times.
-  When the memory is full or when the idle timeout period expires, inactive segments are evicted from off-heap memory, ensuring stable query performance under heavy loads.

Monitoring Cache Status
-----------------------

To troubleshoot performance bottlenecks, check each cluster node's off-heap memory utilization and cache hit rate.

Run the following command to monitor the cache status:

.. code-block:: text

   GET /_vector/stats

Example response:

.. code-block::

   {
     "_nodes" : {          # Node information
       "total" : 1,        # Total number of nodes
       "successful" : 1,           # Number of successful nodes
       "failed" : 0        # Number of failed nodes
     },
     "cluster_name" : "css-d3a7",          # Cluster name
     "cpu_circuit_breaker_triggered" : false,  # Whether circuit breaking is triggered
     "nodes" : {
       "cAHmVUZTR9ON7t6jxcDCkg" : {        # Node UUID
         "cpu_cache_capacity_reached" : false,     # Whether the off-heap memory usage of the current node reaches the upper limit
         "cpu_eviction_count" : 0,         # Number of segment-level cache swap-outs on the current node
         "cpu_hit_count" : 0,              # Number of segment-level cache hits on the current node
         "cpu_load_exception_count" : 0,       # Number of segment-level index loading failures on the current node
         "cpu_load_success_count" : 0,         # Number of segment-level index loading successes on the current node
         "cpu_miss_count" : 0,             # Number of segment-level cache misses on the current node
         "cpu_query_memory_usage" : 0,         # Off-heap memory usage on the current node, in KB
         "cpu_total_load_time" : 0         # Total time loading segments to the off-heap memory on the current node, in ms
       }
     }
   }

Preloading Frequently Accessed Indexes
--------------------------------------

Preload frequently accessed or newly ingested indexes to the off-heap memory to mitigate high first-query latency (because data needs to be loaded from disk).

Run the following command to preload a specified index:

.. code-block:: text

   PUT /_vector/warmup/{index_name}

.. table:: **Table 1** Parameter description

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Type            | Default Value   | Description                                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================================+
   | index_name      | String          | N/A             | Specifies one or more vector indexes.                                                                                                             |
   |                 |                 |                 |                                                                                                                                                   |
   |                 |                 |                 | -  Single index: Enter the index name, for example, **my_index**.                                                                                 |
   |                 |                 |                 | -  Multiple indexes: Enter multiple index names and use a comma (,) to separate them, for example, **my_index1,my_index2**.                       |
   |                 |                 |                 | -  Wildcard: Use the wildcard (*) to match multiple indexes. For example, **myindex\*** indicates all indexes whose name starts with **myindex**. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------+

Example response:

.. code-block::

   {
     "_shards" : {
       "total" : 1,
       "successful" : 1,
       "failed" : 0
     }
   }

Configuring an Automatic Cache Clearing Policy
----------------------------------------------

When data is frequently updated or memory resources become constrained, you can enable automatic cache clearing to automatically evict inactive segments and reclaim off-heap memory, ensuring stable query performance under heavy loads.

Run the following command to enable automatic eviction of segments that have exceeded their idle timeout period:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "native.cache.expiry.enabled": "true",
       "native.cache.expiry.time": "30m"
     }
   }

.. table:: **Table 2** Parameter description

   +-----------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                   | Type            | Default Value   | Description                                                                                                                                   |
   +=============================+=================+=================+===============================================================================================================================================+
   | native.cache.expiry.enabled | Boolean         | false           | Whether to enable automatic cache clearing. When enabled, inactive segments are automatically evicted when their idle timeout period expires. |
   |                             |                 |                 |                                                                                                                                               |
   |                             |                 |                 | The value can be:                                                                                                                             |
   |                             |                 |                 |                                                                                                                                               |
   |                             |                 |                 | -  **true**: Enables automatic cache clearing.                                                                                                |
   |                             |                 |                 | -  **false**: Disables automatic cache clearing.                                                                                              |
   +-----------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+
   | native.cache.expiry.time    | String          | 24h             | Idle timeout period for evicting inactive segments.                                                                                           |
   |                             |                 |                 |                                                                                                                                               |
   |                             |                 |                 | Value format: number + unit                                                                                                                   |
   |                             |                 |                 |                                                                                                                                               |
   |                             |                 |                 | -  Number: a natural number                                                                                                                   |
   |                             |                 |                 | -  Unit: s (second), m (minute), h (hour), or d (day)                                                                                         |
   |                             |                 |                 |                                                                                                                                               |
   |                             |                 |                 | Example: **24h** (24 hours) and **30m** (30 minutes).                                                                                         |
   +-----------------------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------+

Manually Clearing the Cache
---------------------------

When off-heap memory reaches its capacity, the system automatically manages data through a "swap-in and swap-out" process. However, frequent, high-volume cache churn can impact query performance. After deleting indexes or switching workloads, you can manually reclaim off-heap memory occupied by inactive index segments to ensure query performance for hot data indexes.

-  Clear the full cache:

   .. code-block:: text

      PUT /_vector/clear/cache

-  Clear specified indexes from the cache:

   .. code-block:: text

      PUT /_vector/clear/cache/{index_name}

Example response:

.. code-block::

   {
     "acknowledged" : "true"
   }
