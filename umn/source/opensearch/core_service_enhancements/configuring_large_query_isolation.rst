:original_name: css_01_0053.html

.. _css_01_0053:

Configuring Large Query Isolation
=================================

Large query isolation can be configured to manage queries that have high memory usage or take too long to complete. This helps improve the stability of OpenSearch clusters and prevent out-of-memory (OOM) exceptions.

As business grows, your OpenSearch clusters may face mounting query pressure. Some complex queries may occupy excessive node memory, triggering frequent garbage collection or even OOM exceptions, which may compromise cluster performance and stability. Large query isolation enables effective management of memory-intensive, time-consuming query requests, ensuring cluster stability. Large query isolation includes the following:

-  Isolating large queries: Manages memory-intensive/time-consuming queries separately to avoid impacting other queries.
-  Query cancellation based on a heap memory usage threshold: Cancels a large query in the isolation pool when the node heap memory usage reaches a predefined threshold.
-  Global query timeout: Automatically cancels tasks when they last longer than a predefined timeout. This timeout applies globally.

How the Feature Works
---------------------

-  Defining large queries:

   -  The system checks the memory usage of all ongoing queries and flags queries that exceed a predefined memory usage threshold as large queries.
   -  The system periodically checks the execution duration of all ongoing queries and flags queries that exceed a predefined duration threshold as large queries.

-  Query cancellation policies:

   -  fair: Determines which query to cancel by considering both memory usage and execution duration.
   -  mem-first: Cancels the query that has the highest memory usage.
   -  time-first: Cancels the query that has lasted the longest.

-  Native cancel API: OpenSearch's native cancel API can be used to cancel tasks, ensuring compatibility.

Constraints
-----------

Only OpenSearch 2.19.0 supports large query isolation, which is enabled by default. The global timeout is disabled by default for large query isolation. You can enable and configure it via an API when necessary. Any change takes effect immediately.

Logging In to OpenSearch Dashboards
-----------------------------------

Log in to OpenSearch Dashboards and go to the command execution page. OpenSearch clusters support multiple access methods. This topic uses OpenSearch Dashboards as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.


Configuring Large Query Isolation
---------------------------------

Large query isolation places large queries in an isolation pool, where they may be cancelled based on preset memory or duration thresholds. Large query isolation is **enabled by default**. You can modify this setting whenever necessary. Any change takes effect immediately.

#. Run the following command to enable or disable large query isolation:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.enabled": true
        }
      }

   .. table:: **Table 1** Setting large query isolation

      +-------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------+
      | Parameter               | Type            | Default Value   | Description                                                                                                            |
      +=========================+=================+=================+========================================================================================================================+
      | search.isolator.enabled | Boolean         | true            | Whether to enable large query isolation. When enabled, large queries are managed separately from other normal queries. |
      |                         |                 |                 |                                                                                                                        |
      |                         |                 |                 | The value can be:                                                                                                      |
      |                         |                 |                 |                                                                                                                        |
      |                         |                 |                 | -  **true**: Enable large query isolation.                                                                             |
      |                         |                 |                 | -  **false**: Disable large query isolation.                                                                           |
      +-------------------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------+

#. Run the following commands to configure thresholds for defining a large query task:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.memory.task.limit": "50MB",
          "search.isolator.time.management": "10s"
        }
      }

   .. table:: **Table 2** Parameters for configuring large query isolation thresholds

      +-----------------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Type            | Default Value   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      +===================================+=================+=================+==========================================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | search.isolator.memory.task.limit | String          | 50MB            | Large query memory threshold: When a query requests more memory than specified by this threshold, it is placed into an isolation pool.                                                                                                                                                                                                                                                                                                                   |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | Value format: number + unit                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | -  Number: a natural number                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | -  Unit: B, K, KB, M, MB, G, GB, T, TB, P, or PB (case-insensitive)                                                                                                                                                                                                                                                                                                                                                                                      |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | Minimum value: 0 (all queries are placed into the isolation pool)                                                                                                                                                                                                                                                                                                                                                                                        |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | Maximum value: maximum node heap memory                                                                                                                                                                                                                                                                                                                                                                                                                  |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | Lowering this value will cause more queries to be placed into the isolation pool, which will increase its memory usage. If you do lower this value, you should also increase the values of **search.isolator.memory.pool.limit** and **search.isolator.count.limit**, so that the isolation pool can hold more queries. This helps avoid triggering the circuit breaker mechanism due to resource exhaustion (for example, frequent query cancellation). |
      +-----------------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.time.management   | String          | 10s             | Large query execution duration threshold: When a query has lasted longer than specified by this threshold, it is placed into an isolation pool.                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | Value format: number + unit                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | -  Number: a natural number                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | -  Unit: nanos (nanosecond), micros (microsecond), ms (millisecond), s (second), m (minute), h (hour), or d (day)                                                                                                                                                                                                                                                                                                                                        |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | Minimum value: 0 (all queries are placed into the isolation pool)                                                                                                                                                                                                                                                                                                                                                                                        |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
      |                                   |                 |                 | Lowering this value will cause more queries to be placed into the isolation pool, which will increase its memory usage. If you do lower this value, you should also increase the values of **search.isolator.memory.pool.limit** and **search.isolator.count.limit**, so that the isolation pool can hold more queries. This helps avoid triggering the circuit breaker mechanism due to resource exhaustion (for example, frequent query cancellation). |
      +-----------------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Configure the resource usage thresholds for triggering query cancellation.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.memory.pool.limit": "50%",
          "search.isolator.count.limit": 1000,
          "search.isolator.memory.heap.limit": "90%"
        }
      }

   .. table:: **Table 3** Parameters for configuring query cancellation thresholds

      +-----------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Type            | Default Value   | Description                                                                                                                                                                                                                                                                                                                                                  |
      +===================================+=================+=================+==============================================================================================================================================================================================================================================================================================================================================================+
      | search.isolator.memory.pool.limit | String          | 50%             | Maximum memory usage of the isolation pool as a percentage of the maximum node heap memory. When the total memory usage of large queries in the isolation pool exceeds this limit, the system cancels one of the large queries in the isolation pool based on a predefined policy to free resources and prevent memory overflow.                             |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | Value range: 0.0-100.0%                                                                                                                                                                                                                                                                                                                                      |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | If your cluster primarily handles large queries (high memory usage or long execution time), increase this value. Meanwhile, set **search.isolator.memory.task.limit** and **search.isolator.time.management** accordingly to control the number of queries placed into the isolation pool.                                                                   |
      +-----------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.count.limit       | Integer         | 1000            | Maximum number of large queries allowed in the isolation pool. When this limit is reached, no more queries can be added to the isolation pool, preventing resource exhaustion.                                                                                                                                                                               |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | Value range: **10**\ ``-``\ **50000**                                                                                                                                                                                                                                                                                                                        |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | If your cluster primarily handles large queries (high memory usage or long execution time), increase this value. Meanwhile, set **search.isolator.memory.task.limit** and **search.isolator.time.management** accordingly to control the number of queries placed into the isolation pool.                                                                   |
      +-----------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.memory.heap.limit | String          | 90%             | Node heap memory usage that triggers large query cancellation in the isolation pool. When this threshold is reached, the system cancels one of the large queries in the isolation pool based on a predefined policy to free resources and prevent memory overflow.                                                                                           |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | Value range: 0.0-100.0%                                                                                                                                                                                                                                                                                                                                      |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | When **indices.breaker.total.use_real_memory** is enabled, this value must be lower than **indices.breaker.total.limit**. Otherwise, the native OpenSearch circuit breaker will always be triggered first. For details, see `Circuit breaker settings <https://docs.opensearch.org/latest/install-and-configure/configuring-opensearch/circuit-breaker/>`__. |
      |                                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                 |                 | If you anticipate traffic peaks or surges, you can lower this value to have the isolation pool's circuit breaker triggered earlier, thus preventing heap memory overload.                                                                                                                                                                                    |
      +-----------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Run the following command to set the query cancellation policy:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.strategy": "fair",
          "search.isolator.strategy.ratio": "0.5%"
        }
      }

   .. table:: **Table 4** Parameters for configuring a query cancellation policy

      +--------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Type            | Default Value   | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      +================================+=================+=================+==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | search.isolator.strategy       | String          | fair            | Policy for selecting which query to cancel when query isolation is triggered.                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                 |                 | -  fair (default): Determine which query to cancel by considering both memory usage and execution duration. If the difference between the memory usage of two candidate queries <= **maximum OpenSearch heap memory x fair policy threshold**, the query that has a longer execution duration will be cancelled; on the contrary, if the difference is greater than that, the more memory-intensive query will be cancelled instead. Maximum OpenSearch heap memory = **min(31, total node memory/2)** (GB). |
      |                                |                 |                 | -  mem-first: Cancels the query that has the highest memory usage.                                                                                                                                                                                                                                                                                                                                                                                                                                           |
      |                                |                 |                 | -  time-first: Cancels the query that has lasted the longest.                                                                                                                                                                                                                                                                                                                                                                                                                                                |
      |                                |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                 |                 | The large query isolation pool is checked every second until the heap memory is within the safe range.                                                                                                                                                                                                                                                                                                                                                                                                       |
      +--------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.strategy.ratio | String          | 1%              | Fair policy threshold, which is the ratio of the memory difference between two queries in the isolation pool to the maximum node heap memory.                                                                                                                                                                                                                                                                                                                                                                |
      |                                |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                 |                 | -  When the memory usage difference between large queries in the isolation pool is small, the system preferentially cancels the query with the longest execution duration.                                                                                                                                                                                                                                                                                                                                   |
      |                                |                 |                 | -  Otherwise, it cancels the query with the highest memory usage.                                                                                                                                                                                                                                                                                                                                                                                                                                            |
      |                                |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                 |                 | This parameter is valid only when **search.isolator.strategy** is set to **fair**.                                                                                                                                                                                                                                                                                                                                                                                                                           |
      |                                |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                 |                 | Value range: 0.0-100.0%                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
      |                                |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                 |                 | You are advised to use the default value. Adjust only if necessary and with caution.                                                                                                                                                                                                                                                                                                                                                                                                                         |
      +--------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Run the following command to set the maximum number of cancelled query records retained in the large query isolation log:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.log.count": "100"
        }
      }

   .. table:: **Table 5** Parameter description

      +---------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                 | Type            | Default Value   | Description                                                                                                                                                                                                                            |
      +===========================+=================+=================+========================================================================================================================================================================================================================================+
      | search.isolator.log.count | Integer         | 100             | The maximum number of cancelled query records retained in the large query isolation log.                                                                                                                                               |
      |                           |                 |                 |                                                                                                                                                                                                                                        |
      |                           |                 |                 | The large query isolation log records cancelled large queries for query performance analysis and optimization. Once this limit is exceeded, the system automatically deletes the oldest records to control the log's memory footprint. |
      |                           |                 |                 |                                                                                                                                                                                                                                        |
      |                           |                 |                 | Value range: 0-5000                                                                                                                                                                                                                    |
      |                           |                 |                 |                                                                                                                                                                                                                                        |
      |                           |                 |                 | Setting this value to **0** disables the large query isolation log.                                                                                                                                                                    |
      +---------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   You can use the following APIs to query log information about cancelled queries:

   -  Query statistics about cancelled queries on all nodes:

      .. code-block:: text

         GET /_isolator_metrics

   -  Query statistics about cancelled queries on a specified node:

      .. code-block:: text

         GET /_isolator_metrics/{nodeId}

   -  Query details about cancelled queries on all nodes:

      .. code-block:: text

         GET /_isolator_metrics?detailed

   -  Query details about cancelled queries on a specified node:

      .. code-block:: text

         GET /_isolator_metrics/{nodeId}?detailed

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
        "_nodes": {
          "total": 1,
          "successful": 1,
          "failed": 0
        },
        "cluster_name": "test",
        "nodes": {
          "CTqrZFXWTzmLonSZyNMKkQ": {
            "name": "test-ess-esn-1-1",
            "host": "172.16.101.116",
            "total_cancel": 0, //Total number of cancelled queries
            "isolator_cancel": 0, //Number of queries cancelled because isolation pool thresholds were exceeded
            "out_of_time_cancel": 0   //Number of queries cancelled due to timeout
          }
        }
      }

Configuring Global Query Timeout
--------------------------------

When a global query timeout is configured, queries that exceed the specified duration are automatically cancelled, and the message "cancel cause by global time limit" is returned. This prevents long-running queries from consuming excessive resources. Global query timeout is **disabled by default**. You can modify this setting when necessary. Any change takes effect immediately.

Run the following command to enable and configure a global query timeout:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "search.isolator.time.enabled": true,
       "search.isolator.time.limit": "110s"
     }
   }

.. table:: **Table 7** Parameters for setting the global query timeout

   +------------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                    | Type            | Default Value   | Description                                                                                                                                  |
   +==============================+=================+=================+==============================================================================================================================================+
   | search.isolator.time.enabled | Boolean         | false           | Whether to enable a global query timeout. When enabled, queries are automatically cancelled when they last longer than a predefined timeout. |
   |                              |                 |                 |                                                                                                                                              |
   |                              |                 |                 | The value can be:                                                                                                                            |
   |                              |                 |                 |                                                                                                                                              |
   |                              |                 |                 | -  true: Enable global query timeout.                                                                                                        |
   |                              |                 |                 | -  false: Disable global query timeout.                                                                                                      |
   +------------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | search.isolator.time.limit   | String          | 120s            | The value of the global query timeout.                                                                                                       |
   |                              |                 |                 |                                                                                                                                              |
   |                              |                 |                 | Value format: number + unit                                                                                                                  |
   |                              |                 |                 |                                                                                                                                              |
   |                              |                 |                 | -  Number: a natural number                                                                                                                  |
   |                              |                 |                 | -  Unit: nanos (nanosecond), micros (microsecond), ms (millisecond), s (second), m (minute), h (hour), or d (day)                            |
   |                              |                 |                 |                                                                                                                                              |
   |                              |                 |                 | Minimum value: 0 (to cancel all queries)                                                                                                     |
   +------------------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------+
