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

-  Node specifications cannot be modified during cluster scale-out.

-  If you change the number and storage capacity of a specified type of node, nodes in other types will not be changed.

-  The quota of nodes in different types varies. For details, see :ref:`Table 1 <css_01_0151__table10730243193816>`.

   .. _css_01_0151__table10730243193816:

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
#. In the navigation pane on the left, choose **Clusters**. On the displayed **Clusters** page, locate the target cluster and choose **More** > **Scale Cluster** in the **Operation** column.
#. On the **Modify Configuration** page, set scale-out parameters.

   -  **New Nodes**: The number of default nodes. For details about the quota, see :ref:`Table 1 <css_01_0151__table10730243193816>`.
   -  **Node Storage Capacity**: The storage capacity of the default nodes. The quota is determined by the **New Node Specifications**. The value must be a multiple of 20.

   .. note::

      If a cluster has master, client, or cold data nodes, you can change the number of these nodes and expand the storage capacity of cold data nodes. For details about the quotas of the master, client, and cold data node, see :ref:`Table 1 <css_01_0151__table10730243193816>`.

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling out**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled out.
