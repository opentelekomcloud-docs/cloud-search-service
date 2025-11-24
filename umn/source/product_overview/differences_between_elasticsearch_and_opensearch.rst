:original_name: css_04_0042.html

.. _css_04_0042:

Differences Between Elasticsearch and OpenSearch
================================================

CSS provides a fully managed cloud search service based on open-source engines. CSS Elasticsearch and OpenSearch both have the following core capabilities:

-  Unified architecture: a distributed, RESTful search engine, supporting near-real-time search and analytics over petabytes of data
-  A wide range of use cases: log analytics, enterprise search, big data analytics, vector search, semantic search, RAG, etc.
-  Enhanced features: deep optimization based on open-source versions, high performance, high availability, cost effective, and fully managed

A Comparison of Core Functions
------------------------------

.. table:: **Table 1** A comparison of core functions between Elasticsearch and OpenSearch

   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | Dimension             | CSS Elasticsearch                                                                                                                          | CSS OpenSearch                                                                                                       |
   +=======================+============================================================================================================================================+======================================================================================================================+
   | Origin                | Built on Apache Lucene, Elasticsearch is a mature, widely adopted search engine.                                                           | OpenSearch, a fork of Elasticsearch, inherits its core search and analytics capabilities while keeps evolving.       |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | Compatibility         | -  Compatible with the Elasticsearch ecosystem                                                                                             | -  Compatible with the OpenSearch ecosystem                                                                          |
   |                       | -  Compatible with later-version Elasticsearch SDKs                                                                                        | -  Compatible with Elasticsearch 7.10.2                                                                              |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | Version policy        | The mainstream version is 7.10.2, which will be continuously optimized. We recommend upgrading all Elasticsearch clusters to this version. | The version will be continuously updated to keep up with open-source innovations.                                    |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | Kernel features       | CSS will provide continuous kernel enhancement.                                                                                            | CSS will integrate its own unique capabilities with open-source innovations to ensure continuous kernel enhancement. |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+
   | Evolution             | Emphasizes the stability of the 7.x version and enhancements.                                                                              | Actively integrates new cloud native features.                                                                       |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------+

Engine Selection Suggestions
----------------------------

.. table:: **Table 2** When to choose Elasticsearch or OpenSearch

   +-----------------------------------------------------------------+-----------------------------+------------------------------------------------------------------------------------+
   | Scenario                                                        | Recommended Engine          | Reason                                                                             |
   +=================================================================+=============================+====================================================================================+
   | Running Elasticsearch 7.10.2 or earlier for long-term stability | **Elasticsearch**           | -  Mature and stable, fully compatible with the native Elasticsearch toolchain     |
   |                                                                 |                             | -  Compatible with later-version Elasticsearch SDKs                                |
   |                                                                 |                             | -  Backed by the unique strengths of CSS (such as vector search)                   |
   +-----------------------------------------------------------------+-----------------------------+------------------------------------------------------------------------------------+
   | New features of Elasticsearch 8+ are required                   | **OpenSearch**              | -  Inherits Elasticsearch capabilities while keeps evolving                        |
   |                                                                 |                             | -  Backed by the unique strengths of CSS (such as vector search)                   |
   +-----------------------------------------------------------------+-----------------------------+------------------------------------------------------------------------------------+
   | Smooth migration of existing Elasticsearch 7.x clusters         | Elasticsearch or OpenSearch | Both are compatible with Elasticsearch 7.10.2 APIs, with a similar migration cost. |
   +-----------------------------------------------------------------+-----------------------------+------------------------------------------------------------------------------------+
