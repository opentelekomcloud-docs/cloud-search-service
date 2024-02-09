:original_name: css_01_0188.html

.. _css_01_0188:

Deploying a Cross-AZ Cluster
============================

To prevent data loss and minimize the cluster downtime in case of service interruption, CSS supports cross-AZ cluster deployment. When creating a cluster, you can select two or three AZs in the same region. The system will automatically allocate nodes to these AZs.

Allocating Nodes
----------------

If you select two or three AZs when creating a cluster, CSS automatically enables the cross-AZ HA function and properly allocates nodes to different AZs. :ref:`Table 1 <css_01_0188__en-us_topic_0000001478394613_table13143175454216>` describes how the nodes are allocated.

.. note::

   -  When creating a cluster, ensure that the number of selected nodes is no less than the number of AZs. Otherwise, cross-AZ deployment is not supported.
   -  If you enable master nodes when deploying a cross-AZ cluster, the master nodes will also be distributed to different AZs.
   -  The node quantity difference between any two AZs is no more than one.

.. _css_01_0188__en-us_topic_0000001478394613_table13143175454216:

.. table:: **Table 1** Number of nodes and AZ distribution

   ===== ========= ============= === ============= === ===
   Nodes Single AZ Two AZs           Three AZs
   \     AZ1       AZ1           AZ2 AZ1           AZ2 AZ3
   1     1         Not supported     Not supported
   2     2         1             1   Not supported
   3     3         2             1   1             1   1
   4     4         2             2   2             1   1
   ...   ...       ...           ... ...           ... ...
   ===== ========= ============= === ============= === ===

Setting Replicas
----------------

Setting replicas enables clusters effectively use the HA capability of AZs.

-  In two-AZ deployment, if one AZ becomes unavailable, the other AZ continues to provide services. In this case, at least one replica is required. Elasticsearch has one replica by default. You can retain the default value if you do not require higher read performance.

-  In three-AZ deployment, if one AZ becomes unavailable, the other AZs continue to provide services. In this case, at least one replica is required. Elasticsearch has one replica by default. If you need more replicas to improve the cluster's ability to handle queries, modify **settings** to change the number of replicas.

   You can run the following command to modify the number of index replicas:

   **curl -XPUT http://ip:9200/{index_name}/_settings -d '{"number_of_replicas":2}'**

   Alternatively, run the following command to specify the number of replicas in the template:

   **curl -XPUT http://ip:9200/ \_template/templatename -d '{ "template": "*", "settings": {"number_of_replicas": 2}}'**

.. note::

   -  **ip**: private network address
   -  **index_name**: index name
   -  **number_of_replicas**: number of replicas after modification. The value in the preceding command indicates that two replicas are required.

Possible Service Interruptions
------------------------------

The following table describes the possible service interruptions when an AZ of a two- or three-AZ cluster is faulty.

.. table:: **Table 2** Possible service interruptions

   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | AZs                   | Master Nodes          | Service Interruption Analysis                                                                                                                                                                                                                              |
   +=======================+=======================+============================================================================================================================================================================================================================================================+
   | 2                     | 0                     | -  When the number of nodes is an even number:                                                                                                                                                                                                             |
   |                       |                       |                                                                                                                                                                                                                                                            |
   |                       |                       |    -  If half of data nodes are faulty, replace one node in the faulty AZ before you select the master node.                                                                                                                                               |
   |                       |                       |                                                                                                                                                                                                                                                            |
   |                       |                       | -  When the number of nodes is an odd number:                                                                                                                                                                                                              |
   |                       |                       |                                                                                                                                                                                                                                                            |
   |                       |                       |    -  If the faulty AZ contains one more node than the normal AZ, you need to replace one node in the faulty AZ before you select the master node. For details about how to replace nodes, contact technical support.                                      |
   |                       |                       |    -  If the faulty AZ contains one less node than the normal AZ, services will not be interrupted and you can select the master node.                                                                                                                     |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 2                     | 3                     | There is a 50% possibility for service interruption. When two dedicated master nodes are allocated to one AZ and another master node is allocated to the other AZ:                                                                                         |
   |                       |                       |                                                                                                                                                                                                                                                            |
   |                       |                       | -  If service interruption happens in the AZ with one master node, you can select a master node from the AZ that has two dedicated master nodes.                                                                                                           |
   |                       |                       | -  If service interruption happens in the AZ with two dedicated master nodes, you have no choice in the remaining AZ, because it has only one dedicated master node. In this case, services will be interrupted and you need to contact technical support. |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 3                     | 0                     | If you configure four nodes in three AZs, each AZ will have at least one node. If the AZ with two nodes is faulty, the services will be interrupted. You are not advised to configure four nodes when selecting three AZs.                                 |
   |                       |                       |                                                                                                                                                                                                                                                            |
   |                       |                       | Generally, service interruption will not occur.                                                                                                                                                                                                            |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 3                     | 3                     | Service interruption does not occur.                                                                                                                                                                                                                       |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
