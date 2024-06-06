:original_name: en-us_topic_0000001814230837.html

.. _en-us_topic_0000001814230837:

Using PV_GRAPH to Search for Vector Indexes
===========================================

PV_GRAPH deeply optimizes the HNSW algorithm and supports the vector and scalar joint filtering. When the vector and scalar joint filtering is used, the result filling rate and query performance can be greatly improved compared with post-filtering and Boolean query.

Prerequisites
-------------

An Elasticsearch cluster of version 7.10.2 has been created by referring to :ref:`Cluster Planning for Vector Retrieval <en-us_topic_0000001477419716>`.

Creating an Index
-----------------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. Click **Dev Tools** in the navigation tree on the left and run the following command to create a vector index.

   Create an index named **my_index** that contains a vector field **my_vector** and two sub-fields **country** and **category**.

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
              "algorithm": "PV_GRAPH",
              "metric": "euclidean",
              "sub_fields": ["country", "category"]
            }
          }
        }
      }

   For details about the parameters for creating an index, see :ref:`Table 1 <en-us_topic_0000001528299557__en-us_topic_0000001309709789_table189861827103114>`.

   .. note::

      The **metric** parameter of the PV_GRAPH index algorithm can only be set to **euclidean** or **inner_product**.

Importing the Vector and Scalar Data
------------------------------------

When algorithm is set to **PV_GRPAH** and **sub_fields** is specified, the following data writing grammars are supported. The **sub_fields** parameter supports only the **keyword** type and you can specify multiple values for it.

.. code-block::

   # Write a single data record.
   POST my_index/_doc
   {
     "my_vector": {
       "data": [1.0, 1.0],
       "country": "cn",
       "category": ["1", "2"]
     }
   }

   # Write multiple data records in batches.
   POST my_index/_bulk
   {"index": {}}
   {"my_vector": {"data": [1.0, 2.0], "country": "cn", "category": "1"}}
   {"index": {}}
   {"my_vector": {"data": [2.0, 2.0], "country": "cn", "category": ["1", "2"]}}
   {"index": {}}
   {"my_vector": {"data": [2.0, 3.0], "country": "eu", "category": "2"}}

Querying a Vector
-----------------

Based on the existing Elasticsearch APIs, the **filter** parameter is added to **vector** to support vector and scalar joint filtering. The values of **sub_fields** can be used for scalar filtering. Currently, the JSON format is supported. The **should**, **must**, **must_not**, **term**, and **terms** queries are supported. The syntax is the same as that of Elasticsearch query. The restrictions are as follows:

Currently, up to four layers are supported for filtering nesting.

-  **must_not** cannot be nested or contain nest layers.
-  The first layer can contain only one query keyword (such as **must**).

The fields defined in **sub_fields** during index creation are the scalar fields used in the joint filtering and take effect only when the **algorithm** is set to **PV_GRAPH**. If the specified filtering field does not exist, the filtering request becomes invalid and the query is processed with no filtering conditions.

.. code-block::

   # Example of single-label and single-value matching query
   GET my_index/_search
   {
     "query": {
       "vector": {
         "my_vector": {
           "vector": [1.0, 1.0],
           "topk": 10,
           "filter": {
             "term": { "country": "cn" }
           }
         }
       }
     }
   }

   # Example of single-label and multi-value matching query
   GET my_index/_search
   {
     "query": {
       "vector": {
         "my_vector": {
           "vector": [1.0, 1.0],
           "topk": 10,
           "filter": {
             "terms": { "country": ["cn", "eu"] }
           }
         }
       }
     }
   }

   # Example of multi-label matching query
   GET my_index/_search
   {
     "query": {
       "vector": {
         "my_vector": {
           "vector": [1.0, 1.0],
           "topk": 10,
           "filter": {
             "must": [
               {
                 "term": {"country": "cn"}
               },
               {
                 "terms": {"category": ["1", "2"]}
               }
             ]
           }
         }
       }
     }
   }

   # Example of must_not matching query
   GET my_index/_search
   {
     "query": {
       "vector": {
         "my_vector": {
           "vector": [1.0, 1.0],
           "topk": 10,
           "filter": {
             "must_not": [
               {
                 "term": {"country": "eu"}
               }
             ]
           }
         }
       }
     }
   }

For details about vector query parameters, see :ref:`Table 1 <en-us_topic_0000001477899192__en-us_topic_0000001268154489_table112016411577>`.
