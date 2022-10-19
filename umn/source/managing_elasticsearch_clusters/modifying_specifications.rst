:original_name: css_01_0031.html

.. _css_01_0031:

Modifying Specifications
========================

You can scale-in/out your cluster nodes to improve resource utilization and reduce O&M costs.

Scaling out Clusters
--------------------

#. Log in to the CSS management console.

#. Choose **Clusters**. Locate the row containing the target cluster and click Modify in the **Operation** column.

#. On the displayed **Modify Configuration** page, specify **New Nodes** and **Node Storage Capacity**.

   If none of the master nodes, client nodes, and cold data nodes are enabled in your cluster, you can modify the number of nodes or the node storage capacity. You can add 1 to 32 nodes.

   If your cluster has a master node, client node, or cold data node enabled, you can modify the number of master nodes, client nodes, cold data nodes, or the node storage capacity. You can add 1 to 200 nodes, including a maximum of nine master nodes and 32 client nodes.

   .. note::

      -  If you only expand the node quantity, the **Node Specifications** and **Node Storage Capacity** settings of newly added nodes will be the same as the settings you specified during cluster creation.
      -  If none of the master nodes, client nodes, and cold data nodes are enabled in your cluster, and you increase both the node quantity and the storage capacity, the **Node Specifications** settings of newly added nodes will be the same as the settings you specified during cluster creation, whereas the **Node Storage Capacity** settings of all nodes will be changed to the new storage capacity.
      -  If master nodes, client nodes, or cold data nodes are enabled in your cluster, you can increase the quantity and storage capacity of a certain type of nodes, for example, master nodes.
      -  If none of the master nodes, client nodes, and cold data nodes are enabled in your cluster, and you only change the **Node Storage Capacity**, the storage capacity of all the nodes in the cluster will be changed.
      -  If master nodes, client nodes, or cold data nodes are enabled in your cluster, you can increase the storage capacity of a certain type of nodes, for example, master nodes.
      -  You can expand the storage capacity six times at most.
      -  Services will not be interrupted during the cluster scale-out process.


   .. figure:: /_static/images/en-us_image_0000001287293658.png
      :alt: **Figure 1** Modifying specifications


      **Figure 1** Modifying specifications

#. Click **Next**.

#. On the displayed **Details** page, confirm the specifications and click **Submit**.

#. Click **Back to Cluster List** to switch to the **Clusters** page. If **Scaling out** is displayed in the **Task Status** column, the cluster specifications are being modified. If **Available** is displayed in the **Cluster Status** column, the modification is successful.

Scaling in Clusters
-------------------

#. Log in to the CSS management console.
#. Click **Clusters**. Locate the row containing the target cluster and click **Modify** in the **Operation** column.
#. On the displayed **Modify Configuration** page, specify **New Nodes**.

   .. note::

      -  For a cluster without master nodes, the number of remaining data nodes (including cold data nodes and other types of nodes) after scale-in must be greater than half of the original node number, and greater than the maximum number of index replicas.
      -  Ensure each AZ under each node type has at least one node after the scale-in.
      -  For a cluster with master nodes, after scale-in, there has to be an odd number of master nodes, and there has to be at least three of them.
      -  Ensure that the disk usage after scale-in is less than 80%.
      -  Services will not be interrupted during the cluster scale-in process.
      -  During scale-in, data on the node to be brought offline must be migrated to other nodes within 5 hours. Otherwise, the scale-in fails. If the data volume of a cluster is large, you are advised to perform the scale-in for multiple times.

#. Click **Next**.
#. On the displayed **Details** page, confirm the specifications and click **Submit**.
#. Click **Back to Cluster List** to switch to the **Clusters** page. If **Scaling in** is displayed in the **Task Status** column, the cluster specifications are being modified. If **Available** is displayed in the **Cluster Status** column, the scale-in is successful.
