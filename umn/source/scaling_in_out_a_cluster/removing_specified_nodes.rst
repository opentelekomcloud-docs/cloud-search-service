:original_name: css_01_0081.html

.. _css_01_0081:

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
#. In the navigation pane on the left, choose **Clusters**. On the displayed **Clusters** page, locate the target cluster and choose **More** > **Scale Cluster** in the **Operation** column.
#. Choose the **Scale In** tab.
#. Select the target nodes.
#. Click **Scale Now**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling in**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled in.
