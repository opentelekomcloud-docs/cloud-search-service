:original_name: en-us_topic_0000001978134941.html

.. _en-us_topic_0000001978134941:

How Do I Check the List of Default Plugins for Elasticsearch and OpenSearch Clusters?
=====================================================================================

Default plugins are available for the Elasticsearch and OpenSearch clusters in CSS. You can check the default plugins on the CSS web console or on Kibana or OpenSearch Dashboards.

Checking Plugins on the CSS Console
-----------------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters**. Click the target cluster name and go to the **Cluster Information** page.
#. Click the **Plugins** tab.
#. On the **Default** page, check the default plugins supported by the current version.

Checking Plugins on Kibana or OpenSearch Dashboards
---------------------------------------------------

#. Log in to the CSS management console.

#. In the navigation pane, choose **Clusters**. Locate the target cluster and click **Access Kibana** in the **Operation** column to log in to Kibana (for Elasticsearch) or OpenSearch Dashboards (for OpenSearch).

   -  For a non-security mode cluster: The Kibana or OpenSearch Dashboards console is displayed.
   -  For a security-mode cluster: Enter the username and password on the login page and click **Log In** to go to the Kibana or OpenSearch Dashboards console. The default username is **admin** and the password is the administrator password you specified during cluster creation.

#. Go to **Dev Tools** and run the following command to view the cluster plugin information:

   .. code-block:: text

      GET _cat/plugins?v

   The following is an example of the response body:

   .. code-block::

      name                 component                       version
      css-test-ess-esn-1-1 analysis-dynamic-synonym        7.6.2-xxxx-ei-css-v1.0.1
      css-test-ess-esn-1-1 analysis-icu                    7.6.2-xxxx-ei-css-v1.1.6
      css-test-ess-esn-1-1 analysis-ik                     7.6.2-xxxx-ei-css-v1.0.1
      ......

   **name** indicates the cluster node name, **component** indicates the plugin name, and **version** indicates the plugin version.
