:original_name: css_01_0014.html

.. _css_01_0014:

Restarting a Cluster
====================

If a cluster becomes faulty, you can restart it to check if it can run normally. Only clusters in the **Available** or **Abnormal** status can be restarted.

Quick Restart
-------------

-  The cluster is in the **Available** or **Abnormal** status.
-  There are no running tasks, such as importing data, searching for data on the cluster.

.. important::

   -  The cluster will be unavailable during quick restart. If quick restart fails, data may be lost or the cluster may become unavailable. Therefore, exercise caution when performing this operation.
   -  If the cluster you want to restart is available, you are advised to stop all data processing tasks on the cluster before restarting it. If there are running tasks, for example, importing data, searching for data, the transmitted data may be lost upon the restart. Therefore you are advised to stop all cluster tasks before the quick restart.

#. Log in to the CSS management console.
#. Click **Clusters** to switch to the **Clusters** page. In the row that contains the cluster you want to restart, click **More > Restart** in the **Operation** column. The **Restart Cluster** page is displayed. Select **Quick Restart**.

   -  You can quick restart nodes by **Node type** or **Node name**. If you select **Node type**, then you can select multiple node types and perform quick restart at the time. If you select **Node name**, you can perform quick restart only on one node at a time.
   -  The cluster is unavailable during quick restart.

#. Refresh the page and check the cluster status. During the restart, the cluster status is **Processing**, and the task status is **Restarting**. If the cluster status changes to **Available**, the cluster has been restarted successfully. If the cluster status changes to **Abnormal**, contact the technical support for troubleshooting.
