:original_name: css_04_0010.html

.. _css_04_0010:

Advantages
==========

CSS offers a powerful, full-managed enterprise search service. This topic introduces its key advantages.

Efficient and Easy to Use
-------------------------

Gain insights from terabytes of data in milliseconds, and use an intuitive visualization platform for data display and analysis.

Open-source Compatibility
-------------------------

-  Freely use native Elasticsearch and OpenSearch APIs and other software in the ecosystem, such as Logstash, Beats, and Kibana.
-  A few simple configurations allow you to smoothly connect to multiple data sources, such as FTP, OBS, HBase, and Kafka. No extra coding is required.

High Security
-------------

CSS uses network isolation in addition to various host and data security measures.

-  Network isolation

   The network is divided into two planes, service plane and management plane. The two planes are deployed and isolated physically to ensure the security of the service and management networks.

   -  Service plane: refers to the network plane of the cluster. It provides service channels for users and delivers data definition, index, and search capabilities.
   -  Management plane: This is mainly the management console, where you manage CSS.
   -  VPC security groups or isolated networks ensure the security of hosts.

-  Access control

   -  Using the network access control list (ACL), you can permit or deny the network traffic entering and exiting the subnets.
   -  Internal security infrastructure (including the network firewall, intrusion detection system, and protection system) can monitor all network traffic that enters or exits the VPC through the IPsec VPN.
   -  User authentication and index-level authentication are supported. CSS also supports interconnection with third-party user management systems.

-  Data security

   -  In CSS, a multi-replica mechanism is used to ensure data security.
   -  Communication between the client and server can be encrypted using SSL.

-  Operation audit

   Cloud Trace Service (CTS) can be used to perform auditing on key logs and operations.

Enhanced Kernel
---------------

CSS introduces several kernel enhancement features, such as ingestion performance enhancement, decoupled storage and compute, and read/write splitting.

-  Log ingestion performance is improved by 50%.
-  Aggregation acceleration results in 200% higher performance in statistical analysis by sorting fields.
-  With decoupled storage and compute, the cost of cold data storage is reduced by 80%.
-  Zstandard (ZSTD) compression reduces the storage footprint by 20%.
-  Stability is enhanced with heartbeat isolation, flow control, authentication optimization, million-shard optimization, and metadata optimization.

Intelligent O&M
---------------

-  CSS is a fully-managed service that can be made instantly available and supports one-click operations.
-  The intelligent O&M module scans clusters for potential risks, provides mitigation suggestions, and triggers alerts when necessary.

Enhanced Semantic Search
------------------------

-  A proprietary vector search engine delivers remarkable search throughput and low latency, creating a solid foundation for vector databases.
-  Semantic search relies on the collaboration between an AI search model and Elasticsearch/OpenSearch.
-  A well-designed text embeddings model enhances semantic search performance.
