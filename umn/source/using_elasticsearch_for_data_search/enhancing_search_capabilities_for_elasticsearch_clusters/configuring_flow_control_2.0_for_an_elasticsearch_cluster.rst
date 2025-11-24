:original_name: css_01_0192.html

.. _css_01_0192:

Configuring Flow Control 2.0 for an Elasticsearch Cluster
=========================================================

Configure flow control policies for your Elasticsearch cluster in both the inbound and outbound directions, ensuring cluster stability by safeguarding against abnormal traffic.

An Elasticsearch cluster can become overloaded due to traffic surges, malicious requests, and internal resource competition, which can even lead to node failures. Through policies like client request throttling, write backpressure, and traffic pattern analysis, flow control ensures proper resource allocation, thereby protecting clusters from overload. It covers the following scenarios:

-  High-concurrency write handling: mitigates the risk of out-of-memory (OOM) exceptions under heavy write loads.
-  Security defense: controls access by IP address using both blacklists and whitelists.
-  Emergency response: blocks malicious or abnormal traffic in one click.
-  Performance optimization: optimizes flow control thresholds and policies based on collected statistics.

How the Feature Works
---------------------

.. table:: **Table 1** Flow control policies

   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | Policy                     | How It Works                                                                                                                                                                                                                                                                                                                                                                            | Details                                                                                               |
   +============================+=========================================================================================================================================================================================================================================================================================================================================================================================+=======================================================================================================+
   | HTTP/HTTPS flow control    | -  You can control cluster access by client IP address or subnet through the HTTP/HTTPS blacklist or whitelist. If an IP address is in the blacklist, the client is disconnected right away and all its requests are rejected. The whitelist takes precedence over the blacklist. If a client IP address is on both the blacklist and whitelist, requests from it will not be rejected. | :ref:`Enabling HTTP/HTTPS Flow Control per Node <en-us_topic_0000001938218516__section1023014371242>` |
   |                            | -  Flow control based on concurrent HTTP/HTTPS connections limits the total number of HTTP/HTTPS connections to a node per second.                                                                                                                                                                                                                                                      |                                                                                                       |
   |                            | -  Flow control based on new HTTP/HTTPS connections limits the number of new connections to a node.                                                                                                                                                                                                                                                                                     |                                                                                                       |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | Memory flow control        | Memory flow control limits write traffic based on the node heap memory. It uses a backpressure mechanism to ask the client to slow down or stop sending requests. In the meantime, it triggers garbage collection to reclaim resources, and continues to process requests based on heap memory available.                                                                               | :ref:`Enabling Memory Flow Control <en-us_topic_0000001938218516__section12926193210818>`             |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | Request sampling           | Request sampling can record the access of client IP addresses and the type of requests from the client. Based on such statistics, you can identify the access traffic of specific client IP addresses and analyze write and query traffic from them.                                                                                                                                    | :ref:`Enabling Request Sampling <en-us_topic_0000001938218516__section846243514132>`                  |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | One-click traffic blocking | One-click traffic blocking blocks all client connections to a node. This, however, does not include connections for Kibana access, CSS O&M, or monitoring APIs. The purpose is to protect cluster nodes in the face of traffic spikes or to quickly restore clusters.                                                                                                                   | :ref:`Enable One-Click Traffic Blocking <en-us_topic_0000001938218516__section364216459204>`          |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | Flow control               | Flow control provides an independent API for checking traffic statistics, including the number of existing client connections as well as client connections where backpressure has been applied. You can evaluate the flow control threshold and analyze the cluster load based on these statistics.                                                                                    | :ref:`Viewing Flow Control Information <en-us_topic_0000001938218516__section03781045277>`            |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | Access logging             | Access logs record the URLs and bodies of HTTP/HTTPS requests received by nodes within a period of time. You can analyze the current traffic load based on the access logs.                                                                                                                                                                                                             | :ref:`Enabling and Viewing Access Logs <en-us_topic_0000001938218516__section1626791610277>`          |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+
   | Access logging in files    | Any cluster access is recorded in the **{Cluster name\ \_access_log.log}** file. You can use the log backup function to view detailed access logs on OBS.                                                                                                                                                                                                                               | :ref:`Enabling Access Logging in Files <en-us_topic_0000001938218516__section072285622916>`           |
   +----------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------+

Constraints
-----------

-  Elasticsearch 7.6.2 and Elasticsearch 7.10.2 clusters created after January 2023 support Flow Control 2.0 only, whereas those created before that support Flow Control 1.0 only.
-  Flow control may hurt the performance of some nodes.
-  If flow control is enabled, user requests that exceed the flow control threshold will be rejected.
-  Enabling memory flow control may hurt the performance of some search requests or cause some Kibana search requests to fail.
-  Enabling access logging may hurt cluster performance.
-  Memory flow control is based on request paths. Avoid configuring too many paths or paths that are too long, as they may hurt cluster performance.

Logging In to Kibana
--------------------

Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

.. _en-us_topic_0000001938218516__section1023014371242:

Enabling HTTP/HTTPS Flow Control per Node
-----------------------------------------

#. Run the following command to enable HTTP/HTTPS flow control for cluster nodes:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.http.enabled": true,
          "flowcontrol.http.allow": ["192.168.0.1/24", "192.168.2.1/24"],
          "flowcontrol.http.deny": "192.168.1.1/24",
          "flowcontrol.http.concurrent": 1000,
          "flowcontrol.http.newconnect": 1000,
          "flowcontrol.http.warmup_period": 0
        }
      }

   .. table:: **Table 2** Configuration items for HTTP/HTTPS flow control

      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item             | Type                  | Description                                                                                                                                                                                                                                                                          |
      +================================+=======================+======================================================================================================================================================================================================================================================================================+
      | flowcontrol.http.enabled       | Boolean               | Whether to enable HTTP/HTTPS flow control. HTTP/HTTPS flow control is disabled by default. Enabling it may affect node access performance.                                                                                                                                           |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | Value: **true** or **false**                                                                                                                                                                                                                                                         |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | Default value: **false**                                                                                                                                                                                                                                                             |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.allow         | List<String>          | IP address whitelist.                                                                                                                                                                                                                                                                |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | It can contain multiple IP addresses and subnet masks, or lists of IP addresses. Use commas (,) to separate different items. Example: **xx.xx.xx.xx/24,xx.xx.xx.xx/24**, or **xx.xx.xx.xx,xx.xx.xx.xx**.                                                                             |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | The default value is null.                                                                                                                                                                                                                                                           |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.deny          | List<String>          | IP address blacklist.                                                                                                                                                                                                                                                                |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | It can contain multiple IP addresses and subnet masks, or lists of IP addresses. Use commas (,) to separate different items.                                                                                                                                                         |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | The default value is null.                                                                                                                                                                                                                                                           |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.concurrent    | Integer               | Maximum concurrent HTTP/HTTPS connections.                                                                                                                                                                                                                                           |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | Default value: Number of available cores on a node x 600.                                                                                                                                                                                                                            |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.newconnect    | Integer               | Maximum new connections that can be created for HTTP/HTTPS requests per second.                                                                                                                                                                                                      |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | Default value: Number of available cores on a node x 200.                                                                                                                                                                                                                            |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.warmup_period | Integer               | Time required for the HTTP/HTTPS connection setup speed to reach the maximum. If **flowcontrol.http.newconnect** is set to **100** and **flowcontrol.http.warmup_period** is set to **5000ms**, it indicates the system can create up to 100 connections per second 5 seconds later. |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | Value range: 0-10000                                                                                                                                                                                                                                                                 |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | Unit: ms                                                                                                                                                                                                                                                                             |
      |                                |                       |                                                                                                                                                                                                                                                                                      |
      |                                |                       | Default value: **0**                                                                                                                                                                                                                                                                 |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      If all parameters are set to **null**, they will be restored to their default values.

#. Run the following command to disable HTTP/HTTPS flow control for cluster nodes:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.http.enabled": false
        }
      }

.. _en-us_topic_0000001938218516__section12926193210818:

Enabling Memory Flow Control
----------------------------

#. Run the following command to enable memory flow control:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.memory.enabled": true,
          "flowcontrol.memory.heap_limit": "80%"
        }
      }

   .. table:: **Table 3** Configuration items for memory flow control

      +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item                   | Type                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      +======================================+=======================+====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | flowcontrol.memory.enabled           | Boolean               | Whether to enable memory flow control. After this function is enabled, the memory usage is continuously monitored.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Value:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | -  true                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
      |                                      |                       | -  false (default value)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.heap_limit        | String                | Maximum heap memory usage of a node that is used as a threshold for triggering backpressure for flow control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Value range: 10%-100%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Default value: **90%**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | .. note::                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       |    -  The default value 90% of **flowcontrol.memory.heap_limit** is a conservative threshold. When the heap memory usage is greater than 90%, the system stops reading large requests that exceed 64 KB from the client until heap memory usage decreases. Once the heap memory usage decreases to 85%, client data equivalent to **5% x maximum heap memory capacity** can be read. If the heap memory usage stays above 90% for a long time, client requests cannot be processed. In this case, a GC algorithm is triggered to perform garbage collection until the heap memory usage drops below the threshold. |
      |                                      |                       |    -  Generally, you can set the **flowcontrol.memory.heap_limit** threshold to 80% or less to ensure that the node has reserved some heap memory for operations besides data writing, such as Elasticsearch query and segment merge.                                                                                                                                                                                                                                                                                                                                                                              |
      +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.in_flight_factor | Float                 | Backpressure release factor, which works similarly to the circuit breaker parameter **network.breaker.inflight_requests.overhead**. With the memory usage exceeding the limit, a larger value of this parameter indicates stronger backpressure, in which case, write traffic will be limited.                                                                                                                                                                                                                                                                                                                     |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Value range: >= 0.5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Default value: **1.0**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.max              | TimeValue             | Maximum delay of each request. If the delay exceeds the value of this parameter, backpressure may be stopped or the request connection may be disconnected. For details, see the setting of **flowcontrol.holding.max_strategy**.                                                                                                                                                                                                                                                                                                                                                                                  |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Value range: >= 15s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Default value: **60s**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.max_strategy     | String                | The policy applied after the maximum delay time is exceeded.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | The value can be:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | -  **keep** (default value): If the heap memory is still high, continue the backpressure. The server determines when to execute the request based on the real-time memory.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
      |                                      |                       | -  **soft**: The requests will be executed even if the heap memory usage is still high. The **inFlight** circuit breaker will determine whether to execute or reject the requests.                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | -  **hard**: If the heap memory usage is still high, requests will be discarded and the client connections will be disconnected.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.once_free_max     | String                | Maximum memory that can be made available at a time for a suspended request queue. This parameter helps prevent a cluster from becoming completely unavailable due to low memory availability under high pressure.                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Value range: 1%-50%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | Default value: 5%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.nudges_gc         | Boolean               | Whether to trigger garbage collection to ensure write stability when the write pressure is too high. (The backpressure connection pool is checked every second. The write pressure is considered high if all the existing connections are blocked and new write requests cannot be accepted.) The value can be:                                                                                                                                                                                                                                                                                                    |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       | -  true (default value)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
      |                                      |                       | -  false                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      If all parameters are set to **null**, they will be restored to their default values.

#. Run the following command to disable memory flow control:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.memory.enabled": false
        }
      }

.. _en-us_topic_0000001938218516__section846243514132:

Enabling Request Sampling
-------------------------

#. Run the following command to enable request sampling:

   .. code-block:: text

      PUT _cluster/settings
      {
        "transient": {
          "flowcontrol.log.access.enabled": true
        }
      }

   .. table:: **Table 4** Configuration items for request sampling

      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item             | Type                  | Description                                                                                                                                                                                         |
      +================================+=======================+=====================================================================================================================================================================================================+
      | flowcontrol.log.access.enabled | Boolean               | Whether to collect statistics on client IP addresses that accessed the cluster recently and the number of requests from them, including the quantities of bulk write, search, and msearch requests. |
      |                                |                       |                                                                                                                                                                                                     |
      |                                |                       | The value can be:                                                                                                                                                                                   |
      |                                |                       |                                                                                                                                                                                                     |
      |                                |                       | -  true                                                                                                                                                                                             |
      |                                |                       | -  false (default value)                                                                                                                                                                            |
      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.log.access.count   | Integer               | Number of client IP addresses that accessed a cluster recently. The IP address statistics switches control whether to collect request type statistics and whether to enable logging.                |
      |                                |                       |                                                                                                                                                                                                     |
      |                                |                       | Value range: 0-100                                                                                                                                                                                  |
      |                                |                       |                                                                                                                                                                                                     |
      |                                |                       | Default value: **10**                                                                                                                                                                               |
      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   When enabled, you can check relevant statistics through :ref:`Viewing Flow Control Information <en-us_topic_0000001938218516__section03781045277>`.

   .. note::

      If all parameters are set to **null**, they will be restored to their default values.

#. Run the following command to disable request sampling:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.access.enabled": false
        }
      }

.. _en-us_topic_0000001938218516__section364216459204:

Enable One-Click Traffic Blocking
---------------------------------

#. Run the following command to enable one-click traffic blocking:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.break.enabled": true
        }
      }

#. Run the following command to disable one-click traffic blocking:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.break.enabled": false
        }
      }

.. _en-us_topic_0000001938218516__section03781045277:

Viewing Flow Control Information
--------------------------------

-  Check the flow control status of all nodes.

   .. code-block:: text

      GET /_nodes/stats/filter/v2

-  View the flow control details of all nodes.

   .. code-block:: text

      GET /_nodes/stats/filter/v2?detail

-  View the flow control status of a specific node.

   .. code-block:: text

      GET /_nodes/{nodeId}/stats/filter/v2

   **{nodeId}** indicates the ID of the node you want to check.

Example response:

.. code-block::

   {
     "_nodes" : {
       "total" : 1,
       "successful" : 1,
       "failed" : 0
     },
     "cluster_name" : "css-xxxx",
     "nodes" : {
       "d3qnVIpPTtSoadkV0LQEkA" : {
         "name" : "css-xxxx-ess-esn-1-1",
         "host" : "192.168.x.x",
         "timestamp" : 1672236425112,
         "flow_control" : {
           "http" : {
             "current_connect" : 52,
             "rejected_concurrent" : 0,
             "rejected_rate" : 0,
             "rejected_black" : 0,
             "rejected_breaker" : 0
           },
           "access_items" : [
             {
               "remote_address" : "10.0.0.x",
               "search_count" : 0,
               "bulk_count" : 0,
               "other_count" : 4
             }
           ],
           "holding_requests" : 0
         }
       }
     }
   }

.. table:: **Table 5** Response parameters

   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Description                                                                                                                                                                                                                                            |
   +===================================+========================================================================================================================================================================================================================================================+
   | current_connect                   | Number of HTTP connections of a node, which is recorded regardless of whether flow control is enabled. This value is equivalent to the **current_open** value of **GET /_nodes/stats/http** API. It shows the current client connections of each node. |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rejected_concurrent               | Number of concurrent connections rejected during flow control.                                                                                                                                                                                         |
   |                                   |                                                                                                                                                                                                                                                        |
   |                                   | This parameter is counted only when **flowcontrol.http.enabled** is set to **true**. This count will not be cleared when flow control is disabled.                                                                                                     |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rejected_rate                     | Number of new connections rejected during flow control.                                                                                                                                                                                                |
   |                                   |                                                                                                                                                                                                                                                        |
   |                                   | This parameter is counted only when **flowcontrol.http.enabled** is set to **true**. This count will not be cleared when flow control is disabled.                                                                                                     |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rejected_black                    | Number of new connections rejected by a preconfigured blacklist during flow control.                                                                                                                                                                   |
   |                                   |                                                                                                                                                                                                                                                        |
   |                                   | This parameter is counted only when **flowcontrol.http.enabled** is set to **true**. This count will not be cleared when flow control is disabled.                                                                                                     |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rejected_breaker                  | Number of new connections rejected during one-click traffic blocking.                                                                                                                                                                                  |
   |                                   |                                                                                                                                                                                                                                                        |
   |                                   | This parameter is counted only when **flowcontrol.break.enabled** is set to **true**. This count will not be cleared when one-click traffic blocking is disabled.                                                                                      |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | access_items                      | IP addresses of clients that recently accessed the cluster.                                                                                                                                                                                            |
   |                                   |                                                                                                                                                                                                                                                        |
   |                                   | The value is determined by **flowcontrol.log.access.count**.                                                                                                                                                                                           |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | remote_address                    | Remote access IP addresses and the number of requests from them.                                                                                                                                                                                       |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | search_count                      | Number of times a client accessed a database using **\_search** and **\_msearch**.                                                                                                                                                                     |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | bulk_count                        | Number of times a client accessed a database using **\_bulk**.                                                                                                                                                                                         |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | other_count                       | Number of times a client accessed a database using other request methods.                                                                                                                                                                              |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | holding_requests                  | Number of connections to the current node where writes are halted due to flow control.                                                                                                                                                                 |
   +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001938218516__section1626791610277:

Enabling and Viewing Access Logs
--------------------------------

#. Run the following command to enable access logging:

   -  Enable access logging for all nodes in a cluster.

      .. code-block:: text

         PUT /_access_log?duration_limit=30s&capacity_limit=1mb

   -  Enable access logging for a specified node in a cluster.

      .. code-block:: text

         PUT /_access_log/{nodeId}?duration_limit=30s&capacity_limit=1mb

      **{nodeId}** indicates the node ID.

   .. table:: **Table 6** Configuration items for configuring access logging

      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item    | Type                  | Description                                                                                                             |
      +=======================+=======================+=========================================================================================================================+
      | duration_limit        | String                | Maximum duration of access log records. When this duration is reached, the recording stops.                             |
      |                       |                       |                                                                                                                         |
      |                       |                       | Value range: 10 to 120                                                                                                  |
      |                       |                       |                                                                                                                         |
      |                       |                       | Unit: s                                                                                                                 |
      |                       |                       |                                                                                                                         |
      |                       |                       | Default value: **30**                                                                                                   |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------+
      | capacity_limit        | String                | Maximum memory size for recording access logs. When the size of an access log reaches this value, access logging stops. |
      |                       |                       |                                                                                                                         |
      |                       |                       | Value range: 1 to 5                                                                                                     |
      |                       |                       |                                                                                                                         |
      |                       |                       | Unit: MB                                                                                                                |
      |                       |                       |                                                                                                                         |
      |                       |                       | Default value: **1**                                                                                                    |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------+

   .. note::

      -  Access logging stops when either **duration_limit** or **capacity_limit** is reached.
      -  If all parameters are set to **null**, they will be restored to their default values.

#. Run the following command to check access logs:

   -  API for checking the access logs of all nodes in a cluster

      .. code-block:: text

         GET /_access_log

   -  API for checking the access logs of a specified node in a cluster

      .. code-block:: text

         GET /_access_log/{nodeId}

      **{nodeId}** indicates the node ID.

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
          "8x-ZHu-wTemBQwpcGivFKg" : {
            "name" : "css-flowcontroller-ess-esn-1-1",
            "host" : "10.0.0.98",
            "count" : 2,
            "access" : [
              {
                "time" : "2021-02-23 02:09:50",
                "remote_address" : "/10.0.0.98:28191",
                "url" : "/_access/security/log?pretty",
                "method" : "GET",
                "content" : ""
              },
              {
                "time" : "2021-02-23 02:09:52",
                "remote_address" : "/10.0.0.98:28193",
                "url" : "/_access/security/log?pretty",
                "method" : "GET",
                "content" : ""
              }
            ]
          }
        }
      }

   .. table:: **Table 7** Response parameters

      +-----------+----------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter | Description                                                                                                                                  |
      +===========+==============================================================================================================================================+
      | name      | Node name                                                                                                                                    |
      +-----------+----------------------------------------------------------------------------------------------------------------------------------------------+
      | host      | Node IP address                                                                                                                              |
      +-----------+----------------------------------------------------------------------------------------------------------------------------------------------+
      | count     | Number of node access requests in a statistical period                                                                                       |
      +-----------+----------------------------------------------------------------------------------------------------------------------------------------------+
      | access    | Details about node access requests in a statistical period For details, see :ref:`Table 8 <en-us_topic_0000001938218516__table72934522332>`. |
      +-----------+----------------------------------------------------------------------------------------------------------------------------------------------+

   .. _en-us_topic_0000001938218516__table72934522332:

   .. table:: **Table 8** access

      ============== ================================================
      Parameter      Description
      ============== ================================================
      time           Request time
      remote_address Source IP address and port number in the request
      url            Original URL of the request
      method         Method corresponding to the request path
      content        Request content
      ============== ================================================

#. Run the following commands to delete access logs.

   API for deleting access logs for all nodes:

   .. code-block:: text

      DELETE /_access_log

.. _en-us_topic_0000001938218516__section072285622916:

Enabling Access Logging in Files
--------------------------------

Typically you record access logs in files to locate faults. After faults are rectified, you should disable it.

#. Run the following command to enable access logging in files:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.file.enabled": true
        }
      }

   .. table:: **Table 9** Configuration items for enabling access logging in files

      +------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                    | Type                  | Description                                                                                                                                                                               |
      +==============================+=======================+===========================================================================================================================================================================================+
      | flowcontrol.log.file.enabled | Boolean               | Whether to record the details of each request in the access log file. The log file name is **Cluster name_access_log.log**. You can check this file only through the log backup function. |
      |                              |                       |                                                                                                                                                                                           |
      |                              |                       | Value:                                                                                                                                                                                    |
      |                              |                       |                                                                                                                                                                                           |
      |                              |                       | -  true                                                                                                                                                                                   |
      |                              |                       | -  false (default value)                                                                                                                                                                  |
      +------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Run the following command to disable access logging in files:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.file.enabled": false
        }
      }
