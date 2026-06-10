:original_name: css_01_0153.html

.. _css_01_0153:

Scaling In/Down
===============

If an Elasticsearch cluster has excess capacity due to off-peak traffic or reduced data volumes, you can reduce its nodes to optimize costs.

.. table:: **Table 1** Scaling scenarios

   +--------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------+
   | Type                     | Scenario                                           | Change Process                                                                         |
   +==========================+====================================================+========================================================================================+
   | Removing nodes randomly  | Randomly removes cluster nodes to optimize costs.  | #. Migrate the shards on the to-be-removed nodes to the remaining nodes.               |
   |                          |                                                    | #. After data migration, bring the nodes offline and modify the cluster configuration. |
   |                          |                                                    |                                                                                        |
   |                          |                                                    | Nodes are removed one at a time, so as to avoid interrupting services.                 |
   +--------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------+
   | Removing specified nodes | Removes specified cluster nodes to optimize costs. |                                                                                        |
   +--------------------------+----------------------------------------------------+----------------------------------------------------------------------------------------+

Impact on Billing
-----------------

For a pay-per-use cluster, you can see its new price when confirming the scale-in on the console. After the scale-in is complete, the cluster will be billed based on the new price.

.. _en-us_topic_0000001965416781__en-us_topic_0000001338349521_section12477125117522:

Constraints
-----------

-  During a scale-in operation, the data on the to-be-removed nodes needs to be migrated to the remaining nodes. The timeout for data migration per node is 48 hours. Scale-in will fail if this timeout expires.

-  When the cluster has large quantities of data, you are advised to manually adjust the data migration rate and avoid performing the migration during peak hours.

-  After a scale-in operation is complete, the cluster's disk usage must be lower than 80%.

-  Rules for scaling in a cluster that has no master nodes:

   -  Condition: Scale-in is allowed only when **the number of data nodes + the number of cold data nodes >= 3**.

   -  Maximum number of nodes that can be removed during a single scale-in operation: You cannot remove half or more of the cluster's current data nodes and cold data nodes.

      For example, if a cluster has three data nodes, three client nodes, and three cold data nodes, a maximum of two nodes can be removed at a time. Formula: (3+3)/2 = 3; and the number of nodes that can be removed should be less than 3, so the correct result is 2.

   -  Data reliability: After a scale-in operation, the total number of remaining data nodes and cold data nodes must be greater than the maximum number of index replicas in the cluster.

      For example, if the maximum number of replicas for all indexes in the cluster is 2, the total number of data nodes and cold data nodes after the scale-in must be at least 3.

-  Rules for scaling in a cluster that has master nodes:

   -  Non-master nodes (data nodes, client nodes, or cold data nodes): For each node type, the number of nodes must be at least 2 before you can proceed with a scale-in operation.

   -  Master nodes: For a single scale-in operation, you can only remove less than half of the master nodes.

      For example, if a cluster has two data nodes and five master nodes, only two master nodes can be removed for the current scale-in operation. Formula: 5/2 = 2.5; and the number of nodes that can be removed should be less than 2.5, so the correct result is 2.

-  Rules for removing nodes from a multi-AZ cluster:

   -  Even distribution: After a scale-in operation, the difference in the number of same-type nodes across different AZs must not exceed 1.
   -  Minimum number of nodes required to maintain high availability:

      -  **For a two-AZ cluster**, there must be at least four data nodes (or cold data nodes), two for each AZ; and there must be at least two client nodes (if configured), one for each AZ.
      -  **For a three-AZ cluster**, each available node type must have at least one node in each AZ. This means each node type must have at least three nodes in total.

   -  Performance enhancement: To prevent uneven data distribution and ensure optimal query and ingestion performance, the number of data nodes or cold data nodes should be an integer multiple of the number of AZs.

-  For the range of node quantities supported by each node type, see :ref:`Table 2 <en-us_topic_0000001965416781__table02900138572>`.

   .. _en-us_topic_0000001965416781__table02900138572:

   .. table:: **Table 2** Node quantity ranges

      +-----------------------------------+---------------------------------------------------+
      | Node Type                         | Value Range                                       |
      +===================================+===================================================+
      | Data nodes                        | -  Without master nodes: 1 to 32                  |
      |                                   | -  With master nodes: 1 to 200                    |
      +-----------------------------------+---------------------------------------------------+
      | Master nodes                      | 3, 5, 7, or 9 (must be an odd number from 3 to 9) |
      +-----------------------------------+---------------------------------------------------+
      | Client nodes                      | 1~64                                              |
      +-----------------------------------+---------------------------------------------------+
      | Cold data nodes                   | 1-32                                              |
      +-----------------------------------+---------------------------------------------------+

Change Impact
-------------

Before the change, learn about possible impacts and operation suggestions, and develop a plan to minimize these impacts.

-  Impact on performance

   During a scale-in, shards on the to-be-removed nodes are migrated to the remaining nodes. This process will consume I/O performance. This is why you are advised to perform the operation during off-peak hours.

   To minimize this impact, it is advisable to adjust the data migration rate based on the cluster's traffic cycle: increase the data migration rate during off-peak hours to shorten the task duration, and decrease it **before** peak hours arrive to ensure optimal cluster performance. The data migration rate is determined by the **indices.recovery.max_bytes_per_sec** parameter. The default value of this parameter is the number of vCPUs multiplied by 8 MB. For example, for four vCPUs, the data migration rate is 32 MB/s. You can adjust it based on the service requirements.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "transient": {
          "indices.recovery.max_bytes_per_sec": "128MB"
        }
      }

-  Impact on cluster load

   After a scale-in, the remaining nodes will need to handle all of the cluster's load. This may lead to higher CPU, memory, and disk I/O usage, impacting query and ingestion performance. If shards are unevenly allocated, performance bottlenecks may occur. This is why before a scale-in, it is necessary to evaluate whether the remaining nodes have the capacity to handle the current cluster load.

-  Characteristics of this process

   Once started, a scaling task cannot be stopped until it succeeds or fails.

Scale-in Duration
-----------------

The following formula can be used to estimate how long a scale-in operation will take:

**Scale-in duration (min) = 5 (min) x Number of nodes to be removed + Data migration duration (min)**

where, 5 minutes indicates how long non-data migration operations (e.g., initialization) typically take per node. It is an empirical value.

**Data migration duration (min) = Total data size of the nodes to be removed (MB) ÷ [Total number of vCPUs of the data nodes x 8 (MB/s) x 60 (s)]**

where,

-  8 MB/s indicates that each vCPU can process 8 MB of data per second. It is an empirical value.
-  The formulas above use estimates under ideal conditions. The actual migration speed depends on cluster load.

Prerequisites
-------------

-  The cluster status is **Available**, and there are no ongoing tasks.
-  All mission-critical data has been backed up. For details, see :ref:`Creating Snapshots to Back Up Data <css_01_0267>`.

Removing Nodes Randomly
-----------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.
#. In the cluster list, find the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.
#. Click the **Scale Cluster** tab.
#. Click **Scale in** to set parameters.

   .. table:: **Table 3** Removing nodes randomly

      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                              |
      +===================================+==========================================================================================================================================================================+
      | Action                            | Select **Scale in**.                                                                                                                                                     |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Resources                         | Quantities of resources reduced.                                                                                                                                         |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Nodes                             | Reduce the number of nodes in the **Nodes** column. You can change multiple node types at the same time.                                                                 |
      |                                   |                                                                                                                                                                          |
      |                                   | For the range of node quantities supported by each node type, see :ref:`Constraints <en-us_topic_0000001965416781__en-us_topic_0000001338349521_section12477125117522>`. |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to go back to the **Clusters** page. **Task Status** is **Scaling in**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled in.

Removing Specified Nodes
------------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, find the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.

#. On the **Modify Configuration** page, click the **Scale In Nodes** tab.

#. Set scale-in parameters.

   .. table:: **Table 4** Removing specified nodes (Scale In Nodes)

      +-----------+-------------------------------------------------------------------------------------------------------------+
      | Parameter | Description                                                                                                 |
      +===========+=============================================================================================================+
      | Node Type | Expand the node type that needs be changed to show all nodes under it. Select the nodes you want to remove. |
      +-----------+-------------------------------------------------------------------------------------------------------------+

#. Click **Next**.

#. Confirm the change information and click **Submit**. In the confirm dialog box, choose to migrate data, which helps to prevent data loss, and click **OK**.

   During data migration, the system migrates all data from the to-be-removed nodes to the remaining nodes, and removes these nodes upon completion of the data migration. If the data on the to-be-removed nodes has replicas on other nodes, data migration can be skipped and the cluster change can be completed faster.

#. Click **Back to Cluster List** to go back to the **Clusters** page. **Task Status** is **Scaling in**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled in.

Related Documents
-----------------

-  For an Elasticsearch cluster, you can also optimize costs by changing node specifications and EVS disk types. For details, see :ref:`Changing Node Specifications <css_01_0245>`.
-  If you want to reduce cluster nodes even though your cluster is not eligible for a scale-in operation, you can simply create a new cluster. Then you can migrate data to the new cluster using snapshots, and delete the old cluster after data is migrated.
