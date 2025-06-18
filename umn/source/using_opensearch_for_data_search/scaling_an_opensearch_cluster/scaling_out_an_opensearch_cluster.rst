:original_name: css_01_0484.html

.. _css_01_0484:

Scaling Out an OpenSearch Cluster
=================================

If the workloads on the data plane of an OpenSearch cluster increase, you can scale out the cluster by increasing the quantity or capacity of its nodes, including changing the node specifications and types.

Scenario
--------

CSS supports multiple scale-out methods, as described in :ref:`Table 1 <css_01_0484__css_01_0151_table13694163818283>`.

.. _css_01_0484__css_01_0151_table13694163818283:

.. table:: **Table 1** Scaling out an Elasticsearch cluster

   +-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Scenario                                      | Description                                                                                                                                                                                                                                                                                                 | Details                                                                                                                                    |
   +===============================================+=============================================================================================================================================================================================================================================================================================================+============================================================================================================================================+
   | Increasing the quantity and capacity of nodes | Only the quantity and storage capacity of nodes can be increased. Applicable scenarios:                                                                                                                                                                                                                     | :ref:`Adding More Nodes and Increasing Node Storage Capacity <css_01_0484__css_01_0151_en-us_topic_0000001285669680_section1177713055318>` |
   |                                               |                                                                                                                                                                                                                                                                                                             |                                                                                                                                            |
   |                                               | -  If a data node (ess) is under heavy pressure and responds slowly, you can expand its storage capacity to improve its performance and storage reliability. If some nodes become unavailable due to excessively large data volumes or misoperations, you can add new nodes to ensure cluster availability. |                                                                                                                                            |
   |                                               | -  Cold data nodes (ess-cold) are used to share the load of data nodes. To prevent the loss of cold data, you can expand the storage capacity of existing cold data nodes or add new ones.                                                                                                                  |                                                                                                                                            |
   +-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Increasing node specifications                | You can only change the node specifications of a cluster by node type. Applicable scenarios:                                                                                                                                                                                                                | :ref:`Changing the Node Specifications of an OpenSearch Cluster <css_01_0491>`                                                             |
   |                                               |                                                                                                                                                                                                                                                                                                             |                                                                                                                                            |
   |                                               | -  If the allocation of new indexes or shards takes too long or the coordination and scheduling of nodes are inefficient, increase the master node (ess-master) specifications.                                                                                                                             |                                                                                                                                            |
   |                                               | -  If too many requests need to be handled or too many results need to be aggregated, increase the client node (ess-client) specifications.                                                                                                                                                                 |                                                                                                                                            |
   |                                               | -  If data nodes (ess) are becoming slower in responding to data writing and query requests, increase the specifications of the data nodes.                                                                                                                                                                 |                                                                                                                                            |
   |                                               | -  If cold data query becomes slow, increase the cold node (ess-cold) specifications.                                                                                                                                                                                                                       |                                                                                                                                            |
   +-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Adding new node types                         | For a cluster that has no master (ess-master) or client (ess-client) nodes, as the load on its data plane increases, you can add master or client nodes as needed to scale up capacity.                                                                                                                     | :ref:`Adding Master or Client Nodes <css_01_0484__css_01_0151_section1195734814511>`                                                       |
   +-----------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

Constraints
-----------

-  The node storage capacity of a cluster can only be increased but cannot be reduced. Select an appropriate node storage capacity based on the data volume and projected data growth.

-  The storage capacity of the master and client nodes in a cluster cannot be expanded.

-  In each cluster, the number of nodes supported by each node type varies, depending on the types of nodes used in that cluster. For details, see :ref:`Table 2 <css_01_0484__css_01_0151_en-us_topic_0000001285669680_table10730243193816>`.

   .. _css_01_0484__css_01_0151_en-us_topic_0000001285669680_table10730243193816:

   .. table:: **Table 2** Number of nodes of different types allowed in a single cluster

      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | Node Type                                                                                                                                 | Node Quantity                                 |
      +===========================================================================================================================================+===============================================+
      | ess                                                                                                                                       | ess: 1-32                                     |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master                                                                                                                           | ess: 1-200                                    |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-master: an odd number ranging from 3 to 9 |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-client                                                                                                                           | ess: 1-32                                     |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-client: 1-32                              |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-cold                                                                                                                             | ess: 1-32                                     |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-cold: 1-32                                |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-client                                                                                                               | ess: 1-200                                    |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-client: 1-32                              |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-cold                                                                                                                 | ess: 1-200                                    |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-cold: 1-32                                |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-client, ess-cold                                                                                                                 | ess: 1-32                                     |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-client: 1-32                              |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-cold: 1-32                                |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-client, ess-cold                                                                                                     | ess: 1-200                                    |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-client: 1-32                              |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-cold: 1-32                                |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | .. note::                                                                                                                                 |                                               |
      |                                                                                                                                           |                                               |
      |    -  **ess**: data node, which is the default node type that is mandatory for cluster creation. The other three node types are optional. |                                               |
      |    -  **ess-master**: master node                                                                                                         |                                               |
      |    -  **ess-client**: client node                                                                                                         |                                               |
      |    -  **ess-cold**: cold data node                                                                                                        |                                               |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+

Prerequisites
-------------

-  The cluster is available and has no tasks in progress.
-  CSS has sufficient resources to expand cluster capacity.

.. _css_01_0484__css_01_0151_en-us_topic_0000001285669680_section1177713055318:

Adding More Nodes and Increasing Node Storage Capacity
------------------------------------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose a cluster type. The cluster management page is displayed.
#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.
#. Click the **Scale Cluster** tab.
#. Set the necessary parameters.

   .. table:: **Table 3** Adding more nodes or increasing node storage capacity

      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                     |
      +===================================+=================================================================================================================================================================+
      | Action                            | Select **Scale out**.                                                                                                                                           |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Resources                         | Shows the change of resources for this scale-out operation.                                                                                                     |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Nodes                             | Increase the number of nodes and node storage capacity in the **Nodes** and **Node Storage Type** columns. You can change multiple node types at the same time. |
      |                                   |                                                                                                                                                                 |
      |                                   | -  For the value range of node quantity for each node type, see :ref:`Table 2 <css_01_0484__css_01_0151_en-us_topic_0000001285669680_table10730243193816>`.     |
      |                                   | -  The value range of node storage capacity is determined by the node specifications. The value must be a multiple of 20.                                       |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling out**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled out.

.. _css_01_0484__css_01_0151_section1195734814511:

Adding Master or Client Nodes
-----------------------------

#. Log in to the CSS management console.

#. In the navigation pane, choose a cluster type. The cluster management page is displayed.

#. In the cluster list, select the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.

#. On the **Modify Configuration** page, choose the **Add Master/Client Node** tab.

   If a cluster already has both master and client nodes, the **Add Master/Client Node** tab is unavailable.

#. Select the target node type and set the node specifications, quantity, and storage.

   .. table:: **Table 4** Adding master or client nodes

      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                             |
      +===================================+=========================================================================================================================================================================+
      | Node types                        | Select the type of nodes you want to add.                                                                                                                               |
      |                                   |                                                                                                                                                                         |
      |                                   | -  Only one node type can be selected at a time. If you need to add both Master and Client nodes, you need to perform this task twice.                                  |
      |                                   | -  If the cluster already has Master or Client nodes, only the other node type is displayed here.                                                                       |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Node Specifications               | Select node specifications based on site requirements.                                                                                                                  |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Nodes                             | Set the number of nodes to add for this node type. For the value range, see :ref:`Table 2 <css_01_0484__css_01_0151_en-us_topic_0000001285669680_table10730243193816>`. |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Node Storage Type                 | Set the node storage type. The storage capacity of the master and client nodes in a cluster cannot be changed.                                                          |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Next**.

#. Confirm the information and click **Submit**.

   Return to the cluster list page. The **Task Status** of the cluster is **Scaling out**.

   -  If you add a master node and **Cluster Status** changes to **Available**, the master node has been successfully added.
   -  If you add a client node and **Cluster Status** changes to **Available**, the client node has been added. You can restart data nodes and cold data nodes to shut down Cerebro and OpenSearch Dashboards processes on these nodes.
