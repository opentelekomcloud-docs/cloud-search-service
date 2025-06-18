:original_name: css_01_0428.html

.. _css_01_0428:

Configuring Index Monitoring for an Elasticsearch Cluster
=========================================================

Scenario
--------

Index monitoring helps to monitor the index usage and trends of a cluster, allowing users to handle potential risks in a timely manner to ensure cluster reliability. Index usage statistics are collected and stored in the cluster's monitoring index (index name: **monitoring-eye-css-[yyyy-mm-dd]**. By default, these monitoring indexes are retained for one week before being permanently deleted upon expiration.

Constraints
-----------

-  Only Elasticsearch 7.6.2 and 7.10.2 clusters support index monitoring.
-  Indexes starting with **monitoring-eye-css-\*** are identified as monitoring indexes and will not be monitored. Do not use this prefix for regular indexes.
-  The index pattern of **monitoring-eye-css-\*** must not be deleted while index monitoring is enabled. Otherwise, monitoring charts will become abnormal.

Accessing a Cluster
-------------------

#. Log in to the CSS management console.
#. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column to access Kibana.
#. Click **Dev Tools** in the navigation tree on the left.

Enabling Index Monitoring
-------------------------

#. Run the following command to enable index monitoring:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "css.monitoring.index.enabled": "true"
        }
      }

#. To monitor a single index, run the following command:

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

   .. table:: **Table 1** Configuration items

      +---------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item              | Type                  | Description                                                                                                                                           |
      +=================================+=======================+=======================================================================================================================================================+
      | css.monitoring.index.enabled    | Boolean               | Whether to enable index monitoring. Setting this parameter to **true** enables index monitoring.                                                      |
      |                                 |                       |                                                                                                                                                       |
      |                                 |                       | Default value: **false**                                                                                                                              |
      +---------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
      | css.monitoring.index.interval   | Time                  | Index monitoring cycle.                                                                                                                               |
      |                                 |                       |                                                                                                                                                       |
      |                                 |                       | Minimum value: **1s**                                                                                                                                 |
      |                                 |                       |                                                                                                                                                       |
      |                                 |                       | Default value: **10s**                                                                                                                                |
      +---------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
      | css.monitoring.index.indices    | String                | Name of an index to be monitored. By default, all indexes are monitored. You can configure specific indexes or a specific type of indexes to monitor. |
      |                                 |                       |                                                                                                                                                       |
      |                                 |                       | Example:                                                                                                                                              |
      |                                 |                       |                                                                                                                                                       |
      |                                 |                       | -  **"css.monitoring.index.indices": ["**\ *index_name*\ **"]** indicates only *index_name* is monitored.                                             |
      |                                 |                       | -  **"css.monitoring.index.indices": ["log_*"]** indicates that only indexes starting with **log\_** are monitored.                                   |
      |                                 |                       | -  **"css.monitoring.index.indices": ["index1", "index2"]** indicates that **index1** and **index2** are monitored.                                   |
      |                                 |                       |                                                                                                                                                       |
      |                                 |                       | Default value: **\*** (indicating that all indexes are monitored)                                                                                     |
      +---------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
      | css.monitoring.history.duration | Time                  | Retention period of index monitoring data. The default period is a week.                                                                              |
      |                                 |                       |                                                                                                                                                       |
      |                                 |                       | Minimum value: **1d**                                                                                                                                 |
      |                                 |                       |                                                                                                                                                       |
      |                                 |                       | Default value: **7d**                                                                                                                                 |
      +---------------------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Checking the Read and Write Traffic of Indexes
----------------------------------------------

After index monitoring is enabled for a cluster, you can check the read/write traffic of this cluster's indexes during specific periods of time.

-  Run the following command to check the read and write traffic of all indexes:

   .. code-block:: text

      GET  /_cat/monitoring

-  Run the following command to check the read and write traffic of a specified index:

   .. code-block:: text

      GET  /_cat/monitoring/{indexname}

   **{indexName}** indicates the name of the index whose read and write traffic you want to check.

-  Run the following command to check the read and write traffic of an index during specified periods of time:

   .. code-block:: text

      GET _cat/monitoring?begin=1650099461000
      GET _cat/monitoring?begin=2022-04-16T08:57:41
      GET _cat/monitoring?begin=2022-04-16T08:57:41&end=2022-04-17T08:57:41

.. table:: **Table 2** Configuration items

   +-----------------------+-----------------------+----------------------------------------------------------------------------------+
   | Configuration Item    | Mandatory             | Description                                                                      |
   +=======================+=======================+==================================================================================+
   | indexname             | No                    | Index name.                                                                      |
   |                       |                       |                                                                                  |
   |                       |                       | .. note::                                                                        |
   |                       |                       |                                                                                  |
   |                       |                       |    You cannot check the traffic of system indexes, whose names start with **.**. |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------+
   | begin                 | No                    | Start time (UTC time) of the monitoring data you want to view.                   |
   |                       |                       |                                                                                  |
   |                       |                       | Time format: strict_date_optional_time|epoch_millis                              |
   |                       |                       |                                                                                  |
   |                       |                       | The default start time is 5 minutes before the current time.                     |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------+
   | end                   | No                    | End time (UTC time) of the monitoring data you want to view.                     |
   |                       |                       |                                                                                  |
   |                       |                       | Time format: strict_date_optional_time|epoch_millis                              |
   |                       |                       |                                                                                  |
   |                       |                       | The default end time is the current time.                                        |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------+

Information similar to the following is displayed:

.. code-block::

   index   begin               end                 status pri rep init unassign docs.count docs.deleted store.size pri.store.size delete.rate indexing.rate search.rate
   test 2022-03-25T09:46:53.765Z 2022-03-25T09:51:43.767Z yellow  1   1  0    1     9         0      5.9kb        5.9kb         0/s           0/s         0/s

.. table:: **Table 3** Parameters in the returned information

   +----------------+------------------------------------------------------------------------------+
   | Parameter      | Description                                                                  |
   +================+==============================================================================+
   | index          | Index name.                                                                  |
   +----------------+------------------------------------------------------------------------------+
   | begin          | Start time of the monitoring data you queried.                               |
   +----------------+------------------------------------------------------------------------------+
   | end            | End time of the monitoring data you queried.                                 |
   +----------------+------------------------------------------------------------------------------+
   | status         | Index status within the queried monitoring interval.                         |
   +----------------+------------------------------------------------------------------------------+
   | pri            | The number of index shards within the queried monitoring interval.           |
   +----------------+------------------------------------------------------------------------------+
   | rep            | The number of index replicas within the queried monitoring interval.         |
   +----------------+------------------------------------------------------------------------------+
   | init           | The number of initialized indexes within the queried monitoring interval.    |
   +----------------+------------------------------------------------------------------------------+
   | unassign       | The number of unallocated indexes within the queried monitoring interval.    |
   +----------------+------------------------------------------------------------------------------+
   | docs.count     | The number of documents within the queried monitoring interval.              |
   +----------------+------------------------------------------------------------------------------+
   | docs.deleted   | The number of deleted documents within the queried monitoring interval.      |
   +----------------+------------------------------------------------------------------------------+
   | store.size     | Index storage size within the queried monitoring interval.                   |
   +----------------+------------------------------------------------------------------------------+
   | pri.store.size | Size of the primary index shard within the queried monitoring interval.      |
   +----------------+------------------------------------------------------------------------------+
   | delete.rate    | Number of indexes deleted per second within the queried monitoring interval. |
   +----------------+------------------------------------------------------------------------------+
   | indexing.rate  | Number of indexes wrote per second within the queried monitoring interval.   |
   +----------------+------------------------------------------------------------------------------+
   | search.rate    | Number of indexes queried per second within the queried monitoring interval. |
   +----------------+------------------------------------------------------------------------------+

Checking Index Monitoring Data in Kibana Charts
-----------------------------------------------

You can check preconfigured index monitoring charts on the **Dashboard** and **Visualizations** pages of Kibana. You can also customize tables and charts.

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. Check index monitoring results in preconfigured dashboard charts.

   a. In the navigation tree on the left, click **Dashboard**.

   b. Click **[Monitoring] Index monitoring Dashboard** to check preconfigured dashboards.


      .. figure:: /_static/images/en-us_image_0000001987917665.png
         :alt: **Figure 1** Preconfigured dashboard charts

         **Figure 1** Preconfigured dashboard charts

      The preconfigured dashboard displays the number of read and write operations per second in the cluster and the top 10 indexes that have the most read and write operations per second.

      .. table:: **Table 4** Preconfigured charts

         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | Chart Name                                                      | Description                                                                 |
         +=================================================================+=============================================================================+
         | [monitoring] markdown                                           | Markdown chart, which briefly describes the dashboard content.              |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] Indexing Rate (/s)                                 | Number of documents written to a cluster per second.                        |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] Search Rate (/s)                                   | Average number of queries per second in a cluster.                          |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] indexing rate of index for top10                   | Top 10 indexes with the most documents written per second.                  |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] search rate of index for top10                     | Top 10 indexes with the most queries per second.                            |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] total docs count                                   | Total number of documents in a cluster.                                     |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] total docs delete                                  | Total number of deleted documents in a cluster.                             |
         +-----------------------------------------------------------------+-----------------------------------------------------------------------------+
         | [monitoring] total store size in bytes                          | Total storage space occupied by documents in a cluster.                     |
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

#. Check index monitoring results in custom visualizations.

   The index monitoring module periodically stores the index/stats information in the **monitoring-eys-css** index. You can use the Kibana chart function to draw custom charts.

   The following procedure describes how to check the trend of document quantities in a chart as an example.

   a. Click **Visualize** in the navigation tree on the left of the Kibana console.

   b. Click **Create visualization** and select **TSVB**.

   c. Set chart parameters and view the visualizations.

      On the **Data** tab page, set the parameters as needed.

      -  Select **Max** for **Aggregation**, and select **index_stats.primaries.docs.count** in **Field**, indicating the number of documents in a primary shard.
      -  Select **Derivative** from **Aggregation** to indicate differences between aggregation buckets. Set **Units** to **1s** to visualize network rates as "per second".
      -  Set **Aggregation** to **Positive Only** to prevent negative numbers after resetting.
      -  To show statistics by index, set **Group by** to **Terms** and **By** to **index_stats.index**. Statistics will be grouped by index name.
      -  To view data in different time segments, set the aggregation interval, or the displayed data will be incomplete. On the **Panel options** tab page, set **Interval** to **1m** or **30m** to adjust the interval of **timestamp**.


      .. figure:: /_static/images/en-us_image_0000001988037829.png
         :alt: **Figure 2** TSVB page

         **Figure 2** TSVB page


      .. figure:: /_static/images/en-us_image_0000001953598404.png
         :alt: **Figure 3** Setting the interval

         **Figure 3** Setting the interval

#. If the index monitoring charts are not displayed, load them on the Kibana console again.

   .. note::

      If the preset dashboards and visualizations cannot be found for a security-mode Elasticsearch cluster, try switching to the Private or Global space. If the issue persists, import the charts and graphs again.

   a. .. _css_01_0428__en-us_topic_0000001272074721_li779343011306:

      Create the **monitoring-kibana.ndjson** file by referring to :ref:`kibana-monitor Configuration File <css_01_0428__section6555323124717>`.

   b. On the Kibana console, choose **Management > Stack Management > Saved objects**.


      .. figure:: /_static/images/en-us_image_0000001988037837.png
         :alt: **Figure 4** Selecting Saved Objects

         **Figure 4** Selecting Saved Objects

   c. Click **Import** and upload the **monitoring-kibana.ndjson** file created in :ref:`5.a <css_01_0428__en-us_topic_0000001272074721_li779343011306>`.


      .. figure:: /_static/images/en-us_image_0000001953598400.png
         :alt: **Figure 5** Uploading a file

         **Figure 5** Uploading a file

   d. After the file is uploaded, click **done**. The index monitoring charts are imported successfully.


      .. figure:: /_static/images/en-us_image_0000001988037833.png
         :alt: **Figure 6** Index monitoring charts imported successfully

         **Figure 6** Index monitoring charts imported successfully

.. _css_01_0428__section6555323124717:

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
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] total docs delete","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] total docs delete\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"rgba(214,191,87,1)\",\"split_mode\":\"everything\",\"split_color_mode\":\"kibana\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"indices_stats._all.total.docs.deleted\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"totol_docs_delete\",\"type\":\"timeseries\",\"hidden\":false}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"tooltip_mode\":\"show_all\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"drop_last_bucket\":1,\"legend_position\":\"bottom\"}}"},"id":"cfbb4e20-664c-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxMiwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] total store size in bytes","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] total store size in bytes\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"#68BC00\",\"split_mode\":\"everything\",\"split_color_mode\":\"kibana\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"indices_stats._all.total.store.size_in_bytes\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"bytes\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"total store size in bytes\",\"type\":\"timeseries\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"tooltip_mode\":\"show_all\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"legend_position\":\"bottom\",\"background_color_rules\":[{\"id\":\"7712e550-664f-11ed-8b5d-8db37e5b4cc4\"}],\"bar_color_rules\":[{\"id\":\"77680a30-664f-11ed-8b5d-8db37e5b4cc4\"}]}}"},"id":"c7f72ae0-664e-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxMywyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] indexing rate of index for top10(/s)","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] indexing rate of index for top10(/s)\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"#68BC00\",\"split_mode\":\"terms\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"index_stats.total.indexing.index_total\"},{\"unit\":\"1s\",\"id\":\"541ed8f0-a5ee-11ec-aa10-992297d21a2e\",\"type\":\"derivative\",\"field\":\"61ca57f2-469d-11e7-af02-69e470af7417\"},{\"unit\":\"\",\"id\":\"67ec1f50-a5ee-11ec-aa10-992297d21a2e\",\"type\":\"positive_only\",\"field\":\"541ed8f0-a5ee-11ec-aa10-992297d21a2e\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"indexing_rate\",\"type\":\"timeseries\",\"split_filters\":[{\"color\":\"#68BC00\",\"id\":\"81004200-a5ee-11ec-aa10-992297d21a2e\",\"filter\":{\"query\":\"\",\"language\":\"kuery\"}}],\"filter\":{\"query\":\"\",\"language\":\"kuery\"},\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"terms_size\":\"10\",\"terms_direction\":\"desc\",\"split_color_mode\":\"rainbow\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"tooltip_mode\":\"show_all\"}}"},"id":"943b3e00-a5ef-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxNCwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] search rate of index for top10(/s)","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] search rate of index for top10(/s)\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"color\":\"rgba(99,157,12,1)\",\"split_mode\":\"terms\",\"metrics\":[{\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\",\"field\":\"index_stats.total.search.query_total\"},{\"unit\":\"1s\",\"id\":\"fdfdfad0-a5ef-11ec-aa10-992297d21a2e\",\"type\":\"derivative\",\"field\":\"61ca57f2-469d-11e7-af02-69e470af7417\"},{\"unit\":\"\",\"id\":\"0aaa26a0-a5f0-11ec-aa10-992297d21a2e\",\"type\":\"positive_only\",\"field\":\"fdfdfad0-a5ef-11ec-aa10-992297d21a2e\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"number\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"search rate\",\"type\":\"timeseries\",\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"split_color_mode\":\"rainbow\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"tooltip_mode\":\"show_all\"}}"},"id":"ab503550-a5ef-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxNSwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] indices store_size for top10","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] indices store_size for top10\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\",\"series\":[{\"id\":\"38474c50-a5f5-11ec-aa10-992297d21a2e\",\"color\":\"#68BC00\",\"split_mode\":\"terms\",\"metrics\":[{\"id\":\"38474c51-a5f5-11ec-aa10-992297d21a2e\",\"type\":\"max\",\"field\":\"index_stats.total.store.size_in_bytes\"}],\"separate_axis\":0,\"axis_position\":\"right\",\"formatter\":\"bytes\",\"chart_type\":\"line\",\"line_width\":1,\"point_size\":1,\"fill\":0.5,\"stacked\":\"none\",\"label\":\"store_size for index\",\"type\":\"timeseries\",\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"38474c51-a5f5-11ec-aa10-992297d21a2e\",\"filter\":{\"query\":\"\",\"language\":\"kuery\"},\"split_color_mode\":\"rainbow\"}],\"time_field\":\"timestamp\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"axis_position\":\"left\",\"axis_formatter\":\"number\",\"axis_scale\":\"normal\",\"show_legend\":1,\"show_grid\":1,\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"isModelInvalid\":false,\"filter\":{\"query\":\"\",\"language\":\"kuery\"},\"bar_color_rules\":[{\"id\":\"7d9d3cb0-a5f5-11ec-aa10-992297d21a2e\"}],\"tooltip_mode\":\"show_all\"}}"},"id":"c78119a0-a5f5-11ec-9a68-ada9d754c566","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxNiwyXQ=="}
   {"attributes":{"description":"","kibanaSavedObjectMeta":{"searchSourceJSON":"{}"},"title":"[monitoring] search query time in millis of index for top10(ms)","uiStateJSON":"{}","version":1,"visState":"{\"title\":\"[monitoring] search query time in millis of index for top10(ms)\",\"type\":\"metrics\",\"aggs\":[],\"params\":{\"axis_formatter\":\"number\",\"axis_max\":\"\",\"axis_min\":\"\",\"axis_position\":\"left\",\"axis_scale\":\"normal\",\"default_index_pattern\":\"monitoring-eye-css-*\",\"default_timefield\":\"timestamp\",\"id\":\"61ca57f0-469d-11e7-af02-69e470af7417\",\"index_pattern\":\"monitoring-eye-css-*\",\"interval\":\"\",\"isModelInvalid\":false,\"series\":[{\"axis_position\":\"right\",\"chart_type\":\"line\",\"color\":\"#68BC00\",\"fill\":0.5,\"formatter\":\"number\",\"id\":\"61ca57f1-469d-11e7-af02-69e470af7417\",\"label\":\"index_query_time_in_millis\",\"line_width\":1,\"metrics\":[{\"field\":\"index_stats.total.search.query_time_in_millis\",\"id\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"max\"},{\"unit\":\"1s\",\"id\":\"42c92b10-6645-11ed-925a-6de90846447d\",\"type\":\"derivative\",\"field\":\"61ca57f2-469d-11e7-af02-69e470af7417\"}],\"point_size\":1,\"separate_axis\":0,\"split_color_mode\":\"kibana\",\"split_mode\":\"terms\",\"stacked\":\"none\",\"terms_field\":\"index_stats.index\",\"terms_order_by\":\"61ca57f2-469d-11e7-af02-69e470af7417\",\"type\":\"timeseries\"}],\"show_grid\":1,\"show_legend\":1,\"time_field\":\"timestamp\",\"tooltip_mode\":\"show_all\",\"type\":\"timeseries\",\"background_color\":null,\"filter\":{\"query\":\"\",\"language\":\"kuery\"},\"legend_position\":\"right\"}}"},"id":"c8109100-6627-11ed-8cd7-973626cf6f70","references":[],"type":"visualization","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxNywyXQ=="}
   {"attributes":{"description":"","hits":0,"kibanaSavedObjectMeta":{"searchSourceJSON":"{\"query\":{\"language\":\"kuery\",\"query\":\"\"},\"filter\":[]}"},"optionsJSON":"{\"hidePanelTitles\":false,\"useMargins\":true}","panelsJSON":"[{\"gridData\":{\"x\":0,\"y\":0,\"w\":48,\"h\":5,\"i\":\"971ed6c6-81b9-491b-9f08-e3ae9c382abd\"},\"panelIndex\":\"971ed6c6-81b9-491b-9f08-e3ae9c382abd\",\"embeddableConfig\":{},\"panelRefName\":\"panel_0\"},{\"gridData\":{\"x\":0,\"y\":5,\"w\":24,\"h\":15,\"i\":\"5a6982e7-0c6c-4733-8a2d-e4c57cdf7397\"},\"panelIndex\":\"5a6982e7-0c6c-4733-8a2d-e4c57cdf7397\",\"embeddableConfig\":{},\"panelRefName\":\"panel_1\"},{\"gridData\":{\"x\":24,\"y\":5,\"w\":24,\"h\":15,\"i\":\"662476f4-739c-4a05-858c-2ee8230cf410\"},\"panelIndex\":\"662476f4-739c-4a05-858c-2ee8230cf410\",\"embeddableConfig\":{},\"panelRefName\":\"panel_2\"},{\"gridData\":{\"x\":0,\"y\":20,\"w\":16,\"h\":15,\"i\":\"d89c38e2-33f3-4592-b503-20460a6a7a57\"},\"panelIndex\":\"d89c38e2-33f3-4592-b503-20460a6a7a57\",\"embeddableConfig\":{},\"panelRefName\":\"panel_3\"},{\"gridData\":{\"x\":16,\"y\":20,\"w\":16,\"h\":15,\"i\":\"1f693b49-79fa-4807-94e8-0c12f51e54f8\"},\"panelIndex\":\"1f693b49-79fa-4807-94e8-0c12f51e54f8\",\"embeddableConfig\":{},\"panelRefName\":\"panel_4\"},{\"gridData\":{\"x\":32,\"y\":20,\"w\":16,\"h\":15,\"i\":\"616b143d-74e9-4dac-98ba-5849536f0fba\"},\"panelIndex\":\"616b143d-74e9-4dac-98ba-5849536f0fba\",\"embeddableConfig\":{},\"panelRefName\":\"panel_5\"},{\"gridData\":{\"x\":0,\"y\":35,\"w\":24,\"h\":11,\"i\":\"cfa82f27-1b8d-49ba-a7b9-d8809d3b258c\"},\"panelIndex\":\"cfa82f27-1b8d-49ba-a7b9-d8809d3b258c\",\"embeddableConfig\":{},\"panelRefName\":\"panel_6\"},{\"gridData\":{\"x\":24,\"y\":35,\"w\":24,\"h\":11,\"i\":\"135d13eb-aab6-43ca-9029-7d26e91d90e3\"},\"panelIndex\":\"135d13eb-aab6-43ca-9029-7d26e91d90e3\",\"embeddableConfig\":{},\"panelRefName\":\"panel_7\"},{\"gridData\":{\"x\":0,\"y\":46,\"w\":24,\"h\":11,\"i\":\"28a77de1-9110-49e8-b273-724f880b1653\"},\"panelIndex\":\"28a77de1-9110-49e8-b273-724f880b1653\",\"embeddableConfig\":{},\"panelRefName\":\"panel_8\"},{\"gridData\":{\"x\":24,\"y\":46,\"w\":24,\"h\":11,\"i\":\"80ece867-cf23-4935-bfbc-430afa51bcca\"},\"panelIndex\":\"80ece867-cf23-4935-bfbc-430afa51bcca\",\"embeddableConfig\":{},\"panelRefName\":\"panel_9\"},{\"gridData\":{\"x\":0,\"y\":57,\"w\":24,\"h\":11,\"i\":\"2ba970aa-c9c4-491b-bdd3-c1b1ee9bc8d3\"},\"panelIndex\":\"2ba970aa-c9c4-491b-bdd3-c1b1ee9bc8d3\",\"embeddableConfig\":{},\"panelRefName\":\"panel_10\"},{\"gridData\":{\"x\":24,\"y\":57,\"w\":24,\"h\":11,\"i\":\"f2e1b6ab-ddf7-492e-aaca-9460f11aa4aa\"},\"panelIndex\":\"f2e1b6ab-ddf7-492e-aaca-9460f11aa4aa\",\"embeddableConfig\":{},\"panelRefName\":\"panel_11\"},{\"gridData\":{\"x\":0,\"y\":68,\"w\":24,\"h\":11,\"i\":\"dd14182d-d8b9-47f2-bf36-6cba3b09586c\"},\"panelIndex\":\"dd14182d-d8b9-47f2-bf36-6cba3b09586c\",\"embeddableConfig\":{},\"panelRefName\":\"panel_12\"},{\"gridData\":{\"x\":24,\"y\":68,\"w\":24,\"h\":11,\"i\":\"a47f9333-52b7-49b7-8cac-f470cf405131\"},\"panelIndex\":\"a47f9333-52b7-49b7-8cac-f470cf405131\",\"embeddableConfig\":{},\"panelRefName\":\"panel_13\"}]","timeRestore":false,"title":"[Monitoring] Index monitoring Dashboard","version":1},"id":"524eb000-a5f2-11ec-9a68-ada9d754c566","references":[{"id":"b2811c70-a5f1-11ec-9a68-ada9d754c566","name":"panel_0","type":"visualization"},{"id":"de4f8ab0-a5f8-11ec-9a68-ada9d754c566","name":"panel_1","type":"visualization"},{"id":"811df7a0-a5f8-11ec-9a68-ada9d754c566","name":"panel_2","type":"visualization"},{"id":"eea89780-664b-11ed-8cd7-973626cf6f70","name":"panel_3","type":"visualization"},{"id":"cfbb4e20-664c-11ed-8cd7-973626cf6f70","name":"panel_4","type":"visualization"},{"id":"c7f72ae0-664e-11ed-8cd7-973626cf6f70","name":"panel_5","type":"visualization"},{"id":"943b3e00-a5ef-11ec-9a68-ada9d754c566","name":"panel_6","type":"visualization"},{"id":"ab503550-a5ef-11ec-9a68-ada9d754c566","name":"panel_7","type":"visualization"},{"id":"c78119a0-a5f5-11ec-9a68-ada9d754c566","name":"panel_8","type":"visualization"},{"id":"225f6020-a5f1-11ec-9a68-ada9d754c566","name":"panel_9","type":"visualization"},{"id":"17d49220-662a-11ed-8cd7-973626cf6f70","name":"panel_10","type":"visualization"},{"id":"c8109100-6627-11ed-8cd7-973626cf6f70","name":"panel_11","type":"visualization"},{"id":"45d571c0-6626-11ed-8cd7-973626cf6f70","name":"panel_12","type":"visualization"},{"id":"3ae5d820-6628-11ed-8cd7-973626cf6f70","name":"panel_13","type":"visualization"}],"type":"dashboard","updated_at":"2022-12-01T12:41:01.165Z","version":"WzIxOCwyXQ=="}
   {"exportedCount":16,"missingRefCount":0,"missingReferences":[]}
