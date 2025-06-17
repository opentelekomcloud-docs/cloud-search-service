:original_name: css_02_0130.html

.. _css_02_0130:

How Do I Clear Elasticsearch Cache in CSS?
==========================================

-  **Clear the fielddata**

   During aggregation and sorting, data are converted to the fielddata structure, which occupies a large amount of memory.

   #. Run the following command on Kibana to query the fielddata cache status:

      .. code-block:: text

         GET /_cat/nodes?v&h=name,fielddataMemory

   #. If the memory usage of **fielddata** is too high, you can run the following command to clear the **fielddata cache** of a specified index or all indexes:

      .. code-block:: text

         POST /test/_cache/clear?fielddata=true

      In the preceding command, *test* indicates the name of the index whose fielddata occupies a large amount of memory.

      .. code-block:: text

         POST /_cache/clear?fielddata=true

-  **Clear segments**

   The FST structure of each segment is loaded to the memory and will not be cleared. If the number of index segments is too large, the memory usage will be high. You are advised to periodically clear the segments.

   #. Run the following command on Kibana to check the number of segments and their memory usage on each node:

      .. code-block:: text

         GET /_cat/nodes?v&h=segments.count,segments.memory&s=segments.memory:desc

   #. If the memory usage of segments is too high, you can delete or disable unnecessary indexes, or periodically combine indexes that are not updated.

-  **Clear the cache**

   Run the following command on Kibana to clear the cache:

   .. code-block:: text

      POST /_cache/clear
