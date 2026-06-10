:original_name: css_02_0126.html

.. _css_02_0126:

Why Does Disk Usage Increase After Running delete_by_query to Delete Data in an Elasticsearch Cluster?
======================================================================================================

Running the **delete_by_query** command does not immediately delete data. Instead, it adds a deletion mark to the target data. While marked data is filtered out from search results, it still occupies disk space.

The occupied disk space is not released until the next segment merge occurs.

Querying data with the deletion mark occupies disk space. This is why disk usage increases.
