:original_name: en-us_topic_0000001477739368.html

.. _en-us_topic_0000001477739368:

Changing Specifications
=======================

If the workloads on the data plane of a cluster change, you can change its node specifications as needed.

Prerequisites
-------------

-  The target cluster is available and has no tasks in progress.

-  The target cluster has sufficient quotas available.

-  When changing the node specifications, ensure that all service data has copies so the services will not be interrupted.

   Run the **GET \_cat/indices?v** command in Kibana. If the returned **rep** value is greater than **0**, the data has copies. If the returned **rep** value is **0**, the data has no copies. In this case, create snapshot for the cluster by referring to :ref:`Manually Creating a Snapshot <en-us_topic_0000001633220693>`.

-  If the data volume is large, it may take long to modify the node specifications. You are advised to modify specifications during off-peak hours.

Constraints
-----------

-  The number of nodes and the capacity of node storage cannot be changed. You can add nodes and increase the node storage capacity by referring to :ref:`Scaling Out a Cluster <en-us_topic_0000001477899164>`. For details about how to reduce the number of nodes, see :ref:`Scaling in a Cluster <en-us_topic_0000001528299597>`.
-  After decreasing cluster specifications, the cluster performance will deteriorate and service capabilities will be affected. Exercise caution when performing this operation.
-  If a cluster has multiple node types, you can change the specifications of only one type at a time. After the change, nodes in other types still maintain their original specifications.
-  Kibana is unavailable during specification change.
-  During the specification modification, the nodes are stopped and restarted in sequence. It is a rolling process.

Procedure
---------

#. Log in to the CSS management console.

#. In the navigation pane, choose a cluster type. The cluster management page is displayed.

#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.

#. On the **Modify Configuration** page, choose the **Scale Cluster** tab and click **Change Specifications** to set parameters.

   -  **Action**: select **Change specifications**.
   -  **Resources**: The changed amount of resources.
   -  **Nodes**: Specifications of the default data nodes. Select the required specifications from the **Node Specifications** drop-down list and select the node that you want to change the specifications.
   -  If a cluster has master nodes, client nodes, or cold data nodes, you can change their specifications.

#. Click **Next**.

#. Confirm the information and click **Submit**.

#. In the dialog box that is displayed, confirm whether to select **Verify index copies** and **Cluster status check** and click **OK** to start the specifications change.

   Index copy verification:

   By default, CSS checks for indexes that do not have copies. You can skip this step, but the lack of index copies may affect services during a cluster specifications change.

   -  If you selected **Verify index copies** and the cluster has no master node, indexes must have at least one copy and the cluster must have at least three nodes.
   -  If you selected **Verify index copies** and the cluster has no master node, indexes must have at least one copy.

   Cluster status check:

   The cluster status is checked before the specifications change by default. The specifications of nodes are changed one by one to ensure success and data security. If a cluster is overloaded and services are faulty, the request for a specifications change will not be delivered. In this case, you can disable cluster status check. If you ignore the cluster status check before the specifications change, the cluster may be faulty and services may be interrupted. Exercise caution when performing this operation.

#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Cluster Status** is **Configuration modified**. When **Cluster Status** changes to **Available**, the cluster specifications have been successfully modified.
