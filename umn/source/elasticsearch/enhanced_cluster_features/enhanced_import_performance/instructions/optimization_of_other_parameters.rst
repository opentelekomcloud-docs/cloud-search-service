:original_name: css_01_0233_0.html

.. _css_01_0233_0:

Optimization of Other Parameters
================================

After the import performance is enhanced, the number of index merge tasks increases accordingly. You can adjust the following configuration to reduce the impact of merge task overhead on the import performance:

You can increase the value of **index.merge.scheduler.max_thread_count** to increase the number of shard merge threads and reduce the traffic limit on data import. The default value is **4** and you are advised to set it to **8**.

Procedure
---------

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. In the navigation tree on the left, choose **Dev Tools**.

#. On the **Dev Tools** page, run the following command:

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index.merge.scheduler.max_thread_count": 8
        }
      }
