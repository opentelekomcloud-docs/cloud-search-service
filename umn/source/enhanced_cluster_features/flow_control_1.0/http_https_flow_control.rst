:original_name: en-us_topic_0000001477579352.html

.. _en-us_topic_0000001477579352:

HTTP/HTTPS Flow Control
=======================

Context
-------

You can run commands in Kibana to enable or disable HTTP/HTTPS flow control for your cluster. The command parameters are as follows.

.. table:: **Table 1** HTTP/HTTPS flow control parameters

   +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                      | Type                  | Description                                                                                                                                                                                                                                                                 |
   +================================+=======================+=============================================================================================================================================================================================================================================================================+
   | flowcontrol.http.enabled       | Boolean               | Whether to enable HTTP/HTTPS flow control. This function is disabled by default. Enabling it may affect node access performance.                                                                                                                                            |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | Value: **true** or **false**                                                                                                                                                                                                                                                |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | Default value: **false**                                                                                                                                                                                                                                                    |
   +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.http.allow         | List<String>          | IP address whitelist.                                                                                                                                                                                                                                                       |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | It can contain multiple IP addresses and masks, or an IP address list. Use commas (,) to separate multiple values. Example: *xx.xx.xx.xx*\ **/24,**\ *xx.xx.xx.xx*\ **/24**, or *xx.xx.xx.xx.xx*\ **,**\ *xx.xx.xx*.                                                        |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | The default value is null.                                                                                                                                                                                                                                                  |
   +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.http.deny          | List<String>          | IP address blacklist.                                                                                                                                                                                                                                                       |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | Multiple IP addresses and masks or an IP address list can be configured. Use commas (,) to separate multiple IP addresses and masks.                                                                                                                                        |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | The default value is null.                                                                                                                                                                                                                                                  |
   +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.http.concurrent    | Integer               | Maximum concurrent HTTP/HTTPS connections.                                                                                                                                                                                                                                  |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | Default value: Number of available cores on a node x 400                                                                                                                                                                                                                    |
   +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.http.newconnect    | Integer               | Maximum new connections that can be created for HTTP/HTTPS requests per second.                                                                                                                                                                                             |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | Default value: Number of available cores on a node x 200                                                                                                                                                                                                                    |
   +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.http.warmup_period | Integer               | Time required for the HTTP/HTTPS connection setup speed to reach the maximum. If **flowcontrol.http.newconnect** is set to **100** and **flowcontrol.http.warmup_period** is set to **5000ms**, it indicates the system can set up 100 connections per second in 5 seconds. |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | Value range: 0-10000                                                                                                                                                                                                                                                        |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | Unit: ms                                                                                                                                                                                                                                                                    |
   |                                |                       |                                                                                                                                                                                                                                                                             |
   |                                |                       | Default value: **0**                                                                                                                                                                                                                                                        |
   +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Procedure
---------

#. Log in to the CSS management console.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
#. In the navigation pane on the left, choose **Dev Tools** and run commands to enable or disable HTTP/HTTPS flow control.

   -  Enabling HTTP/HTTPS flow control for a node

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.http.enabled": true,
             "flowcontrol.http.allow": ["192.168.0.1/24", "192.168.2.1/24"],
             "flowcontrol.http.deny": "192.168.1.1/24",
             "flowcontrol.http.concurrent": 1000,
             "flowcontrol.http.newconnect": 1000,
             "flowcontrol.http.warmup_period": 0
           }
         }

      .. note::

         If all parameters are set to **null**, they will be restored to default values.

   -  Disabling HTTP/HTTPS flow control for a node

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.http.enabled": false
           }
         }
