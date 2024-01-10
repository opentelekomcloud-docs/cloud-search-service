:original_name: css_01_0142.html

.. _css_01_0142:

Memory Flow Control
===================

Context
-------

Elasticsearch provides a circuit breaker, which will terminate requests if the memory usage exceeds its threshold. However, Elasticsearch does not check the heap memory usage when an API is called, and does not allow users to configure the threshold for a single request. In this case, memory usage can only be calculated during request processing, which may lead to frequent circuit breaking and cannot avoid heap memory waste. To solve this problem, CSS checks the heap memory usage when receiving REST requests, blocking excess API requests and protecting nodes. You can configure global memory flow control, or configure the request path and heap memory threshold for a specific request path. Before a request is processed, the system checks the configured heap memory threshold. If the threshold is exceeded, the request path will be blocked.

.. note::

   -  Memory flow control may affect request processing performance.
   -  If the memory flow control is enabled, some Kibana search requests may fail.
   -  If memory flow control is enabled in Elasticsearch 5.5.1, \_mget requests will be blocked and Kibana access will be abnormal. You can add \_mget requests to the request whitelist to avoid this problem.

The following table describes memory flow control parameters.

.. table:: **Table 1** Memory flow control parameters

   +----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                        | Type                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   +==================================+=======================+==============================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | flowcontrol.memory.enabled       | Boolean               | Whether to enable memory flow control. This function is disabled by default. Enabling memory flow control may slightly affect node performance.                                                                                                                                                                                                                                                                                                              |
   |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   |                                  |                       | Value: **true** or **false**                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   |                                  |                       | Default value: **false**                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   +----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.memory.allow_path    | List<String>          | Request path whitelist for memory flow control.                                                                                                                                                                                                                                                                                                                                                                                                              |
   |                                  |                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   |                                  |                       | Whitelisted paths are blocked in memory flow control. Wildcard characters are supported. By default, query APIs controlled by the cluster are not blocked in memory flow control. This prevents the failure to query cluster information when the memory usage reaches the threshold.                                                                                                                                                                        |
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
   | flowcontrol.memory.heap_limit    | String                | Maximum global heap memory usage of a node. The value cannot be less than 10% of the heap memory.                                                                                                                                                                                                                                                                                                                                                            |
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

Procedure
---------

#. Log in to the CSS management console.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
#. In the navigation pane on the left, choose **Dev Tools** and run commands to enable or disable memory flow control.

   -  Enabling memory flow control

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.memory.enabled": true,
             "flowcontrol.memory.allow_path": "/index/_search",
             "flowcontrol.memory.heap_limit": "85%"
           }
         }

   -  Enabling memory flow control for a request path

      Configure the heap memory usage threshold for a request path. You can configure the priorities of such threshold rules.

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

   -  Deleting the memory flow control configuration of a request path

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

   -  Disabling cluster memory flow control

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.memory.enabled": false
           }
         }
