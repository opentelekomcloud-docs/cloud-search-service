:original_name: css_01_0179.html

.. _css_01_0179:

HTTP Status Code Monitoring
===========================

Context
-------

When an external system accesses Elasticsearch through the HTTP protocol, a response and the corresponding status code are returned. The open-source Elasticsearch server does not collect the status code, so users cannot monitor Elasticsearch APIs status or cluster request status. CSS allows you to monitor the HTTP status codes of clusters.

Prerequisites
-------------

Currently, only clusters of versions 7.6.2 and 7.10.2 support HTTP status code monitoring.

Obtaining Status Codes
----------------------

#. Log in to the CSS management console.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
#. In the navigation tree on the left, choose **Dev Tools**.
#. On the console page of **Dev Tools**, run commands based on the cluster version.

   -  For clusters of version 7.6.2, run the following command to obtain the status code statistics:

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

   -  For clusters of version 7.10.2, run the following command to obtain the status code statistics:

      .. code-block:: text

         GET _nodes/stats/http

      Example response:

      .. code-block::

         {
         // ...
           "cluster_name" : "css-2985",
           "nodes" : {
         // ...
             "omvR9_W-TsGApraMApREjA" : {

         // ...
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
