:original_name: css_01_0133.html

.. _css_01_0133:

Procedure
=========

The large query isolation and global timeout features are disabled by default. If you enable them, the configuration will take effect immediately. Perform the following steps to configure the features:

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. In the navigation pane of Kibana on the left, choose **Dev Tools**. Run the following command to enable large query isolation and global timeout features:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "search.isolator.enabled": true,
          "search.isolator.time.enabled": true
        }
      }

   The two features each has an independent switch and the following parameters.

   .. table:: **Table 1** Parameters for large query isolation and global timeout duration

      +------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Switch                       | Parameter                         | Description                                                                                                                                                                                                                    |
      +==============================+===================================+================================================================================================================================================================================================================================+
      | search.isolator.enabled      | search.isolator.memory.task.limit | Thresholds of a shard query task. A query task exceeding one of these thresholds is regarded as a large query task.                                                                                                            |
      |                              |                                   |                                                                                                                                                                                                                                |
      |                              | search.isolator.time.management   |                                                                                                                                                                                                                                |
      +------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                              | search.isolator.memory.pool.limit | Resource usage thresholds in the isolation pool. If the resource usage of a query task exceeds one of these thresholds, the task will be intercepted.                                                                          |
      |                              |                                   |                                                                                                                                                                                                                                |
      |                              | search.isolator.memory.heap.limit | .. note::                                                                                                                                                                                                                      |
      |                              |                                   |                                                                                                                                                                                                                                |
      |                              | search.isolator.count.limit       |    **search.isolator.memory.heap.limit** defines the limit on the heap memory consumed by write, query, and other operations of a node. If the limit is exceeded, large query tasks in the isolation pool will be interrupted. |
      +------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                              | search.isolator.strategy          | Policy for selecting a query task in the isolation pool.                                                                                                                                                                       |
      |                              |                                   |                                                                                                                                                                                                                                |
      |                              | search.isolator.strategy.ratio    |                                                                                                                                                                                                                                |
      +------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | search.isolator.time.enabled | search.isolator.time.limit        | Global timeout interval of query tasks.                                                                                                                                                                                        |
      +------------------------------+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Configure the large query isolation and global timeout duration separately.

   -  Configure the thresholds of a shard query task. A query task exceeding one of these thresholds is regarded as a large query task.

      .. code-block:: text

         PUT _cluster/settings
         {
           "persistent": {
             "search.isolator.memory.task.limit": "50MB",
             "search.isolator.time.management": "10s"
           }
         }

      .. table:: **Table 2** Parameter description

         +-----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Data Type             | Description                                                                                                                                                                          |
         +===================================+=======================+======================================================================================================================================================================================+
         | search.isolator.memory.task.limit | String                | Threshold of the memory requested by a query task to perform aggregation or other operations. If the requested memory exceeds the threshold, the task will be isolated and observed. |
         |                                   |                       |                                                                                                                                                                                      |
         |                                   |                       | Value range: **0b** to the maximum heap memory of a node                                                                                                                             |
         |                                   |                       |                                                                                                                                                                                      |
         |                                   |                       | Default value: **50MB**                                                                                                                                                              |
         |                                   |                       |                                                                                                                                                                                      |
         |                                   |                       | .. note::                                                                                                                                                                            |
         |                                   |                       |                                                                                                                                                                                      |
         |                                   |                       |    You can run the following command to query the current heap memory and the maximum heap memory of a cluster:                                                                      |
         |                                   |                       |                                                                                                                                                                                      |
         |                                   |                       |    **GET \_cat/nodes?&h=id,ip,port,r,ramPercent,ramCurrent,heapMax,heapCurrent**                                                                                                     |
         +-----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | search.isolator.time.management   | String                | Threshold of the duration of a query. (started when cluster resources are used for query). If the duration of a query exceeds the threshold, it will be isolated and observed.       |
         |                                   |                       |                                                                                                                                                                                      |
         |                                   |                       | Value range: >= **0ms**                                                                                                                                                              |
         |                                   |                       |                                                                                                                                                                                      |
         |                                   |                       | Default value: **10s**                                                                                                                                                               |
         +-----------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   -  Configure the resource usage thresholds in the isolation pool. If the resource usage of a query task exceeds one of these thresholds, the task will be intercepted.

      .. code-block:: text

         PUT _cluster/settings
         {
           "persistent": {
             "search.isolator.memory.pool.limit": "50%",
             "search.isolator.memory.heap.limit": "90%",
             "search.isolator.count.limit": 1000
           }
         }

      .. table:: **Table 3** Parameter description

         +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Data Type             | Description                                                                                                                                                                                                                                                                            |
         +===================================+=======================+========================================================================================================================================================================================================================================================================================+
         | search.isolator.memory.pool.limit | String                | Threshold of the heap memory percentage of the current node. If the total memory requested by large query tasks in the isolation pool exceeds the threshold, the interrupt control program will be triggered to cancel one of the tasks.                                               |
         |                                   |                       |                                                                                                                                                                                                                                                                                        |
         |                                   |                       | Value range: **0.0** to **100.0%**                                                                                                                                                                                                                                                     |
         |                                   |                       |                                                                                                                                                                                                                                                                                        |
         |                                   |                       | Default value: **50%**                                                                                                                                                                                                                                                                 |
         +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | search.isolator.memory.heap.limit | String                | Heap memory threshold of the current node. If the heap memory of the node exceeds the threshold, the interrupt control program will be triggered to cancel a large query task in the isolation pool.                                                                                   |
         |                                   |                       |                                                                                                                                                                                                                                                                                        |
         |                                   |                       | Value range: **0.0** to **100.0%**                                                                                                                                                                                                                                                     |
         |                                   |                       |                                                                                                                                                                                                                                                                                        |
         |                                   |                       | Default value: **90%**                                                                                                                                                                                                                                                                 |
         +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | search.isolator.count.limit       | Integer               | Threshold of the number of large query tasks in the current node isolation pool. If the number of observed query tasks exceeds the threshold, the interrupt control program will be triggered to stop accepting new large queries. New large query requests will be directly canceled. |
         |                                   |                       |                                                                                                                                                                                                                                                                                        |
         |                                   |                       | Value range: **10**\ ``-``\ **50000**                                                                                                                                                                                                                                                  |
         |                                   |                       |                                                                                                                                                                                                                                                                                        |
         |                                   |                       | Default value: **1000**                                                                                                                                                                                                                                                                |
         +-----------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

      .. note::

         In addition to **search.isolator.memory.pool.limit** and **search.isolator.count.limit** parameters, you can configure **search.isolator.memory.task.limit** and **search.isolator.time.management** to control the number of query tasks that enter the isolation pool.

   -  Policy for selecting a query task in the isolation pool.

      .. code-block:: text

         PUT _cluster/settings
         {
           "persistent": {
             "search.isolator.strategy": "fair",
             "search.isolator.strategy.ratio": "0.5%"
           }
         }

      +--------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Data Type             | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
      +================================+=======================+===============================================================================================================================================================================================================================================================================================================================================================================================================================+
      | search.isolator.strategy       | String                | Policy for selecting large queries when the interrupt control program is triggered. The selected query will be interrupted.                                                                                                                                                                                                                                                                                                   |
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
      |                                |                       | Value range: **0.0** to **100.0%**                                                                                                                                                                                                                                                                                                                                                                                            |
      |                                |                       |                                                                                                                                                                                                                                                                                                                                                                                                                               |
      |                                |                       | Default value: **1%**                                                                                                                                                                                                                                                                                                                                                                                                         |
      +--------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   -  Configure the global timeout duration of query tasks.

      .. code-block:: text

         PUT _cluster/settings
         {
           "persistent": {
             "search.isolator.time.limit": "120s"
           }
         }

      +----------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                  | Data Type             | Description                                                                                                                          |
      +============================+=======================+======================================================================================================================================+
      | search.isolator.time.limit | String                | Global query timeout duration. If this function is enabled, all the query tasks that exceed the specified duration will be canceled. |
      |                            |                       |                                                                                                                                      |
      |                            |                       | Value range: >= **0ms**                                                                                                              |
      |                            |                       |                                                                                                                                      |
      |                            |                       | Default value: **120s**                                                                                                              |
      +----------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------+
