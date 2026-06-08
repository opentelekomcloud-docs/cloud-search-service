:original_name: css_01_0250.html

.. _css_01_0250:

CSS Resource Monitoring and Alarms
==================================

For enterprises using CSS for data search and analytics, service continuity and system stability are critical. Sudden surges in data volumes or query requests can lead to performance bottlenecks and availability risks, including high CPU usage, disk exhaustion, and JVM heap memory exhaustion. To enable you to intuitively monitor cluster health, identify performance trends, and receive notifications even before issues occur, CSS integrates Cloud Eye to provide monitoring dashboards (**Monitoring**) as well as metrics and alarms on the **Dashboard** page. With intuitive visualizations and proactive alerting, you can track resource usage and cluster performance in real time, ensuring greater operational resilience.

Method 1: Monitoring Trends on the **Monitoring** Page (Monitoring Dashboards)
------------------------------------------------------------------------------

CSS's out-of-the-box monitoring dashboards offer a one-stop resource monitoring solution. By integrating cloud resource usage data and core service metrics, the monitoring dashboards quickly build unified, intuitive monitoring views for the service, facilitating cluster health inspection and trend analysis.

The monitoring dashboards depend on the following:

-  Metric collection: Collects key resource metrics for the cloud service.
-  Preset dashboards: Displays prebuilt monitoring dashboards for the cloud service. There is no need to manually configure metrics.
-  Data visualization: Intuitively shows resource usage, service status, and trends using configurable charts.

**Constraints:**

-  Region: The monitoring dashboards are available only in some regions. If they are unavailable in your region, the console will show a message informing you of that.
-  Configuration: The **Monitoring** page on the CSS console provides pre-built dashboards only. It does not support custom metrics. To use a custom dashboard, click **More** in the upper-right corner to go to the Cloud Eye console to configure the dashboard.
-  Monitoring scope: Only resources in the current region can be monitored. Cross-region monitoring is not supported.

**Procedure**

#. Log in to the CSS management console.

#. In the navigation pane, choose **Monitoring** to view the preset monitoring dashboards.

   Monitoring dashboards cover the following core metrics:

   -  Resource metrics: cluster health status, average indexing speed, average query speed, maximum CPU usage, maximum JVM heap usage, maximum node loads, number of shards, maximum disk usage, total number of tasks in the write queue, and total number of tasks in the search queue.
   -  Data metrics: current, maximum, minimum, average, and sum values.
   -  Trend analysis: week-on-week (this week vs. last week) and day-on-day (today vs. yesterday) comparisons.

Method 2: Checking Key Metrics on the **Dashboard** Page
--------------------------------------------------------

The **Dashboard** page on the CSS console provides a lightweight monitoring view where you can quickly check cluster health.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Dashboard**.

#. In the **Monitoring** area, check the metrics there.

   This area shows the thumbnails of selected metrics.


   .. figure:: /_static/images/en-us_image_0000002515896182.png
      :alt: **Figure 1** Metrics

      **Figure 1** Metrics

   .. note::

      The metrics of deleted resources are retained for one hour to allow traceability even after deletion.

#. (Optional) Create a custom view.

   a. Click **Configure**. In the displayed dialog box, select the metrics you want to display (for example, **Cluster Health Status**), and set **Rollup** and **Chart Type**.
   b. Click **OK** to save the custom view.

#. Click **More** to go to the Cloud Eye console and see more information about CSS.

Managing Resource Alarms
------------------------

The **Dashboard** page on the CSS console provides a lightweight alarm management view where you quickly check generated alarms. You can set custom alarm thresholds (for example, maximum CPU usage > 80%). When a preset threshold is crossed, the system sends an SMS or email to notify the O&M team promptly.

**Configure alarm rules:**

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Dashboard**.
#. In the upper right corner of the **Alarm Management** area, click **Create Alarm Rule**.
#. In the displayed dialog box, configure alarm rules.

   a. Enable recommended alarm rules. CSS provides recommended alarm rules that, when enabled, automatically apply to all resources in the current region.

      Select **Enable All Recommended Alarm Rules** to enable the recommended alarm rules. Then you can check and modify alarm rules in the list below.

   b. (Optional) Modify recommended alarm rules. If the recommended alarm rules do not meet your needs, click **Cloud Eye One-Click Monitoring** to go to the Cloud Eye console and modify the recommended alarm rules or add new ones. For details, see section "Creating an Alarm Rule and Notifications" in the *Cloud Eye User Guide*.

#. (Optional) Configure a notification policy. To have notifications automatically sent via SMS or email, turn on **Batch Configure Notification Policies**, and configure a notification policy.
#. Click **OK** to save the alarm rules.

**Check alarm information:**

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Dashboard**.

#. Check alarm information in the **Alarm Management** area.


   .. figure:: /_static/images/en-us_image_0000002547376089.png
      :alt: **Figure 2** Alarm Management

      **Figure 2** Alarm Management

   -  Hover the mouse pointer over a resource name to check alarm information in a floating tooltip.
   -  Click **All**. On the displayed **Alarm Records** page, check detailed alarm information.
