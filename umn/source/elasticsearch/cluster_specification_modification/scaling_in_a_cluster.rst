:original_name: en-us_topic_0000001528299597.html

.. _en-us_topic_0000001528299597:

Scaling in a Cluster
====================

If a cluster can process existing data without fully using its resources, you can scale in the cluster to reduce costs. You are advised to scale in clusters during off-peak hours.

Prerequisites
-------------

The target cluster is available and has no tasks in progress.

Constraints
-----------

-  Only the number of nodes can be modified during cluster scale-in. The node specifications and node storage capacity cannot be modified. You can modify node specifications by referring to :ref:`Changing Specifications <en-us_topic_0000001477739368>`. You can modify node storage capacity by referring to :ref:`Scaling Out a Cluster <en-us_topic_0000001477899164>`.

-  If you change the number and storage capacity of a specified type of node, nodes in other types will not be changed.

-  Ensure that the disk usage after scale-in is less than 80% and each AZ of each node type has at least one node.

-  When scaling in a cluster, the data in the node to be deleted is migrated to other nodes. The timeout threshold for data migration is five hours. If data migration is not complete within 5 hours, the cluster scale-in fails. You are advised to perform scale-in for multiple times when the cluster has huge amounts of data.

-  For a cluster without master nodes, the number of remaining data nodes (including cold data nodes and other types of nodes) after scale-in must be greater than half of the original node number, and greater than the maximum number of index replicas.

-  For a cluster with master nodes, the number of removed master nodes in a scale-in must be fewer than half of the original master node number. After scale-in, there has to be an odd number of master nodes, and there has to be at least three of them.

-  A cluster with two nodes cannot be scaled in. You can create a cluster using a single node.

-  The quota of nodes in different types varies. For details, see :ref:`Table 1 <en-us_topic_0000001528299597__en-us_topic_0000001338349521_table10730243193816>`.

   .. _en-us_topic_0000001528299597__en-us_topic_0000001338349521_table10730243193816:

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
#. On the **Modify Configuration** page, choose the **Scale Cluster** tab and click **Scale in** to set parameters.

   -  **Action**: Select **Scale in**.
   -  **Resources**: The changed amount of resources.
   -  **Nodes**: The number of the default data nodes. For details about the value range that can be changed, see :ref:`Table 1 <en-us_topic_0000001528299597__en-us_topic_0000001338349521_table10730243193816>`.

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling in**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled in.
