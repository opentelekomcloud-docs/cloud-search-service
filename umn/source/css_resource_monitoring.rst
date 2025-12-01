:original_name: css_01_0250.html

.. _css_01_0250:

CSS Resource Monitoring
=======================

On the **Monitoring** and **Dashboard** pages of the CSS management console, you can check the resource monitoring metrics and alarms of CSS.

Checking the Monitoring Dashboards
----------------------------------

CSS's out-of-the-box monitoring dashboards offer a one-stop resource monitoring solution. By integrating cloud resource usage data and core service metrics, the monitoring dashboards quickly build unified, intuitive monitoring views for key services, enabling more effective resource monitoring.

The monitoring dashboards depend on the following:

-  Metric collection: Collects key resource metrics for cloud services.
-  Preset dashboards: Display prebuilt monitoring dashboards for key cloud services. There is no need to manually configure metrics.
-  Data visualization: Intuitively shows resource usage, service status, and trends using charts.

To check CSS's monitoring dashboards, perform the following steps:

#. Log in to the CSS management console.

#. In the navigation pane, choose **Monitoring** to view the default monitoring dashboards.

   .. caution::

      -  Monitoring dashboards are not yet available in all regions. For regions where they are unavailable, a message will be displayed indicating no support.
      -  Custom metrics cannot be configured. Only preset dashboards are provided. To use a custom dashboard, click **More** in the upper-right corner to go to the Cloud Eye console and configure the dashboard.
      -  Cross-region resource monitoring is not supported. You can only monitor resources in the current region.

   Monitoring dashboards cover the following core metrics:

   -  Resource metrics: cluster health status, average indexing speed, average query speed, maximum CPU usage, maximum JVM heap usage, maximum node loads, number of shards, maximum disk usage, total number of tasks in the write queue, and total number of tasks in the search queue.
   -  Data metrics: current, maximum, minimum, average, and sum values.
   -  Trend analysis: week-on-week (this week vs last week) and day-on-day (today vs yesterday) comparisons.

For how to use the monitoring dashboards, see section "Overview of Dashboards" in Cloud Eye User Guide.

Checking Resource Alarms
------------------------

Check CSS alarms on the **Dashboard** page.

#. Log in to the CSS management console.

#. In the navigation tree on the left, choose **Dashboard**. Check CSS alarms in the **Alarm Management** area.


   .. figure:: /_static/images/en-us_image_0000002005878574.png
      :alt: **Figure 1** Alarm Management

      **Figure 1** Alarm Management

   -  Click **All**. On the displayed **Alarm Records** page, check detailed alarm information.
   -  Hover the mouse pointer over a resource name to check alarm information.

#. Click **Create Alarm Rule**. On the **Alarm Configuration** page, set alarm rules as needed.

   If the preset alarm rules cannot meet your requirements, click **Create Alarm Rule** to create new rules. For details, see section "Creating an Alarm Rule".

Checking Resource Monitoring Metrics
------------------------------------

Check CSS resource monitoring metrics on the **Dashboard** page.

#. Log in to the CSS management console.

#. In the navigation tree on the left, choose **Dashboard**. Check resource monitoring metrics in the **Monitoring** area.


   .. figure:: /_static/images/en-us_image_0000002006038546.png
      :alt: **Figure 2** Monitoring metrics

      **Figure 2** Monitoring metrics

   -  Click **Configure**. In the displayed dialog box, set the metrics to be displayed, **Rollup** (aggregation method), and **Chart Type**.
   -  Click **More** to go to the Cloud Eye console to check more details.
