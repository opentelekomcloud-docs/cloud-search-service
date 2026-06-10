:original_name: css_01_0123.html

.. _css_01_0123:

Performing Vector Search
========================

In modern AI search applications, high-dimensional vectors capture the semantic essence of data, while business-specific tags (such as category, price, and region) enable precise filtering. While standard vector search is fast, it often struggles to accommodate complex business logic or custom ranking requirements. To bridge the gap between performance and flexibility, the CSS vector database supports a wide range of query methods, from ultra-fast approximate nearest neighbor (ANN) search to intensive re-scoring and fully customizable, script-based ranking. By strategically implementing pre-filtering to narrow the search space, or leveraging re-scoring to compensate for precision loss from vector quantization, developers can build intelligent search engines capable of efficiently processing datasets with hundreds of millions of records while meeting service requirements for both low latency and high recall.

Comparing Different Query Methods
---------------------------------

To balance search accuracy and performance, select an appropriate query method based on the size of your dataset.

.. table:: **Table 1** A comparison of different query methods

   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
   | Query Method                | How It Works                                                                                                                                                                                                                                                                                                                                                      | When to Use                                                                                                                                                | Cluster Version                |
   +=============================+===================================================================================================================================================================================================================================================================================================================================================================+============================================================================================================================================================+================================+
   | Standard vector search      | Executes ANN searches using graph-based structures like HNSW. Navigating pre-built hierarchical layers enables millisecond-level latency. This method maintains both ultra-high throughput and high recall precision (with only a slight loss).                                                                                                                   | Large-scale general search: scenarios that prioritize low latency, such as searching through hundreds of millions of images and recommending short videos. | Elasticsearch: 7.6.2 or 7.10.2 |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            |                                |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            | OpenSearch: 1.3.6 or 2.19.0    |
   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
   | Hybrid query: pre-filtering | Applies metadata filtering (such as category and region) first, and then executes full vector search on the filtered candidate set. By drastically pruning the search space, this method ensures excellent search performance and high recall. The returned results match the applied filters.                                                                    | Conditional search: precise metadata filtering, for example, searching for similar products under a specific brand.                                        | Elasticsearch: 7.10.2          |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            |                                |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            | OpenSearch: 2.19.0             |
   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
   | Hybrid query: Boolean query | Boolean query is in fact a post-filtering query method, where vector search and tag-based filtering are performed separately and then their results are merged using Boolean logic.                                                                                                                                                                               | Simple logic combination: where fusion scoring is required or a legacy version does not support pre-filtering.                                             | Elasticsearch: 7.6.2 or 7.10.2 |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            |                                |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            | OpenSearch: 1.3.6 or 2.19.0    |
   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
   | Script score query          | This method does not deal with vector indexes. It performs brute-force search on an intermediate result set obtained through pre-filtering. A 100% recall rate can be achieved on the filtered subset. However, latency increases linearly with the data volume, leading to performance bottlenecks on large datasets.                                            | Small-scale ranking: high-precision matching over small datasets (less than 10,000 records) or second-pass ranking after precise metadata filtering.       | Elasticsearch: 7.6.2 or 7.10.2 |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            |                                |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            | OpenSearch: 1.3.6 or 2.19.0    |
   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
   | Rescore query               | This method uses a two-stage retrieval process: pre-filtering and reranking. First, an initial query quickly retrieves a relatively large candidate set from the vector index, and then the top N more relevant results are retrieved through a precise reranking. This method significantly improves retrieval precision with only a slight increase in latency. | Large-scale quantization: Mitigates the precision loss of PQ quantization and ensures high recall while keeping a low memory footprint.                    | Elasticsearch: 7.6.2 or 7.10.2 |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            |                                |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            | OpenSearch: 1.3.6 or 2.19.0    |
   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+
   | Painless syntax extension   | Calls specialized vector functions via a custom script to implement complex, multi-weighted scoring formulas. Performance and precision can be tuned flexibly, with support for high-dimensional custom service logic.                                                                                                                                            | Dynamic, multi-factor ranking, for example, based on "similarity + price offset + promotion weight"                                                        | Elasticsearch: 7.6.2 or 7.10.2 |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            |                                |
   |                             |                                                                                                                                                                                                                                                                                                                                                                   |                                                                                                                                                            | OpenSearch: 1.3.6 or 2.19.0    |
   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+

Logging in to Dev Tools
-----------------------

Log into Dev Tools to run DSL commands.

-  **For an Elasticsearch cluster, log in to Kibana**

   #. Log in to the CSS management console.

   #. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   #. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   #. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

-  **For an OpenSearch cluster, log in to Dashboards**

   #. Log in to the CSS management console.

   #. In the navigation pane on the left, choose **Clusters > OpenSearch**.

   #. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

   #. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

.. _en-us_topic_0000002555376597__en-us_topic_0000001268154489_section344710865418:

Standard Vector Query
---------------------

Run the following command to retrieve the top K records that are the closest matches to the query vector.

.. code-block:: text

   POST my_index/_search
   {
     "size":2,
     "_source": false,
     "query": {
       "vector": {
         "my_vector": {
           "vector": [1, 1],
           "topk":2
         }
       }
     }
   }

.. table:: **Table 2** Parameters for standard query

   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter              | Mandatory   | Type         | Default Value | Description                                                                                                                                                                                                                                                                                   |
   +========================+=============+==============+===============+===============================================================================================================================================================================================================================================================================================+
   | size                   | No          | Integer      | 10            | Number of final search results to return.                                                                                                                                                                                                                                                     |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | \_source               | No          | Boolean      | true          | Whether to return the source text in documents. To reduce data transmission and improve query performance, set this parameter to **false**.                                                                                                                                                   |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | The value can be:                                                                                                                                                                                                                                                                             |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | -  **true**: Returns the source text.                                                                                                                                                                                                                                                         |
   |                        |             |              |               | -  **false**: Not to return the source text.                                                                                                                                                                                                                                                  |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | query                  | Yes         | Map          | N/A           | Specifies the query vector.                                                                                                                                                                                                                                                                   |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Parameter description:                                                                                                                                                                                                                                                                        |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | **vector** (mandatory): indicates a vector query (vector similarity-based search), including the vector field and query vector value.                                                                                                                                                         |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | **my_vector** (mandatory): queried vector field (for example, **my_vector**).                                                                                                                                                                                                                 |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | vector (sub-parameter) | Yes         | Array/String | N/A           | Query vector value. It is used to calculate the similarity between indexed vectors and the query vector.                                                                                                                                                                                      |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | The value can be an array (for example, [1, 1]) or Base64-encoded value (for example, **AAABAAACAAAD**).                                                                                                                                                                                      |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | topk                   | Yes         | Integer      | N/A           | The number of the most similar or relevant results to be returned.                                                                                                                                                                                                                            |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Keep the value consistent with **size**.                                                                                                                                                                                                                                                      |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ef                     | No          | Integer      | 200           | The number of neighbor nodes to explore within the HNSW graph during a query. A larger value indicates a higher query accuracy yet slower query speed.                                                                                                                                        |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Constraints: This parameter is available only for graph-based indexing algorithms. Specifically, it takes effect when **algorithm** is set to **GRAPH**, **GRAPH_PQ**, **GRAPH_SQ8**, or **GRAPH_SQ4**.                                                                                       |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Value range: 0-100000                                                                                                                                                                                                                                                                         |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | max_scan_num           | No          | Integer      | 10000         | Maximum number of graph nodes to scan within the HNSW graph during a query. A larger value indicates a higher query accuracy yet slower query speed.                                                                                                                                          |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Constraints: This parameter is available only for graph-based indexing algorithms. Specifically, it takes effect when **algorithm** is set to **GRAPH**, **GRAPH_PQ**, **GRAPH_SQ8**, or **GRAPH_SQ4**.                                                                                       |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Value range: 0-1000000                                                                                                                                                                                                                                                                        |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rescore                | No          | Boolean      | false         | Whether to enable rescore query. During PQ or SQ index queries, this parameter determines whether to enable rescore query. The effect is the same as :ref:`Rescore Query <en-us_topic_0000002555376597__en-us_topic_0000001268154489_section107953451661>`, but the configuration is simpler. |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Constraints: This parameter is available only for Elasticsearch 7.10.2 and OpenSearch 2.19.0 clusters, and the image version must be x.x.x_26.1.0_xxx or later.                                                                                                                               |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | The value can be:                                                                                                                                                                                                                                                                             |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | -  **true**: Enable rescore query.                                                                                                                                                                                                                                                            |
   |                        |             |              |               | -  **false**: Disable rescore query.                                                                                                                                                                                                                                                          |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | nprobe                 | No          | Integer      | 100           | Number of centroids to explore during an IVF index query. A larger value indicates a higher query accuracy yet slower query speed.                                                                                                                                                            |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Constraints: This parameter is available only for IVF-based algorithms. Specifically, it takes effect when **algorithm** is set to **IVF_GRAPH** or **IVF_GRAPH_PQ**.                                                                                                                         |
   |                        |             |              |               |                                                                                                                                                                                                                                                                                               |
   |                        |             |              |               | Value range: 0-100000                                                                                                                                                                                                                                                                         |
   +------------------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Hybrid Query: Pre-filtering
---------------------------

.. caution::

   Only Elasticsearch 7.10.2 and OpenSearch 2.19.0 clusters support pre-filtering.

A hybrid query means combining vector search with other DSL queries. With pre-filtering, documents are first filtered using metadata tags (such as colors and categories), and then vector similarity search is performed on the filtered result set to return the most similar results.

Run the following command to retrieve the top 10 results whose **my_label** is **red**:

.. code-block:: text

   POST my_index/_search
   {
     "size": 10,
     "query": {
       "vector": {
         "my_vector": {
           "vector": [1, 2],
           "topk": 10,
           "filter": {
             "term": { "my_label": "red" }
           }
         }
       }
     }
   }

.. table:: **Table 3** Parameters of pre-filtering query

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
   +=================+=================+=================+===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | filter          | Yes             | Map             | Vector query filters.                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 | The filters are in key-value pairs. The key can be a standard filter such as term and range, and the value is the specific filtering condition.                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 | If **filter** is too restrictive, leading to a small intermediate result set, you can set the **index.vector.exact_search_threshold** parameter, so that when the intermediate result set is smaller than this threshold, pre-filtering query automatically switches over to brute-force query (FLAT algorithm), which ensures a high recall rate. For more information, see :ref:`Creating a Vector Index <en-us_topic_0000002523711048__en-us_topic_0000001309709789_section137344225249>`. |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | term            | No              | Map             | Term query is a type of exact query.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 | In the key-value pair, the key is the field name, and the value is the exact value to match.                                                                                                                                                                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   |                 |                 |                 | For example, **{"term": {"my_label": "red"}}** means only to return documents whose **my_label** value is **red**.                                                                                                                                                                                                                                                                                                                                                                            |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Hybrid Query: Boolean Query
---------------------------

A hybrid query means combining vector search with other DSL queries. A Boolean query is in fact a post-filtering query method. Filtering and vector similarity-based search are performed separately. Then, the results of the two are combined using Boolean logic defined by clauses like must, should, and filter.

Run the following command to retrieve the top 10 results whose **my_label** is **red**:

.. code-block:: text

   POST my_index/_search
   {
     "size": 10,
     "query": {
       "bool": {
         "must": {
           "vector": {
             "my_vector": {
               "vector": [1, 2],
               "topk": 10
             }
           }
         },
         "filter": {
           "term": { "my_label": "red" }
         }
       }
     }
   }

.. table:: **Table 4** Boolean query parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                  |
   +=================+=================+=================+==============================================================================================+
   | bool            | Yes             | Map             | A compound query clause that combines subqueries using configured Boolean logic.             |
   |                 |                 |                 |                                                                                              |
   |                 |                 |                 | Parameter description:                                                                       |
   |                 |                 |                 |                                                                                              |
   |                 |                 |                 | -  **must**: Clauses that must match for documents to be included in the results.            |
   |                 |                 |                 | -  **filter**: It is similar to **must**, but does not contribute to the relevance score.    |
   |                 |                 |                 | -  **should**: Clauses that should match, but are not required. They are like nice-to-haves. |
   |                 |                 |                 | -  **must_not**: Clauses that must not match for documents to be included in the results.    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+
   | bool.must       | Yes             | Map             | Clauses that must match for documents to be included in the results.                         |
   |                 |                 |                 |                                                                                              |
   |                 |                 |                 | Parameter description:                                                                       |
   |                 |                 |                 |                                                                                              |
   |                 |                 |                 | -  **vector**: query vector                                                                  |
   |                 |                 |                 | -  **my_vector**: vector field                                                               |
   |                 |                 |                 | -  **topk**: number of results to return                                                     |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+
   | bool.filter     | Yes             | Map             | Clauses that must match, but do not contribute to the relevance score.                       |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------+

Script Score Query
------------------

This method calculates vector similarity on pre-filtered results by executing a user-defined script. It does not use vector indexes. Its performance depends on the size of the pre-filtered result set. If the pre-filtering condition is set to **match_all**, a brute-force search is performed on all data.

Run the following command to perform a brute-force search to retrieve two vector records:

.. code-block:: text

   POST my_index/_search
    {
      "size":2,
      "query": {
      "script_score": {
          "query": {
            "match_all": {}
          },
          "script": {
            "source": "vector_score",
            "lang": "vector",
            "params": {
              "field": "my_vector",
              "vector": [1.0, 2.0],
              "metric": "euclidean"
            }
          }
        }
      }
    }

.. table:: **Table 5** script_score query parameters

   +--------------+-------------+--------------+---------------+----------------------------------------------------------------------------------------------------------------------------+
   | Parameter    | Mandatory   | Type         | Default Value | Description                                                                                                                |
   +==============+=============+==============+===============+============================================================================================================================+
   | script_score | Yes         | Map          | N/A           | A root parameter for the script_score query.                                                                               |
   |              |             |              |               |                                                                                                                            |
   |              |             |              |               | Parameter description:                                                                                                     |
   |              |             |              |               |                                                                                                                            |
   |              |             |              |               | -  **query**: pre-filtering criteria. When it is set to **match_all**, a brute-force search is performed on all data.      |
   |              |             |              |               | -  **script**: custom script that calculates similarity scores.                                                            |
   +--------------+-------------+--------------+---------------+----------------------------------------------------------------------------------------------------------------------------+
   | source       | Yes         | String       | N/A           | Script name. The value is fixed to **vector_score**, indicating that a built-in script is used for calculating similarity. |
   +--------------+-------------+--------------+---------------+----------------------------------------------------------------------------------------------------------------------------+
   | lang         | Yes         | String       | N/A           | Script language type. The value is fixed to **vector**.                                                                    |
   +--------------+-------------+--------------+---------------+----------------------------------------------------------------------------------------------------------------------------+
   | field        | Yes         | String       | N/A           | Queried vector field, for example, **my_vector**.                                                                          |
   +--------------+-------------+--------------+---------------+----------------------------------------------------------------------------------------------------------------------------+
   | vector       | Yes         | Array/String | N/A           | Query vector value. It is used to calculate the similarity between indexed vectors and the query vector.                   |
   |              |             |              |               |                                                                                                                            |
   |              |             |              |               | The value can be an array (for example, [1, 1]) or Base64-encoded value (for example, **AAABAAACAAAD**).                   |
   +--------------+-------------+--------------+---------------+----------------------------------------------------------------------------------------------------------------------------+
   | metric       | No          | String       | euclidean     | Vector distance metric, which measures the similarity or distance between vectors.                                         |
   |              |             |              |               |                                                                                                                            |
   |              |             |              |               | The value can be:                                                                                                          |
   |              |             |              |               |                                                                                                                            |
   |              |             |              |               | -  **euclidean**: Euclidean distance                                                                                       |
   |              |             |              |               | -  **inner_product**: inner product distance                                                                               |
   |              |             |              |               | -  **cosine**: cosine distance                                                                                             |
   |              |             |              |               | -  **hamming**: Hamming distance, which can be used only when **dim_type** is set to **binary**.                           |
   +--------------+-------------+--------------+---------------+----------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002555376597__en-us_topic_0000001268154489_section107953451661:

Rescore Query
-------------

When the index uses the GRAPH_PQ or IVF_GRAPH_PQ algorithm, the query consists of two stages: first, a quick filtering is performed on the compressed vectors; then, the original vectors are retrieved to accurately rank the top K results to improve recall.

Assume that **my_index** is an index that utilizes product quantization. Run the following command to perform a rescore query to return 10 results:

.. code-block:: text

   GET my_index/_search
    {
      "size": 10,
      "query": {
        "vector": {
          "my_vector": {
            "vector": [1.0, 2.0],
            "topk": 100
          }
        }
      },
      "rescore": {
        "window_size": 100,
        "vector_rescore": {
          "field": "my_vector",
          "vector": [1.0, 2.0],
          "metric": "euclidean"
        }
      }
    }

.. table:: **Table 6** Rescore query parameters

   +-------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter   | Mandatory   | Type         | Default Value | Description                                                                                                                                                                                                                                                                             |
   +=============+=============+==============+===============+=========================================================================================================================================================================================================================================================================================+
   | rescore     | Yes         | Map          | N/A           | Defines rescoring parameters.                                                                                                                                                                                                                                                           |
   |             |             |              |               |                                                                                                                                                                                                                                                                                         |
   |             |             |              |               | Parameter description:                                                                                                                                                                                                                                                                  |
   |             |             |              |               |                                                                                                                                                                                                                                                                                         |
   |             |             |              |               | -  **window_size**: rescoring/reranking window size.                                                                                                                                                                                                                                    |
   |             |             |              |               | -  **vector_rescore**: other vector rescoring settings.                                                                                                                                                                                                                                 |
   |             |             |              |               |                                                                                                                                                                                                                                                                                         |
   |             |             |              |               | .. caution::                                                                                                                                                                                                                                                                            |
   |             |             |              |               |                                                                                                                                                                                                                                                                                         |
   |             |             |              |               |    CAUTION:                                                                                                                                                                                                                                                                             |
   |             |             |              |               |    To implement rescore query for nested fields, perform :ref:`Standard Vector Query <en-us_topic_0000002555376597__en-us_topic_0000001268154489_section344710865418>`.                                                                                                                 |
   +-------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | window_size | No          | Integer      | 100           | Rescoring/reranking window size. The vector search returns the top k results, but only the first *window_size* results are rescored and reranked. A larger value indicates a larger reranking scope and hence a higher recall rate, but it also leads to higher computational overhead. |
   +-------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | field       | Yes         | String       | N/A           | Queried vector field, for example, **my_vector**.                                                                                                                                                                                                                                       |
   +-------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | vector      | Yes         | Array/String | N/A           | Query vector value. It is used to calculate the similarity between indexed vectors and the query vector.                                                                                                                                                                                |
   |             |             |              |               |                                                                                                                                                                                                                                                                                         |
   |             |             |              |               | The value can be an array (for example, [1, 1]) or Base64-encoded value (for example, **AAABAAACAAAD**).                                                                                                                                                                                |
   +-------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | metric      | No          | String       | euclidean     | Vector distance metric, which measures the similarity or distance between vectors.                                                                                                                                                                                                      |
   |             |             |              |               |                                                                                                                                                                                                                                                                                         |
   |             |             |              |               | The value can be:                                                                                                                                                                                                                                                                       |
   |             |             |              |               |                                                                                                                                                                                                                                                                                         |
   |             |             |              |               | -  **euclidean**: Euclidean distance                                                                                                                                                                                                                                                    |
   |             |             |              |               | -  **inner_product**: inner product distance                                                                                                                                                                                                                                            |
   |             |             |              |               | -  **cosine**: cosine distance                                                                                                                                                                                                                                                          |
   |             |             |              |               | -  **hamming**: Hamming distance, which can be used only when **dim_type** is set to **binary**.                                                                                                                                                                                        |
   +-------------+-------------+--------------+---------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Painless Syntax Extension
-------------------------

This method allows you to embed vector distance or similarity calculation functions in custom scripts to implement complex logic.

Run the following command to perform a Painless syntax extension-based query to retrieve 10 vector records:

.. code-block:: text

   POST my_index/_search
   {
     "size": 10,
     "query": {
       "script_score": {
         "query": {
           "match_all": {}
         },
         "script": {
           "source": "1 / (1 + euclidean(params.vector, doc[params.field]))",
           "params": {
             "field": "my_vector",
             "vector": [1, 2]
           }
         }
       }
     }
   }

As shown in :ref:`Table 7 <en-us_topic_0000002555376597__table17610185023516>`, CSS supports several vector distance/similarity calculation functions, which users can use readily in custom Painless scripts to build flexible rescoring formulas.

.. _en-us_topic_0000002555376597__table17610185023516:

.. table:: **Table 7** Supported vector distance/similarity calculation functions

   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
   | Function Signature                | Description                                                                                                             |
   +===================================+=========================================================================================================================+
   | euclidean(Float[], DocValues)     | Euclidean distance                                                                                                      |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
   | cosine(Float[], DocValues)        | Cosine similarity                                                                                                       |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
   | innerproduct(Float[], DocValues)  | Inner product                                                                                                           |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
   | hamming(String, DocValues)        | Hamming distance                                                                                                        |
   |                                   |                                                                                                                         |
   |                                   | Constraints:                                                                                                            |
   |                                   |                                                                                                                         |
   |                                   | -  Only vectors whose **dim_type** is **binary** are supported. The input query vector must be a Base64-encoded string. |
   |                                   | -  Only Elasticsearch 7.6.2, Elasticsearch 7.10.2, and OpenSearch 1.3.6 clusters support this function.                 |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
   | hammings(String, DocValues)       | Hamming distance                                                                                                        |
   |                                   |                                                                                                                         |
   |                                   | Constraints:                                                                                                            |
   |                                   |                                                                                                                         |
   |                                   | -  Only vectors whose **dim_type** is **binary** are supported. The input query vector must be a Base64-encoded string. |
   |                                   | -  Only OpenSearch 2.19.0 clusters support this function.                                                               |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------+
