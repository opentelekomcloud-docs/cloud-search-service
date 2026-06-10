:original_name: css_01_0192.html

.. _css_01_0192:

Configuring Flow Control 2.0
============================

Configure flow control policies for your Elasticsearch cluster in both the inbound and outbound directions, ensuring cluster stability by safeguarding against abnormal traffic.

An Elasticsearch cluster can become overloaded due to traffic surges, malicious requests, and internal resource competition, which can even lead to node failures. Through policies like client request throttling, backpressure, and traffic pattern analysis, flow control ensures proper resource allocation, thereby protecting clusters from overload. It covers the following scenarios:

-  High-concurrency write handling: mitigates the risk of out-of-memory (OOM) exceptions under heavy write loads.
-  Security defense: controls access by IP address using both blacklists and whitelists.
-  Emergency response: blocks malicious or abnormal traffic in one click.
-  Performance optimization: optimizes flow control thresholds and policies based on collected statistics.

How the Feature Works
---------------------

.. table:: **Table 1** Flow control policies

   +------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Policy                                   | How It Works                                                                                                                                                                                                                                                                                                          | Details                                                                                                         |
   +==========================================+=======================================================================================================================================================================================================================================================================================================================+=================================================================================================================+
   | HTTP/HTTPS flow control                  | Controls client access traffic using blacklists and whitelists, an upper limit on concurrent connections, and a rate limit on new connection attempts.                                                                                                                                                                | :ref:`Configuring HTTP/HTTPS Flow Control <en-us_topic_0000001938218516__section1023014371242>`                 |
   |                                          |                                                                                                                                                                                                                                                                                                                       |                                                                                                                 |
   |                                          | -  Blacklists and whitelists: A whitelist takes precedence over a blacklist. If an IP address is on both lists, it is allowed. Requests sent through blacklisted connections will be ignored.                                                                                                                         |                                                                                                                 |
   |                                          | -  Concurrent connection limit: Limits the total number of concurrent HTTP connections to prevent overload.                                                                                                                                                                                                           |                                                                                                                 |
   |                                          | -  New connection limit: Limits the number of new connections that can be set up per second. The warmup_period parameter protects against connection floods, allowing traffic to grow gradually and steadily.                                                                                                         |                                                                                                                 |
   |                                          |                                                                                                                                                                                                                                                                                                                       |                                                                                                                 |
   |                                          | When HTTP/HTTPS flow control is enabled, requests from blacklisted IP addresses are always rejected; for IP addresses on the whitelist, no flow control rules apply; for other IP addresses, when either the concurrent connection limit or the new connection limit is reached, requests from them will be rejected. |                                                                                                                 |
   +------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Memory-based flow control                | When the heap memory usage exceeds a pre-defined threshold (for example, 80%), the system stops receiving large requests, and garbage collection (GC) is triggered to reclaim memory.                                                                                                                                 | :ref:`Configuring Memory-based Flow Control <en-us_topic_0000001938218516__section12926193210818>`              |
   |                                          |                                                                                                                                                                                                                                                                                                                       |                                                                                                                 |
   |                                          | Write traffic is throttled by setting the backpressure factor (in_flight_factor) and the maximum delay for request handling (max).                                                                                                                                                                                    |                                                                                                                 |
   |                                          |                                                                                                                                                                                                                                                                                                                       |                                                                                                                 |
   |                                          | When memory-based flow control is enabled, large requests may be delayed for a long time when the cluster's heap memory usage exceeds the configured threshold.                                                                                                                                                       |                                                                                                                 |
   +------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | One-click traffic blocking               | When triggered, the system immediately disconnects all client connections that are not whitelisted, with the exception of those used for Kibana access or O&M and monitoring APIs, as an effort to restore the cluster.                                                                                               | :ref:`Configuring One-Click Traffic Blocking <en-us_topic_0000001938218516__section846243514132>`               |
   +------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Request statistics sampling and analysis | Records request metrics (such as bulk writes and queries) by client IP address, and exposes them via a statistics API to evaluate the cluster load and proactively identify abnormal traffic patterns.                                                                                                                | :ref:`Configuring Request Statistics Sampling and Analysis <en-us_topic_0000001938218516__section364216459204>` |
   +------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Access logging                           | Records the URLs and bodies of HTTP/HTTPS requests for cluster load and client request analysis.                                                                                                                                                                                                                      | -  :ref:`Configuring Access Logging <en-us_topic_0000001938218516__section03781045277>`                         |
   |                                          |                                                                                                                                                                                                                                                                                                                       | -  :ref:`Configuring Access Logging in Files <en-us_topic_0000001938218516__section1626791610277>`              |
   |                                          | Access logs can also be saved to files (that is, persisted to disk) to facilitate troubleshooting and performance analysis.                                                                                                                                                                                           |                                                                                                                 |
   |                                          |                                                                                                                                                                                                                                                                                                                       |                                                                                                                 |
   |                                          | Enabling access logging incurs extra CPU and memory overhead, which may slow down request handling.                                                                                                                                                                                                                   |                                                                                                                 |
   +------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

Constraints
-----------

Elasticsearch 7.6.2 and 7.10.2 clusters created after February 2023 support Flow Control 2.0 only, while clusters created before that support Flow Control 1.0 only.

Logging In to Kibana
--------------------

Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

.. _en-us_topic_0000001938218516__section1023014371242:

Configuring HTTP/HTTPS Flow Control
-----------------------------------

Control client access traffic using blacklists and whitelists, an upper limit on concurrent connections, and a rate limit on new connection attempts, to prevent overload.

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

      +--------------------------------+-----------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Type            | Default Value                                         | Description                                                                                                                                                                                               |
      +================================+=================+=======================================================+===========================================================================================================================================================================================================+
      | flowcontrol.http.enabled       | Boolean         | false                                                 | Enable or disable HTTP/HTTPS flow control. When enabled, flow control will be performed based on relevant settings.                                                                                       |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | The value can be:                                                                                                                                                                                         |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | -  true: Enable HTTP/HTTPS flow control.                                                                                                                                                                  |
      |                                |                 |                                                       | -  false: Disable HTTP/HTTPS flow control.                                                                                                                                                                |
      +--------------------------------+-----------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.allow         | List<String>    | Null (no whitelist)                                   | A whitelist of client IP addresses or CIDR blocks that are allowed to access the cluster, supporting:                                                                                                     |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | -  Individual IP addresses, for example, **192.18.0.1**.                                                                                                                                                  |
      |                                |                 |                                                       | -  CIDR blocks, for example, **192.168.0.0/24**.                                                                                                                                                          |
      |                                |                 |                                                       | -  Multiple IP addresses or CIDR blocks separated by commas (,), for example, **192.168.0.1/24, 192.168.2.1/24**.                                                                                         |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      +--------------------------------+-----------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.deny          | List<String>    | Null (no blacklist)                                   | A blacklist of client IP addresses or CIDR blocks that are not allowed to access the cluster. A whitelist takes precedence over a blacklist. A blacklist supports the following:                          |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | -  Individual IP addresses, for example, **192.18.0.1**.                                                                                                                                                  |
      |                                |                 |                                                       | -  CIDR blocks, for example, **192.168.0.0/24**.                                                                                                                                                          |
      |                                |                 |                                                       | -  Multiple IP addresses or CIDR blocks separated by commas (,), for example, **192.168.0.1/24, 192.168.2.1/24**.                                                                                         |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      +--------------------------------+-----------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.concurrent    | Integer         | Node vCPUs x 600                                      | Maximum number of concurrent HTTP/HTTPS connections that can be handled by a node.                                                                                                                        |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Minimum value: **10**                                                                                                                                                                                     |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      +--------------------------------+-----------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.newconnect    | Integer         | Node vCPUs x 200                                      | Maximum number of new HTTP/HTTPS connections that can be created per second per node.                                                                                                                     |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Minimum value: **10**                                                                                                                                                                                     |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      +--------------------------------+-----------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.warmup_period | Integer         | 0 (no grace period before reaching the full capacity) | A grace period during which a system gradually ramps up from accepting zero HTTP/HTTPS requests to its full, maximum capacity.                                                                            |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Value range: 0-10000                                                                                                                                                                                      |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Unit: ms                                                                                                                                                                                                  |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | For example, if **flowcontrol.http.newconnect** is set to **100** and **flowcontrol.http.warmup_period** is set to **5000ms**, it takes 5 seconds for the system to reach 100 new connections per second. |
      |                                |                 |                                                       |                                                                                                                                                                                                           |
      |                                |                 |                                                       | Setting this parameter to **null** restores the default value.                                                                                                                                            |
      +--------------------------------+-----------------+-------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Disable HTTP/HTTPS flow control.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.http.enabled": false
        }
      }

.. _en-us_topic_0000001938218516__section12926193210818:

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

      +--------------------------------------+-----------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                            | Type            | Default Value                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      +======================================+=================+==============================+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | flowcontrol.memory.enabled           | Boolean         | true                         | Whether to enable memory-based flow control. When enabled, node heap memory usage is monitored and a threshold is set, and writes are throttled when this threshold is reached.                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | The value can be:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | -  true: Enable memory-based flow control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                      |                 |                              | -  false: Disable memory-based flow control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      +--------------------------------------+-----------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.heap_limit        | String          | 90% (conservative threshold) | Node heap memory usage threshold. When this threshold is exceeded, a backpressure mechanism is triggered.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Value range: 10%-100%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | -  When the heap memory usage exceeds this threshold, the system stops processing client requests that are larger than 64 KB. Processing resumes only when the heap memory usage drops below this threshold.                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                 |                              | -  When the heap memory usage is five percentage points below this threshold, the system continues processing requests. However, it restricts the total data read to 5% of the total heap memory capacity per cycle. This limit, which is configured using the **flowcontrol.memory.once_free_max** parameter, creates a memory buffer to prevent immediate exhaustion when processing resumes.                                                                                                                                                                          |
      |                                      |                 |                              | -  While the heap memory usage stays above this threshold, the system cannot accept new client requests. If the **flowcontrol.memory.nudges_gc** parameter is set to **true**, the system will actively trigger garbage collection (GC) and repeatedly attempt to reclaim memory until usage drops below this threshold. This helps prevent system breakdown caused by potential memory leaks.                                                                                                                                                                           |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | In practice, you are advised to set this parameter to 80% or lower to reserve heap memory for non-read tasks, for example, segment merge.                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.in_flight_factor | Float           | 1.0 (recommended)            | Backpressure factor, which controls the sensitivity of memory-based backpressure. A larger value indicates more powerful write throttling.                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Value range: >= 0.5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | This parameter estimates the potential heap memory impact of an incoming large request. The calculation is as follows: **in_flight_factor x Request body size**. The resulting estimate is then used to apply memory-based backpressure and throttling.                                                                                                                                                                                                                                                                                                                  |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.max              | TimeValue       | 60s                          | Maximum request handling delay allowed before requests are handled according to the policy defined by **flowcontrol.holding.max_strategy**.                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Value range: >= 15s                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Unit: second                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Generally, you should configure this parameter based on the **flowcontrol.holding.max_strategy** setting.                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | -  When **flowcontrol.holding.max_strategy** is set to **soft**, keep the value of this parameter lower than the client request timeout. Additionally, reserve some request execution time.                                                                                                                                                                                                                                                                                                                                                                              |
      |                                      |                 |                              | -  When **flowcontrol.holding.max_strategy** is set to **hard**, keep the value of this parameter higher than the client request timeout.                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                      |                 |                              | -  When **flowcontrol.holding.max_strategy** is set to **keep**, this parameter is invalid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.holding.max_strategy     | String          | keep                         | Handling policy or action taken for requests delayed longer than **flowcontrol.holding.max**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | The value can be:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | -  **keep**: Maintain the backpressure state and wait for the heap memory usage to drop. The server determines whether to release requests based on real-time memory usage. In this mode, requests will be delayed until the memory usage drops to a level that allows the processing to resume. This may cause request timeout.                                                                                                                                                                                                                                         |
      |                                      |                 |                              | -  **soft**: Forcibly execute the requests, but the **inFlight** circuit breaker gets to decide whether to reject them. **inFlight** is a native Elasticsearch circuit breaker designed to prevent system overload. For details, see `Circuit breaker settings <https://www.elastic.co/docs/reference/elasticsearch/configuration-reference/circuit-breaker-settings>`__. This mode allows requests that have been delayed longer than **flowcontrol.holding.max** to proceed. However, it may still cause memory usage to spike and eventually lead to memory overflow. |
      |                                      |                 |                              | -  **hard**: Reject the requests immediately and disconnect client connections. This will drop some requests.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.once_free_max     | String          | 5%                           | Maximum amount of memory (in the form of a percentage of node memory) that flow control is allowed to free in a single reclamation cycle. This parameter prevents overly aggressive memory reclamation that could lead to sudden request surges after memory pressure subsides.                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Value range: 1%-50%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.nudges_gc         | Boolean         | true (recommended)           | Whether to trigger garbage collection (GC) to reclaim memory when the write pressure is too high. (The backpressure connection pool is checked every second. The write pressure is considered high if all existing connections are blocked and new write requests cannot be accepted.)                                                                                                                                                                                                                                                                                   |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | The value can be:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | -  true: Trigger GC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      |                                      |                 |                              | -  false: Not to trigger GC.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                                      |                 |                              |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                      |                 |                              | Setting this parameter to **null** restores the default value.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------+------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Disable memory-based flow control.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.memory.enabled": false
        }
      }

.. _en-us_topic_0000001938218516__section846243514132:

Configuring One-Click Traffic Blocking
--------------------------------------

When triggered, the system immediately disconnects all client connections, but not those used for Kibana access or O&M and monitoring APIs, as an effort to restore the cluster.

#. Enable one-click traffic blocking.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.break.enabled": true
        }
      }

   .. table:: **Table 4** Parameters for configuring one-click traffic blocking

      +---------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                 | Type            | Default Value   | Description                                                                                                                                                                                                            |
      +===========================+=================+=================+========================================================================================================================================================================================================================+
      | flowcontrol.break.enabled | Boolean         | false           | Whether to enable one-click traffic blocking (similar to a circuit breaker). When enabled, the system immediately disconnects all client connections, but not those used for Kibana access or O&M and monitoring APIs. |
      |                           |                 |                 |                                                                                                                                                                                                                        |
      |                           |                 |                 | The value can be:                                                                                                                                                                                                      |
      |                           |                 |                 |                                                                                                                                                                                                                        |
      |                           |                 |                 | -  true: Enable one-click blocking.                                                                                                                                                                                    |
      |                           |                 |                 | -  false: Disable one-click blocking.                                                                                                                                                                                  |
      +---------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Disable one-click traffic blocking.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.break.enabled": false
        }
      }

.. _en-us_topic_0000001938218516__section364216459204:

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

      +--------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Type            | Default Value   | Description                                                                                                                                                        |
      +================================+=================+=================+====================================================================================================================================================================+
      | flowcontrol.log.access.enabled | Boolean         | false           | Whether to enable request statistics sampling, that is, whether to collect request metrics (such as bulk writes and search/msearch requests) by client IP address. |
      |                                |                 |                 |                                                                                                                                                                    |
      |                                |                 |                 | The value can be:                                                                                                                                                  |
      |                                |                 |                 |                                                                                                                                                                    |
      |                                |                 |                 | -  true: Enable request statistics sampling.                                                                                                                       |
      |                                |                 |                 | -  false (default): Disable request statistics sampling.                                                                                                           |
      +--------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.log.access.count   | Integer         | 10              | Maximum number of client IP addresses sampled.                                                                                                                     |
      |                                |                 |                 |                                                                                                                                                                    |
      |                                |                 |                 | Value range: 0-100                                                                                                                                                 |
      |                                |                 |                 |                                                                                                                                                                    |
      |                                |                 |                 | Setting this parameter to **null** restores the default value.                                                                                                     |
      +--------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Check the sampled statistics to analyze the traffic pattern and flow control status by client IP address.

   -  Check the flow control status of all nodes.

      .. code-block:: text

         GET /_nodes/stats/filter/v2

   -  Check the flow control details of all nodes.

      .. code-block:: text

         GET /_nodes/stats/filter/v2?detail

   -  Check the flow control status of a specified node.

      .. code-block:: text

         GET /_nodes/{node_id}/stats/filter/v2

      .. table:: **Table 6** Parameter description

         +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------+
         | Parameter       | Type            | Default Value   | Description                                                                      |
         +=================+=================+=================+==================================================================================+
         | node_id         | String          | N/A             | Specifies one or more cluster nodes.                                             |
         |                 |                 |                 |                                                                                  |
         |                 |                 |                 | -  Single node: Enter the node ID.                                               |
         |                 |                 |                 | -  Multiple nodes: Enter multiple node IDs and use a comma (,) to separate them. |
         |                 |                 |                 |                                                                                  |
         |                 |                 |                 | You can run the following command to obtain node IDs:                            |
         |                 |                 |                 |                                                                                  |
         |                 |                 |                 | .. code:: text                                                                   |
         |                 |                 |                 |                                                                                  |
         |                 |                 |                 |    GET _cat/nodes?s=n&h=n,id&v=true&full_id=true                                 |
         +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------+

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

   .. table:: **Table 7** Response parameters

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

.. _en-us_topic_0000001938218516__section03781045277:

Configuring Access Logging
--------------------------

When access logging is enabled, the system records the URLs and bodies of HTTP/HTTPS requests for cluster load and request analysis. Then, you can use the result to optimize cluster performance.

#. Enable access logging.

   -  Enable access logging for all nodes in a cluster.

      .. code-block:: text

         PUT /_access_log?duration_limit=30s&capacity_limit=1mb

   -  Enable access logging for a specified node in a cluster.

      .. code-block:: text

         PUT /_access_log/{node_id}?duration_limit=30s&capacity_limit=1mb

   .. table:: **Table 8** Parameters for enabling access logging

      +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------+
      | Parameter       | Type            | Default Value   | Description                                                                                       |
      +=================+=================+=================+===================================================================================================+
      | duration_limit  | String          | 30              | Maximum duration for access logging. When this limit is reached, access logging stops.            |
      |                 |                 |                 |                                                                                                   |
      |                 |                 |                 | Value range: 10 to 120                                                                            |
      |                 |                 |                 |                                                                                                   |
      |                 |                 |                 | Unit: s                                                                                           |
      |                 |                 |                 |                                                                                                   |
      |                 |                 |                 | Setting this parameter to **null** restores the default value.                                    |
      |                 |                 |                 |                                                                                                   |
      |                 |                 |                 | Access logging stops when either **duration_limit** or **capacity_limit** is reached.             |
      +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------+
      | capacity_limit  | String          | 1               | Maximum access log size. When the size of an access log reaches this limit, access logging stops. |
      |                 |                 |                 |                                                                                                   |
      |                 |                 |                 | Value range: 1 to 5                                                                               |
      |                 |                 |                 |                                                                                                   |
      |                 |                 |                 | Unit: MB                                                                                          |
      |                 |                 |                 |                                                                                                   |
      |                 |                 |                 | Setting this parameter to **null** restores the default value.                                    |
      |                 |                 |                 |                                                                                                   |
      |                 |                 |                 | Access logging stops when either **duration_limit** or **capacity_limit** is reached.             |
      +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------+

#. Check access logs.

   -  Check the access logs of all nodes in a cluster.

      .. code-block:: text

         GET /_access_log

   -  Check the access logs of a specified cluster node.

      .. code-block:: text

         GET /_access_log/{node_id}

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

   .. table:: **Table 9** Response parameters

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

#. Delete access logs. Logs are stored in the memory. After viewing the logs, you should delete them promptly to reclaim memory resources, and by doing so avoid impacting system performance.

   a. Delete access logs for all nodes.

      .. code-block:: text

         DELETE /_access_log

   b. Check the access logs again to confirm successful deletion.

      .. code-block:: text

         GET /_access_log

.. _en-us_topic_0000001938218516__section1626791610277:

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

   .. table:: **Table 10** Enabling access logging in files

      +------------------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                    | Type            | Default Value   | Description                                                                                                                                                                                                                                                               |
      +==============================+=================+=================+===========================================================================================================================================================================================================================================================================+
      | flowcontrol.log.file.enabled | Boolean         | false           | Whether to record access logs in files. When enabled, the log of each access request is recorded in files.                                                                                                                                                                |
      |                              |                 |                 |                                                                                                                                                                                                                                                                           |
      |                              |                 |                 | The log file name is **Cluster name_access_log.log**. You can check this file only through the log backup function. For details about how to back up logs, see :ref:`Enabling Log Backup <en-us_topic_0000002558581145__en-us_topic_0000001223434432_section3460103108>`. |
      |                              |                 |                 |                                                                                                                                                                                                                                                                           |
      |                              |                 |                 | The value can be:                                                                                                                                                                                                                                                         |
      |                              |                 |                 |                                                                                                                                                                                                                                                                           |
      |                              |                 |                 | -  true: Record access logs in files.                                                                                                                                                                                                                                     |
      |                              |                 |                 | -  false: Not to record access logs in files.                                                                                                                                                                                                                             |
      +------------------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Disable access logging in files.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.file.enabled": false
        }
      }
