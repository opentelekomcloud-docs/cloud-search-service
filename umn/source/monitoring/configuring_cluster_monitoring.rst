:original_name: en-us_topic_0000001477579336.html

.. _en-us_topic_0000001477579336:

Configuring Cluster Monitoring
==============================

You can use Cloud Eye to monitor the created clusters. After configuring the cluster monitoring, you can log in to the Cloud Eye management console to view cluster metrics.

The procedure for configuring cluster monitoring:

#. :ref:`Creating Alarm Rules <en-us_topic_0000001477579336__en-us_topic_0000001263429532_section15621114112420>`: Customize alarm rules for the monitoring metrics. Once a metric exceeds the threshold, the system will notify you by sending emails or HTTP/HTTPS requests.
#. :ref:`Configuring Monitoring Metrics <en-us_topic_0000001477579336__en-us_topic_0000001263429532_section1136460963>`: Configure monitoring metrics for a cluster or a node in the cluster.
#. :ref:`Viewing Monitoring Metrics <en-us_topic_0000001477579336__en-us_topic_0000001263429532_section322123712611>`: View the statistics of the monitoring metrics in specific periods.

Prerequisites
-------------

-  The cluster is in the **Available** or **Processing** status.
-  The cluster has been running properly for more than 10 minutes.

Recommended Monitoring Metrics
------------------------------

-  Cluster CPU and JVM usage. You are advised to configure the following monitoring metrics: average JVM heap usage, maximum JVM heap usage, average CPU usage, and maximum CPU usage.
-  Cluster write and query latency and throughput. You are advised to configure the following monitoring metrics: average index latency, average index rate, average search latency, and average QPS.
-  Cluster write and query queue and rejected tasks. You are advised to configure the following monitoring metrics: tasks in write queue, tasks in search queue, rejected tasks in write queue, and rejected tasks in search queue.

.. _en-us_topic_0000001477579336__en-us_topic_0000001263429532_section15621114112420:

Creating Alarm Rules
--------------------

#. Log in to the Cloud Eye console.

#. In the navigation pane on the left, choose **Alarm Management** > **Alarm Rules**.

#. In the **Resource Type** column, select **Cloud Search Service** as criteria to search for alarm rules that meet the requirements.

   If no alarm rules are available, create one by referring to the "Creating an Alarm Rule" section. For details about how to set **Resource Type** and **Dimension**, see :ref:`Table 1 <en-us_topic_0000001477579336__en-us_topic_0000001263429532_table15676621164617>`.

   .. _en-us_topic_0000001477579336__en-us_topic_0000001263429532_table15676621164617:

   .. table:: **Table 1** Alarm rule configuration parameter

      +-----------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------+
      | Parameter             | Description                                             | Remark                                                                               |
      +=======================+=========================================================+======================================================================================+
      | Resource Type         | Type of the resource that the alarm rule is created for | Select **Cloud Search Service**.                                                     |
      +-----------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------+
      | Dimension             | Metric dimension of the selected resource type          | CSS supports two dimensions. Select a dimension as required.                         |
      |                       |                                                         |                                                                                      |
      |                       |                                                         | -  **CSS Clusters**: Alarm rules are specified by cluster.                           |
      |                       |                                                         | -  **CSS Clusters - CSS Instances**: Alarm rules are specified by node in a cluster. |
      +-----------------------+---------------------------------------------------------+--------------------------------------------------------------------------------------+

.. _en-us_topic_0000001477579336__en-us_topic_0000001263429532_section1136460963:

Configuring Monitoring Metrics
------------------------------

#. Create a monitoring panel by referring to the "Creating a Dashboard" section. If an available monitoring panel has been created, skip this step.

#. Add CSS monitoring graphs by referring to the "Adding a Graph" section.

   For details about how to set **Resource Type** and **Dimension**, see :ref:`Table 2 <en-us_topic_0000001477579336__en-us_topic_0000001263429532_table10410173801911>`.

   .. _en-us_topic_0000001477579336__en-us_topic_0000001263429532_table10410173801911:

   .. table:: **Table 2** Graph configuration parameter

      +-----------------------+--------------------------------------+-----------------------------------------------------------------------------------+
      | Parameter             | Description                          | Remark                                                                            |
      +=======================+======================================+===================================================================================+
      | Resource Type         | Type of the resource to be monitored | Select **Cloud Search Service**.                                                  |
      +-----------------------+--------------------------------------+-----------------------------------------------------------------------------------+
      | Dimension             | Metric dimension                     | CSS supports two dimensions. Select a dimension as required.                      |
      |                       |                                      |                                                                                   |
      |                       |                                      | -  **CSS Clusters**: Monitoring is executed by cluster.                           |
      |                       |                                      | -  **CSS Clusters - CSS Instances**: Monitoring is executed by node in a cluster. |
      +-----------------------+--------------------------------------+-----------------------------------------------------------------------------------+

.. _en-us_topic_0000001477579336__en-us_topic_0000001263429532_section322123712611:

Viewing Monitoring Metrics
--------------------------

#. Log in to the CSS management console.
#. Choose **Clusters**. Locate the target cluster and choose **More** > **View Metric** in the **Operation** column.
#. Select a time range.
#. View the monitoring metrics.
