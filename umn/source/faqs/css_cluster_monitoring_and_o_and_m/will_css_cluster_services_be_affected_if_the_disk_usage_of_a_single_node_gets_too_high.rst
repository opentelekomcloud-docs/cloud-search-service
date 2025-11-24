:original_name: css_02_0135.html

.. _css_02_0135:

Will CSS Cluster Services Be Affected If the Disk Usage of a Single Node Gets Too High?
=======================================================================================

Symptom
-------

According to the cluster monitoring information, the disk usage of some individual nodes of an Elasticsearch cluster exceeds 80%. Does it impact cluster performance?

Impact on Services
------------------

-  When the disk usage of a node exceeds 85%, disk space cannot be allocated to new replicas, but can still be allocated to new primary shards. This ensures service continuity, but it impacts the high availability of the Elasticsearch cluster.
-  When the disk usage of a node exceeds 90%, a shard migration is automatically triggered to reallocate shards on this node to other data nodes with lower disk usage. During this process, disk space cannot be allocated to new shards. Shard migration and reallocation may increase query delay or temporarily interrupt services, impacting service continuity.
-  When the disk usage of a node exceeds 95%, the **read_only_allow_delete** attribute is enabled in its indexes. In this case, indexes on this node can only be read or deleted but data cannot be written in.

If per-node disk usage is too high, you can add more nodes or expand the capacity of existing nodes. For details, see :ref:`Scaling Out/Up an Elasticsearch Cluster <css_01_0151>`. After new nodes are added, index shards automatically re-allocate to balance the load. You can launch Cerebro to check the shard allocation process. You can also modify **indices.recovery.max_bytes_per_sec** and **cluster.routing.allocation.cluster_concurrent_rebalance** to speed up this process.
