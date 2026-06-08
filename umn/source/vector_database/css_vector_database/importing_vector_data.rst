:original_name: css_01_0296.html

.. _css_01_0296:

Importing Vector Data
=====================

In large-scale search and analytics scenarios, efficiently ingesting tens to hundreds of millions of high-dimensional vectors is a critical challenge. Because vector data is significantly larger than standard text, real-time construction of complex index structures (such as HNSW) consumes extensive CPU resources, which can bottleneck write throughput. To maximize ingestion performance, the CSS vector database supports two formats: directly readable floating-point arrays, and Base64 encoding optimized for higher network transmission efficiency. Additionally, where real-time retrieval is not required during the ingestion phase, the CSS vector database supports offline index building. This allows you to use the Bulk API to rapidly ingest massive datasets and later trigger offline index building during off-peak hours. This decoupled approach ensures high ingestion efficiency even with limited hardware resources.

How the Feature Works
---------------------

The CSS vector database supports two primary formats:

-  Floating-point arrays: Standard JSON format (for example, [1.0, 2.0]), which is directly readable and easy to debug. Use this format for small datasets.
-  Base64 encoding: Transforms single-precision floating-point numbers (little-endian byte order) into strings. For vectors of the same dimensionality, Base64-encoded data is approximately one-third the size of JSON arrays, significantly reducing network transmission overhead and accelerating the processing of high-dimensional vectors.

Choose an appropriate ingestion method based on your service requirements.

-  Single-record import: Use for small-scale applications or testing.
-  Bulk import: Use for large-scale applications, where write requests are batched to reduce network overhead.

The vector database utilizes an LSM (Log-Structured Merge) tree-like model for data persistence. When data is written in, it is first stored in a memory buffer and then periodically flushed to disk as index segments.

-  Real-time index building (default): For each segment generated, the system immediately builds an HNSW graph index. This can cause write jitter, and the subsequent merging of small segments leads to redundant vector index computations.
-  Offline index building: When **lazy_indexing** is set to **true**, the system delays indexing until data ingestion is complete. You then manually trigger offline index building, which merges all segments and constructs the index at once. This significantly accelerates end-to-end performance for ingestion and indexing. Use this option for large-scale offline migrations where high ingestion speed is critical and real-time search capabilities are not required during the ingestion phase.

Constraints
-----------

-  The dimensions of the ingested vectors must strictly match the **dimension** defined during index creation.
-  Base64 encoding must use the little-endian byte order. Otherwise, parsing errors may occur.
-  Use offline index building only when there are no real-time query requirements; and for Elasticsearch clusters, the image version is 7.10.2_24.3.3_x.x.x or later, or for OpenSearch clusters, the version is 2.19.0.

Importing a Single Record
-------------------------

-  Floating-point array

   .. code-block:: text

      POST my_index/_doc
      {
        "my_vector": [1.0, 2.0]
      }

-  Base64

   .. code-block:: text

      POST my_index/_doc
      {
        "my_vector": "AACAPwAAAEA="
      }

Bulk Import
-----------

When importing data in bulk, we recommend keeping the size of each batch between 5 MB and 15 MB (approximately 100 to 1000 records) to balance between CPU load and network latency.

-  Floating-point array

   .. code-block:: text

      POST my_index/_bulk
      {"index": {}}
      {"my_vector": [1.0, 2.0], "my_label": "red"}
      {"index": {}}
      {"my_vector": [2.0, 2.0], "my_label": "green"}
      {"index": {}}
      {"my_vector": [2.0, 3.0], "my_label": "red"}

-  Base64

   .. code-block:: text

      POST my_index/_bulk
      {"index":{}}
      {"my_vector":"AACAPwAAAEA=", "my_label": "red"}
      {"index":{}}
      {"my_vector":"AAAAQAAAAEA=", "my_label": "green"}
      {"index":{}}
      {"my_vector":"AAAAQAAAQEA=", "my_label": "red"}

For details about how to use the Bulk API, see `Bulk API <https://www.elastic.co/guide/en/elasticsearch/reference/7.7/docs-bulk.html>`__.

.. _en-us_topic_0000002353678449__section164656265118:

(Optional) Triggering Offline Index Building
--------------------------------------------

If lazy_indexing is enabled, offline index building must be performed after data ingestion. Otherwise, the system will return error code 500 for standard vector query, with the error message "Load native index failed exception." To solve this, perform offline index building before vector queries.

.. caution::

   Use offline index building only when there are no real-time query requirements; and for Elasticsearch clusters, the image version is 7.10.2_24.3.3_x.x.x or later, or for OpenSearch clusters, the version is 2.19.0.

Offline index building consists of two steps:

#. Merge index segments.
#. Create the final vector index based on the final index segments.

Run the following command to trigger offline index building:

.. code-block:: text

   POST _vector/indexing/{index_name}
   {
     "field": "my_vector"
   }

.. table:: **Table 1** Parameters for offline index building

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                  |
   +=================+=================+=================+==============================================================================================+
   | index_name      | Yes             | String          | Name of the index to be built offline.                                                       |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+
   | field           | Yes             | String          | Vector field name.                                                                           |
   |                 |                 |                 |                                                                                              |
   |                 |                 |                 | Constraints: **lazy_indexing** must have been set to **true** for this field in the mapping. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+
