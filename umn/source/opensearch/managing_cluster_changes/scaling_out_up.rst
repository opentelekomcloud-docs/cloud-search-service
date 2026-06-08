:original_name: css_01_0304.html

.. _css_01_0304:

Scaling Out/Up
==============

If an OpenSearch cluster struggles to maintain performance in the face of rapid data growth or sustained high memory usage, you may scale it horizontally by adding more nodes and more node types, or do so vertically by increasing the storage capacity of existing nodes.

.. table:: **Table 1** Scaling scenarios

   +----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Type                             | Scenario                                                                                                                                                                                                                                                                    | Change Process                                                                                                                                                                                                                            |
   +==================================+=============================================================================================================================================================================================================================================================================+===========================================================================================================================================================================================================================================+
   | Adding new nodes                 | If a cluster experiences rapid data growth or sustained high memory usage, you may add more nodes to it to improve cluster availability.                                                                                                                                    | Procedure for adding data nodes or cold data nodes:                                                                                                                                                                                       |
   |                                  |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                           |
   |                                  |                                                                                                                                                                                                                                                                             | #. New nodes are added and cluster configuration is modified.                                                                                                                                                                             |
   |                                  |                                                                                                                                                                                                                                                                             | #. A shard redistribution is automatically triggered to reallocate certain shards to newly added nodes.                                                                                                                                   |
   |                                  |                                                                                                                                                                                                                                                                             | #. After the redistribution is complete, the new nodes start to handle query and indexing requests.                                                                                                                                       |
   |                                  |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                           |
   |                                  |                                                                                                                                                                                                                                                                             | Adding master or client nodes does not trigger data migration.                                                                                                                                                                            |
   |                                  |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                           |
   |                                  |                                                                                                                                                                                                                                                                             | During the capacity expansion, the system ensures that each shard has at least one available replica to ensure service continuity.                                                                                                        |
   +----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Adding master nodes              | As your cluster's data volume grows, you can improve its stability and reliability by adding dedicated master nodes for more effective cluster node management.                                                                                                             | Procedure for adding a new node type: Add new nodes and modify cluster configuration. Adding master nodes does not trigger data migration, and therefore does not interrupt services.                                                     |
   +----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Adding client nodes              | To handle increased query and write loads as your cluster's data volume grows, you can add dedicated client nodes. This offloads request processing from your data nodes, improving overall cluster scalability.                                                            | Procedure for adding a new node type: Add new nodes and modify cluster configuration. Adding client nodes does not trigger data migration, and therefore does not interrupt services.                                                     |
   |                                  |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                           |
   |                                  |                                                                                                                                                                                                                                                                             | However, when client nodes are added, the cluster's address changes from the data node address to the client node address. You must update the client configuration to use this new address. Otherwise, the client nodes cannot function. |
   +----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Adding cold data nodes           | As your cluster's data volume keeps growing, you may have large quantities of historical data that is infrequently accessed but still useful for analytical purposes. To optimize both storage costs and query performance, you can add cold data nodes to store such data. | Procedure for adding a new node type: Add new nodes and modify cluster configuration. Adding cold data nodes does not trigger data migration, and therefore does not interrupt services.                                                  |
   +----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Increasing node storage capacity | -  If a cluster experiences rapid data growth and its storage capacity becomes insufficient, you can expand the cluster nodes' storage capacity.                                                                                                                            | #. A request is sent to the EVS service to expand the disk capacities for all cluster nodes.                                                                                                                                              |
   |                                  | -  If the disk usage of a cluster remains high, you can expand the cluster nodes' storage capacity.                                                                                                                                                                         | #. After disk capacity is expanded by EVS, the size of existing disk volumes is expanded on all cluster nodes.                                                                                                                            |
   |                                  |                                                                                                                                                                                                                                                                             |                                                                                                                                                                                                                                           |
   |                                  |                                                                                                                                                                                                                                                                             | The disk capacity expansion will not interrupt ongoing services.                                                                                                                                                                          |
   +----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Impact on Billing
-----------------

For a pay-per-use cluster, you can see its new price when confirming the scale-out or scale-up on the console. After the change is complete, the cluster will be billed based on the new price.

.. _en-us_topic_0000001955726526__en-us_topic_0000001938218180_en-us_topic_0000001285669680_section12477125117522:

Constraints
-----------

-  The node storage capacity of a cluster can only be increased—not decreased. Select an appropriate node storage capacity based on the data volume and projected data growth.

-  The storage capacity of the master and client nodes in a cluster cannot be expanded.

-  The storage capacity of data nodes that use local disks cannot be expanded.

-  For a multi-AZ cluster, the total number of client nodes must be greater than or equal to the number of AZs. (For a cluster spanning two AZs, this means a minimum of two client nodes; for a three-AZ deployment, a minimum of three client nodes.)

-  Principles for adding cold data nodes to a multi-AZ cluster:

   -  Node quantity requirement: A two-AZ cluster **must** have at least four cold data nodes (two in each AZ); and a three-AZ cluster **must** have at least three cold data nodes (one in each AZ).
   -  Performance enhancement: To prevent uneven data distribution and ensure optimal query and ingestion performance, the number of cold data nodes should be an integer multiple of the number of AZs.

-  For the range of node quantities supported by each node type, see :ref:`Table 2 <en-us_topic_0000001955726526__en-us_topic_0000001938218180_en-us_topic_0000001285669680_table10730243193816>`.

   .. _en-us_topic_0000001955726526__en-us_topic_0000001938218180_en-us_topic_0000001285669680_table10730243193816:

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

Expanding the storage capacity of cluster nodes (vertical scaling) does not impact services, whereas adding new nodes or new node types (horizontal scaling) may have the following impacts:

-  Impact on performance

   Adding new nodes does not interrupt services. However, after new nodes are added, data shards need to be redistributed to these nodes to balance the load, and this process will consume I/O performance. This is why you are advised to perform the operation during off-peak hours.

   To minimize this impact, it is advisable to adjust the data migration rate based on the cluster's traffic cycle: increase the data migration rate during off-peak hours to shorten the task duration, and decrease it **before** peak hours arrive to ensure optimal cluster performance. The data migration rate is determined by the **indices.recovery.max_bytes_per_sec** parameter. The default value of this parameter is the number of vCPUs multiplied by 8 MB. For example, for four vCPUs, the data migration rate is 32 MB/s. You can adjust it based on the service requirements.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "transient": {
          "indices.recovery.max_bytes_per_sec": "128MB"
        }
      }

-  Characteristics of this process

   Once started, a scaling task cannot be stopped until it succeeds or fails.

Duration
--------

-  It takes 10 to 30 minutes to add new nodes or new node types (horizontal scaling), depending on the cluster's scheduling capabilities.
-  It takes 10 to 15 minutes to expand the storage capacity of cluster nodes (vertical scaling).

Prerequisites
-------------

-  The cluster status is **Available**, and there are no ongoing tasks.
-  Your CSS resource quotas are sufficient for the capacity expansion you are about to perform. You can check available resources on the **Modify Configuration** page.

Adding More Nodes or Increasing Node Storage Capacity
-----------------------------------------------------

If a cluster experiences rapid data growth or sustained high memory usage, you may add more nodes to it or increase the cluster nodes' storage capacity. This helps to improve service and data availability and durability.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, find the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.
#. Click the **Scale Cluster** tab.
#. Set the necessary parameters.

   .. table:: **Table 3** Adding more nodes or increasing node storage capacity

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                              |
      +===================================+==========================================================================================================================================================================================================+
      | Action                            | Select **Scale out**.                                                                                                                                                                                    |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Resources                         | Quantities of resources added.                                                                                                                                                                           |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Nodes                             | Increase the number of nodes and node storage capacity in the **Nodes** and **Node Storage Type** columns. You can change multiple node types at the same time.                                          |
      |                                   |                                                                                                                                                                                                          |
      |                                   | -  For the range of node quantities supported by each node type, see :ref:`Constraints <en-us_topic_0000001955726526__en-us_topic_0000001938218180_en-us_topic_0000001285669680_section12477125117522>`. |
      |                                   | -  The value range of node storage capacity is determined by the node flavor you select. The value must be divisible by 20.                                                                              |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to go back to the **Clusters** page. The **Task Status** is **Scaling out**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled out.

.. _en-us_topic_0000001955726526__en-us_topic_0000001938218180_section1195734814511:

Adding New Node Types
---------------------

For a cluster that has no dedicated master, client, or cold data nodes, as the load on its data plane increases, you may dynamically add such nodes to it to share the load of the data nodes.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.

#. Click the **Add Node Types** tab.

   If a cluster already has dedicated master, client, and cold data nodes, the **Add Node Types** tab is unavailable.

#. On the **Add Node Types** tab, configure the nodes.

   .. table:: **Table 4** Adding new node types

      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                     |
      +===================================+=================================================================================================================================================================================================================+
      | Node types                        | Select the type of nodes you want to add.                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                 |
      |                                   | -  Only the node types that the cluster does not already have are displayed. For example, if the cluster already has dedicated master nodes, only **Client Node** and **Cold Data Node** are displayed.         |
      |                                   | -  Only one node type can be added at a time. For example, if you need to add both master and client nodes, you need to perform this task twice.                                                                |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Node Specifications               | Select node specifications based on site requirements.                                                                                                                                                          |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Nodes                             | Set the number of nodes to add for this node type. For the value range, see :ref:`Constraints <en-us_topic_0000001955726526__en-us_topic_0000001938218180_en-us_topic_0000001285669680_section12477125117522>`. |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Node Storage Type                 | Set the node storage type.                                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                 |
      |                                   | The storage capacity per master or client node is fixed to 40 GB.                                                                                                                                               |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Next**.

#. Confirm the information and click **Submit**.

   Return to the cluster list page. The **Task Status** of the cluster is **Scaling out**. When **Cluster Status** changes to **Available**, nodes have been added successfully.

   -  When adding client nodes, you can choose whether to restart data nodes and cold data nodes and bring the Cerebro and OpenSearch Dashboards processes offline after **Cluster Status** changes to **Available**. This helps avoid conflicts.
   -  When adding cold data nodes, you must restart data nodes to activate the hot tag after **Cluster Status** changes to **Available**. This ensures that the cold data nodes function properly. After cold data nodes are added, manually migrate historical data to them. For details, see :ref:`Switching Between Hot and Cold Data <css_01_0200>`.

   For details about the restart operation, see :ref:`Restarting a Cluster <css_01_0286>`.

Related Documents
-----------------

-  You can also upgrade the node specifications and change the EVS disk type of an OpenSearch cluster. For details, see :ref:`Changing Node Specifications <css_01_0246>`.
-  During a capacity expansion, if the resources in an AZ become insufficient, you can migrate the nodes in this AZ to another that has sufficient resources, and then perform the capacity expansion in the new AZ. For details, see :ref:`Switching AZs <css_01_0311>`.
