:original_name: css_04_0010.html

.. _css_04_0010:

Advantages
==========

CSS has the following features and advantages.

Efficient and Ease of Use
-------------------------

You can get insights from terabyte-scale data in milliseconds. In addition, you can use the visualized platform for data display and analysis.

Flexible and Scalable
---------------------

You can request resources as needed and perform capacity expansion online with zero service interruption.

Easy O&M
--------

CSS is a fully-managed, out-of-the-box service. You can start using it with several clicks, instead of managing clusters.

Kernel Enhancement
------------------

-  **Vector search**

   When you search for unstructured data, such as images, videos, and corpuses, the nearest neighbors or approximate nearest neighbors are searched based on feature vectors.

-  **Decoupled storage and compute**

   CSS provides an API for freezing indexes. Hot data stored on SSD can be dumped to OBS to reduce data storage costs and decouple compute from storage.

-  **Flow control**

   CSS can control traffic at the node level. You can configure the blacklist and whitelist, the maximum concurrent HTTPS connections, and the maximum HTTP connections for a node. Each function has an independent control switch.

-  **Large query isolation**

   CSS allows you to separately manage large queries. You can isolate query requests that consume a large amount of memory or take a long period of time.

-  **Index monitoring**

   CSS monitors various metrics of the running status and change trend of cluster indexes to measure service usage and handle potential risks in a timely manner, ensuring that clusters can run stably.

-  **Enhanced monitoring**

   CSS supports enhanced cluster monitoring. It can monitor the P99 latency of cluster search requests and the HTTP status codes of clusters.

High Reliability
----------------

You can choose to trigger snapshots manually or on a periodic basis for backup and restore snapshots to the current or other clusters. Snapshots of a cluster can be restored to another cluster to implement cluster data migration.

-  Automatic backup using snapshots

   CSS provides the backup function. You can enable the automatic backup function on the CSS management console and set the backup period based on the actual requirements.

   Automatic backup is to back up the index data of a cluster. Index backup is implemented by creating cluster snapshots. For backup of the first time, you are advised to back up all index data.

   CSS allows you to store the snapshot data of Elasticsearch instances to OBS, thereby achieving cross-region backup with the cross-region replication function of OBS.

-  Restoring data using snapshots

   If data loss occurs or you want to retrieve data of a certain period, click **Restore** in the **Operation** column in the **Snapshots** area to restore the backup index data to the specified cluster by using existing snapshots.

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

High Availability
-----------------

To prevent data loss and minimize the cluster downtime in case of service interruption, CSS supports cross-AZ cluster deployment. When creating a cluster, you can select two or three AZs in the same region. The system will automatically allocate nodes to these AZs. If an AZ is faulty, the remaining AZs can still run properly, significantly enhancing cluster availability and improving service stability.
