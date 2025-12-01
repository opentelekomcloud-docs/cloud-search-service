:original_name: css_01_0304.html

.. _css_01_0304:

Scaling Out/Up an OpenSearch Cluster
====================================

If an OpenSearch cluster struggles to maintain performance in the face of rapid data growth or sustained high memory usage, you may scale it horizontally by adding more nodes and more node types, or do so vertically by increasing the storage capacity of existing nodes.

.. table:: **Table 1** Scaling scenarios

   +----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Type                             | Scenario                                                                                                                                                                 | Change Process                                                                                                                                                                                                                   |
   +==================================+==========================================================================================================================================================================+==================================================================================================================================================================================================================================+
   | Adding new nodes                 | If a cluster experiences rapid data growth or sustained high memory usage, you may add more nodes to it to improve cluster availability.                                 | Procedure for adding data nodes or cold data nodes:                                                                                                                                                                              |
   |                                  |                                                                                                                                                                          |                                                                                                                                                                                                                                  |
   |                                  |                                                                                                                                                                          | #. New nodes are added and cluster configuration is modified.                                                                                                                                                                    |
   |                                  |                                                                                                                                                                          | #. A shard redistribution is automatically triggered to reallocate certain shards to newly added nodes.                                                                                                                          |
   |                                  |                                                                                                                                                                          | #. After the redistribution is complete, the new nodes start to handle query and indexing requests.                                                                                                                              |
   |                                  |                                                                                                                                                                          |                                                                                                                                                                                                                                  |
   |                                  |                                                                                                                                                                          | Adding master or client nodes does not trigger data migration.                                                                                                                                                                   |
   |                                  |                                                                                                                                                                          |                                                                                                                                                                                                                                  |
   |                                  |                                                                                                                                                                          | During the capacity expansion, the system ensures that each shard has at least one available replica to ensure service continuity.                                                                                               |
   +----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Adding new node types            | For a cluster that has no master or client nodes, as the load on its data plane increases, you may add master or client nodes to it to share the load of the data nodes. | Procedure for adding a new node type: New nodes are added and cluster configuration is modified. Adding master or client nodes does not trigger data migration, and therefore does not interrupt services.                       |
   |                                  |                                                                                                                                                                          |                                                                                                                                                                                                                                  |
   |                                  |                                                                                                                                                                          | When client nodes are added, the cluster's address changes from the data node address to the client node address. You must update the client configuration to use this new address. Otherwise, the client nodes cannot function. |
   +----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Increasing node storage capacity | -  If a cluster experiences rapid data growth and its storage capacity becomes insufficient, you can expand the cluster nodes' storage capacity.                         | #. A request is sent to the EVS service to expand the disk capacities for all cluster nodes.                                                                                                                                     |
   |                                  | -  If the disk usage of a cluster remains high, you can expand the cluster nodes' storage capacity.                                                                      | #. After disk capacity is expanded by EVS, the size of existing disk volumes is expanded on all cluster nodes.                                                                                                                   |
   |                                  |                                                                                                                                                                          |                                                                                                                                                                                                                                  |
   |                                  |                                                                                                                                                                          | The disk capacity expansion will not interrupt ongoing services.                                                                                                                                                                 |
   +----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Impact on Billing
-----------------

For a pay-per-use cluster, you can see its new price when confirming the scale-out or scale-up on the console. After the scale-out or scale-up is complete, the new price will apply. For pricing details, see .

.. _en-us_topic_0000001955726526__en-us_topic_0000001938218180_en-us_topic_0000001285669680_section12477125117522:

Constraints
-----------

-  The node storage capacity of a cluster can only be increased—not decreased. Select an appropriate node storage capacity based on the data volume and projected data growth.

-  The storage capacity of the master and client nodes in a cluster cannot be expanded.

-  The storage capacity of data nodes that use local disks cannot be expanded.

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
      | Client nodes                      | 1-32                                              |
      +-----------------------------------+---------------------------------------------------+
      | Cold data nodes                   | 1-32                                              |
      +-----------------------------------+---------------------------------------------------+

Change Impact
-------------

Before the change, learn about possible impacts and operation suggestions, and develop a plan to minimize these impacts.

Expanding the storage capacity of cluster nodes (vertical scaling) does not impact services, whereas adding new nodes or new node types (horizontal scaling) may have the following impacts:

-  Impact on performance

   Adding new nodes does not interrupt services. However, after new nodes are added, data shards need to be redistributed to these nodes to balance the load, and this process will consume I/O performance. This is why you are advised to perform the operation during off-peak hours.

   To minimize this impact, it is advisable to adjust the data migration rate based on the cluster's traffic cycle: increase the data migration rate during off-peak hours to shorten the task duration, and decrease it **before** peak hours arrive to ensure optimal cluster performance. The data migration rate is determined by the **indices.recovery.max_bytes_per_sec** parameter. The default value of this parameter is the number of vCPUs multiplied by 32 MB. For example, for four vCPUs, the data migration rate is 128 MB. Set this parameter to a value between 40 MB and 1000 MB based on your service requirements.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "transient": {
          "indices.recovery.max_bytes_per_sec": "1000MB"
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

Adding New Node Types
---------------------

For a cluster that has no master or client nodes, as the load on its data plane increases, you may add master or client nodes to it to share the load of the data nodes.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.

#. On the **Modify Configuration** page, choose the **Add Master/Client Nodes** tab.

   If a cluster already has both master and client nodes, the **Add Master/Client Nodes** tab is unavailable.

#. On the Add Master/Client Nodes tab, configure the nodes.

   .. table:: **Table 4** Adding master or client nodes

      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                     |
      +===================================+=================================================================================================================================================================================================================+
      | Node types                        | Select the type of nodes you want to add.                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                 |
      |                                   | -  Only one node type can be selected at a time. If you need to add both Master and Client nodes, you need to perform this task twice.                                                                          |
      |                                   | -  If the cluster already has Master or Client nodes, only the other node type is displayed here.                                                                                                               |
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

   Return to the cluster list page. The **Task Status** of the cluster is **Scaling out**.

   -  If you added master nodes, you can tell they are added successfully when **Cluster Status** changes to **Available**.
   -  This is also true with client nodes. You can restart data nodes and cold data nodes to stop Cerebro and OpenSearch Dashboards processes on them.

Related Documents
-----------------

-  You can also upgrade the node specifications and change the EVS disk type of an OpenSearch cluster. For details, see :ref:`Changing the Node Specifications of an OpenSearch Cluster <css_01_0246>`.
-  During a capacity expansion, if the resources in an AZ become insufficient, you can migrate the nodes in this AZ to another that has sufficient resources, and then perform the capacity expansion in the new AZ. For details, see :ref:`Switching AZs for an OpenSearch Cluster <css_01_0311>`.
