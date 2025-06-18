:original_name: css_02_0102.html

.. _css_02_0102:

How Do I Set search.max_buckets for an Elasticsearch Cluster of CSS?
====================================================================

Function
--------

By default, CSS allows a maximum of 10,000 buckets to be returned during aggregation. If more than 10,000 buckets need to be returned, you can increase the value of **search.max_buckets**. Note that increasing the value of **search.max_buckets** also increases the cluster load and memory usage. Exercise caution when performing this operation.

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
