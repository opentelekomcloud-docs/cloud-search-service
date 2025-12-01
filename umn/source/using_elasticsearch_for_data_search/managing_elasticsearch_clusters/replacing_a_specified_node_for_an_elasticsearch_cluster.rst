:original_name: css_01_0156.html

.. _css_01_0156:

Replacing a Specified Node for an Elasticsearch Cluster
=======================================================

If a node in an Elasticsearch cluster is faulty, you can replace it to restore services.

The node replacement process is as follows:

#. Migrate data from the node that needs to be replaced to other available nodes.
#. Rebuild a new node using this node's current ID, IP address, specifications, and AZ.
#. Add the new node into the cluster. The system automatically triggers a shard reallocation, migrating some of the shards to the new node.

This process does not interrupt services because data is migrated from the replaced node to other available nodes.

Constraints
-----------

-  Only one node can be replaced at a time. Each new node is rebuilt using the ID, IP address, specifications, and AZ of the node it is replacing.
-  The configurations you modified manually will not be retained after node replacement. For example, if you have manually added a return route for the original node, you need to add it again for the new node after the node replacement is complete.
-  If the node you want to replace is a data node or cold data node, pay attention to the following precautions:

   -  When a data node or cold data node is replaced, its data is first migrated to other data nodes. This means the **total number of data nodes and cold data nodes must be greater than the maximum number of index replicas plus 1**.
   -  Elasticsearch clusters whose version is earlier than 7.6.2 cannot have closed indexes. Otherwise, their data nodes or cold data nodes cannot be replaced.
   -  In the AZ that contains the data node or cold data node to be replaced, there has to be at least another data node or cold data node.
   -  If the cluster has not master nodes, the total number of data nodes plus cold data nodes must be at least three.
   -  The precautions above do not apply if you are replacing a faulty node, regardless of its type. This is because faulty nodes are not included in **\_cat/nodes**.

Change Impact
-------------

Before replacing a node, it is essential to assess the potential impacts and review operational recommendations. This enables proper scheduling of the node replacement, minimizing service interruptions.

-  Impact on performance

   Replacing a node does not interrupt services. However, data migration that occurs during this process consumes I/O performance, and taking individual nodes offline still has some impact on the overall cluster performance.

   To minimize this impact, it is advisable to adjust the data migration rate based on the cluster's traffic cycle: increase the data migration rate during off-peak hours to shorten the task duration, and decrease it **before** peak hours arrive to ensure optimal cluster performance. The data migration rate is determined by the **indices.recovery.max_bytes_per_sec** parameter. The default value of this parameter is the number of vCPUs multiplied by 32 MB. For example, for four vCPUs, the data migration rate is 128 MB. Set this parameter to a value between 40 MB and 1000 MB based on your service requirements.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "transient": {
          "indices.recovery.max_bytes_per_sec": "1000MB"
        }
      }

-  Impact on request handling

   While a node is being replaced, requests sent to it may fail. To mitigate this impact, the following measures may be taken:

   -  Use a VPC endpoint or a dedicated load balancer to handle access requests to your cluster, which makes sure that requests are automatically routed to available nodes.
   -  Enable an exponential backoff & retry mechanism on the client (configure three retries).
   -  Perform this operation during off-peak hours.

-  Characteristics of this process

   Once started, a node replacement task cannot be stopped until it succeeds or fails. A task failure only impacts a single node, and does not interrupt services if there are data replicas, but the failed node still needs to be restored promptly.

Node Replacement Duration
-------------------------

The following formula can be used to estimate how long it will take to replace a specified node of a cluster:

**Change duration (min) = 15 (min) + Data migration duration (min)**

where, 15 minutes indicates how long non-data migration operations (e.g., initialization) typically take per node. It is an empirical value.

**Data migration duration (min) = Total data size (MB)/[Total number of vCPUs of the data nodes x 32 (MB/s) x 60 (s)]**

where,

-  32 MB/s indicates that each vCPU can process 32 MB of data per second. It is an empirical value.
-  The formulas above use estimates under ideal conditions. The actual migration speed depends on cluster load.

Prerequisites
-------------

-  The cluster status is **Available**, and there are no ongoing tasks.
-  All mission-critical data has been backed up. For details, see :ref:`Creating Snapshots to Back Up the Data of an Elasticsearch Cluster <css_01_0267>`.

Replacing a Specified Node
--------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.
#. In the cluster list, find the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.
#. On the **Modify Configuration** page, click the **Replace Node** tab.
#. On the **Replace Node** tab, set the parameters as needed.

   .. table:: **Table 1** Replacing a specified node

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                               |
      +===================================+===========================================================================================================================================================================+
      | Whether to perform data migration | Selecting this option means data migration will be performed. If the target node has disabled indexes or has indexes that have no replicas, this option must be selected. |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Node Type                         | Select the node you want to replace. You can expand a node type to check all the nodes under it.                                                                          |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Submit**.
#. Click **Back to Cluster List** to go back to the **Clusters** page. The **Task Status** is **Replacing nodes**. When **Cluster Status** changes to **Available**, the node has been successfully replaced.
