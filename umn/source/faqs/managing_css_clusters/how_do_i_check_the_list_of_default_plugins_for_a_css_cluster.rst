:original_name: css_02_0078.html

.. _css_02_0078:

How Do I Check the List of Default Plugins for a CSS Cluster?
=============================================================

Default plugins are available for the Elasticsearch and OpenSearch clusters in CSS. You can check them on the CSS management console or query them by running commands on Kibana or OpenSearch Dashboards.

Querying Default Plugins on the CSS Management Console
------------------------------------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, expand **Clusters**. Select a cluster type based on the target cluster. The cluster list is displayed.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Choose **Cluster Settings** > **Plugins**.
#. On the **Default Plugins** tab, check the default plugins supported by the current cluster.

Querying Default Plugins by Running Commands
--------------------------------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, expand **Clusters**. Select a cluster type based on the target cluster. The cluster list is displayed.

#. For an Elasticsearch cluster, click **Kibana** in the **Operation** column to log in to Kibana. For an OpenSearch cluster, click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. Expand the menu in the upper-left corner, and choose **Dev Tools**.

#. Run the following command to check the cluster's plugins:

   .. code-block:: text

      GET _cat/plugins?v

   The following is an example of the response body:

   .. code-block::

      name                 component                       version
      css-test-ess-esn-1-1 analysis-dynamic-synonym        x.x.x-xxxx-ei-css-v1.0.1
      css-test-ess-esn-1-1 analysis-icu                    x.x.x-xxxx-ei-css-v1.1.6
      css-test-ess-esn-1-1 analysis-ik                     x.x.x-xxxx-ei-css-v1.0.1
      ......

   **name** indicates the cluster node name, **component** indicates the plugin name, and **version** indicates the plugin version.
