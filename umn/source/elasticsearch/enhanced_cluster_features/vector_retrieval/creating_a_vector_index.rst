:original_name: css_01_0121.html

.. _css_01_0121:

Creating a Vector Index
=======================

Prerequisites
-------------

-  A cluster of version 7.6.2 or 7.10.2 has been created by referring to :ref:`Cluster Planning for Vector Retrieval <css_01_0122>`.
-  Cluster advanced settings have been configured as required by referring to :ref:`Advanced Cluster Configurations <css_01_0121__en-us_topic_0000001309709789_section8992201842518>`.

.. _css_01_0121__en-us_topic_0000001309709789_section137344225249:


Creating a Vector Index
-----------------------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. Click **Dev Tools** in the navigation tree on the left and run the following command to create a vector index.

   Create an index named **my_index** that contains a vector field **my_vector** and a text field **my_label**. The vector field creates the graph index and uses Euclidean distance to measure similarity.

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index": {
            "vector": true
          }
        },
        "mappings": {
          "properties": {
            "my_vector": {
              "type": "vector",
              "dimension": 2,
              "indexing": true,
              "algorithm": "GRAPH",
              "metric": "euclidean"
            },
            "my_label": {
              "type": "text"
            }
          }
        }
      }

   .. table:: **Table 1** Parameters for creating an index

      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Type                      | Parameter                                                                     | Description                                                                                                                                                                                                                                                                                          |
      +===========================+===============================================================================+======================================================================================================================================================================================================================================================================================================+
      | Index settings parameters | vector                                                                        | To use a vector index, set this parameter to **true**.                                                                                                                                                                                                                                               |
      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Field mappings parameters | type                                                                          | Field type, for example, **vector**.                                                                                                                                                                                                                                                                 |
      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | dimension                                                                     | Vector dimension.                                                                                                                                                                                                                                                                                    |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | The default value is **768** and cannot be changed.                                                                                                                                                                                                                                                  |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | Value range: [1, 4096]                                                                                                                                                                                                                                                                               |
      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | indexing                                                                      | Whether to enable vector index acceleration.                                                                                                                                                                                                                                                         |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | The value can be:                                                                                                                                                                                                                                                                                    |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | -  **false**: disables vector index acceleration. If this parameter is set to **false**, vector data is written only to docvalues, and only **ScriptScore** and **Rescore** can be used for vector query.                                                                                            |
      |                           |                                                                               | -  **true**: enables vector index acceleration. If this parameter is set to **true**, an extra vector index is created. The index algorithm is specified by the **algorithm** field and **VectorQuery** can be used for data query.                                                                  |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | Default value: **false**                                                                                                                                                                                                                                                                             |
      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | algorithm                                                                     | Index algorithm. This parameter is valid only when **indexing** is set to **true**.                                                                                                                                                                                                                  |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | The value can be:                                                                                                                                                                                                                                                                                    |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | -  **FLAT**: brute-force algorithm that calculates the distance between the target vector and all vectors in sequence. The algorithm relies on sheer computing power and its recall rate reaches 100%. You can use this algorithm if you require high recall accuracy.                               |
      |                           |                                                                               | -  **GRAPH**: Hierarchical Navigable Small Worlds (HNSW) algorithm for graph indexes. This algorithm is mainly used in scenarios where high performance and precision are required and the data records of a single shard is fewer than 10 million.                                                  |
      |                           |                                                                               | -  **GRAPH_PQ**: combination of the HNSW algorithm and the PQ algorithm. The PQ algorithm reduces the storage overhead of original vectors, so that HNSW can easily search for data among hundreds of millions of records.                                                                           |
      |                           |                                                                               | -  **IVF_GRAPH**: combination of IVF and HNSW. The entire space is divided into multiple cluster centroids, which makes search much faster but slightly inaccurate. You can use this algorithm if you require high performance when searching for data among hundreds of millions of records.        |
      |                           |                                                                               | -  **IVF_GRAPH_PQ**: combination of the PQ algorithm with the IVF or HNSW algorithm to further improve the system capacity and reduce the system overhead. This algorithm is applicable to scenarios where there are more than 1 billion files in shards and high retrieval performance is required. |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | Default value: **GRAPH**                                                                                                                                                                                                                                                                             |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | .. note::                                                                                                                                                                                                                                                                                            |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               |    If **IVF_GRAPH** or **IVF_GRAPH_PQ** is specified, you need to pre-build and register a central point index. For details, see :ref:`(Optional) Pre-Building and Registering a Center Point Vector <css_01_0124>`.                                                                                 |
      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | :ref:`Table 2 <css_01_0121__en-us_topic_0000001309709789_table9916164920432>` | If **Indexing** is set to **true**, CSS provides optional parameters for vector search to achieve higher query performance or precision.                                                                                                                                                             |
      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | metric                                                                        | Method of calculating the distance between vectors.                                                                                                                                                                                                                                                  |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | The value can be:                                                                                                                                                                                                                                                                                    |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | -  **euclidean**: Euclidean distance                                                                                                                                                                                                                                                                 |
      |                           |                                                                               | -  **inner_product**: inner product distance                                                                                                                                                                                                                                                         |
      |                           |                                                                               | -  **cosine**: cosine distance                                                                                                                                                                                                                                                                       |
      |                           |                                                                               | -  **hamming**: Hamming distance, which can be used only when **dim_type** is set to **binary**.                                                                                                                                                                                                     |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | Default value: **euclidean**                                                                                                                                                                                                                                                                         |
      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | dim_type                                                                      | Type of the vector dimension value.                                                                                                                                                                                                                                                                  |
      |                           |                                                                               |                                                                                                                                                                                                                                                                                                      |
      |                           |                                                                               | The value can be **binary** and **float** (default).                                                                                                                                                                                                                                                 |
      +---------------------------+-------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _css_01_0121__en-us_topic_0000001309709789_table9916164920432:

   .. table:: **Table 2** Optional parameters

      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Type                                 | Parameter             | Description                                                                                                                                                                                  |
      +======================================+=======================+==============================================================================================================================================================================================+
      | Graph index configuration parameters | neighbors             | Number of neighbors of each vector in a graph index. The default value is **64**. A larger value indicates higher query precision. A larger index results in a slower build and query speed. |
      |                                      |                       |                                                                                                                                                                                              |
      |                                      |                       | Value range: [10, 255]                                                                                                                                                                       |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                                      | shrink                | Cropping coefficient during HNSW build. The default value is **1.0f**.                                                                                                                       |
      |                                      |                       |                                                                                                                                                                                              |
      |                                      |                       | Value range: (0.1, 10)                                                                                                                                                                       |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                                      | scaling               | Scaling ratio of the upper-layer graph nodes during HNSW build. The default value is **50**.                                                                                                 |
      |                                      |                       |                                                                                                                                                                                              |
      |                                      |                       | Value range: (0, 128]                                                                                                                                                                        |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                                      | efc                   | Queue size of the neighboring node during HNSW build. The default value is **200**. A larger value indicates a higher precision and slower build speed.                                      |
      |                                      |                       |                                                                                                                                                                                              |
      |                                      |                       | Value range: (0, 100000]                                                                                                                                                                     |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                                      | max_scan_num          | Maximum number of nodes that can be scanned. The default value is **10000**. A larger value indicates a higher precision and slower indexing speed.                                          |
      |                                      |                       |                                                                                                                                                                                              |
      |                                      |                       | Value range: (0, 1000000]                                                                                                                                                                    |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | PQ index configuration parameters    | centroid_num          | Number of cluster centroids of each fragment. The default value is **255**.                                                                                                                  |
      |                                      |                       |                                                                                                                                                                                              |
      |                                      |                       | Value range: (0, 65535]                                                                                                                                                                      |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                                      | fragment_num          | Number of fragments. The default value is **0**. The plug-in automatically sets the number of fragments based on the vector length.                                                          |
      |                                      |                       |                                                                                                                                                                                              |
      |                                      |                       | Value range: [0, 4096]                                                                                                                                                                       |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _css_01_0121__en-us_topic_0000001309709789_section137931314240:

Importing Vector Data
---------------------

Run the following command to import vector data. When writing vector data to the **my_index** index, you need to specify the vector field name and vector data.

-  If the input vector data is an array of floating-point numbers separated by commas (,):

   .. code-block:: text

      POST my_index/_doc
      {
        "my_vector": [1.0, 2.0]
      }

-  If the input vector data is a Base64 string encoded using little endian:

   When writing binary vectors or high dimensional vectors that have a large number of valid bits, the Base64 encoding format is efficient for data transmission and parsing.

   .. code-block:: text

      POST my_index/_doc
      {
        "my_vector": "AACAPwAAAEA="
      }

-  To write a large amount of data, bulk operations are recommended.

   .. code-block:: text

      POST my_index/_bulk
      {"index": {}}
      {"my_vector": [1.0, 2.0], "my_label": "red"}
      {"index": {}}
      {"my_vector": [2.0, 2.0], "my_label": "green"}
      {"index": {}}
      {"my_vector": [2.0, 3.0], "my_label": "red"}

.. _css_01_0121__en-us_topic_0000001309709789_section8992201842518:

Advanced Cluster Configurations
-------------------------------

-  When importing data offline, you are advised to set **refresh_interval** of indexes to **-1** to disable automatic index refreshing and improve batch write performance.
-  You are advised to set **number_of_replicas** to **0**. After the offline data import is complete, you can modify the parameter value as needed.
-  The parameters of other advanced functions as follows:

   .. table:: **Table 3** Cluster parameters

      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                              | Description                                                                                                                                                                                                                                                                          |
      +========================================+======================================================================================================================================================================================================================================================================================+
      | native.cache.circuit_breaker.enabled   | Whether to enable the circuit breaker for off-heap memory.                                                                                                                                                                                                                           |
      |                                        |                                                                                                                                                                                                                                                                                      |
      |                                        | Default value: **true**                                                                                                                                                                                                                                                              |
      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | native.cache.circuit_breaker.cpu.limit | Upper limit of off-heap memory usage of the vector index.                                                                                                                                                                                                                            |
      |                                        |                                                                                                                                                                                                                                                                                      |
      |                                        | For example, if the overall memory of a host is 128 GB and the heap memory occupies 31 GB, the default upper limit of the off-heap memory usage is 43.65 GB, that is, (128 - 31) x 45%. If the off-heap memory usage exceeds its upper limit, the circuit breaker will be triggered. |
      |                                        |                                                                                                                                                                                                                                                                                      |
      |                                        | Default value: **45%**                                                                                                                                                                                                                                                               |
      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | native.cache.expire.enabled            | Whether to enable the cache expiration policy. If this parameter is set to **true**, some cache items that have not been accessed for a long time will be cleared.                                                                                                                   |
      |                                        |                                                                                                                                                                                                                                                                                      |
      |                                        | Value: **true** or **false**                                                                                                                                                                                                                                                         |
      |                                        |                                                                                                                                                                                                                                                                                      |
      |                                        | Default value: **false**                                                                                                                                                                                                                                                             |
      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | native.cache.expire.time               | Expiration time.                                                                                                                                                                                                                                                                     |
      |                                        |                                                                                                                                                                                                                                                                                      |
      |                                        | Default value: **24h**                                                                                                                                                                                                                                                               |
      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | native.vector.index_threads            | Number of threads used for creating underlying indexes. Each shard uses multiple threads. Set a relatively small value to avoid resource preemption caused by the build queries of too many threads.                                                                                 |
      |                                        |                                                                                                                                                                                                                                                                                      |
      |                                        | Default value: **4**                                                                                                                                                                                                                                                                 |
      +----------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
