:original_name: css_01_0458.html

.. _css_01_0458:

Enhancing the Data Import Performance of OpenSearch Clusters
============================================================

Overview
--------

This unique CSS feature significantly improves data import performance and reduces write rejections through bulk route optimization, text index acceleration, and word segmentation acceleration. You are advised to use this feature for clusters that contain a large number of index shards and text indexes, or have a high inbound data throughput.

.. table:: **Table 1** Ways to improve data import performance

   +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
   | Method                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                             | Details                                                                              |
   +===============================+=========================================================================================================================================================================================================================================================================================================================================================================================================================================================================+======================================================================================+
   | Bulk route optimization       | According to the default routing rule of OpenSearch, each piece of data in a bulk request is routed to a different shard. When a large amount of data is written in and a large number of index shards exist, excessive internal request forwarding may trigger bulk rejection. Additionally, in a large-scale cluster, the long tail effect causes a high latency for bulk requests.                                                                                   | :ref:`Bulk Route Optimization <css_01_0458__css_01_0397_section9414161115511>`       |
   |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                      |
   |                               | You can specify the **index.bulk_routing** configuration item to enable bulk route optimization. You can use it to reduce the number of requests that need to be internally forwarded. For a cluster that has a large number of shards, this setting can improve write performance and reduce bulk rejection.                                                                                                                                                           |                                                                                      |
   |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                      |
   |                               | .. note::                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                      |
   |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                      |
   |                               |    After bulk route optimization is enabled (that is, **index.bulk_routing** is set to **pack** or **local_pack**), data writes are no longer routed based on **\_id**, and routing-related functionality may be affected. For example, ID-based GET requests may fail.                                                                                                                                                                                                 |                                                                                      |
   +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
   | Bulk aggregation optimization | You can specify the **index.aggr_perf_batch_size** configuration item to enable or disable bulk aggregation optimization. When bulk aggregation optimization is enabled, documents in a bulk request are written in batches, rather than individually. This helps to reduce the overheads of memory requests, lock requests, and other calls, improving data import performance.                                                                                        | :ref:`Bulk Aggregation Optimization <css_01_0458__css_01_0397_section1443152195614>` |
   +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
   | Text index acceleration       | You can configure **index.native_speed_up** to enable or disable text index acceleration. This setting optimizes the indexing process and memory access to accelerate index building for text fields (text and keyword). When text index acceleration is enabled, you can configure **index.native_analyzer** to enable word segmentation acceleration as well. For texts that need common word segmentation, you can use the analyzer to accelerate word segmentation. | :ref:`Text Index Acceleration <css_01_0458__css_01_0397_section15513121414583>`      |
   |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                      |
   |                               | .. note::                                                                                                                                                                                                                                                                                                                                                                                                                                                               |                                                                                      |
   |                               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |                                                                                      |
   |                               |    -  Word segmentation acceleration can be enabled (set **index.native_analyzer** to **true**) only when text index acceleration is enabled (set **index.native_speed_up** to **true**). Otherwise, word segmentation acceleration will not take effect.                                                                                                                                                                                                               |                                                                                      |
   |                               |    -  Text index acceleration cannot be enabled for indexes that contain nested fields.                                                                                                                                                                                                                                                                                                                                                                                 |                                                                                      |
   +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+
   | Index merge task optimization | Enabling the three optimization options above will increase the number of index merge tasks in the cluster. You can configure **index.merge.scheduler.max_thread_count** to reduce the impact of index merge tasks on data import performance. The optimization is about increasing the number of shard merging threads and thereby alleviate the throttling of data import.                                                                                            | :ref:`Index Merge Task Optimization <css_01_0458__css_01_0397_section124450517595>`  |
   +-------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------+

Constraints
-----------

Only OpenSearch 1.3.6 clusters support data import performance enhancement.

Prerequisites
-------------

The cluster whose data import performance you want to enhance is in the Available state.

.. _css_01_0458__css_01_0397_section9414161115511:

Bulk Route Optimization
-----------------------

You can specify the **index.bulk_routing** configuration item to enable bulk route optimization. You can use it to reduce the number of requests that need to be internally forwarded. For a cluster that has a large number of shards, this setting can improve write performance and reduce bulk rejection.

.. note::

   After bulk route optimization is enabled (that is, **index.bulk_routing** is set to **pack** or **local_pack**), data writes are no longer routed based on **\_id**, and routing-related functionality may be affected. For example, ID-based GET requests may fail.

#. Choose **Clusters** from the navigation pane. On the **Clusters** page, select an available cluster, and click **Access Kibana** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation tree on the OpenSearch Dashboards console, choose **Dev Tools**.

#. On the **Dev Tools** page, run the following command to enable bulk route optimization:

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index.bulk_routing": "local_pack"
        }
      }

   The options for the **index.bulk_routing** configuration item are as follows:

   -  **default**: Use the default routing mechanism. Records in a bulk request are split and then routed separately.
   -  **pack**: All data of a single bulk request is randomly routed to the same shard.
   -  **local_pack**: The data of a single bulk request is routed to a local shard of the data node that has received the bulk request. If the node does not contain the corresponding index shard, the data is randomly routed to another node that contains the index shard. This solution depends on the random distribution of client bulk requests and the balanced distribution of primary shards.

.. _css_01_0458__css_01_0397_section1443152195614:

Bulk Aggregation Optimization
-----------------------------

You can specify the **index.aggr_perf_batch_size** configuration item to enable or disable bulk aggregation optimization. When bulk aggregation optimization is enabled, documents in a bulk request are written in batches, rather than individually. This helps to reduce the overheads of memory requests, lock requests, and other calls, improving data import performance.

#. Choose **Clusters** from the navigation pane. On the **Clusters** page, select an available cluster, and click **Access Kibana** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation tree on the OpenSearch Dashboards console, choose **Dev Tools**.

#. On the **Dev Tools** page, run the following command to enable bulk aggregation optimization:

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index.aggr_perf_batch_size": "128"
        }
      }

   The value range of the **index.aggr_perf_batch_size** configuration item is [1, Integer.MAX_VALUE]. The default value is 1, indicating that bulk aggregation optimization is disabled. If the value is greater than 1, bulk aggregation optimization is enabled, the value of **MIN(bulk_doc_size, aggr_perf_batch_size)** indicates the bulk size.

.. _css_01_0458__css_01_0397_section15513121414583:

Text Index Acceleration
-----------------------

You can configure **index.native_speed_up** to enable or disable text index acceleration. This setting optimizes the indexing process and memory access to accelerate index building for text fields (text and keyword). When text index acceleration is enabled, you can configure **index.native_analyzer** to enable word segmentation acceleration as well. For texts that need common word segmentation, you can use the analyzer to accelerate word segmentation.

.. note::

   -  Word segmentation acceleration can be enabled (set **index.native_analyzer** to **true**) only when text index acceleration is enabled (set **index.native_speed_up** to **true**). Otherwise, word segmentation acceleration will not take effect.
   -  Text index acceleration cannot be enabled for indexes that contain nested fields.

#. Choose **Clusters** from the navigation pane. On the **Clusters** page, select an available cluster, and click **Access Kibana** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation tree on the OpenSearch Dashboards console, choose **Dev Tools**.

#. On the **Dev Tools** page, run the following command to enable text index acceleration:

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index.native_speed_up": true,
          "index.native_analyzer": true
        }
      }

   The values of **index.native_speed_up** and **index.native_analyzer** are **true** or **false**. The default value is **false**.

.. _css_01_0458__css_01_0397_section124450517595:

Index Merge Task Optimization
-----------------------------

Enabling the three optimization options above will increase the number of index merge tasks in the cluster. You can configure **index.merge.scheduler.max_thread_count** to reduce the impact of index merge tasks on data import performance. The optimization is about increasing the number of shard merging threads and thereby alleviate the throttling of data import.

#. Choose **Clusters** from the navigation pane. On the **Clusters** page, select an available cluster, and click **Access Kibana** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation tree on the OpenSearch Dashboards console, choose **Dev Tools**.

#. On the **Dev Tools** page, run the following command to start index merge task optimization:

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index.merge.scheduler.max_thread_count": 8
        }
      }

   The value range of **index.merge.scheduler.max_thread_count** is [1, node.processors/2]. The default value is 4, and the recommended value is 8.
