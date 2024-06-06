:original_name: en-us_topic_0000001528379301.html

.. _en-us_topic_0000001528379301:

Monitoring OBS Operations
=========================

To clearly display the operations of the storage and compute decoupling plugin in OBS, the real-time OBS rate metric is added to CSS and recorded in the system index.

Prerequisite
------------

This feature is available in Elasticsearch clusters of versions 7.6.2 and 7.10.2 and OpenSearch clusters created after March 2023.

Description
-----------

-  The :ref:`GET _frozen_stats/obs_rate <en-us_topic_0000001528379301__en-us_topic_0000001520039673_section1130685012812>` API is used to query the real-time rate of OBS operations.
-  The system index :ref:`.freeze_obs_rate-YYYY.mm.dd <en-us_topic_0000001528379301__en-us_topic_0000001520039673_section1319142217244>` is added to store the real-time OBS operation rate and OBS operation data, helping you monitor the OBS operations.
-  The :ref:`low_cost.obs_rate_index.evict_time <en-us_topic_0000001528379301__en-us_topic_0000001520039673_section37841313194117>` parameter is added to control the storage duration of the **.freeze_obs_rate-YYYY.mm.dd** index

.. _en-us_topic_0000001528379301__en-us_topic_0000001520039673_section1130685012812:

**GET \_frozen_stats/obs_rate** API
-----------------------------------

-  Calculation method: The average OBS operation rate in the last 5 seconds is calculated every 5 seconds.

-  Example request:

   .. code-block:: text

      GET _frozen_stats/obs_rate
      GET _frozen_stats/obs_rate/{nodeId}

   **{nodeId}** indicates the ID of the node whose OBS operation rate you want to query.

-  Example response:

   .. code-block::

      {
         "_nodes" : {
           "total" : 1,
           "successful" : 1,
           "failed" : 0
         },
         "cluster_name" : "elasticsearch",
         "nodes" : {
           "dflDvcSwTJ-fkiIlT2zE3A" : {
             "name" : "node-1",
             "transport_address" : "127.0.0.1:9300",
             "host" : "127.0.0.1",
             "ip" : "127.0.0.1",
             "update_time" : 1671777600482,                            // Time when the current statistics are updated.
             "obs_rate" : {
               "list_op_rate" : 0.0,                                   // Rate of OBS list operations. Unit: times/s.
               "get_meta_op_rate" : 0.0,                               // Rate of OBS get meta operations. Unit: times/s.
               "get_obj_op_rate" : 0.0,                                // Rate of OBS get operations. Unit: times/s.
               "put_op_rate" : 0.0,                                    // Rate of OBS put operations. Unit: times/s.
               "obs_total_op_rate" : 0.0,                              // Rate of all OBS operations. The unit is times/s.
               "obs_upload_rate" : "0.0 MB/s",                         // Data upload rate of OBS, in MB/s.
               "obs_download_rate" : "0.0 MB/s"                        // Data download rate of OBS, in MB/s.
             }
           }
         }
       }

.. _en-us_topic_0000001528379301__en-us_topic_0000001520039673_section1319142217244:

System Index
------------

-  System index name: **.freeze_obs_rate-YYYY.mm.dd**.
-  Example: **.freeze_obs_rate-2023.01.23**

   .. note::

      The default retention period of indexes is 30 days.

.. _en-us_topic_0000001528379301__en-us_topic_0000001520039673_section37841313194117:

Configuration Item
------------------

+------------------------------------+-------------+-------------+---------------------------------+--------------------------------------------------------------------+
| **Configuration Item**             | **Type**    | **Scope**   | **Can Be Dynamically Modified** | **Description**                                                    |
+------------------------------------+-------------+-------------+---------------------------------+--------------------------------------------------------------------+
| low_cost.obs_rate_index.evict_time | String      | node        | Yes                             | The retention period of the **.freeze_obs_rate-YYYY.mm.dd** index. |
|                                    |             |             |                                 |                                                                    |
|                                    |             |             |                                 | -  Value range: 1d to 365d                                         |
|                                    |             |             |                                 | -  Default value: **30d**                                          |
|                                    |             |             |                                 | -  Unit: day                                                       |
+------------------------------------+-------------+-------------+---------------------------------+--------------------------------------------------------------------+

For example, run the following command to modify the retention period of the **.freeze_obs_rate-YYYY.mm.dd** index:

.. code-block:: text

   PUT _cluster/settings
    {
      "persistent": {
        "low_cost.obs_rate_index.evict_time":  "7d"
      }
    }
