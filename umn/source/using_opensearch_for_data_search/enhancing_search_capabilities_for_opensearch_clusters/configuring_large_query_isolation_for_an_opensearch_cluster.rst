:original_name: css_01_0053.html

.. _css_01_0053:

Configuring Large Query Isolation for an OpenSearch Cluster
===========================================================

Large query isolation can be configured to manage queries that have high memory usage or take too long to complete. This helps improve the stability of OpenSearch clusters and prevent out-of-memory (OOM) exceptions.

As business grows, your OpenSearch clusters may face mounting query pressure. Some complex queries may occupy excessive node memory, triggering frequent garbage collection or even OOM exceptions, which may compromise cluster performance and stability. Large query isolation enables effective management of memory-intensive, time-consuming query requests, ensuring cluster stability. Large query isolation includes the following:

-  Isolating large queries: Manages memory-intensive/time-consuming queries separately to avoid impacting other queries.
-  Query cancelation based on a heap memory usage threshold: Cancels a large query in the isolation pool when the node heap memory usage reaches a predefined threshold.
-  Global query timeout: Automatically cancels tasks when they last longer than a predefined timeout. This timeout applies globally.

How the Feature Works
---------------------

-  Isolation pool management: Large queries are placed in an isolation pool, where they are managed separately from other normal queries. Tasks in the isolation pool may be canceled based on preset memory or duration thresholds.
-  Query cancelation policies:

   -  fair: Selects which query to cancel by considering both memory usage and query duration.
   -  mem-first: Cancels the query that has the highest memory usage.
   -  time-first: Cancels the query that has lasted the longest.

-  Native cancel API: OpenSearch's native cancel API can be used to cancel tasks, ensuring compatibility.

Constraints
-----------

-  Only OpenSearch 2.19.0 supports large query isolation.
-  Large query isolation is enabled by default, whereas global query timeout is disabled by default. If you enable them, the configuration will take effect immediately.

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

Large query isolation places large queries in an isolation pool, where they may be canceled based on preset memory or duration thresholds. Large query isolation is enabled by default. Any change takes effect immediately.

#. Run the following command to enable large query isolation:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.enabled": true
        }
      }

   .. table:: **Table 1** Enabling large query isolation

      +-------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------+
      | Parameter               | Type                  | Description                                                                                                            |
      +=========================+=======================+========================================================================================================================+
      | search.isolator.enabled | Boolean               | Whether to enable large query isolation. When enabled, large queries are managed separately from other normal queries. |
      |                         |                       |                                                                                                                        |
      |                         |                       | -  **true** (default): Enable large query isolation.                                                                   |
      |                         |                       | -  **false**: Disable large query isolation.                                                                           |
      +-------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------+

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

      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Type                  | Description                                                                                                                            |
      +===================================+=======================+========================================================================================================================================+
      | search.isolator.memory.task.limit | String                | Large query memory threshold: When a query requests more memory than specified by this threshold, it is placed into an isolation pool. |
      |                                   |                       |                                                                                                                                        |
      |                                   |                       | Value range: **0b** to the maximum heap memory of a node.                                                                              |
      |                                   |                       |                                                                                                                                        |
      |                                   |                       | Unit: MB, GB, or other units supported by OpenSearch.                                                                                  |
      |                                   |                       |                                                                                                                                        |
      |                                   |                       | The default value is **50 MB**.                                                                                                        |
      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.time.management   | String                | Large query duration threshold: When a query has lasted longer than specified by this threshold, it is placed into an isolation pool.  |
      |                                   |                       |                                                                                                                                        |
      |                                   |                       | Value range: >= **0ms**                                                                                                                |
      |                                   |                       |                                                                                                                                        |
      |                                   |                       | Unit: s (second), ms (millisecond), m (minute), or h (hour).                                                                           |
      |                                   |                       |                                                                                                                                        |
      |                                   |                       | The default value is **10s**.                                                                                                          |
      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------+

#. Configure the resource usage thresholds for triggering query cancelation.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.memory.pool.limit": "50%",
          "search.isolator.memory.heap.limit": "90%",
          "search.isolator.count.limit": 1000
        }
      }

   .. table:: **Table 3** Parameters for configuring query cancelation thresholds

      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Type                  | Description                                                                                                                                                                                                                                                                            |
      +===================================+=======================+========================================================================================================================================================================================================================================================================================+
      | search.isolator.memory.pool.limit | String                | Isolation pool memory usage threshold, which indicates the maximum node heap memory usage allowed. When the total memory requested by all large queries in the isolation pool exceeds this threshold, one of the large queries is automatically canceled based on a predefined policy. |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | Value range: 0.0-100.0%                                                                                                                                                                                                                                                                |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | The default value is **50**.                                                                                                                                                                                                                                                           |
      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.memory.heap.limit | String                | Heap memory usage threshold, which indicates the actual node heap memory usage, contributed by both writes and queries. When the node heap memory usage exceeds this threshold, one of the large queries is automatically canceled based on a predefined policy.                       |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | Value range: 0.0-100.0%                                                                                                                                                                                                                                                                |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | The default value is 90%.                                                                                                                                                                                                                                                              |
      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.count.limit       | Integer               | The maximum number of queries in the isolation pool. When this threshold is reached, query cancelation is triggered, and no new queries will be accepted.                                                                                                                              |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | Value range: **10**\ ``-``\ **50000**                                                                                                                                                                                                                                                  |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | The default value is **1000**.                                                                                                                                                                                                                                                         |
      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      In addition to **search.isolator.memory.pool.limit** and **search.isolator.count.limit**, you can configure **search.isolator.memory.task.limit** and **search.isolator.time.management** to control the number of query tasks that enter the isolation pool.

#. Configure a policy for selecting queries to cancel in the isolation pool.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.strategy": "fair",
          "search.isolator.strategy.ratio": "0.5%"
        }
      }

   .. table:: **Table 4** Parameters for configuring a query cancelation policy

      +--------------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Type                  | Description                                                                                                                                                                                                                                                                                                                                                                  |
      +================================+=======================+==============================================================================================================================================================================================================================================================================================================================================================================+
      | search.isolator.strategy       | String                | Policy for selecting which query to cancel when query isolation is triggered.                                                                                                                                                                                                                                                                                                |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                       | -  fair (default): Selects which query to cancel by considering both memory usage and query duration. If the difference between the memory used by two queries <= **maximum node heap memory x fair policy threshold**, the query that has lasted the longest is canceled; on the contrary, if it is greater than that, the most memory-intensive query is canceled instead. |
      |                                |                       | -  mem-first: Cancels the query that has the highest memory usage.                                                                                                                                                                                                                                                                                                           |
      |                                |                       | -  time-first: Cancels the query that has lasted the longest.                                                                                                                                                                                                                                                                                                                |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                       | The large query isolation pool is checked every second until the heap memory is within the safe range.                                                                                                                                                                                                                                                                       |
      +--------------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.strategy.ratio | String                | Fair policy threshold, which is the ratio of the memory difference between two queries in the isolation pool to the maximum node heap memory. If this threshold is not reached, the query that has lasted the longest will be canceled. Otherwise, the query that occupies the most memory will be canceled.                                                                 |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                       | This parameter is valid only when **search.isolator.strategy** is set to **fair**.                                                                                                                                                                                                                                                                                           |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                       | Value range: 0.0-100.0%                                                                                                                                                                                                                                                                                                                                                      |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                              |
      |                                |                       | The default value is **1**.                                                                                                                                                                                                                                                                                                                                                  |
      +--------------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Configuring Global Query Timeout
--------------------------------

A global query timeout, as the name indicates, applies to all queries. Global query timeout is disabled by default. Any change takes effect immediately.

Run the following command to enable and configure a global query timeout:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "search.isolator.time.enabled": true,
       "search.isolator.time.limit": "110s"
     }
   }

.. table:: **Table 5** Parameter description

   +------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                    | Type                  | Description                                                                                                                                 |
   +==============================+=======================+=============================================================================================================================================+
   | search.isolator.time.enabled | Boolean               | Whether to enable a global query timeout. When enabled, queries are automatically canceled when they last longer than a predefined timeout. |
   |                              |                       |                                                                                                                                             |
   |                              |                       | -  true: Enable global query timeout.                                                                                                       |
   |                              |                       | -  false (default): Disable global query timeout.                                                                                           |
   +------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
   | search.isolator.time.limit   | String                | The value of the global query timeout.                                                                                                      |
   |                              |                       |                                                                                                                                             |
   |                              |                       | Value range: >= 0 ms                                                                                                                        |
   |                              |                       |                                                                                                                                             |
   |                              |                       | The default value is 120s.                                                                                                                  |
   +------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Configuring the Maximum Number of Log Records Retained for Query Cancelation
----------------------------------------------------------------------------

Run the following command to set the maximum number of log records retained for canceled queries:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "search.isolator.log.count": "100"
     }
   }

+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter                 | Data Type             | Description                                                                                                                                                                                                  |
+===========================+=======================+==============================================================================================================================================================================================================+
| search.isolator.log.count | Integer               | Maximum number of log records retained for canceled queries. Canceled query requests are recorded in the memory for the purpose of analyzing and optimizing large queries. Excess records will be discarded. |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | This parameter is valid only when **search.isolator.enabled** is set to **true**.                                                                                                                            |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | Value range: 0-5000                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | The default value is **100**.                                                                                                                                                                                |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | You can use the following API to check query cancelation logs:                                                                                                                                               |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | -  Query all nodes:                                                                                                                                                                                          |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |    .. code:: text                                                                                                                                                                                            |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |       GET /_isolator_metrics                                                                                                                                                                                 |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | -  Query a single node:                                                                                                                                                                                      |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |    .. code:: text                                                                                                                                                                                            |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |       GET /_isolator_metrics/{nodeId}                                                                                                                                                                        |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | -  Query details about canceled queries on all nodes:                                                                                                                                                        |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |    .. code:: text                                                                                                                                                                                            |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |       GET /_isolator_metrics?detailed                                                                                                                                                                        |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | -  Query details about canceled queries on a single node:                                                                                                                                                    |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |    .. code:: text                                                                                                                                                                                            |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |       GET /_isolator_metrics/{nodeId}?detailed                                                                                                                                                               |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | In the commands above, **nodeId** indicates the node ID. Example response:                                                                                                                                   |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       | .. code-block::                                                                                                                                                                                              |
|                           |                       |                                                                                                                                                                                                              |
|                           |                       |    {                                                                                                                                                                                                         |
|                           |                       |      "_nodes": {                                                                                                                                                                                             |
|                           |                       |        "total": 1,                                                                                                                                                                                           |
|                           |                       |        "successful": 1,                                                                                                                                                                                      |
|                           |                       |        "failed": 0                                                                                                                                                                                           |
|                           |                       |      },                                                                                                                                                                                                      |
|                           |                       |      "cluster_name": "test",                                                                                                                                                                                 |
|                           |                       |      "nodes": {                                                                                                                                                                                              |
|                           |                       |        "CTqrZFXWTzmLonSZyNMKkQ": {                                                                                                                                                                           |
|                           |                       |          "name": "test-ess-esn-1-1",                                                                                                                                                                         |
|                           |                       |          "host": "172.16.101.116",                                                                                                                                                                           |
|                           |                       |          "total_cancel": 0, //Total number of canceled queries                                                                                                                                               |
|                           |                       |          "isolator_cancel": 0, //Number of queries canceled because isolation pool thresholds were exceeded                                                                                                  |
|                           |                       |          "out_of_time_cancel": 0   //Number of queries canceled due to timeout                                                                                                                               |
|                           |                       |        }                                                                                                                                                                                                     |
|                           |                       |      }                                                                                                                                                                                                       |
|                           |                       |    }                                                                                                                                                                                                         |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
