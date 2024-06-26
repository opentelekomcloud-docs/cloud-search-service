:original_name: en-us_topic_0000001476977554.html

.. _en-us_topic_0000001476977554:

What Are the Impacts If an Elasticsearch Cluster Has Too Many Shards?
=====================================================================

#. A large number of shards in a cluster slows down shard creation.
#. If automatic index creation is enabled, slow index creation may cause a large number of write requests to be stacked in the memory or result in a cluster break down.
#. If there are too many shards and you cannot properly monitor workloads, the number of records in a single shard may exceed the threshold, and write requests may be denied.
