:original_name: css_01_0399.html

.. _css_01_0399:

Using DSL to Search for Data in Elasticsearch
=============================================

DSL is the specified query language for Elasticsearch. It is the best language for interaction between Elasticsearch clusters and clients. Elasticsearch DSL is a JSON-based language. Other languages, such as SQL, are translated into Elasticsearch DSL before they can be used for interacting with Elasticsearch clusters.

This topic lists some of the most commonly used Elasticsearch DSL query statements. For more, see `Query DSL <https://www.elastic.co/guide/en/elasticsearch/reference/7.10/query-dsl.html>`__.

DSL Usage Example
-----------------

Compile the request content in JSON format on Dev Tools of Kibana and execute the search request.

For example, run the following command to retrieve all documents in the **test** index:

.. code-block:: text

   GET /test/_search
   {
     "query": {
       "match_all": {}
     }
   }

The search result is also in JSON format.

Common DSL Query Statements
---------------------------

-  Sets the query filters, which is equivalent to **where** in the SQL language.

   In the command below, there is no index filter in front of **\_search**, so all indexes are queried. A bool query allows you to combine multiple search queries with boolean conditions. **filter** forcibly filters documents whose **status** field is **published** and **publish_date** is later than **2015-01-01**. **must** specifies that both **title** and **content** must include **Search**.

   .. note::

      The difference between **must** and **filter** is that **filter** is equivalent to **where** in SQL but its results are not used for scoring. The **must** field is also a mandatory filter criteria, but the matching documents are scored based on relevance. The most relevant documents are displayed at the top.

   .. code-block:: text

      GET /_search
      {
        "query": {
          "bool": {
            "must": [
              {
                "match": {
                  "title": "Search"
                }
              },
              {
                "match": {
                  "content": "search"
                }
              }
            ],
            "filter": [
              {
                "term": {
                  "status": "published"
                }
              },
              {
                "range": {
                  "publish_date": {
                    "gte": "2015-01-01"
                  }
                }
              }
            ]
          }
        }
      }

-  **Aggregations** are similar to **Group by** in SQL.

   An aggregation summarizes your data as metrics, statistics, or other analytics. In the example below, the results are aggregated based on the title field in the **test** index. If **title** is of the text (including keyword) type, use **title.keyword** for aggregation. By default, a cluster cannot directly aggregate data of the text type. **titles** is only an example name of the aggregation. You can name the aggregation **titleaggs** instead.

   .. code-block:: text

      GET /test/_search
      {
        "aggs": {
          "titles": {
            "terms": {
              "field": "title.keyword"
            }
          }
        }
      }

   The example above for query aggregation includes all documents in the **test** index. That is, **match_all** is used. You can set search criteria to narrow the scope of the aggregation to specific documents.
