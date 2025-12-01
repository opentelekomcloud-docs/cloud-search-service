:original_name: css_02_0093.html

.. _css_02_0093:

How Do I Check the Number of Index Shards and Replicas in a CSS Elasticsearch Cluster?
======================================================================================

#. Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. Run the following command on Kibana to query the number of shards and replicas of each index:

   .. code-block:: text

      GET _cat/indices?v

   In :ref:`Figure 1 <en-us_topic_0000001933318558__fig76081122183010>`, the **pri** column indicates the number of index shards, and the **rep** column indicates the number of replicas. Once an index is created, its **pri** value cannot be changed, but its **rep** value can be changed.

   .. _en-us_topic_0000001933318558__fig76081122183010:

   .. figure:: /_static/images/en-us_image_0000001960397705.png
      :alt: **Figure 1** Querying index information

      **Figure 1** Querying index information
