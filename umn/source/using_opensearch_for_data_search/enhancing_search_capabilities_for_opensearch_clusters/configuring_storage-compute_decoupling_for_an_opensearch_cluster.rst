:original_name: css_01_0473.html

.. _css_01_0473:

Configuring Storage-Compute Decoupling for an OpenSearch Cluster
================================================================

CSS stores new data as hot data on SSDs to ensure optimal query performance, and historical data as cold data in OBS to cut storage costs.

Scenario
--------

With storage-compute decoupling, you freeze an index and then transfer historical data to OBS for cold data storage. This allows you to reduce storage costs.

In terms of how frequent data is accessed, data can be divided into cold and hot data. Data newly written in is usually hot data, which is usually stored on SSDs for fast retrieval. As time goes by, the data is no longer updated and the query QPS decreases, the data has turned into cold data. By this time, you transfer the data to OBS for less expensive storage. In the meantime, you can still keep hot data on SSDs.


.. figure:: /_static/images/en-us_image_0000002060244820.png
   :alt: **Figure 1** Decoupled storage and compute

   **Figure 1** Decoupled storage and compute

Storage-compute decoupling enables index lifecycle management.

-  Hot indexes are writable, and their data can be retrieved within milliseconds.
-  Frozen indexes store historical data that is rarely accessed for a long time and is dumped to an OBS bucket of CSS for less expensive storage. This also frees up SSDs for hot data. (Users are unaware of the existence of this OBS bucket and cannot check it on the OBS service console. However, the OBS usage does incur additional charges.) It may take seconds or even minutes to retrieve data stored in a frozen index.
-  If historical data in OBS becomes obsolete, you can have it automatically deleted via a predefined policy, reclaiming storage resources.

This section describes how to use storage-compute decoupling after accessing a cluster using OpenSearch Dashboards.

Constraints
-----------

-  Only OpenSearch 1.3.6 clusters support decoupled storage and compute.

-  While an index is being frozen, the system sets the index to the read-only state. Even after the data in the index is dumped to OBS, the index remains read-only and no data can be written into the index.
-  During index freezing, the data in it can still be queried. After the freezing is complete, the index is closed and then re-opened. After that, the index cannot be queried, and the cluster may be in the **red** status for a short time. The index is restored after being opened.
-  Dumping the data in an index to OBS consumes network bandwidth.
-  After an index is frozen, the data in the index is dumped to OBS and the index data on the local disk is deleted. A frozen index has an increased query latency. During aggregation, the latency becomes even longer because the query is complex and a large amount of data needs to be retrieved.
-  A frozen index with data already dumped to OBS cannot be unfrozen. That is, a read-only index cannot be rolled back to writable.
-  In the case of two clusters configured with read/write splitting, the secondary cluster cannot set storage-compute decoupling for indexes synchronized from the primary cluster.
-  The storage-compute decoupling feature depends on OBS. Therefore, you must comply with the restrictions on OBS bandwidth and QPS. If these restrictions are violated, the performance of queries on OBS will deteriorate. For example, the speed of restoring shards and querying data will become slow.

Accessing a Cluster
-------------------

#. Log in to the CSS management console.
#. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column to access OpenSearch Dashboards.
#. Click **Dev Tools** in the navigation tree on the left.

.. _css_01_0473__css_01_0405_section1590610319481:

Freezing an Index
-----------------

Run the following command to dump the data of a specified index to OBS and set its storage class to Standard:

.. code-block:: text

   POST ${index_name}/_freeze_low_cost

.. table:: **Table 1** Request parameters

   ========== ===============================
   Parameter  Description
   ========== ===============================
   index_name Name of the index to be frozen.
   ========== ===============================

Information similar to the following is returned:

.. code-block::

   {
       "freeze_uuid": "pdsRgUtSTymVDWR_HoTGFw"
   }

.. table:: **Table 2** Response parameters

   +-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter   | Description                                                                                                                                                                                                              |
   +=============+==========================================================================================================================================================================================================================+
   | freeze_uuid | ID of the index freezing task. After an index freezing request is submitted, an asynchronous job is started, and an asynchronous job ID is returned, which can be used to query the progress of the index freezing task. |
   +-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Checking the Progress of an Index Freezing Task
-----------------------------------------------

Run the following command to check the progress of the index freezing task:

.. code-block:: text

   GET _freeze_low_cost_progress/${freeze_uuid}

.. table:: **Table 3** Request parameters

   +-------------+------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter   | Description                                                                                                                        |
   +=============+====================================================================================================================================+
   | freeze_uuid | ID of the index freezing task, which is generated during :ref:`Freezing an Index <css_01_0473__css_01_0405_section1590610319481>`. |
   +-------------+------------------------------------------------------------------------------------------------------------------------------------+

Information similar to the following is returned:

.. code-block::

   {

     "stage" : "STARTED",
     "shards_stats" : {
       "INIT" : 0,
       "FAILURE" : 0,
       "DONE" : 0,
       "STARTED" : 3,
       "ABORTED" : 0
     },
     "indices" : {
       "data1" : [
         {
           "uuid" : "7OS-G1-tRke2jHZPlckexg",
           "index" : {
             "name" : "data1",
             "index_id" : "4b5PHXJITLaS6AurImfQ9A",
             "shard" : 2
           },
           "start_ms" : 1611972010852,
           "end_ms" : -1,
           "total_time" : "10.5s",
           "total_time_in_millis" : 10505,
           "stage" : "STARTED",
           "failure" : null,
           "size" : {
             "total_bytes" : 3211446689,
             "finished_bytes" : 222491269,
             "percent" : "6.0%"
           },
           "file" : {
             "total_files" : 271,
             "finished_files" : 12,
             "percent" : "4.0%"
           },
           "rate_limit" : {
             "paused_times" : 1,
             "paused_nanos" : 946460970
           }
         },
         {
           "uuid" : "7OS-G1-tRke2jHZPlckexg",
           "index" : {
             "name" : "data1",
             "index_id" : "4b5PHXJITLaS6AurImfQ9A",
             "shard" : 0
           },
           "start_ms" : 1611972010998,
           "end_ms" : -1,
           "total_time" : "10.3s",
           "total_time_in_millis" : 10359,
           "stage" : "STARTED",
           "failure" : null,
           "size" : {
             "total_bytes" : 3221418186,
             "finished_bytes" : 272347118,
             "percent" : "8.0%"
           },
           "file" : {
             "total_files" : 372,
             "finished_files" : 16,
             "percent" : "4.0%"
           },
           "rate_limit" : {
             "paused_times" : 5,
             "paused_nanos" : 8269016764
           }
         },
         {
           "uuid" : "7OS-G1-tRke2jHZPlckexg",
           "index" : {
             "name" : "data1",
             "index_id" : "4b5PHXJITLaS6AurImfQ9A",
             "shard" : 1
           },
           "start_ms" : 1611972011021,
           "end_ms" : -1,
           "total_time" : "10.3s",
           "total_time_in_millis" : 10336,
           "stage" : "STARTED",
           "failure" : null,
           "size" : {
             "total_bytes" : 3220787498,
             "finished_bytes" : 305789614,
             "percent" : "9.0%"
           },
           "file" : {
             "total_files" : 323,
             "finished_files" : 14,
             "percent" : "4.0%"
           },
           "rate_limit" : {
             "paused_times" : 3,
             "paused_nanos" : 6057933087
           }
         }
       ]
     }
   }

.. table:: **Table 4** Response parameters

   +-----------------------------------+---------------------------------------------------------------------+
   | Parameter                         | Description                                                         |
   +===================================+=====================================================================+
   | stage                             | Task status. Its value can be:                                      |
   |                                   |                                                                     |
   |                                   | -  **INIT**: The instance has just started or is being initialized. |
   |                                   | -  **FAILURE**: failed                                              |
   |                                   | -  **DONE**: complete                                               |
   |                                   | -  **STARTED**: started                                             |
   |                                   | -  **ABORTED**: canceled. This field is reserved.                   |
   +-----------------------------------+---------------------------------------------------------------------+
   | shards_stats                      | Numbers of shards in each state.                                    |
   +-----------------------------------+---------------------------------------------------------------------+
   | indices                           | Index status details.                                               |
   +-----------------------------------+---------------------------------------------------------------------+

.. table:: **Table 5** Return values of **indices**

   +-------------------------+---------------------------------------------------------------------------+
   | Parameter               | Description                                                               |
   +=========================+===========================================================================+
   | uuid                    | UUID of the freezing operation                                            |
   +-------------------------+---------------------------------------------------------------------------+
   | index                   | Index and shard information                                               |
   +-------------------------+---------------------------------------------------------------------------+
   | start_ms                | Start time                                                                |
   +-------------------------+---------------------------------------------------------------------------+
   | end_ms                  | End time. If no end time is specified, the value **-1** is displayed.     |
   +-------------------------+---------------------------------------------------------------------------+
   | total_time              | Time spent                                                                |
   +-------------------------+---------------------------------------------------------------------------+
   | total_time_in_millis    | Time spent, in milliseconds                                               |
   +-------------------------+---------------------------------------------------------------------------+
   | stage                   | Status of the current shard.                                              |
   +-------------------------+---------------------------------------------------------------------------+
   | failure                 | Failure cause. If no failure occurs, **null** is returned.                |
   +-------------------------+---------------------------------------------------------------------------+
   | size.total_bytes        | Size of files to be frozen, in bytes                                      |
   +-------------------------+---------------------------------------------------------------------------+
   | size.finished_bytes     | Frozen bytes                                                              |
   +-------------------------+---------------------------------------------------------------------------+
   | size.percent            | Percentage of frozen bytes                                                |
   +-------------------------+---------------------------------------------------------------------------+
   | file.total_bytes        | Number of files to be frozen                                              |
   +-------------------------+---------------------------------------------------------------------------+
   | file.finished_bytes     | Number of frozen files                                                    |
   +-------------------------+---------------------------------------------------------------------------+
   | file.percent            | Percentage of frozen files                                                |
   +-------------------------+---------------------------------------------------------------------------+
   | rate_limit.paused_times | Number of times that freezing is suspended due to rate limiting           |
   +-------------------------+---------------------------------------------------------------------------+
   | rate_limit.paused_nanos | Duration of freezing task suspension due to rate limiting, in nanoseconds |
   +-------------------------+---------------------------------------------------------------------------+

The following parameters are added to a frozen index. For details, see :ref:`Table 6 <css_01_0473__css_01_0405_en-us_topic_0000001223594408_table1196310214353>`.

.. _css_01_0473__css_01_0405_en-us_topic_0000001223594408_table1196310214353:

.. table:: **Table 6** Frozen index parameters

   +-----------------------+------------------------------------------------------------------------------+
   | Parameter             | Description                                                                  |
   +=======================+==============================================================================+
   | index.frozen_low_cost | Whether an index is frozen. The value is **true**.                           |
   +-----------------------+------------------------------------------------------------------------------+
   | index.blocks.write    | Whether data writing to a frozen index is disallowed. The value is **true**. |
   +-----------------------+------------------------------------------------------------------------------+
   | index.store.type      | Storage type of an index. The value is **obs**.                              |
   +-----------------------+------------------------------------------------------------------------------+

Querying the Index List Based on Freezing Status
------------------------------------------------

Run the following command to query the index list based on freezing status:

.. code-block:: text

   GET _cat/freeze_indices?stage=${STAGE}

.. table:: **Table 7** Request parameters

   +-----------------------------------+------------------------------------------------------------------------------------------+
   | Parameter                         | Description                                                                              |
   +===================================+==========================================================================================+
   | STAGE                             | Index freezing status. The values are as follows:                                        |
   |                                   |                                                                                          |
   |                                   | -  **start**: List of indexes that are being frozen.                                     |
   |                                   | -  **done**: List of indexes that have been frozen.                                      |
   |                                   | -  **unfreeze**: List of indexes that are not frozen.                                    |
   |                                   | -  Empty or other values: List of all indexes that are being frozen or have been frozen. |
   +-----------------------------------+------------------------------------------------------------------------------------------+

Information similar to the following is returned:

.. code-block::

   green open data2 0bNtxWDtRbOSkS4JYaUgMQ 3 0  5 0  7.9kb  7.9kb
   green open data3 oYMLvw31QnyasqUNuyP6RA 3 0 51 0 23.5kb 23.5kb

.. note::

   The parameters and return values of this command are the same as those of open-source OpenSearch's **\_cat/indices**.

Modifying Cache Settings for Cold Data Stored in OBS
----------------------------------------------------

After data is dumped to OBS, some data is cached to reduce access to OBS and improve cluster query performance. Data that is requested for the first time is retrieved from OBS. The retrieved data is then cached in the cluster memory. In response to subsequent queries, the system searches for data in the cache first.

Elasticsearch accesses different files using different methods. The cache system supports multi-level cache and uses blocks of different sizes to cache different files. For example, a large number of small blocks are used to cache .fdx and .tip files, while a small number of large blocks are used to cache .fdt files. The cache configuration can be modified based on service requirements. For details about the configuration items, see :ref:`Table 8 <css_01_0473__css_01_0405_en-us_topic_0000001223594444_table1151755661711>`.

.. _css_01_0473__css_01_0405_en-us_topic_0000001223594444_table1151755661711:

.. table:: **Table 8** Cache configuration items

   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Configuration Item                                   | Type                  | Description                                                                                                                                                                                                                                                                                  |
   +======================================================+=======================+==============================================================================================================================================================================================================================================================================================+
   | low_cost.obs.blockcache.names                        | Array                 | The cache system supports multi-level cache for data of different access granularities. This configuration lists the names of all caches. If this parameter is not set, the system has a cache named **default**. To customize the configuration, ensure there is a cache named **default**. |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **default**                                                                                                                                                                                                                                                                   |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | low_cost.obs.blockcache.<NAME>.type                  | ENUM                  | Cache type, which can be **memory** or **file**.                                                                                                                                                                                                                                             |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | If it is set to **memory**, certain memory capacity will be occupied. If it is set to **file**, cache will be stored on disks. You are advised to use ultra-high I/O disks to improve cache performance.                                                                                     |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **memory**                                                                                                                                                                                                                                                                    |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | low_cost.obs.blockcache.<NAME>.blockshift            | Integer               | Size of each block in the cache. Its value is the number of bytes shifted left. For example, if this parameter is set to **16**, the block size is **2\ 16** bytes, that is, 65536 bytes (64 KB).                                                                                            |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **13** (8 KB)                                                                                                                                                                                                                                                                 |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | low_cost.obs.blockcache.<NAME>.bank.count            | Integer               | Number of cache partitions.                                                                                                                                                                                                                                                                  |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **1**                                                                                                                                                                                                                                                                         |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | low_cost.obs.blockcache.<NAME>.number.blocks.perbank | Integer               | Number of blocks inside each cache partition.                                                                                                                                                                                                                                                |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **8192**                                                                                                                                                                                                                                                                      |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | low_cost.obs.blockcache. <NAME>.exclude.file.types   | Array                 | Extensions of files that are not cached. If the extensions of certain files are neither in the **exclude** list nor in the **include** list, they are stored in the default cache.                                                                                                           |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | low_cost.obs.blockcache. <NAME>.file.types           | Array                 | Extensions of cached files. If the extensions of certain files are neither in the **exclude** list nor in the **include** list, they are stored in the default cache.                                                                                                                        |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index.frozen.obs.max_bytes_per_sec                   | String                | Maximum rate of uploading files to OBS during freezing. It takes effect immediately after you submit configuration.                                                                                                                                                                          |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **150 MB**                                                                                                                                                                                                                                                                    |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | low_cost.obs.index.upload.threshold.use.multipart    | String                | If the file size exceeds the value of this parameter during freezing, the multipart upload function of OBS is used.                                                                                                                                                                          |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **1 GB**                                                                                                                                                                                                                                                                      |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index.frozen.reader.cache.expire.duration.seconds    | Integer               | Timeout duration.                                                                                                                                                                                                                                                                            |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | To reduce the heap memory occupied by frozen indexes, the reader caches data for a period of time after the index shard is started, and stops caching after it times out.                                                                                                                    |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **300s**                                                                                                                                                                                                                                                                      |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | index.frozen.reader.cache.max.size                   | Integer               | Maximum cache size.                                                                                                                                                                                                                                                                          |
   |                                                      |                       |                                                                                                                                                                                                                                                                                              |
   |                                                      |                       | Default value: **100**                                                                                                                                                                                                                                                                       |
   +------------------------------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following is a common cache configuration. It uses two levels of caches: **default** and **large**. The **default** cache uses 64-KB blocks and has a total of 30 x 4096 blocks. It is used to cache non-.fdt files. The **large** cache uses 2-MB blocks and contains 5 x 1000 blocks. It is used to cache .fdx, .dvd, and .tip files.

.. code-block::

   low_cost.obs.blockcache.names: ["default", "large"]
   low_cost.obs.blockcache.default.type: file
   low_cost.obs.blockcache.default.blockshift: 16
   low_cost.obs.blockcache.default.number.blocks.perbank: 4096
   low_cost.obs.blockcache.default.bank.count: 30
   low_cost.obs.blockcache.default.exclude.file.types: ["fdt"]

   low_cost.obs.blockcache.large.type: file
   low_cost.obs.blockcache.large.blockshift: 21
   low_cost.obs.blockcache.large.number.blocks.perbank: 1000
   low_cost.obs.blockcache.large.bank.count: 5
   low_cost.obs.blockcache.large.file.types: ["fdx", "dvd", "tip"]

Querying the Cache Status of Cold Data Stored in OBS
----------------------------------------------------

When the data of a frozen index is queried for the first time, the data retrieved from OBS is automatically cached by the cluster. You can query the cache status of cold data stored in OBS. You can also reset the cache status when you need to debug cluster performance.

#. Query the cache status of cold data stored in OBS.

   -  Query statistics about cold data caching on all nodes:

      .. code-block:: text

         GET _frozen_stats

   -  Query statistics about cold data caching on specified nodes:

      .. code-block:: text

         GET _frozen_stats/${node_id}

      .. table:: **Table 9** Request parameters

         ========= ===========
         Parameter Description
         ========= ===========
         node_id   Node ID
         ========= ===========

   Information similar to the following is returned:

   .. code-block::

      {
        "_nodes" : {
          "total" : 3, //Total number of nodes
          "successful" : 3,  //Successful nodes
          "failed" : 0  //Failed nodes
        },
        "cluster_name" : "css-zzz1", //Cluster name
        "nodes" : {
          "7uwKO38RRoaON37YsXhCYw" : {
            "name" : "css-zzz1-ess-esn-2-1", //Node name
            "transport_address" : "10.0.0.247:9300", //Node transport address
            "host" : "10.0.0.247", //Node host
            "ip" : "10.0.0.247", //Node IP address
            "block_cache" : {
              "default" : {
                "type" : "memory", //Cache type. memory indicates in-memory cache.
                "block_cache_capacity" : 8192, //Cache capacity
                "block_cache_blocksize" : 8192, //Single-block size in the cache, in bytes. In the example, the block size is 8 KB.
                "block_cache_size" : 12, //Cache capacity used.
                "block_cache_hit" : 14,  //Number of cache hits.
                "block_cache_miss" : 0, //Number of cache misses.
                "block_cache_eviction" : 0, //Number of cache evictions.
                "block_cache_store_fail" : 0 //Number of cache storage failures, which occur when the cache is full.
              }
            },
            "obs_stats" : {
              "list" : {
                "obs_list_count" : 17, //Number of times the OBS list API was called.
                "obs_list_ms" : 265, //Total length of time spent calling the OBS list API.
                "obs_list_avg_ms" : 15 //Average time spent calling the OBS list API.
              },
              "get_meta" : {
                "obs_get_meta_count" : 79, //Number of times the OBS get metadata API was called.
                "obs_get_meta_ms" : 183, //Total length of time spent calling the OBS get metadata API.
                "obs_get_meta_avg_ms" : 2 //Average time spent calling the OBS get metadata API.
              },
              "get_obj" : {
                "obs_get_obj_count" : 12, //Number of times the OBS get object API was called.
                "obs_get_obj_ms" : 123, //Total length of time spent calling the OBS get object API.
                "obs_get_obj_avg_ms" : 10 //Average time spent calling the OBS get object API.
              },
              "put_obj" : {
                "obs_put_obj_count" : 12, //Number of times the OBS put object API was called.
                "obs_put_obj_ms" : 2451, //Total length of time spent calling the OBS put object API.
                "obs_put_obj_avg_ms" : 204 //Average time spent calling the OBS put object API.
              },
              "obs_op_total" : {
                "obs_op_total_ms" : 3022, //Total length of time spent calling OBS APIs.
                "obs_op_total_count" : 120, //Total number of times calling OBS APIs.
                "obs_op_avg_ms" : 25 //Average time spent calling OBS APIs.
              }
            },
            "reader_cache" : {
              "hit_count" : 0,
              "miss_count" : 1,
              "load_success_count" : 1,
              "load_exception_count" : 0,
              "total_load_time" : 291194714,
              "eviction_count" : 0
            }
          },
          "73EDpEqoQES749umJqxOzQ" : {
            "name" : "css-zzz1-ess-esn-3-1",
            "transport_address" : "10.0.0.201:9300",
            "host" : "10.0.0.201",
            "ip" : "10.0.0.201",
            "block_cache" : {
              "default" : {
                "type" : "memory",
                "block_cache_capacity" : 8192,
                "block_cache_blocksize" : 8192,
                "block_cache_size" : 12,
                "block_cache_hit" : 14,
                "block_cache_miss" : 0,
                "block_cache_eviction" : 0,
                "block_cache_store_fail" : 0
              }
            },
            "obs_stats" : {
              "list" : {
                "obs_list_count" : 17,
                "obs_list_ms" : 309,
                "obs_list_avg_ms" : 18
              },
              "get_meta" : {
                "obs_get_meta_count" : 79,
                "obs_get_meta_ms" : 216,
                "obs_get_meta_avg_ms" : 2
              },
              "get_obj" : {
                "obs_get_obj_count" : 12,
                "obs_get_obj_ms" : 140,
                "obs_get_obj_avg_ms" : 11
              },
              "put_obj" : {
                "obs_put_obj_count" : 12,
                "obs_put_obj_ms" : 1081,
                "obs_put_obj_avg_ms" : 90
              },
              "obs_op_total" : {
                "obs_op_total_ms" : 1746,
                "obs_op_total_count" : 120,
                "obs_op_avg_ms" : 14
              }
            },
            "reader_cache" : {
              "hit_count" : 0,
              "miss_count" : 1,
              "load_success_count" : 1,
              "load_exception_count" : 0,
              "total_load_time" : 367179751,
              "eviction_count" : 0
            }
          },
          "EF8WoLCUQbqJl1Pkqo9-OA" : {
            "name" : "css-zzz1-ess-esn-1-1",
            "transport_address" : "10.0.0.18:9300",
            "host" : "10.0.0.18",
            "ip" : "10.0.0.18",
            "block_cache" : {
              "default" : {
                "type" : "memory",
                "block_cache_capacity" : 8192,
                "block_cache_blocksize" : 8192,
                "block_cache_size" : 12,
                "block_cache_hit" : 14,
                "block_cache_miss" : 0,
                "block_cache_eviction" : 0,
                "block_cache_store_fail" : 0
              }
            },
            "obs_stats" : {
              "list" : {
                "obs_list_count" : 17,
                "obs_list_ms" : 220,
                "obs_list_avg_ms" : 12
              },
              "get_meta" : {
                "obs_get_meta_count" : 79,
                "obs_get_meta_ms" : 139,
                "obs_get_meta_avg_ms" : 1
              },
              "get_obj" : {
                "obs_get_obj_count" : 12,
                "obs_get_obj_ms" : 82,
                "obs_get_obj_avg_ms" : 6
              },
              "put_obj" : {
                "obs_put_obj_count" : 12,
                "obs_put_obj_ms" : 879,
                "obs_put_obj_avg_ms" : 73
              },
              "obs_op_total" : {
                "obs_op_total_ms" : 1320,
                "obs_op_total_count" : 120,
                "obs_op_avg_ms" : 11
              }
            },
            "reader_cache" : {
              "hit_count" : 0,
              "miss_count" : 1,
              "load_success_count" : 1,
              "load_exception_count" : 0,
              "total_load_time" : 235706838,
              "eviction_count" : 0
            }
          }
        }
      }

#. Run the following command to reset the cache status:

   .. code-block:: text

      POST _frozen_stats/reset

   .. note::

      This command is used to debug performance issues. If you reset the cache status and then run the cache query command, you can check the accurate cache command status. It is not advisable to use this command during service running.

   Information similar to the following is returned:

   .. code-block::

      {
        "_nodes" : {
          "total" : 1,
          "successful" : 1,
          "failed" : 0
        },
        "cluster_name" : "Es-0325-007_01",
        "nodes" : {
          "mqTdk2YRSPyOSXfesREFSg" : {
            "result" : "ok"
          }
        }
      }

Improving Cold Data Query Performance
-------------------------------------

When cold data is queried on the **Discover** page of OpenSearch Dashboards for the first time, all data needs to be retrieved from OBS because there is no cache. If a large number of documents need to be returned, it takes a long time to retrieve the corresponding time fields and file metadata from OBS. By caching this part of data within the cluster, you can significantly improve query performance. This is how CSS improves the query performance for cold data. Local cache settings are preset. You can modify them as needed. You can also view the local cache settings.

#. Modify local cache settings for cold data.

   .. table:: **Table 10** Local cache configuration items

      +---------------------------------------+-------------+-------------+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configuration Item                    | Type        | scope       | Can Be Changed Dynamically | Description                                                                                                                                                                                                                                    |
      +=======================================+=============+=============+============================+================================================================================================================================================================================================================================================+
      | low_cost.local_cache.max.capacity     | Integer     | node        | Yes                        | Maximum number of available cold data caches on a node. Each shard corresponds to a cache object.                                                                                                                                              |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | Value range: 10-5000                                                                                                                                                                                                                           |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | Default value: **500**                                                                                                                                                                                                                         |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | .. note::                                                                                                                                                                                                                                      |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            |    -  If the heap memory usage remains high, you can decrease this value.                                                                                                                                                                      |
      |                                       |             |             |                            |    -  If the value of **load_overflow_count** keeps increasing rapidly, increase this value.                                                                                                                                                   |
      +---------------------------------------+-------------+-------------+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | index.low_cost.local_cache.threshold  | Integer     | index       | Yes                        | Threshold for enabling the local cache of cold data.                                                                                                                                                                                           |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | -  If in an index, the percentage of fields whose type is **date** is less than the value of this parameter, you can enable local cache for cold data of the **date** type. Otherwise, do not use it.                                          |
      |                                       |             |             |                            | -  If date fields account for the vast majority of all fields in the current index, you are advised not to use this setting.                                                                                                                   |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | Unit: %                                                                                                                                                                                                                                        |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | Value range: **0** to **100**                                                                                                                                                                                                                  |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | Default value: **50**                                                                                                                                                                                                                          |
      +---------------------------------------+-------------+-------------+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | index.low_cost.local_cache.evict_time | String      | index       | Yes                        | Retention duration for cold data in the local cache. The value is determined based on index.frozen_date (time when the freezing is successful). If index.frozen_date is unavailable, the value is determined based on the index creation time. |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | Unit: days                                                                                                                                                                                                                                     |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | Value range: 1 to 365 days                                                                                                                                                                                                                     |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | Default value: **30d**                                                                                                                                                                                                                         |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            | .. note::                                                                                                                                                                                                                                      |
      |                                       |             |             |                            |                                                                                                                                                                                                                                                |
      |                                       |             |             |                            |    You are advised to adjust the retention duration based on your disk usage.                                                                                                                                                                  |
      +---------------------------------------+-------------+-------------+----------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

#. Query the local cache information for cold data.

   -  Query statistics and metrics about cold data caching on all nodes:

      .. code-block:: text

         GET /_frozen_stats/local_cache

   -  Query statistics and metrics about cold data caching on specified nodes:

      .. code-block:: text

         GET /_frozen_stats/local_cache/{nodeId}

      **{nodeId}** indicates the node ID.

   Information similar to the following is returned:

   .. code-block::

      {
         "_nodes" : {
           "total" : 1,
           "successful" : 1,
           "failed" : 0
         },
         "cluster_name" : "opensearch",
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
                 "load_fail_count" : 0,                               //Number of failures for loading cold data from the local cache
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

Querying the Real-Time Rates of OBS in Handling Cold Data
---------------------------------------------------------

To help you understand how the storage-compute decoupling plug-in is working with OBS, an API for collecting statistics on the real-time rates of OBS has been added, and the real-time rates are recorded in the index **.freeze_obs_rate-YYYY.mm.dd**.

Calculation method: The average OBS operation rates in the last 5 seconds are calculated every 5 seconds.

The system index **.freeze_obs_rate-YYYY.mm.dd** records statistics on OBS real-time operation rates, helping you understand relevant trends about the OBS that stores cold data. The default retention period of the index is 30 days.

#. Querying the real-time rates of OBS in handling cold data.

   -  Run the following command to query the real-time OBS rates on all nodes:

      .. code-block:: text

         GET _frozen_stats/obs_rate

   -  Run the following command to query the real-time OBS rates on specified nodes:

      .. code-block:: text

         GET _frozen_stats/obs_rate/{nodeId}

      **{nodeId}** indicates the node ID.

   Example response:

   .. code-block::

      {
         "_nodes" : {
           "total" : 1,
           "successful" : 1,
           "failed" : 0
         },
         "cluster_name" : "opensearch",
         "nodes" : {
           "dflDvcSwTJ-fkiIlT2zE3A" : {
             "name" : "node-1",
             "transport_address" : "127.0.0.1:9300",
             "host" : "127.0.0.1",
             "ip" : "127.0.0.1",
             "update_time" : 1671777600482,                            // Time when the current statistics were updated.
             "obs_rate" : {
               "list_op_rate" : 0.0,                                   // Rate of OBS list operations. Unit: times/s.
               "get_meta_op_rate" : 0.0,                               // Rate of OBS get meta operations. Unit: times/s.
               "get_obj_op_rate" : 0.0,                                // Rate of OBS get operations. Unit: times/s.
               "put_op_rate" : 0.0,                                    // Rate of OBS put operations. Unit: times/s.
               "obs_total_op_rate" : 0.0,                              // Rate of all OBS operations. Unit: times/s.
               "obs_upload_rate" : "0.0 MB/s",                         // Data upload rate of OBS, in MB/s.
               "obs_download_rate" : "0.0 MB/s"                        // Data download rate of OBS, in MB/s.
             }
           }
         }
       }

#. Modify the retention period of the **.freeze_obs_rate-YYYY.mm.dd** index that stores the OBS real-time rates. The default retention period of indexes is 30 days.

   Run the following command to change the index retention period to seven days:

   .. code-block:: text

      PUT _cluster/settings
       {
         "persistent": {
           "low_cost.obs_rate_index.evict_time":  "7d"
         }
       }

   .. table:: **Table 11** Configuration items

      +------------------------------------+-------------+-------------+----------------------------+--------------------------------------------------------------------+
      | Configuration Item                 | Type        | scope       | Can Be Changed Dynamically | Description                                                        |
      +====================================+=============+=============+============================+====================================================================+
      | low_cost.obs_rate_index.evict_time | String      | node        | Yes                        | The retention period of the **.freeze_obs_rate-YYYY.mm.dd** index. |
      |                                    |             |             |                            |                                                                    |
      |                                    |             |             |                            | -  Value range: 1 to 365 days                                      |
      |                                    |             |             |                            | -  Default value: **30d**                                          |
      |                                    |             |             |                            | -  Unit: days                                                      |
      +------------------------------------+-------------+-------------+----------------------------+--------------------------------------------------------------------+
