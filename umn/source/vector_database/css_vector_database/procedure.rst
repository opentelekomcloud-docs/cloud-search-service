:original_name: css_01_0118.html

.. _css_01_0118:

Procedure
=========

In the age of AI, unstructured data, such as images, videos, audios, and text, is growing rapidly. Traditional keyword-based search cannot effectively handle unstructured data because it fails to capture deep semantic or visual features. The CSS vector database addresses this challenge. Designed for storing, managing, and retrieving high-dimensional vectors, it transforms unstructured data into vectors and leverages techniques like approximate nearest neighbor (ANN) search to enable high-throughput, high-accuracy similarity search.

Use Cases
---------

The CSS vector database supports a diverse range of use cases:

-  Reverse image/video search: Upload an image or video clip to quickly retrieve visually similar images or videos from massive datasets.
-  Similar product recommendations: Based on the item you are currently viewing, the system intelligently recommends other products with similar appearance, functionality, or attributes, improving user experience and conversion rates.
-  Semantic text search: Unlike traditional keyword search, the vector database understands the semantic meaning of text and returns results more aligned with your query intent, even if the text does not contain exact keyword matches.
-  Cross-modal search: The vector database enables seamless search across different data modalities. For example, you can enter a textual description to search for relevant images or videos.
-  Retrieval-augmented generation (RAG): In an LLM-powered Q&A system, the vector database serves as an external knowledge base for the LLM, supporting efficient retrieval of domain-specific knowledge. This ensures the model generates answers that are more accurate, more contextually relevant, and more firmly grounded in domain-specific knowledge.

Advantages
----------

The CSS vector database delivers the following key advantages:

-  High performance: The built-in CSS vector search engine can search through tens to hundreds of millions of vectors in milliseconds. The CSS vector database supports all major indexing algorithms, including brute-force search, graph-based algorithms (such as HNSW), and Inverted File Product Quantization (IVF-PQ). This allows you to flexibly select algorithms based on precision and latency requirements.
-  High reliability: Based on the native distributed architecture of Elasticsearch/OpenSearch, CSS delivers enterprise-grade reliability guarantees, including multi-replica, snapshots, and permission control, ensuring zero data loss.
-  Extensive ecosystem compatibility: The CSS vector database is fully compatible with native Elasticsearch/OpenSearch query language, so there is zero learning curve for developers. It supports mainstream client languages such as Python, Java, and Go, and can seamlessly integrate components such as Logstash, Kibana and Dashboards.
-  Security: The CSS vector database provides comprehensive security features, including network isolation, access control, and data encryption.

How It Works
------------

The CSS vector database uses approximate nearest neighbor (ANN) search to mitigate the intensive computational load of exact k-NN search. While exact k-NN guarantees recall by exhaustively comparing the query vector against all data points, it incurs prohibitive latency on large-scale datasets. ANN significantly reduces computational overhead and search latency, balancing high recall with substantial gains in throughput and efficiency. Key points include:

-  Reducing the candidate set: Traditional text search filters out irrelevant documents through inverted indexes, while vector search quickly retrieves potentially relevant vectors using index structures like HNSW graphs or IVF-PQ, avoiding scanning the full dataset. For example, HNSW uses a multi-layer structure to quickly find nearest neighbors to the query vector.
-  Reducing computational complexity: The funnel model first performs coarse quantization (such as IVF-PQ) on vectors to quickly obtain the candidate set. Then, it performs fine retrieval or reranking (such as cosine similarity) on the candidate set. Quantization uses the product quantization (PQ) algorithm to encode high-dimensional vectors into compact codes, reducing storage and computational overheads.
-  Balancing performance and accuracy: Indexing parameters (such as the number of HNSW layers and the number of IVF clusters) can be dynamically tuned to trade off between recall and query latency.

Supported Cluster Versions
--------------------------

.. table:: **Table 1** Clusters that support CSS Vector Database

   ============= ===============
   Cluster Type  Cluster Version
   ============= ===============
   Elasticsearch 7.6.2, 7.10.2
   OpenSearch    1.3.6, 2.19.0
   ============= ===============


Procedure
---------


.. figure:: /_static/images/en-us_image_0000002554934281.png
   :alt: **Figure 1** Procedure for using the CSS vector database

   **Figure 1** Procedure for using the CSS vector database

.. table:: **Table 2** Procedure for using the CSS vector database

   +-------------------+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
   | Category          | Operation               |                                                                                                                                                                                                               | Details                                                     |
   +===================+=========================+===============================================================================================================================================================================================================+=============================================================+
   | Use               | Environment preparation | Create a proper CSS vector database based on your memory planning.                                                                                                                                            | :ref:`Preparing the Environment <css_01_0195>`              |
   +-------------------+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
   |                   | Creating indexes        | Create vector indexes in your cluster and define mappings that contain vector fields, including vector dimensions, indexing algorithm, and similarity measurement methods.                                    | :ref:`Creating a Vector Index <css_01_0121>`                |
   +-------------------+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
   |                   | Data writing            | Write vectors (typically along with the original data or metadata) into indexes.                                                                                                                              | :ref:`Importing Vector Data <css_01_0296>`                  |
   +-------------------+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
   |                   | Vector search           | Use the standard Elasticsearch query DSL to provide the query vector and specify the number (k) of nearest neighbors you expect to return as well as the similarity score.                                    | :ref:`Performing Vector Search <css_01_0123>`               |
   +-------------------+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
   | Advanced features | Nested fields           | Nested fields allow multiple independent vectors to be stored within a single document. The document is returned as a match if the query vector meets the similarity threshold for any of its nested vectors. | :ref:`Implementing Nested Vector Search <css_01_0264>`      |
   +-------------------+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
   | Management        | Performance tuning      | Provides ways to optimize the write and query performance of the CSS vector database.                                                                                                                         | :ref:`Optimizing Query and Write Performance <css_01_0126>` |
   +-------------------+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
   |                   | Cache management        | Flexibly monitors and tunes the usage of the vector index cache to ensure stable query performance.                                                                                                           | :ref:`Managing the Vector Search Cache <css_01_0130>`       |
   +-------------------+-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------+
