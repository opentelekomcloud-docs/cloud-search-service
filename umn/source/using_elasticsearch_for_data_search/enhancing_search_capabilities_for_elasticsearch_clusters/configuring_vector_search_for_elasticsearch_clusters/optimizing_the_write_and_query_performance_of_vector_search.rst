:original_name: css_01_0126.html

.. _css_01_0126:

Optimizing the Write and Query Performance of Vector Search
===========================================================

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

-  To fetch a small number of fields that support doc values, such as keywords and numerical fields, use the docvalue_fields parameter to specify the fields you want to fetch. This helps to reduce overhead during the fetch phase.

   .. code-block:: text

      POST my_index/_search
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
