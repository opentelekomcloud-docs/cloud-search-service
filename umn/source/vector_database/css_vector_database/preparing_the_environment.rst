:original_name: css_01_0195.html

.. _css_01_0195:

Preparing the Environment
=========================

During environment preparation for a CSS vector database, estimate memory requirements based on vector dimensions, data volume, and the selected indexing algorithm (such as HNSW or PQ); and configure an appropriate circuit breaker threshold. They help build a vector search environment that delivers both high performance and enterprise-grade reliability.

.. _en-us_topic_0000002554790925__section1710010020225:

Planning Memory Capacity
------------------------

On each node of a CSS vector database, the physical memory is divided into two logical areas:

-  JVM heap memory: used for service processing, such as index metadata mapping, aggregation queries, and cluster management. By default, this accounts for 50% of the physical memory, with an upper limit of 31 GB.
-  Off-heap memory: used for vector computations. Graph index structures that require resident memory are directly loaded into off-heap memory to enable high-speed parallel computation.

Before selecting cluster node specifications, calculate the required off-heap memory based on the selected indexing algorithm. :ref:`Table 1 <en-us_topic_0000002554790925__table2388155616495>` provides the formulas for estimating the off-heap memory required by a single index replica for each indexing algorithm.

.. _en-us_topic_0000002554790925__table2388155616495:

.. table:: **Table 1** Estimating off-heap memory per indexing algorithm

   +--------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Algorithm    | Off-Heap Memory Formula (Unit: Bytes)                                          | Algorithm Description                                                                                                                                                                                                                          |
   +==============+================================================================================+================================================================================================================================================================================================================================================+
   | FLAT         | mem_size = dim \* dim_size \* num + delta                                      | Full brute-force indexing. Suitable for: Datasets with less than 10,000 records, or scenarios requiring maximum recall accuracy.                                                                                                               |
   +--------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | GRAPH        | mem_size = (dim \* dim_size + neighbors \* 4) \* num + delta                   | Hierarchical Navigable Small Worlds (HNSW), a graph-based indexing algorithm for efficient approximate nearest neighbor (ANN) search. Suitable for: Datasets up to 100 million records, millisecond-level latency and high precision required. |
   +--------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | GRAPH_PQ     | mem_size = (fragment_num + neighbors \* 4) \* num + delta                      | A combination of HNSW with product quantization (PQ). Suitable for: Datasets with up to a billion records.                                                                                                                                     |
   +--------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | GRAPH_SQ8    | mem_size = (dim + neighbors \* 4) \* num + delta                               | A combination of HNSW with 8-bit scalar quantization. Suitable for: Datasets with up to a billion records.                                                                                                                                     |
   +--------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | GRAPH_SQ4    | mem_size = (dim / 2 + neighbors \* 4) \* num + delta                           | A combination of HNSW with 4-bit scalar quantization. Suitable for: Datasets with up to a billion records.                                                                                                                                     |
   +--------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | IVF_GRAPH    | Relies on a pre-built centroid vector dictionary; no resident memory required. | A combination of Inverted File Index (IVF) with HNSW. Suitable for: Use cases that demand high write performance.                                                                                                                              |
   +--------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | IVF_GRAPH_PQ | Relies on a pre-built centroid vector dictionary; no resident memory required. | A combination of IVF, HNSW, and PQ. Suitable for: Use cases that demand high write throughput.                                                                                                                                                 |
   +--------------+--------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Parameter description:

-  **mem_size**: The size of off-heap memory required by vector indexes. (This estimate assumes there are no replicas. If index replicas are involved, the required memory size multiplies with the number of replicas.)

-  **dim**: Number of vector dimensions.

-  **dim_size**: Number of bytes required by each dimension. By default, each dimension is a 4-byte float value.

-  **num**: Total number of vectors.

-  **delta**: Metadata size. This factor can be ignored.

-  **neighbors**: Number of neighbors for each vector in a graph index. The default value is 64.

-  **fragment_num**: Number of segments a vector is split into when product quantization is used.

   If fragment_num is not configured during index creation, the value is determined by **dim**.

   .. code-block::

      if dim <= 256:
          fragment_num = dim / 4
      elif dim <= 512:
          fragment_num = dim / 8
      else:
          fragment_num = 64

**Example**

Scenario: SIFT10M dataset (128-dimensional vectors and 10 million records), GRAPH algorithm, 64 neighbors, one replica.

#. Off-heap memory for a single replica: mem_size = (128 \* 4 + 64 \* 4) x 10,000,000 + delta ≈ 7.7 GB
#. Off-heap memory for two replicas: 7.7 x 2 = 15.4 GB
#. Safety guarantee considering the circuit breaker (assume the default circuit breaker threshold is 80%): 15.4/80% = 19.3 GB
#. Final node specifications: The JVM heap memory accounts for 50% of the physical memory (no more than 31 GB). Therefore, you should select a node with 64 GB memory (for example, 8U64G) or two nodes each with 32 GB memory (for example, 8U32G).

Creating a Cluster
------------------

The CSS vector database is based on Elasticsearch or OpenSearch clusters. Create an Elasticsearch or OpenSearch cluster based on service requirements. :ref:`Table 2 <en-us_topic_0000002554790925__table67371341152017>` describes the key parameters.

.. _en-us_topic_0000002554790925__table67371341152017:

.. table:: **Table 2** Key parameters for creating a cluster

   +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Cluster Type          | Elasticsearch                                                                                                                                               | OpenSearch                                                                                                                                                  |
   +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Cluster Version       | Select **7.6.2** or **7.10.2**. Other versions do not support the CSS vector search engine.                                                                 | Select **1.3.6** or **2.19.0**. Other versions do not support the CSS vector search engine.                                                                 |
   |                       |                                                                                                                                                             |                                                                                                                                                             |
   |                       | **7.10.2** is recommended, because it provides more comprehensive features.                                                                                 | **2.19.0** is recommended, because it provides more comprehensive features.                                                                                 |
   +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | CPU Architecture      | **x86** is recommended.                                                                                                                                     | **x86** is recommended.                                                                                                                                     |
   +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Node Specifications   | You are advised to select a **Memory-optimized** flavor. Flavors of this type have a high memory-to-CPU ratio, making them ideal for vector computations.   | You are advised to select a **Memory-optimized** flavor. Flavors of this type have a high memory-to-CPU ratio, making them ideal for vector computations.   |
   |                       |                                                                                                                                                             |                                                                                                                                                             |
   |                       | The cluster's physical memory must meet the requirements described in :ref:`Planning Memory Capacity <en-us_topic_0000002554790925__section1710010020225>`. | The cluster's physical memory must meet the requirements described in :ref:`Planning Memory Capacity <en-us_topic_0000002554790925__section1710010020225>`. |
   +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Documentation         | :ref:`Creating a Cluster <css_01_0270>`.                                                                                                                    | :ref:`Creating a Cluster <css_01_0269>`.                                                                                                                    |
   +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

(Optional) Configuring the Circuit Breaker
------------------------------------------

To mitigate out-of-memory (OOM) errors and maintain optimal vector query performance, a circuit breaker mechanism is employed. When the cluster's off-heap memory usage exceeds a predefined threshold, this mechanism automatically blocks vector data writes to the cluster.

The purposes of this mechanism are as follows:

-  Preventing memory overload: Write throttling lowers off-heap memory usage.
-  Maintaining query performance: Optimal vector query performance can be maintained by preventing memory overload.

The off-heap memory circuit breaker is enabled by default. You can enable or disable it and adjust its threshold based on service requirements.

Run the following command on Dev Tools in Kibana or OpenSearch Dashboards:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "native.cache.circuit_breaker.enabled": "true",
       "native.cache.circuit_breaker.cpu.limit": "80%"
     }
   }

.. table:: **Table 3** Circuit breaker parameters

   +----------------------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                              | Type            | Default Value   | Description                                                                                                                                                                                                                                                                        |
   +========================================+=================+=================+====================================================================================================================================================================================================================================================================================+
   | native.cache.circuit_breaker.enabled   | Boolean         | true            | Whether to enable the off-heap memory circuit breaker.                                                                                                                                                                                                                             |
   |                                        |                 |                 |                                                                                                                                                                                                                                                                                    |
   |                                        |                 |                 | The value can be:                                                                                                                                                                                                                                                                  |
   |                                        |                 |                 |                                                                                                                                                                                                                                                                                    |
   |                                        |                 |                 | -  **true**: Enable the off-heap memory circuit breaker. When the off-heap memory usage reaches the circuit breaker threshold, write requests are blocked.                                                                                                                         |
   |                                        |                 |                 | -  **false**: Disable the off-heap memory circuit breaker. OOM errors may occur in case of excessive off-heap memory usage.                                                                                                                                                        |
   +----------------------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | native.cache.circuit_breaker.cpu.limit | String          | 80%             | Circuit breaker threshold in terms of maximum off-heap memory usage.                                                                                                                                                                                                               |
   |                                        |                 |                 |                                                                                                                                                                                                                                                                                    |
   |                                        |                 |                 | This parameter is available only when **native.cache.circuit_breaker.enabled=true**.                                                                                                                                                                                               |
   |                                        |                 |                 |                                                                                                                                                                                                                                                                                    |
   |                                        |                 |                 | Value range: a value in percentage                                                                                                                                                                                                                                                 |
   |                                        |                 |                 |                                                                                                                                                                                                                                                                                    |
   |                                        |                 |                 | Assume a cluster uses 128 GB memory. The required heap memory is 31 GB, and the default circuit breaker threshold is 80%, then: (128 - 31) x 80% = 77.6 GB. This means when the off-heap memory usage exceeds 77.6 GB, the circuit breaker is triggered to block write operations. |
   +----------------------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
