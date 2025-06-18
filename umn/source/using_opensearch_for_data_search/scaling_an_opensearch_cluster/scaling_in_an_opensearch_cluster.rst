:original_name: css_01_0485.html

.. _css_01_0485:

Scaling In an OpenSearch Cluster
================================

If a cluster can process current traffic without fully utilizing its resources, you can scale in the cluster to cut costs.

Scenario
--------

CSS supports multiple scale-in methods, as described in :ref:`Table 1 <css_01_0151__table13694163818283>`.

.. table:: **Table 1** Scaling in an Elasticsearch cluster

   +--------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
   | Scenario                 | Description                                                                                    | Details                                                                                                      |
   +==========================+================================================================================================+==============================================================================================================+
   | Reducing nodes randomly  | Randomly removes some of the nodes of a cluster, so that it is less costly to keep it running. | :ref:`Reducing Nodes Randomly <css_01_0485__css_01_0153_en-us_topic_0000001338349521_section1177713055318>`  |
   +--------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+
   | Removing specified nodes | Removes specified nodes of a cluster, so that it is less costly to keep it running.            | :ref:`Removing Specified Nodes <css_01_0485__css_01_0153_en-us_topic_0000001338468977_section1177713055318>` |
   +--------------------------+------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------+

Constraints
-----------

-  To reduce the impact on services, you are advised to perform scale-in during off-peak hours.

-  During a scale-in, the data on the to-be-removed nodes needs to be migrated to other nodes. The timeout threshold for data migration is five hours. If data migration is not complete within 5 hours, the cluster scale-in fails. If the cluster stores large amounts of data, you are advised to break down the scale-in task into multiple batches, and complete each batch one at a time.

-  Ensure that the disk usage after scale-in is less than 80% and each AZ has at least one node of each type.

-  In a cross-AZ cluster, the difference between the numbers of the same type nodes in different AZs cannot exceed 1.

-  For a cluster without master nodes, the number of removed data nodes plus cold data nodes in a scale-in must be fewer than half of the original data nodes plus cold data nodes, and the number of remaining data nodes plus cold data nodes after a scale-in must be greater than the maximum number of index replicas.

-  For a cluster with master nodes, the number of removed master nodes in a scale-in must be fewer than half of the original master nodes. After scale-in, there has to be an odd number of master nodes, and there has to be at least three of them.

-  In each cluster, the number of nodes supported by each node type varies, depending on the types of nodes used in that cluster. For details, see :ref:`Table 2 <css_01_0485__css_01_0153_table144451631608>`.

   .. _css_01_0485__css_01_0153_table144451631608:

   .. table:: **Table 2** Number of nodes of different types allowed in a single cluster

      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | Node Type                                                                                                                                 | Node Quantity                                 |
      +===========================================================================================================================================+===============================================+
      | ess                                                                                                                                       | ess: 1-32                                     |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master                                                                                                                           | ess: 1-200                                    |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-master: an odd number ranging from 3 to 9 |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-client                                                                                                                           | ess: 1-32                                     |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-client: 1-32                              |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-cold                                                                                                                             | ess: 1-32                                     |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-cold: 1-32                                |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-client                                                                                                               | ess: 1-200                                    |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-client: 1-32                              |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-cold                                                                                                                 | ess: 1-200                                    |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-cold: 1-32                                |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-client, ess-cold                                                                                                                 | ess: 1-32                                     |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-client: 1-32                              |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-cold: 1-32                                |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | ess, ess-master, ess-client, ess-cold                                                                                                     | ess: 1-200                                    |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-master: an odd number ranging from 3 to 9 |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-client: 1-32                              |
      |                                                                                                                                           |                                               |
      |                                                                                                                                           | ess-cold: 1-32                                |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+
      | .. note::                                                                                                                                 |                                               |
      |                                                                                                                                           |                                               |
      |    -  **ess**: data node, which is the default node type that is mandatory for cluster creation. The other three node types are optional. |                                               |
      |    -  **ess-master**: master node                                                                                                         |                                               |
      |    -  **ess-client**: client node                                                                                                         |                                               |
      |    -  **ess-cold**: cold data node                                                                                                        |                                               |
      +-------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------+

Prerequisites
-------------

-  The cluster is in the **Available** state and has no ongoing tasks.
-  All mission-critical data has been backed up before a cluster scale-in. This is to prevent data loss.

.. _css_01_0485__css_01_0153_en-us_topic_0000001338349521_section1177713055318:

Reducing Nodes Randomly
-----------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose a cluster type. The cluster management page is displayed.
#. In the cluster list, select the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.
#. Click the **Scale Cluster** tab.
#. Click **Scale in** to set parameters.

   .. table:: **Table 3** Reducing nodes randomly

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                               |
      +===================================+===========================================================================================================================+
      | Action                            | Select **Scale in**.                                                                                                      |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
      | Resources                         | Shows the change of resources for this scale-in operation.                                                                |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+
      | Nodes                             | Reduce the number of nodes in the **Nodes** column. You can change multiple node types at the same time.                  |
      |                                   |                                                                                                                           |
      |                                   | For the value range of node quantity for each node type, see :ref:`Table 2 <css_01_0485__css_01_0153_table144451631608>`. |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------+

#. Click **Next**.
#. Confirm the information and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling in**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled in.

.. _css_01_0485__css_01_0153_en-us_topic_0000001338468977_section1177713055318:

Removing Specified Nodes
------------------------

#. Log in to the CSS management console.

#. In the navigation pane, choose a cluster type. The cluster management page is displayed.

#. In the cluster list, select the target cluster, and choose **More** > **Modify Configuration** in the **Operation** column. The **Modify Configuration** page is displayed.

#. On the **Modify Configuration** page, click the **Scale In** tab.

#. Set scale-in parameters.

   .. table:: **Table 4** Removing specified nodes

      +-----------+-------------------------------------------------------------------------------------------------------------+
      | Parameter | Description                                                                                                 |
      +===========+=============================================================================================================+
      | Node Type | Expand the node type that needs be changed to show all nodes under it. Select the nodes you want to remove. |
      +-----------+-------------------------------------------------------------------------------------------------------------+

#. Click **Next**.

#. Confirm the change information and click **Submit**. In the confirm dialog box, choose to migrate data, which helps to prevent data loss, and click **OK**.

   During data migration, the system migrates all data from the to-be-removed nodes to the remaining nodes, and removes these nodes upon completion of the data migration. If the data on the to-be-removed nodes has replicas on other nodes, data migration can be skipped and the cluster change can be completed faster.

#. Click **Back to Cluster List** to switch to the **Clusters** page. The **Task Status** is **Scaling in**. When **Cluster Status** changes to **Available**, the cluster has been successfully scaled in.
