:original_name: css_02_0089.html

.. _css_02_0089:

How Do I Change the Number of Replicas for Elasticsearch Indexes in CSS?
========================================================================

When creating an index for an Elasticsearch cluster, you can specify the number of shards, that is, the number of primary shards. Once an index is created, the number of primary shards cannot be changed, but the number of replicas can be changed. **Number of replica shards = Number of primary shards x Number of replicas.**

#. Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. On the Kibana console, run the following command to check the number of replicas for each Elasticsearch index:

   .. code-block:: text

      GET _cat/indices?v


   .. figure:: /_static/images/en-us_image_0000002021082885.png
      :alt: **Figure 1** Checking the number of replicas

      **Figure 1** Checking the number of replicas

#. Run the following command to configure the number of index replicas:

   .. code-block:: text

      PUT /indexname/_settings
      {
        "number_of_replicas" :1       //Number of replicas
      }

   **indexname** indicates the name of the index to be modified, and **number_of_replicas** indicates the number of replicas to be set.
