:original_name: en-us_topic_0000001528097317.html

.. _en-us_topic_0000001528097317:

How Do I Clear the Cache of a CSS Cluster?
==========================================

-  **Clear the fielddata**

   During aggregation and sorting, data are converted to the fielddata structure, which occupies a large amount of memory.

   #. Run the following commands on Kibana to check the memory occupied by index fielddata:

      .. code-block:: text

         DELETE /_search/scroll
         {
         "scroll_id" :
         "DXF1ZXJ5QW5kRmV0Y2gBAAAAAAAAAD4WYm9laVYtZndUQlNsdDcwakFMNjU1QQ=="
         }

   #. If the memory usage of fielddata is too high, you can run the following command to clear fielddata:

      .. code-block:: text

         POST /test/_cache/clear?fielddata=true

   In the preceding command, *test* indicates the name of the index whose fielddata occupies a large amount of memory.

-  **Clear segments**

   The FST structure of each segment is loaded to the memory and will not be cleared. If the number of index segments is too large, the memory usage will be high. You are advised to periodically clear the segments.

   #. Run the following command on Kibana to check the number of segments and their memory usage on each node:

      .. code-block:: text

         GET /_cat/nodes?v&h=segments.count,segments.memory&s=segments.memory:desc

   #. If the memory usage of segments is too high, you can delete or disable unnecessary indexes, or periodically combine indexes that are not updated.

-  **Clear the cache**

   Run the following command on Kibana to clear the cache:

   .. code-block:: text

      POST _cache/clear
