:original_name: css_01_0156.html

.. _css_01_0156:

Replacing Specified Nodes for an Elasticsearch Cluster
======================================================

If a node in a cluster becomes faulty, you can create a new node with the same specifications to replace it. Before the replacement of a specified node, the data of that node will be migrated away in advance and will not be lost.

Prerequisites
-------------

-  The target cluster is available and has no tasks in progress.
-  All mission-critical data has been backed up before a node replacement. This is to prevent data loss.

Constraints
-----------

-  Only one node can be replaced at a time.
-  The ID, IP address, specifications, and AZ of the new node will be the same as those of the original one.
-  The configurations you modified manually will not be retained after node replacement. For example, if you have manually added a return route to the original node, you need to add it to the new node again after the node replacement is complete.
-  If the node you want to replace is a data node or cold data node, pay attention to the following precautions:

   -  Before a data node or cold data node is replaced, its data needs to be migrated to other nodes. To ensure data security, ensure the maximum total of replicas and primary shards of an index is smaller than the total number of data nodes plus cold data nodes in the cluster. The time it takes to replace the node depends on how fast the data can be migrated.
   -  Clusters whose version is earlier than 7.6.2 cannot have closed indexes. Otherwise, their data nodes or cold data nodes cannot be replaced.
   -  The AZ of the node to be replaced must have two or more data nodes or cold data nodes.
   -  If the cluster where a data node or cold data node needs to be replaced does not have a master node, the total number of available data nodes and cold data nodes in the cluster must be at least 3.
   -  If it is a master or client node that needs to be replaced, the precautions above do not apply.
   -  The precautions above do not apply if you are replacing a faulty node, regardless of its type. Faulty nodes are not included in **\_cat/nodes**.

Replacing a Specified Node
--------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose a cluster type. The cluster management page is displayed.
#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.
#. On the **Modify Configuration** page, click the **Replace Node** tab.
#. On the **Replace Node** tab, set the parameters as needed.

   .. table:: **Table 1** Replacing a specified node

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                               |
      +===================================+===========================================================================================================================================================================+
      | Whether to perform data migration | Selecting this option means data migration will be performed. If the target node has disabled indexes or has indexes that have no replicas, this option must be selected. |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Node Type                         | Expand the node type that needs be changed to show all nodes under it. Select the nodes you want to replace.                                                              |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Replacing nodes**. When **Cluster Status** changes to **Available**, the node has been successfully replaced.
