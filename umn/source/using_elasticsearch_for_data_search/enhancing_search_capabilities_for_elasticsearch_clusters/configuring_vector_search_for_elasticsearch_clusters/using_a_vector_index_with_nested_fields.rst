:original_name: css_01_0401.html

.. _css_01_0401:

Using a Vector Index with Nested Fields
=======================================

Nested fields allow multiple vectorized records to be stored in a single document. For example, in an RAG scenario, documents usually need to be segmented by paragraph or by a fixed length, and then vectorized into multiple semantic vectors. By means of nested fields, these vectors can be written into a same Elasticsearch document. For a document that contains multiple vector records, if the query vector matches any of them, the document is returned.

Constraints
-----------

Only Elasticsearch 7.10.2 clusters support this feature.

Creating a Vector Index
-----------------------

Create a vector index with nested fields. The index contains an **id** field whose type is **keyword**, and an **embedding** field whose type is **nested**. The embedding field contains two subfields: **chunk** and **emb**. The **chunk** subfield is of the **keyword** type, and the **emb** subfield is of the **vector** type.

.. code-block:: text

   PUT my_index
   {
     "settings": {
       "index.vector": true
     },
     "mappings": {
       "properties": {
         "id": {
           "type": "keyword"
         },
         "embedding": {
           "type": "nested",
           "properties": {
             "chunk": {
               "type": "keyword"
             },
             "emb": {
               "type": "vector",
               "dimension": 2,
               "indexing": true,
               "algorithm": "GRAPH",
               "metric": "euclidean"
             }
           }
         }
       }
     }
   }

Importing Vector Data
---------------------

Use the bulk operation to write data in arrays. Each document contains two vector records.

.. code-block:: text

   POST my_index/_bulk
   {"index":{}}
   {"id": 1, "embedding": [{"chunk":1,"emb": [1, 1]}, {"chunk":2,"emb": [2, 2]}]}
   {"index":{}}
   {"id": 2, "embedding": [{"chunk":1,"emb": [2, 2]}, {"chunk":2,"emb": [3, 3]}]}
   {"index":{}}
   {"id": 3, "embedding": [{"chunk":1,"emb": [3, 3]}, {"chunk":2,"emb": [4, 4]}]}

Vector Search
-------------

The nested query is required for nested fields. To perform such a query, you need to set the path parameter to specify the nested path, and set **score_mode** to **max**, indicating the maximum similarity between all vectors in the document and the query vector.

-  Standard query

   Query the top 10 documents that are most similar to vector [1, 1].

   .. code-block:: text

      GET my_index/_search
      {
        "_source": {"excludes": ["embedding"]},
        "query": {
          "nested": {
            "path": "embedding",
            "score_mode": "max",
            "query": {
              "vector": {
                "embedding.emb": {
                  "vector": [1, 1],
                  "topk": 10
                }
              }
            }
          }
        }
      }

   An example of the query result:

   .. code-block::

      {
        "took" : 2,
        "timed_out" : false,
        "_shards" : {
          "total" : 1,
          "successful" : 1,
          "skipped" : 0,
          "failed" : 0
        },
        "hits" : {
          "total" : {
            "value" : 3,
            "relation" : "eq"
          },
          "max_score" : 1.0,
          "hits" : [
            {
              "_index" : "my_index",
              "_type" : "_doc",
              "_id" : "Hc4Vc5QBSxCnghau22AE",
              "_score" : 1.0,
              "_source" : {
                "id" : 1
              }
            },
            {
              "_index" : "my_index",
              "_type" : "_doc",
              "_id" : "Hs4Vc5QBSxCnghau22AE",
              "_score" : 0.33333334,
              "_source" : {
                "id" : 2
              }
            },
            {
              "_index" : "my_index",
              "_type" : "_doc",
              "_id" : "H84Vc5QBSxCnghau22AE",
              "_score" : 0.11111111,
              "_source" : {
                "id" : 3
              }
            }
          ]
        }
      }

-  Pre-filtering query

   First retrieve documents whose ID is ["2", "3"], and then return the top 10 documents that are most similar to the query vector [1, 1].

   .. code-block:: text

      GET my_index/_search
      {
        "query": {
          "nested": {
            "path": "embedding",
            "score_mode": "max",
            "query": {
              "vector": {
                "embedding.emb": {
                  "vector": [1, 1],
                  "topk": 10,
                  "filter": {
                    "terms": {"id": ["2", "3"]}
                  }
                }
              }
            }
          }
        }
      }

   An example of the query result:

   .. code-block::

      {
        "took" : 2,
        "timed_out" : false,
        "_shards" : {
          "total" : 1,
          "successful" : 1,
          "skipped" : 0,
          "failed" : 0
        },
        "hits" : {
          "total" : {
            "value" : 2,
            "relation" : "eq"
          },
          "max_score" : 0.33333334,
          "hits" : [
            {
              "_index" : "my_index",
              "_type" : "_doc",
              "_id" : "Hs4Vc5QBSxCnghau22AE",
              "_score" : 0.33333334,
              "_source" : {
                "id" : 2
              }
            },
            {
              "_index" : "my_index",
              "_type" : "_doc",
              "_id" : "H84Vc5QBSxCnghau22AE",
              "_score" : 0.11111111,
              "_source" : {
                "id" : 3
              }
            }
          ]
        }
      }
