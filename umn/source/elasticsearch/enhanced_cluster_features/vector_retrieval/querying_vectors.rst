:original_name: css_01_0123.html

.. _css_01_0123:

Querying Vectors
================

Standard Query
--------------

Standard vector query syntax is provided for vector fields with vector indexes. The following command will return *n* (specified by **size**/**topk**) data records that are most close to the query vector.

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

   +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                                                                    | Description                                                                                                                       |
   +==============================================================================+===================================================================================================================================+
   | vector (the first one)                                                       | Indicates that the query type is **VectorQuery**.                                                                                 |
   +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | my_vector                                                                    | Indicates the name of the vector field you want to query.                                                                         |
   +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | vector (the second one)                                                      | Indicates the vector value you want to query, which can be an array or a Base64 string                                            |
   +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | topk                                                                         | Same as the value of **size** generally.                                                                                          |
   +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | :ref:`Table 2 <css_01_0123__en-us_topic_0000001268154489_table172381842595>` | Indicates optional query parameters. You can adjust the vector index parameters to achieve higher query performance or precision. |
   +------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------+

.. _css_01_0123__en-us_topic_0000001268154489_table172381842595:

.. table:: **Table 2** Optional query parameters

   +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Type                                 | Parameter             | Description                                                                                                                                                  |
   +======================================+=======================+==============================================================================================================================================================+
   | Graph index configuration parameters | ef                    | Queue size of the neighboring node during the query. A larger value indicates a higher query precision and slower query speed. The default value is **200**. |
   |                                      |                       |                                                                                                                                                              |
   |                                      |                       | Value range: (0, 100000]                                                                                                                                     |
   +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                                      | max_scan_num          | Maximum number of scanned nodes. A larger value indicates a higher query precision and slower query speed. The default value is **10000**.                   |
   |                                      |                       |                                                                                                                                                              |
   |                                      |                       | Value range: (0, 1000000]                                                                                                                                    |
   +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | IVF index configuration parameters   | nprobe                | Number of center points. A larger value indicates a higher query precision and slower query speed. The default value is **100**.                             |
   |                                      |                       |                                                                                                                                                              |
   |                                      |                       | Value range: (0, 100000]                                                                                                                                     |
   +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

Compound Query
--------------

Vector search can be used together with other Elasticsearch subqueries, such as Boolean query and post-filtering, for compound query.

In the following two examples, top 10 (**topk**) results closest to the query vector are queried first. **filter** retains only the results whose **my_label** field is **red**.

-  Example of a Boolean query

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

-  Example of post-filtering

   .. code-block:: text

      GET my_index/_search
      {
        "size": 10,
        "query": {
          "vector": {
            "my_vector": {
              "vector": [1, 2],
              "topk": 10
            }
          }
        },
        "post_filter": {
          "term": { "my_label": "red" }
        }
      }

ScriptScore Query
-----------------

You can use **script_score** to perform Nearest Neighbor Search (NSS) on vectors. The query syntax is provided below.

The pre-filtering condition can be any query. **script_score** traverses only the pre-filtered results, calculates the vector similarity, and sorts and returns the results. The performance of this query depends on the size of the intermediate result set after the pre-filtering. If the pre-filtering condition is set to **match_all**, brute-force search is performed on all data.

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

.. table:: **Table 3** script_score parameters

   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | Parameter                         | Description                                                                                     |
   +===================================+=================================================================================================+
   | source                            | Script description. Its value is **vector_score** if the vector similarity is used for scoring. |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | lang                              | Script syntax description. Its value is **vector**.                                             |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | field                             | Vector field name                                                                               |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | vector                            | Vector data to be queried                                                                       |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | metric                            | Measurement method, which can be **euclidean**, **inner_product**, **cosine**, and **hamming**. |
   |                                   |                                                                                                 |
   |                                   | Default value: **euclidean**                                                                    |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+

Re-Score Query
--------------

If the **GRAPH_PQ** or **IVF_GRAPH_PQ** index is used, the query results are sorted based on the asymmetric distance calculated by PQ. CSS supports re-scoring and ranking of query results to improve the recall rate.

Assuming that **my_index** is a PQ index, an example of re-scoring the query results is as follows:

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

.. table:: **Table 4** Rescore parameter description

   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | Parameter                         | Description                                                                                     |
   +===================================+=================================================================================================+
   | window_size                       | Vector retrieval returns *topk* search results and ranks the first *window_size* results.       |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | field                             | Vector field name                                                                               |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | vector                            | Vector data to be queried                                                                       |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+
   | metric                            | Measurement method, which can be **euclidean**, **inner_product**, **cosine**, and **hamming**. |
   |                                   |                                                                                                 |
   |                                   | Default value: **euclidean**                                                                    |
   +-----------------------------------+-------------------------------------------------------------------------------------------------+

Painless Syntax Extension
-------------------------

CSS extension supports multiple vector distance calculation functions, which can be directly used in customized painless scripts to build flexible re-score formulas.

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

The following table lists the distance calculation functions supported by the CSS.

+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| Function Signature               | Description                                                                                                                                              |
+==================================+==========================================================================================================================================================+
| euclidean(Float[], DocValues)    | Euclidean distance function                                                                                                                              |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| cosine(Float[], DocValues)       | Cosine similarity function                                                                                                                               |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| innerproduct(Float[], DocValues) | Inner product function                                                                                                                                   |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
| hamming(String, DocValues)       | Hamming distance function Only vectors whose **dim_type** is **binary** are supported. The input query vector must be a Base64-encoded character string. |
+----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
