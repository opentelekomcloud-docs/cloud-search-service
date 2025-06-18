:original_name: css_01_0121.html

.. _css_01_0121:

Creating Vector Indexes in an Elasticsearch Cluster
===================================================

To create a vector index, perform the following steps:

#. :ref:`(Optional) Preparations <css_01_0121__en-us_topic_0000001309709789_section8992201842518>`: Configure advanced cluster settings based on service needs.
#. :ref:`(Optional) Pre-Building and Registering a Center Point Vector <css_01_0121__section68017273556>`: If index algorithms **IVF_GRAPH** and **IVF_GRAPH_PQ** are selected when creating a vector index, pre-build and register a center point vector.
#. :ref:`Creating a Vector Index <css_01_0121__en-us_topic_0000001309709789_section137344225249>`: Create a vector index based on service needs.
#. :ref:`Importing Vector Data <css_01_0121__en-us_topic_0000001309709789_section137931314240>`: Import vector data to the cluster.
#. :ref:`(Optional) Offline Index Creation <css_01_0121__section164656265118>`: If lazy indexing is enabled for vector fields, you need to use an offline API to create the vector index structure after all data is written in.
#. :ref:`Using Vector Indexes for Data Search in an Elasticsearch Cluster <css_01_0123>`: Perform a vector search.

Prerequisites
-------------

You have created a cluster by following the instructions in :ref:`Cluster Node Specifications Selection for Vector Search <css_01_0118__section18221195417136>`. The cluster must be an Elasticsearch cluster of version 7.6.2 or 7.10.2.

.. _css_01_0121__en-us_topic_0000001309709789_section8992201842518:

(Optional) Preparations
-----------------------

Before creating a vector index, configure advanced settings for the cluster based on service needs.

-  When importing data offline, you are advised to set **refresh_interval** of indexes to **-1** to disable automatic index refreshing and thus improve batch write performance.

-  You are advised to set **number_of_replicas** to **0**. After the offline data import is complete, you can modify the parameter value again as needed.

-  :ref:`Table 1 <css_01_0121__en-us_topic_0000001309709789_table14840054154616>` describes the other advanced settings.

   .. _css_01_0121__en-us_topic_0000001309709789_table14840054154616:

   .. table:: **Table 1** Parameters for advanced cluster settings

      +----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                              | Description                                                                                                                                                                                                                                                                         |
      +========================================+=====================================================================================================================================================================================================================================================================================+
      | native.cache.circuit_breaker.enabled   | Whether to enable the circuit breaker for off-heap memory.                                                                                                                                                                                                                          |
      |                                        |                                                                                                                                                                                                                                                                                     |
      |                                        | Default value: **true**                                                                                                                                                                                                                                                             |
      +----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | native.cache.circuit_breaker.cpu.limit | Upper limit of off-heap memory usage of the vector index.                                                                                                                                                                                                                           |
      |                                        |                                                                                                                                                                                                                                                                                     |
      |                                        | For example, if the overall memory of a host is 128 GB and the heap memory occupies 31 GB, the default upper limit of the off-heap memory usage is 77.6 GB, that is, (128 - 31) x 80%. If the off-heap memory usage exceeds its upper limit, the circuit breaker will be triggered. |
      |                                        |                                                                                                                                                                                                                                                                                     |
      |                                        | Default value: **80%**                                                                                                                                                                                                                                                              |
      +----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | native.cache.expiry.enabled            | Whether to enable the cache expiration policy. If this parameter is set to **true**, some cache items that have not been accessed for a long time will be cleared.                                                                                                                  |
      |                                        |                                                                                                                                                                                                                                                                                     |
      |                                        | Value: **true** or **false**                                                                                                                                                                                                                                                        |
      |                                        |                                                                                                                                                                                                                                                                                     |
      |                                        | Default value: **false**                                                                                                                                                                                                                                                            |
      +----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | native.cache.expiry.time               | Expiration time.                                                                                                                                                                                                                                                                    |
      |                                        |                                                                                                                                                                                                                                                                                     |
      |                                        | Default value: **24h**                                                                                                                                                                                                                                                              |
      +----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | native.vector.index_threads            | Number of threads used for creating underlying indexes. Each shard uses multiple threads. Set a relatively small value to avoid resource preemption caused by the build queries of too many threads.                                                                                |
      |                                        |                                                                                                                                                                                                                                                                                     |
      |                                        | Default value: **4**                                                                                                                                                                                                                                                                |
      +----------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _css_01_0121__section68017273556:

(Optional) Pre-Building and Registering a Center Point Vector
-------------------------------------------------------------

If index algorithms **IVF_GRAPH** and **IVF_GRAPH_PQ** are selected when creating a vector index, you need to pre-build and register a center point vector.

The vector index acceleration algorithms **IVF_GRAPH** and **IVF_GRAPH_PQ** are suitable for ultra-large-scale computing. These two algorithms allow you to narrow down the query scope by dividing a vector space into subspaces through clustering or random sampling. Before pre-build, you need to obtain all center point vectors by clustering or random sampling. Center point vectors are pre-built into the GRAPH or GRAPH_PQ index and then registered with the Elasticsearch cluster. All nodes in the cluster can share this index file. Reuse of the center index among shards can effectively reduce the training overhead and the number of center index queries, improving the write and query performance.

#. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. Click **Dev Tools** in the navigation tree on the left.

#. Create a center point index table.

   -  For example, if the created index is named **my_dict**, **number_of_shards** of the index must be set to **1**. Otherwise, the index cannot be registered.
   -  If you want to use the **IVF_GRAPH** index, set **algorithm** of the center point index to **GRAPH**.
   -  If you want to use the **IVF_GRAPH_PQ** index, set **algorithm** of the center point index to **GRAPH_PQ**.

   .. code-block:: text

      PUT my_dict
       {
         "settings": {
           "index": {
             "vector": true
           },
           "number_of_shards": 1,
           "number_of_replicas": 0
         },
         "mappings": {
           "properties": {
             "my_vector": {
               "type": "vector",
               "dimension": 2,
               "indexing": true,
               "algorithm": "GRAPH",
               "metric": "euclidean"
             }
           }
         }
       }

#. Write the center point vector to the created index.

   Write the center point vector obtained through sampling or clustering into the created **my_dict** index. For details, see :ref:`Importing Vector Data <css_01_0121__en-us_topic_0000001309709789_section137931314240>`.

#. Call the registration API.

   Register the created **my_dict** index with a **Dict** object with a globally unique identifier name (**dict_name**).

   .. code-block:: text

      PUT _vector/register/my_dict
       {
         "dict_name": "my_dict"
       }

#. Create an **IVF_GRAPH** or **IVF_GRAPH_PQ** index.

   You do not need to specify the dimension or metric information. Simply specify the registered dictionary name.

   .. code-block:: text

      PUT my_index
       {
         "settings": {
           "index": {
             "vector": true,
             "sort.field": "my_vector.centroid" # Set the centroid subfield of each vector field as a sorting field.
           }
         },
         "mappings": {
           "properties": {
             "my_vector": {
               "type": "vector",
               "indexing": true,
               "algorithm": "IVF_GRAPH",
               "dict_name": "my_dict",
               "offload_ivf": true
             }
           }
         }
       }

   .. table:: **Table 2** Field mappings parameters

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                     |
      +===================================+=================================================================================================================================================================================================================================+
      | dict_name                         | Specifies the name of the depended central point index. The vector dimensions and metrics of the index are the same as those of the Dict index.                                                                                 |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | offload_ivf                       | Unloads the IVF inverted index implemented by the underlying index to Elasticsearch. This reduces the use of non-heap memory and the overhead of write and merge operations. You are advised to set this parameter to **true**. |
      |                                   |                                                                                                                                                                                                                                 |
      |                                   | Value: **true** or **false**                                                                                                                                                                                                    |
      |                                   |                                                                                                                                                                                                                                 |
      |                                   | Default value: **false**                                                                                                                                                                                                        |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
              "type": "keyword"
            }
          }
        }
      }

   .. table:: **Table 3** Parameters for creating an index

      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Type                      | Parameter                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +===========================+===============================+=======================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | Index settings parameters | vector                        | To use a vector index, set this parameter to **true**.                                                                                                                                                                                                                                                                                                                                                                                                                                |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | vector.exact_search_threshold | The minimum size of the intermediate result set that triggers a switchover from pre-filtering search to brute-force search.                                                                                                                                                                                                                                                                                                                                                           |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | When the size of the intermediate result set in a segment is lower than this threshold, brute-force search starts.                                                                                                                                                                                                                                                                                                                                                                    |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | The default value is **null**, which disables a switchover to brute-force search.                                                                                                                                                                                                                                                                                                                                                                                                     |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Field mappings parameters | type                          | Field type, for example, **vector**.                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | dimension                     | Vector dimensionality. Value range: [1, 4096]                                                                                                                                                                                                                                                                                                                                                                                                                                         |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | indexing                      | Whether to enable vector index acceleration.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | The value can be:                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | -  **false**: disables vector index acceleration. If this parameter is set to **false**, vector data is written only to docvalues, and only **ScriptScore** and **Rescore** can be used for vector query.                                                                                                                                                                                                                                                                             |
      |                           |                               | -  **true**: enables vector index acceleration. If this parameter is set to **true**, an extra vector index is created. The index algorithm is specified by the **algorithm** field and **VectorQuery** can be used for data query.                                                                                                                                                                                                                                                   |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | Default value: **false**                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | lazy_indexing                 | The configuration of lazy_indexing takes effect only when: **indexing** is set to **true**; the cluster version is Elasticsearch 7.10.2 or later; and the cluster image version is no earlier than 7.10.2_24.3.3_x.x.x.                                                                                                                                                                                                                                                               |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | Whether to enable lazy indexing for a vector field, allowing for offline index creation.                                                                                                                                                                                                                                                                                                                                                                                              |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | The value can be:                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | -  **false**: disables lazy indexing.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                           |                               | -  **true**: enables lazy indexing. In this case, the cluster does not create the vector index (e.g., a graph index) in real time as data is being written in. Instead, it performs :ref:`offline index creation <css_01_0121__section164656265118>` to create the vector index after data has been written in. The vector index can then be used for vector search.                                                                                                                  |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | algorithm                     | Index algorithm. This parameter is valid only when **indexing** is set to **true**.                                                                                                                                                                                                                                                                                                                                                                                                   |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | The value can be:                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | -  **FLAT**: brute-force algorithm that calculates the distance between the target vector and all vectors in sequence. The algorithm relies on sheer computing power and its recall rate reaches 100%. You can use this algorithm if you require high recall accuracy.                                                                                                                                                                                                                |
      |                           |                               | -  **GRAPH**: Hierarchical Navigable Small Worlds (HNSW) algorithm for graph indexes. This algorithm is mainly used in scenarios where high performance and precision are required and the data records of a single shard is fewer than 10 million.                                                                                                                                                                                                                                   |
      |                           |                               | -  **GRAPH_PQ**: a combination of the HNSW algorithm and the product quantization (PQ) algorithm. The PQ algorithm reduces the storage overhead of the original vectors, so that HNSW can easily search through hundreds of millions of records.                                                                                                                                                                                                                                      |
      |                           |                               | -  **GRAPH_SQ8**: a combination of the HNSW algorithm and the scalar quantization (SQ) algorithm. By quantizing float32 values into int8, this algorithm reduces the storage overhead of the original vectors and improves build and query efficiency. The downside is slightly decreased recall rate. Only Elasticsearch 7.10.2 clusters support this algorithm.                                                                                                                     |
      |                           |                               | -  **GRAPH_SQ4**: a combination of the HNSW algorithm and the SQ algorithm. By quantizing float32 values into int4, this algorithm reduces the storage overhead of the original vectors and improves build and query efficiency. The downside is a slightly decreased recall rate. SQ4 has a higher quantization/compression ratio and higher computational efficiency than SQ8, but also a large decrease in recall rate. Only Elasticsearch 7.10.2 clusters support this algorithm. |
      |                           |                               | -  **IVF_GRAPH**: combination of IVF and HNSW. The entire space is divided into multiple cluster centroids, which makes search much faster but slightly inaccurate. You can use this algorithm if you require high performance when searching for data among hundreds of millions of records.                                                                                                                                                                                         |
      |                           |                               | -  **IVF_GRAPH_PQ**: combination of the PQ algorithm with the IVF or HNSW algorithm to further improve the system capacity and reduce the system overhead. This algorithm is applicable to scenarios where there are more than 1 billion files in shards and high retrieval performance is required.                                                                                                                                                                                  |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | Default value: **GRAPH**                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | .. note::                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               |    If **IVF_GRAPH** or **IVF_GRAPH_PQ** is specified, you need to pre-build and register a central point index. For details, see :ref:`(Optional) Pre-Building and Registering a Center Point Vector <css_01_0121__section68017273556>`.                                                                                                                                                                                                                                              |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | Other optional parameters     | If **Indexing** is set to **true**, CSS provides optional parameters for vector search that you can configure to achieve higher query performance or precision. For more information, see :ref:`Table 4 <css_01_0121__en-us_topic_0000001309709789_table9916164920432>`.                                                                                                                                                                                                              |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | metric                        | Method of calculating the distance between vectors.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | The value can be:                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | -  **euclidean**: Euclidean distance                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      |                           |                               | -  **inner_product**: inner product distance                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                           |                               | -  **cosine**: cosine distance                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      |                           |                               | -  **hamming**: Hamming distance, which can be used only when **dim_type** is set to **binary**.                                                                                                                                                                                                                                                                                                                                                                                      |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | Default value: **euclidean**                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                           | dim_type                      | Type of the vector dimension value.                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      |                           |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                           |                               | The value can be **binary** and **float** (default).                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +---------------------------+-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _css_01_0121__en-us_topic_0000001309709789_table9916164920432:

   .. table:: **Table 4** Optional parameters

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
      |                                      | efc                   | Queue size of the neighboring node during HNSW build. The default value is **200**. A larger value indicates a higher precision and slower indexing speed.                                   |
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

.. _css_01_0121__section164656265118:

(Optional) Offline Index Creation
---------------------------------

Use offline index creation via an API only when: real-time data is not required or crucial; the cluster version is Elasticsearch 7.10.2 or later; and the cluster image version is no earlier than 7.10.2_24.3.3_x.x.x.

Elasticsearch uses an LSM (Log-Structured Merge) tree-like model to accelerate write operations. As data is continuously written in and updated, numerous small index segments are generated and later merged via a backend task to enhance query performance. As vector indexing is computationally intensive, frequent index merging during the writing of vector data consumes significant CPU resources. Therefore, where real-time data is not crucial, it is advisable to set **lazy_indexing** to **true** for vector fields. This allows a final vector index to be created via a non-real time API after all data has been written in. This approach significantly reduces index merges, thereby improving overall write and index merging performance.

Offline index creation consists of two steps:

#. Merge index segments.
#. Create the final vector index based on the final index segments.

The API used for offline index creation is as follows:

.. code-block:: text

   POST _vector/indexing/{index_name}
   {
     "field": "{field_name}"
   }

where, {index_name} indicates the name of the index to create. {field_name} indicates the name of the vector field for which **lazy_indexing** has been set to **true**.

.. note::

   If **lazy_indexing** is enabled for the vector field but the vector index was not created by calling the API after all data has been written, the vector field cannot be queried using the standard vector query statement. Additionally, error code 500 will be returned for such query requests, along with the error message that contains **Load native index failed exception**. In this case, you are advised to manually create the vector index first.
