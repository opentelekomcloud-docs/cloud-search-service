:original_name: css_01_0153.html

.. _css_01_0153:

Scaling in a Cluster
====================

If a cluster can process existing data without fully using its resources, you can scale in the cluster to reduce costs. Services are not interrupted during cluster scale-in.

Prerequisites
-------------

The target cluster is available and has no tasks in progress.

Constraints
-----------

-  The node specifications and storage capacity cannot be modified during scale-in.

-  If you change the number and storage capacity of a specified type of node, nodes in other types will not be changed.

-  Ensure that the disk usage after scale-in is less than 80% and each AZ of each node type has at least one node.

-  When scaling in a cluster, the data in the node to be deleted is migrated to other nodes. The timeout threshold for data migration is five hours. If data migration is not complete within 5 hours, the cluster scale-in fails. You are advised to perform scale-in for multiple times when the cluster has huge amounts of data.

-  For a cluster without master nodes, the number of remaining data nodes (including cold data nodes and other types of nodes) after scale-in must be greater than half of the original node number, and greater than the maximum number of index replicas.

-  The quota of nodes in different types varies. For details, see :ref:`Table 1 <css_01_0153__table10730243193816>`.

   .. _css_01_0153__table10730243193816:

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
#. On the **Modify Configuration** page, set scale-in parameters.

   -  **New Nodes**: The number of default nodes. For details about the quota, see :ref:`Table 1 <css_01_0153__table10730243193816>`.
   -  If a cluster has master nodes, client nodes, or cold data nodes, you can change the node number. For details about the quotas of the master, client, and cold data node, see :ref:`Table 1 <css_01_0153__table10730243193816>`.

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling in**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled in.
