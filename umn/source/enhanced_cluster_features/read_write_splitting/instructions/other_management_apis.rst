:original_name: en-us_topic_0000001528499169.html

.. _en-us_topic_0000001528499169:

Other Management APIs
=====================

-  **Querying the created patterns**.

   This API is used to query the pattern list and query a specified pattern by name.

   An example request is as follows:

   .. code-block:: text

      GET auto_sync/pattern
      GET auto_sync/pattern/{pattern_name}

   The following is an example of the response:

   .. code-block::

      {
        "patterns" : [
          {
            "name" : "pattern1",
            "pattern" : {
              "remote_cluster" : "leader",
              "remote_index_patterns" : [
                "log*"
              ],
              "local_index_pattern" : "{{remote_index}}-sync",
              "settings" : { }
            }
          }
        ]
      }

-  **Deleting a created schema**.

   This API is used to delete a specified pattern.

   An example request is as follows:

   .. code-block:: text

      DELETE auto_sync/pattern/{pattern_name}

-  **Obtaining the automatic synchronization status**.

   This API is used to obtain the synchronization status of matched indexes.

   An example request is as follows:

   .. code-block:: text

      GET auto_sync/stats

   The following is an example of the response:

   .. code-block::

      {
        "success_count" : 3,
        "failed_count" : 0,
        "failed_remote_cluster_state_requests_count" : 0,
        "last_fail_exception" : { },
        "last_fail_remote_cluster_requests_exception" : { }
      }

-  **Obtaining the synchronization status of the index that is being synchronized**.

   An example request is as follows:

   .. code-block:: text

      GET {index_name}/sync_stats

   The following is an example of the response:

   .. code-block::

      {
        "indices" : {
          "data1_follower" : {
            "shards" : {
              "0" : [
                {
                  "primary" : false,
                  "total_synced_times" : 27,
                  "total_empty_times" : 25,
                  "total_synced_files" : 4,
                  "total_synced_bytes" : 3580,
                  "total_paused_nanos" : 0,
                  "total_paused_times" : 0,
                  "current" : {
                    "files_count" : 0,
                    "finished_files_count" : 0,
                    "bytes" : 0,
                    "finished_bytes" : 0
                  }
                },
                {
                  "primary" : true,
                  "total_synced_times" : 28,
                  "total_empty_times" : 26,
                  "total_synced_files" : 20,
                  "total_synced_bytes" : 17547,
                  "total_paused_nanos" : 0,
                  "total_paused_times" : 0,
                  "current" : {
                    "files_count" : 0,
                    "finished_files_count" : 0,
                    "bytes" : 0,
                    "finished_bytes" : 0
                  }
                }
              ]
            }
          }
        }
      }

-  **Changing the synchronization period**.

   The synchronization period is 30 seconds by default and can be modified.

   An example request is as follows (change the synchronization period to 2 seconds):

   .. code-block:: text

      PUT {index_name}/_settings
      {
        "index.remote_sync.sync_interval": "2s"
      }

-  **Enabling forcible synchronization**

   By default, the plug-in determines whether to synchronize metadata based on whether the number of documents in the index of the primary cluster changes. If the primary cluster only updates documents and the number of documents remains unchanged, the plug-in does not synchronize the updates to the secondary cluster. The configuration can be modified. After this function is enabled, the index metadata of the primary cluster is forcibly synchronized to the secondary cluster in each synchronization period.

   The following is an example of enabling forcible synchronization:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "remote_sync.force_synchronize": true
        }
      }
