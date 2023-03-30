:original_name: css_02_0096.html

.. _css_02_0096:

How Do I Configure the Threshold for CSS Slow Query Logs?
=========================================================

The slow query log settings of CSS are the same as those of Elasticsearch. You can configure slow query logs via the \_settings API. For example, you can run the following command in Kibana to set the index level:

.. code-block:: text

   PUT /my_index/_settings
   {
       "index.search.slowlog.threshold.query.warn": "10s",
       "index.search.slowlog.threshold.fetch.debug": "500ms",
       "index.indexing.slowlog.threshold.index.info": "5s"
   }

-  If a query takes longer than 10 seconds, a WARN log will be generated.
-  If retrieval takes longer than 500 milliseconds, a DEBUG log will be generated.
-  If an index takes longer than 5 seconds, an INFO log will be generated.

For details, visit the official website: https://www.elastic.co/guide/cn/elasticsearch/guide/current/logging.html
