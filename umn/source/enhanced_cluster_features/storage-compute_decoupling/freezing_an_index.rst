:original_name: en-us_topic_0000001528299569.html

.. _en-us_topic_0000001528299569:

Freezing an Index
=================

Precautions
-----------

-  Before freezing an index, ensure no data is being written to it. The index will be set to read only before being frozen, and data write will fail.
-  After an index is frozen:

   -  It becomes read-only.
   -  The index data will be dumped to OBS. This process occupies network bandwidth.
   -  The query latency of a dumped index will increase. During aggregation, the latency of processing complex queries and reading a large volume of data is long.
   -  It cannot be unfrozen. That is, a read-only index cannot be changed to writable.
   -  After the freezing is complete, the index data in your local disks will be deleted.

Procedure
---------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. Click **Dev Tools** in the navigation tree on the left.

#. .. _en-us_topic_0000001528299569__en-us_topic_0000001223594408_li79781447687:

   Run the following command to freeze a specified index and dump it to OBS:

   .. code-block:: text

      POST ${index_name}/_freeze_low_cost

   .. table:: **Table 1** Parameter description

      ========== ===============================
      Parameter  Description
      ========== ===============================
      index_name Name of the index to be frozen.
      ========== ===============================

   Information similar to the following is displayed:

   .. code-block::

      {
          "freeze_uuid": "pdsRgUtSTymVDWR_HoTGFw"
      }

   .. table:: **Table 2** Response parameter

      +-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter   | Description                                                                                                                                                                                      |
      +=============+==================================================================================================================================================================================================+
      | freeze_uuid | After an index freezing request is submitted, an asynchronous job will be started. The request returns the asynchronous job ID, which can be used to query the progress of the asynchronous job. |
      +-------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. note::

      After an index freezing request is submitted, data cannot be written to the index. During the index freezing, query requests are not affected. After the freezing is complete, the index is closed and then opened. During this period, the index cannot be queried, and the cluster may be in the **red** status for a short time. The index is restored after being opened.

#. Run the following command to check the freezing task progress:

   .. code-block:: text

      GET _freeze_low_cost_progress/${freeze_uuid}

   .. table:: **Table 3** Parameter description

      +-------------+---------------------------------------------------------------------------------------------------------------------------------+
      | Parameter   | Description                                                                                                                     |
      +=============+=================================================================================================================================+
      | freeze_uuid | Asynchronous task ID, which is obtained in :ref:`4 <en-us_topic_0000001528299569__en-us_topic_0000001223594408_li79781447687>`. |
      +-------------+---------------------------------------------------------------------------------------------------------------------------------+

   Information similar to the following is displayed:

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
      | stage                             | Status. Its value can be:                                           |
      |                                   |                                                                     |
      |                                   | -  **INIT**: The instance has just started or is being initialized. |
      |                                   | -  **FAILURE**: failed                                              |
      |                                   | -  **DONE**: complete                                               |
      |                                   | -  **STARTED**: started                                             |
      |                                   | -  **ABORTED**: Canceled. This field is reserved.                   |
      +-----------------------------------+---------------------------------------------------------------------+
      | shards_stats                      | Numbers of shards in each state.                                    |
      +-----------------------------------+---------------------------------------------------------------------+
      | indices                           | Index status details.                                               |
      +-----------------------------------+---------------------------------------------------------------------+

   .. table:: **Table 5** Return values of **indices**

      +-------------------------+------------------------------------------------------------------------+
      | Parameter               | Description                                                            |
      +=========================+========================================================================+
      | uuid                    | UUID of the freezing operation                                         |
      +-------------------------+------------------------------------------------------------------------+
      | index                   | Index and shard information                                            |
      +-------------------------+------------------------------------------------------------------------+
      | start_ms                | Start time                                                             |
      +-------------------------+------------------------------------------------------------------------+
      | end_ms                  | End time. If no end time is specified, the value **-1** is displayed.  |
      +-------------------------+------------------------------------------------------------------------+
      | total_time              | Time spent                                                             |
      +-------------------------+------------------------------------------------------------------------+
      | total_time_in_millis    | Time spent, in milliseconds                                            |
      +-------------------------+------------------------------------------------------------------------+
      | stage                   | Status of the current shard.                                           |
      +-------------------------+------------------------------------------------------------------------+
      | failure                 | Failure cause. If no failure occurs, **null** is displayed.            |
      +-------------------------+------------------------------------------------------------------------+
      | size.total_bytes        | Size of files to be frozen, in bytes                                   |
      +-------------------------+------------------------------------------------------------------------+
      | size.finished_bytes     | Frozen bytes                                                           |
      +-------------------------+------------------------------------------------------------------------+
      | size.percent            | Percentage of frozen bytes                                             |
      +-------------------------+------------------------------------------------------------------------+
      | file.total_bytes        | Number of files to be frozen                                           |
      +-------------------------+------------------------------------------------------------------------+
      | file.finished_bytes     | Number of frozen files                                                 |
      +-------------------------+------------------------------------------------------------------------+
      | file.percent            | Percentage of frozen files                                             |
      +-------------------------+------------------------------------------------------------------------+
      | rate_limit.paused_times | Number of times that freezing is suspended due to rate limit           |
      +-------------------------+------------------------------------------------------------------------+
      | rate_limit.paused_nanos | Duration of freezing task suspension due to rate limit, in nanoseconds |
      +-------------------------+------------------------------------------------------------------------+

   The following parameters are added to a frozen index. For details, see :ref:`Table 6 <en-us_topic_0000001528299569__en-us_topic_0000001223594408_table1196310214353>`.

   .. _en-us_topic_0000001528299569__en-us_topic_0000001223594408_table1196310214353:

   .. table:: **Table 6** Frozen index parameters

      +-----------------------+------------------------------------------------------------------------------------+
      | Parameter             | Description                                                                        |
      +=======================+====================================================================================+
      | index.frozen_low_cost | Indicates whether an index is frozen. The value is **true**.                       |
      +-----------------------+------------------------------------------------------------------------------------+
      | index.blocks.write    | Indicates whether data writing is denied in a frozen index. The value is **true**. |
      +-----------------------+------------------------------------------------------------------------------------+
      | index.store.type      | Storage type of an index. The value is **obs**.                                    |
      +-----------------------+------------------------------------------------------------------------------------+

#. After an index is frozen, its data will be cached. Run the following command to check the current cache status: For details about the cache, see :ref:`Configuring Cache <en-us_topic_0000001528379309>`.

   .. code-block:: text

      GET _frozen_stats
      GET _frozen_stats/${node_id}

   .. table:: **Table 7** Parameter description

      +-----------+------------------------------------------------------------------+
      | Parameter | Description                                                      |
      +===========+==================================================================+
      | node_id   | Node ID, which can be used to obtain the cache status of a node. |
      +-----------+------------------------------------------------------------------+

   Information similar to the following is displayed:

   .. code-block::

      {
        "_nodes" : {
          "total" : 3,
          "successful" : 3,
          "failed" : 0
        },
        "cluster_name" : "css-zzz1",
        "nodes" : {
          "7uwKO38RRoaON37YsXhCYw" : {
            "name" : "css-zzz1-ess-esn-2-1",
            "transport_address" : "10.0.0.247:9300",
            "host" : "10.0.0.247",
            "ip" : "10.0.0.247",
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
                "obs_list_ms" : 265,
                "obs_list_avg_ms" : 15
              },
              "get_meta" : {
                "obs_get_meta_count" : 79,
                "obs_get_meta_ms" : 183,
                "obs_get_meta_avg_ms" : 2
              },
              "get_obj" : {
                "obs_get_obj_count" : 12,
                "obs_get_obj_ms" : 123,
                "obs_get_obj_avg_ms" : 10
              },
              "put_obj" : {
                "obs_put_obj_count" : 12,
                "obs_put_obj_ms" : 2451,
                "obs_put_obj_avg_ms" : 204
              },
              "obs_op_total" : {
                "obs_op_total_ms" : 3022,
                "obs_op_total_count" : 120,
                "obs_op_avg_ms" : 25
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

   Information similar to the following is displayed:

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

   .. note::

      This command is used to debug performance issues. If you reset the cache status and run this command, you can check the cache command status. You do not need to run this command during service running.

#. Run the following command to check all the frozen indexes:

   .. code-block:: text

      GET _cat/freeze_indices?stage=${STAGE}

   .. table:: **Table 8** Parameter description

      +-----------------------------------+-----------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                             |
      +===================================+=========================================================================================+
      | STAGE                             | Its value can be:                                                                       |
      |                                   |                                                                                         |
      |                                   | -  **start**: List of indexes that are being frozen                                     |
      |                                   | -  **done**: List of indexes that have been frozen                                      |
      |                                   | -  **unfreeze**: List of indexes that are not frozen                                    |
      |                                   | -  Empty or other values: List of all indexes that are being frozen or have been frozen |
      +-----------------------------------+-----------------------------------------------------------------------------------------+

   Information similar to the following is displayed:

   .. code-block::

      green open data2 0bNtxWDtRbOSkS4JYaUgMQ 3 0  5 0  7.9kb  7.9kb
      green open data3 oYMLvw31QnyasqUNuyP6RA 3 0 51 0 23.5kb 23.5kb

   .. note::

      The parameters and return values of this command are the same as those of **\_cat/indices** of Elasticsearch.
