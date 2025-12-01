:original_name: css_01_0195.html

.. _css_01_0195:

Creating an Elasticsearch Vector Cluster
========================================

Integrating efficient indexing techniques, the CSS vector database delivers a high-performance, low-cost, scalable solution for high-dimensional vector search. An Elasticsearch vector cluster converts unstructured data into high-dimensional vectors and uses vector indexing algorithms (such as HNSW graph-based indexing and product quantization) to enable approximate nearest neighbor (ANN) search. This significantly reduces computational complexity while ensuring a high recall rate.

This topic focus on the memory capacity requirements and planning for an Elasticsearch vector cluster, so as to provide guidance on how to choose cluster nodes of the appropriate specifications. All other procedures are the same as those for other regular search clusters. For details, see :ref:`Elasticsearch Cluster Planning Suggestions <css_01_0188>`.

Memory Planning
---------------

Before creating an Elasticsearch vector cluster, properly plan the cluster's memory capacity based on the data size, vector dimensions, and index types.

-  **Node type**

   The CSS vector search engine relies heavily on in-memory computing, and vector indexing relies on off-heap memory. For a vector cluster, we recommend **memory-optimized** nodes.

-  **Memory calculation formula**

   Estimate the required off-heap memory based on the index algorithms used, vector dimensions, and data volume.

   -  FLAT index: mem_size = dim x dim_size x num + delta
   -  GRAPH index: mem_size = (dim x dim_size + neighbors x 4) x num + delta
   -  GRAPH_PQ index: mem_size = (fragment_num + neighbors x 4) x num + delta
   -  GRAPH_SQ8 index: mem_size = (dim x 2 + neighbors x 4) x num + delta
   -  GRAPH_SQ4 index: mem_size = (dim + neighbors x 4) x num + delta
   -  IVF_GRAPH and IVF_GRAPH_PQ indexes do not require resident memory, so there is need to estimate their memory requirements.

   .. table:: **Table 1** Parameter description

      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                         |
      +===================================+=====================================================================================================================================================================================================+
      | mem_size                          | Size of off-heap memory required by vector indexes. (This estimate assumes there are no replicas. If index replicas are involved, the required memory size multiplies with the number of replicas.) |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | dim                               | Number of vector dimensions.                                                                                                                                                                        |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | dim_size                          | Number of bytes required by each dimension. By default, each dimension is a 4-byte float value.                                                                                                     |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | neighbors                         | Number of neighbors for each vector in a graph index. The default value is 64.                                                                                                                      |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | num                               | Total number of vectors.                                                                                                                                                                            |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | fragment_num                      | Number of segments a vector is split into when product quantization is used.                                                                                                                        |
      |                                   |                                                                                                                                                                                                     |
      |                                   | If fragment_num is not configured during index creation, the value is determined by **dim**.                                                                                                        |
      |                                   |                                                                                                                                                                                                     |
      |                                   | .. code-block::                                                                                                                                                                                     |
      |                                   |                                                                                                                                                                                                     |
      |                                   |    if dim <= 256:                                                                                                                                                                                   |
      |                                   |      fragment_num = dim / 4                                                                                                                                                                         |
      |                                   |    elif dim <= 512:                                                                                                                                                                                 |
      |                                   |      fragment_num = dim / 8                                                                                                                                                                         |
      |                                   |    else :                                                                                                                                                                                           |
      |                                   |      fragment_num = 64                                                                                                                                                                              |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | delta                             | Metadata size. This factor can be ignored.                                                                                                                                                          |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   When selecting node specifications, you also need to consider the heap memory overhead of each node. Heap memory allocation policy: The size of the heap memory of each node is half of the node's physical memory, and the maximum size is **31 GB**.

   Example:

   When creating a graph index based on the SIFT10M dataset (128-dimensional vector, 10 million records), if **neighbors** is set to 32, the off-heap memory required is as follows: **mem_size = (128 x 4 + 32 x 4) x 10,000,000 + delta ≈ 6 GB**. If one index replica is needed, at least 12 GB (6 x 2) of off-heap memory is required. In this case, select one 8U32G or two 8U16G node for the cluster.

Creating a Cluster
------------------

The procedure for creating a vector cluster is the same as that for creating any other regular search cluster. For details, see :ref:`Creating an Elasticsearch Cluster <css_01_0270>`.

Pay attention to the following key parameters:

-  **Cluster Version**: Select 7.6.2 or 7.10.2. Only clusters of these two versions support the built-in CSS vector search engine.
-  **Node Specifications**: Select the node specifications based on the result of cluster memory planning.

(Optional) Configuring the Circuit Breaker
------------------------------------------

To mitigate out-of-memory (OOM) errors and maintain optimal vector query performance, a circuit breaker mechanism is employed. When the cluster's off-heap memory usage exceeds a predefined threshold, this mechanism automatically blocks vector data writes to the cluster. The purposes of this mechanism are as follows:

-  Preventing memory overload: Write throttling lowers off-heap memory usage.
-  Maintaining query performance: Optimal vector query performance can be maintained by preventing memory overload.

The off-heap memory circuit breaker is enabled by default. You can enable or disable it and adjust its threshold based on service requirements. The command is as follows:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "native.cache.circuit_breaker.enabled": "true",
       "native.cache.circuit_breaker.cpu.limit": "80%"
     }
   }

.. table:: **Table 2** Parameter description

   +----------------------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                              | Type                  | Description                                                                                                                                                                                                                                                                        |
   +========================================+=======================+====================================================================================================================================================================================================================================================================================+
   | native.cache.circuit_breaker.enabled   | Boolean               | Whether to enable the off-heap memory circuit breaker.                                                                                                                                                                                                                             |
   |                                        |                       |                                                                                                                                                                                                                                                                                    |
   |                                        |                       | Value range:                                                                                                                                                                                                                                                                       |
   |                                        |                       |                                                                                                                                                                                                                                                                                    |
   |                                        |                       | -  **true** (default value): Enable the off-heap memory circuit breaker. When the off-heap memory usage reaches the circuit breaker threshold, write requests are blocked.                                                                                                         |
   |                                        |                       | -  **false**: Disable the off-heap memory circuit breaker. OOM errors may occur in case of excessive off-heap memory usage.                                                                                                                                                        |
   +----------------------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | native.cache.circuit_breaker.cpu.limit | String                | Circuit breaker threshold in terms of maximum off-heap memory usage.                                                                                                                                                                                                               |
   |                                        |                       |                                                                                                                                                                                                                                                                                    |
   |                                        |                       | This parameter is available only when **native.cache.circuit_breaker.enabled=true**.                                                                                                                                                                                               |
   |                                        |                       |                                                                                                                                                                                                                                                                                    |
   |                                        |                       | Value range: a value in percentage                                                                                                                                                                                                                                                 |
   |                                        |                       |                                                                                                                                                                                                                                                                                    |
   |                                        |                       | Default value: 80%                                                                                                                                                                                                                                                                 |
   |                                        |                       |                                                                                                                                                                                                                                                                                    |
   |                                        |                       | Assume a cluster uses 128 GB memory. The required heap memory is 31 GB, and the default circuit breaker threshold is 80%, then: (128 - 31) x 80% = 77.6 GB. This means when the off-heap memory usage exceeds 77.6 GB, the circuit breaker is triggered to block write operations. |
   +----------------------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
