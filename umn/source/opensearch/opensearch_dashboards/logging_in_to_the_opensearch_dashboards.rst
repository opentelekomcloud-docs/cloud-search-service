:original_name: en-us_topic_0000001591776274.html

.. _en-us_topic_0000001591776274:

Logging In to the OpenSearch Dashboards
=======================================

Prerequisites
-------------

An OpenSearch cluster has been created.

Procedure
---------

-  Logging in to the console

   #. Log in to the CSS management console.
   #. In the navigation pane, choose **Clusters** > **OpenSearch**.
   #. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column to go to the OpenSearch login page.

      -  Non-security cluster: The OpenSearch Dashboards console is displayed.

      -  Security cluster: Enter the username and password on the login page and click **Log In** to go to the OpenSearch console. The default username is **admin** and the password is the one specified during cluster creation.


         .. figure:: /_static/images/en-us_image_0000001607915032.png
            :alt: **Figure 1** Logging in to OpenSearch

            **Figure 1** Logging in to OpenSearch

   #. After the login is successful, access the cluster and perform related operations on the OpenSearch Dashboards.

-  Logging in using an EIP

   If you have enabled Kibana public access during cluster creation, you can use the Kibana public IP address to log in to the cluster. For details, see .
