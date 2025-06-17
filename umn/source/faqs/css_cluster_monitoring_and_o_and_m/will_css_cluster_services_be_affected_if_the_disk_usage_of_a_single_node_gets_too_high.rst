:original_name: css_02_0135.html

.. _css_02_0135:

Will CSS Cluster Services Be Affected If the Disk Usage of a Single Node Gets Too High?
=======================================================================================

Symptom
-------

According to the cluster monitoring information, the disk usage of an Elasticsearch cluster exceeds 80%. Does it affect cluster performance?

Impact on Services
------------------

-  When the disk usage of a node exceeds 85%, disk space cannot be allocated to new replicas, but can still be allocated to new primary shards. This ensures service continuity, but it impacts the high availability of the Elasticsearch cluster.
-  When the disk usage of a node exceeds 90%, a shard migration mechanism is automatically triggered to reallocate shards on this node to other data nodes with lower disk usage. During this process, disk space cannot be allocated to new shards. Shard migration and reallocation may increase query delay or temporarily interrupt services, impacting service continuity.
-  When the disk usage of a node exceeds 95%, the **read_only_allow_delete** attribute will be enabled in its indexes. In this case, indexes on this node can only be read or deleted but data cannot be written in.

If per-node resource usage is too high, you can add more nodes or expand the capacity of existing nodes. For details, see :ref:`Scaling Out an Elasticsearch Cluster <css_01_0151>`. Indexes will not be allocated to new nodes immediately. You can open the Cerebro file to check index allocation to nodes. You can also change the values of **indices.recovery.max_bytes_per_sec** and **cluster.routing.allocation.cluster_concurrent_rebalance** to speed up index allocation.
