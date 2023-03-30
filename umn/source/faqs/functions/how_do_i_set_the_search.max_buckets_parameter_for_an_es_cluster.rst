:original_name: css_02_0102.html

.. _css_02_0102:

How Do I Set the search.max_buckets Parameter for an ES Cluster?
================================================================

Function
--------

If the query results on shards exceed the upper limit of records that can be returned (default value: **10000**), you need to increase the limit by changing the value of **search.max_buckets**.

Solution
--------

Run the following command on the **Dev Tools** page of Kibana:

.. code-block:: text

   PUT _cluster/settings
   {
       "persistent": {
           "search.max_buckets": 20000
       }
   }
