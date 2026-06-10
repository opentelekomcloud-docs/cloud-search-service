:original_name: css_02_0091.html

.. _css_02_0091:

Why Does Data Volume Differ After Migration?
============================================

After migrating data using tools like Logstash, it's normal for the data volume in the source and destination clusters to differ. We recommend comparing document counts first — differences in volumes do not affect data integrity.

This difference may be attributed to the following factors:

-  Elasticsearch storage mechanism

   CSS Elasticsearch uses a shard- and segment-based storage architecture with dynamic management. Each index is divided into multiple shards, and each shard contains multiple segments. During migration, write operations cause the destination cluster to regenerate its segment and shard structures, which can lead to changed data volumes.

-  Data bloat during data rewriting

   When migrating in data rewriting mode, the destination cluster rebuilds its storage structure based on the current index configuration and load. Newly generated segments may occupy more storage than those in the original cluster due to differences in parameters such as compression policies and encoding methods. This is especially noticeable in scenarios involving both hot and cold data.

-  Index configuration differences

   Index configurations, including the number of replicas, sharding policies, and compression settings, directly affect the final data volumes. For example, if the destination cluster uses a different compression algorithm than the source, data volumes may change in non-linear ways.

To confirm data integrity after migration, compare the document counts rather than data volumes. Document count is a reliable indicator of data consistency.
