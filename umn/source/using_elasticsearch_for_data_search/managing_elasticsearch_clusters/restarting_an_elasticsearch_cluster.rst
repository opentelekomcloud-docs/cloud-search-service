:original_name: css_01_0014.html

.. _css_01_0014:

Restarting an Elasticsearch Cluster
===================================

If an Elasticsearch cluster has stopped working, you can try to recover it by restarting it. Two restart options are available: quick restart and rolling restart. You are advised to perform the restart during off-peak hours.

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

#. In the navigation pane on the left, expand **Clusters** and select a cluster type. A cluster list is displayed.

#. Locate the target cluster and click **More** > **Restart** in the **Operation** column.

#. On the **Restart Cluster** page, set parameters.

   .. table:: **Table 1** Configuring a quick restart

      +-----------------------------------+-----------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                   |
      +===================================+===============================================================================================+
      | Restart Mode                      | Select **Quick Restart**.                                                                     |
      |                                   |                                                                                               |
      |                                   | .. note::                                                                                     |
      |                                   |                                                                                               |
      |                                   |    The cluster will be unavailable for the entire duration of a quick restart.                |
      +-----------------------------------+-----------------------------------------------------------------------------------------------+
      | Operation Role                    | Select **Node type** or **Node name**.                                                        |
      |                                   |                                                                                               |
      |                                   | -  **Node type**: You can select multiple node types to restart them at the same time.        |
      |                                   | -  **Node name**: You can restart only one node at a time.                                    |
      +-----------------------------------+-----------------------------------------------------------------------------------------------+
      | Operation Value                   | Select one or more node types or a node name, depending on the setting of **Operation Role**. |
      |                                   |                                                                                               |
      |                                   | Values for **Node type**:                                                                     |
      |                                   |                                                                                               |
      |                                   | -  **ess**: data node                                                                         |
      |                                   | -  **ess-master**: master node                                                                |
      |                                   | -  **ess-client**: client node                                                                |
      |                                   | -  **ess-cold**: cold data node                                                               |
      +-----------------------------------+-----------------------------------------------------------------------------------------------+

#. Click OK to start the restart task.

   Refresh the page and check the cluster status. During the restart, the cluster status is **Processing**, and the task status is **Restarting**. When the cluster status changes to **Available**, the cluster has restarted successfully.

Rolling Restart
---------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, expand **Clusters** and select a cluster type. A cluster list is displayed.

#. Locate the target cluster and click **More** > **Restart** in the **Operation** column.

#. On the **Restart Cluster** page, set parameters.

   .. table:: **Table 2** Configuring a rolling restart

      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                               |
      +===================================+===========================================================================================================================================================+
      | Restart Mode                      | Select **Rolling Restart**.                                                                                                                               |
      |                                   |                                                                                                                                                           |
      |                                   | .. note::                                                                                                                                                 |
      |                                   |                                                                                                                                                           |
      |                                   |    -  Rolling restart is supported only for clusters with three or more nodes, including the master node, client node, and cold data nodes.               |
      |                                   |    -  During a rolling restart, the nodes of a cluster are restarted one at time. This may take a long time if the cluster has a large number of indexes. |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Operation Role                    | Only **Node type** is supported. You can select multiple node types to restart them at the same time.                                                     |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Operation Value                   | Select node types for the restart.                                                                                                                        |
      |                                   |                                                                                                                                                           |
      |                                   | Values for **Node type**:                                                                                                                                 |
      |                                   |                                                                                                                                                           |
      |                                   | -  **ess**: data node                                                                                                                                     |
      |                                   | -  **ess-master**: master node                                                                                                                            |
      |                                   | -  **ess-client**: client node                                                                                                                            |
      |                                   | -  **ess-cold**: cold data node                                                                                                                           |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click OK to start the restart task.

   Refresh the page and check the cluster status. During the restart, the cluster status is **Processing**, and the task status is **Restarting**. When the cluster status changes to **Available**, the cluster has restarted successfully.
