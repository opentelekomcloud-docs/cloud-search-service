:original_name: css_02_0101.html

.. _css_02_0101:

How Do I Modify the TLS Algorithm for a CSS Cluster?
====================================================

The TLS algorithm can be modified for Elasticsearch 7.6.2 and later as well as OpenSearch clusters.

#. Log in to the CSS management console.

#. In the navigation pane on the left, expand **Clusters**. Select a cluster type based on the target cluster. The cluster list is displayed.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Cluster Settings** > **Parameter Settings**.

#. Click **Edit**, expand **Custom**, and click **Add**.

   -  For an Elasticsearch cluster, add the **opendistro_security.ssl.http.enabled_ciphers** parameter and set it to **['TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384']**.
   -  For an OpenSearch cluster, add the **plugins.security.ssl.http.enabled_ciphers** parameter and set it to **['TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384']**.

   If the parameter value contains multiple algorithms, enclose the value with a pair of square brackets ([]). If the parameter value is a single algorithm, enclose the value with a pair of single quotation marks(' ').

#. After the change is complete, click **Submit**.In the displayed **Submit Configuration** dialog box, select the box indicating "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

   If the **Status** is **Succeeded** in the parameter change list, the change has been saved.

#. Click **Restart** in the upper right corner to restart the cluster, thus making the change take effect.
