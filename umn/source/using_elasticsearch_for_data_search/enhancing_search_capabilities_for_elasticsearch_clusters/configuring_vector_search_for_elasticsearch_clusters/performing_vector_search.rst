:original_name: css_01_0123.html

.. _css_01_0123:

Performing Vector Search
========================

The CSS vector database supports a variety of query methods, including standard query, hybrid query, script_score query, rescore query, and painless syntax extension. They enable efficient vector data search by accommodating diverse search needs.

-  :ref:`Standard Query <en-us_topic_0000002319719730__en-us_topic_0000001268154489_section344710865418>`: retrieves documents that are most similar to the query vector.
-  :ref:`Hybrid Query <en-us_topic_0000002319719730__en-us_topic_0000001268154489_section102341611718>`: combines vector search with traditional Elasticsearch queries, such as pre-filtering and Boolean queries.
-  :ref:`Script Score Query <en-us_topic_0000002319719730__en-us_topic_0000001268154489_section4946246546>`: enables custom similarity calculations for vector searches by executing a custom script
-  :ref:`Rescore Query <en-us_topic_0000002319719730__en-us_topic_0000001268154489_section107953451661>`: rescores and reranks the top results returned by an initial query to improve recall.
-  :ref:`Painless Syntax Extension <en-us_topic_0000002319719730__section102071126171611>`: allows the use of vector distance or similarity calculation functions in custom scripts.

.. _en-us_topic_0000002319719730__en-us_topic_0000001268154489_section344710865418:

Standard Query
--------------

Standard query is used to retrieve documents that are most similar to the query vector.

The following command will return *k* (specified by **size**/**topk**) records that are the closest matches to the query vector.

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

.. table:: **Table 1** Parameters for standard query

   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter              | Mandatory       | Type            | Description                                                                                                                                                |
   +========================+=================+=================+============================================================================================================================================================+
   | size                   | Yes             | Integer         | Number of search results to return.                                                                                                                        |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Default value: **10**                                                                                                                                      |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | \_source               | No              | Boolean         | Whether to return the source text in documents. To reduce data transmission and improve query performance, set this parameter to **false**.                |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Value range:                                                                                                                                               |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | -  **true** (default): Returns the source text.                                                                                                            |
   |                        |                 |                 | -  **false**: Not to return the source text.                                                                                                               |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | query                  | Yes             | Map             | Specifies the query vector.                                                                                                                                |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Parameters:                                                                                                                                                |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | **vector** (mandatory): indicates a vector query (vector similarity-based search), including the vector field and query vector value.                      |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | **my_vector** (mandatory): queried vector field (for example, **my_vector**).                                                                              |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | vector (sub-parameter) | Yes             | Array/String    | Query vector value. It is used to calculate the similarity between indexed vectors and the query vector.                                                   |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | The value can be an array (for example, [1, 1]) or Base64-encoded value (for example, **AAABAAACAAAD**).                                                   |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | topk                   | Yes             | Integer         | The number of the most similar or relevant results to be returned.                                                                                         |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Default value: same as **size**.                                                                                                                           |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ef                     | No              | Integer         | How many nearest neighbors to explore when inserting a new vector into the graph. A larger value indicates a higher query accuracy yet slower query speed. |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | This parameter is available only when **algorithm** is set to GRAPH, GRAPH_PQ, GRAPH_SQ8, or GRAPH_SQ4.                                                    |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Value range: 0-100000                                                                                                                                      |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Default value: **200**                                                                                                                                     |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | max_scan_num           | No              | Integer         | Maximum number of graph nodes to scan during search. A larger value indicates a higher query accuracy yet slower query speed.                              |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | This parameter is available only when **algorithm** is set to GRAPH, GRAPH_PQ, GRAPH_SQ8, or GRAPH_SQ4.                                                    |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Value range: 0-1000000                                                                                                                                     |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Default value: **10000**                                                                                                                                   |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | nprobe                 | No              | Integer         | Number of centroids to explore during an IVF index query. A larger value indicates a higher query accuracy yet slower query speed.                         |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | This parameter is available only when **algorithm** is IVF_GRAPH or IVF_GRAPH_PQ.                                                                          |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Value range: 0-100000                                                                                                                                      |
   |                        |                 |                 |                                                                                                                                                            |
   |                        |                 |                 | Default value: **100**                                                                                                                                     |
   +------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002319719730__en-us_topic_0000001268154489_section102341611718:

Hybrid Query
------------

Hybrid query combines vector search with traditional Elasticsearch queries, such as pre-filtering and Boolean queries.

.. warning::

   Only Elasticsearch 7.10.2 clusters support pre-filtering queries.

In the following example, the top 10 records whose **my_label** value is **red** are returned.

-  **Pre-filtering query**

   First, filters are applied to retrieve matching results. Then, vector search is performed on these results to retrieve the most relevant vectors based on similarity.

   The following is an example:

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

   .. table:: **Table 2** Parameters for pre-filtering query

      +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      +=================+=================+=================+===============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | filter          | Yes             | Map             | Vector query filters. Standard Elasticsearch query filters are supported, such as term and range.                                                                                                                                                                                                                                                                                                                                                                                             |
      |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                 |                 |                 | If **filter** is too restrictive, leading to a small intermediate result set, you can set the **index.vector.exact_search_threshold** parameter, so that when the intermediate result set is smaller than this threshold, pre-filtering query automatically switches over to brute-force query (FLAT algorithm), which ensures a high recall rate. For more information, see :ref:`Creating a Vector Index <en-us_topic_0000002319559898__en-us_topic_0000001309709789_section137344225249>`. |
      +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | term            | No              | Map             | Term query is a type of exact query. Documents that contain the exact term will be returned. For example, **{"term": {"my_label": "red"}}** means only to return documents whose **my_label** value is **red**.                                                                                                                                                                                                                                                                               |
      +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  **Boolean query**

   A Boolean query is in fact a post-filtering query method. Filtering and vector similarity-based search are performed separately. Then, the results of the two are combined using Boolean logic defined by clauses like must, should, and filter.

   The following is an example:

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

   .. table:: **Table 3** Boolean query parameters

      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter       | Mandatory       | Type            | Description                                                                                                                                        |
      +=================+=================+=================+====================================================================================================================================================+
      | bool            | Yes             | Map             | A compound query clause that combines subqueries using configured Boolean logic.                                                                   |
      |                 |                 |                 |                                                                                                                                                    |
      |                 |                 |                 | Parameter description:                                                                                                                             |
      |                 |                 |                 |                                                                                                                                                    |
      |                 |                 |                 | -  **must**: Clauses that must match for documents to be included in the results.                                                                  |
      |                 |                 |                 | -  **filter**: It is similar to **must**, but do not contribute to the relevance score.                                                            |
      |                 |                 |                 | -  **should**: Clauses that should match, but are not required. They are like nice-to-haves.                                                       |
      |                 |                 |                 | -  **must_not**: Clauses that must not match for documents to be included in the results.                                                          |
      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
      | bool.must       | Yes             | Map             | Clauses that must match for documents to be included in the results. Parameter description:                                                        |
      |                 |                 |                 |                                                                                                                                                    |
      |                 |                 |                 | -  **vector**: query vector                                                                                                                        |
      |                 |                 |                 | -  **my_vector**: vector field                                                                                                                     |
      |                 |                 |                 | -  **topk**: number of results to return                                                                                                           |
      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
      | bool.filter     | Yes             | Map             | Clauses that must match, but do not contribute to the relevance score. Standard Elasticsearch query filters are supported, such as term and range. |
      +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002319719730__en-us_topic_0000001268154489_section4946246546:

Script Score Query
------------------

Script_score query enables custom similarity calculations for vector searches by executing a user-defined script. It works as follows:

Pre-filtering works with any query. **script_score** then calculates vector similarity on the pre-filtered results, and ranks the results. This query method does not use vector indexes. Its performance depends on the size of the intermediate result set after the pre-filtering. If the pre-filtering condition is set to **match_all**, a brute-force search is performed on all data.

The following is an example:

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

.. table:: **Table 4** script_score query parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                |
   +=================+=================+=================+============================================================================================================================+
   | script_score    | Yes             | Map             | A root parameter for the script_score query.                                                                               |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | Parameter description:                                                                                                     |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | -  **query**: pre-filtering criteria. When it is set to **match_all**, a brute-force search is performed on all data.      |
   |                 |                 |                 | -  **script**: custom script that calculates similarity scores.                                                            |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+
   | source          | Yes             | String          | Script name. The value is fixed to **vector_score**, indicating that a built-in script is used for calculating similarity. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+
   | lang            | Yes             | String          | Script language type. The value is fixed to **vector**.                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+
   | field           | Yes             | String          | Queried vector field, for example, **my_vector**.                                                                          |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+
   | vector          | Yes             | Array/String    | Query vector value. It is used to calculate the similarity between indexed vectors and the query vector.                   |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | The value can be an array (for example, [1, 1]) or Base64-encoded value (for example, **AAABAAACAAAD**).                   |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+
   | metric          | Yes             | String          | Vector distance metric, which measures the similarity or distance between vectors.                                         |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | Value range:                                                                                                               |
   |                 |                 |                 |                                                                                                                            |
   |                 |                 |                 | -  **euclidean** (default): Euclidean distance                                                                             |
   |                 |                 |                 | -  **inner_product**: inner product distance                                                                               |
   |                 |                 |                 | -  **cosine**: cosine distance                                                                                             |
   |                 |                 |                 | -  **hamming**: Hamming distance, which can be used only when **dim_type** is set to **binary**.                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002319719730__en-us_topic_0000001268154489_section107953451661:

Rescore Query
-------------

Rescore query rescores and reranks the top results returned by an initial query to improve recall.

When the GRAPH_PQ or IVF_GRAPH_PQ indexing algorithm is used, query results are ranked based on the asymmetric distance calculated by PQ. Rescore query then rescores and reranks the initial search results to improve recall.

The following is an example of rescore query on a PQ index named **my_index**:

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

.. table:: **Table 5** Rescore query parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================================================================================================================================================================+
   | rescore         | Yes             | Map             | Defines rescoring parameters.                                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | Key parameters:                                                                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | -  window_size: rescoring/reranking window size.                                                                                                                                                                                                                                        |
   |                 |                 |                 | -  vector_rescore: other vector rescoring settings.                                                                                                                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | window_size     | Yes             | Integer         | Rescoring/reranking window size. The vector search returns the top k results, but only the first *window_size* results are rescored and reranked. A larger value indicates a larger reranking scope and hence a higher recall rate, but it also leads to higher computational overhead. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | Default value: **100**                                                                                                                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | field           | Yes             | String          | Queried vector field, for example, **my_vector**.                                                                                                                                                                                                                                       |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | vector          | Yes             | Array/String    | Query vector value. It is used to calculate the similarity between indexed vectors and the query vector.                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | The value can be an array (for example, [1, 1]) or Base64-encoded value (for example, **AAABAAACAAAD**).                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | metric          | Yes             | String          | Vector distance metric, which measures the similarity or distance between vectors.                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | Value range:                                                                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                         |
   |                 |                 |                 | -  **euclidean** (default): Euclidean distance                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **inner_product**: inner product distance                                                                                                                                                                                                                                            |
   |                 |                 |                 | -  **cosine**: cosine distance                                                                                                                                                                                                                                                          |
   |                 |                 |                 | -  **hamming**: Hamming distance, which can be used only when **dim_type** is set to **binary**.                                                                                                                                                                                        |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002319719730__section102071126171611:

Painless Syntax Extension
-------------------------

Painless syntax extension allows the use of vector distance or similarity calculation functions in custom scripts. CSS extension supports several vector distance/similarity calculation functions, which users can use readily in custom Painless scripts to build flexible rescoring formulas.

The following is an example:

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

.. table:: **Table 6** Supported vector distance/similarity calculation functions

   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
   | Function Signature               | Description                                                                                                                                     |
   +==================================+=================================================================================================================================================+
   | euclidean(Float[], DocValues)    | Euclidean distance                                                                                                                              |
   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
   | cosine(Float[], DocValues)       | Cosine similarity                                                                                                                               |
   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
   | innerproduct(Float[], DocValues) | Inner product                                                                                                                                   |
   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
   | hamming(String, DocValues)       | Hamming distance Only vectors whose **dim_type** is **binary** are supported. The input query vector must be a Base64-encoded character string. |
   +----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
