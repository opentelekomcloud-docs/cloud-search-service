:original_name: css_01_0364.html

.. _css_01_0364:

Setting Alarm Alerting via SMN for an OpenSearch Cluster
========================================================

This topic describes how to use an open-source alerting or notification plugin to configure alarm alerting via the Simple Message Notification (SMN) service for OpenSearch clusters in OpenSearch Dashboards.

Scenarios
---------

In CSS, the open-source OpenSearch alerting plugin (opensearch-alerting) and OpenSearch notification plugin (opensearch-notifications and opensearch-notifications-core) are installed by default. They trigger alerts when data meets predefined conditions.

-  By default, the open-source alert plugin **opensearch-alerting** is installed for OpenSearch clusters of version 1.3.6. This plugin consists of three components: **Alerts**, **Monitors**, and **Destinations**. CSS integrates the SMN service in the **Destinations** component, allowing it to send alarm notifications to the SMN service as a destination.
-  For OpenSearch 2.19.0 clusters, the open-source OpenSearch alerting plugin (opensearch-alerting) and OpenSearch notification plugin (opensearch-notifications and opensearch-notifications-core) are installed by default. The Destinations component of the OpenSearch alerting plugin is now an independent notification plugin that manages notification channels. CSS integrates the SMN service in its **Notifications** component, so it can use SMN as a notification channel.

For more information about the OpenSearch alerting plugin, see `Alerting - OpenSearch Documentation <https://docs.opensearch.org/2.19/observing-your-data/alerting/index/>`__. For more information about the OpenSearch notifications plugin, see `Notifications - OpenSearch Documentation <https://docs.opensearch.org/2.19/observing-your-data/notifications/index/>`__.

.. _en-us_topic_0000001938218372__section14330827195719:

Prerequisites
-------------

-  You have created a topic on the SMN console.
-  You have obtained the CSS administrator account. This account has the permission to access CSS, check the agency list, create agencies, and grant permissions to agencies.

Authorizing Users to Use SMN
----------------------------

#. Log in to the CSS management console.

   You must log in using a CSS administrator account.

#. In the navigation pane, choose **Service Authorization**.

#. On the **Service Authorization** page, click **Create Agency**. In the dialog box displayed, confirm that the agency is successfully created.

   -  If an agency has been created, "css_smn_agency exist, no need to created." is displayed in the upper right corner.
   -  If you do not have the permission to create an agency, an error message will be displayed in the upper right corner indicating "no permission", in which case, check that the administrator account has been assigned the IAM permission.

Setting Alarm Notifications via SMN (OpenSearch 2.19.0)
-------------------------------------------------------

#. Log in to the CSS management console.

   Log in using an account with CSS permissions.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. On the OpenSearch Dashboards console, expand the menu in the upper-left corner, and choose **Notifications**.

#. .. _en-us_topic_0000001938218372__li1220804983114:

   Create an SMN channel to send alert messages.

   a. On the **Channels** page, click **Create channel** and configure a notification channel.

      .. table:: **Table 1** Channel parameters

         +-------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter   | Description                                                                                                                                     |
         +=============+=================================================================================================================================================+
         | Name        | Custom channel name.                                                                                                                            |
         +-------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
         | Description | Custom channel description.                                                                                                                     |
         +-------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
         | Type        | Retain the default value **SMN**.                                                                                                               |
         +-------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
         | Topic       | Select the SMN topic you have created in :ref:`Prerequisites <en-us_topic_0000001938218372__section14330827195719>` for sending alert messages. |
         +-------------+-------------------------------------------------------------------------------------------------------------------------------------------------+


      .. figure:: /_static/images/en-us_image_0000002417423609.png
         :alt: **Figure 1** Create channel

         **Figure 1** Create channel

   b. Click **Create**.

   c. Return to the **Channels** page. If the new channel is displayed, it has been created successfully.


      .. figure:: /_static/images/en-us_image_0000002417543465.png
         :alt: **Figure 2** Channels list

         **Figure 2** Channels list

#. On the OpenSearch Dashboards console, expand the menu in the upper-left corner, and choose **Alerting**.

#. Create a monitor and configure alarm triggers and monitoring frequency.

   a. Click the **Monitors** tab on the **Alerting** page and click **Create monitor** to configure monitor information.

      .. table:: **Table 2** Monitor parameters

         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                                                                                                                    |
         +===================================+================================================================================================================================================================================================================+
         | **Monitor details**               |                                                                                                                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Monitor name                      | User-defined monitor name                                                                                                                                                                                      |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Monitor type                      | Monitor type, which can be:                                                                                                                                                                                    |
         |                                   |                                                                                                                                                                                                                |
         |                                   | -  Per query monitor                                                                                                                                                                                           |
         |                                   | -  Per bucket monitor                                                                                                                                                                                          |
         |                                   | -  Per cluster metrics monitor                                                                                                                                                                                 |
         |                                   | -  Per document monitors                                                                                                                                                                                       |
         |                                   | -  Composite monitors                                                                                                                                                                                          |
         |                                   |                                                                                                                                                                                                                |
         |                                   | In this example, **Per query monitor** is selected. For more information, see `Monitors <https://docs.opensearch.org/2.19/observing-your-data/alerting/monitors/>`__ in the OpenSearch official documentation. |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Monitor defining method           | Monitor defining method. **Extraction query editor** is recommended.                                                                                                                                           |
         |                                   |                                                                                                                                                                                                                |
         |                                   | -  **Visual editor**                                                                                                                                                                                           |
         |                                   | -  **Extraction query editor**                                                                                                                                                                                 |
         |                                   | -  **Anomaly detector**                                                                                                                                                                                        |
         |                                   |                                                                                                                                                                                                                |
         |                                   | The options of **Monitor defining method** are determined by the **Monitor type** you selected.                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Detector                          | If **Monitor defining method** is set to **Anomaly detector**, select an exception detection task.                                                                                                             |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Frequency                         | Select the monitoring frequency and set the monitoring interval. The options include:                                                                                                                          |
         |                                   |                                                                                                                                                                                                                |
         |                                   | -  **By interval**                                                                                                                                                                                             |
         |                                   | -  **Daily**                                                                                                                                                                                                   |
         |                                   | -  **Weekly**                                                                                                                                                                                                  |
         |                                   | -  **Monthly**                                                                                                                                                                                                 |
         |                                   | -  **Custom cron expression**                                                                                                                                                                                  |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | **Select data**                   |                                                                                                                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Index                             | When **Monitor defining method** is set to **Visual editor** or **Extraction query editor**, you need to specify the index to be monitored.                                                                    |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Time field                        | When **Monitor defining method** is set to **Visual editor**, you need to specify the time field to define counting parameters such as **count**.                                                              |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | **Query**                         |                                                                                                                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Metrics                           | When **Monitor defining method** is set to **Visual editor**, you need to set the metrics range for extracting statistics.                                                                                     |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Time range for the last           | When **Monitor defining method** is set to **Visual editor**, you need to set the monitoring time range for plugins.                                                                                           |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Data filter                       | When **Monitor defining method** is set to **Visual editor**, you need to set filters for data search.                                                                                                         |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Group by                          | When **Monitor defining method** is set to **Visual editor**, you need to specify a field so that each value of the field triggers an alarm.                                                                   |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Define extraction query           | When **Monitor defining method** is set to **Extraction query editor**, you need to enter the query statement to define the monitoring.                                                                        |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Request type                      | When **Monitor type** is set to **Per cluster metrics monitor**, you need to specify the request type to monitor cluster metrics, such as the running status and CPU usage.                                    |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Preview query and performance     | Preview the query result and verify query performance under the current configuration.                                                                                                                         |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   b. Click **Add trigger** to add triggers and specify the alarm triggering conditions and actions to be triggered when an alarm is reported.

   c. On the **Triggers** page, set the alarm triggering sensitivity and message release on the destination end.

      .. table:: **Table 3** Trigger parameters

         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                                                                                                                                                                      |
         +===================================+==================================================================================================================================================================================================================================================================+
         | Trigger name                      | User-defined trigger name.                                                                                                                                                                                                                                       |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Severity level                    | Sensitivity of a trigger, that is, the number of alarms that need to be triggered before an alarm message is sent. **1** indicates the highest sensitivity.                                                                                                      |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Trigger condition                 | Trigger condition. An alarm is triggered when the trigger condition is hit.                                                                                                                                                                                      |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Action name                       | Trigger action name.                                                                                                                                                                                                                                             |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Channels                          | Select the SMN destination created in :ref:`5 <en-us_topic_0000001938218372__li1220804983114>`.                                                                                                                                                                  |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Message subject                   | A description of the message.                                                                                                                                                                                                                                    |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Message                           | Alarm message body. By default, the subject and body are defined when the destination is an email address.                                                                                                                                                       |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Perform action                    | When **Monitor type** is set to **Per bucket monitor**, you need to set whether to send alarms in combination. The value can be:                                                                                                                                 |
         |                                   |                                                                                                                                                                                                                                                                  |
         |                                   | -  **Per execution**: A combination alarm is sent when multiple alarm triggering conditions are hit.                                                                                                                                                             |
         |                                   | -  **Per alert**: Alarms are sent separately when multiple alarm triggering conditions are hit.                                                                                                                                                                  |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Actionable alerts                 | When **Monitor type** is set to **Per bucket monitor**, set this parameter to **Per alert**. You need to set the alarms that can be executed after alarm triggering conditions are hit.                                                                          |
         |                                   |                                                                                                                                                                                                                                                                  |
         |                                   | -  **De-duplicated**: Alarms that have been triggered. OpenSearch retains the existing alarms to prevent the plugin from creating duplicate alarms.                                                                                                              |
         |                                   | -  **New**: Newly created alarms.                                                                                                                                                                                                                                |
         |                                   | -  **Completed**: Alarms that are no longer ongoing.                                                                                                                                                                                                             |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Throttling                        | Message sending frequency. It limits the number of notification messages can be received in a specified period.                                                                                                                                                  |
         |                                   |                                                                                                                                                                                                                                                                  |
         |                                   | For example, if this parameter is set to 10 minutes, SMN sends only one alarm notification in the next 10 minutes even if the trigger condition is hit for multiple times. After 10 minutes, SMN sends another alarm notification if the alarm condition is met. |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


      .. figure:: /_static/images/en-us_image_0000002383984212.png
         :alt: **Figure 3** Setting the destination of a trigger action

         **Figure 3** Setting the destination of a trigger action

   d. Click **Send test message**. If a subscriber receives an email, as shown in :ref:`Figure 5 <en-us_topic_0000001938218372__fig176191820154018>`, the trigger is configured successfully.


      .. figure:: /_static/images/en-us_image_0000002417543469.png
         :alt: **Figure 4** Sending a test message

         **Figure 4** Sending a test message

      .. _en-us_topic_0000001938218372__fig176191820154018:

      .. figure:: /_static/images/en-us_image_0000002383824328.png
         :alt: **Figure 5** Email notification

         **Figure 5** Email notification

   e. Click **Create** to return to the monitor details page. The detector is successfully created.

Setting Alarm Notifications via SMN (OpenSearch 1.3.6)
------------------------------------------------------

#. Log in to the CSS management console.

   Log in using an account with CSS permissions.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. On the **OpenSearch Dashboards** page, choose **OpenSearch Plugins** > **Alerting** in the navigation tree on the left.

#. .. _en-us_topic_0000001938218372__li10273150152314:

   Create an SMN destination to send alert messages.

   a. On the **Alerting** page, click the **Destinations** tab, and click **Add destination** to configure destination information.

      .. table:: **Table 4** Destinations parameters

         +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter | Description                                                                                                                                     |
         +===========+=================================================================================================================================================+
         | Name      | User-defined destination name                                                                                                                   |
         +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------+
         | Type      | Retain the default value **SMN**.                                                                                                               |
         +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------+
         | Topic     | Select the SMN topic you have created in :ref:`Prerequisites <en-us_topic_0000001938218372__section14330827195719>` for sending alert messages. |
         +-----------+-------------------------------------------------------------------------------------------------------------------------------------------------+


      .. figure:: /_static/images/en-us_image_0000001965417005.png
         :alt: **Figure 6** Add destination

         **Figure 6** Add destination

   b. Click Create to create destinations.

   c. Return to the **Destinations** page. If the new channel is displayed, it has been created successfully.


      .. figure:: /_static/images/en-us_image_0000001938378012.png
         :alt: **Figure 7** Destination list

         **Figure 7** Destination list

#. Create a monitor and configure alarm triggers and monitoring frequency.

   a. Click the **Monitors** tab on the **Alerting** page and click **Create monitor** to configure monitor information.

      .. table:: **Table 5** Monitor parameters

         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                                                                                                                    |
         +===================================+================================================================================================================================================================================================================+
         | **Monitor details**               |                                                                                                                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Monitor name                      | User-defined monitor name                                                                                                                                                                                      |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Monitor type                      | Monitor type, which can be:                                                                                                                                                                                    |
         |                                   |                                                                                                                                                                                                                |
         |                                   | -  Per query monitor                                                                                                                                                                                           |
         |                                   | -  Per bucket monitor                                                                                                                                                                                          |
         |                                   | -  Per cluster metrics monitor                                                                                                                                                                                 |
         |                                   | -  Per document monitors                                                                                                                                                                                       |
         |                                   | -  Composite monitors                                                                                                                                                                                          |
         |                                   |                                                                                                                                                                                                                |
         |                                   | In this example, **Per query monitor** is selected. For more information, see `Monitors <https://docs.opensearch.org/2.19/observing-your-data/alerting/monitors/>`__ in the OpenSearch official documentation. |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Monitor defining method           | Monitor defining method. **Extraction query editor** is recommended.                                                                                                                                           |
         |                                   |                                                                                                                                                                                                                |
         |                                   | -  **Visual editor**                                                                                                                                                                                           |
         |                                   | -  **Extraction query editor**                                                                                                                                                                                 |
         |                                   | -  **Anomaly detector**                                                                                                                                                                                        |
         |                                   |                                                                                                                                                                                                                |
         |                                   | The options of **Monitor defining method** are determined by the **Monitor type** you selected.                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Detector                          | If **Monitor defining method** is set to **Anomaly detector**, select an exception detection task.                                                                                                             |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Frequency                         | Select the monitoring frequency and set the monitoring interval. The options include:                                                                                                                          |
         |                                   |                                                                                                                                                                                                                |
         |                                   | -  **By interval**                                                                                                                                                                                             |
         |                                   | -  **Daily**                                                                                                                                                                                                   |
         |                                   | -  **Weekly**                                                                                                                                                                                                  |
         |                                   | -  **Monthly**                                                                                                                                                                                                 |
         |                                   | -  **Custom cron expression**                                                                                                                                                                                  |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | **Data source**                   |                                                                                                                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Index                             | When **Monitor defining method** is set to **Visual editor** or **Extraction query editor**, you need to specify the index to be monitored.                                                                    |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Time field                        | When **Monitor defining method** is set to **Visual editor**, you need to specify the time field to define counting parameters such as **count**.                                                              |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | **Query**                         |                                                                                                                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Metrics                           | When **Monitor defining method** is set to **Visual editor**, you need to set the metrics range for extracting statistics.                                                                                     |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Time range for the last           | When **Monitor defining method** is set to **Visual editor**, you need to set the monitoring time range for plugins.                                                                                           |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Data filter                       | When **Monitor defining method** is set to **Visual editor**, you need to set filters for data search.                                                                                                         |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Group by                          | When **Monitor defining method** is set to **Visual editor**, you need to specify a field so that each value of the field triggers an alarm.                                                                   |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Define extraction query           | When **Monitor defining method** is set to **Extraction query editor**, you need to enter the query statement to define the monitoring.                                                                        |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Request type                      | When **Monitor type** is set to **Per cluster metrics monitor**, you need to specify the request type to monitor cluster metrics, such as the running status and CPU usage.                                    |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   b. Click **Add trigger** to add triggers and specify the alarm triggering conditions and actions to be triggered when an alarm is reported.

   c. On the **Triggers** page, set the alarm triggering sensitivity and message release on the destination end.

      .. table:: **Table 6** Trigger parameters

         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                                                                                                                                                                      |
         +===================================+==================================================================================================================================================================================================================================================================+
         | Trigger name                      | User-defined trigger name                                                                                                                                                                                                                                        |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Severity level                    | Sensitivity of a trigger, that is, the number of alarms that need to be triggered before an alarm message is sent. **1** indicates the highest sensitivity.                                                                                                      |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Trigger condition                 | Trigger condition. An alarm is triggered when the trigger condition is hit.                                                                                                                                                                                      |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Action name                       | Trigger action name                                                                                                                                                                                                                                              |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Destination                       | Select the SMN destination created in :ref:`5 <en-us_topic_0000001938218372__li10273150152314>`.                                                                                                                                                                 |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Message                           | Alarm message body By default, the subject and body are defined when the destination is an email address.                                                                                                                                                        |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Perform action                    | When **Monitor type** is set to **Per bucket monitor**, you need to set whether to send alarms in combination. The value can be:                                                                                                                                 |
         |                                   |                                                                                                                                                                                                                                                                  |
         |                                   | -  **Per execution**: A combination alarm is sent when multiple alarm triggering conditions are hit.                                                                                                                                                             |
         |                                   | -  **Per alert**: Alarms are sent separately when multiple alarm triggering conditions are hit.                                                                                                                                                                  |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Actionable alerts                 | When **Monitor type** is set to **Per bucket monitor**, set this parameter to **Per alert**. You need to set the alarms that can be executed after alarm triggering conditions are hit.                                                                          |
         |                                   |                                                                                                                                                                                                                                                                  |
         |                                   | -  **De-duplicated**: Alarms that have been triggered. OpenSearch retains the existing alarms to prevent the plugin from creating duplicate alarms.                                                                                                              |
         |                                   | -  **New**: Newly created alarms.                                                                                                                                                                                                                                |
         |                                   | -  **Completed**: Alarms that are no longer ongoing.                                                                                                                                                                                                             |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Throttling                        | Message sending frequency. It limits the number of notification messages can be received in a specified period.                                                                                                                                                  |
         |                                   |                                                                                                                                                                                                                                                                  |
         |                                   | For example, if this parameter is set to 10 minutes, SMN sends only one alarm notification in the next 10 minutes even if the trigger condition is hit for multiple times. After 10 minutes, SMN sends another alarm notification if the alarm condition is met. |
         +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+


      .. figure:: /_static/images/en-us_image_0000001938378016.png
         :alt: **Figure 8** Setting the destination of a trigger action

         **Figure 8** Setting the destination of a trigger action

   d. Click **Send test message**. If a subscriber receives an email, as shown in :ref:`Figure 10 <en-us_topic_0000001938218372__fig341274195412>`, the trigger is configured successfully.


      .. figure:: /_static/images/en-us_image_0000001938218660.png
         :alt: **Figure 9** Sending a test message

         **Figure 9** Sending a test message

      .. _en-us_topic_0000001938218372__fig341274195412:

      .. figure:: /_static/images/en-us_image_0000001965497233.png
         :alt: **Figure 10** Email notification

         **Figure 10** Email notification

   e. Click **Create** to return to the monitor details page. The detector is successfully created.
