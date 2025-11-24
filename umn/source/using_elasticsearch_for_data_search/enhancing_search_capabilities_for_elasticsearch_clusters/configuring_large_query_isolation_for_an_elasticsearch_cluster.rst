:original_name: css_01_0132.html

.. _css_01_0132:

Configuring Large Query Isolation for an Elasticsearch Cluster
==============================================================

Scenario
--------

You can isolate query requests that consume a large amount of memory or take a long period of time. This way, you ensure service availability for other requests. If the heap memory usage of a node is too high, an interrupt control program will be triggered to terminate a large query based on the policies you configured. You can also configure a global query timeout duration. Long queries will be intercepted by an Elasticsearch-native cancel API.

Large query isolation can effectively solve the following problems and improve the search performance of clusters:

-  A small number of queries occupy large chunks of node heap memory, resulting in frequent Garbage Collection (GC) and even out of memory (OOM) exceptions.
-  Frequent GC causes node disconnections. As a result, queries cannot get response and may fail.
-  The CPU usage is high due to heavy query load, affecting online services.

Constraints
-----------

Only Elasticsearch 7.6.2 and Elasticsearch 7.10.2 clusters support large query isolation.

Logging In to Kibana
--------------------

Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

Enabling Large Query Isolation
------------------------------

Large query isolation is enabled by default, while global query timeout is disabled by default. If you enable them, the configuration will take effect immediately.

Run the following commands to enable large query isolation and global query timeout:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "search.isolator.enabled": true,
       "search.isolator.time.enabled": true
     }
   }

The two features each has an independent switch. :ref:`Table 1 <en-us_topic_0000001938377744__table289124893815>` describes their parameters.

.. _en-us_topic_0000001938377744__table289124893815:

.. table:: **Table 1** Parameters for configuring large query isolation and global query timeout

   +------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Switch                       | Parameter                         | Description                                                                                                                                                                                                                |
   +==============================+===================================+============================================================================================================================================================================================================================+
   | search.isolator.enabled      | search.isolator.memory.task.limit | Thresholds for identifying a single shard query task as a large query.                                                                                                                                                     |
   |                              |                                   |                                                                                                                                                                                                                            |
   |                              | search.isolator.time.management   |                                                                                                                                                                                                                            |
   +------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                              | search.isolator.memory.pool.limit | Resource usage thresholds for isolation. If the resource usage of a query task exceeds one of these thresholds, the task will be paused.                                                                                   |
   |                              |                                   |                                                                                                                                                                                                                            |
   |                              | search.isolator.memory.heap.limit | .. note::                                                                                                                                                                                                                  |
   |                              |                                   |                                                                                                                                                                                                                            |
   |                              | search.isolator.count.limit       |    **search.isolator.memory.heap.limit** defines the limit on the heap memory consumed by write, query, and other operations of a node. If this limit is exceeded, large query tasks in the isolation pool will be paused. |
   +------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   |                              | search.isolator.strategy          | Policy for selecting query tasks to pause in the isolation pool.                                                                                                                                                           |
   |                              |                                   |                                                                                                                                                                                                                            |
   |                              | search.isolator.strategy.ratio    |                                                                                                                                                                                                                            |
   +------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | search.isolator.time.enabled | search.isolator.time.limit        | Global timeout for query tasks.                                                                                                                                                                                            |
   +------------------------------+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Configuring Large Query Isolation Thresholds
--------------------------------------------

-  Run the following commands to configure thresholds for defining a large query task:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.memory.task.limit": "50MB",
          "search.isolator.time.management": "10s"
        }
      }

   .. table:: **Table 2** Parameters for configuring large query isolation thresholds

      +-----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Type                  | Description                                                                                                                                                                          |
      +===================================+=======================+======================================================================================================================================================================================+
      | search.isolator.memory.task.limit | String                | Threshold of the memory requested by a query task to perform aggregation or other operations. If the requested memory exceeds the threshold, the task will be isolated and observed. |
      |                                   |                       |                                                                                                                                                                                      |
      |                                   |                       | -  Value range: **0b** to the maximum heap memory of a node                                                                                                                          |
      |                                   |                       | -  Default value: **50MB**                                                                                                                                                           |
      +-----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.time.management   | String                | Threshold of the duration of a query (started when cluster resources are used for query). If the duration of a query exceeds the threshold, it will be isolated and observed.        |
      |                                   |                       |                                                                                                                                                                                      |
      |                                   |                       | -  Value range: >= **0ms**                                                                                                                                                           |
      |                                   |                       | -  Default value: **10s**                                                                                                                                                            |
      +-----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  Configure the resource usage thresholds for triggering the isolation of query tasks.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.memory.pool.limit": "50%",
          "search.isolator.memory.heap.limit": "90%",
          "search.isolator.count.limit": 1000
        }
      }

   .. table:: **Table 3** Parameters for configuring isolation pool thresholds

      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Type                  | Description                                                                                                                                                                                                                                                                            |
      +===================================+=======================+========================================================================================================================================================================================================================================================================================+
      | search.isolator.memory.pool.limit | String                | Threshold of the heap memory percentage of the current node. If the total memory requested by large query tasks in the isolation pool exceeds the threshold, the interrupt control program will be triggered to cancel one of the tasks.                                               |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | -  Value range: **0.0** to **100.0%**                                                                                                                                                                                                                                                  |
      |                                   |                       | -  Default value: **50%**                                                                                                                                                                                                                                                              |
      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.memory.heap.limit | String                | Heap memory threshold of the current node. If the heap memory of the node exceeds the threshold, the interrupt control program will be triggered to cancel a large query task in the isolation pool.                                                                                   |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | -  Value range: **0.0** to **100.0%**                                                                                                                                                                                                                                                  |
      |                                   |                       | -  Default value: **90%**                                                                                                                                                                                                                                                              |
      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.count.limit       | Integer               | Threshold of the number of large query tasks in the current node isolation pool. If the number of observed query tasks exceeds the threshold, the interrupt control program will be triggered to stop accepting new large queries. New large query requests will be directly canceled. |
      |                                   |                       |                                                                                                                                                                                                                                                                                        |
      |                                   |                       | -  Value range: **10**\ ``-``\ **50000**                                                                                                                                                                                                                                               |
      |                                   |                       | -  Default value: **1000**                                                                                                                                                                                                                                                             |
      +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      In addition to **search.isolator.memory.pool.limit** and **search.isolator.count.limit** parameters, you can configure **search.isolator.memory.task.limit** and **search.isolator.time.management** to control the number of query tasks that enter the isolation pool.

-  Configure a policy for selecting query tasks to pause in the isolation pool.

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.strategy": "fair",
          "search.isolator.strategy.ratio": "0.5%"
        }
      }

   .. table:: **Table 4** Parameters for configuring a query cancelation policy

      +--------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Type                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
      +================================+=======================+===============================================================================================================================================================================================================================================================================================================================================================================================================================+
      | search.isolator.strategy       | String                | Policy for selecting large queries when the interrupt control program is triggered. The selected queries will be interrupted.                                                                                                                                                                                                                                                                                                 |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                |                       | .. note::                                                                                                                                                                                                                                                                                                                                                                                                                     |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                |                       |    The large query isolation pool is checked every second until the heap memory is within the safe range.                                                                                                                                                                                                                                                                                                                     |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                |                       | Values: **fair**, **mem-first**, or **time-first**                                                                                                                                                                                                                                                                                                                                                                            |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                |                       | -  **mem-first**: The query task that uses the most heap memory in the isolation pool is interrupted.                                                                                                                                                                                                                                                                                                                         |
      |                                |                       | -  **time-first**: The query task that has been running for the longest time in the isolation pool is interrupted.                                                                                                                                                                                                                                                                                                            |
      |                                |                       | -  **fair**: If the difference between the heap memory of shard queries is smaller than *Maximum_heap_memory* x **search.isolator.strategy.ratio**, the query that takes the longest time should be interrupted. Otherwise, the query that uses the most heap memory is interrupted.                                                                                                                                          |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                |                       | Default value: **fair**                                                                                                                                                                                                                                                                                                                                                                                                       |
      +--------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.strategy.ratio | String                | Threshold of the **fair** policy. This parameter takes effect only if **search.isolator.strategy** is set to **fair**. If the difference between the memory usage of large query tasks does not exceed the threshold, the query that takes the longest time should be interrupted. If the difference between the memory usage of large query tasks exceeds the threshold, the query that uses the most memory is interrupted. |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                |                       | -  Value range: **0.0** to **100.0%**                                                                                                                                                                                                                                                                                                                                                                                         |
      |                                |                       | -  Default value: **1%**                                                                                                                                                                                                                                                                                                                                                                                                      |
      +--------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Configuring the Global Query Timeout
------------------------------------

Run the following command to set the global timeout of query tasks:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "search.isolator.time.limit": "120s"
     }
   }

.. table:: **Table 5** Description

   +----------------------------+-----------------------+--------------------------------------------------------------------------------------------+
   | Parameter                  | Type                  | Description                                                                                |
   +============================+=======================+============================================================================================+
   | search.isolator.time.limit | String                | Global query timeout duration. Any query task that exceeds this duration will be canceled. |
   |                            |                       |                                                                                            |
   |                            |                       | -  Value range: >= **0ms**                                                                 |
   |                            |                       | -  Default value: **120s**                                                                 |
   +----------------------------+-----------------------+--------------------------------------------------------------------------------------------+

Configuring the Maximum Number of Log Records for Canceled Query Requests
-------------------------------------------------------------------------

Run the following command to set the maximum number of log records kept for canceled query requests:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "search.isolator.log.count": "100"
     }
   }

+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------+
| Parameter                 | Data Type             | Description                                                                                            |
+===========================+=======================+========================================================================================================+
| search.isolator.log.count | Integer               | Maximum number of records of canceled query requests that can be recorded in the memory.               |
|                           |                       |                                                                                                        |
|                           |                       | -  Value range: 0-5000                                                                                 |
|                           |                       | -  Default value: **100**                                                                              |
|                           |                       |                                                                                                        |
|                           |                       | .. note::                                                                                              |
|                           |                       |                                                                                                        |
|                           |                       |    You can use the following APIs to query canceled requests:                                          |
|                           |                       |                                                                                                        |
|                           |                       |    -  GET /_isolator_metrics: Queries all nodes.                                                       |
|                           |                       |    -  GET /_isolator_metrics/{nodeId}: Queries a single node.                                          |
|                           |                       |    -  GET /_isolator_metrics? detailed: Queries request cancellation details of all nodes.             |
|                           |                       |    -  GET /_isolator_metrics/{nodeId}?detailed: Queries request cancellation details of a single node. |
|                           |                       |                                                                                                        |
|                           |                       |    In the commands above, **nodeId** indicates the node ID.                                            |
+---------------------------+-----------------------+--------------------------------------------------------------------------------------------------------+
