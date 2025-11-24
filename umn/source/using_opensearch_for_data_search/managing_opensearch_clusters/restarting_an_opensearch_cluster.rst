:original_name: css_01_0286.html

.. _css_01_0286:

Restarting an OpenSearch Cluster
================================

If an OpenSearch cluster has stopped working, you can try to recover it by restarting it. Two restart options are available: quick restart and rolling restart. You are advised to perform the restart during off-peak hours.

Constraints
-----------

-  Avoid restarting a cluster during peak hours, as doing so may impact data integrity and service availability.
-  During a quick restart, the cluster is unavailable for the entire duration of the restart.
-  Rolling restart is supported only for clusters with three or more nodes, including the master node, client node, and cold data nodes. During a rolling restart, only the nodes that are being restarted are unavailable. When the cluster stores a large amount of data, the restart may take a long time.

Prerequisites
-------------

-  The cluster you want to restart is not frozen and has no task in progress.
-  The cluster is available and is not processing any service requests, such as importing and searching for data. Otherwise, data loss may occur during a cluster restart.

Quick Restart
-------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and choose **More > Restart** in the **Operation** column.

#. On the **Restart Cluster** page, set parameters.

   .. table:: **Table 1** Configuring a quick restart

      +-----------------------------------+------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                              |
      +===================================+==========================================================================================+
      | Restart Mode                      | Select **Quick Restart**.                                                                |
      |                                   |                                                                                          |
      |                                   | .. warning::                                                                             |
      |                                   |                                                                                          |
      |                                   |    The cluster will be unavailable for the entire duration of a quick restart.           |
      +-----------------------------------+------------------------------------------------------------------------------------------+
      | Select By                         | Select **Node type** or **Node name**.                                                   |
      |                                   |                                                                                          |
      |                                   | -  **Node type**: You can select multiple node types to restart them at the same time.   |
      |                                   | -  **Node name**: You can restart only one node at a time.                               |
      +-----------------------------------+------------------------------------------------------------------------------------------+
      | Value                             | Select one or more node types or a node name, depending on the setting of **Select By**. |
      |                                   |                                                                                          |
      |                                   | Values for **Node type**:                                                                |
      |                                   |                                                                                          |
      |                                   | -  **ess**: data node                                                                    |
      |                                   | -  **ess-master**: master node                                                           |
      |                                   | -  **ess-client**: client node                                                           |
      |                                   | -  **ess-cold**: cold data node                                                          |
      +-----------------------------------+------------------------------------------------------------------------------------------+

#. Click **OK** to start the restart task.

   Refresh the page and check the cluster status. During the restart, the cluster status is **Processing**, and the task status is **Restarting**. When the cluster status changes to **Available**, the cluster has restarted successfully.

Rolling Restart
---------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and choose **More > Restart** in the **Operation** column.

#. On the **Restart Cluster** page, set parameters.

   .. table:: **Table 2** Configuring a rolling restart

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                              |
      +===================================+==========================================================================================================================================================+
      | Restart Mode                      | Select **Rolling Restart**.                                                                                                                              |
      |                                   |                                                                                                                                                          |
      |                                   | -  Rolling restart is supported only for clusters with three or more nodes, including the master node, client node, and cold data nodes.                 |
      |                                   | -  During a rolling restart, the nodes of a cluster are restarted one at a time. This may take a long time if the cluster has a large number of indexes. |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Select By                         | Only **Node type** is supported. You can select multiple node types to restart them at the same time.                                                    |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Value                             | Select node types for the restart.                                                                                                                       |
      |                                   |                                                                                                                                                          |
      |                                   | Values for **Node type**:                                                                                                                                |
      |                                   |                                                                                                                                                          |
      |                                   | -  **ess**: data node                                                                                                                                    |
      |                                   | -  **ess-master**: master node                                                                                                                           |
      |                                   | -  **ess-client**: client node                                                                                                                           |
      |                                   | -  **ess-cold**: cold data node                                                                                                                          |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **OK** to start the restart task.

   Refresh the page and check the cluster status. During the restart, the cluster status is **Processing**, and the task status is **Restarting**. When the cluster status changes to **Available**, the cluster has restarted successfully.
