:original_name: en-us_topic_0000001477579404.html

.. _en-us_topic_0000001477579404:

Replacing a Specified Node
==========================

If a node in the cluster is faulty, you can create a new node with the same specifications to replace it. During the replacement of a specified node, data of that node will be migrated in advance and will not be lost.

Prerequisites
-------------

The target cluster is available and has no tasks in progress.

Constraints
-----------

-  Only one node can be replaced at a time.
-  The ID, IP address, specifications, and AZ of the new node will be the same as those of the original one.
-  The configurations you modified manually will not be retained after node replacement. For example, if you have manually added a return route to the original node, you need to add it to the new node again after the node replacement is complete.
-  If the node you want to replace is a data node (ess) or cold data node (ess-cold), pay attention to the following precautions:

   #. Before a data node or cold data node is replaced, its data needs to be migrated to other nodes. To properly store the data, ensure the maximum sum of replicas and primary shards of an index is smaller than the total number of data nodes (ess and ess-cold nodes) in the cluster. The node replacement duration depends heavily on the migration speed.
   #. Clusters whose version is earlier than 7.6.2 cannot have closed indexes. Otherwise, data nodes or cold data nodes cannot be replaced.
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

   -  **Agency**: Select an IAM agency to grant the current account the permission to switch AZs.

      If no agency is available, click **Create IAM Agency** to go to the IAM console and create an agency.

      .. note::

         The selected agency must be assigned the **Tenant Administrator** or **VPC Administrator** policy.

   -  **Whether to perform data migration**: If this option is selected, data migration is performed. If the target node has disabled indexes or indexes that have no replicas, this option must be selected.
   -  Select the node to be replaced in the data node table.

#. Click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Upgrading**. When **Cluster Status** changes to **Available**, the node has been successfully replaced.
