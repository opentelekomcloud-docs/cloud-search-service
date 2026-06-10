:original_name: css_01_0311.html

.. _css_01_0311:

Switching AZs
=============

CSS supports cross-AZ deployment. By switching AZs for a cluster, you can make more resources available to the cluster or improve the cluster's availability.

You can **Add AZ** or **Migrate AZ**.

-  **Add AZ**: Add one or two AZs for a single-AZ cluster, or add one AZ for a dual-AZ cluster to enhance cluster availability.
-  **Migrate AZ**: Migrate data from the current AZ to another AZ that has sufficient resources for the cluster.

The AZ change process is as follows:

#. Migrate data from one node to other available nodes.

#. Rebuild the node for the target AZ. Keep the node ID, IP address, and specifications unchanged.

#. Add the new node into the cluster. The system automatically triggers a shard reallocation, migrating some of the shards to the new node. Then repeat these steps on all the other nodes.

The nodes are changed one at a time to prevent service interruptions.

Constraints
-----------

-  To ensure service continuity, the total number of data nodes plus cold data nodes in the cluster must be at least three.
-  During the change, nodes are brought offline one by one and then new nodes are created. Ensure that the total disk capacity of the remaining nodes is sufficient for handling all the data of the cluster, and that the nodes' disk usage stays below 80%.
-  To make sure that all index shards in the cluster can be allocated to the remaining data nodes and cold data nodes, the **total number of data nodes and cold data nodes must be greater than the maximum number of index replicas plus 1**.
-  Before a change completes, some nodes may have already been moved to a new AZ. In this case, the AZs before and after the change are both displayed. After the change succeeds, the new AZs and their nodes will be displayed properly.
-  When you **add an AZ** for a cluster, the current AZ must be retained. When adding one or two AZs for a single-AZ cluster, you must change AZs for all nodes. When adding one AZ for a dual-AZ cluster, you can choose to change AZs for specific types of nodes or all nodes in the cluster. For example, for a dual-AZ cluster, you can use three AZs for its master nodes, while still using two AZs for the rest of its nodes. To complete this AZ change, the system will try to move as few nodes as possible to rebuild the cluster. During this process, the YML configuration file of the nodes that are not modified is also updated. You need to restart the cluster to make the change take effect.
-  When adding AZs for an existing cluster for high availability, follow the node allocation rules below:

   -  To ensure high service availability and prevent individual node overload in a multi-AZ deployment, the following node count requirements must be met:

      -  **For a two-AZ cluster**, there must be at least four data nodes (or cold data nodes), two for each AZ; and there must be at least two client nodes (if configured), one for each AZ.
      -  **For a three-AZ cluster**, each available node type must have at least one node in each AZ. This means each node type must have at least three nodes in total.
      -  For node types that are not deployed (for example, no cold data nodes), the minimum node count requirement does not apply.

   -  Performance enhancement: To prevent uneven data distribution and ensure optimal query and ingestion performance, the number of data nodes or cold data nodes should be an integer multiple of the number of AZs.

-  When migrating an AZ (**Migrate AZ**), you can select only one target AZ. For this operation, you can choose to migrate only specific types of nodes or all nodes in the cluster. For example, for a dual-AZ cluster, you may move the master nodes from one AZ to the other, while keeping the rest of the nodes unchanged. If you migrate from one AZ to another, there is no need to restart the cluster. If multiple AZs are migrated, you must restart the cluster to make the change take effect.

Change Impact
-------------

Before changing a cluster's AZs, it is essential to assess the potential impacts and review operational recommendations. This enables proper scheduling of the change, minimizing service interruptions.

-  Performance

   Changing AZs for a cluster does not interrupt services. However, data migration that occurs during this process consumes I/O performance, and taking individual nodes offline still has some impact on the overall cluster performance.

   To minimize this impact, it is advisable to adjust the data migration rate based on the cluster's traffic cycle: increase the data migration rate during off-peak hours to shorten the task duration, and decrease it **before** peak hours arrive to ensure optimal cluster performance. The data migration rate is determined by the **indices.recovery.max_bytes_per_sec** parameter. The default value of this parameter is the number of vCPUs multiplied by 8 MB. For example, for four vCPUs, the data migration rate is 32 MB/s. You can adjust it based on the service requirements.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "transient": {
          "indices.recovery.max_bytes_per_sec": "128MB"
        }
      }

-  Impact on request handling

   While a node is offline, requests sent to it may fail. To mitigate this impact, the following measures may be taken:

   -  Use a VPC endpoint or a dedicated load balancer to handle access requests to your cluster, which makes sure that requests are automatically routed to available nodes.
   -  Enable an exponential backoff & retry mechanism on the client (configure three retries).
   -  Perform this operation during off-peak hours.

-  Characteristics of this process

   Once started, an AZ change task cannot be stopped until it succeeds or fails.

Change Duration
---------------

The following formula can be used to estimate how long it will take to change AZs for a cluster:

**Change duration (min) = 15 (min) x Total number of nodes involved + Data migration duration (min)**

where, 15 minutes indicates how long non-data migration operations (e.g., initialization) typically take per node. It is an empirical value.

**Data migration duration (min) = Total data size of the nodes to be migrated (MB) ÷ [Total number of vCPUs of the data nodes x 8 (MB/s) x 60 (s)]**

where,

-  8 MB/s indicates that each vCPU can process 8 MB of data per second. It is an empirical value.
-  The formulas above use estimates under ideal conditions. The actual migration speed depends on cluster load.

Prerequisites
-------------

-  The cluster status is **Available**, and there are no ongoing tasks.
-  Make sure that the cluster has not had any non-standard modifications, such as the configuration of custom return routes and system parameters. Such modifications, if ever made, will be lost after the AZ change, which may affect your services.
-  All mission-critical data has been backed up. For details, see :ref:`Creating Snapshots to Back Up Data <css_01_0298>`.

Changing AZs
------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.

#. Click the **Change AZ** tab.

#. On the **Change AZ** page, set parameters.

   .. caution::

      If the number of data nodes plus cold data nodes in a cluster is not divisible by the number of AZs, data in the cluster may be unevenly distributed after the AZ change is completed. For example, if the cluster has two AZs and three data nodes, one node may need to store twice as much data as the other two nodes. This uneven distribution of data may affect the cluster's query and ingestion performance.

   .. table:: **Table 1** Parameters for changing AZs

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                                     |
      +===================================+=================================================================================================================================================================================================================================================================================+
      | Operation Type                    | -  **Add AZ**: Add one or two AZs for a single-AZ cluster, or add one AZ for a dual-AZ cluster.                                                                                                                                                                                 |
      |                                   |                                                                                                                                                                                                                                                                                 |
      |                                   |    To complete this AZ change, the system will try to move as few nodes as possible to rebuild the cluster. During this process, the YML configuration file of the nodes that are not modified is also updated. You need to restart the cluster to make the change take effect. |
      |                                   |                                                                                                                                                                                                                                                                                 |
      |                                   | -  **Migrate AZ**: Migrate data from one AZ to another.                                                                                                                                                                                                                         |
      |                                   |                                                                                                                                                                                                                                                                                 |
      |                                   |    After adding AZs, you need to restart the cluster to make the modification take effect.                                                                                                                                                                                      |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Node Type                         | Select a node type for the AZ change.                                                                                                                                                                                                                                           |
      |                                   |                                                                                                                                                                                                                                                                                 |
      |                                   | Select one node type or **All nodes** to change their AZ. When adding one or two AZs for a single-AZ cluster, you can only select **All nodes**.                                                                                                                                |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Current AZ                        | Current AZ of a cluster                                                                                                                                                                                                                                                         |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Target AZ                         | AZ to add or migrate to.                                                                                                                                                                                                                                                        |
      |                                   |                                                                                                                                                                                                                                                                                 |
      |                                   | -  **Add AZ**: Select up to three AZs, which must include all your current AZs.                                                                                                                                                                                                 |
      |                                   | -  **Migrate AZ**: Select only one target AZ, which cannot be your current AZ.                                                                                                                                                                                                  |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Submit**. In the displayed dialog box, choose whether to check for the presence of a full index snapshot, and click **OK** to start the change.

   .. note::

      You are advised to select **Check full index snapshot**. This ensures that all data has been backed up, so that in case the task fails, the data can be restored using this snapshot.

   When **Task Status** in the task list below changes to **Successful**, the AZ change is completed.

#. Confirm the result.

   a. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
   b. On the **Overview** tab, check the cluster's AZs in the **Basic Information** area to determine whether the change is successful.

Checking the Progress of an AZ Change Task
------------------------------------------

In the **Jobs** area on the **Change AZ** tab, find the AZ change task.

Expand the task list and click **View Progress** to check the task progress and node status.

If **Task Status** is **Failed**, you can retry the task or terminate it.

-  Retry a task: Click **Retry** in the **Operation** column.
-  Terminate a task: Click **Terminate** in the **Operation** column. Before terminating a task, make sure that AZ has been successfully changed for none of the nodes.
