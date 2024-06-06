:original_name: en-us_topic_0000001477419748.html

.. _en-us_topic_0000001477419748:

P99 Latency Monitoring
======================

Context
-------

The Elasticsearch community only discusses how to monitor the average latency of search requests, which cannot reflect the actual search performance of a cluster. To enhance monitoring, CSS allows you to monitor the P99 latency of search requests in clusters.

Prerequisites
-------------

Currently, only clusters of version 7.6.2 and 7.10.2 support P99 latency monitoring.

Obtaining Monitoring Information
--------------------------------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. In the navigation tree on the left, choose **Dev Tools** and run the following command to check the P99 latency of the current cluster:

   .. code-block:: text

      GET /search/stats/percentile

   Example response:

   .. code-block::

      {
        "overall" : {
          "1.0" : 2.0,
          "5.0" : 2.0,
          "25.0" : 6.5,
          "50.0" : 19.5,
          "75.0" : 111.0,
          "95.0" : 169.0,
          "99.0" : 169.0,
          "max" : 169.0,
          "min" : 2.0
        },
        "last_one_day" : {
          "1.0" : 2.0,
          "5.0" : 2.0,
          "25.0" : 6.5,
          "50.0" : 19.5,
          "75.0" : 111.0,
          "95.0" : 169.0,
          "99.0" : 169.0,
          "max" : 169.0,
          "min" : 2.0
        },
        "latest" : {
          "1.0" : 26.0,
          "5.0" : 26.0,
          "25.0" : 26.0,
          "50.0" : 26.0,
          "75.0" : 26.0,
          "95.0" : 26.0,
          "99.0" : 26.0,
          "max" : 26.0,
          "min" : 26.0
        }
      }

   .. note::

      -  In the response, **overall** indicates all the statistics that have been collected since the cluster startup, **last_one_day** indicates the statistics collected in the last day, and **latest** indicates the statistics that have been collected since the last reset.
      -  The calculated P99 latency is an estimation. It is more precise than the P50 latency.
      -  The P99 latency of a cluster is cleared and recalculated if the cluster is restarted.

Other Operations
----------------

-  Define percentage.

   You can run the following command to specify the percentage:

   .. code-block:: text

      GET /search/stats/percentile
      {
        "percents": [1, 50, 90]
      }

-  Reset the **latest** statistics.

   You can run the following command to reset the **latest** statistics:

   .. code-block:: text

      POST /search/stats/reset

   Example response:

   .. code-block::

      {
        "nodes" : {
          "css-c9c8-ess-esn-1-1" : "ok"
        }
      }
