:original_name: en-us_topic_0000001477899188.html

.. _en-us_topic_0000001477899188:

Adding Master/Client Nodes
==========================

If workloads on the data plane of a cluster increase, you can add master or client nodes as needed. Services are not interrupted while they are added.

Prerequisites
-------------

The target cluster is available and has no tasks in progress.

Constraints
-----------

-  If a cluster already has master and client nodes, the **Add Master/Client Node** tab is not displayed on the **Modify Configuration** page. In this case, you need to add the master or client nodes by referring to :ref:`Scaling Out a Cluster <en-us_topic_0000001477899164>`.

-  When you add master or client nodes, the number of nodes that can be configured varies depending on the node type. For details, see :ref:`Table 1 <en-us_topic_0000001477899188__en-us_topic_0000001360218292_table10730243193816>`.

   .. _en-us_topic_0000001477899188__en-us_topic_0000001360218292_table10730243193816:

   .. table:: **Table 1** Number of nodes in different types

      =========== =================================
      Node Flavor Number
      =========== =================================
      Master node An odd number ranging from 3 to 9
      Client node 1 to 32
      =========== =================================

Procedure
---------

#. Log in to the CSS management console.

#. In the navigation pane, choose a cluster type. The cluster management page is displayed.

#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.

#. On the **Modify Configuration** page, choose the **Add Master/Client Node** tab.

#. Select the target node type and set the node specifications, quantity, and storage.

   -  Master and client nodes cannot be added at the same time.
   -  If a cluster already has a master or client node, you can only add nodes of the other type.

#. Click **Next**.

#. Confirm the information and click **Submit**.

   Return to the cluster list page. The **Task Status** of the cluster is **Scaling out**.

   -  If you added a master node and **Cluster Status** changed to **Available**, the master node has been successfully added.

      .. important::

         If the cluster version is earlier than 7.\ *x*, when the **Cluster Status** changes to **Available**, you need to restart all data nodes and cold data nodes in the cluster to make the new node take effect. If the data nodes and cold data nodes are not restarted, the cluster may be reported as unavailable. (The cluster services still run properly.) For details, see :ref:`Restarting a Cluster <en-us_topic_0000001528499141>`.

   -  If you added a client node and **Cluster Status** changed to **Available**, the client node has been added. You can restart data nodes and cold data nodes to shut down Cerebro and Kibana processes on the nodes.
