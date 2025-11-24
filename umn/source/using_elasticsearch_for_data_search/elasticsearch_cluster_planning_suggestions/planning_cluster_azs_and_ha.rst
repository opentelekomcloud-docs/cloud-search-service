:original_name: css_01_0001.html

.. _css_01_0001:

Planning Cluster AZs and HA
===========================

This topic describes how to improve cluster availability by deploying a cluster across multiple AZs, including the rules for distributing cluster nodes among AZs, the recommended number of replicas, and policies for handling AZ failures.

An availability zone (AZ) is a physical region where resources use independent power supplies and networks. AZs in the same region can communicate with each other through internal networks but are physically isolated.

Multi-AZ deployment is a high availability feature provided by CSS. Deploying a cluster across two or three AZs located in the same region can help prevent data loss and lower the possibility of service outages.

.. _en-us_topic_0000002316900222__section14999164703320:

Suggestions on Multi-AZ Deployment
----------------------------------

If you select multi-AZ deployment when creating a cluster, CSS automatically enables cross-AZ HA to ensure that cluster nodes will be evenly distributed across the selected AZs (the difference between the number of nodes in each AZ cannot exceed 1).

You are advised to select three AZs, instead of two AZs, for multi-AZ deployment. If only two AZs are selected and one AZ becomes faulty, the cluster may not be able to elect a master node. As a result, the cluster may become unavailable.

Node Distribution Rules
-----------------------

When a multi-AZ cluster is created, nodes of all types are evenly distributed across different AZs. A maximum of three AZs can be used. :ref:`Table 1 <en-us_topic_0000002316900222__en-us_topic_0000002287671248_table539520458522>` shows the node distribution when the number of AZs varies.

.. warning::

   -  When creating a multi-AZ cluster, ensure that the number of selected nodes of any type is greater than or equal to the number of AZs. Otherwise, multi-AZ cluster deployment will fail.
   -  If the number of data nodes or cold data nodes in a cluster is not divisible by the number of AZs, data in the cluster may be unevenly distributed, affecting data query or write performance.

.. _en-us_topic_0000002316900222__en-us_topic_0000002287671248_table539520458522:

.. table:: **Table 1** Node distribution when the numbers of nodes and AZs vary

   ============= ========= ============= === ============= === ===
   Node Quantity Single AZ Two AZs           Three AZs
   \             AZ1       AZ1           AZ2 AZ1           AZ2 AZ3
   1             1         Not supported     Not supported
   2             2         1             1   Not supported
   3             3         2             1   1             1   1
   4             4         2             2   2             1   1
   ...           ...       ...           ... ...           ... ...
   ============= ========= ============= === ============= === ===

Replica Configuration Suggestions
---------------------------------

For a multi-AZ cluster, configure the number of index replicas in a manner that can better capitalize on the high availability that comes with such as deployment.

-  With a dual-AZ deployment, if one AZ becomes unavailable, the other AZ continues to provide services. In this case, configure at least one replica. If higher query performance is desired, you can increase the number of replicas.
-  In the case of a three-AZ deployment, if one AZ becomes unavailable, the other AZs can continue to provide services. In this case, also configure at least one replica. To enhance the cluster's query performance, increase the number of replicas.

For Elasticsearch and OpenSearch clusters, the default number of index replicas is 1. To enable more replicas, modify settings. The following are two examples.

-  Adjust the number of replicas for an existing index:

   **curl -XPUT http://ip:9200/{index_name}/_settings -d '{"number_of_replicas":2}'**

-  Set the number of replicas for new indexes using a template:

   **curl -XPUT http://ip:9200/_template/templatename -d '{ "template": "*", "settings": {"number_of_replicas": 2}}'**

where, **ip** indicates the private IP address of the cluster; **index_name** indicates the index name; **templatename** indicates the template name; **template** indicates the index name matching rule (meaning the template will automatically apply to indexes that match this rule. The asterisk (``*``) indicates that the template will apply to all new indexes); and **number_of_replicas** indicates the number of index replicas to change to. In this example, the number of index replicas is changed to 2.

Service Outage Pattern Analysis
-------------------------------

Master nodes manage cluster-wide operations, including metadata, indexes, and shard allocation. In a cluster with master nodes, the master nodes perform these tasks. In a cluster without them, data nodes and cold data nodes share the responsibilities of the master nodes.

In the case of a single AZ failure, if fewer than half (including half) of the nodes assuming master node responsibilities are still available, service availability will be affected. In this case, you need to restore services by referring to :ref:`Table 2 <en-us_topic_0000002316900222__en-us_topic_0000002287671248_table15496183015206>`.

For example, a cluster has three master nodes distributed in two AZs. If the AZ that contains one master node becomes unavailable while the other AZ remains available, services will still be available. However, if it is the other AZ, which contains two of the three master nodes, that fails, services will be interrupted, because fewer than half of the master nodes (or nodes that assume master node responsibilities) are available. In this case, restore services by referring to :ref:`Table 2 <en-us_topic_0000002316900222__en-us_topic_0000002287671248_table15496183015206>`.

.. _en-us_topic_0000002316900222__en-us_topic_0000002287671248_table15496183015206:

.. table:: **Table 2** Possible service outage patterns in the face of the failure of a single AZ

   +-----------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Number of AZs         | Number of Master Nodes                                                                       | Service Outage Patterns and Handling Suggestions                                                                                                                                                                                                                                                                                                                                                                         |
   +=======================+==============================================================================================+==========================================================================================================================================================================================================================================================================================================================================================================================================================+
   | 2                     | 0 (In this case, data nodes and cold data nodes share the responsibilities of master nodes.) | -  If the number of data nodes plus cold data nodes is an even number:                                                                                                                                                                                                                                                                                                                                                   |
   |                       |                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                          |
   |                       |                                                                                              |    If half of the nodes become unavailable due to the failure of a single AZ, you must add one node to the still available AZ to ensure a master node can be elected for the cluster. To add nodes to your cluster, contact technical support.                                                                                                                                                                           |
   |                       |                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                          |
   |                       |                                                                                              | -  If the number of data nodes plus cold data nodes is an old number:                                                                                                                                                                                                                                                                                                                                                    |
   |                       |                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                          |
   |                       |                                                                                              |    -  If the failed AZ is the one that has one more node, you must add two nodes to the surviving AZ to ensure a master node can be elected for the cluster. To add nodes to your cluster, contact technical support.                                                                                                                                                                                                    |
   |                       |                                                                                              |    -  If the failed AZ is the other one—the one that has one less node, services will not be interrupted and a master node can be elected.                                                                                                                                                                                                                                                                               |
   +-----------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 2                     | 3                                                                                            | There is a 50% chance of service interruption when one AZ fails. In this situation, one AZ has two master nodes, and the other has one:                                                                                                                                                                                                                                                                                  |
   |                       |                                                                                              |                                                                                                                                                                                                                                                                                                                                                                                                                          |
   |                       |                                                                                              | -  If the AZ that has one master node fails while the other AZ remains available, two master nodes are still available, so a master node can be elected from among them. In this case, services remain available.                                                                                                                                                                                                        |
   |                       |                                                                                              | -  If the failed AZ is the other one, only one master node survives, in which case, no master node can be elected, and services will be interrupted. In this case, contact technical support.                                                                                                                                                                                                                            |
   +-----------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 3                     | 0 (In this case, data nodes and cold data nodes share the responsibilities of master nodes.) | There is a small chance of service interruption when a single node fails. However, there is one high-risk scenario: If the cluster spans three AZs and the total number of data nodes plus cold data nodes is 4, so the node distribution across the three AZs is 2-1-1, the failure of the AZ containing two nodes will cause a service interruption. To avoid this, avoid selecting four nodes for a three-AZ cluster. |
   +-----------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 3                     | 3                                                                                            | A single AZ failure will not result in service interruptions.                                                                                                                                                                                                                                                                                                                                                            |
   +-----------------------+----------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
