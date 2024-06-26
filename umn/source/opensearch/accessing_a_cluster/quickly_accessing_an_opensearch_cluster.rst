:original_name: en-us_topic_0000001641003025.html

.. _en-us_topic_0000001641003025:

Quickly Accessing an OpenSearch Cluster
=======================================

OpenSearch clusters have built-in Kibana and Cerebro components. You can quickly access an OpenSearch cluster through Kibana and Cerebro.

Accessing a Cluster Through Kibana
----------------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters** > **OpenSearch**.
#. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column to go to the OpenSearch Dashboards login page.

   -  Non-security cluster: The OpenSearch Dashboards console is displayed.
   -  Security cluster: Enter the username and password on the login page and click **Log In** to go to the Kibana console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, access the cluster and perform related operations on the OpenSearch Dashboards.

Accessing a Cluster Through Cerebro
-----------------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters** > **OpenSearch**.
#. On the **Clusters** page, locate the target cluster and click **More** > **Cerebro** in the **Operation** column to go to the Cerebro login page.

   -  Non-security cluster: Click the cluster name on the Cerebro login page to go to the Cerebro console.
   -  Security cluster: Click the cluster name on the Cerebro login page, enter the username and password, and click **Authenticate** to go to the Cerebro console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access clusters through Cerebro.
