:original_name: en-us_topic_0000001528499141.html

.. _en-us_topic_0000001528499141:

Restarting a Cluster
====================

If a cluster becomes faulty, you can restart it to check if it can run normally.

Prerequisites
-------------

-  The target cluster is not frozen and has no task in progress.
-  If a cluster is available, ensure that it has stopped processing service requests (such as importing data and searching for data). Otherwise, data may be lost when the cluster is restarted. You are advised to perform this operation during off-peak hours.

Context
-------

CSS supports quick restart and rolling restart.

:ref:`Quick Restart <en-us_topic_0000001528499141__en-us_topic_0000001223594400_section144817324321>`

-  All clusters support this function.
-  If you select a node type for quick restart, all nodes of the selected type will be restarted together.
-  If you select a node name for quick restart, only the specified node will be restarted.
-  The cluster is unavailable during quick restart.

:ref:`Rolling Restart <en-us_topic_0000001528499141__en-us_topic_0000001223594400_section1533564513219>`

-  Rolling restart is supported only when a cluster has at least three nodes (including master nodes, client nodes, and cold data nodes).
-  Rolling restart can be performed only by specifying node types. If you select a node type for rolling restart, the nodes of the selected type will be restarted in sequence.
-  During the rolling restart, only the nodes that are being restarted are unavailable and other nodes can run normally.
-  When the data volume is large, rolling restart will take a long time.

.. _en-us_topic_0000001528499141__en-us_topic_0000001223594400_section144817324321:

Quick Restart
-------------

#. Log in to the CSS management console.

#. In the navigation tree on the left, select a cluster type. The cluster management list page is displayed.

#. In the **Operation** column of the target cluster, choose **More** > **Restart**.

#. On the **Restart Cluster** page, select **Quick Restart**.

   You can quick restart nodes by **Node type** or **Node name**. If you select **Node type**, then you can select multiple node types and perform quick restart at the time. If you select **Node name**, you can perform quick restart only on one node at a time.

#. Refresh the page and check the cluster status. During the restart, the cluster status is **Processing**, and the task status is **Restarting**. If the cluster status changes to **Available**, the cluster has been restarted successfully.

.. _en-us_topic_0000001528499141__en-us_topic_0000001223594400_section1533564513219:

Rolling Restart
---------------

#. Log in to the CSS management console.

#. In the navigation tree on the left, select a cluster type. The cluster management list page is displayed.

#. In the **Operation** column of the target cluster, choose **More** > **Restart**.

#. On the **Restart Cluster** page, select **Rolling Restart**.

   You can perform rolling restart by **Node type**. Select specific node types for restart.

#. Refresh the page and check the cluster status. During the restart, the cluster status is **Processing**, and the task status is **Restarting**. If the cluster status changes to **Available**, the cluster has been restarted successfully.
