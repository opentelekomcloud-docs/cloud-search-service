:original_name: css_01_0465.html

.. _css_01_0465:

About Vector Search
===================

Unstructured data, such as images, videos, and language corpora, is converted into vectors, which are searched based on similarity using either an exact or approximate nearest neighbors algorithm.

How It Works
------------

Vector search works in a way similar to traditional search. To improve vector search performance, we need to:

-  **Narrow down the matched scope**

   Similar to traditional text search, vector search use indexes to accelerate the search instead of going through all data. Traditional text search uses inverted indexes to filter out irrelevant documents, whereas vector search creates indexes for vectors to bypass irrelevant vectors, narrowing down the search scope.

-  **Reduce the complexity of calculating a single vector**

   The vector search method can quantize and approximate high dimensional vectors first. By doing this, a smaller and more relevant dataset can be obtained. Then more sophisticated algorithms are applied to this smaller dataset to perform computation and sorting. This way, complex computation is performed on only part of the vectors, and efficiency is improved.

Vector search means to retrieve the k-nearest neighbors (KNN) to the query vector in a given vector data set by using a specific measurement method. Generally, CSS only focuses on Approximate Nearest Neighbor (ANN), because a KNN search requires excessive computational resources.

Description
-----------

The CSS vector search engine integrates a variety of vector indexes, such as brute-force search, Hierarchical Navigable Small World (HNSW) graphs, product quantization, and IVF-HNSW. It also supports multiple similarity calculation methods, such as Euclidean, inner product, cosine, and Hamming. The recall rate and retrieval performance of the engine are better than those of open-source engines. It can meet the requirements for high performance, high precision, low costs, and multi-modal computation.

The search engine also supports all the capabilities of the native OpenSearch, including distribution, multi-replica, error recovery, snapshot, and permission control. The engine is compatible with the native OpenSearch ecosystem, including the cluster monitoring tool Cerebro, the visualization tool Kibana, and the real-time data ingestion tool Logstash. Several client languages, such as Python, Java, Go, and C++, are supported.

Constraints
-----------

-  The built-in CSS vector search engine is available for OpenSearch 1.3.6 clusters only.
-  The vector search plug-in performs in-memory computing and requires more memory than common indexes do. You are advised to use memory-optimized compute specifications.

.. _css_01_0465__css_01_0118_section18221195417136:

Cluster Node Specifications Selection for Vector Search
-------------------------------------------------------

Off-heap memory is used for index construction and query in vector search. Therefore, the required cluster capacity is related to the index type and off-heap memory size. You can estimate the off-heap memory required by full indexing to select the appropriate cluster specifications. Due to high memory usage of vector search, CSS disables the vector search plug-in by default for clusters whose memory is 8 GB or less.

There are different methods for estimating the size of off-heap memory required by different types of indexes. The calculation formulas are as follows:

-  **GRAPH index**

   mem_needs = (dim x dim_size + neighbors x 4) x num + delta

   .. note::

      If you need to update indexes in real time, consider the off-heap memory overhead required for vector index construction and automatic merge. The actual size of required **mem_needs** is at least 1.5 to 2 times of the original estimation.

-  **PQ index**

   mem_needs = frag_num x frag_size x num + delta

-  **FLAT and IVF indexes**

   mem_needs = dim x dim_size x num + delta

.. table:: **Table 1** Parameter description

   +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Description                                                                                                                                                                      |
   +===================================+==================================================================================================================================================================================+
   | dim                               | Vector dimensionality                                                                                                                                                            |
   +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | neighbors                         | Number of neighbors of a graph node. The default value is **64**.                                                                                                                |
   +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | dim_size                          | Number of bytes required by each dimension. The default value is four bytes in the float type.                                                                                   |
   +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | num                               | Total number of vectors                                                                                                                                                          |
   +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | delta                             | Metadata size. This parameter can be left blank.                                                                                                                                 |
   +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | frag_num                          | Number of vector segments during quantization and coding. If this parameter is not specified when an index is created, the value is determined by vector dimensionality **dim**. |
   |                                   |                                                                                                                                                                                  |
   |                                   | .. code-block::                                                                                                                                                                  |
   |                                   |                                                                                                                                                                                  |
   |                                   |    if dim <= 256:                                                                                                                                                                |
   |                                   |      frag_num = dim / 4                                                                                                                                                          |
   |                                   |    elif dim <= 512:                                                                                                                                                              |
   |                                   |      frag_num = dim / 8                                                                                                                                                          |
   |                                   |    else :                                                                                                                                                                        |
   |                                   |      frag_num = 64                                                                                                                                                               |
   +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | frag_size                         | Size of the center point during quantization and coding. The default value is 1.                                                                                                 |
   +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

These calculation methods can estimate the size of off-heap memory required by a complete vector index. To determine cluster specifications, you also need to consider the heap memory overhead of each node.

Heap memory allocation policy: The size of the heap memory of each node is half of the node physical memory, and the maximum size is **31 GB**.

For example, if you create a Graph index for the SIFT10M dataset, with **dim** set to **128**, **dim_size** to **4**, **neighbors** to the default value **64**, and **num** to **10 million**, the off-heap memory required by the Graph index is around 7.5 GB. Calculation formula: **mem_needs = (128 x 4 + 64 x 4) x 10000000 ≈ 7.5**.

Considering the overhead of heap memory, a single server with **8 vCPUs** and **16 GB memory** is recommended. If real-time write or update is required, you need to apply for larger memory.
