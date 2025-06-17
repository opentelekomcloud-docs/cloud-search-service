:original_name: css_02_0124.html

.. _css_02_0124:

What Are the Impacts If an Elasticsearch Cluster of CSS Has Too Many Shards?
============================================================================

#. A large number of shards in a cluster slows down shard creation.
#. If automatic index creation is enabled, slow index creation may cause a large number of write requests to be stacked in the memory or result in a cluster breakdown.
#. If there are too many shards and you cannot properly monitor workloads, the number of records in a single shard may exceed the threshold, and write requests may be denied.
