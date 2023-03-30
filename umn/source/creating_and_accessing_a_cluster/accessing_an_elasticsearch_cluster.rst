:original_name: css_01_0190.html

.. _css_01_0190:

Accessing an Elasticsearch Cluster
==================================

Elasticsearch clusters have built-in Kibana and Cerebro components. You can quickly access an Elasticsearch cluster through Kibana and Cerebro.

Access a Cluster Through Kibana
-------------------------------

#. Log in to the CSS management console.
#. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column to go to the Kibana login page.

   -  Non-security cluster: The Kibana console is displayed.
   -  Security cluster: Enter the username and password on the login page and click **Log In** to go to the Kibana console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access the Elasticsearch cluster through Kibana.

Accessing a Cluster Through Cerebro
-----------------------------------

#. Log in to the CSS management console.
#. On the **Clusters** page, locate the target cluster and click **More** > **Cerebro** in the **Operation** column to go to the Cerebro login page.

   -  Non-security cluster: Click the cluster name on the Cerebro login page to go to the Cerebro console.
   -  Security cluster: Click the cluster name on the Cerebro login page, enter the username and password, and click **Authenticate** to go to the Cerebro console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access the Elasticsearch cluster through Cerebro.
