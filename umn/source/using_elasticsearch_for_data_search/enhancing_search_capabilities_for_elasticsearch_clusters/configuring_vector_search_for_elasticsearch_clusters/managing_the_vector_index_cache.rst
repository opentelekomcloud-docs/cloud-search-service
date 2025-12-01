:original_name: css_01_0130.html

.. _css_01_0130:

Managing the Vector Index Cache
===============================

The CSS vector search engine is built on C++. It uses off-heap memory to enhance performance and efficiency. To better manage and optimize the vector index cache, the CSS vector database provides a number of dedicated APIs that can be used to flexibly monitor and tune cache usage to ensure stable query performance.

Checking Cache Statistics
-------------------------

Use the following API to check the off-heap memory usage and return key metrics such as the current off-heap memory usage, cache hits, and data loading times. These metrics help you understand the cache status, so you can adjust the cache based on its usage. In the implementation of the vector search plug-in, each segment constructs and stores an index file. During query, all these files are loaded to the off-heap memory, and the plug-in uses a cache mechanism to manage the off-heap memory.

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
         "cpu_total_load_time" : 0         # Total segment-level index loading time on the current node, in ms
       }
     }
   }

Preloading Vector Indexes
-------------------------

Use the following API to preload specified vector indexes to the off-heap memory. This ensures that these indexes can be quickly accessed in subsequent queries, with high query efficiency and low latency.

.. code-block:: text

   PUT /_vector/warmup/{index_name}

where, {index_name} specifies an index.

Example response:

.. code-block::

   {
     "_shards" : {
       "total" : 1,
       "successful" : 1,
       "failed" : 0
     }
   }

Clearing the Cache
------------------

When the cache is full, the system automatically swaps its data. However, frequent cache swapping may affect query performance. You can use the following API to manually clear the vector index cache. This way, you can reclaim off-heap memory resources and ensure hot data query performance.

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
