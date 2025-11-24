:original_name: css_02_0150.html

.. _css_02_0150:

How Do I Enable Audit Logs for a CSS Cluster?
=============================================

Audit logs can be enabled for security-mode Elasticsearch 7.6.2 clusters as well as security-mode OpenSearch clusters.

Audit logs are disabled for Elasticsearch clusters by default.

#. Log in to the CSS management console.

#. In the navigation pane on the left, expand **Clusters**. Select a cluster type based on the target cluster. The cluster list is displayed.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Cluster Settings** > **Parameter Settings**.

#. Click **Edit**, expand **Custom**, and click **Add**.

   -  For an Elasticsearch cluster, set **Key** to **opendistro_security.audit.type** and **Value** to **internal_elasticsearch**.
   -  For an OpenSearch cluster, set **Key** to **plugins.security.audit.type** and **Value** to **internal_opensearch**.

#. After the change is complete, click **Submit**.In the displayed **Submit Configuration** dialog box, select the box indicating "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

   If the **Status** is **Succeeded** in the parameter change list, the change has been saved.

#. Click **Restart** in the upper right corner to restart the cluster, thus making the change take effect.

#. After cluster restart, check whether audit logs have been enabled.

   a. For an Elasticsearch cluster, click **Kibana** in the **Operation** column to log in to Kibana. For an OpenSearch cluster, click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

   b. Expand the menu in the upper-left corner, and choose **Dev Tools**.

   c. Run the following command. If the result contains indexes whose name contain **.*audit\***, audit logs have been enabled.

      .. code-block:: text

         GET _cat/indices?v
