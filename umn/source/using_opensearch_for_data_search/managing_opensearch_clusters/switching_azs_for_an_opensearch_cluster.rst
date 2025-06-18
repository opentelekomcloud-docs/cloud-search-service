:original_name: css_01_0494.html

.. _css_01_0494:

Switching AZs for an OpenSearch Cluster
=======================================

CSS supports cross-AZ deployment. By switching AZs for a cluster, you can obtain more resources for the cluster or improve cluster availability.

Scenarios
---------

You can **Add AZ** or **Migrate AZ**.

-  **Add AZ**: Add one or two AZs to a single-AZ cluster, or add an AZ to a dual-AZ cluster to improve cluster availability.
-  **Migrate AZ**: Completely migrate data from the current AZ to another AZ that has sufficient resources.

Prerequisites
-------------

-  Ensure that an AZ with sufficient resources exists.
-  The target cluster is available and has no tasks in progress.
-  Make sure that no non-standard operations have been performed in the cluster. If you have made non-standard modifications, such as modifying return routes, system parameters, and Kibana configurations, these modifications will be lost after the AZ change and your services may be affected.
-  All mission-critical data has been backed up before an AZ switchover. This is to prevent data loss.

Constraints
-----------

-  To ensure service continuity, the total number of data nodes and cold data nodes in a cluster must be greater than or equal to 3.
-  During the change, nodes are brought offline one by one and then new nodes are created. Ensure that the disk capacity of other nodes can store all the data of the node after a single node is brought offline.
-  To prevent backup allocation failures after a node is brought offline during the change, ensure that the maximum number of primary and standby index shards of an index can be allocated to the remaining data nodes and cold data nodes. That is, the maximum number of primary and standby shards of an index plus 1 is less than or equal to the total number of data nodes and cold data nodes in the current cluster.
-  Before a change completes, some nodes may have been moved to a new AZ. In this case, the AZs before and after the change are both displayed. After the change succeeds, the new AZs and their nodes will be displayed properly.
-  When adding AZs, the current AZ must be retained in the change. When adding one or two AZs to a single-AZ cluster, you must change AZs for all nodes at the same time. When adding an AZ to a dual-AZ cluster, you can change AZs for a single type of nodes or all nodes in a cluster at a time. For example, in a cluster using the dual-AZ architecture, you can use the three-AZ architecture for master nodes alone. During HA modification, the nodes with the smallest configurations are modified to rebuild the cluster. After the HA modification is complete, the YML configuration of the nodes that are not modified is also updated. You need to restart the cluster to make the modification take effect.
-  When migrating an AZ, you can select only one target AZ. You can migrate AZs for a single type of nodes or all nodes in a cluster at a time. For example, in a cluster with two AZs, you can migrate the AZ of the master node to the other AZ. After adding AZs, you need to restart the cluster to make the modification take effect.

Changing AZs
------------

#. Log in to the CSS management console.

#. In the navigation pane, choose a cluster type. The cluster management page is displayed.

#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.

#. Click the **Change AZ** tab.

#. On the **Change AZ** page, set parameters.

   .. table:: **Table 1** Parameters for changing AZs

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                                                       |
      +===================================+===================================================================================================================================================================================================================================================================================================+
      | Operation Type                    | -  **Add AZ**: Add one or two AZs to a single-AZ cluster, or add an AZ to a dual-AZ cluster.                                                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                                                                                   |
      |                                   |    During HA modification, the nodes with the smallest configurations are modified to rebuild the cluster. After the HA modification is complete, the YML configuration of the nodes that are not modified is also updated. You need to restart the cluster to make the modification take effect. |
      |                                   |                                                                                                                                                                                                                                                                                                   |
      |                                   | -  **Migrate AZ**: Migrate data from one AZ to another.                                                                                                                                                                                                                                           |
      |                                   |                                                                                                                                                                                                                                                                                                   |
      |                                   |    After adding AZs, you need to restart the cluster to make the modification take effect.                                                                                                                                                                                                        |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Node Type                         | Select a type of node or **All nodes** to change their AZ.                                                                                                                                                                                                                                        |
      |                                   |                                                                                                                                                                                                                                                                                                   |
      |                                   | .. note::                                                                                                                                                                                                                                                                                         |
      |                                   |                                                                                                                                                                                                                                                                                                   |
      |                                   |    When adding one or two AZs to a single-AZ cluster, you can only select **All nodes** to change AZs for all nodes at a time.                                                                                                                                                                    |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Current AZ                        | Current AZ of a cluster                                                                                                                                                                                                                                                                           |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Target AZ                         | Target AZ.                                                                                                                                                                                                                                                                                        |
      |                                   |                                                                                                                                                                                                                                                                                                   |
      |                                   | -  **Add AZ**: Select up to three AZs, which must include all your current AZs.                                                                                                                                                                                                                   |
      |                                   | -  **Migrate AZ**: Select only one target AZ, which cannot be your current AZ.                                                                                                                                                                                                                    |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Submit**. Determine whether to check for the backup of all indexes and click **OK** to start the change.

#. The current AZ change task is displayed in the task list. If the task status is **Running**, expand the task list and click **View Progress** to view the progress details.

   If the task status is **Failed**, you can retry or terminate the task.

   -  Retry a task: Click **Retry** in the **Operation** column of a task.

   -  Terminate a task: Click **Terminate** in the **Operation** column of a task.

      If the AZ of the original node is not changed after the task is terminated, you can recover the node by referring to :ref:`Replacing Specified Nodes for an Elasticsearch Cluster <css_01_0156>`.

      .. note::

         If the AZ of some nodes has been changed and the AZ form of the cluster has changed, stopping the switchover task may make the delivery of the previous switchover request fail. Exercise caution when stopping the switchover task.
