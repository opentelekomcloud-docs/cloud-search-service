:original_name: en-us_topic_0000001477579364.html

.. _en-us_topic_0000001477579364:

One-click Traffic Blocking
==========================

You can block all connections in one click, except the connections that passes through O&M APIs, to handle unexpected traffic burst and quickly recover your cluster.

Procedure
---------

#. Log in to the CSS management console.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
#. In the navigation pane on the left, choose **Dev Tools** and run commands to enable or disable one-click traffic blocking.

   -  Enable one-click traffic blocking

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.break.enabled": true
           }
         }

   -  Disable one-click traffic blocking

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.break.enabled": false
           }
         }
