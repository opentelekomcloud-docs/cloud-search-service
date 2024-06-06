:original_name: en-us_topic_0000001477899208.html

.. _en-us_topic_0000001477899208:

Managing the Vector Index Cache
===============================

The vector retrieval engine is developed in C++ and uses off-heap memory. You can use the following APIs to manage the index cache.

-  **View cache statistics.**

   .. code-block:: text

      GET /_vector/stats

   In the implementation of the vector plug-in, the vector index is the same as other types of Lucene indexes. Each segment constructs and stores an index file. During query, the index file is loaded to the non-heap memory. The plug-in uses the cache mechanism to manage the non-heap memory. You can use this API to query the non-heap memory usage, number of cache hits, and number of loading times.

-  **Preload the vector index.**

   .. code-block:: text

      PUT /_vector/warmup/{index_name}

   You can use this API to preload the vector index specified by **index_name** to the off-heap memory for query.

-  **Clear the cache.**

   .. code-block:: text

      PUT /_vector/clear/cache

   .. code-block:: text

      PUT /_vector/clear/cache/index_name

   The caching mechanism limits the non-heap memory usage when vector indexes are used. When the total index size exceeds the cache size limit, index entry swap-in and swap-out occur, which affects the query performance. You can use this API to clear unnecessary index cache to ensure the query performance of hot data indexes.
