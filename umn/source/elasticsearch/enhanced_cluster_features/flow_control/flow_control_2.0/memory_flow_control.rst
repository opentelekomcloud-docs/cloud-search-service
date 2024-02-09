:original_name: css_01_0194.html

.. _css_01_0194:

Memory Flow Control
===================

Context
-------

Elasticsearch provides a circuit breaker, which will terminate requests or return the error code **429** if the memory usage exceeds its threshold. However, the circuit breaker rejects a request only after the node reads the entire request, which occupies heap memory. To prevent a request from being fully received by a node before the request is rejected, you can control the client traffic based on the real-time status of the node heap memory.

Configuring Parameters
----------------------

The following table describes memory flow control parameters.

.. table:: **Table 1** Memory flow control parameters

   +--------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                            | Type                  | Description                                                                                                                                                                                                                                                                                                   |
   +======================================+=======================+===============================================================================================================================================================================================================================================================================================================+
   | flowcontrol.memory.enabled           | Boolean               | Whether to enable memory flow control. After this function is enabled, the memory usage is continuously monitored. The value can be:                                                                                                                                                                          |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | -  **true**                                                                                                                                                                                                                                                                                                   |
   |                                      |                       | -  **false** (default value)                                                                                                                                                                                                                                                                                  |
   +--------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.memory.heap_limit        | String                | Maximum global heap memory usage of a node. If the value of this parameter is exceeded, traffic backpressure is performed.                                                                                                                                                                                    |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | Value range: 10%-100%                                                                                                                                                                                                                                                                                         |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | Default value: **90%**                                                                                                                                                                                                                                                                                        |
   +--------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.holding.in_flight_factor | Float                 | Backpressure release factor. The principle is similar to that of the circuit breaker parameter **network.breaker.inflight_requests.overhead**. When the memory usage reaches the limit, a larger value indicates stronger backpressure. The write traffic will be limited.                                    |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | Value range: >= 0.5                                                                                                                                                                                                                                                                                           |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | Default value: **1.0**                                                                                                                                                                                                                                                                                        |
   +--------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.holding.max              | TimeValue             | Maximum delay of each request. If the delay exceeds the value of this parameter, you can disconnect the request backpressure or disconnect the request link. For details, see the configuration of **flowcontrol.holding.max_strategy**.                                                                      |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | Value range: >= 15s                                                                                                                                                                                                                                                                                           |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | Default value: **60s**                                                                                                                                                                                                                                                                                        |
   +--------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.holding.max_strategy     | String                | Policy after the maximum delay time is exceeded. The value can be:                                                                                                                                                                                                                                            |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | -  **keep** (default value): If the heap memory is still high, continue the backpressure. The server determines when to execute the request based on the real-time memory.                                                                                                                                    |
   |                                      |                       | -  **soft**: The requests will be executed even if the heap memory is still high. The **inFlight** circuit breaker will determine whether to execute or reject the requests.                                                                                                                                  |
   |                                      |                       | -  **hard**: If the heap memory is still high, requests will be discarded and the client connection of the requests will be disconnected.                                                                                                                                                                     |
   +--------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.memory.once_free_max     | String                | Maximum memory that can be opened at a time for a suspended request queue. This parameter is used to prevent a cluster from being entirely suspended due to temporary low memory under high pressure.                                                                                                         |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | Value range: 1 to 50                                                                                                                                                                                                                                                                                          |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | Default value: **10%**                                                                                                                                                                                                                                                                                        |
   +--------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.memory.nudges_gc         | Boolean               | Whether to trigger garbage collection to ensure write stability when the write pressure is too high. (The backpressure connection pool is checked every second. The write pressure is regarded high if all the existing connections are blocked and new write requests cannot be released.) The value can be: |
   |                                      |                       |                                                                                                                                                                                                                                                                                                               |
   |                                      |                       | -  **true** (default value)                                                                                                                                                                                                                                                                                   |
   |                                      |                       | -  **false**                                                                                                                                                                                                                                                                                                  |
   +--------------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   -  **flowcontrol.memory.enabled** and **flowcontrol.memory.heap_limit** are the most important parameters. *enabled* indicates the memory flow control switch, and *heap_limit* indicates the heap memory threshold of a node.
   -  The default value 90% of **flowcontrol.memory.heap_limit** is a conservative threshold. When the heap memory usage is greater than 90%, the system stops reading large requests that exceed 64 KB from the client until the heap memory decreases. If the heap memory decreases to 85%, the maximum client data that can be read is 5% of the maximum heap memory. If the heap memory usage has been higher than 90% for a long time, client connection requests cannot be read. In this case, the GC algorithm is triggered to perform garbage collection until the heap memory usage is lower than the threshold.
   -  Generally, you can set the **flowcontrol.memory.heap_limit** threshold to 80% or less to ensure that the node has certain heap memory for operations besides data writing, such as Elasticsearch query and segment merge.

Procedure
---------

#. Log in to the CSS management console.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
#. In the navigation pane on the left, choose **Dev Tools** and run commands to enable or disable memory flow control.

   -  Enable memory flow control

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.memory.enabled": true,
             "flowcontrol.memory.heap_limit": "80%"
           }
         }

   -  Disable cluster memory flow control

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.memory.enabled": false
           }
         }
