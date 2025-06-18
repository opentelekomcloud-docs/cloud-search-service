:original_name: css_01_0427.html

.. _css_01_0427:

Configuring Kernel Monitoring for an Elasticsearch Cluster
==========================================================

Scenario
--------

.. table:: **Table 1** Introduction to cluster kernel monitoring

   +-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------+
   | Enhanced Monitoring Feature | Description                                                                                                                                                                                                                                                                                                                                               | Cluster Version                           | Details                                                                 |
   +=============================+===========================================================================================================================================================================================================================================================================================================================================================+===========================================+=========================================================================+
   | P99 latency                 | Open-source Elasticsearch provides only the average latency metric when monitoring responses to search requests. This may not accurately reflect the actual search performance of a cluster. To improve on this, the P99 latency metric is added in CSS to monitor the 99th percentile latency of each cluster.                                           | Elasticsearch 7.6.2, Elasticsearch 7.10.2 | :ref:`Monitoring P99 Latency <css_01_0427__section7236204762019>`       |
   +-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------+
   | HTTP status codes           | When you access Elasticsearch through HTTP, you receive HTTP status codes in response to your requests. The native open-source Elasticsearch does not collect statistics on these status codes. To improve on this, HTTP status code monitoring is added in CSS, allowing you to monitor HTTP status codes and get a sense of how the service is running. | Elasticsearch 7.6.2, Elasticsearch 7.10.2 | :ref:`Monitoring HTTP Status Codes <css_01_0427__section1367052018215>` |
   +-----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------+-------------------------------------------------------------------------+

Accessing a Cluster
-------------------

#. Log in to the CSS management console.
#. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column to access Kibana.
#. Click **Dev Tools** in the navigation tree on the left.

.. _css_01_0427__section7236204762019:

Monitoring P99 Latency
----------------------

Run the following command to obtain the P99 latency of the current cluster:

.. code-block:: text

   GET /search/stats/percentile

An example output is as follows:

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

.. table:: **Table 2** Response parameters

   +--------------+----------------------------------------------------------------+
   | Parameter    | Description                                                    |
   +==============+================================================================+
   | overall      | Statistics between cluster starting and the current time.      |
   +--------------+----------------------------------------------------------------+
   | last_one_day | Statistics for the most recent day.                            |
   +--------------+----------------------------------------------------------------+
   | latest       | Statistics from the most recent resetting to the current time. |
   +--------------+----------------------------------------------------------------+

.. note::

   -  The calculated P99 latency is an estimation, but it is more precise than the P50 latency.
   -  When a cluster is restarted, its P99 latency data is cleared, and is re-measured after the cluster restarts successfully.

The command used for monitoring the P99 latency of clusters can also be used to set other configuration items.

-  You can customize the percentile of latency to be monitored.

   For example, run the following command to show the P1, P50, and P90 latency values:

   .. code-block:: text

      GET /search/stats/percentile
      {
        "percents": [1, 50, 90]
      }

-  You can manually reset the **latest** statistics.

   Run the following command to reset the **latest** statistics:

   .. code-block:: text

      POST /search/stats/reset

   If **ok** is returned, the reset is successful.

   .. code-block::

      {
        "nodes" : {
          "css-c9c8-ess-esn-1-1" : "ok"
        }
      }

.. _css_01_0427__section1367052018215:

Monitoring HTTP Status Codes
----------------------------

The command used for monitoring HTTP status codes varies with cluster versions.

-  In an Elasticsearch 7.6.2 cluster, run the following command to obtain statistics on HTTP status codes:

   .. code-block:: text

      GET /_nodes/http_stats

   Example response:

   .. code-block::

      {
          "_nodes" : {
            "total" : 1,
            "successful" : 1,
            "failed" : 0   },
           "cluster_name" : "css-8362",
           "nodes" : {
            "F9IFdQPARaOJI7oL7HOXtQ" : {
               "http_code" : {
                  "200" : 114,
                  "201" : 5,
                  "429" : 0,
                  "400" : 7,
                  "404" : 0,
                  "405" : 0
                 }
               }
            }
       }

-  In an Elasticsearch 7.10.2 cluster, run the following command to obtain statistics on HTTP status codes:

   .. code-block:: text

      GET _nodes/stats/http

   Example response:

   .. code-block::

      {
      ......
        "cluster_name" : "css-2985",
        "nodes" : {
      ......
          "omvR9_W-TsGApraMApREjA" : {
      ......
            "http" : {
              "current_open" : 4,
              "total_opened" : 37,
              "http_code" : {
                "200" : 25,
                "201" : 7,
                "429" : 0,
                "400" : 3,
                "404" : 0,
                "405" : 0
              }
            }
          }
        }
      }
