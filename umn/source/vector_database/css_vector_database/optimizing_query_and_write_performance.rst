:original_name: css_01_0126.html

.. _css_01_0126:

Optimizing Query and Write Performance
======================================

In large-scale vector search scenarios, as vector dimensionality and data volume grow, clusters may face performance bottlenecks such as low write throughput and severe jitter in query latency (P99). Unlike traditional keyword-based search, vector search is defined by compute-intensive index building and memory-intensive retrieval. Standard Elasticsearch and OpenSearch configurations may struggle with the complex topology computations involved. To address these challenges, the CSS vector database supports full-stack performance tuning for clusters, covering both write and query. It helps you achieve the optimal balance between system performance and costs while ensuring high recall.

Optimizing Write Performance
----------------------------

Vector data ingestion involves three major overheads: replica synchronization, index refresh, and segment merging. During real-time index data ingestion, frequent index refresh operations generate a large number of small segments. This triggers frequent vector index build and merge operations, which consume excessive CPU/IO resources. You can try the following solutions to optimize write performance.

Solution 1: Temporarily disable replicas

-  Description

   Temporarily disable replicas during data ingestion and enable them after data ingestion is complete. Use this solution when importing historical data in batches or performing a full update (for example, when initializing a vector database).

-  Operation

   Set the number of replicas:

   .. code-block:: text

      PUT {index_name}/_settings
      {
          "number_of_replicas": 0
      }

-  Result

   Write performance is enhanced by avoiding real-time vector index building on replica nodes.

Solution 2: Adjust the refresh interval

-  Description

   Set the index refresh interval to 120s or longer to reduce the number of small segments generated during frequent index refreshes and also reduce the vector index building overhead caused by segment merges. You can also disable automatic index refresh by setting the refresh interval to -1. Use this solution in high-throughput write scenarios (for example, when writing vectorized log data).

-  Operation

   Set **refresh_interval**.

   .. code-block:: text

      PUT {index_name}/_settings
      {
          "refresh_interval": "120s"
      }

-  Result

   Index refreshes occur less frequently. This reduces the number of small segments and also the overhead of segment merges, leading to enhanced write performance.

Solution 3: Increase indexing threads

-  Description

   Increasing the number of threads for vector index building accelerates the indexing process. However, too many such threads will compete for query resources. Use this solution when there are sufficient CPU resources but the write latency is high—such as in GPU-accelerated environments.

-  Operation

   The default value of **native.vector.index_threads** is 4. Change this value as needed.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "native.vector.index_threads": 8
        }
      }

-  Result

   Vector index building is accelerated, and concurrent write performance is enhanced.

Optimizing Query Performance
----------------------------

Query performance is affected by the following factors: the number of segments, the memory circuit breaker mechanism, and field recall. An excessively large number of segments impacts search efficiency; when off-heap memory becomes insufficient, vector index data is frequently swapped in and out of the memory; recalling all fields increases the load during the fetch phase. You can optimize query performance by addressing these factors.

Solution 1: Perform force merge

-  Description

   After batch data ingestion, perform the force merge operation to forcibly merge segments, thus reducing the number of segments. Typically, you should perform this operation after data ingestion and before data query (for example, after a scheduled batch ingestion).

-  Operation

   Perform the force merge operation:

   .. code-block:: text

      POST {index_name}/_forcemerge?max_num_segments=1

-  Result

   Multiple segments are merged into a single segment. This reduces the file scanning overhead and accelerates the query speed.

Solution 2: Adjust the automatic merge policy

-  Description

   In real-time ingestion and update scenarios, many small, fragmented segments may be created. You can tune the automatic merge policy to accelerate the merging of these segments into larger ones. This reduces the total number of segments and improves query performance.

-  Operation

   Adjust the automatic merge policy for an index.

   .. code-block:: text

      PUT {index_name}/_settings
      {
        "index": {
          "merge": {
            "policy": {
              "max_merged_segment": "10gb",
              "max_merge_at_once": 10,
              "segments_per_tier": 5,
              "floor_segment": "200mb"
            }
          }
        }
      }

   .. table:: **Table 1** Parameters for adjusting the automatic merge policy

      +--------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter          | Type            | Default Value   | Description                                                                                                                                                                                                                                                                                                                                |
      +====================+=================+=================+============================================================================================================================================================================================================================================================================================================================================+
      | max_merged_segment | String          | 5GB             | Maximum segment size after merging. Segments exceeding this size are excluded from automatic merging, but they remain eligible for forcible merge. This prevents segments from growing indefinitely, as they may block I/O links. For vector indexes, increasing this value helps reduce the total number of segments.                     |
      |                    |                 |                 |                                                                                                                                                                                                                                                                                                                                            |
      |                    |                 |                 | Value format: positive integer + unit.                                                                                                                                                                                                                                                                                                     |
      |                    |                 |                 |                                                                                                                                                                                                                                                                                                                                            |
      |                    |                 |                 | Supported units: B, KB, MB, and GB (case-insensitive).                                                                                                                                                                                                                                                                                     |
      +--------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | max_merge_at_once  | Integer         | 10              | Maximum number of segments that can be processed in a single merge task. Increasing this value can reduce the total number of segments, but will lead to high disk I/O and CPU spikes during the merge.                                                                                                                                    |
      |                    |                 |                 |                                                                                                                                                                                                                                                                                                                                            |
      |                    |                 |                 | Minimum value: 2                                                                                                                                                                                                                                                                                                                           |
      +--------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | segments_per_tier  | Integer         | 10              | Maximum number of segments per tier. A smaller value indicates more frequent merging and faster query, but higher I/O pressure. A larger value enhances write throughput but may compromise query performance. You can decrease this value to trigger automatic merging more frequently and thus reduce the number of fragmented segments. |
      |                    |                 |                 |                                                                                                                                                                                                                                                                                                                                            |
      |                    |                 |                 | Value range: >= max_merge_at_once                                                                                                                                                                                                                                                                                                          |
      +--------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | floor_segment      | String          | 2MB             | Minimum segment size. Segments below this threshold will be merged first. You can increase this value to trigger automatic merging more frequently and thus reduce the number of fragmented segments.                                                                                                                                      |
      |                    |                 |                 |                                                                                                                                                                                                                                                                                                                                            |
      |                    |                 |                 | Value format: positive integer + unit.                                                                                                                                                                                                                                                                                                     |
      |                    |                 |                 |                                                                                                                                                                                                                                                                                                                                            |
      |                    |                 |                 | Supported units: B, KB, MB, and GB (case-insensitive).                                                                                                                                                                                                                                                                                     |
      +--------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Result

   Increasing the maximum segment size helps to reduce the number of segments and thus accelerate query performance.

Solution 3: Adjust the circuit breaker limit for off-heap memory

-  Description

   When the off-heap memory required by vector indexes exceeds the circuit breaker limit, the index cache manager frequently swaps in and out index data from the cache, which slows down queries. You can raise the circuit breaker limit to reduce circuit breaking (indicated by CircuitBreakingException recorded in the log) resulted from insufficient memory.

-  Operation

   The default circuit breaker limit for off-heap memory is 80%. You can adjust this limit as required.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "native.cache.circuit_breaker.cpu.limit": "85%"
        }
      }

-  Result

   It is less likely for vector index data to be swapped out from the memory, and query jitter is reduced.

Solution 4: Optimize field recall

-  Description

   If the query result needs to return only a few fields that are either keywords or numeric values, you can use the docvalue_fields parameter to fetch them. Use this method if only numeric or enumerated metadata (such as product IDs and class labels) needs to be fetched. It can significantly reduce overhead during the fetch phase.

-  Operation

   Use the docvalue_fields parameter to fetch only specific fields:

   .. code-block:: text

      POST {index_name}/_search
      {
        "size": 2,
        "stored_fields": ["_none_"],
        "docvalue_fields": ["my_label"],
        "query": {
          "vector": {
            "my_vector": {
              "vector": [1, 1],
              "topk": 2
            }
          }
        }
      }

-  Result

   There is no need to parse the entire \_source document. Column-oriented storage (docvalues) reduces the overhead during the fetch phase and improves query performance.
