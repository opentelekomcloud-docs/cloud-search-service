:original_name: en-us_topic_0000001534148568.html

.. _en-us_topic_0000001534148568:

Bulk Route Optimization
=======================

According to the default routing rule of Elasticsearch, data in a bulk request is routed to different shards. When massive data is written and a large number of index shards exist, excessive internal requests forwarding may trigger bulk rejection. In a large-scale cluster, the long tail effect causes a high bulk request latency.

You can specify the **index.bulk_routing** configuration item to enable bulk route optimization. This function reduces the requests that need to be internally forwarded. For clusters containing a large number of shards, this function can improve write performance and reduce bulk rejection.

Procedure
---------

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. In the navigation tree on the left, choose **Dev Tools**.

#. On the **Dev Tools** page, run the following command:

   .. code-block:: text

      PUT my_index
      {
        "settings": {
          "index.bulk_routing": "local_pack"
        }
      }

   .. table:: **Table 1** Values of **index.bulk_routing**

      +------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Value      | Description                                                                                                                                                                                                                                            |
      +============+========================================================================================================================================================================================================================================================+
      | default    | The default routing mechanism of Elasticsearch is used. Records in a bulk request are split and routed independently.                                                                                                                                  |
      +------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | pack       | Data of a single bulk request is randomly routed to the same shard.                                                                                                                                                                                    |
      +------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | local_pack | The data of a single bulk request is routed to the local shard of the data node that receives the bulk request. If the node does not contain the corresponding index shard, the data is randomly routed to another node that contains the index shard. |
      +------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
