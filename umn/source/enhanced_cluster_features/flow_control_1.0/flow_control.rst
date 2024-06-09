:original_name: en-us_topic_0000001528299577.html

.. _en-us_topic_0000001528299577:

Flow Control
============

Flow control can be implemented via an independent API.

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. In the navigation pane on the left, choose **Dev Tools** and run the commands to query traffic control information.

   -  Check the traffic control status of all nodes.

      .. code-block:: text

         GET /_nodes/stats/filter

   -  View the traffic control status of a specific node.

      .. code-block:: text

         GET /_nodes/{nodeId}/stats/filter

      **{nodeId}** indicates the ID of the node you want to check.

   Example response:

   .. code-block::

      {
        "_nodes" : {
          "total" : 1,
          "successful" : 1,
          "failed" : 0
        },
        "cluster_name" : "css-flowcontroller",
        "nodes" : {
          "ElBRNCMbTj6L1C-Wke-Dnw" : {
            "name" : "css-flowcontroller-ess-esn-1-1",
            "host" : "10.0.0.133",
            "timestamp" : 1613979513747,
            "flow_control" : {
              "transport" : {
                "concurrent_req" : 0,
                "rejected_concurrent" : 0,
                "rejected_new" : 0,
                "rejected_deny" : 0
              },
              "http" : {
                "concurrent_req" : 0,
                "rejected_concurrent" : 0,
                "rejected_new" : 0,
                "rejected_deny" : 0
              },
              "memory" : {
                "memory_allow" : 41,
                "memory_rejected" : 0
              },
              "cpu": {
                "rejected_cpu" : 0
              }
              "ip_address" : [
                {
                  "ip" : "/10.0.0.198",
                  "count" : 453
                },
                {
                  "ip" : "/198.19.49.1",
                  "count" : 42
                }
              ],
              "url_sample" : [
                {
                  "url" : "/*/_search?pretty=true",
                  "method" : "GET",
                  "remote_address" : "/10.0.0.198:16763",
                  "count" : 1
                }
              ]
            }
        }
      }

   In the response, the information of each node is separated. The **http** field records the numbers of concurrent connections and new connections. The **memory** records memory flow control statistics. The **ip_address** field records the recent client IP addresses that are accessed most recently. The **url_sample** field records the recent URLs that are requested most frequently. The **cpu** field records CPU flow control statistics.

   .. table:: **Table 1** Response parameters

      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter           | Description                                                                                                                                                                                                                                                                                                                                |
      +=====================+============================================================================================================================================================================================================================================================================================================================================+
      | concurrent_req      | Number of TCP connections of a node, which is recorded no matter whether flow control is enabled. This value is similar to the value of **current_open** of the **GET /_nodes/stats/http** API but is smaller, because whitelisted IP addresses and internal node IP addresses are not counted.                                            |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | rejected_concurrent | Number of concurrent connections rejected during HTTP flow control. This value is not cleared when HTTP flow control is disabled.                                                                                                                                                                                                          |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | rejected_new        | Number of new connections rejected during HTTP flow control. This value is not cleared when HTTP flow control is disabled.                                                                                                                                                                                                                 |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | rejected_deny       | Number of requests rejected based on the blacklist during HTTP flow control. This value is not cleared when HTTP flow control is disabled.                                                                                                                                                                                                 |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | memory_allow        | Number of allowed requests during memory flow control. This parameter takes effect when memory flow control is enabled, and its value is not cleared after memory flow control is disabled. The requests from the paths in the **allow_path** whitelist are not recorded. If **allow_path** is set to **\*\***, no requests are recorded.  |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | memory_rejected     | Number of rejected requests during memory flow control. This parameter takes effect when memory flow control is enabled, and its value is not cleared after memory flow control is disabled. The requests from the paths in the **allow_path** whitelist are not recorded. If **allow_path** is set to **\*\***, no requests are recorded. |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | rejected_cpu        | Number of requests rejected when the CPU flow control threshold is exceeded. This parameter takes effect when CPU flow control is enabled, and its value is not cleared after CPU flow control is disabled.                                                                                                                                |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | ip_address          | IP addresses and the number of requests. For details, see :ref:`Table 2 <en-us_topic_0000001528299577__en-us_topic_0000001273451905_table8881825155010>`.                                                                                                                                                                                  |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | url_sample          | Request path sampling. The number of URLs of a request are collected based on the configured time and sampling interval. For details, see :ref:`Table 3 <en-us_topic_0000001528299577__en-us_topic_0000001273451905_table72712520501>`.                                                                                                    |
      +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0000001528299577__en-us_topic_0000001273451905_table8881825155010:

   .. table:: **Table 2** ip_address

      ========= =============================================
      Parameter Description
      ========= =============================================
      ip        Source IP address for accessing the node.
      method    Number of access requests from an IP address.
      ========= =============================================

   .. _en-us_topic_0000001528299577__en-us_topic_0000001273451905_table72712520501:

   .. table:: **Table 3** url_sample

      ============== ================================================
      Parameter      Description
      ============== ================================================
      url            Request URL
      method         Method corresponding to the request path
      remote_address Source IP address and port number of the request
      count          How many times a path is sampled
      ============== ================================================
