:original_name: css_04_0023.html

.. _css_04_0023:

Multi-AZ HA
===========

To prevent data loss and minimize the cluster downtime in case of service interruption, select two or three AZs in the same region when you create a cluster.

Allocating Nodes
----------------

If you select two or three AZs when creating a cluster, CSS automatically enables the cross-AZ HA function and properly allocates nodes to different AZs.

The following table lists the way nodes are allocated.

===== ====== ============= === ============= === ===
Nodes One AZ Two AZs           Three AZs
\     AZ1    AZ1           AZ2 AZ1           AZ2 AZ3
1     1      Not supported     Not supported
2     2      1             1   Not supported
3     3      2             1   1             1   1
4     4      2             2   2             1   1
...   ...    ...           ... ...           ... ...
===== ====== ============= === ============= === ===

.. note::

   -  CSS does not require that the number of nodes be a multiple of the number of AZs.
   -  When you create a cluster, ensure that the number of nodes you configure is no less than the number of AZs.
   -  The node quantity gap between any two AZs is no more than one.

Configuring Replicas
--------------------

HA can be ensured when you properly configure the number of replicas.

-  In a two-AZ deployment mode, when one AZ is unavailable, the other AZ is required to provide services. Therefore, at least one replica is required. The default number of Elasticsearch replicas is one. In this case, you can retain the default value if you do not have high requirements on read performance.

-  In a three-AZ deployment mode, when one AZ is unavailable, the other AZs are required to provide services. Therefore, at least one replica is required. To improve the cluster query capability, you can set more replicas. In this case, you need to modify the replica configurations to change the number of replicas because the default number of Elasticsearch replicas is one.

   You can run the following command to modify the number of index replicas:

   **curl -XPUT http://ip:9200/{index_name}/_settings -d '{"number_of_replicas":2}'**

   Alternatively, specify the number of replicas in the template:

   **curl -XPUT http://ip:9200/ \_template/templatename -d '{ "template": "*", "settings": {"number_of_replicas": 2}}'**

.. note::

   -  **ip**: private network address
   -  **number_of_replicas**: number of replicas after modification. The value in the preceding command indicates that two replicas are required.

Selecting Master Nodes
----------------------

If you select the master node function when you create a cluster, master nodes will be allocated in different AZs when you select multiple AZs.

Service Interruption
--------------------

:ref:`Table 1 <css_04_0023__en-us_topic_0196327977_table119868579442>` shows the service fault analysis if you select two or three AZs when you create a cluster and one AZ is faulty.

.. _css_04_0023__en-us_topic_0196327977_table119868579442:

.. table:: **Table 1** Service fault analysis when an AZ is faulty

   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | AZs                   | Master Nodes          | Service Interruption Analysis                                                                                                                                                                                                                                                |
   +=======================+=======================+==============================================================================================================================================================================================================================================================================+
   | 2                     | 0                     | -  When the number of nodes is a multiple of 2,                                                                                                                                                                                                                              |
   |                       |                       |                                                                                                                                                                                                                                                                              |
   |                       |                       |    -  If half of data nodes are faulty, replace one node in the faulty AZ before you select the master node.                                                                                                                                                                 |
   |                       |                       |                                                                                                                                                                                                                                                                              |
   |                       |                       | -  When the number of nodes is an odd number,                                                                                                                                                                                                                                |
   |                       |                       |                                                                                                                                                                                                                                                                              |
   |                       |                       |    -  If the faulty AZ contains one more node than the normal AZ, you need to replace one node in the faulty AZ before you select the master node. For details about how to replace nodes, contact technical support.                                                        |
   |                       |                       |    -  If the faulty AZ contains one less node than the normal AZ, services will not be interrupted and you can select the master node.                                                                                                                                       |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 2                     | 3                     | There is a 50% possibility for service interruption. When two dedicated master nodes are allocated to one AZ and another master node is allocated to the other AZ,                                                                                                           |
   |                       |                       |                                                                                                                                                                                                                                                                              |
   |                       |                       | -  If service interruption happens in the AZs with one master node, you can select master nodes from the AZs that have two dedicated master nodes.                                                                                                                           |
   |                       |                       | -  If service interruption happens in the AZs with two dedicated master nodes, you cannot select two master nodes from the remaining AZ because it has only one dedicated master node. In this case, services will be interrupted and you need to contact technical support. |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 3                     | 0                     | If you configure four nodes in three AZs, each AZ is allocated with two, one, and one node respectively. Services will be interrupted if the AZ with two nodes is faulty. You are advised not to configure four nodes when selecting three AZs.                              |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 3                     | 3                     | Service interruption does not occur.                                                                                                                                                                                                                                         |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
