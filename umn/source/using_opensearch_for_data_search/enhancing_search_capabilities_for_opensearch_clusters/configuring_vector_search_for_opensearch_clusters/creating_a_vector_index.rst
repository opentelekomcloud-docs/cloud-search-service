:original_name: css_01_0115.html

.. _css_01_0115:

Creating a Vector Index
=======================

Create a vector index in your OpenSearch cluster and define a mapping that contains vector fields, including vector dimensions, indexing algorithm, and similarity measurement methods. Then store vectors (typically along with the original data or metadata) into this index.

Logging In to OpenSearch Dashboards
-----------------------------------

Log in to OpenSearch Dashboards and go to the command execution page. OpenSearch clusters support multiple access methods. This topic uses OpenSearch Dashboards as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

.. _en-us_topic_0000001992165597__en-us_topic_0000001309709789_section137344225249:


Creating a Vector Index
-----------------------

Run the following command on OpenSearch Dashboards to create a vector index.

For example, create an index named **my_index**. This index contains a vector field named **my_vector** and a text field named **my_label**. A graph-based index is created for the vector field, and Euclidean distance is used for similarity measurement.

.. code-block:: text

   PUT my_index
   {
     "settings": {
       "index": {
         "vector": true,
         "number_of_shards": 1,
         "number_of_replicas": 1
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

.. table:: **Table 1** settings parameters

   +-------------------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                           | Mandatory       | Type            | Description                                                                                                                                                                                                       |
   +=====================================+=================+=================+===================================================================================================================================================================================================================+
   | index.vector                        | Yes             | Boolean         | Whether to enable vector indexes.                                                                                                                                                                                 |
   |                                     |                 |                 |                                                                                                                                                                                                                   |
   |                                     |                 |                 | Set this parameter to **true**. Otherwise, vector indexes cannot be created.                                                                                                                                      |
   +-------------------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index.number_of_shards              | No              | Integer         | Number of index shards. This value should be divisible by the number of cluster nodes.                                                                                                                            |
   |                                     |                 |                 |                                                                                                                                                                                                                   |
   |                                     |                 |                 | Value range: 1-1024                                                                                                                                                                                               |
   |                                     |                 |                 |                                                                                                                                                                                                                   |
   |                                     |                 |                 | Default value: **1**                                                                                                                                                                                              |
   +-------------------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index.number_of_replicas            | No              | Integer         | Number of index replicas. Replicas improve data availability.                                                                                                                                                     |
   |                                     |                 |                 |                                                                                                                                                                                                                   |
   |                                     |                 |                 | Value range: 0 to the number of nodes minus 1                                                                                                                                                                     |
   |                                     |                 |                 |                                                                                                                                                                                                                   |
   |                                     |                 |                 | Default value: **1**                                                                                                                                                                                              |
   +-------------------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index.vector.exact_search_threshold | No              | Integer         | Threshold for automatically switching from pre-filtering search to brute-force search. When the size of the intermediate result set in a segment is lower than this threshold, a brute-force search is performed. |
   |                                     |                 |                 |                                                                                                                                                                                                                   |
   |                                     |                 |                 | Value range: null (disables auto switchover from pre-filtering search to brute-force search) or a positive integer                                                                                                |
   |                                     |                 |                 |                                                                                                                                                                                                                   |
   |                                     |                 |                 | Default value: null (disables auto switchover from pre-filtering search to brute-force search)                                                                                                                    |
   +-------------------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** mappings parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   +=================+=================+=================+====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | type            | Yes             | String          | Data type of a field.                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Set this parameter to **vector** to indicate vector fields.                                                                                                                                                                                                                                                                                                                                                                                                                        |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | dimension       | Yes             | Integer         | Number of vector dimensions.                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Value range: 1-4096                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | indexing        | No              | Boolean         | Whether to enable vector index acceleration.                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  **true**: Enables vector index acceleration. When this parameter is set to **true**, an extra vector index is created. The indexing algorithm is specified by the **algorithm** field and the index supports vector search.                                                                                                                                                                                                                                                     |
   |                 |                 |                 | -  **false**: Disables vector index acceleration. When this parameter is set to **false**, vector data is written only to docvalues, and only **ScriptScore** and **Rescore** can be used for vector search.                                                                                                                                                                                                                                                                       |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | lazy_indexing   | No              | Boolean         | Whether to enable lazy indexing, where vector indexes are not built immediately when data is ingested. The aim to speed up write operations.                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Lazy indexing takes effect only when **indexing** is set to **true** and the cluster version is OpenSearch 2.19.0.                                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  **true**: Enables lazy indexing. Vector indexes (such as graph-based indexes) are not built immediately when data is ingested. Instead, :ref:`offline index building <en-us_topic_0000002333390490__section164656265118>` needs to be performed to build vector indexes. The vector indexes can then be used for vector search.                                                                                                                                                 |
   |                 |                 |                 | -  **false** (default): Disables lazy indexing.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | algorithm       | No              | String          | Vector indexing algorithm.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | This parameter is valid only when **indexing** is set to **true**. When this parameter is set to **IVF_GRAPH** or **IVF_GRAPH_PQ**, :ref:`(Optional) Pre-Building and Registering Centroid Vectors <en-us_topic_0000001992165597__section1291152903010>` is required.                                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  **FLAT**: brute-force algorithm that calculates the distance between the target vector and all vectors in sequence. The algorithm relies on sheer computing power and its recall rate can reach 100%. You can use this algorithm if you require high recall accuracy.                                                                                                                                                                                                           |
   |                 |                 |                 | -  **GRAPH** (default): Hierarchical Navigable Small Worlds (HNSW) algorithm for graph-based indexes. This algorithm is mainly used when high performance and precision are required and the number of documents in a single shard reaches 10 million.                                                                                                                                                                                                                             |
   |                 |                 |                 | -  **GRAPH_PQ**: a combination of the HNSW algorithm and the PQ algorithm. The PQ algorithm reduces the storage overhead of the original vectors, so that HNSW can easily search through hundreds of millions of records.                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **GRAPH_SQ8**: a combination of the HNSW algorithm and the scalar quantization (SQ) algorithm. By quantizing float32 values into int8, this algorithm reduces the storage overhead of the original vectors and improves build and query efficiency. The downside is a slightly decreased recall rate. Only OpenSearch 2.19.0 clusters support this algorithm.                                                                                                                   |
   |                 |                 |                 | -  **GRAPH_SQ4**: a combination of the HNSW algorithm and the SQ algorithm. By quantizing float32 values into int4, this algorithm reduces the storage overhead of the original vectors and improves build and query efficiency. The downside is a slightly decreased recall rate. SQ4 has a higher quantization/compression ratio and higher computational efficiency than SQ8, but also a large decrease in recall rate. Only OpenSearch 2.19.0 clusters support this algorithm. |
   |                 |                 |                 | -  **IVF_GRAPH**: a combination of IVF and HNSW. The entire space is divided into multiple cluster centroids, which makes search much faster but slightly inaccurate. You can use this algorithm if you require high performance when searching through hundreds of millions of records.                                                                                                                                                                                           |
   |                 |                 |                 | -  **IVF_GRAPH_PQ**: a combination of the PQ algorithm with the IVF or HNSW algorithm to further improve the system capacity and reduce the system overhead. This algorithm is applicable when there are more than 1 billion documents in shards and high retrieval performance is required.                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | When the indexing algorithm is set to GRAPH, GRAPH_PQ, GRAPH_SQ8, or GRAPH_SQ4, CSS provides additional parameters, as shown in :ref:`Table 3 <en-us_topic_0000001992165597__table96225128514>` and :ref:`Table 4 <en-us_topic_0000001992165597__table119841865016>`, that you can choose to configure for enhanced query performance and accuracy.                                                                                                                                |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | dim_type        | No              | String          | Vector data type.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  binary: binary value                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
   |                 |                 |                 | -  float (default): floating-point number                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | metric          | No              | String          | Vector distance metric, which measures the similarity or distance between vectors.                                                                                                                                                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  **euclidean** (default): Euclidean distance                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   |                 |                 |                 | -  **inner_product**: inner product distance                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   |                 |                 |                 | -  **cosine**: cosine distance                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   |                 |                 |                 | -  **hamming**: Hamming distance, which can be used only when **dim_type** is set to **binary**.                                                                                                                                                                                                                                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001992165597__table96225128514:

.. table:: **Table 3** Optional parameters for the GRAPH indexing algorithm

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================================+
   | neighbors       | No              | Integer         | Number of neighbors of each vector in the graph index. A larger value results in higher query accuracy but slower index building and query.                 |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | This parameter is available only when **indexing** is set to **true**, and **algorithm** is GRAPH, GRAPH_PQ, GRAPH_SQ8, or GRAPH_SQ4.                       |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Value range: 20-255                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Default value: **64**                                                                                                                                       |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | shrink          | No              | Float           | How aggressively the HNSW graph removes redundant edges during construction. This setting affects the structure of the HNSW graph.                          |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Default value: 1.0f                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | This parameter is available only when **indexing** is set to **true**, and **algorithm** is GRAPH, GRAPH_PQ, GRAPH_SQ8, or GRAPH_SQ4.                       |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Value range: 0.1-10                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Default value: **1**                                                                                                                                        |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | scaling         | No              | Integer         | Scaling ratio for the number of upper-layer graph nodes in the HNSW graph. This setting affects the layers of the HNSW graph.                               |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | This parameter is available only when **indexing** is set to **true**, and **algorithm** is GRAPH, GRAPH_PQ, GRAPH_SQ8, or GRAPH_SQ4.                       |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Value range: 0-128                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Default value: 50                                                                                                                                           |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | efc             | No              | Integer         | How many nearest neighbors to explore when inserting a new vector into the HNSW graph. A larger value results in higher accuracy but slower index building. |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | This parameter is available only when **indexing** is set to **true**, and **algorithm** is GRAPH, GRAPH_PQ, GRAPH_SQ8, or GRAPH_SQ4.                       |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Value range: 0-100000                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Default value: **200**                                                                                                                                      |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | max_scan_num    | No              | Integer         | Maximum number of nodes to be scanned during search or index building. A larger value results in higher query accuracy but slower indexing.                 |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | This parameter is available only when **indexing** is set to **true**, and **algorithm** is GRAPH, GRAPH_PQ, GRAPH_SQ8, or GRAPH_SQ4.                       |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Value range: 0 to 1000000                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Default value: **10000**                                                                                                                                    |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001992165597__table119841865016:

.. table:: **Table 4** Optional parameters for the GRAPH_PQ indexing algorithm

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | centroid_num    | No              | Integer         | Number of centroids used during the coarse quantization stage of the algorithm. It affects quantization granularity and storage. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | This parameter is available only when **indexing** is set to **true**, and **algorithm** is GRAPH_PQ.                            |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Value range: 0-65535                                                                                                             |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Default value: 255                                                                                                               |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | fragment_num    | No              | Integer         | Number of fragments each vector is split into. It affects the PQ quantization granularity.                                       |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | The default value is **0**. The plug-in automatically sets the number of fragments based on the vector length.                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | This parameter is available only when **indexing** is set to **true**, and **algorithm** is GRAPH_PQ.                            |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Value range: 0-4096                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Default value: **0**. The plug-in automatically sets the number of fragments based on the vector length.                         |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001992165597__section1291152903010:

(Optional) Pre-Building and Registering Centroid Vectors
--------------------------------------------------------

When the IVF_GRAPH or IVF_GRAPH_PQ algorithm is used for vector indexing, you need to pre-build and register centroid vectors.

IVF_GRAPH and IVF_GRAPH_PQ help to accelerate indexing and queries in ultra-large-scale clusters. These two algorithms allow you to narrow down the query scope by dividing a vector space into subspaces through clustering or random sampling. Before pre-build, you need to obtain all centroid vectors through clustering or random sampling. Centroid vectors are pre-built into a GRAPH or GRAPH_PQ index and then registered with the Elasticsearch cluster. All nodes in the cluster can share this index. Reuse of the centroid index among shards can effectively reduce the training overhead and the number of centroid index queries, improving write and query performance.

#. Create a centroid index.

   For example, run the following command on OpenSearch Dashboards to create a centroid index named **my_dict**:

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

   For detailed parameter configuration, see :ref:`Creating a Vector Index <en-us_topic_0000001992165597__en-us_topic_0000001309709789_section137344225249>`. Pay attention to the following mandatory parameters:

   -  **index.number_of_shards**: The number of index shards must be set to **1**. Otherwise, the centroid index cannot be registered.
   -  **indexing**: This parameter must be set to **true** to enable vector index acceleration.
   -  **algorithm**: Set the indexing algorithm. Set it to **GRAPH** for the IVF_GRAPH algorithm, and GRAPH_PQ if the IVF_GRAPH_PQ algorithm is used.

#. Write centroid vectors to the created index. Write the centroid vectors obtained through sampling or clustering into the newly created index **my_dict**.

#. Call the registration API.

   Run the following command on OpenSearch Dashboards to register the centroid index as a Dict object with a globally unique name (**dict_name**):

   .. code-block:: text

      PUT _vector/register/my_dict
       {
         "dict_name": "my_dict"
       }

#. Create an IVF_GRAPH or IVF_GRAPH_PQ vector index.

   When creating the vector index, you do not need to specify **dimension** or **metric**. Rather, you specify the registered Dict object. :ref:`Table 5 <en-us_topic_0000001992165597__table3711163717243>` describes key parameters for specifying a Dict object. For details about other parameters, see :ref:`Creating a Vector Index <en-us_topic_0000001992165597__en-us_topic_0000001309709789_section137344225249>`.

   For example, run the following command to create an IVF_GRAPH vector index:

   .. code-block:: text

      PUT my_index
       {
         "settings": {
           "index": {
             "vector": true,
             "sort.field": "my_vector.centroid" # Set the centroid subfield of each vector field as a ranking field.
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

   .. _en-us_topic_0000001992165597__table3711163717243:

   .. table:: **Table 5** Field mappings parameters

      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                    |
      +=================+=================+=================+================================================================================================================================================================================================================+
      | dict_name       | Yes             | String          | Name of the centroid index. For example, **my_dict**. The vector dimensions and metrics of the index must be the same as those of the Dict index.                                                              |
      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | offload_ivf     | Yes             | Boolean         | Whether to offload the IVF inverted index to Elasticsearch.                                                                                                                                                    |
      |                 |                 |                 |                                                                                                                                                                                                                |
      |                 |                 |                 | Value: **true** or **false**.                                                                                                                                                                                  |
      |                 |                 |                 |                                                                                                                                                                                                                |
      |                 |                 |                 | -  **true** (recommended value): Offloads the IVF inverted index implemented by the underlying index to Elasticsearch. This reduces the use of off-heap memory and the overhead of write and merge operations. |
      |                 |                 |                 | -  **false** (default value): Not to offload the IVF inverted index.                                                                                                                                           |
      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
