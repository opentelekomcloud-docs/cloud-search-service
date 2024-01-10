:original_name: css_01_0232.html

.. _css_01_0232:

Text Index Acceleration
=======================

-  You can configure **index.native_speed_up** to enable or disable text index acceleration. This function optimizes the index process and memory usage to accelerate index building for text fields (text and keyword).
-  You can configure **index.native_analyzer** to enable or disable word segmentation acceleration. For texts that require common word segmentation, you can use the analyzer to accelerate word segmentation.

Procedure
---------

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. In the navigation tree on the left, choose **Dev Tools**.

#. On the **Dev Tools** page, run the following command:

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index.native_speed_up": true,
          "index.native_analyzer": true
        },
        "mappings": {
          "properties": {
            "my_field": {
              "type": "text"
            }
          }
        }
      }
