:original_name: css_01_0135.html

.. _css_01_0135:

Configuring Index-Level Monitoring
==================================

When maintaining large-scale Elasticsearch clusters, operations teams frequently encounter a critical visibility gap: while cluster-wide metrics (such as CPU and memory) indicate a healthy state, specific workloads or services experience long read/write latency. Traditional cluster-level monitoring often relies on aggregated averages and fails to identify the specific indexes causing the problem. As a result, root-cause analysis is often time-consuming and labor-intensive. CSS supports index-level monitoring. It automatically collects real-time read/write traffic, latency, and storage changes for each index, and visualizes the data using a built-in Kibana dashboard. This helps you quickly identify abnormal indexes without writing any complex script. You can then make necessary adjustments to optimize performance and ensure service stability.

How the Feature Works
---------------------

Index monitoring tracks the status and performance of each index in an Elasticsearch cluster in real time, helping operations teams promptly detect and resolve performance issues. The feature works as follows:

#. Collection: A background task periodically (every 10 seconds by default, configurable) collects statistics about each target index, including the number of documents, storage size, and shard status.
#. Storage: The collected data is written to a dedicated monitoring index named **monitoring-eye-css-[yyyy-mm-dd]**.
#. Visualization: Kibana reads data from the monitoring index and visualizes it through preset dashboards or custom visualizations, enabling time series analysis, trend comparison, and fault detection.

Constraints
-----------

-  Only Elasticsearch 7.6.2 and 7.10.2 support index monitoring.
-  Do not create regular indexes with their names starting with **monitoring-eye-css-\***. Doing so may interfere with the collection of index monitoring data.
-  Do not delete the **monitoring-eye-css-[yyyy-mm-dd]** index or its associated index pattern. Otherwise, index monitoring data will be unavailable.

Logging In to Kibana
--------------------

Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

Enabling Index Monitoring
-------------------------

-  Run the following command to enable monitoring for all indexes in the current cluster:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "css.monitoring.index.enabled": "true"
        }
      }

-  Run the following command to enable monitoring for specified high-priority indexes:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "css.monitoring.index.enabled": "true",
          "css.monitoring.index.interval": "30s",
          "css.monitoring.index.indices": ["index_name"],
          "css.monitoring.history.duration": "3d"
        }
      }

.. table:: **Table 1** Parameters for enabling index monitoring

   +---------------------------------+-----------------+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                       | Type            | Default Value                                      | Description                                                                                                                                                                           |
   +=================================+=================+====================================================+=======================================================================================================================================================================================+
   | css.monitoring.index.enabled    | Boolean         | false                                              | To enable or disable index monitoring.                                                                                                                                                |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | The value can be:                                                                                                                                                                     |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | -  **true**: To enable index monitoring.                                                                                                                                              |
   |                                 |                 |                                                    | -  **false**: To disable index monitoring.                                                                                                                                            |
   +---------------------------------+-----------------+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | css.monitoring.index.indices    | String          | \* (indicating that all indexes will be monitored) | The names of the indexes you want to monitor.                                                                                                                                         |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | -  Single index: Enter the index name, for example, **my_index**.                                                                                                                     |
   |                                 |                 |                                                    | -  Multiple indexes: Enter multiple index names and use a comma (,) to separate them, for example, **my_index1,my_index2**.                                                           |
   |                                 |                 |                                                    | -  Wildcard: Use the wildcard (*) to match multiple indexes. For example, **myindex\*** matches all indexes whose name starts with **myindex**.                                       |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | By default, all indexes are monitored. If you have a large number of indexes, consider monitoring only high-priority ones.                                                            |
   +---------------------------------+-----------------+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | css.monitoring.index.interval   | Time            | 10s                                                | Index monitoring data collection interval.                                                                                                                                            |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | Value format: number + unit                                                                                                                                                           |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | -  Number: a natural number                                                                                                                                                           |
   |                                 |                 |                                                    | -  Unit: nanos (nanosecond), micros (microsecond), ms (millisecond), s (second), m (minute), h (hour), or d (day)                                                                     |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | Minimum value: **1s**                                                                                                                                                                 |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | Set an appropriate data collection interval based on your monitoring needs and cluster load. Collecting monitoring data too frequently can impact performance.                        |
   +---------------------------------+-----------------+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | css.monitoring.history.duration | Time            | 7d                                                 | Retention duration of index monitoring data, that is, the data in the **monitoring-eye-css-[yyyy-mm-dd]** index. Upon expiration, data will be deleted automatically and permanently. |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | Value format: number + unit                                                                                                                                                           |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | -  Number: a natural number                                                                                                                                                           |
   |                                 |                 |                                                    | -  Unit: nanos (nanosecond), micros (microsecond), ms (millisecond), s (second), m (minute), h (hour), or d (day)                                                                     |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | Minimum value: **1d**                                                                                                                                                                 |
   |                                 |                 |                                                    |                                                                                                                                                                                       |
   |                                 |                 |                                                    | Set an appropriate data retention duration to balance your monitoring needs with storage costs. A longer retention duration increases storage costs.                                  |
   +---------------------------------+-----------------+----------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Checking the Read and Write Traffic of Indexes
----------------------------------------------

When index monitoring is enabled for a cluster, you can use an API to query the real-time read and write traffic of indexes.

.. caution::

   System indexes (those starting with **.**) contain internal management and maintenance information. To ensure system security, their read and write traffic cannot be queried.

-  Run the following command to query the real-time read and write traffic information of all indexes in the cluster:

   .. code-block:: text

      GET /_cat/monitoring

-  Run the following command to query the real-time read and write traffic of specified indexes in the cluster:

   .. code-block:: text

      GET /_cat/monitoring/{index_name}

-  Run the following command to query the read/write traffic of indexes in a specified period:

   .. code-block:: text

      GET _cat/monitoring?begin=1650099461000
      GET _cat/monitoring?begin=2022-04-16T08:57:41
      GET _cat/monitoring?begin=2022-04-16T08:57:41&end=2022-04-17T08:57:41

.. table:: **Table 2** Parameters for querying the read and write traffic of indexes

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Type            | Default Value   | Description                                                                                                                                     |
   +=================+=================+=================+=================================================================================================================================================+
   | index_name      | String          | N/A             | Specifies one or more indexes.                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                 |
   |                 |                 |                 | -  Single index: Enter the index name, for example, **my_index**.                                                                               |
   |                 |                 |                 | -  Multiple indexes: Enter multiple index names and use a comma (,) to separate them, for example, **my_index1,my_index2**.                     |
   |                 |                 |                 | -  Wildcard: Use the wildcard (*) to match multiple indexes. For example, **myindex\*** matches all indexes whose name starts with **myindex**. |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
   | begin           | String          | Last 5 minutes  | Start time of the monitoring period.                                                                                                            |
   |                 |                 |                 |                                                                                                                                                 |
   |                 |                 |                 | Use the UTC time.                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                 |
   |                 |                 |                 | Supported formats:                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                 |
   |                 |                 |                 | -  Standard date and time format: yyyy-MM-dd or yyyy-MM-ddTHH:mm:ss                                                                             |
   |                 |                 |                 | -  A timestamp in milliseconds                                                                                                                  |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------+
   | end             | String          | Current time    | End time of the monitoring period.                                                                                                              |
   |                 |                 |                 |                                                                                                                                                 |
   |                 |                 |                 | Use the UTC time.                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                 |
   |                 |                 |                 | Supported formats:                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                 |
   |                 |                 |                 | -  Standard date and time format: yyyy-MM-dd or yyyy-MM-ddTHH:mm:ss                                                                             |
   |                 |                 |                 | -  A timestamp in milliseconds                                                                                                                  |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------+

Example response:

.. code-block::

   index   begin               end                 status pri rep init unassign docs.count docs.deleted store.size pri.store.size delete.rate indexing.rate search.rate
   test 2022-03-25T09:46:53.765Z 2022-03-25T09:51:43.767Z yellow  1   1  0    1     9         0      5.9kb        5.9kb         0/s           0/s         0/s

.. table:: **Table 3** Response parameters

   +----------------+-----------------------------------------------------------------+
   | Parameter      | Description                                                     |
   +================+=================================================================+
   | index          | Index name.                                                     |
   +----------------+-----------------------------------------------------------------+
   | begin          | Start time of the monitoring data you queried.                  |
   +----------------+-----------------------------------------------------------------+
   | end            | End time of the monitoring data you queried.                    |
   +----------------+-----------------------------------------------------------------+
   | status         | Index status within the queried period.                         |
   +----------------+-----------------------------------------------------------------+
   | pri            | The number of index shards within the queried period.           |
   +----------------+-----------------------------------------------------------------+
   | rep            | The number of index replicas within the queried period.         |
   +----------------+-----------------------------------------------------------------+
   | init           | The number of initialized indexes within the queried period.    |
   +----------------+-----------------------------------------------------------------+
   | unassign       | The number of unallocated indexes within the queried period.    |
   +----------------+-----------------------------------------------------------------+
   | docs.count     | The number of documents within the queried period.              |
   +----------------+-----------------------------------------------------------------+
   | docs.deleted   | The number of deleted documents within the queried period.      |
   +----------------+-----------------------------------------------------------------+
   | store.size     | Index storage size within the queried period.                   |
   +----------------+-----------------------------------------------------------------+
   | pri.store.size | Size of a primary index shard within the queried period.        |
   +----------------+-----------------------------------------------------------------+
   | delete.rate    | Number of indexes deleted per second within the queried period. |
   +----------------+-----------------------------------------------------------------+
   | indexing.rate  | Number of indexes written per second within the queried period. |
   +----------------+-----------------------------------------------------------------+
   | search.rate    | Number of indexes queried per second within the queried period. |
   +----------------+-----------------------------------------------------------------+

Visualizing and Analyzing Index Monitoring Data in Kibana
---------------------------------------------------------

Kibana enables efficient analysis of index monitoring data, including time series analysis, trend comparison, and fault detection.

CSS provides a pre-built Kibana dashboard that allows you to quickly view index monitoring information. You can also create custom visualizations in Kibana for more flexible monitoring.

-  Check index monitoring results in the pre-built dashboard.

   #. In the Kibana console, click the menu button in the upper-left corner, and click **Dashboard**.

   #. Find and click **[Monitoring] Index monitoring Dashboard** to view the index monitoring results.

      The pre-built dashboard displays the number of read and write operations per second in the cluster, as well as the top 10 indexes by read and write requests.


      .. figure:: /_static/images/en-us_image_0000002547709719.png
         :alt: **Figure 1** Pre-built dashboard

         **Figure 1** Pre-built dashboard

      .. table:: **Table 4** Charts on the pre-built dashboard

         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | Chart Name                                                      | Description                                                                 |
         +=================================================================+=============================================================================+
         | [monitoring] markdown                                           | Markdown chart, which briefly describes the dashboard content.              |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] Indexing Rate (/s)                                 | Number of documents written to the cluster per second.                      |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] Search Rate (/s)                                   | Average number of queries per second in the cluster.                        |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] indexing rate of index for top10                   | Top 10 indexes with the most documents written per second.                  |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] search rate of index for top10                     | Top 10 indexes with the most queries per second.                            |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] total docs count                                   | Total number of documents in the cluster.                                   |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] total docs delete                                  | Total number of deleted documents in the cluster.                           |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] total store size in bytes                          | Total storage space occupied by documents in the cluster.                   |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] indices store_size for top10                       | Top 10 indexes that occupy the largest storage space.                       |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] indices docs_count for top10                       | Top 10 indexes that store the largest number of documents.                  |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] indexing time in millis of index for top10(ms)     | Top 10 indexes with the longest document write latency in a unit time (ms). |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] search query time in millis of index for top10(ms) | Top 10 indexes with the longest index query time in a unit time (ms).       |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] segment count of index for top10                   | Top 10 indexes with the largest number of index segments.                   |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] segment memory in bytes of index for top10         | Top 10 indexes with the largest heap memory usage of index segments.        |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+

-  Check index monitoring results in custom visualizations.

   The following procedure describes how to create a custom visualization to monitor the changes in the document counts of indexes.

   #. Click **Visualize** in the upper-left menu of the Kibana console.

   #. Click **Create visualization**, and select **TSVB**.

   #. Set the chart parameters.

      On the **Data** tab shown in :ref:`Figure 2 <en-us_topic_0000001938218528__fig1253516431502>`, set the parameters as needed.

      -  Select **Max** for **Aggregation**, and select **index_stats.primaries.docs.count** in **Field**, indicating the number of documents in a primary shard.
      -  Select **Derivative** from **Aggregation** to indicate differences between aggregation buckets. Set **Units** to **1s** to visualize network rates as "per second".
      -  Set **Aggregation** to **Positive Only** to prevent negative numbers after resetting.
      -  To show statistics by index, set **Group by** to **Terms** and **By** to **index_stats.index**. Statistics will be grouped by index name.

      .. _en-us_topic_0000001938218528__fig1253516431502:

      .. figure:: /_static/images/en-us_image_0000002516189814.png
         :alt: **Figure 2** TSVB page

         **Figure 2** TSVB page

      To view data in different time segments, set the aggregation interval, or the displayed data will be incomplete. On the page shown in :ref:`Figure 3 <en-us_topic_0000001938218528__fig6536174310012>`, select the **Panel options** tab, and set **Interval** to **1m** or **30m** to adjust the granularity of **timestamp**.

      .. _en-us_topic_0000001938218528__fig6536174310012:

      .. figure:: /_static/images/en-us_image_0000002547669721.png
         :alt: **Figure 3** Setting the interval

         **Figure 3** Setting the interval

FAQ: What Do I Do If Index Monitoring Charts Are Not Displayed?
---------------------------------------------------------------

**Symptom**: The cluster's preset dashboards and visualizations are not displayed.

**Solution**:

#. In the cluster list, check whether the security mode is enabled for the cluster.

   -  If **Security Mode** is **Enabled**, switch to the Global space.

      On the Kibana page, click the username in the upper right corner and choose **Switch tenants**. On the **Select your tenant** page, switch the space and click **Confirm**. Then, check whether the charts are now displayed properly. If they are still not, go to the next step.

   -  If **Security Mode** is **Disabled**, go to the next step.

#. Import the charts again.

   a. Create the **monitoring-kibana.ndjson** file by referring to :ref:`kibana-monitor Configuration File <en-us_topic_0000001938218528__section6555323124717>`.

   b. On the Kibana console, choose **Management > Stack Management > Saved objects**.


      .. figure:: /_static/images/en-us_image_0000002517299081.png
         :alt: **Figure 4** Selecting Saved Objects

         **Figure 4** Selecting Saved Objects

   c. Click **Import** and upload the created **monitoring-kibana.ndjson** file.


      .. figure:: /_static/images/en-us_image_0000002517339091.png
         :alt: **Figure 5** Uploading a file

         **Figure 5** Uploading a file

   d. After the file is uploaded, click **done**. The index monitoring charts are imported successfully.


      .. figure:: /_static/images/en-us_image_0000002517299087.png
         :alt: **Figure 6** Index monitoring charts imported successfully

         **Figure 6** Index monitoring charts imported successfully

   If the problem persists, contact technical support.

.. _en-us_topic_0000001938218528__section6555323124717:

kibana-monitor Configuration File
---------------------------------

The content of **kibana-monitor** configuration file is as follows. You are advised to save the file as **monitoring-kibana.ndjson**.

.. code-block::

   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] segment memory in bytes of index for top10","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] segment memory in bytes of index for top10\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"#68BC00\",\"split_mode\":\"terms\",\"split_color_mode\":\"kibana\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"index_stats.total.segments.memory_in_bytes\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"bytes\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"segments memory in bytes \",\"type\":\"timeseries\",\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"61ca57f2-469d-11e7-af02-69e470af7417\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"tooltip_mode\":\"show_all\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false}}"},"id":"3ae5d820-6628-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIwNiwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] segment count of index for top10","uiStateJSON":"{}","version":1,"visState":"{\"aggs\":[],\"params\":{\"axis_formatter\":\"number\",\"axis_position\":\"left\",\"axis_scale\":\"normal\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"filter\":{\"language\":\"kuery\",\"query\":\"\"},\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"isModelInvalid\":false,\"series\":[{\"axis_position\":\"right\",\"chart_type\":\"line\",\"color\":\"rgba(231,102,76,1)\",\"fill\":0.5,\"formatter\":\"number\",\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"label\":\"segment count of index for top10\",\"line_width\":1,\"metrics\":[{\"field\":\"index_stats.total.segments.count\",\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\"}],\"point_size\":1,\"separate_axis\":0,\"split_color_mode\":\"kibana\",\"split_mode\":\"terms\",\"stacked\":\"none\",\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\"}],\"show_grid\":1,\"show_legend\":1,\"time_field\":\"timestamp\",\"tooltip_mode\":\"show_all\",\"type\":\"timeseries\"},\"title\":\"[monitoring] segment count of index for top10\",\"type\":\"metrics\"}"},"id":"45d571c0-6626-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIwNywyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] markdown","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] markdown\",\"type\":\"markdown\",\"params\":{\"fontSize\":12,\"openLinksInNewTab\":false,\"markdown\":\"### Index Monitoring \\nThis dashboard contains default table for you to play with. You can view it, search it, and interact with the visualizations.\"},\"aggs\":[]}"},"id":"b2811c70-a5f1-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIwOCwyXQ=="}
   {"attributes":{"description":"number of document being indexing for primary and replica shards","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] Indexing Rate (/s)","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] Indexing Rate (/s)\",\"type\":\"metrics\",\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"rgba(0,32,188,1)\",\"split_mode\":\"everything\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"indices_stats._all.total.indexing.index_total\"},{\"unit\":\"1s\",\"id\":\"fed72db0-a5f8-11ec-aa10-992297d21a2e\",\"type\":\"derivative\",\"field\":\"61ca57f2-469d-11e7-af02-69e470af7417\"},{\"unit\":\"\",\"id\":\"14b66420-a5f9-11ec-aa10-992297d21a2e\",\"type\":\"positive_only\",\"field\":\"fed72db0-a5f8-11ec-aa10-992297d21a2e\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"Indexing Rate (/s)\",\"type\":\"timeseries\",\"split_color_mode\":\"rainbow\",\"hidden\":false}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"legend_position\":\"bottom\"},\"aggs\":[]}"},"id":"de4f8ab0-a5f8-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIwOSwyXQ=="}
   {"attributes":{"description":"number of search request being executed in primary and replica shards","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] Search Rate (/s)","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] Search Rate (/s)\",\"type\":\"metrics\",\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"rgba(0,33,224,1)\",\"split_mode\":\"everything\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"indices_stats._all.total.search.query_total\"},{\"unit\":\"1s\",\"id\":\"b1093ac0-a5f7-11ec-aa10-992297d21a2e\",\"type\":\"derivative\",\"field\":\"61ca57f2-469d-11e7-af02-69e470af7417\"},{\"unit\":\"\",\"id\":\"c17db930-a5f7-11ec-aa10-992297d21a2e\",\"type\":\"positive_only\",\"field\":\"b1093ac0-a5f7-11ec-aa10-992297d21a2e\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"split_color_mode\":\"rainbow\",\"label\":\"Search Rate (/s)\",\"type\":\"timeseries\",\"filter\":{\"query\":\"\",\"language\":\"kuery\"}}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"legend_position\":\"bottom\"},\"aggs\":[]}"},"id":"811df7a0-a5f8-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxMCwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] total docs count","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] total docs count\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"rgba(218,139,69,1)\",\"split_mode\":\"everything\",\"split_color_mode\":\"kibana\",\"metrics\":[{\"unit\":\"\",\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"indices_stats._all.total.docs.count\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"total_docs_count\",\"type\":\"timeseries\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"tooltip_mode\":\"show_all\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"legend_position\":\"bottom\"}}"},"id":"eea89780-664b-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxMSwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] total docs delete","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] total docs delete\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"rgba(214,191,87,1)\",\"split_mode\":\"everything\",\"split_color_mode\":\"kibana\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"indices_stats._all.total.docs.deleted\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"total_docs_delete\",\"type\":\"timeseries\",\"hidden\":false}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"tooltip_mode\":\"show_all\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"drop_last_bucket\":1,\"legend_position\":\"bottom\"}}"},"id":"cfbb4e20-664c-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxMiwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] total store size in bytes","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] total store size in bytes\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"#68BC00\",\"split_mode\":\"everything\",\"split_color_mode\":\"kibana\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"indices_stats._all.total.store.size_in_bytes\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"bytes\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"total store size in bytes\",\"type\":\"timeseries\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"tooltip_mode\":\"show_all\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"legend_position\":\"bottom\",\"background_color_rules\":[{\"id\":\"7712e550-664f-11ed-8b5d-8db37e5b4cc4\"}],\"bar_color_rules\":[{\"id\":\"77680a30-664f-11ed-8b5d-8db37e5b4cc4\"}]}}"},"id":"c7f72ae0-664e-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxMywyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] indexing rate of index for top10(/s)","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] indexing rate of index for top10(/s)\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"#68BC00\",\"split_mode\":\"terms\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"index_stats.total.indexing.index_total\"},{\"unit\":\"1s\",\"id\":\"541ed8f0-a5ee-11ec-aa10-992297d21a2e\",\"type\":\"derivative\",\"field\":\"61ca57f2-469d-11e7-af02-69e470af7417\"},{\"unit\":\"\",\"id\":\"67ec1f50-a5ee-11ec-aa10-992297d21a2e\",\"type\":\"positive_only\",\"field\":\"541ed8f0-a5ee-11ec-aa10-992297d21a2e\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"indexing_rate\",\"type\":\"timeseries\",\"split_filters\":[{\"color\":\"#68BC00\",\"id\":\"81004200-a5ee-11ec-aa10-992297d21a2e\",\"filter\":{\"query\":\"\",\"language\":\"kuery\"}}],\"filter\":{\"query\":\"\",\"language\":\"kuery\"},\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"terms_size\":\"10\",\"terms_direction\":\"desc\",\"split_color_mode\":\"rainbow\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"tooltip_mode\":\"show_all\"}}"},"id":"943b3e00-a5ef-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxNCwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] search rate of index for top10(/s)","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] search rate of index for top10(/s)\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"rgba(99,157,12,1)\",\"split_mode\":\"terms\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"index_stats.total.search.query_total\"},{\"unit\":\"1s\",\"id\":\"fdfdfad0-a5ef-11ec-aa10-992297d21a2e\",\"type\":\"derivative\",\"field\":\"61ca57f2-469d-11e7-af02-69e470af7417\"},{\"unit\":\"\",\"id\":\"0aaa26a0-a5f0-11ec-aa10-992297d21a2e\",\"type\":\"positive_only\",\"field\":\"fdfdfad0-a5ef-11ec-aa10-992297d21a2e\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"search rate\",\"type\":\"timeseries\",\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"split_color_mode\":\"rainbow\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"tooltip_mode\":\"show_all\"}}"},"id":"ab503550-a5ef-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxNSwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] indices store_size for top10","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] indices store_size for top10\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"38474c50-a5f5-11ec-aa10-992297d21a2e\",\"color\":\"#68BC00\",\"split_mode\":\"terms\",\"metrics\":[{\"id\":\"38474c51-a5f5-11ec-aa10-992297d21a2e\",\"type\":\"max\",\"field\":\"index_stats.total.store.size_in_bytes\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"bytes\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"store_size for index\",\"type\":\"timeseries\",\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"38474c51-a5f5-11ec-aa10-992297d21a2e\",\"filter\":{\"query\":\"\",\"language\":\"kuery\"},\"split_color_mode\":\"rainbow\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"filter\":{\"query\":\"\",\"language\":\"kuery\"},\"bar_color_rules\":[{\"id\":\"7d9d3cb0-a5f5-11ec-aa10-992297d21a2e\"}],\"tooltip_mode\":\"show_all\"}}"},"id":"c78119a0-a5f5-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxNiwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] search query time in millis of index for top10(ms)","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] search query time in millis of index for top10(ms)\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"axis_formatter\":\"number\",\"axis_max\":\"\",\"axis_min\":\"\",\"axis_position\":\"left\",\"axis_scale\":\"normal\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"isModelInvalid\":false,\"series\":[{\"axis_position\":\"right\",\"chart_type\":\"line\",\"color\":\"#68BC00\",\"fill\":0.5,\"formatter\":\"number\",\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"label\":\"index_query_time_in_millis\",\"line_width\":1,\"metrics\":[{\"field\":\"index_stats.total.search.query_time_in_millis\",\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\"},{\"unit\":\"1s\",\"id\":\"42c92b10-6645-11ed-925a-6de90846447d\",\"type\":\"derivative\",\"field\":\"61ca57f2-469d-11e7-af02-69e470af7417\"}],\"point_size\":1,\"separate_axis\":0,\"split_color_mode\":\"kibana\",\"split_mode\":\"terms\",\"stacked\":\"none\",\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\"}],\"show_grid\":1,\"show_legend\":1,\"time_field\":\"timestamp\",\"tooltip_mode\":\"show_all\",\"type\":\"timeseries\",\"background_color\":null,\"filter\":{\"query\":\"\",\"language\":\"kuery\"},\"legend_position\":\"right\"}}"},"id":"c8109100-6627-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxNywyXQ=="}
   {"attributes":{"description":"","hits":0,"kibanaSavedObjectMeta":{"searchSourceJSON":"{\"query\":{\"language\":\"kuery\",\"query\":\"\"},\"filter\":[]}"},"optionsJSON":"{\"hidePanelTitles\":false,\"useMargins\":true}","panelsJSON":"[{\"gridData\":{\"x\":0,\"y\":0,\"w\":48,\"h\":5,\"i\":\"971ed6c6-81b9-491b-9f08-e3ae9c382abd\"},\"panelIndex\":\"971ed6c6-81b9-491b-9f08-e3ae9c382abd\",\"embeddableConfig\":{},\"panelRefName\":\"panel_0\"},{\"gridData\":{\"x\":0,\"y\":5,\"w\":24,\"h\":15,\"i\":\"5a6982e7-0c6c-4733-8a2d-e4c57cdf7397\"},\"panelIndex\":\"5a6982e7-0c6c-4733-8a2d-e4c57cdf7397\",\"embeddableConfig\":{},\"panelRefName\":\"panel_1\"},{\"gridData\":{\"x\":24,\"y\":5,\"w\":24,\"h\":15,\"i\":\"662476f4-739c-4a05-858c-2ee8230cf410\"},\"panelIndex\":\"662476f4-739c-4a05-858c-2ee8230cf410\",\"embeddableConfig\":{},\"panelRefName\":\"panel_2\"},{\"gridData\":{\"x\":0,\"y\":20,\"w\":16,\"h\":15,\"i\":\"d89c38e2-33f3-4592-b503-20460a6a7a57\"},\"panelIndex\":\"d89c38e2-33f3-4592-b503-20460a6a7a57\",\"embeddableConfig\":{},\"panelRefName\":\"panel_3\"},{\"gridData\":{\"x\":16,\"y\":20,\"w\":16,\"h\":15,\"i\":\"1f693b49-79fa-4807-94e8-0c12f51e54f8\"},\"panelIndex\":\"1f693b49-79fa-4807-94e8-0c12f51e54f8\",\"embeddableConfig\":{},\"panelRefName\":\"panel_4\"},{\"gridData\":{\"x\":32,\"y\":20,\"w\":16,\"h\":15,\"i\":\"616b143d-74e9-4dac-98ba-5849536f0fba\"},\"panelIndex\":\"616b143d-74e9-4dac-98ba-5849536f0fba\",\"embeddableConfig\":{},\"panelRefName\":\"panel_5\"},{\"gridData\":{\"x\":0,\"y\":35,\"w\":24,\"h\":11,\"i\":\"cfa82f27-1b8d-49ba-a7b9-d8809d3b258c\"},\"panelIndex\":\"cfa82f27-1b8d-49ba-a7b9-d8809d3b258c\",\"embeddableConfig\":{},\"panelRefName\":\"panel_6\"},{\"gridData\":{\"x\":24,\"y\":35,\"w\":24,\"h\":11,\"i\":\"135d13eb-aab6-43ca-9029-7d26e91d90e3\"},\"panelIndex\":\"135d13eb-aab6-43ca-9029-7d26e91d90e3\",\"embeddableConfig\":{},\"panelRefName\":\"panel_7\"},{\"gridData\":{\"x\":0,\"y\":46,\"w\":24,\"h\":11,\"i\":\"28a77de1-9110-49e8-b273-724f880b1653\"},\"panelIndex\":\"28a77de1-9110-49e8-b273-724f880b1653\",\"embeddableConfig\":{},\"panelRefName\":\"panel_8\"},{\"gridData\":{\"x\":24,\"y\":46,\"w\":24,\"h\":11,\"i\":\"80ece867-cf23-4935-bfbc-430afa51bcca\"},\"panelIndex\":\"80ece867-cf23-4935-bfbc-430afa51bcca\",\"embeddableConfig\":{},\"panelRefName\":\"panel_9\"},{\"gridData\":{\"x\":0,\"y\":57,\"w\":24,\"h\":11,\"i\":\"2ba970aa-c9c4-491b-bdd3-c1b1ee9bc8d3\"},\"panelIndex\":\"2ba970aa-c9c4-491b-bdd3-c1b1ee9bc8d3\",\"embeddableConfig\":{},\"panelRefName\":\"panel_10\"},{\"gridData\":{\"x\":24,\"y\":57,\"w\":24,\"h\":11,\"i\":\"f2e1b6ab-ddf7-492e-aaca-9460f11aa4aa\"},\"panelIndex\":\"f2e1b6ab-ddf7-492e-aaca-9460f11aa4aa\",\"embeddableConfig\":{},\"panelRefName\":\"panel_11\"},{\"gridData\":{\"x\":0,\"y\":68,\"w\":24,\"h\":11,\"i\":\"dd14182d-d8b9-47f2-bf36-6cba3b09586c\"},\"panelIndex\":\"dd14182d-d8b9-47f2-bf36-6cba3b09586c\",\"embeddableConfig\":{},\"panelRefName\":\"panel_12\"},{\"gridData\":{\"x\":24,\"y\":68,\"w\":24,\"h\":11,\"i\":\"a47f9333-52b7-49b7-8cac-f470cf405131\"},\"panelIndex\":\"a47f9333-52b7-49b7-8cac-f470cf405131\",\"embeddableConfig\":{},\"panelRefName\":\"panel_13\"}]","timeRestore":false,"title":"[Monitoring] Index monitoring Dashboard","version":1},"id":"524eb000-a5f2-11ec-9a68-ada9d754c566","references":[{"id":"b2811c70-a5f1-11ec-9a68-ada9d754c566","name":"panel_0","type":"visualization"},{"id":"de4f8ab0-a5f8-11ec-9a68-ada9d754c566","name":"panel_1","type":"visualization"},{"id":"811df7a0-a5f8-11ec-9a68-ada9d754c566","name":"panel_2","type":"visualization"},{"id":"eea89780-664b-11ed-8cd7-973626cf6f70","name":"panel_3","type":"visualization"},{"id":"cfbb4e20-664c-11ed-8cd7-973626cf6f70","name":"panel_4","type":"visualization"},{"id":"c7f72ae0-664e-11ed-8cd7-973626cf6f70","name":"panel_5","type":"visualization"},{"id":"943b3e00-a5ef-11ec-9a68-ada9d754c566","name":"panel_6","type":"visualization"},{"id":"ab503550-a5ef-11ec-9a68-ada9d754c566","name":"panel_7","type":"visualization"},{"id":"c78119a0-a5f5-11ec-9a68-ada9d754c566","name":"panel_8","type":"visualization"},{"id":"225f6020-a5f1-11ec-9a68-ada9d754c566","name":"panel_9","type":"visualization"},{"id":"17d49220-662a-11ed-8cd7-973626cf6f70","name":"panel_10","type":"visualization"},{"id":"c8109100-6627-11ed-8cd7-973626cf6f70","name":"panel_11","type":"visualization"},{"id":"45d571c0-6626-11ed-8cd7-973626cf6f70","name":"panel_12","type":"visualization"},{"id":"3ae5d820-6628-11ed-8cd7-973626cf6f70","name":"panel_13","type":"visualization"}],"type":"dashboard","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxOCwyXQ=="}
   {"exportedCount":16,"missingRefCount":0,"missingReferences":[]}
