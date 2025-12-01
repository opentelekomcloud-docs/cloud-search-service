:original_name: css_02_0043.html

.. _css_02_0043:

How Do I Query the Snapshot Information of a CSS Cluster?
=========================================================

You can query snapshot information only if cluster snapshots are enabled and some snapshots have been created.

You can check them on the CSS management console or query them by running commands on Kibana or OpenSearch Dashboards.

Querying Snapshots on the CSS Management Console
------------------------------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, expand **Clusters**. Select a cluster type based on the target cluster. The cluster list is displayed.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Click the **Cluster Snapshots** tab.
#. In the cluster snapshot task list, click the target snapshot name, and check snapshot information in the displayed dialog box.

Querying Snapshots by Running Commands
--------------------------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, expand **Clusters**. Select a cluster type based on the target cluster. The cluster list is displayed.

#. For an Elasticsearch cluster, click **Kibana** in the **Operation** column to log in to Kibana. For an OpenSearch cluster, click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. Expand the menu in the upper-left corner, and choose **Dev Tools**.

#. Run the following command to query the snapshot repository information, that is, the basic cluster snapshot settings.

   .. code-block:: text

      GET _snapshot/_all

   Example response:

   .. code-block::

      {
        "repo_auto": {
          "type": "obs",
          "settings": {
            "bucket": "123xxx",   // OBS bucket name
            "chunk_size": "2g",   // Chunk size in snapshots (unit: GB)
            "endpoint": "obs.xxx.example.com:443",    // OBS VPC endpoint
            "max_restore_bytes_per_sec": "0MB",   // Maximum recovery rate (per second)
            "compress": "true",   // Whether to enable data compression
            "base_path": "css_repository/css-xxx",    // Backup path
            "region": "xxx",      // Region
            "max_snapshot_bytes_per_sec": "40MB"      // Maximum backup rate (per second)
          }
        }
      }

#. Run the following command to query the snapshot list:

   .. code-block:: text

      GET _snapshot/repo_auto/_all

   Example output (two snapshots are returned):

   .. code-block::

      {
        "snapshots": [
          {
            "snapshot": "snapshot-2dc3",       // Snapshot name
            "uuid": "VW5y2NBJS9iPh7YcGLxxxx",  // Snapshot ID
            "version_id": xxxxxxx,        // Internal cluster version
            "version": "x.x.x",       // Cluster version
            "indices": [              // Backed up indexes
              ".opendistro_security"
            ],
            "data_streams": [ ],          // Data streams
            "include_global_state": true,     // Whether to include the global cluster status
            "state": "SUCCESS",           // Snapshot status
            "start_time": "2025-08-30T01:41:57.068Z",  // Snapshot start time
            "start_time_in_millis": 1756518117068,    // Snapshot start time in milliseconds
            "end_time": "2025-08-30T01:41:57.469Z",   // Snapshot end time
            "end_time_in_millis": 1756518117469,      // Snapshot end time in milliseconds
            "duration_in_millis": 401,            // Snapshot creation duration (from start to completion) in milliseconds
            "failures": [ ],                  // Failed shards during snapshot creation
            "shards": {                   // Shard statistics
              "total": 1,                     // Total number of shards
              "failed": 0,                    // Number of failed shards
              "successful": 1                 // Number of successful shards
            }
          },
          {
            "snapshot": "snapshot-dd37",
            "uuid": "FD4VcooLS8yjPY3w0-x-xx",
            "version_id": xxxxxxx,
            "version": "x.x.x",
            "indices": [
              ".kibana",
              ".opendistro_security"
            ],
            "data_streams": [ ],
            "include_global_state": true,
            "state": "SUCCESS",
            "start_time": "2025-08-30T01:54:55.750Z",
            "start_time_in_millis": 1756518895750,
            "end_time": "2025-08-30T01:54:55.950Z",
            "end_time_in_millis": 1756518895950,
            "duration_in_millis": 200,
            "failures": [ ],
            "shards": {
              "total": 2,
              "failed": 0,
              "successful": 2
            }
          }
        ]
      }

   To query information about a specified snapshot, run the following command:

   .. code-block:: text

      GET _snapshot/repo_auto/{snapshot_name}

   Replace *snapshot_name* with the actual snapshot name. Wildcard matching is supported.

#. (Optional) Run the following command to delete a specified snapshot:

   .. code-block:: text

      DELETE _snapshot/repo_auto/{snapshot_name}

   Exercise caution when choosing snapshots to delete.
