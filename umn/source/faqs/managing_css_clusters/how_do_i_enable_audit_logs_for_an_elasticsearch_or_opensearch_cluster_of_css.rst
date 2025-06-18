:original_name: css_02_0150.html

.. _css_02_0150:

How Do I Enable Audit Logs for an Elasticsearch or OpenSearch Cluster of CSS?
=============================================================================

Audit logs are disabled for Elasticsearch clusters by default.

Audit logs can be enabled for security-mode Elasticsearch 7.6.2 clusters as well as security-mode OpenSearch clusters.

#. Log in to the CSS management console.

#. In the navigation pane, choose **Clusters**. The cluster list is displayed.

#. Click the name of the target cluster to go to the cluster details page.

#. In the navigation pane on the left, choose **Parameter Configurations**. Click **Edit**, expand the **Customize** parameter, and click **Add**.

   -  For an Elasticsearch cluster, set **Key** to **opendistro_security.audit.type** and **Value** to **internal_elasticsearch**.
   -  For an OpenSearch cluster, set **Key** to **plugins.security.audit.type** and **Value** to **internal_opensearch**.


   .. figure:: /_static/images/en-us_image_0000001960397717.png
      :alt: **Figure 1** Configuring a custom parameter

      **Figure 1** Configuring a custom parameter

#. After the change is complete, click **Submit**.In the displayed **Submit Configuration** dialog box, select the box indicating "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

   If the **Status** is **Succeeded** in the parameter change list, the change has been saved.

#. Return to the cluster list and choose **More** > **Restart** in the **Operation** column to restart the cluster and make the change take effect.

#. After the cluster is restarted, click **Access Kibana** in the **Operation** column. On the displayed page, enter the username and password. The **Dev Tools** page is displayed.

#. In the **Console** page, run the **GET \_cat/indices?v** command. If there are indexes related to **.*audit\***, the audit log function is enabled.
