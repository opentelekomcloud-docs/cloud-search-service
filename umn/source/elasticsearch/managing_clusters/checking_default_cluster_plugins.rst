:original_name: css_01_0170.html

.. _css_01_0170:

Checking Default Cluster Plugins
================================

Some of the CSS enhancements over open-source Elasticsearch are delivered as default cluster plugins. These plugins are automatically injected to each cluster node during cluster creation and are loaded when the JVM process starts. CSS allows you to check these plugins through the web console or via a standard RESTful API.

Constraints
-----------

The default cluster plugins cannot be manually uninstalled.

Checking the Plugins on the CSS Console
---------------------------------------

Quickly check all default plugins supported by the current cluster without writing any code.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Choose **Cluster Settings** > **Plugins**.
#. On the **Default Plugins** tab, check the default plugins supported by the current cluster.

Checking the Plugins via an API
-------------------------------

Check the loading of default plugins on specific cluster nodes through an API, for example, when you need to troubleshoot the tokenizer.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

#. In the left navigation pane on Kibana, choose **Dev Tools**.

#. Run the following command to check the cluster's plugins:

   .. code-block:: text

      GET _cat/plugins?v

   Example response:

   .. code-block::

      name                 component                       version
      css-test-ess-esn-1-1 analysis-dynamic-synonym        1.0.1
      css-test-ess-esn-1-1 analysis-icu                    1.1.6
      css-test-ess-esn-1-1 analysis-ik                     1.0.1
      ......

   .. table:: **Table 1** Response parameters

      +-----------+------------------------------------------------------------------------------------------+
      | Parameter | Description                                                                              |
      +===========+==========================================================================================+
      | name      | Node name. Use this field to determine whether each plugin has been loaded on all nodes. |
      +-----------+------------------------------------------------------------------------------------------+
      | component | Unique plugin ID. This name is required when you configure mappings or the tokenizer.    |
      +-----------+------------------------------------------------------------------------------------------+
      | version   | Plugin version.                                                                          |
      +-----------+------------------------------------------------------------------------------------------+
