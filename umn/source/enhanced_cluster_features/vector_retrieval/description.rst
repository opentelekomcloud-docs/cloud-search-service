:original_name: en-us_topic_0000001528299617.html

.. _en-us_topic_0000001528299617:

Description
===========

Image recognition and retrieval, video search, and personalized recommendation impose high requirements on the latency and accuracy of high-dimensional space vector retrieval. To facilitate large-scale vector search, CSS integrates the vector search feature powered by vector search engine and the Elasticsearch plug-in mechanism.

Principles
----------

Vector search works in a way similar to traditional search. To improve vector search performance, we need to:

-  **Narrow down the matched scope**

   Similar to traditional text search, vector search use indexes to accelerate the search instead of going through all data. Traditional text search uses inverted indexes to filter out irrelevant documents, whereas vector search creates indexes for vectors to bypass irrelevant vectors, narrowing down the search scope.

-  **Reduce the complexity of calculating a single vector**

   The vector search method can quantize and approximate high dimensional vectors first. By doing this, you can acquire a smaller and more relevant data set. Then more sophisticated algorithms are applied to this smaller data set to perform computation and sorting. This way, complex computation is performed on only part of the vectors, and efficiency is improved.

Vector search means to retrieve the k-nearest neighbors (KNN) to the query vector in a given vector data set by using a specific measurement method. Generally, CSS only focuses on Approximate Nearest Neighbor (ANN), because a KNN search requires excessive computational resources.

Functions
---------

The engine integrates a variety of vector indexes, such as brute-force search, Hierarchical Navigable Small World (HNSW) graphs, product quantization, and IVF-HNSW. It also supports multiple similarity calculation methods, such as Euclidean, inner product, cosine, and Hamming. The recall rate and retrieval performance of the engine are better than those of open-source engines. It can meet the requirements for high performance, high precision, low costs, and multi-modal computation.

The search engine also supports all the capabilities of the native Elasticsearch, including distribution, multi-replica, error recovery, snapshot, and permission control. The engine is compatible with the native Elasticsearch ecosystem, including the cluster monitoring tool Cerebro, the visualization tool Kibana, and the real-time data ingestion tool Logstash. Several client languages, such as Python, Java, Go, and C++, are supported.

Constraints
-----------

-  Only Elasticsearch clusters of versions 7.6.2 and 7.10.2 and OpenSearch clusters of version 1.3.6 support vector search.
-  The vector search plug-in performs in-memory computing and requires more memory than common indexes do. It is recommended that the memory of the cluster node be greater than or equal to 8 GB and the cluster computing specifications be memory-optimized.
