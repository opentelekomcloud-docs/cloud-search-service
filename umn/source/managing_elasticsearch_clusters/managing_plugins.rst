:original_name: css_01_0078.html

.. _css_01_0078:

Managing Plugins
================

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

#. Go to **Dev Tools** and run the following command to view the cluster plugin information:

   .. code-block:: text

      GET _cat/plugins?v

   The following is an example of the response body:

   .. code-block::

      name                 component                       version
      css-2918-ess-esn-1-1 analysis-dynamic-synonym        7.10.2-h0.cbu.css.v1.0.0.0.r1
      css-2918-ess-esn-1-1 analysis-icu                    7.10.2-h0.cbu.css.v1.0.0.3.r1
      css-2918-ess-esn-1-1 analysis-ik                     7.10.2-h0.cbu.css.v1.0.0.0.r1
      ......

   **name** indicates the cluster node name, **component** indicates the plugin name, and **version** indicates the plugin version.
