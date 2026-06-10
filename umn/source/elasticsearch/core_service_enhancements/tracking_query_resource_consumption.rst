:original_name: css_01_0137.html

.. _css_01_0137:

Tracking Query Resource Consumption
===================================

During routine maintenance, O&M engineers may need to identify and analyze top (resource-consuming) queries that are causing high resource consumption or performance issues in Elasticsearch clusters. Typically, this requires calling Elasticsearch APIs to retrieve a list of ongoing tasks and examining hot threads to determine which queries are causing excessive resource usage, such as high CPU consumption. The process can be complex and time-consuming. To improve O&M efficiency, CSS provides a query resource tracker. With this feature, O&M personnel can call an API to obtain top queries with the highest latency, CPU usage, or memory consumption, filter the queries by time range, and quickly identify problematic queries. This can significantly improve troubleshooting efficiency and accuracy.

How the Feature Works
---------------------

The query resource tracker helps identify and optimize top resource-consuming queries, improving system performance and resource utilization. It is a useful tool in big data analytics and log processing scenarios.


.. figure:: /_static/images/en-us_image_0000002522213993.png
   :alt: **Figure 1** How the query resource tracker works

   **Figure 1** How the query resource tracker works

During query execution, the system records the resource consumption of each sub-phase (such as Query, Fetch, and Scroll), tracking metrics like CPU time and memory usage. The data is aggregated by a fixed time window (for example, 5 minutes). Queries with the highest resource consumption are recorded in a dedicated top queries index for analysis. A new top queries index is created daily to store these query resource statistics. The naming format is top-queries-xxx (where xxx indicates the date).

The top queries are ranked by the metric you specify, which can be CPU usage, memory usage, or latency. By default, the system ranks queries by latency.

Constraints
-----------

-  The query resource tracker adds memory cache fields, which may impact cluster performance.
-  The query resource tracker is supported only when the Elasticsearch cluster version is 7.10.2 and the image version is 7.10.2_25.9.0_xxx or later. It is **enabled by default** for clusters that meet these version requirements.

Modifying Top Queries Monitoring Settings
-----------------------------------------

Run the following command to modify the top queries monitoring settings as needed:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "search.insights.top_queries.cpu.enabled": true,
       "search.insights.top_queries.cpu.window_size": "10m",
       "search.insights.top_queries.cpu.top_n_size": 20,
       "search.insights.top_queries.exporter.delete_after_days": 8,
       "search.insights.top_queries.group_by": "none"
     }
   }

.. table:: **Table 1** Parameter description

   +------------------------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                                                  | Type            | Default Value   | Description                                                                                                                          |
   +============================================================+=================+=================+======================================================================================================================================+
   | search.insights.top_queries.<metric>.enabled               | Boolean         | true            | Whether to enable top query monitoring by the specified metric.                                                                      |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | Supported metrics: **latency**, **cpu** (CPU usage), or **memory** (memory usage).                                                   |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | The value can be:                                                                                                                    |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | -  **true**: Enable top query monitoring.                                                                                            |
   |                                                            |                 |                 | -  **false**: Disable top query monitoring.                                                                                          |
   +------------------------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | search.insights.top_queries.<metric>.window_size           | String          | 5m              | The size of the observation window. Monitoring data is aggregated and computed by a fixed window (for example, 5 minutes).           |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | Supported metrics: **latency**, **cpu** (CPU usage), or **memory** (memory usage).                                                   |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | Value range: 1m (1 minute), 5m (5 minutes), 10m (10 minutes), 30m (30 minutes), or *x*\ h (*x* hours, where *x* ranges from 1 to 24) |
   +------------------------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | search.insights.top_queries.<metric>.top_n_size            | Integer         | 10              | Number of top N queries monitored in each time window.                                                                               |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | For example, if this parameter is set to 20, only the top 20 queries are monitored in each time window.                              |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | Supported metrics: **latency**, **cpu** (CPU usage), or **memory** (memory usage).                                                   |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | Value range: 1 to 100                                                                                                                |
   +------------------------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | search.insights.top_queries.exporter.delete_after_days     | Integer         | 7               | Retention period of the top-queries-*xxx* index.                                                                                     |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | For example, if this parameter is set to 8, the index is retained for eight days.                                                    |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | Value range: 1 to 180                                                                                                                |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | Unit: days                                                                                                                           |
   +------------------------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | search.insights.top_queries.group_by                       | String          | none            | Whether to enable top query grouping.                                                                                                |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | The value can be:                                                                                                                    |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | -  **none**: No grouping.                                                                                                            |
   |                                                            |                 |                 | -  **similarity**: Group queries by feature similarity. Within each time window, only the first query is displayed for each group.   |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | For more information, see :ref:`Introduction to Query Grouping <en-us_topic_0000002485888678__section1754833345417>`.                |
   +------------------------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | search.insights.top_queries.grouping.attributes.field_name | Boolean         | true            | Whether to use query field names for query grouping.                                                                                 |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | This item takes effect only when **search.insights.top_queries.group_by** is set to **similarity**.                                  |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | The value can be:                                                                                                                    |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | -  **true**: Group queries by field name.                                                                                            |
   |                                                            |                 |                 | -  **false**: Ignore query field names.                                                                                              |
   +------------------------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | search.insights.top_queries.grouping.attributes.field_type | Boolean         | true            | Whether to use query field types for query grouping.                                                                                 |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | This item takes effect only when **search.insights.top_queries.group_by** is set to **similarity**.                                  |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | The value can be:                                                                                                                    |
   |                                                            |                 |                 |                                                                                                                                      |
   |                                                            |                 |                 | -  **true**: Group queries by field type.                                                                                            |
   |                                                            |                 |                 | -  **false**: Ignore query field types.                                                                                              |
   +------------------------------------------------------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Obtaining Top Queries
---------------------

The following is an example of the command that you can run to obtain top queries by a specified metric and time range:

.. code-block:: text

   GET _insights/top_queries?type=cpu&from=2025-12-02T00:00:00.000Z&to=2025-12-02T17:00:00.000Z

.. table:: **Table 2** Request parameters

   +-----------------+-----------------+---------------------------------------------------------+------------------------------------------------------------------------------+
   | Parameter       | Type            | Default Value                                           | Description                                                                  |
   +=================+=================+=========================================================+==============================================================================+
   | type            | String          | latency                                                 | The metric by which top queries are identified.                              |
   |                 |                 |                                                         |                                                                              |
   |                 |                 |                                                         | Value range: **latency**, **cpu** (CPU usage), or **memory** (memory usage). |
   +-----------------+-----------------+---------------------------------------------------------+------------------------------------------------------------------------------+
   | from            | String          | Null (obtain the top N queries in the last two windows) | Start time of the query time range.                                          |
   |                 |                 |                                                         |                                                                              |
   |                 |                 |                                                         | **from** and **to** must both be configured.                                 |
   |                 |                 |                                                         |                                                                              |
   |                 |                 |                                                         | Value format: YYYY-MM-DDTHH:mm:ss.SSSZ (timestamp in ISO 8601 format)        |
   +-----------------+-----------------+---------------------------------------------------------+------------------------------------------------------------------------------+
   | to              | String          | Null (obtain the top N queries in the last two windows) | End time of the query time range.                                            |
   |                 |                 |                                                         |                                                                              |
   |                 |                 |                                                         | **from** and **to** must both be configured.                                 |
   |                 |                 |                                                         |                                                                              |
   |                 |                 |                                                         | Value format: YYYY-MM-DDTHH:mm:ss.SSSZ (timestamp in ISO 8601 format)        |
   +-----------------+-----------------+---------------------------------------------------------+------------------------------------------------------------------------------+

Example response:

.. code-block::

   {
     "top_queries": [
       {
         "timestamp": 1764662136273,                            //Timestamp of the query.
         "date": "2025-12-02 07:55:36Z",                        //Time when the query was executed.
         "id": "4a5b4b1e-b502-4621-a5c1-09b8d9a1b81c",          //Unique ID of the query.
         "task_resource_usages": [
           {
             "action": "indices:data/read/search[phase/query]", // CPU and memory consumption of the query phase on node FB2ixw4IQCuXzCR83GT5Yg
             "taskId": 1877927,
             "parentTaskId": 111295,
             "nodeId": "FB2ixw4IQCuXzCR83GT5Yg",
             "taskResourceUsage": {
               "cpu_time_in_nanos": 3017078,
               "memory_in_bytes": 102360
             }
           },
           {
             "action": "indices:data/read/search[phase/query]", // CPU and memory consumption of the query phase on node FB2ixw4IQCuXzCR83GT5Yg
             "taskId": 1877926,
             "parentTaskId": 111295,
             "nodeId": "FB2ixw4IQCuXzCR83GT5Yg",
             "taskResourceUsage": {
               "cpu_time_in_nanos": 5618940,
               "memory_in_bytes": 271680
             }
           },
           {
             "action": "indices:data/read/search[phase/query]", // CPU and memory consumption of the query phase on node 2ICOHICoSS26YeQu5PIrlg
             "taskId": 107710,
             "parentTaskId": 111295,
             "nodeId": "2ICOHICoSS26YeQu5PIrlg",
             "taskResourceUsage": {
               "cpu_time_in_nanos": 8703914,
               "memory_in_bytes": 501560
             }
           },
           {
             "action": "indices:data/read/search[phase/fetch/id]", // CPU and memory consumption of the fetch phase on node FB2ixw4IQCuXzCR83GT5Yg
             "taskId": 1877928,
             "parentTaskId": 111295,
             "nodeId": "FB2ixw4IQCuXzCR83GT5Yg",
             "taskResourceUsage": {
               "cpu_time_in_nanos": 424055,
               "memory_in_bytes": 59000
             }
           },
           {
             "action": "indices:data/read/search[phase/fetch/id]", // CPU and memory consumption of the fetch phase on node 2ICOHICoSS26YeQu5PIrlg
             "taskId": 107711,
             "parentTaskId": 111295,
             "nodeId": "2ICOHICoSS26YeQu5PIrlg",
             "taskResourceUsage": {
               "cpu_time_in_nanos": 1279677,
               "memory_in_bytes": 337504
             }
           },
           {
             "action": "indices:data/read/search",                // CPU and memory consumption on the access node gzsjh_47SjCe6QFs9pKjEg during the query start phase
             "taskId": 111295,
             "parentTaskId": -1,
             "nodeId": "gzsjh_47SjCe6QFs9pKjEg",
             "taskResourceUsage": {
               "cpu_time_in_nanos": 297268,
               "memory_in_bytes": 8632
             }
           }
         ],
         "source": {                                              //Specific query statement
           "query": {
             "match": {
               "message": {
                 "query": "http",
                 "operator": "OR",
                 "prefix_length": 0,
                 "max_expansions": 50,
                 "fuzzy_transpositions": true,
                 "lenient": false,
                 "zero_terms_query": "NONE",
                 "auto_generate_synonyms_phrase_query": true,
                 "boost": 1
               }
             }
           }
         },
         "indices": [                                           //Queried index
           "log1"
         ],
         "total_shards": 3,                                     //Total number of shards queried
         "phase_latency_map": {                                 //Time consumed during each phase
           "expand": 0,                                         //Time consumed in the expand phase
           "query": 16,                                         //Time consumed in the query phase
           "fetch": 3                                          //Time consumed in the fetch phase
         },
         "labels": {},
         "group_by": "NONE",                                    //Query grouping type
         "node_id": "gzsjh_47SjCe6QFs9pKjEg",                   //ID of the node that received the request
         "search_type": "query_then_fetch",                     //Query type
         "measurements": {                                      //Metrics used
           "memory": {                                         //Memory consumption
             "number": 1280736,
             "count": 1,
             "aggregationType": "NONE"
           },
           "latency": {                                          //Latency
             "number": 20,
             "count": 1,
             "aggregationType": "NONE"
           },
           "cpu": {                                              //CPU consumption
             "number": 19340932,
             "count": 1,
             "aggregationType": "NONE"
           }
         }
       }
     ]
   }

Obtaining the Resource Consumption of the Query Resource Tracker
----------------------------------------------------------------

Run the following command to obtain the resource consumption of the query resource tracker:

.. code-block:: text

   GET _insights/health_stats

Example response:

.. code-block::

   {
     "QDyhJ8Q6Td2acc3KGQ43bQ" : {
       "ThreadPoolInfo" : {
         "query_insights_executor" : {  //Dedicated queue for the plugin, used to execute top query analysis tasks
           "type" : "scaling",
           "core" : 1,
           "max" : 1,
           "keep_alive" : "5m",
           "queue_size" : -1
         }
       },
       "QueryRecordsQueueSize" : 0,  //Number of unprocessed tasks in the query_insights_executor queue
       "TopQueriesHealthStats" : {
         "latency" : {
           "TopQueriesHeapSize" : 0,  //Memory occupied by top queries statistics
           "QueryGroupCount_Total" : 0,  //Number of groups kept in the memory when grouping is enabled
           "QueryGroupCount_MaxHeap" : 0  //Memory used to store groups when grouping is enabled
         },
         "cpu" : {
           "TopQueriesHeapSize" : 0,
           "QueryGroupCount_Total" : 0,
           "QueryGroupCount_MaxHeap" : 0
         },
         "memory" : {
           "TopQueriesHeapSize" : 0,
           "QueryGroupCount_Total" : 0,
           "QueryGroupCount_MaxHeap" : 0
         }
       },
       "FieldTypeCacheStats" : { //Cache statistics. When query grouping is enabled, the field mapping is cached to avoid repeated mapping lookups.
         "size_in_bytes" : 0,
         "entry_count" : 0,
         "evictions" : 0,
         "hit_count" : 0,
         "miss_count" : 0
       }
     }
   }

.. _en-us_topic_0000002485888678__section1754833345417:

Introduction to Query Grouping
------------------------------

When a single query continuously consumes excessive resources, it can monopolize the TopN statistics, obscuring other resource-intensive queries. Query grouping addresses this by aggregating similar queries through pattern matching, ensuring that only the first query from each group appears in the TopN results.

.. table:: **Table 3** Grouping modes

   +-----------------------------------------------------+---------------------------------------------------------------------------------+
   | Grouping Mode                                       | Description                                                                     |
   +=====================================================+=================================================================================+
   | Complete query structure (structure + field + type) | Precisely matches the field type.                                               |
   +-----------------------------------------------------+---------------------------------------------------------------------------------+
   | Query structure only                                | Considers the query structure only, while ignoring field names and types.       |
   +-----------------------------------------------------+---------------------------------------------------------------------------------+
   | Query structure + field only                        | Considers the query structure and field names only, while ignoring field types. |
   +-----------------------------------------------------+---------------------------------------------------------------------------------+
   | Query structure + type only                         | Considers the query structure and field types only, while ignoring field names. |
   +-----------------------------------------------------+---------------------------------------------------------------------------------+

.. note::

   Choose field type matching if the field types in your database remain relatively constant. The system will cache field types to improve grouping efficiency.

**Example**

The mapping of an index is as follows:

.. code-block::

   "mappings": {
     "properties": {
       "field1": {
         "type": "keyword"
       },
       "field2": {
         "type": "text"
       },
       "field3": {
         "type": "text"
       },
       "field4": {
         "type": "long"
       }
     }
   }

Perform the following query on the index:

.. code-block::

   {
     "query": {
       "bool": {
         "must": [
           {
             "term": {
               "field1": "example_value"
             }
           }
         ],
         "filter": [
           {
             "match": {
               "field2": "search_text"
             }
           },
           {
             "range": {
               "field4": {
                 "gte": 1,
                 "lte": 100
               }
             }
           }
         ],
         "should": [
           {
             "regexp": {
               "field3": ".*"
             }
           }
         ]
       }
     }
   }

:ref:`Table 4 <en-us_topic_0000002485888678__table56081397393>` provides examples that help you understand how each grouping mode behaves.

.. _en-us_topic_0000002485888678__table56081397393:

.. table:: **Table 4** Behavior of different grouping modes

   +-----------------------------------------------------+-----------------------------------+
   | Grouping Mode                                       | Pattern                           |
   +=====================================================+===================================+
   | Complete query structure (structure + field + type) | .. code-block::                   |
   |                                                     |                                   |
   |                                                     |    bool []                        |
   |                                                     |      must:                        |
   |                                                     |        term [field1, keyword]     |
   |                                                     |      filter:                      |
   |                                                     |        match [field2, text]       |
   |                                                     |        range [field4, long]       |
   |                                                     |      should:                      |
   |                                                     |        regexp [field3, text]      |
   +-----------------------------------------------------+-----------------------------------+
   | Query structure only                                | .. code-block::                   |
   |                                                     |                                   |
   |                                                     |    bool                           |
   |                                                     |      must:                        |
   |                                                     |        term                       |
   |                                                     |      filter:                      |
   |                                                     |        match                      |
   |                                                     |        range                      |
   |                                                     |      should:                      |
   |                                                     |        regexp                     |
   +-----------------------------------------------------+-----------------------------------+
   | Query structure + field only                        | .. code-block::                   |
   |                                                     |                                   |
   |                                                     |    bool []                        |
   |                                                     |      must:                        |
   |                                                     |        term [field1]              |
   |                                                     |      filter:                      |
   |                                                     |        match [field2]             |
   |                                                     |        range [field4]             |
   |                                                     |      should:                      |
   |                                                     |        regexp [field3]            |
   +-----------------------------------------------------+-----------------------------------+
   | Query structure + type only                         | .. code-block::                   |
   |                                                     |                                   |
   |                                                     |    bool []                        |
   |                                                     |      must:                        |
   |                                                     |        term [keyword]             |
   |                                                     |      filter:                      |
   |                                                     |        match [text]               |
   |                                                     |        range [long]               |
   |                                                     |      should:                      |
   |                                                     |        regexp [text]              |
   +-----------------------------------------------------+-----------------------------------+
