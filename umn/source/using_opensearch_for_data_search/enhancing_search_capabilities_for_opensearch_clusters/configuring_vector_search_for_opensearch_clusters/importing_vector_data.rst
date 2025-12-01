:original_name: css_01_0019.html

.. _css_01_0019:

Importing Vector Data
=====================

Importing vector data is the process of ingesting data to the CSS vector database. When writing vector data to a vector index, you need to specify the vector field (for example, **my_vector**) and the corresponding data format. The CSS vector database supports two common formats: floating-point arrays and Base64.

-  Floating-point arrays: transmitting readable arrays directly.
-  Base64: encoding vectors (little-endian byte order) into character strings to reduce network transmission overhead and improve efficiency in handling high-dimensional/binary vectors.

Choose a format based on the characteristics of your data. Also, choose an appropriate data importing method.

-  Importing a single record: Use for small-scale applications or testing.
-  Bulk import: Use for large-scale applications, where write requests are merged to reduce network overhead.

Constraints
-----------

-  Ensure that the vector field names and vector dimensions are consistent with those defined for the index.
-  Base64 encoding must use the little-endian byte order. Otherwise, parsing errors may occur.
-  In the case of bulk imports, you are advised to submit 100 to 1000 records per request. This balances throughput and memory overhead.

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

.. _en-us_topic_0000002333390490__section164656265118:

(Optional) Post-processing after Data Ingestion: Offline Index Building
-----------------------------------------------------------------------

.. warning::

   -  Use offline index creation via an API only when real-time data is not required or crucial and the cluster version is OpenSearch 2.19.0.
   -  If lazy_indexing is enabled, offline index building must be performed after data ingestion. Otherwise, the system will return error code 500 for standard vector query, with the error message "Load native index failed exception." To solve this problem, perform offline index building before vectors queries.

OpenSearch uses an LSM (Log-Structured Merge) tree-like model to accelerate write operations. As data is continuously written in and updated, numerous small index segments are generated and later merged via a backend task to enhance query performance. As vector indexing is computationally intensive, frequent index merging while vector data is being written in consumes significant CPU resources. Therefore, where real-time data is not crucial, it is advisable to set **lazy_indexing** to **true** for vector fields. This allows a final vector index to be created via a non-real time API after all data has been written in. This approach significantly reduces index merges, thereby improving overall write and index merging performance.

Offline index building consists of two steps:

#. Merge index segments.
#. Create the final vector index based on the final index segments.

The API used for offline index building is as follows:

.. code-block:: text

   POST _vector/indexing/{index_name}
   {
     "field": "{field_name}"
   }

where, {index_name} indicates the name of the index to create. {field_name} indicates the name of the vector field for which **lazy_indexing** has been set to **true**.
