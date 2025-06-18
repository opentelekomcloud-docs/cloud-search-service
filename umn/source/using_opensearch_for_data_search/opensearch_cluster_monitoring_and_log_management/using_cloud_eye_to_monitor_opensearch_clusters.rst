:original_name: css_01_0506.html

.. _css_01_0506:

Using Cloud Eye to Monitor OpenSearch Clusters
==============================================

With CSS, you can use Cloud Eye to monitor created clusters. After configuring the cluster monitoring, you can log in to the Cloud Eye management console to view cluster metrics. For details about Cloud Eye, see the `Cloud Eye User Guide <https://docs.otc.t-systems.com/en-us/usermanual/ces/ces_07_0001.html>`__.

The procedure for configuring cluster monitoring:

#. :ref:`Creating Alarm Rules <css_01_0506__css_01_0155_en-us_topic_0000001263429532_section15621114112420>`: Customize alarm rules for the monitoring metrics. Once a metric exceeds the threshold, the system will notify you by sending emails or HTTP/HTTPS requests.
#. :ref:`Configuring Monitoring Metrics <css_01_0506__css_01_0155_en-us_topic_0000001263429532_section1136460963>`: Configure monitoring metrics for a cluster or a node in the cluster.
#. :ref:`Viewing Cluster Monitoring Information <css_01_0506__css_01_0155_section19225545132518>`: View the statistics of the monitoring metrics in specific periods.

Recommended Monitoring Metrics
------------------------------

-  For routine monitoring of a cluster, you are advised to focus on disk usage and cluster health status.
-  Cluster CPU and JVM usage. You are advised to configure the following monitoring metrics: average JVM heap usage, maximum JVM heap usage, average CPU usage, and maximum CPU usage.
-  Cluster write and search latency and throughput. You are advised to configure the following monitoring metrics: average index latency, average index rate, average search latency, and average QPS.
-  Cluster write and query queue and rejected tasks. You are advised to configure the following monitoring metrics: tasks in write queue, tasks in search queue, rejected tasks in write queue, and rejected tasks in search queue.

Prerequisites
-------------

-  The cluster is in the **Available** or **Processing** status.
-  The cluster has been running properly for more than 10 minutes.

.. _css_01_0506__css_01_0155_en-us_topic_0000001263429532_section15621114112420:

Creating Alarm Rules
--------------------

#. Log in to the Cloud Eye console.

#. In the navigation pane on the left, choose **Alarm Management** > **Alarm Rules**.

#. In the **Resource Type** column, select Cloud Search Service to filter alarm rules.

   If no alarm rules are available, create one by referring to section "Creating an Alarm Rule". :ref:`Table 1 <css_01_0506__css_01_0155_en-us_topic_0000001263429532_table15676621164617>` describes the key parameters. For more parameters, customize them as needed.

   .. _css_01_0506__css_01_0155_en-us_topic_0000001263429532_table15676621164617:

   .. table:: **Table 1** Alarm rule configuration parameters

      +-----------------------------------+--------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                          |
      +===================================+======================================================================================+
      | Alarm Type                        | Select **Metric**.                                                                   |
      +-----------------------------------+--------------------------------------------------------------------------------------+
      | Cloud Service                     | Select **Cloud Search Service**.                                                     |
      +-----------------------------------+--------------------------------------------------------------------------------------+
      | Resource Layer                    | Select the layer by which you are going to configure alarm rules.                    |
      |                                   |                                                                                      |
      |                                   | -  **CSS Clusters**: Alarm rules are specified by cluster.                           |
      |                                   | -  **CSS Clusters - CSS Instances**: Alarm rules are specified by node in a cluster. |
      +-----------------------------------+--------------------------------------------------------------------------------------+

.. _css_01_0506__css_01_0155_en-us_topic_0000001263429532_section1136460963:

Configuring Monitoring Metrics
------------------------------

#. Create a monitoring panel by referring to section "Creating a Dashboard". If an available monitoring panel has been created, skip this step.
#. Add CSS monitoring graphs by referring to section "Adding a Graph".

.. _css_01_0506__css_01_0155_section19225545132518:

Viewing Cluster Monitoring Information
--------------------------------------

In the cluster list, check the monitoring information of clusters and cluster nodes.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters**, and click a cluster type to go to the cluster list.

#. In the cluster list, select a cluster and click **View Metric** in the **Operation** column to check the metrics of the cluster and cluster nodes.


   .. figure:: /_static/images/en-us_image_0000002005921800.png
      :alt: **Figure 1** Viewing metrics

      **Figure 1** Viewing metrics

   -  Click the **Instances** tab to check cluster metrics.

      -  **Instances**: Select a cluster to check its metrics. The current cluster is selected by default. Multiple clusters can be selected so that you may compare between them.
      -  You can also set monitoring periods so that you can compare metrics between different periods for the same cluster.
      -  Add Graph Group: You can add a custom group in addition to the default group. When you move the pointer over a group name on the left, the icons for changing the group name and deleting the group are displayed on the right. You can modify the group.
      -  Select Metric: In the displayed **Select Metric** dialog box, set **All Metrics** and **Top N Metrics**.

   -  Click the **CSS Instances** tab to check the metrics of cluster nodes. Only the node monitoring information of the first cluster selected on the **Instances** tab is displayed.

      -  CSS Instances: Select the cluster nodes whose metrics and information you want to check. By default, the first node of the current cluster is selected. Multiple nodes can be selected so that you may compare between them.
      -  You can also set monitoring periods so that you can compare metrics between different periods for the same cluster.
      -  Add Graph Group: You can add a custom group in addition to the default group. When you move the pointer over a group name on the left, the icons for changing the group name and deleting the group are displayed on the right. You can modify the group.
      -  Select Metric: In the displayed **Select Metric** dialog box, set **All Metrics**.
