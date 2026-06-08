:original_name: css_01_0286.html

.. _css_01_0286:

Restarting a Cluster
====================

A cluster restart may be necessary for purposes such as configuration updates or fault recovery. CSS OpenSearch clusters support two restart modes: quick restart and rolling restart. To balance cluster availability and restart efficiency, select the mode best suited to your operational requirements.

Comparing the Two Restart Modes
-------------------------------

.. table:: **Table 1** Introducing the two restart modes

   +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Restart Mode          | Quick Restart                                                                                                                                | Rolling Restart                                                                                                                                                          |
   +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Impact                | High:                                                                                                                                        | Low:                                                                                                                                                                     |
   |                       |                                                                                                                                              |                                                                                                                                                                          |
   |                       | The cluster becomes unavailable for both read and write operations for the entire duration of the upgrade.                                   | Only the node that is being restarted is unavailable. The cluster as a whole remains available all the time.                                                             |
   +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | How It Works          | Parallel operations: All selected nodes are stopped and restarted at once.                                                                   | Serial operations: Restart node A > Wait for it to recover > Restart node B > Wait for it to recover, and so on                                                          |
   +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Data Security         | There is risk of data loss if you forcibly restart nodes that are still serving write requests.                                              | Data security is guaranteed as the system automatically handles shard allocation.                                                                                        |
   +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Time Required         | All nodes are restarted simultaneously. The total restart time is typically shorter.                                                         | The selected nodes are restarted one at a time. After the first node, each node can restart only after the previous node has fully recovered. This process takes longer. |
   +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | When to Use           | Use this mode in development or testing environments, where clusters are completely deadlocked, or where service interruption is acceptable. | Use this model in production environments, where high availability takes top priority and clusters store large amounts of data.                                          |
   +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Node Quantity         | There is no limit on the number of nodes.                                                                                                    | There are at least three nodes.                                                                                                                                          |
   +-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Constraints
-----------

Clusters whose **Task Status** is **Frozen** or that have ongoing tasks cannot be restarted.

Before You Start
----------------

-  Check the target cluster's health status. Check the **Task Status** column to ensure there are no ongoing tasks.
-  Pause high-concurrency data ingestion tasks to prevent write failures caused by primary shard changes during the restart.
-  Avoid restarting a cluster during peak hours, as doing so may impact data integrity and service availability.
-  Before performing a **rolling restart**, check that mission-critical indexes have at least one replica shard. Without any replica, an index will be temporarily unavailable when the node that hosts its primary shard restarts.

Quick Restart
-------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, find the target cluster, and choose **More > Restart** in the **Operation** column.
#. On the **Restart Cluster** page, set parameters.

   .. table:: **Table 2** Configuring a quick restart

      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                           |
      +===================================+=======================================================================================================================================================+
      | Restart Mode                      | Select **Quick Restart**.                                                                                                                             |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Select By                         | Select **Node type** or **Node name**.                                                                                                                |
      |                                   |                                                                                                                                                       |
      |                                   | -  **Node type**: Select one or more node types for restart. For example, you can use this option to restart all client nodes to release connections. |
      |                                   | -  **Node name**: Restart only one node at a time. Use this option to restart individual nodes, for example, to restore faulty nodes.                 |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Value                             | Select one or more node types or a node name, depending on the setting of **Select By**.                                                              |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Manually type in **YES**, and click **OK** to start the restart task.

   .. warning::

      The cluster will be unavailable for the entire duration of a quick restart.

#. When the cluster status changes from **Processing** to **Available**, the cluster has restarted successfully.

Rolling Restart
---------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, find the target cluster, and choose **More > Restart** in the **Operation** column.
#. On the **Restart Cluster** page, set parameters.

   .. table:: **Table 3** Configuring a rolling restart

      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                     |
      +===================================+=================================================================================================================================================+
      | Restart Mode                      | Select **Rolling Restart**.                                                                                                                     |
      |                                   |                                                                                                                                                 |
      |                                   | This option is unavailable when the cluster has fewer than three nodes.                                                                         |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
      | Select By                         | The default value is **Node type**.                                                                                                             |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
      | Value                             | Select node types for the restart.                                                                                                              |
      |                                   |                                                                                                                                                 |
      |                                   | -  **Select all**: Select all node types.                                                                                                       |
      |                                   | -  Select specific node types: For instance, to restart cold data nodes, select **Cold Data Nodes** only. The system will skip all other nodes. |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

#. Manually type in **YES**, and click **OK** to start the restart task.
#. When the cluster status changes from **Processing** to **Available**, the cluster has restarted successfully.

FAQ
---

-  **Question 1: What should I do if a rolling restart is stuck in **Restarting** for a long time?**

   During a rolling restart, after the last node is restarted, the system waits for the cluster to recover (health status turns green/yellow). If the cluster has extremely large indexes or index shards are still being restored, the task will be stuck in **Restarting** for a long time. You can run the **GET \_cat/recovery?v** command to check the shard recovery progress.

-  **Question 2: How do I perform a rolling-like restart on a cluster with just two nodes?**

   The rolling restart option is unavailable for clusters with just two nodes, but you can achieve a similar process manually:

   #. Check the number of index replicas. To ensure service continuity, ensure that each index has at least one replica.
   #. Select **Fast Restart**, then select **Node name** for **Select By**. Select one of the nodes to restart it.
   #. Wait for this node to fully recover and the cluster status to change to **Available**. Then restart the other node.
