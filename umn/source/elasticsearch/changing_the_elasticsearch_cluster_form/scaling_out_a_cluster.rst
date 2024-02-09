:original_name: css_01_0151.html

.. _css_01_0151:

Scaling Out a Cluster
=====================

If the workloads on the data plane of a cluster change, you can scale out the cluster by increasing the number or capacity of its nodes. Services are not interrupted during cluster scale-out.

Prerequisites
-------------

-  The target cluster is available and has no tasks in progress.
-  The target cluster has sufficient quotas available.

Constraints
-----------

-  The **Node Specifications** cannot be modified during scale-out. You can modify **Node Specifications** by referring to :ref:`Changing Specifications <css_01_0152>`.

-  If you change the number and storage capacity of a specified type of node, nodes in other types will not be changed.

-  The quota of nodes in different types varies. For details, see :ref:`Table 1 <css_01_0151__en-us_topic_0000001285669680_table10730243193816>`.

   .. _css_01_0151__en-us_topic_0000001285669680_table10730243193816:

   .. table:: **Table 1** Number of nodes in different types

      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | Node Type                                                                                                          | Number                                        |
      +====================================================================================================================+===============================================+
      | ess                                                                                                                | ess: 1-32                                     |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master                                                                                                    | ess: 1-200                                    |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-master: an odd number ranging from 3 to 9 |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-client                                                                                                    | ess: 1-32                                     |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-client: 1-32                              |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-cold                                                                                                      | ess: 1-32                                     |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-cold: 1-32                                |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-client                                                                                        | ess: 1-200                                    |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-client: 1-32                              |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-cold                                                                                          | ess: 1-200                                    |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-cold: 1-32                                |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-client, ess-cold                                                                                          | ess: 1-32                                     |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-client: 1-32                              |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-cold: 1-32                                |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-client, ess-cold                                                                              | ess: 1-200                                    |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-client: 1-32                              |
      |                                                                                                                    |                                               |
      |                                                                                                                    | ess-cold: 1-32                                |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | Details about the four node types:                                                                                 |                                               |
      |                                                                                                                    |                                               |
      | -  **ess**: the default node type that is mandatory for cluster creation. The other three node types are optional. |                                               |
      | -  **ess-master**: master node                                                                                     |                                               |
      | -  **ess-client**: client node                                                                                     |                                               |
      | -  **ess-cold**: cold data node                                                                                    |                                               |
      +--------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+

Procedure
---------

#. Log in to the CSS management console.
#. In the navigation pane, choose a cluster type. The cluster management page is displayed.
#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.
#. On the **Modify Configuration** page, choose the **Scale Cluster** tab and click **Scale out** to set parameters.

   -  **Action**: Select **Scale out**.
   -  **Resource**: The changed amount of resources.
   -  **Nodes**: The number of nodes and node storage capacity of the default data node.

      -  **Nodes**: For details, see :ref:`Table 1 <css_01_0151__en-us_topic_0000001285669680_table10730243193816>`.
      -  The value range of **Node Storage Type** depends on the **Node Specifications**. The value must be a multiple of 20.

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling out**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled out.
