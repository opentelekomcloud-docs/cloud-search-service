:original_name: css_01_0407.html

.. _css_01_0407:

Configuring Flow Control 1.0 for an Elasticsearch Cluster
=========================================================

Scenario
--------

Flow Control 1.0 controls traffic at the node level. You can configure blacklists and whitelists per node, the maximum concurrent HTTP connections allowed, the maximum HTTP connections allowed, the maximum heap memory used by specific request paths, and the maximum CPU usage. You can block access in one click, and collect statistics on IP addresses and URLs accessing the nodes. If flow control is enabled, requests will be blocked at the entry, which alleviates the cluster pressure in high-concurrency scenarios and reduces the likelihood of unavailability issues.

.. table:: **Table 1** Flow control policies

   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | Policy                                 | Description                                                                                                                                                                                                                                                                                                                                                                             | Details                                                                                 |
   +========================================+=========================================================================================================================================================================================================================================================================================================================================================================================+=========================================================================================+
   | HTTP/HTTPS flow control                | -  You can control cluster access by client IP address or subnet through the HTTP/HTTPS blacklist or whitelist. If an IP address is in the blacklist, the client is disconnected right away and all its requests are rejected. The whitelist takes precedence over the blacklist. If a client IP address is on both the blacklist and whitelist, requests from it will not be rejected. | :ref:`Enabling HTTP/HTTPS Flow Control per Node <css_01_0407__section1023014371242>`    |
   |                                        | -  Flow control based on concurrent HTTP/HTTPS connections limits the total number of HTTP/HTTPS connections to a node per second.                                                                                                                                                                                                                                                      |                                                                                         |
   |                                        | -  Flow control based on new HTTP/HTTPS connections limits the number of new connections to a node.                                                                                                                                                                                                                                                                                     |                                                                                         |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | Memory flow control                    | Memory flow control limits request paths based on heap memory usage. You can configure a whitelist for memory flow control, a global memory usage threshold, and per-path heap memory thresholds. The global memory flow control threshold takes precedence over the memory threshold of a single path. Paths on the whitelist are exempt from memory flow control.                     | :ref:`Enabling Memory Flow Control <css_01_0407__section12926193210818>`                |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | Global path whitelist for flow control | You can configure the global path whitelist for flow control as required when you need to use custom plug-ins.                                                                                                                                                                                                                                                                          | :ref:`Adding a Global Path Whitelist for Flow Control <css_01_0407__section8250826148>` |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | Request sampling                       | Request sampling can record the number of access requests from client IP addresses and the request paths of sampled users. Based on the statistics, you can identify and analyze access traffic by client IP addresses and request paths.                                                                                                                                               | :ref:`Enabling Request Sampling <css_01_0407__section846243514132>`                     |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | One-click traffic blocking             | One-click traffic blocking blocks all client connections to a node. This, however, does not include connections for Kibana access or Elasticsearch monitor APIs.                                                                                                                                                                                                                        | :ref:`Enable One-Click Traffic Blocking <css_01_0407__section364216459204>`             |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | Flow control                           | Flow control provides an independent API for checking traffic statistics and records the number API calls. You can evaluate the flow control threshold and analyze the cluster load based on these statistics.                                                                                                                                                                          | :ref:`Viewing Flow Control Information <css_01_0407__section03781045277>`               |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | Access logging                         | Access logs record the URLs and bodies of HTTP/HTTPS requests received by nodes within a period of time. You can analyze the current traffic load based on the access logs.                                                                                                                                                                                                             | :ref:`Enabling and Viewing Access Logs <css_01_0407__section1626791610277>`             |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | Access logging in files                | Any cluster access is recorded in the **{Cluster name\ \_access_log.log}** file. You can use the log backup function to view detailed access logs on OBS.                                                                                                                                                                                                                               | :ref:`Enabling Access Logging in Files <css_01_0407__section072285622916>`              |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+
   | CPU flow control                       | You can configure the node CPU usage threshold to limit inbound traffic for each node.                                                                                                                                                                                                                                                                                                  | :ref:`Enabling CPU Flow Control <css_01_0407__section159551120113420>`                  |
   +----------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------+

Constraints
-----------

-  Elasticsearch 7.6.2 and Elasticsearch 7.10.2 clusters created after January 2023 support Flow Control 2.0 only, whereas those created before that support Flow Control 1.0 only.
-  Flow control may hurt the performance of some nodes.
-  If flow control is enabled, user requests that exceed the flow control threshold will be rejected.
-  Enabling memory flow control may hurt the performance of some search requests or cause some Kibana search requests to fail.
-  Enabling access logging may hurt cluster performance.
-  Memory flow control and CPU flow control are based on request paths. Avoid configuring too many paths or paths that are too long, as they may hurt cluster performance.

.. _css_01_0407__section1023014371242:

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

      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item             | Type                  | Description                                                                                                                                                                                                                                                                    |
      +================================+=======================+================================================================================================================================================================================================================================================================================+
      | flowcontrol.http.enabled       | Boolean               | Whether to enable HTTP/HTTPS flow control. HTTP/HTTPS flow control is disabled by default. Enabling it may affect node access performance.                                                                                                                                     |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | Value: **true** or **false**                                                                                                                                                                                                                                                   |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | Default value: **false**                                                                                                                                                                                                                                                       |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.allow         | List<String>          | IP address whitelist.                                                                                                                                                                                                                                                          |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | It can contain multiple IP addresses and subnet masks, or lists of IP addresses. Use commas (,) to separate different items. Example: **xx.xx.xx.xx/24,xx.xx.xx.xx/24**, or **xx.xx.xx.xx,xx.xx.xx.xx**.                                                                       |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | The default value is null.                                                                                                                                                                                                                                                     |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.deny          | List<String>          | IP address blacklist.                                                                                                                                                                                                                                                          |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | It can contain multiple IP addresses and subnet masks, or lists of IP addresses. Use commas (,) to separate different items.                                                                                                                                                   |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | The default value is null.                                                                                                                                                                                                                                                     |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.concurrent    | Integer               | Maximum concurrent HTTP/HTTPS connections.                                                                                                                                                                                                                                     |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | Default value: Number of available cores on a node x 600.                                                                                                                                                                                                                      |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.newconnect    | Integer               | Maximum new connections that can be created for HTTP/HTTPS requests per second.                                                                                                                                                                                                |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | Default value: Number of available cores on a node x 200.                                                                                                                                                                                                                      |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.http.warmup_period | Integer               | Time required for the HTTP/HTTPS connection setup speed to reach the maximum. If **flowcontrol.http.newconnect** is set to **100** and **flowcontrol.http.warmup_period** is set to **5000ms**, it indicates the system can set up 100 connections per second 5 seconds later. |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | Value range: 0-10000                                                                                                                                                                                                                                                           |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | Unit: ms                                                                                                                                                                                                                                                                       |
      |                                |                       |                                                                                                                                                                                                                                                                                |
      |                                |                       | Default value: **0**                                                                                                                                                                                                                                                           |
      +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

.. _css_01_0407__section12926193210818:

Enabling Memory Flow Control
----------------------------

.. note::

   Enabling memory flow control in Elasticsearch 5.5.1 will cause **\_mget** requests to be blocked and Kibana access to become unavailable. You can add \_mget requests to the flow control whitelist to avoid this problem.

#. Enable memory flow control.

   -  Run the following command to enable memory flow control:

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.memory.enabled": true,
             "flowcontrol.memory.allow_path": "/index/_search",
             "flowcontrol.memory.heap_limit": "85%"
           }
         }

   -  Run the following command to enable memory flow control for a single request path.

      Configure the heap memory usage threshold for a request path. You can configure priorities for such threshold rules.

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.memory.enabled": true,
             "flowcontrol.memory": {
               "flowcontrol_search": {
                 "filter_path": "index1/_search",
                 "heap_limit": "50%"
               },
               "flowcontrol_bulk": {
                 "filter_path": "index*/_bulk",
                 "heap_limit": "50%"
               }
             }
           }
         }

   .. table:: **Table 3** Configuration items for memory flow control

      +----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item               | Type                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +==================================+=======================+==============================================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | flowcontrol.memory.enabled       | Boolean               | Whether to enable memory flow control. This function is disabled by default. Enabling memory flow control may slightly affect node performance.                                                                                                                                                                                                                                                                                                              |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Value: **true** or **false**                                                                                                                                                                                                                                                                                                                                                                                                                                 |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Default value: **false**                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      +----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.allow_path    | List<String>          | Request path whitelist for memory flow control.                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Whitelisted paths are exempt from memory flow control. Wildcard characters are supported. By default, query APIs controlled by the cluster are exempt from memory flow control. This prevents the failure to query cluster information when the memory usage reaches the threshold.                                                                                                                                                                          |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Example:                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | -  "flowcontrol.memory.allow_path": "/index/_search",                                                                                                                                                                                                                                                                                                                                                                                                        |
      |                                  |                       | -  "flowcontrol.memory.allow_path": "/index*/_search",                                                                                                                                                                                                                                                                                                                                                                                                       |
      |                                  |                       | -  "flowcontrol.memory.allow_path": ["/index/_search", "/index1/_bulk"],                                                                                                                                                                                                                                                                                                                                                                                     |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | A maximum of 10 paths can be configured. A path can contain up to 32 characters.                                                                                                                                                                                                                                                                                                                                                                             |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | The default value is null.                                                                                                                                                                                                                                                                                                                                                                                                                                   |
      +----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.heap_limit    | String                | Maximum global heap memory usage of a node before flow control is triggered. The value cannot be less than 10% of the heap memory.                                                                                                                                                                                                                                                                                                                           |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Value range: 10%-100%                                                                                                                                                                                                                                                                                                                                                                                                                                        |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Default value: **90%**                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      +----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.*.filter_path | String                | Paths under memory flow control.                                                                                                                                                                                                                                                                                                                                                                                                                             |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | The default value is **\*\***, indicating all paths. If **flowcontrol.memory.heap_limit** is configured and **flowcontrol.memory.*.filter_path** is not, it indicates that all the paths, except those in the whitelist, are under control. The whitelist takes precedence over the single-path rule. If a path is specified in both **flowcontrol.memory.allow_path** and **flowcontrol.memory.*.filter_path**, the requests from the path will be allowed. |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | For example, if **flowcontrol.memory.allow_path** and **flowcontrol.memory.*.filter_path** are both set to **abc/_search**, then **abc/_search** will not be under flow control.                                                                                                                                                                                                                                                                             |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Maximum length: **32** characters                                                                                                                                                                                                                                                                                                                                                                                                                            |
      +----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.memory.*.heap_limit  | String                | Heap memory usage threshold of request paths. If the heap memory usage exceeds the threshold, flow control will be triggered.                                                                                                                                                                                                                                                                                                                                |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Value range: 0-100%                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                  |                       | Default value: **90%**                                                                                                                                                                                                                                                                                                                                                                                                                                       |
      +----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      If all parameters are set to **null**, they will be restored to their default values.

#. Run the following command to disable memory flow control:

   -  Run the following command to delete memory flow control for a single request path.

      Before disabling memory flow control, you need delete per-request path memory flow control configuration.

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.memory.enabled": true,
             "flowcontrol.memory": {
               "flowcontrol_search": {
                 "filter_path": null,
                 "heap_limit": null
               }
             }
           }
         }

   -  Run the following command to disable memory flow control:

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.memory.enabled": false
           }
         }

.. _css_01_0407__section8250826148:

Adding a Global Path Whitelist for Flow Control
-----------------------------------------------

Run the following command to add a global path whitelist for flow control:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "flowcontrol.path.white_list": "xxxx"
     }
   }

.. table:: **Table 4** Configuration items for a global path whitelist for flow control

   +-----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Configuration Item          | Type                  | Description                                                                                                                                                                         |
   +=============================+=======================+=====================================================================================================================================================================================+
   | flowcontrol.path.white_list | List<String>          | Paths that are exempt from flow control. These paths are not affected by memory flow control, CPU flow control, or one-click blocking; but are under IP address-based flow control. |
   |                             |                       |                                                                                                                                                                                     |
   |                             |                       | A maximum of 10 paths can be configured. A path can contain up to 32 characters.                                                                                                    |
   |                             |                       |                                                                                                                                                                                     |
   |                             |                       | The default value is null.                                                                                                                                                          |
   |                             |                       |                                                                                                                                                                                     |
   |                             |                       | .. note::                                                                                                                                                                           |
   |                             |                       |                                                                                                                                                                                     |
   |                             |                       |    You are advised not to configure this parameter, unless required by plug-ins.                                                                                                    |
   +-----------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   If all parameters are set to **null**, they will be restored to their default values.

.. _css_01_0407__section846243514132:

Enabling Request Sampling
-------------------------

#. Run the following command to enable request sampling:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.statics.enabled": true,
          "flowcontrol.statics.threshold": 100,
          "flowcontrol.statics.sample_frequency": 50
        }
      }

   .. table:: **Table 5** Configuration items for request sampling

      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item                   | Type                  | Description                                                                                                                                                                                                                                        |
      +======================================+=======================+====================================================================================================================================================================================================================================================+
      | flowcontrol.statics.enabled          | Boolean               | Whether to enable request sampling. Request sampling may affect node performance.                                                                                                                                                                  |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       | Value: **true** or **false**                                                                                                                                                                                                                       |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       | Default value: **false**                                                                                                                                                                                                                           |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.statics.threshold        | Integer               | Number of recent access requests whose statistics are collected. The value **100** indicates that statistics will be collected on the 100 IP addresses and 100 URLs that are most frequently accessed.                                             |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       | Minimum value: **10**                                                                                                                                                                                                                              |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       | Maximum value: **1000**                                                                                                                                                                                                                            |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       | Default value: **100**                                                                                                                                                                                                                             |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       | .. note::                                                                                                                                                                                                                                          |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       |    -  The IP address statistics and URL sampling statistics are cached based on their access time. If the number of cached records reaches the threshold configured using **flowcontrol.statics.threshold**, the earliest records will be deleted. |
      |                                      |                       |    -  In URL sampling, an access path is uniquely identified by its URL hash.                                                                                                                                                                      |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.statics.sample_frequency | Integer               | Path sampling frequency. If this parameter is set to **100**, samples are collected from every 100 requests.                                                                                                                                       |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       | Minimum value: **50**                                                                                                                                                                                                                              |
      |                                      |                       |                                                                                                                                                                                                                                                    |
      |                                      |                       | Default value: **100**                                                                                                                                                                                                                             |
      +--------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      If all parameters are set to **null**, they will be restored to their default values.

#. Run the following command to disable request sampling:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.statics.enabled": false
        }
      }

.. _css_01_0407__section364216459204:

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

.. _css_01_0407__section03781045277:

Viewing Flow Control Information
--------------------------------

-  Check the flow control status of all nodes.

   .. code-block:: text

      GET /_nodes/stats/filter

-  View the flow control status of a specific node.

   .. code-block:: text

      GET /_nodes/{nodeId}/stats/filter

   **{nodeId}** indicates the ID of the node you want to check.

Example response:

.. note::

   In the response, the information of each node is separated. The **http** field records the numbers of concurrent connections and new connections. The **memory** records memory flow control statistics. The **ip_address** field records the recent client IP addresses that are accessed most recently. The **url_sample** field records the recent URLs that are requested most frequently. The **cpu** field records CPU flow control statistics.

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

.. table:: **Table 6** Response parameters

   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter           | Description                                                                                                                                                                                                                                                                                                                                |
   +=====================+============================================================================================================================================================================================================================================================================================================================================+
   | concurrent_req      | Number of TCP connections of a node, which is recorded no matter whether flow control is enabled. This value is similar to the value of **current_open** of the **GET /_nodes/stats/http** API but is smaller, because whitelisted IP addresses and internal node IP addresses are not counted.                                            |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rejected_concurrent | Number of concurrent connections rejected during HTTP flow control. Disabling HTTP flow control does not clear this record.                                                                                                                                                                                                                |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rejected_new        | Number of new connections rejected during HTTP flow control. Disabling HTTP flow control does not clear this record.                                                                                                                                                                                                                       |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rejected_deny       | Number of requests rejected based on the blacklist during HTTP flow control. Disabling HTTP flow control does not clear this record.                                                                                                                                                                                                       |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | memory_allow        | Number of allowed requests during memory flow control. This parameter takes effect when memory flow control is enabled, and its value is not cleared after memory flow control is disabled. The requests from the paths in the **allow_path** whitelist are not recorded. If **allow_path** is set to **\*\***, no requests are recorded.  |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | memory_rejected     | Number of rejected requests during memory flow control. This parameter takes effect when memory flow control is enabled, and its value is not cleared after memory flow control is disabled. The requests from the paths in the **allow_path** whitelist are not recorded. If **allow_path** is set to **\*\***, no requests are recorded. |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | rejected_cpu        | Number of requests rejected when the CPU flow control threshold is exceeded. This parameter takes effect when CPU flow control is enabled, and its value is not cleared after CPU flow control is disabled.                                                                                                                                |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ip_address          | IP addresses and the number of requests. For details, see :ref:`Table 7 <css_01_0407__en-us_topic_0000001273451905_table8881825155010>`\ :ref:`Table 7 <css_01_0407__en-us_topic_0000001273451905_table8881825155010>`.                                                                                                                    |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | url_sample          | Request path sampling. The number of URLs of a request are collected based on the configured time and sampling interval. For details, see :ref:`Table 8 <css_01_0407__en-us_topic_0000001273451905_table72712520501>`.                                                                                                                     |
   +---------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _css_01_0407__en-us_topic_0000001273451905_table8881825155010:

.. table:: **Table 7** ip_address

   ========= =============================================
   Parameter Description
   ========= =============================================
   ip        Source IP address for accessing the node.
   method    Number of access requests from an IP address.
   ========= =============================================

.. _css_01_0407__en-us_topic_0000001273451905_table72712520501:

.. table:: **Table 8** url_sample

   ============== ================================================
   Parameter      Description
   ============== ================================================
   url            Request URL
   method         Method corresponding to the request path
   remote_address Source IP address and port number in the request
   count          How many times a path is sampled
   ============== ================================================

.. _css_01_0407__section1626791610277:

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

   .. table:: **Table 9** Configuration items for configuring access logging

      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
      | Configuration Item    | Type                  | Description                                                                                     |
      +=======================+=======================+=================================================================================================+
      | duration_limit        | String                | Duration recorded in an access log.                                                             |
      |                       |                       |                                                                                                 |
      |                       |                       | Value range: 10 to 120                                                                          |
      |                       |                       |                                                                                                 |
      |                       |                       | Unit: s                                                                                         |
      |                       |                       |                                                                                                 |
      |                       |                       | Default value: **30**                                                                           |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+
      | capacity_limit        | String                | Size of an access log. When the size of an access log reaches this value, access logging stops. |
      |                       |                       |                                                                                                 |
      |                       |                       | Value range: 1 to 5                                                                             |
      |                       |                       |                                                                                                 |
      |                       |                       | Unit: MB                                                                                        |
      |                       |                       |                                                                                                 |
      |                       |                       | Default value: **1**                                                                            |
      +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------+

   .. note::

      -  Access logging stops when either **duration_limit** or **capacity_limit** reaches their thresholds.
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

   .. table:: **Table 10** Response parameters

      +-----------+------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter | Description                                                                                                                              |
      +===========+==========================================================================================================================================+
      | name      | Node name                                                                                                                                |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------------+
      | host      | Node IP address                                                                                                                          |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------------+
      | count     | Number of node access requests in a statistical period                                                                                   |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------------+
      | access    | Details about node access requests in a statistical period For details, see :ref:`Table 11 <css_01_0407__css_01_0406_table72934522332>`. |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------------+

   .. _css_01_0407__css_01_0406_table72934522332:

   .. table:: **Table 11** access

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

   -  Delete access logs of all nodes in a cluster.

      .. code-block:: text

         DELETE /_access_log

   -  Delete access logs of a specified node in a cluster.

      .. code-block:: text

         DELETE /_access_log/{nodeId}

      **{nodeId}** indicates the node ID.

.. _css_01_0407__section072285622916:

Enabling Access Logging in Files
--------------------------------

.. note::

   -  When access logging in files is enabled, any cluster access is recorded in the **{Cluster name\ \_access_log.log}** file. You can use the log backup function to view detailed access logs on OBS.
   -  You are advised to use this function for troubleshooting only. After problems are solved, disable this function.

#. Run the following command to enable access logging in files:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.file.enabled": true
        }
      }

   .. table:: **Table 12** Configuration items for enabling access logging in files

      +------------------------------+-----------------------+----------------------------------------------------------------+
      | Parameter                    | Type                  | Description                                                    |
      +==============================+=======================+================================================================+
      | flowcontrol.log.file.enabled | Boolean               | Whether to record the details of each request in the log file. |
      |                              |                       |                                                                |
      |                              |                       | Value:                                                         |
      |                              |                       |                                                                |
      |                              |                       | -  true                                                        |
      |                              |                       | -  false (default value)                                       |
      +------------------------------+-----------------------+----------------------------------------------------------------+

#. Run the following command to disable access logging in files:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.log.file.enabled": false
        }
      }

.. _css_01_0407__section159551120113420:

Enabling CPU Flow Control
-------------------------

#. Run the following command to enable CPU flow control:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.cpu.enabled": true,
          "flowcontrol.cpu.percent_limit": 80,
          "flowcontrol.cpu.allow_path": ["index/_search"]
        }
      }

   .. table:: **Table 13** Configuration items for configuring access logging

      +-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item            | Type                  | Description                                                                                                                                                                                                                                                    |
      +===============================+=======================+================================================================================================================================================================================================================================================================+
      | flowcontrol.cpu.enabled       | Boolean               | Whether to enable CPU flow control.                                                                                                                                                                                                                            |
      |                               |                       |                                                                                                                                                                                                                                                                |
      |                               |                       | The value can be:                                                                                                                                                                                                                                              |
      |                               |                       |                                                                                                                                                                                                                                                                |
      |                               |                       | -  true                                                                                                                                                                                                                                                        |
      |                               |                       | -  false (default value)                                                                                                                                                                                                                                       |
      +-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.cpu.percent_limit | Integer               | Maximum CPU usage (%) of a node before flow control is triggered.                                                                                                                                                                                              |
      |                               |                       |                                                                                                                                                                                                                                                                |
      |                               |                       | Default value: **90**                                                                                                                                                                                                                                          |
      +-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | flowcontrol.cpu.allow_path    | List<String>          | Path whitelist for CPU flow control.                                                                                                                                                                                                                           |
      |                               |                       |                                                                                                                                                                                                                                                                |
      |                               |                       | The paths specified using this parameter are exempt from CPU flow control. By default, query APIs controlled by the cluster are exempt from CPU flow control. This prevents the failure to query cluster information when the CPU usage reaches the threshold. |
      |                               |                       |                                                                                                                                                                                                                                                                |
      |                               |                       | Example:                                                                                                                                                                                                                                                       |
      |                               |                       |                                                                                                                                                                                                                                                                |
      |                               |                       | -  "flowcontrol.memory.allow_path": "/index/_search",                                                                                                                                                                                                          |
      |                               |                       | -  "flowcontrol.memory.allow_path": "/index*/_search",                                                                                                                                                                                                         |
      |                               |                       | -  "flowcontrol.memory.allow_path": ["/index/_search", "/index1/_bulk"],                                                                                                                                                                                       |
      |                               |                       |                                                                                                                                                                                                                                                                |
      |                               |                       | A maximum of 10 paths can be configured. A path can contain up to 32 characters.                                                                                                                                                                               |
      |                               |                       |                                                                                                                                                                                                                                                                |
      |                               |                       | The default value is null.                                                                                                                                                                                                                                     |
      +-------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      If all parameters are set to **null**, they will be restored to their default values.

#. Run the following command to disable CPU flow control:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent": {
          "flowcontrol.cpu.enabled": false
        }
      }
