:original_name: css_01_0074.html

.. _css_01_0074:

Changing Specifications
=======================

If the workloads on the data plane of a cluster change, you can change its node specifications as needed.

Prerequisites
-------------

-  The target cluster is available and has no tasks in progress.
-  The target cluster has sufficient quotas available.

Constraints
-----------

-  The node number and storage capacity cannot be modified when you change the node specifications.

-  The specifications can only be increased. To decrease cluster specifications, create a cluster with smaller specifications and migrate the data from the current cluster to it.

-  If a cluster has multiple node types, you can change the specifications of only one type at a time. After the change, nodes in other types still maintain their original specifications.

-  If the data volume is large, it may take long to modify the node specifications. You are advised to modify specifications during off-peak hours.

-  Kibana is unavailable during specification change.

-  When changing the node specifications, ensure that all service data has copies so the services will not be interrupted.

   Run the **GET \_cat/indices?v** command in Kibana. If the returned **rep** value is greater than **0**, the data has copies. If the returned **rep** value is **0**, the data has no copies. In this case, create snapshot for the cluster by referring to :ref:`Manually Creating a Snapshot <css_01_0033__section43906502025>`.

-  During the specification modification, the nodes are stopped and restarted in sequence. It is a rolling process.

Procedure
---------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters**. On the displayed **Clusters** page, locate the target cluster and choose **More** > **Scale Cluster** in the **Operation** column.
#. On the **Modify Configuration** page, set parameters to change specifications.

   -  **New Node Specifications** The specifications of the default data nodes. Select the specifications from the drop-down list as required.
   -  If a cluster has master nodes, client nodes, or cold data nodes, you can change their specifications.

#. Click **Next: Scale Now**.
#. Confirm the information and click **Submit**.
#. In the displayed **Verify Index Copy** dialog box, select **Verify index copies** if you need. Click **OK**.

   -  If you selected **Verify index copies** and the cluster has no master node, indexes must have at least one copy and the cluster must have at least three nodes.
   -  If you selected **Verify index copies** and the cluster has no master node, indexes must have at least one copy.

#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Cluster Status** is **Configuration modified**. When **Cluster Status** changes to **Available**, the cluster specifications have been successfully modified.
