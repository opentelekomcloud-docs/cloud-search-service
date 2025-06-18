:original_name: css_01_0429.html

.. _css_01_0429:

Synchronizing Elasticsearch Alerts to Prometheus
================================================

Make necessary configurations in Kibana to synchronize Elasticsearch alerts to Prometheus so you can use Prometheus to monitor and analyze key performance metrics for Elasticsearch clusters in real time.

Prometheus is an open-source monitoring system with a dimensional data model, flexible query language, efficient time series database and modern alerting approach.

Constraints
-----------

Only Elasticsearch 7.10.2 clusters (with an image version no earlier than 7.10.2_24.3.3_x.x.x) support alert synchronization to Prometheus.

Prerequisites
-------------

-  The Prometheus monitor server is ready, and the Pushgateway address has been obtained. Prometheus and Elasticsearch must be connected. Otherwise, alerts cannot be sent.
-  The Elasticsearch cluster is available.

Configuring Alert Synchronization
---------------------------------

#. Log in to the CSS management console.

#. Choose **Clusters** > **Elasticsearch**, select the target cluster and click **Access Kibana** in the **Operation** column.

#. On the Kibana page, choose **Open Distro for Elasticsearch** > **Alerting** in the navigation pane on the left.

#. .. _css_01_0429__li10273150152314:

   Create a Prometheus destination to send alert messages.

   a. On the **Alerting** page, click the **Destinations** tab, and click **Add destination** to configure destination information.

      .. table:: **Table 1** Destinations parameters

         +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                                                                                                             |
         +===================================+=========================================================================================================================================================================================================+
         | Name                              | User-defined destination name                                                                                                                                                                           |
         +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Type                              | Select **PROMETHEUS**.                                                                                                                                                                                  |
         +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Settings                          | Enter the Pushgateway address of the Prometheus monitor server.                                                                                                                                         |
         |                                   |                                                                                                                                                                                                         |
         |                                   | -  Currently, only Prometheus Gauge dashboards can be added or deleted. Metrics are queried using specific statements and numeric values are synchronized to Pushgateway for monitoring via Prometheus. |
         |                                   | -  Two types of Pushgateway addresses are supported: HTTP and HTTPS.                                                                                                                                    |
         +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


      .. figure:: /_static/images/en-us_image_0000002124604594.png
         :alt: **Figure 1** Add destination

         **Figure 1** Add destination

   b. Click **Create** to return to the Destinations list. The created Prometheus destination is displayed in the list.


      .. figure:: /_static/images/en-us_image_0000002124606390.png
         :alt: **Figure 2** Destinations list

         **Figure 2** Destinations list

#. Create a monitoring task to configure the alert triggering conditions and monitoring interval.

   a. Click the **Monitors** tab on the **Alerting** page, and click **Create monitors** to configure monitoring information.

      .. table:: **Table 2** Monitor parameters

         +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                           |
         +===================================+=======================================================================================================================+
         | Monitor name                      | User-defined monitor name                                                                                             |
         +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
         | Monitor state                     | Monitoring status. You are advised to keep this function enabled.                                                     |
         +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
         | Method of definition              | Select a method to define monitoring. You are advised to use **Define using extraction query**.                       |
         |                                   |                                                                                                                       |
         |                                   | -  **Define using visual graph**: use visualized query statement                                                      |
         |                                   | -  **Define using extraction query**: use specific query statement                                                    |
         +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
         | Index                             | Index to be monitored                                                                                                 |
         +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
         | Time field                        | When **Define using visual graph** is selected, select a time field and define counting parameters such as **count**. |
         +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+
         | Frequency                         | Select the monitoring frequency and set the monitoring interval. The options include:                                 |
         |                                   |                                                                                                                       |
         |                                   | -  **By interval**                                                                                                    |
         |                                   | -  **Daily**                                                                                                          |
         |                                   | -  **Weekly**                                                                                                         |
         |                                   | -  **Monthly**                                                                                                        |
         |                                   | -  **Custom cron expression**                                                                                         |
         +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------+

   b. Click **Create**. The **Create trigger** page is displayed.

   c. On the **Create trigger** page, set the alert triggering conditions and the actions to be triggered.

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
         |                       |                       | .. note::                                                                                                                                                                                                                                                                          |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       |    You are advised to set a trigger condition that can almost always be triggered so that the queried metrics will always be synchronized to the Pushgateway.                                                                                                                      |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Configure actions     | Action name           | Name of the triggered action.                                                                                                                                                                                                                                                      |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         |                       | Destination           | Select the destination created in :ref:`4 <css_01_0429__li10273150152314>`.                                                                                                                                                                                                        |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         |                       | Message               | Defines the body of the message to be published. See the following for an example.                                                                                                                                                                                                 |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       | .. code-block::                                                                                                                                                                                                                                                                    |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       |    {                                                                                                                                                                                                                                                                               |
         |                       |                       |     "metricsName":"hits_total_value", //Prometheus metric name                                                                                                                                                                                                                     |
         |                       |                       |     "metricsLabel": {"label_key1":"label_value1","label_key2":"label_value2"}, //Prometheus labels                                                                                                                                                                                 |
         |                       |                       |     "metricsValue":{{ctx.results.0.hits.total.value}}, //Prometheus metric values                                                                                                                                                                                                  |
         |                       |                       |     "jobName":"job_name" //Prometheus monitor task name                                                                                                                                                                                                                            |
         |                       |                       |    "metricsHelp":"***" //Metric explanation. Optional.                                                                                                                                                                                                                             |
         |                       |                       |    }                                                                                                                                                                                                                                                                               |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         |                       | Action throttling     | Message sending interval. It limits the number of notification messages that can be sent over a specified period.                                                                                                                                                                  |
         |                       |                       |                                                                                                                                                                                                                                                                                    |
         |                       |                       | For example, if this parameter is set to 10 minutes, Prometheus sends only one alert notification in the next 10 minutes even if the trigger condition is met multiple times. After 10 minutes, Prometheus sends another alert notification if the trigger condition is met again. |
         +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   d. Click **Send test message** to send a test message to Prometheus to check whether the trigger is set successfully.


      .. figure:: /_static/images/en-us_image_0000002162710369.png
         :alt: **Figure 3** Sending a test message

         **Figure 3** Sending a test message

      As shown in :ref:`Figure 4 <css_01_0429__fig341274195412>`, Prometheus can receive a triggered message, meaning the trigger is set successfully.

      .. _css_01_0429__fig341274195412:

      .. figure:: /_static/images/en-us_image_0000002127428880.png
         :alt: **Figure 4** Message received successfully

         **Figure 4** Message received successfully

   e. Click **Create** to return to the **Monitor** details page.
