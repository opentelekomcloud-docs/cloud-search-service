:original_name: css_01_0219.html

.. _css_01_0219:

Synchronizing Alerts and Metrics to Prometheus
==============================================

When building a full-stack monitoring system, O&M teams often use Prometheus to aggregate infrastructure and application metrics. However, business-level data stored in Elasticsearch (such as user access patterns, clickstream events, or transaction logs) remains in document form and is not natively available as Prometheus-format time series, hindering unified analysis and alerting in Grafana dashboards. How can we expose Elasticsearch aggregation results as Prometheus-compatible time series? CSS Elasticsearch clusters address this gap using the built-in Open Distro Alerting plugin, which provides a Prometheus-compatible export channel. Using the Prometheus Pushgateway, this plugin periodically executes queries, transforms the results into structured metrics, and pushes them to the Pushgateway where they can be scraped by Prometheus. This approach enables Elasticsearch clusters to act as intelligent metric sources, supporting unified analysis of business and infrastructure data and consistent, threshold-based alerting within a single observability stack.

How the Feature Works
---------------------

Elasticsearch business metrics must be pushed by the alerting plugin, whereas Prometheus uses a pull-based model by default. The Prometheus Pushgateway bridges this gap: it receives push-based metrics and exposes them via a scrape endpoint for Prometheus. The Open Distro Alerting plugin built into CSS Elasticsearch clusters provides a Prometheus-compatible export channel connected to the Pushgateway.


.. figure:: /_static/images/en-us_image_0000002523087784.png
   :alt: **Figure 1** Alert & metric synchronization link

   **Figure 1** Alert & metric synchronization link

#. **Monitor**: Defines the aggregation query (which metrics to compute), the target indexes, and the execution schedule (query frequency).
#. **Trigger**: Evaluates query results against threshold conditions to determine if and when an alert should be generated. It also triggers an action. **Action**: Transforms Elasticsearch aggregation results (in document form) into standard Prometheus JSON format.
#. **Destination**: A message channel that sends Prometheus-compatible JSON packets to the Pushgateway.
#. **Pushgateway**: A temporary storage area that receives push-based metrics from Elasticsearch.
#. **Prometheus**: Periodically pulls data from the Pushgateway and stores it in its time-series database, where Grafana queries the data and visualizes metrics on unified dashboards.

For more about the Open Distro alerting plugin, see `Open Distro Alerting <https://opendistro.github.io/for-elasticsearch-docs/docs/alerting/>`__. For more about Prometheus Pushgateway, see `Prometheus Pushgateway <https://github.com/prometheus/pushgateway>`__.

Constraints
-----------

-  This feature is available only for Elasticsearch clusters whose image version is no earlier than 7.10.2_24.3.3_xxx.
-  The Elasticsearch cluster must be able to access the Prometheus Pushgateway endpoint. Prometheus and Elasticsearch must be connected. Otherwise, alerts cannot be sent.
-  Only Gauge-type metrics (used in dashboards) can be synchronized. They include statistical or percentage values that can both increase and decrease.

Configuring Alert Synchronization
---------------------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

#. On the Kibana page, choose **Open Distro for Elasticsearch** > **Alerting** in the navigation pane on the left.

#. .. _en-us_topic_0000002122797792__li10273150152314:

   Create a Prometheus destination to establish a physical connection between Elasticsearch and Pushgateway.

   a. On the **Alerting** page, click the **Destinations** tab, and click **Add destination** to configure destination information.

      .. table:: **Table 1** Destinations parameters

         +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                                                                                                                                                                                          |
         +===================================+======================================================================================================================================================================================================================================================================================+
         | Name                              | User-defined destination name                                                                                                                                                                                                                                                        |
         +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Type                              | Type of the notification. Select **PROMETHEUS**.                                                                                                                                                                                                                                     |
         +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Settings                          | Enter the Prometheus Pushgateway endpoint address.                                                                                                                                                                                                                                   |
         |                                   |                                                                                                                                                                                                                                                                                      |
         |                                   | -  Currently, dashboards can only visualize Gauge-type metrics. These include statistical and percentage values that can both increase and decrease. Metrics are queried using specific statements and numeric values are synchronized to Pushgateway for monitoring via Prometheus. |
         |                                   | -  Two types of Pushgateway addresses are supported: HTTP and HTTPS.                                                                                                                                                                                                                 |
         +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


      .. figure:: /_static/images/en-us_image_0000002124604594.png
         :alt: **Figure 2** Add destination

         **Figure 2** Add destination

   b. Click **Create**.

   c. Return to the **Destinations** page. If the new destination is displayed, it has been created.


      .. figure:: /_static/images/en-us_image_0000002124606390.png
         :alt: **Figure 3** Destinations list

         **Figure 3** Destinations list

#. Create a monitor and trigger to define the alarm triggering conditions and monitor interval.

   a. On the **Alerting** page, click the **Monitors** tab. Then click **Create monitor**, and configure the data source and query frequency.

      .. table:: **Table 2** Monitor parameters

         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------+
         | Parameter             |                       | Description                                                                                          |
         +=======================+=======================+======================================================================================================+
         | Configure monitor     | Monitor name          | User-defined monitor name                                                                            |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------+
         |                       | Monitor state         | Whether to disable the monitor.                                                                      |
         |                       |                       |                                                                                                      |
         |                       |                       | -  Select **Disable monitor**: Disable the monitor.                                                  |
         |                       |                       | -  (Recommended) Deselect **Disable monitor**: Enable the monitor.                                   |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------+
         | Define monitor        | Method of definition  | Select a method to define the monitor. You are advised to use **Define using extraction query**.     |
         |                       |                       |                                                                                                      |
         |                       |                       | -  **Define using visual graph**: use a visual query                                                 |
         |                       |                       | -  **Define using extraction query**: use a specific query                                           |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------+
         |                       | Index                 | Index to be monitored                                                                                |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------+
         |                       | Time field            | Timestamp used for time-based aggregations, such as **count**.                                       |
         |                       |                       |                                                                                                      |
         |                       |                       | This parameter is required only when you select **Define using visual graph** to define the monitor. |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------+
         | Monitor schedule      | Frequency             | Select the monitor frequency and set the monitor interval. The options include:                      |
         |                       |                       |                                                                                                      |
         |                       |                       | -  **By interval**                                                                                   |
         |                       |                       | -  **Daily**                                                                                         |
         |                       |                       | -  **Weekly**                                                                                        |
         |                       |                       | -  **Monthly**                                                                                       |
         |                       |                       | -  **Custom cron expression**                                                                        |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------+

   b. Click **Create**. The **Create trigger** page is displayed.

   c. On the **Create trigger** page, define how to convert data into Prometheus-readable formats.

      .. table:: **Table 3** Trigger parameters

         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter             |                       | Description                                                                                                                                                                                                                                                                        |
         +=======================+=======================+====================================================================================================================================================================================================================================================================================+
         | Define trigger        | Trigger name          | User-defined trigger name.                                                                                                                                                                                                                                                         |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         |                       | Severity level        | Sensitivity of the trigger, that is, how many alerts need to be triggered before an alert is actually sent. **1** indicates the highest sensitivity.                                                                                                                               |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         |                       | Trigger condition     | Trigger condition. An alert is triggered when the trigger condition is met.                                                                                                                                                                                                        |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       | You are advised to set a trigger condition that can almost always be triggered (for example, **1 > 0**) so that the query results will always be synchronized to the Pushgateway.                                                                                                  |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Configure actions     | Action name           | Name of the triggered action.                                                                                                                                                                                                                                                      |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         |                       | Destination           | Select the Prometheus destination created in :ref:`5 <en-us_topic_0000002122797792__li10273150152314>`.                                                                                                                                                                            |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         |                       | Message               | Defines the body of the message to be published, which must use the JSON format.                                                                                                                                                                                                   |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       | Message template:                                                                                                                                                                                                                                                                  |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       | .. code-block::                                                                                                                                                                                                                                                                    |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       |    {                                                                                                                                                                                                                                                                               |
         |                       |                       |     "metricsName":"hits_total_value", //Prometheus metric name                                                                                                                                                                                                                     |
         |                       |                       |     "metricsLabel": {"label_key1":"label_value1","label_key2":"label_value2"}, //Prometheus labels                                                                                                                                                                                 |
         |                       |                       |     "metricsValue":{{ctx.results.0.hits.total.value}}, //Prometheus metric values                                                                                                                                                                                                  |
         |                       |                       |     "jobName":"job_name", //Prometheus monitor task name                                                                                                                                                                                                                           |
         |                       |                       |    "metricsHelp":"***" //Metric explanation. Optional.                                                                                                                                                                                                                             |
         |                       |                       |    }                                                                                                                                                                                                                                                                               |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         |                       | Action throttling     | Specify the message frequency to limit the number of notifications you receive within a given span of time. Without it, high-frequency or low-severity triggers may cause information overload or result in unexpected cloud costs.                                                |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       | For example, if this parameter is set to 10 minutes, Prometheus sends only one alert notification in the next 10 minutes even if the trigger condition is met multiple times. After 10 minutes, Prometheus sends another alert notification if the trigger condition is met again. |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   d. Click **Send test message** to test the link to Prometheus.


      .. figure:: /_static/images/en-us_image_0000002554314959.png
         :alt: **Figure 4** Sending a test message

         **Figure 4** Sending a test message

   e. As shown in :ref:`Figure 5 <en-us_topic_0000002122797792__fig128831816195014>`, Prometheus can receive a triggered message, meaning the trigger is set successfully.

      .. _en-us_topic_0000002122797792__fig128831816195014:

      .. figure:: /_static/images/en-us_image_0000002127428880.png
         :alt: **Figure 5** Message received successfully

         **Figure 5** Message received successfully

   f. Click **Create** to go to the monitor details page.
