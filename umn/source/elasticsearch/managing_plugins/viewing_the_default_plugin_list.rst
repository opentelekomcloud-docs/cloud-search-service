:original_name: css_01_0078.html

.. _css_01_0078:

Viewing the Default Plugin List
===============================

CSS clusters have default plugins. You can view the default plugin information on the console or Kibana.

Viewing Plugins on the Console
------------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters**. Click the target cluster name and go to the **Basic Information** page of the cluster.
#. Click the **Plugins** tab.
#. On the **Default** page, view default plugins supported by the current version.

Viewing Plugins on the Kibana
-----------------------------

#. Log in to the CSS management console.

#. In the navigation pane, choose **Clusters**. Locate the target cluster and click **Access Kibana** in the **Operation** column to log in to Kibana.

   -  Non-security cluster: The Kibana console is displayed.
   -  Security cluster: Enter the username and password on the login page and click **Log In** to go to the Kibana console. The default username is **admin** and the password is the administrator password you specified during cluster creation.

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
