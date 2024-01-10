:original_name: css_01_0231.html

.. _css_01_0231:

Bulk Aggregation Optimization
=============================

You can specify the **index.aggr_perf_batch_size** configuration item to enable or disable batch import optimization. After the batch import function is enabled, documents in bulk requests are written in batches. This function reduces the overhead of memory application, application lock, and other calls, improving data import performance.

.. note::

   The value range of **index.aggr_perf_batch_size** is [1, Integer.MAX_VALUE]. The default value is **1**, indicating that the batch import function is disabled. If the value is greater than 1, the batch import function is enabled and the value of **MIN(bulk_doc_size, aggr_perf_batch_size)** indicates the batch size.

Procedure
---------

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. In the navigation tree on the left, choose **Dev Tools**.

#. On the **Dev Tools** page, run the following command:

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index.aggr_perf_batch_size": "128"
        }
      }
