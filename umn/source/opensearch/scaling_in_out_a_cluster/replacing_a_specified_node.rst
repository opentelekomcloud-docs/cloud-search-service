:original_name: en-us_topic_0000001640892937.html

.. _en-us_topic_0000001640892937:

Replacing a Specified Node
==========================

If a node in the cluster is faulty, you can create a new node with the same specifications to replace it.

Prerequisites
-------------

The target cluster is available and has no tasks in progress.

Constraints
-----------

-  Only one node can be replaced at a time.
-  The ID, IP address, specifications, and AZ of the new node will be the same as those of the original one.
-  The configurations you modified manually will not be retained after node replacement. For example, if you have manually added a return route to the original node, you need to add it to the new node again after the node replacement is complete.
-  If the node you want to replace is a data node (ess) or cold data node (ess-cold), pay attention to the following precautions:

   #. For data node replacement, data from the original node will be migrated to other nodes, and then the node will be rebuilt. Therefore, the total number of replicas and primary shards of each index in the cluster must be less than the total number of data nodes (including ess and ess-cold) in the cluster. The time required for node replacement is closely related to the time required for migrating data to other nodes.
   #. The AZ of the node to be replaced must have two or more data nodes (including ess and ess-cold).
   #. If the cluster of the node to be replaced does not have a master node (ess-master), the number of available data nodes (including ess and ess-cold) in the cluster must be greater than or equal to 3.
   #. The preceding precautions do not apply if you are replacing a master node (ess-master) or client node (ess-client).
   #. The precautions 1 to 4 do not apply if you are replacing a faulty node, regardless of its type. Faulty nodes are not included in **\_cat/nodes**.

Procedure
---------

#. Log in to the CSS management console.
#. In the navigation pane, choose a cluster type. The cluster management page is displayed.
#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.
#. On the **Modify Configuration** page, click the **Replace Node** tab.
#. On the **Replace Node** tab page, set the following parameters:

   -  **Whether to perform data migration**: If this option is selected, data migration is performed. If the target node has disabled indexes or indexes that have no replicas, this option must be selected.
   -  Select the node to be replaced in the data node table.

#. Click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Upgrading**. When **Cluster Status** changes to **Available**, the node has been successfully replaced.
