:original_name: css_02_0101.html

.. _css_02_0101:

Can I Modify the TLS Algorithm of an Elasticsearch Cluster?
===========================================================

You can modify TLS algorithms in CSS 7.6.2 and later versions.

#. Log in to the CSS management console.

#. In the navigation pane, choose **Clusters**. The cluster list is displayed.

#. Click the name of the target cluster to go to the cluster details page.

#. Select **Parameter Configurations**, click **Edit**, expand the **Customize** parameter, and click **Add**.

   Add the **opendistro_security.ssl.http.enabled_ciphers** parameter and set it to **['TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256', 'TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384']**.

   .. note::

      If the parameter value contains multiple algorithm protocols, enclose the value with a pair of square brackets ([]). If the parameter value is a single algorithm protocol, enclose the value with a pair of single quotation marks(' ').

#. After the modification is complete, click **Submit**.In the displayed **Submit Configuration** dialog box, select the box indicating "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

   If the **Status** is **Succeeded** in the parameter modification list, the modification has been saved.

#. Return to the cluster list and choose **More** > **Restart** in the **Operation** column to restart the cluster and make the modification take effect.
