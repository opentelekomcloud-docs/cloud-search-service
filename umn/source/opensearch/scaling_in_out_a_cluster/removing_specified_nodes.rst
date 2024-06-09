:original_name: en-us_topic_0000001590612676.html

.. _en-us_topic_0000001590612676:

Removing Specified Nodes
========================

If a cluster can process existing data without fully using its nodes, you can remove one or more specified nodes from the cluster to reduce costs. Services will not be interrupted during the removal of specified nodes.

Prerequisites
-------------

The target cluster is available and has no tasks in progress.

Constraints
-----------

-  Ensure that the disk usage after scale-in is less than 80% and each AZ of each node type has at least one node.
-  In a cross-AZ cluster, the difference between the numbers of the same type nodes in different AZs cannot exceed 1.
-  For a cluster without master nodes, the number of removed data nodes and cold data nodes in a scale-in must be fewer than half of the original number of data nodes and cold data nodes, and the number of remaining data nodes and cold data nodes after a scale-in must be greater than the maximum number of index replicas.
-  For a cluster with master nodes, the number of removed master nodes in a scale-in must be fewer than half of the original master node number. After scale-in, there has to be an odd number of master nodes, and there has to be at least three of them.

Procedure
---------

#. Log in to the CSS management console.
#. In the navigation pane, choose a cluster type. The cluster management page is displayed.
#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.
#. On the **Modify Configuration** page, click the **Scale In** tab.
#. On the **Scale In** tab page, set the following parameters:

   -  **Whether to perform data migration**: If this option is selected, data migration is performed. If the target node contains disabled indexes or indexes that have no replicas, this option must be selected.
   -  In the data node table, select the node to be scaled in.

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling in**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled in.
