:original_name: css_01_0126.html

.. _css_01_0126:

Optimizing the Performance of Vector Retrieval
==============================================

Optimizing Write Performance
----------------------------

-  To reduce the cost of backup, disable the backup function before data import and enable it afterwards.

-  Set **refresh_interval** to **120s** or a larger value. Larger segments can reduce the vector index build overhead caused by merging.

-  Increase the value of **native.vector.index_threads** (the default value is **4**) to increase the number of threads for vector index build.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "native.vector.index_threads": 8
        }
      }

Optimizing Query Performance
----------------------------

-  After importing data in batches, you can run the **forcemerge** command to improve the query efficiency.

   .. code-block:: text

      POST index_name/_forcemerge?max_num_segments=1

-  If the off-heap memory required by the vector index exceeds the circuit breaker limit, index entry swap-in and swap-out occur, which affects the query performance. In this case, you can increase the circuit breaker threshold of off-heap memory.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "native.cache.circuit_breaker.cpu.limit": "75%"
        }
      }

-  If the end-to-end latency is greater than the **took** value in the returned result, you can configure **\_source** to reduce the **fdt** file size and reduce the **fetch** overhead.

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index": {
            "vector": "true"
          },
          "index.soft_deletes.enabled": false
        },
        "mappings": {
          "_source": {
            "excludes": ["my_vector"]
          },
          "properties": {
            "my_vector": {
              "type": "vector",
              "dimension": 128,
              "indexing": true,
              "algorithm": "GRAPH",
              "metric": "euclidean"
            }
          }
        }
      }
