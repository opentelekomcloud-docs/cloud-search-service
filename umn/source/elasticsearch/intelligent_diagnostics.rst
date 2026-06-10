:original_name: css_01_0262.html

.. _css_01_0262:

Intelligent Diagnostics
=======================

During routine operations, you must periodically monitor the health of your Elasticsearch clusters to ensure service stability. However, manual health checks are time-consuming, labor-consuming, and prone to oversight. Key issues may be easily missed. To address this, CSS provides an Intelligent O&M feature. It supports both scheduled and on-demand diagnostics, covering essential checks such as data node disk usage, cluster health status, and node CPU usage. Through these checks, O&M personnel can detect and handle potential risks in a timely manner to ensure cluster reliability and availability. By default, Intelligent O&M retains the most recent 11 diagnostic reports, so you can always review the latest results. You can also export any report for further analysis or long-term archiving.

Constraints
-----------

-  Intelligent diagnostics cannot be enabled while the cluster is in one of the following **Cluster Status**: frozen, creating, or creation failed.
-  While a diagnostic task is in progress, you cannot manually start another task.
-  Running diagnostics on a cluster that is in the process of a configuration change (for example, being scaled up or down, or having its node specifications changed) may lead to inaccurate results. You are advised to avoid such times.
-  When intelligent diagnostics is enabled, the system is allowed by default to read cluster settings and data configuration information for diagnostic or analytical purposes.

Diagnostic Items
----------------

:ref:`Table 1 <en-us_topic_0000001938377800__table522219045718>` lists the diagnostic items supported by Intelligent O&M.

.. _en-us_topic_0000001938377800__table522219045718:

.. table:: **Table 1** Diagnostic items

   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | No.                   | Diagnostic Item                                      | Description                                                                                                                                                                                                                                                                                           |
   +=======================+======================================================+=======================================================================================================================================================================================================================================================================================================+
   | 1                     | Data Node Disk Usage Check                           | Identify data nodes (including cold data nodes) with the highest disk usage in the cluster. Excessive disk usage can affect cluster stability.                                                                                                                                                        |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  High risk: When a node's disk usage reaches 85%, no new index replicas will be allocated to it.                                                                                                                                                                                                    |
   |                       |                                                      | -  Medium risk: When a node's disk usage exceeds 80%, take immediate action to prevent further increase.                                                                                                                                                                                              |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 2                     | Data Node Disk Usage Balance Check                   | Check whether disk usage is balanced across all regular data nodes and cold data nodes. Unbalanced disk usage may cause performance issues.                                                                                                                                                           |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  High risk: Maximum disk usage difference between nodes >= 40%                                                                                                                                                                                                                                      |
   |                       |                                                      | -  Medium risk: 25% <= Maximum disk usage difference between nodes < 40%                                                                                                                                                                                                                              |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 3                     | Large Index Shard Check                              | Check for large index shards that may cause cluster load imbalance.                                                                                                                                                                                                                                   |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  High risk: Shard storage >= 50 GB; and the index only has one primary shard.                                                                                                                                                                                                                       |
   |                       |                                                      | -  Medium risk: Shard storage >= 50 GB; and the number of shards is not divisible by the number of data nodes or cold data nodes.                                                                                                                                                                     |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 4                     | Cluster Node Configuration Check                     | Check the high availability settings of clusters.                                                                                                                                                                                                                                                     |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  Single/Dual Node Risk: For clusters without a dedicated Master node, at least three Data nodes (including cold data nodes) are required to ensure cluster availability during a single node failure.                                                                                               |
   |                       |                                                      | -  Overloaded Master Node Risk: When there are 10 or more Data nodes, dedicated Master nodes should be configured to prevent excessive load on the Master node.                                                                                                                                       |
   |                       |                                                      | -  Single Client Node Risk: A cluster containing only one dedicated Client node may result in cluster inaccessibility if that single Client node fails.                                                                                                                                               |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 5                     | Cluster Health Check                                 | Check the overall health status of all indices in the cluster.                                                                                                                                                                                                                                        |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  High risk (red): There are unallocated primary shards (i.e., some indices are unavailable).                                                                                                                                                                                                        |
   |                       |                                                      | -  Medium risk (yellow): Primary shards are properly allocated, but replicas are missing (compromised data availability).                                                                                                                                                                             |
   |                       |                                                      | -  Normal (green): All primary and replica shards are properly allocated.                                                                                                                                                                                                                             |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 6                     | Maximum Per-Node Shard Quantity Check                | Check that the number of shards allocated to each node remains within the limit set by cluster.max_shards_per_node, preventing shard allocation failures.                                                                                                                                             |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  High risk: Maximum number of shards allocated to a node >= 90% of the per-node shard limit                                                                                                                                                                                                         |
   |                       |                                                      | -  Medium risk: 85% of the per-node shard limit <= Maximum number of shards allocated to a node < 90% of the per-node shard limit                                                                                                                                                                     |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 7                     | Oversized Shard Check                                | Check for shards that have reached or exceeded 100 GB in the cluster. Oversized shards can increase query latency and slow down fault recovery. You are advised to keep the shard size under 50 GB.                                                                                                   |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  High risk: Maximum shard size >= 500 GB                                                                                                                                                                                                                                                            |
   |                       |                                                      | -  Medium risk: 100 GB <= Maximum shard size < 500 GB                                                                                                                                                                                                                                                 |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 8                     | Hot Index Read/Write Check (Every Minute)            | Identify the 10 indices with the most query and write requests within the last minute and display them in descending order. For each of these identified indices, verify that the number of its primary shards is divisible by the number of data nodes or cold data nodes to prevent load imbalance. |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 9                     | Node Disconnection Check                             | Check the connectivity of cluster nodes. Node disconnection will severely compromise cluster performance and therefore needs to be handled immediately.                                                                                                                                               |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 10                    | Balanced Node Connections Check                      | Check the number of connections to port 9200 on the client nodes (or data nodes if there are no client nodes), and display nodes by their connection count in descending order.                                                                                                                       |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 11                    | Client Connection Check (Source IP Address Analysis) | Check the number of connections to port 9200 on the client nodes (or data nodes if there are no client nodes), and display all external source IP addresses by connection count in descending order as well as details about the top 10 connections.                                                  |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 12                    | Node CPU Usage Check (Interval: 1 Minute)            | Measure the CPU usage of each node twice every minute, and calculate the average for each node to evaluate their load status.                                                                                                                                                                         |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  High risk: Average CPU usage >= 90% or no data is obtained.                                                                                                                                                                                                                                        |
   |                       |                                                      | -  Medium risk: 80% <= Average CPU usage < 90%                                                                                                                                                                                                                                                        |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 13                    | JVM Heap Memory Usage Check (Interval: 1 Minute)     | Measure the JVM heap memory usage of each node twice every minute, and calculate the average for each node to evaluate their load status.                                                                                                                                                             |
   |                       |                                                      |                                                                                                                                                                                                                                                                                                       |
   |                       |                                                      | -  High risk: Average JVM heap memory usage >= 90% or no data is obtained.                                                                                                                                                                                                                            |
   |                       |                                                      | -  Medium risk: 80% <= Average JVM heap memory usage < 90%                                                                                                                                                                                                                                            |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | 14                    | Local-Disk Cluster Index Replica Check               | For a cluster consisting of nodes that use local disks, check whether all indices have replicas. Otherwise, a single disk failure can lead to permanent data loss.                                                                                                                                    |
   +-----------------------+------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Scheduled Diagnostics
---------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Intelligent O&M > Intelligent Diagnostics**.

#. On the **Intelligent Diagnostics** page, click **Enable Scheduled Diagnostics**. In the displayed dialog box, configure a scheduled diagnostics task.

   .. table:: **Table 2** Enabling scheduled diagnostics

      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                             |
      +===================================+=========================================================================================================================================+
      | Diagnostic Type                   | Select a diagnostic type.                                                                                                               |
      |                                   |                                                                                                                                         |
      |                                   | -  **Full check**: All check items are supported. You can select all or only some of the check items.                                   |
      |                                   | -  **Cluster unavailability check**: When a cluster is unavailable, run this diagnosis to quickly diagnose its health status.           |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
      | Diagnostic Item                   | Select diagnostic items to be included in the scheduled task.                                                                           |
      |                                   |                                                                                                                                         |
      |                                   | -  When **Diagnostic Type** is set to **Full check**, you can customize the diagnostic items.                                           |
      |                                   | -  When **Diagnostic Type** is set to **Cluster unavailability check**, the cluster unavailability check items are selected by default. |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
      | Time Zone                         | Select your current time zone. The start time of the scheduled diagnostic task is affected by it.                                       |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
      | Diagnosed                         | Start time of the scheduled diagnostic task.                                                                                            |
      |                                   |                                                                                                                                         |
      |                                   | Diagnostics will run at the specified time every day.                                                                                   |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

#. Click **OK** to save the task information.

   The **Intelligent Diagnostics** page shows the newly created task.

   The report generated by the scheduled diagnostic task is displayed below or on the **Historical Reports** tab.

#. On the **Intelligent Diagnostics** page, manage the scheduled diagnostic task, including modifying and disabling it.

   -  Modify the scheduled diagnostic task: Click **Modify Settings**. In the displayed dialog box, modify the settings and click **OK** to update the scheduled diagnostic policy.
   -  Disable the scheduled diagnostic task: Click **Disable Scheduled Diagnostics**. In the displayed dialog box, click **OK** to disable scheduled diagnostics. The scheduled task is removed from the Intelligent Diagnostics page.

Manual Diagnostics
------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Intelligent O&M > Intelligent Diagnostics**.

#. On the **Intelligent Diagnostics** page, configure a diagnostic task and click **Run Diagnostics**.

   .. table:: **Table 3** Manual diagnostics

      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                             |
      +===================================+=========================================================================================================================================+
      | Diagnostic Type                   | Select a diagnostic type.                                                                                                               |
      |                                   |                                                                                                                                         |
      |                                   | -  **Full check**: All check items are supported. You can select all or only some of the check items.                                   |
      |                                   | -  **Cluster unavailability check**: When a cluster is unavailable, run this diagnosis to quickly diagnose its health status.           |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
      | Diagnostic Item                   | Select diagnostic items.                                                                                                                |
      |                                   |                                                                                                                                         |
      |                                   | -  When **Diagnostic Type** is set to **Full check**, you can customize the diagnostic items.                                           |
      |                                   | -  When **Diagnostic Type** is set to **Cluster unavailability check**, the cluster unavailability check items are selected by default. |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

#. Wait for 1 to 3 minutes. The diagnostic report will be displayed below.

   You can click **Export Report** to save the diagnostic report locally for analysis or archiving.

Viewing Historical Reports
--------------------------

The **Historical Reports** tab shows the most recent 10 reports of both scheduled and manual diagnostics.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Intelligent O&M > Historical Reports**.

#. Set **Created** to filter diagnostic reports by time range.

   You can click **Export Report** to save a historical report locally for analysis or long-term archiving.
