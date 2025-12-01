:original_name: css_01_0056.html

.. _css_01_0056:

Configuring Flow Control for an OpenSearch Cluster
==================================================

Configure flow control policies for your OpenSearch cluster in both the inbound and outbound directions, ensuring cluster stability by safeguarding against abnormal traffic.

An OpenSearch cluster can become overloaded due to traffic surges, malicious requests, and internal resource competition, which can even lead to node failures. Through policies like client request throttling, write backpressure, and traffic pattern analysis, flow control ensures proper resource allocation, thereby protecting clusters from overload. It covers the following scenarios:

-  High-concurrency write handling: mitigates the risk of out-of-memory (OOM) exceptions under heavy write loads.
-  Security defense: controls access by IP address using both blacklists and whitelists.
-  Emergency response: blocks malicious or abnormal traffic in one click.
-  Performance optimization: optimizes flow control thresholds and policies based on collected statistics.

How the Feature Works
---------------------

.. table:: **Table 1** Flow control policies

   +------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Policy                                   | What It Does                                                                                                                                                                                                  | Details                                                                                                         |
   +==========================================+===============================================================================================================================================================================================================+=================================================================================================================+
   | HTTP/HTTPS flow control                  | Controls client access traffic using blacklists and whitelists, an upper limit on concurrent connections, and a rate limit on new connection attempts.                                                        | :ref:`Configuring HTTP/HTTPS Flow Control <en-us_topic_0000002353029832__section1023014371242>`                 |
   |                                          |                                                                                                                                                                                                               |                                                                                                                 |
   |                                          | -  Blacklists and whitelists: A whitelist takes precedence over a blacklist. If an IP address is on both lists, it is allowed. Requests sent through blacklisted connections will be ignored.                 |                                                                                                                 |
   |                                          | -  Concurrent connection limit: Limits the total number of HTTP connections per second to prevent overload.                                                                                                   |                                                                                                                 |
   |                                          | -  New connection limit: Limits the number of new connections that can be set up per second. The warmup_period parameter protects against connection floods, allowing traffic to grow gradually and steadily. |                                                                                                                 |
   +------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Memory flow control                      | When the heap memory usage exceeds a pre-defined threshold (for example, 80%), the system stops receiving large requests, and garbage collection (GC) is triggered to reclaim memory.                         | :ref:`Configuring Memory-based Flow Control <en-us_topic_0000002353029832__section12926193210818>`              |
   |                                          |                                                                                                                                                                                                               |                                                                                                                 |
   |                                          | Write traffic is throttled by setting the backpressure factor (in_flight_factor) and the maximum delay for request handling (max).                                                                            |                                                                                                                 |
   +------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | One-click traffic blocking               | When enabled, the system immediately disconnects all client connections, but not those used for OpenSearch Dashboards access or O&M and monitoring APIs, in order to restore the cluster.                     | :ref:`Configuring One-Click Traffic Blocking <en-us_topic_0000002353029832__section364216459204>`               |
   +------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Request statistics sampling and analysis | Records request metrics (such as bulk writes and queries) by client IP address, and exposes them via a statistics API to evaluate the cluster load and proactively identify abnormal traffic patterns.        | :ref:`Configuring Request Statistics Sampling and Analysis <en-us_topic_0000002353029832__section846243514132>` |
   +------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Access logging                           | Records the URLs and bodies of HTTP/HTTPS requests for cluster load and client request analysis.                                                                                                              | -  :ref:`Configuring Access Logging <en-us_topic_0000002353029832__section1626791610277>`                       |
   |                                          |                                                                                                                                                                                                               | -  :ref:`Configuring Access Logging in Files <en-us_topic_0000002353029832__section072285622916>`               |
   |                                          | Access logs can also be saved to files (that is, persisted to disk) to facilitate troubleshooting and performance analysis.                                                                                   |                                                                                                                 |
   +------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

Constraints
-----------

-  Only OpenSearch 2.19.0 supports flow control.
-  Enabling flow control may compromise cluster and node performance. For example, memory-based flow control may cause query failures on OpenSearch Dashboards.
-  Configuring too many paths for memory-based flow control has a significant impact on performance.
-  Enabling access logging will hurt cluster performance.
-  After flow control policies are enabled, excess or non-compliant requests are rejected directly.

Logging In to OpenSearch Dashboards
-----------------------------------

Log in to OpenSearch Dashboards and go to the command execution page. OpenSearch clusters support multiple access methods. This topic uses OpenSearch Dashboards as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

.. _en-us_topic_0000002353029832__section1023014371242:

Configuring HTTP/HTTPS Flow Control
-----------------------------------

Control client access traffic using blacklists and whitelists, an upper limit on concurrent connections, and a rate limit on new connection attempts.

#. Enable HTTP/HTTPS flow control.

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

   .. table:: **Table 2** Parameters for configuring HTTP/HTTPS flow control

      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Type                  | Description                                                                                                                                                                                               |
      +================================+=======================+===========================================================================================================================================================================================================+
      | flowcontrol.http.enabled       | Boolean               | Whether to enable HTTP/HTTPS flow control. Enabling it may impact node performance.                                                                                                                       |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | -  true: Enable HTTP/HTTPS flow control.                                                                                                                                                                  |
      |                                |                       | -  false (default): Disable HTTP/HTTPS flow control.                                                                                                                                                      |
      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.allow         | List<String>          | A whitelist of client IP addresses or CIDR blocks that are allowed to access the cluster, supporting:                                                                                                     |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | -  Individual IP addresses, for example, **192.18.0.1**.                                                                                                                                                  |
      |                                |                       | -  CIDR blocks, for example, **192.168.0.0/24**.                                                                                                                                                          |
      |                                |                       | -  Multiple IP addresses or CIDR blocks separated by commas (,), for example, **192.168.0.1/24, 192.168.2.1/24**.                                                                                         |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | The default is an empty list, indicating no whitelist.                                                                                                                                                    |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.deny          | List<String>          | A blacklist of client IP addresses or CIDR blocks that are not allowed to access the cluster. A whitelist takes precedence over a blacklist. A blacklist supports the following:                          |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | -  Individual IP addresses, for example, **192.18.0.1**.                                                                                                                                                  |
      |                                |                       | -  CIDR blocks, for example, **192.168.0.0/24**.                                                                                                                                                          |
      |                                |                       | -  Multiple IP addresses or CIDR blocks separated by commas (,), for example, **192.168.0.1/24, 192.168.2.1/24**.                                                                                         |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | The default is an empty list, indicating no blacklist.                                                                                                                                                    |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.concurrent    | Integer               | Maximum number of concurrent HTTP/HTTPS connections that can be handled by each node per second. The default value is the number of available node vCPUs multiplied by 600.                               |
      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.newconnect    | Integer               | Maximum number of new HTTP/HTTPS connections that can be created per second per node.                                                                                                                     |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | The default value is the number of available node vCPUs multiplied by 200.                                                                                                                                |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.warmup_period | Integer               | A grace period during which a system gradually ramp up from accepting zero HTTP/HTTPS requests to its full, maximum capacity.                                                                             |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | Value range: 0-10000                                                                                                                                                                                      |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | Unit: ms                                                                                                                                                                                                  |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | The default value is 0, indicating that there is no such warm-up period, and the maximum rate can be reached instantly.                                                                                   |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      |                                |                       |                                                                                                                                                                                                           |
      |                                |                       | For example, if **flowcontrol.http.newconnect** is set to **100** and **flowcontrol.http.warmup_period** is set to **5000ms**, it takes 5 seconds for the system to reach 100 new connections per second. |
      +--------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Disable HTTP/HTTPS flow control.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.http.enabled": false
        }
      }

.. _en-us_topic_0000002353029832__section12926193210818:

Configuring Memory-based Flow Control
-------------------------------------

Enable write throttling to mitigate the risk of OOM exceptions when the heap memory usage of a node exceeds a predefined threshold.

#. Enable memory-based flow control.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.memory.enabled": true,
          "flowcontrol.memory.heap_limit": "80%"
        }
      }

   .. table:: **Table 3** Memory-based flow control parameters

      +--------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                            | Type                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      +======================================+=======================+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | flowcontrol.memory.enabled           | Boolean               | Whether to enable memory-based flow control. When enabled, node heap memory usage is monitored and a threshold is set, and writes are throttled when this threshold is reached.                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | -  true: Enable memory-based flow control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
      |                                      |                       | -  false (default): Disable memory-based flow control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      +--------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.heap_limit        | String                | Node heap memory usage threshold. When this threshold is exceeded, a write backpressure mechanism is triggered.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Value range: 10%-100%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | The default value 90% of **flowcontrol.memory.heap_limit** is a conservative threshold. When the heap memory usage exceeds 90%, the system stops accepting client requests that exceed 64 KB, until heap memory usage decreases. Once the heap memory usage decreases to 85%, client data equivalent to **5% x maximum heap memory capacity** can be read. If the heap memory usage stays above 90% for a long time, client requests cannot be processed. In this case, garbage collection is triggered until the heap memory usage drops below this threshold. |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Generally, you can set this threshold to 80% or less to ensure that cluster nodes have reserved some heap memory for operations besides data writing, such as segment merges.                                                                                                                                                                                                                                                                                                                                                                                   |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +--------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.in_flight_factor | Float                 | Backpressure factor, which controls the sensitivity of memory-based backpressure. A larger value indicates more powerful write throttling.                                                                                                                                                                                                                                                                                                                                                                                                                      |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Value range: >= 0.5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | The default value is **1.0**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +--------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.max              | TimeValue             | Maximum request handling delay allowed before requests are handled according to the policy defined by **flowcontrol.holding.max_strategy**.                                                                                                                                                                                                                                                                                                                                                                                                                     |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Value range: >= 15s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Unit: second                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Default value: 60s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +--------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.max_strategy     | String                | Handling policy for requests delayed longer than **flowcontrol.holding.max**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | -  **keep** (default): Keep the backpressure status while waiting for the memory usage to drop. The server determines when to execute the requests based on real-time memory usage.                                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                       | -  **soft**: Forcibly execute the requests, but the **inFlight** circuit breaker gets to decide whether to reject them.                                                                                                                                                                                                                                                                                                                                                                                                                                         |
      |                                      |                       | -  **hard**: Reject the requests immediately and disconnect client connections.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +--------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.once_free_max     | String                | Maximum memory that can be made available at a time for a re-enabled request queue. This parameter can be configured to prevent cluster overload caused by a flood of incoming requests.                                                                                                                                                                                                                                                                                                                                                                        |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Value range: 1%-50%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | The default value is 5%.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +--------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.nudges_gc         | Boolean               | Whether to trigger garbage collection (GC) to reclaim memory when the write pressure is too high. (The backpressure connection pool is checked every second. The write pressure is considered high if all existing connections are blocked and new write requests cannot be accepted.)                                                                                                                                                                                                                                                                          |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | -  true (default): Trigger GC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      |                                      |                       | -  false: Not to trigger GC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                      |                       | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +--------------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Disable memory-based flow control.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.memory.enabled": false
        }
      }

.. _en-us_topic_0000002353029832__section364216459204:

Configuring One-Click Traffic Blocking
--------------------------------------

In case of emergencies, the system immediately disconnects all client connections (excluding those used for OpenSearch Dashboards access or O&M and monitoring APIs) to restore clusters.

#. Enable one-click traffic blocking.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.break.enabled": true
        }
      }

   .. table:: **Table 4** Parameters for configuring one-click traffic blocking

      +---------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                 | Type                  | Description                                                                                                                                                                                                                           |
      +===========================+=======================+=======================================================================================================================================================================================================================================+
      | flowcontrol.break.enabled | Boolean               | Whether to enable one-click traffic blocking (similar to a circuit breaker). When enabled, the system immediately disconnects all client connections, but not those used for OpenSearch Dashboards access or O&M and monitoring APIs. |
      |                           |                       |                                                                                                                                                                                                                                       |
      |                           |                       | -  true: Enable one-click disconnection.                                                                                                                                                                                              |
      |                           |                       | -  false (default): Disable one-click disconnection.                                                                                                                                                                                  |
      +---------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Disable one-click disconnection:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.break.enabled": false
        }
      }

.. _en-us_topic_0000002353029832__section846243514132:

Configuring Request Statistics Sampling and Analysis
----------------------------------------------------

Collect request metrics by client IP address to help identify abnormal traffic patterns.

#. Enable request statistics sampling.

   .. code-block:: text

      PUT _cluster/settings
      {
        "transient": {
          "flowcontrol.log.access.enabled": true
        }
      }

   .. table:: **Table 5** Parameters for request statistics sampling

      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Type                  | Description                                                                                                                                                        |
      +================================+=======================+====================================================================================================================================================================+
      | flowcontrol.log.access.enabled | Boolean               | Whether to enable request statistics sampling, that is, whether to collect request metrics (such as bulk writes and search/msearch requests) by client IP address. |
      |                                |                       |                                                                                                                                                                    |
      |                                |                       | -  true: Enable request statistics sampling.                                                                                                                       |
      |                                |                       | -  false (default): Disable request statistics sampling.                                                                                                           |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.log.access.count   | Integer               | Maximum number of client IP addresses sampled.                                                                                                                     |
      |                                |                       |                                                                                                                                                                    |
      |                                |                       | Value range: 0-100                                                                                                                                                 |
      |                                |                       |                                                                                                                                                                    |
      |                                |                       | Default value: **10**                                                                                                                                              |
      |                                |                       |                                                                                                                                                                    |
      |                                |                       | Setting this parameter to **null** restores the default value.                                                                                                     |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Check the sampled statistics.

   -  Check the flow control status of all nodes.

      .. code-block:: text

         GET /_nodes/stats/filter/v2

   -  Check the flow control details of all nodes.

      .. code-block:: text

         GET /_nodes/stats/filter/v2?detail

   -  Check the flow control status of a specified node.

      .. code-block:: text

         GET /_nodes/{nodeId}/stats/filter/v2

      **{nodeId}** indicates the node ID.

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

   .. table:: **Table 6** Response parameters

      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                            |
      +===================================+========================================================================================================================================================================================================================================================+
      | current_connect                   | Number of HTTP connections to a node, which is recorded regardless of whether flow control is enabled. This value is equivalent to the **current_open** value of **GET /_nodes/stats/http** API. It shows the current client connections of each node. |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | rejected_concurrent               | Number of concurrent connections rejected during flow control.                                                                                                                                                                                         |
      |                                   |                                                                                                                                                                                                                                                        |
      |                                   | This metric is available only when **flowcontrol.http.enabled** is set to **true**. The count will not be cleared when flow control is disabled.                                                                                                       |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | rejected_rate                     | Number of new connections rejected during flow control.                                                                                                                                                                                                |
      |                                   |                                                                                                                                                                                                                                                        |
      |                                   | This metric is available only when **flowcontrol.http.enabled** is set to **true**. The count will not be cleared when flow control is disabled.                                                                                                       |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | rejected_black                    | Number of new connections rejected by a preconfigured blacklist during flow control.                                                                                                                                                                   |
      |                                   |                                                                                                                                                                                                                                                        |
      |                                   | This metric is available only when **flowcontrol.http.enabled** is set to **true**. The count will not be cleared when flow control is disabled.                                                                                                       |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | rejected_breaker                  | Number of new connections rejected during one-click traffic blocking.                                                                                                                                                                                  |
      |                                   |                                                                                                                                                                                                                                                        |
      |                                   | This metric is available only when **flowcontrol.break.enabled** is set to **true**. The count will not be cleared when one-click traffic blocking is disabled.                                                                                        |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | access_items                      | IP addresses of clients that recently accessed the cluster.                                                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                                                        |
      |                                   | The number of client IP addresses sampled is determined by **flowcontrol.log.access.count**.                                                                                                                                                           |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | remote_address                    | IP addresses and the number of requests.                                                                                                                                                                                                               |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search_count                      | Number of times a client accessed a database using **\_search** and **\_msearch**.                                                                                                                                                                     |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | bulk_count                        | Number of times a client accessed a database using **\_bulk**.                                                                                                                                                                                         |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | other_count                       | Number of times a client accessed a database using other request methods.                                                                                                                                                                              |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | holding_requests                  | Number of connections to the current node where writes are halted due to flow control.                                                                                                                                                                 |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Disable request statistics sampling.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.access.enabled": false
        }
      }

.. _en-us_topic_0000002353029832__section1626791610277:

Configuring Access Logging
--------------------------

When access logging is enabled, the system records the URLs and bodies of HTTP/HTTPS requests for cluster load and request analysis.

#. Enable access logging.

   -  Enable access logging for all nodes in a cluster.

      .. code-block:: text

         PUT /_access_log?duration_limit=30s&capacity_limit=1mb

   -  Enable access logging for a specified node in a cluster.

      .. code-block:: text

         PUT /_access_log/{nodeId}?duration_limit=30s&capacity_limit=1mb

      **{nodeId}** indicates the node ID.

   .. table:: **Table 7** Parameters for enabling access logging

      +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------+
      | Parameter             | Type                  | Description                                                                                                                 |
      +=======================+=======================+=============================================================================================================================+
      | duration_limit        | String                | Maximum duration of access log records. When this duration is reached, access logging stops.                                |
      |                       |                       |                                                                                                                             |
      |                       |                       | Value range: 10 to 120                                                                                                      |
      |                       |                       |                                                                                                                             |
      |                       |                       | Unit: s                                                                                                                     |
      |                       |                       |                                                                                                                             |
      |                       |                       | The default value is **30**.                                                                                                |
      |                       |                       |                                                                                                                             |
      |                       |                       | Setting this parameter to **null** restores the default value.                                                              |
      |                       |                       |                                                                                                                             |
      |                       |                       | Access logging stops when either **duration_limit** or **capacity_limit** is reached.                                       |
      +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------+
      | capacity_limit        | String                | Maximum memory capacity for recording access logs. When the size of an access log reaches this limit, access logging stops. |
      |                       |                       |                                                                                                                             |
      |                       |                       | Value range: 1 to 5                                                                                                         |
      |                       |                       |                                                                                                                             |
      |                       |                       | Unit: MB                                                                                                                    |
      |                       |                       |                                                                                                                             |
      |                       |                       | The default value is **1**.                                                                                                 |
      |                       |                       |                                                                                                                             |
      |                       |                       | Setting this parameter to **null** restores the default value.                                                              |
      |                       |                       |                                                                                                                             |
      |                       |                       | Access logging stops when either **duration_limit** or **capacity_limit** is reached.                                       |
      +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------+

#. Check access logs.

   -  Check the access logs of all nodes in a cluster.

      .. code-block:: text

         GET /_access_log

   -  Check the access logs of a specified cluster node.

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

   .. table:: **Table 8** Response parameters

      +----------------+----------------------------------------------------------------------------------+
      | Parameter      | Description                                                                      |
      +================+==================================================================================+
      | name           | Node name                                                                        |
      +----------------+----------------------------------------------------------------------------------+
      | host           | Node IP address                                                                  |
      +----------------+----------------------------------------------------------------------------------+
      | count          | Number of node access requests in a statistical period                           |
      +----------------+----------------------------------------------------------------------------------+
      | access         | Details about node access requests in a statistical period                       |
      +----------------+----------------------------------------------------------------------------------+
      | time           | Request time                                                                     |
      +----------------+----------------------------------------------------------------------------------+
      | remote_address | Source IP address and port number in the request                                 |
      +----------------+----------------------------------------------------------------------------------+
      | url            | Original URL of the request                                                      |
      +----------------+----------------------------------------------------------------------------------+
      | method         | Request method                                                                   |
      +----------------+----------------------------------------------------------------------------------+
      | content        | Request content. If the value is an empty string (""), there is no request body. |
      +----------------+----------------------------------------------------------------------------------+

#. Delete access logs. Logs are recorded in the memory. After reading the logs, you are advised to delete them to reclaim resources.

   Delete access logs for all nodes:

   .. code-block:: text

      DELETE /_access_log

.. _en-us_topic_0000002353029832__section072285622916:

Configuring Access Logging in Files
-----------------------------------

Access logs can be persisted to disk for troubleshooting and analysis. Use this function sparingly, as it can impact cluster performance. Remember to disable it immediately after resolving the issue.

#. Enable access logging in files.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.file.enabled": true
        }
      }

   .. table:: **Table 9** Enable access logging in files

      +------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+
      | Parameter                    | Type                  | Description                                                                                                         |
      +==============================+=======================+=====================================================================================================================+
      | flowcontrol.log.file.enabled | Boolean               | Whether to record access logs in files. When enabled, the log of each access request is recorded in files.          |
      |                              |                       |                                                                                                                     |
      |                              |                       | The log file name is **Cluster name_access_log.log**. You can check this file only through the log backup function. |
      |                              |                       |                                                                                                                     |
      |                              |                       | -  true: Record access logs in files.                                                                               |
      |                              |                       | -  false (default): Not to record access logs in files.                                                             |
      +------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------+

#. Disable access logging in files.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.file.enabled": false
        }
      }
