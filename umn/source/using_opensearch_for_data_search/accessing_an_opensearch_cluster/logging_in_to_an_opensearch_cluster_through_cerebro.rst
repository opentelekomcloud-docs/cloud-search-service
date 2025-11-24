:original_name: css_01_0029.html

.. _css_01_0029:

Logging In to an OpenSearch Cluster Through Cerebro
===================================================

Cerebro is an open-source Elasticsearch web admin tool, designed for real-time monitoring and efficient cluster operations. Cerebro works for OpenSearch just as well. In CSS, Cerebro is pre-built for each OpenSearch cluster. You can start Cerebro with one click, without installing anything. Cerebro allows you to quickly check a cluster's health status, node distribution, and index details. For routine O&M tasks, including shard adjustment, index management, and performance monitoring, we recommend using Cerebro. Its intuitive cluster topology views and comprehensive management features streamline O&M workflows, reducing complexity while improving efficiency. Cerebro is suitable for different roles, including developers, O&M teams, and data analysts.

Accessing a Cluster Through Cerebro on the CSS Console
------------------------------------------------------

The OpenSearch clusters created in CSS provide a built-in Cerebro component, using which you can quickly access these clusters.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. Find the target cluster, and choose **More** > **Cerebro** in the **Operation** column. The Cerebro login page is displayed.

   -  Non-security cluster: Click the cluster name on the Cerebro login page to go to the Cerebro console.
   -  Security cluster: Click the cluster name on the Cerebro login page, enter the username and password, and click **Authenticate** to go to the Cerebro console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access clusters through Cerebro.

Accessing a Cluster Using an In-House Built Cerebro
---------------------------------------------------

.. caution::

   When using in-house built Cerebro to access a cluster, make sure the network between them is connected.

#. Obtain the cluster access address. For details about how to obtain the cluster access address for different network configurations, see :ref:`Network Configuration <en-us_topic_0000001992165561__en-us_topic_0000001975823337_section855085010198>`.
#. Start Cerebro, and enter the cluster access address.

   -  For a cluster in security mode, enter https://*access address*:9200.

      To log in to a cluster in security mode, you need to provide a username and password.

   -  For a cluster in non-security mode, enter http://*access address*:9200.
