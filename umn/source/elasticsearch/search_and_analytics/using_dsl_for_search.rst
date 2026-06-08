:original_name: css_01_0007.html

.. _css_01_0007:

Using DSL for Search
====================

When you need to interact with an Elasticsearch cluster to perform complex full-text search or data analysis, the domain-specific language (DSL) is your best choice. As a JSON-based query language native to Elasticsearch, DSL enables you to express sophisticated query logic with clarity and precision while giving you fine-grained control over how your queries are executed.

What Is DSL?
------------

The Elasticsearch Query DSL is a JSON-based query language that defines the structure and semantics of search and data retrieval requests. It contains two contexts:

-  Query context: In the query context, a query clause answers the question "How well does this document match this query clause?" Besides deciding whether or not the document matches, the query clause also calculates a relevance score in the **\_score** metadata field. One example of such query clauses: match.
-  In a filter context, a query clause answers the question "Does this document match this query clause?" The answer is a simple Yes or No. No scores are calculated, but frequently used filters will be cached automatically by Elasticsearch, to speed up performance. Examples of such queries: term and range.

DSL queries are usually executed in Dev Tools of Kibana. Both the request body and returned information are in JSON.

This topic lists some of the most commonly used DSL query clauses. For more, see `Query DSL <https://www.elastic.co/guide/en/elasticsearch/reference/7.10/query-dsl.html>`__.

Basic Query: match_all
----------------------

Use **match_all** to match all documents in the index. It is equivalent to **SELECT \* FROM table** in SQL. Use it when you want to search all documents.

For example, run the following command to match all documents in the **test** index:

.. code-block:: text

   GET /test/_search
   {
     "query": {
       "match_all": {}
     }
   }

Compound Queries: Combining Multiple Query Clauses
--------------------------------------------------

Use a bool query with clauses such as must and filter to construct compound query conditions. This is similar to the **where** clause in SQL. Use this query when you need to apply multiple conditions to filter documents.

For example, run the following command to retrieve all documents whose status is **published** and whose publish_date is later than **2015-01-01** (filter condition), and whose title or content contains **Search** (search condition).

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

The differences between **must** and **filter** are as follows:

-  **must**: Specifies conditions that documents must meet. These conditions affect the relevance score of documents, and documents with higher scores are ranked higher in the results.
-  **filter**: Also specifies conditions that documents must meet, but these conditions do not affect the relevance score. **filter** is typically more efficient than **must**, making it better suited for filtering structured data.

For conditions that do not require relevance scoring (such as status, time range, and category), use **filter** to improve query performance.

Aggregations
------------

The **aggs (such as the terms aggregation)** structure is used to perform aggregation queries. It is similar to the **Group by** clause in SQL. Use it when you want to group documents to calculate metrics.

For example, run the following command to count how many times different titles appear in the **test** index:

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

The reason for using **title.keyword** is as follows:

-  Text fields are used for full-text retrieval (they undergo tokenization). For example, "Hello World" will be split into "hello" and "world". If you attempt to aggregate on a text field directly, an error (Fielddata is disabled) will be return. This is because it is an extremely memory-intensive operation.
-  Keyword fields are used for exact match and aggregations. It keeps "Hello World" as a single value.

By default, the cluster automatically creates multi-fields for strings. That means **title** is used for search, and **title.keyword** for aggregations.
