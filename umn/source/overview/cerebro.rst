:original_name: css_04_0022.html

.. _css_04_0022:

Cerebro
=======

Cerebro is an open-source Elasticsearch web visualized management tool built using Scala, Play Framework, AngularJS, and Bootstrap. Cerebro allows you to manage clusters on a visualized page, such as executing REST requests, modifying Elasticsearch configurations, monitoring real-time disks, cluster load, and memory usage.

Accessing Cerebro with a Few Clicks
-----------------------------------

CSS is integrated with Cerebro. You can access Cerebro with a few clicks, without installing Cerebro.

Log in to the CSS management console. In the left navigation pane, click **Clusters**. On the displayed **Clusters** page, locate the row containing the target cluster and choose **More** > **Access Cerebro** in the **Operation** column.

On the displayed page, enter one private access address of the cluster.

-  If the cluster does not have the security mode enabled, enter **http://**\ *IP address*\ **:9200**.
-  If the cluster has the security mode enabled, enter **https://**\ *IP address*\ **:9200** and then enter the username and password to log in.

Cerebro Functions
-----------------

CSS is fully compatible with the open-source Cerebro and the latest version Cerebro 0.8.4 is supported. Cerebro delivers the following functions:

-  Elasticsearch visualized and real-time load monitoring
-  Elasticsearch visualized data management
