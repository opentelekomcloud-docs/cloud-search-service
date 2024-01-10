:original_name: css_01_0187.html

.. _css_01_0187:

Enhanced Cold Data Query Performance
====================================

Context
-------

When you query data on the **Discover** page of Kibana for the first time, all data needs to be obtained from OBS because there is no cache. If a large number of documents are returned, it takes a long time to obtain the corresponding time fields and file metadata from OBS. To accelerate queries the first time they run on the **Discover** page, you can cache data locally.

Prerequisites
-------------

This feature is available in Elasticsearch clusters of versions 7.6.2 and 7.10.2 and Opensearch clusters created after February 2023.

API for Querying Cold Data from Local Cache
-------------------------------------------

This API can be used to query the cold data from local cache.

Example request:

.. code-block:: text

   GET /_frozen_stats/local_cache
   GET /_frozen_stats/local_cache/{nodeId}

Response example:

.. code-block::

   {
      "_nodes" : {
        "total" : 1,
        "successful" : 1,
        "failed" : 0
      },
      "cluster_name" : "elasticsearch",
      "nodes" : {
        "6by3lPy1R3m55Dcq3liK8Q" : {
          "name" : "node-1",
          "transport_address" : "127.0.0.1:9300",
          "host" : "127.0.0.1",
          "ip" : "127.0.0.1",
          "local_cache" : {
            "get_stats" : {
              "get_total_count" : 562,                            //Total number of times data was retrieved from the local cold data cache.
              "get_hit_count" : 562,                              //Total number of hits in the local cold data cache.
              "get_miss_count" : 0,                               //Total number of local cold data cache misses.
              "get_total_ns" : 43849200,                          //Total duration for retrieving data from the local cold data cache.
              "get_avg_ns" : 78023                                //Average duration for retrieving data from the local cold data cache.
            },
            "load_stats" : {
              "load_count" : 2,                                    //Number of times cold data was loaded from the local cache
              "load_total_ms" : 29,                                //Total duration for loading cold data from the local cache
              "load_avg_ms" : 14,                                  //Average duration for loading cold data from the local cache
              "load_fail_count" : 0,                               //Number of failure times for loading cold data from the local cache
              "load_overflow_count" : 0                            //Number of times the local cold data cache exceeds the cache pool size.
            },
            "reload_stats" : {
              "reload_count" : 0,                                  //Number of times the local cold data cache was regenerated.
              "reload_total_ms" : 0,                               //Total duration for regenerating the local cold data cache.
              "reload_avg_ms" : 0,                                 //Average duration for regenerating the local cold data cache.
              "reload_fail_count" : 0                              //Number of failures in regenerating the local cold data cache.
            },
            "init_stats" : {
              "init_count" : 0,                                     //Number of times the local cold data cache was initialized.
              "init_total_ms" : 0,                                  //Total duration for initializing the local cold data cache.
              "init_avg_ms" : 0,                                    //Average duration for initializing the local cold data cache.
              "init_fail_count" : 0                                 //Number of failures in initializing the local cold data cache.
            }
          }
        }
      }
    }

Configuring Parameters
----------------------

+---------------------------------------+---------+---------+-----------------------------------------------------------------+---------+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Configuration Item                    | Type    | Unit    | Value Range                                                     | Scope   | Can Be Dynamically Modified | Description                                                                                                                                                                          |
+=======================================+=========+=========+=================================================================+=========+=============================+======================================================================================================================================================================================+
| low_cost.local_cache.max.capacity     | Integer | ``-``   | The value ranges from 10 to 5000. The default value is **500**. | node    | Yes                         | Maximum number of available cold data caches on a node. Each shard corresponds to a cache object.                                                                                    |
|                                       |         |         |                                                                 |         |                             |                                                                                                                                                                                      |
|                                       |         |         |                                                                 |         |                             | .. note::                                                                                                                                                                            |
|                                       |         |         |                                                                 |         |                             |                                                                                                                                                                                      |
|                                       |         |         |                                                                 |         |                             |    -  If the heap memory usage remains high, decrease the value.                                                                                                                     |
|                                       |         |         |                                                                 |         |                             |    -  If the value of **load_overflow_count** keeps increasing rapidly, increase the value.                                                                                          |
+---------------------------------------+---------+---------+-----------------------------------------------------------------+---------+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| index.low_cost.local_cache.threshold  | Integer | %       | The value ranges from 0 to 100. The default value is **50**.    | index   | Yes                         | Threshold for enabling the local cache of cold data.                                                                                                                                 |
|                                       |         |         |                                                                 |         |                             |                                                                                                                                                                                      |
|                                       |         |         |                                                                 |         |                             | .. note::                                                                                                                                                                            |
|                                       |         |         |                                                                 |         |                             |                                                                                                                                                                                      |
|                                       |         |         |                                                                 |         |                             |    -  If the percentage of date fields is less than the value of this parameter, the cold data of the date type will be cached locally. Otherwise, this parameter is not used.       |
|                                       |         |         |                                                                 |         |                             |    -  If the date fields of the current index occupy most of the data volume of the current index, you are not advised to use this function.                                         |
+---------------------------------------+---------+---------+-----------------------------------------------------------------+---------+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| index.low_cost.local_cache.evict_time | String  | Days    | The value ranges from 1d to 365d. The default value is **30d**. | index   | Yes                         | Wait time before cold data is deleted from local cache. The value is determined based on **index.frozen_date** (time when the freezing is successful).                               |
|                                       |         |         |                                                                 |         |                             |                                                                                                                                                                                      |
|                                       |         |         |                                                                 |         |                             | .. note::                                                                                                                                                                            |
|                                       |         |         |                                                                 |         |                             |                                                                                                                                                                                      |
|                                       |         |         |                                                                 |         |                             |    -  For indexes that have been frozen in old clusters and do not have **index.frozen_date** specified, the value of this parameter is determined based on the index creation time. |
|                                       |         |         |                                                                 |         |                             |    -  You are advised to adjust the deletion time based on the disk usage to avoid high disk usage.                                                                                  |
+---------------------------------------+---------+---------+-----------------------------------------------------------------+---------+-----------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Modifying Parameters
--------------------

-  Run the following command to modify **low_cost.local_cache.max.capacity**:

   .. code-block:: text

      PUT _cluster/settings
       {
         "persistent": {
           "low_cost.local_cache.max.capacity":1000
         }
       }

-  Run the following command to modify **index.low_cost.local_cache.threshold**:

   .. code-block:: text

      PUT es_write_pref2-00000000021/_settings
       {
       "index.low_cost.local_cache.threshold":20
       }

-  Run the following command to modify **index.low_cost.local_cache.evict_time**:

   .. code-block:: text

      PUT es_write_pref2-00000000021/_settings
       {
       "index.low_cost.local_cache.evict_time":"7d"
       }
