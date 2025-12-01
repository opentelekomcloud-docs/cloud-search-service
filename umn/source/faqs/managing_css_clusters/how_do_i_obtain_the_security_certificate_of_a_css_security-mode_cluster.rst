:original_name: css_02_0106.html

.. _css_02_0106:

How Do I Obtain the Security Certificate of a CSS Security-Mode Cluster?
========================================================================

The security certificate (**CloudSearchService.cer**) can be downloaded only for security-mode clusters that have enabled HTTPS access. The security certificate cannot be used in the public network environment.

-  Obtain the security certificate of an Elasticsearch cluster.

   #. Log in to the CSS management console.

   #. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   #. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

   #. Click the **Overview** tab. In the **Configuration** area, click **Download Certificate** next to **HTTPS Access**.


      .. figure:: /_static/images/en-us_image_0000002412557593.png
         :alt: **Figure 1** Downloading a security certificate

         **Figure 1** Downloading a security certificate

-  Obtain the security certificate of an OpenSearch cluster.

   #. Log in to the CSS management console.
   #. In the navigation pane on the left, choose **Clusters > OpenSearch**.
   #. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
   #. Click the **Overview** tab. In the **Configuration** area, click **Download Certificate** next to **HTTPS Access**.
