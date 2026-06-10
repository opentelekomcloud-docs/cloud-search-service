:original_name: css_01_0264.html

.. _css_01_0264:

Implementing Nested Vector Search
=================================

When processing long documents, such as technical manuals or legal provisions, documents are often partitioned into semantic chunks based on paragraph boundaries or fixed token lengths, with vector embeddings generated for each chunk. Traditional flat storage structures make it difficult to maintain the mapping between document-level metadata (such as IDs and titles) and per-chunk vectors, so it can be difficult to accurately locate the chunk that triggered a match during retrieval. To address this, the CSS vector database supports vector search with nested fields. This allows multiple sub-documents to be nested within a parent document. At query time, the search engine traversed all nested vectors in a single request, and the most relevant chunk can be retrieved based on similarity score. This greatly simplifies architectural complexity for long-text retrieval.

How the Feature Works
---------------------

In standard Elasticsearch and OpenSearch configurations, object arrays are flattened into a single multi-value field at the storage layer. This causes the association between different sub-fields to get lost. By using nested fields, each nested object is stored as a separate, hidden sub-document linked to a single parent document, ensuring that each chunk in a nested object remains associated with its corresponding vector during retrieval.

When you perform vector search on a nested field, the following process happens:

#. Sub-document scanning: Traverses the vectors of all sub-documents within each parent document.
#. Partial scoring: Calculate the similarity score between each sub-vector and the query vector.
#. Score aggregation: Determine the final relevance score of each parent document based on the defined score_mode. Typically, score_mode is set to **max**, indicating that a document should get a high score if any of its chunks is most relevant to the query.

Constraints
-----------

-  Only Elasticsearch 7.10.2 and OpenSearch 2.19.0 clusters support vector search with nested fields.
-  Nested fields increase the total number of documents. For a large-scale dataset, you should carefully evaluate this operational overhead.
-  Rescore query cannot be implemented for nested fields through the rescore statement. Only the query.vector statement (see :ref:`Standard Vector Query <en-us_topic_0000002555376597__en-us_topic_0000001268154489_section344710865418>`) can be used to do that.

Creating a Vector Index with Nested Fields
------------------------------------------

Run the following command to create a vector index with nested fields. The index contains an **id** field whose type is **keyword**, and an **embedding** field whose type is **nested**. The embedding field contains two subfields: **chunk** and **emb**. The **chunk** subfield is of the **keyword** type, and the **emb** subfield is of the **vector** type.

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
           "type": "nested",        // Declares the nested type.
           "properties": {
             "chunk": {
               "type": "keyword"
             },
             "emb": {               // Vector embedding in the subfield
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

Run the following command to bulk-import parent documents along with their corresponding chunk embeddings as nested objects. Each parent document contains two vector embeddings.

.. code-block:: text

   POST my_index/_bulk
   {"index":{}}
   {"id": 1, "embedding": [{"chunk":1,"emb": [1, 1]}, {"chunk":2,"emb": [2, 2]}]}
   {"index":{}}
   {"id": 2, "embedding": [{"chunk":1,"emb": [2, 2]}, {"chunk":2,"emb": [3, 3]}]}
   {"index":{}}
   {"id": 3, "embedding": [{"chunk":1,"emb": [3, 3]}, {"chunk":2,"emb": [4, 4]}]}

Performing a Nested Vector Search
---------------------------------

Retrieve and rank parent documents based on the similarity scores of their most relevant internal chunks. Because the data is stored in a nested structure, you must use a nested query to retrieve nested fields. To perform such a query, you need to set the path parameter to specify the nested path, and set **score_mode** to **max**, indicating the maximum similarity between all vectors in the document and the query vector.

-  Standard query

   Query the top 10 documents that are most similar to vector [1, 1].

   .. code-block:: text

      GET my_index/_search
      {
        "_source": {"excludes": ["embedding"]}, // Returns only the parent document ID, and the complex vector array remains hidden.
        "query": {
          "nested": {
            "path": "embedding",                // The nested field path must be specified.
            "score_mode": "max",                // Policy for consolidating the scores of sub-documents for the parent document: Use the score of the most relevant chunk.
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
            "path": "embedding",                // The nested field path must be specified.
            "score_mode": "max",                // Policy for consolidating the scores of sub-documents for the parent document: Use the score of the most relevant chunk.
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
        "took" : 3,
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
              "_id" : "3t0ZypcB-Tff59gMTZO2",
              "_score" : 0.33333334,
              "_source" : {
                "id" : 2,
                "embedding" : [
                  {
                    "chunk" : 1,
                    "emb" : [
                      2,
                      2
                    ]
                  },
                  {
                    "chunk" : 2,
                    "emb" : [
                      3,
                      3
                    ]
                  }
                ]
              }
            },
            {
              "_index" : "my_index",
              "_type" : "_doc",
              "_id" : "390ZypcB-Tff59gMTZO2",
              "_score" : 0.11111111,
              "_source" : {
                "id" : 3,
                "embedding" : [
                  {
                    "chunk" : 1,
                    "emb" : [
                      3,
                      3
                    ]
                  },
                  {
                    "chunk" : 2,
                    "emb" : [
                      4,
                      4
                    ]
                  }
                ]
              }
            }
          ]
        }
      }
