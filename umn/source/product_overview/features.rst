:original_name: css_04_0003.html

.. _css_04_0003:

Features
========

This topic describes the features that CSS supports. You can check the regions where each feature is available on the console.

Rapid Deployment
----------------

CSS enables you to create Elasticsearch clusters ready to run enterprise workloads in a few simple steps. CSS will automatically install and deploy a search engine based on the cluster type, version, and node specifications you select.

-  Elasticsearch clusters are suited for log analytics, enterprise search, and real-time data visualization, particularly where a robust analytics ecosystem and strong community support are required. For more information, see :ref:`Creating a Cluster <css_01_0270>`.

Enhanced Kernel
---------------

CSS features an enhanced kernel that boosts cluster performance and stability, while optimizing costs across diverse deployment scenarios.

-  Vector search: Unstructured data, such as images, videos, and language corpora, is converted into vectors, which are searched based on similarity using either an exact or approximate nearest neighbors algorithm.
-  Decoupled storage and compute: CSS stores new data (hot data) on SSDs to ensure optimal query performance, and historical data (cold data) in OBS to cut storage costs.
-  Flow control: Flow control policies, such as client request throttling, shard indexing backpressure, and traffic pattern analysis clusters, protect clusters from overload, ensuring proper resource allocation and risk prevention.
-  Large query isolation: Queries that have high memory usage or take too long to complete are suspended or isolated to improve cluster stability and prevent out-of-memory (OOM) exceptions.
-  Enhanced aggregation: CSS enhances aggregation performance in the face of large data volumes by leveraging vectorization and optimized clustering techniques, enabling faster analytics and decision-making in complex situations.
-  Read/write splitting: This feature relies on collaboration between a pair of leader and follower clusters, where the leader exclusively handles write requests, and the follower serves read queries. This separation of workloads enhances the stability, scalability, and high-concurrency processing capabilities of clusters.
-  Switching between hot and cold storage: Data is allocated to nodes of different performance standards based on data temperature (that is, how often data is accessed). The goal is to achieve optimal storage costs and query performance. Typically, high-performance hardware (such as SSDs) is used to store hot data that is frequently accessed, while inexpensive hardware (such as HDDs) is used to store cold data that is infrequently accessed.
-  Index recycle bin: To prevent data loss caused by accidental deletion, CSS provides an index recycle bin. When it is enabled, deleted indexes are temporarily stored in the recycle bin, allowing for recovery before they are permanently removed. This feature improves data reliability and operational security.
-  Enhanced data ingestion: This feature significantly enhances data ingestion performance and reduces write rejections through bulk route optimization, text index acceleration, and word segmentation acceleration.
-  Index monitoring: This feature helps you monitor the index status, statistics, and trends of clusters, allowing you to promptly handle potential risks to ensure cluster reliability.

For more information, see :ref:`CSS Enhancements Over Open-Source Elasticsearch <css_01_0013>` or :ref:`CSS Enhancements Over Open-Source OpenSearch <css_01_0098>`.

Public Network Access
---------------------

In CSS, you can enable public network access for Elasticsearch and OpenSearch clusters that have the security mode enabled and use HTTPS. With public network access enabled, a cluster is automatically assigned a public IP address with dedicated dynamic BGP bandwidth, making it accessible from the Internet via HTTPS.

For more information, see :ref:`Configuring Public Network Access <css_01_0076>` or :ref:`Configuring Public Network Access <css_01_0290>`.

VPC Endpoint
------------

VPC Endpoint enables you to access resources across Virtual Private Clouds (VPCs) using a dedicated gateway, without exposing the network information of servers. When VPC Endpoint is enabled for an Elasticsearch or OpenSearch cluster, a VPC endpoint is automatically allocated to it, through which users will be able to access this cluster.

For more information, see :ref:`Configuring VPC Endpoints <css_01_0082>` or :ref:`Configuring VPC Endpoints <css_01_0291>`.

Dedicated Load Balancers
------------------------

In CSS, you can configure dedicated load balancers for clusters. Compared with shared load balancers, dedicated load balancers provide higher performance and more diverse features. If your Elasticsearch or OpenSearch cluster contains a large number of nodes and stores large quantities of data, you are advised to configure load balancers for it to improve stability.

For more information, see :ref:`Configuring a Dedicated Load Balancer <css_01_0181>` or :ref:`Configuring a Dedicated Load Balancer <css_01_0182>`.

Backup and Restoration
----------------------

In CSS, you can use snapshots to back up and restore the data of Elasticsearch and OpenSearch clusters. By storing a snapshot in an OBS bucket, you save a point-in-time copy of the cluster's data. Later, you can restore this snapshot to the original cluster or another eligible cluster.

There are two ways to create snapshots: automatic and manual.

-  Automatic snapshot creation: Snapshots are automatically created daily or weekly based on a preset time schedule, ensuring ongoing data protection. By configuring an automatic snapshot policy, you reduce manual operations while improving backup reliability and efficiency.
-  Manual snapshot creation: You create snapshots manually for special occasions, for example, prior to a high-risk operation (such as a cluster upgrade). This ensures you can restore data using snapshots in case anything should go wrong. Manual snapshots provide additional flexibility.

This process fetches the backed-up index data, metadata, and shard structure from OBS and reconstruct them in the selected destination cluster, ensuring data consistency. This capability is essential for operations like data rollback, cluster migration, and disaster recovery.

For more information, see :ref:`Backup and Restoration <css_01_0033>` or :ref:`Backup and Restoration <css_01_0297>`.

Flexible Scalability
--------------------

CSS clusters support flexible scaling options, allowing you to dynamically adjust capacities to meet changing demand, ensuring optimal performance and efficiency.

-  Scaling out or up: If a cluster struggles to maintain performance in the face of rapid data growth or sustained high memory usage, you may scale it horizontally by adding more nodes and more node types, or do so vertically by increasing the storage capacity of existing nodes.
-  Scaling in: If a cluster has excess capacity due to off-peak traffic or reduced data volume, you can reduce its nodes to optimize costs.
-  Node specification changes: If the workloads on a cluster's data plane change or the cluster is experiencing performance bottlenecks, you can scale the cluster vertically by changing its node specifications or node storage type.
-  Replacing a specified node: You can use this option to replace failed cluster nodes.
-  Changing the security mode: You can enable or disable the security mode for an existing cluster to accommodate changing security needs.
-  Switching AZs: CSS supports cross-AZ deployment. By switching AZs for a cluster, you can make more resources available to the cluster or improve the cluster's availability.

Upgrade
-------

In CSS, you can upgrade clusters to use feature and performance enhancements or fix known issues.

-  Same-version upgrade: Install kernel patches for a cluster. The cluster is upgraded to the latest image of the current version to fix known issues or optimize performance.
-  Cross-version upgrade: Upgrade the cluster version. The cluster will be upgraded to the latest image of the target version to enhance performance or incorporate older versions.

For more information, see :ref:`Upgrading the Cluster Version <css_01_0186>` or :ref:`Upgrading the Cluster Version <css_01_0263>`.

Custom Word Dictionaries
------------------------

CSS supports custom dictionaries. You can configure custom word dictionaries to support word segmentation. This gives the search engine enhanced performance when searching by keywords. CSS uses the IK and synonym analyzers. The IK analyzer uses a main word dictionary and a stop word dictionary. The synonym analyzer uses a synonym word dictionary. CSS provides four preset word dictionaries: static main word dictionary, static stop word dictionary, extra main word dictionary, and extra stop word dictionary.

For more information, see or .

Log Management
--------------

CSS provides log ingestion, log query, and log backup, enabling you to easily manage and analyze logs to efficiently locate faults, optimize performance, and enhance system security.

-  Log query: On the log management page of the CSS management console, you can query the latest log records by node, log type, and other criteria, so you can quickly locate or diagnose issues.
-  Log backup: Cluster logs are periodically synchronized to OBS buckets. You can download them for in-depth analysis at any time. Custom backup policies (such as backup time and storage path) are supported.
-  Log ingestion (for Elasticsearch and OpenSearch clusters only): Cluster logs are transmitted in real time to the current cluster or another cluster on the same network. (Certain version and network compatibility requirements must be met.) You can use Kibana, OpenSearch Dashboards, or other visualization tools for log search and analytics. You can also set index prefixes and retention periods to flexibly manage the log lifecycle. Logs can be transferred across clusters, facilitating centralized monitoring in a multi-cluster environment.

For more information, see :ref:`Querying Logs <css_01_0077>` or :ref:`Querying Logs <css_01_0321>`.

Intelligent O&M
---------------

CSS supports both scheduled and manual cluster checks, including multiple check items, such as data node disk usage, overall cluster health, and node CPU usage. Through these check items, O&M personnel can identify potential risks in a timely manner and take recommended measures to improve system reliability and availability.

Monitoring and Alerting
-----------------------

Through Cloud Eye, you can monitor the health status of CSS clusters by checking alarms and events generated for them. You can customize alarm thresholds for individual metrics. When such thresholds are reached, alarms will be triggered automatically. CSS can also interconnect with the Simple Message Notification (SMN) service to push alarm notifications to users via text messages or email.
