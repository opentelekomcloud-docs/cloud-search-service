:original_name: css_01_0410.html

.. _css_01_0410:

Configuring Read/Write Splitting Between Two Elasticsearch Clusters
===================================================================

Scenario
--------

Data written to the primary cluster (**Leader**) is automatically synchronized to the secondary cluster (**Follower**). This allows data to be queried from the secondary cluster, improving query performance while alleviating the pressure of the primary cluster. If the primary cluster is unable to provide services, a primary/secondary switchover can be performed to use the secondary cluster to handle write and query requests, ensuring service continuity.


.. figure:: /_static/images/en-us_image_0000001981763825.jpg
   :alt: **Figure 1** Two application scenarios for read/write splitting

   **Figure 1** Two application scenarios for read/write splitting

Scenario 1 (left in the figure): Data is written into the primary cluster but queried from the secondary cluster, alleviating pressure for both clusters.

Scenario 2 (right in the figure): When the primary cluster fails, the secondary cluster takes over to ensure service continuity.

Constraints
-----------

-  Only Elasticsearch 7.6.2 and Elasticsearch 7.10.2 clusters support read/write splitting.
-  The versions of the primary and secondary clusters must be kept consistent, or errors may occur.

Prerequisites
-------------

Two clusters of the same version have been created. One functions as the primary cluster, and the other the secondary cluster. The secondary cluster must be able to access the REST API (default port: 9200) of the primary cluster.

.. _css_01_0410__section1023014371242:

Connecting the Primary and Secondary Clusters
---------------------------------------------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the secondary cluster and click **Access Kibana** in the **Operation** column.

#. Click **Dev Tools** in the navigation tree on the left.

#. Run the following command to configure information about the primary cluster in the secondary cluster:

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent" : {
          "cluster" : {
            "remote.rest" : {
              "leader1" : {
                "seeds" : [
                  "http://10.0.0.1:9200",
                  "http://10.0.0.2:9200",
                  "http://10.0.0.3:9200"
                ] ,
                  "username": "elastic",
                  "password": "*****"
              }
            }
          }
        }
      }

   .. table:: **Table 1** Request body parameters

      +-----------+------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter | Description                                                                                                                        |
      +===========+====================================================================================================================================+
      | *leader1* | Name of the primary cluster configuration task, which is user-defined and will be used for configuring read/write splitting later. |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------+
      | seeds     | Address for accessing the primary cluster. When HTTPS is enabled for the cluster, the URL schema must use HTTPS.                   |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------+
      | username  | Username of the primary cluster. This parameter is required only when security mode is enabled for the primary cluster.            |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------+
      | password  | Password of the primary cluster. This parameter is required only when security mode is enabled for the primary cluster.            |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------+

   Example response:

   .. code-block::

      {
        "acknowledged" : true,  //Whether the operation is successful
        "persistent" : {
          "cluster" : {
            "remote" : {
              "rest" : {
                "leader1" : {
                  "seeds" : [
                  "http://10.0.0.1:9200",
                  "http://10.0.0.2:9200",
                  "http://10.0.0.3:9200"
                  ] ,
                  "username": "elastic",
                   "password": "*****"
                }
              }
            }
          }
        },
        "transient" : { }
      }

#. After the configuration is complete, run the following command in the secondary cluster to check the connection between the secondary and primary clusters:

   .. code-block:: text

      GET _remote/rest/info

   Example response:

   .. code-block::

      {
        "leader1" : {
          "connected" : true  //The two clusters are connected.
        }
      }

.. _css_01_0410__section97051931358:

Index Synchronization
---------------------

There are two ways to synchronize indexes: specified index synchronization and matching index synchronization.

During synchronization, indexes in the secondary cluster become read-only. The synchronization is performed periodically. The default synchronization interval is 30 seconds. For how to change it, see :ref:`Changing the Synchronization Interval <css_01_0410__section94973244119>`.

**Synchronizing Specified Indexes**

-  Run the following command in the secondary cluster to synchronize a single index from the primary cluster to the secondary cluster without modifying index settings:

   .. code-block:: text

      PUT start_remote_sync
      {
        "remote_cluster": "leader1",
        "remote_index": "data1_leader",
        "local_index": "data1_follower"
      }

-  Run the following command in the secondary cluster to synchronize a single index from the primary cluster to the secondary cluster while modifying some of the index settings—enabling synchronization of index settings:

   .. code-block:: text

      PUT start_remote_sync
      {
        "remote_cluster": "leader1",
        "remote_index": "data1_leader",
        "local_index": "data1_follower",
        "settings": {
          "number_of_replicas": 4
        },
        "settings_sync_enable": true,
        "settings_sync_patterns": ["*"],
        "settings_sync_exclude_patterns": ["index.routing.allocation.*"],
        "alias_sync_enable": true,
        "state_sync_enable": true
      }

   .. note::

      The following index configuration items cannot be modified: **number_of_shards**, **version.created**, **uuid**, **creation_date**, and **soft_deletes.enabled**.

.. table:: **Table 2** Request body parameters

   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                      | Description                                                                                                                                                                                                                                     |
   +================================+=================================================================================================================================================================================================================================================+
   | remote_cluster                 | Name of the primary cluster configuration task, which was set in :ref:`Connecting the Primary and Secondary Clusters <css_01_0410__section1023014371242>`. **leader1** was set in our example.                                                  |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | remote_index                   | Name of the index to be synchronized in the primary cluster                                                                                                                                                                                     |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | local_index                    | Index name in the secondary cluster                                                                                                                                                                                                             |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings                       | Index settings to be synchronized                                                                                                                                                                                                               |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings_sync_enable           | Whether to enable synchronization of index settings in the primary cluster. The default value is **false**.                                                                                                                                     |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings_sync_patterns         | Prefix of primary cluster index settings to be synchronized. The default value is **\***. This parameter takes effect when **settings_sync_enable** is set to **true**. The index settings configured in **settings** will not be synchronized. |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings_sync_exclude_patterns | Prefix of primary cluster index settings not to be synchronized. The default value is empty. This parameter is valid only when **settings_sync_enable** is set to **true**.                                                                     |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | alias_sync_enable              | Whether to enable index alias synchronization in the primary cluster. The default value is **false**.                                                                                                                                           |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | state_sync_enable              | Whether to enable index status synchronization in the primary cluster. The default value is **false**.                                                                                                                                          |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

**Matching Index Synchronization**

-  Run the following command in the secondary cluster to create a pattern-matching index synchronization policy, which synchronizes matched indexes from the primary cluster to the secondary cluster:

   .. code-block:: text

      PUT auto_sync/pattern/${PATTERN}
      {
       "remote_cluster": "leader1",
       "remote_index_patterns": "log*",
       "local_index_pattern": "{{remote_index}}-sync",
       "apply_exist_index": true
      }

-  Run the following command in the secondary cluster to create a pattern-matching index synchronization policy, which synchronizes matched indexes from the primary cluster to the secondary cluster, with some of the index settings modified—enabling synchronization of index settings:

   .. code-block:: text

      PUT auto_sync/pattern/${PATTERN}
      {
       "remote_cluster": "leader1",
       "remote_index_patterns": "log*",
       "local_index_pattern": "{{remote_index}}-sync",
       "apply_exist_index": true,
       "settings": {
         "number_of_replicas": 4
       },
       "settings_sync_enable": true,
       "settings_sync_patterns": ["*"],
       "settings_sync_exclude_patterns": ["index.routing.allocation.*"],
       "alias_sync_enable": true,
       "state_sync_enable": true
      }

   .. note::

      The following index configuration items cannot be modified: **number_of_shards**, **version.created**, **uuid**, **creation_date**, and **soft_deletes.enabled**.

.. table:: **Table 3** Request body parameters

   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                      | Description                                                                                                                                                                                                                                     |
   +================================+=================================================================================================================================================================================================================================================+
   | PATTERN                        | Name of the pattern for index matching.                                                                                                                                                                                                         |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | remote_cluster                 | Name of the primary cluster configuration task, which was set in :ref:`Connecting the Primary and Secondary Clusters <css_01_0410__section1023014371242>`. In our example, **leader1** is used.                                                 |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | remote_index_patterns          | Pattern for matching indexes to be synchronized in the primary cluster. The wildcard (``*``) is supported.                                                                                                                                      |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | local_index_pattern            | Index pattern in the secondary cluster. The index template can be replaced. For example, if this parameter is set to **{{remote_index}}-sync**, the index **log1** changes to **log1-sync** after synchronization.                              |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | apply_exist_index              | Whether to synchronize existing indexes in the primary cluster. The default value is **true**.                                                                                                                                                  |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings                       | Index settings to be synchronized                                                                                                                                                                                                               |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings_sync_enable           | Whether to enable synchronization of index settings in the primary cluster. The default value is **false**.                                                                                                                                     |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings_sync_patterns         | Prefix of primary cluster index settings to be synchronized. The default value is **\***. This parameter takes effect when **settings_sync_enable** is set to **true**. The index settings configured in **settings** will not be synchronized. |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings_sync_exclude_patterns | Prefix of primary cluster index settings not to be synchronized. The default value is empty. This parameter is valid only when **settings_sync_enable** is set to **true**.                                                                     |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | alias_sync_enable              | Whether to enable index alias synchronization in the primary cluster. The default value is **false**.                                                                                                                                           |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | state_sync_enable              | Whether to enable index status synchronization in the primary cluster. The default value is **false**.                                                                                                                                          |
   +--------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _css_01_0410__section1012905085616:

Stopping Index Synchronization
------------------------------

Run the following command in the secondary cluster to stop synchronization tasks for specified indexes. Subsequent changes to the indexes in the primary cluster will not be synchronized to the secondary cluster. The read-only state of the indexes in the secondary cluster will be cancelled, so that new data can be written into them.

.. code-block:: text

   PUT log*/stop_remote_sync

In this command, **log\*** indicates the index name. You can specify multiple index names (separated by commas) or use a wildcard. In this example, synchronization tasks for all indexes that start with **log** are stopped.

.. _css_01_0410__section1147716276219:

Querying and Deleting Created Patterns
--------------------------------------

#. Run the following command in the secondary cluster to query created patterns:

   -  Query the list of patterns.

      .. code-block:: text

         GET auto_sync/pattern

   -  Query a specified pattern by name.

      .. code-block:: text

         GET auto_sync/pattern/{PATTERN}

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

#. Run the following command in the secondary cluster to delete a specified pattern by name:

   .. code-block:: text

      DELETE auto_sync/pattern/{PATTERN}

Enabling Forcible Synchronization
---------------------------------

By default, the plug-in determines whether to synchronize metadata based on whether the number of documents in the index of the primary cluster changes. If the primary cluster only updates documents and the number of documents remains unchanged, the plug-in does not synchronize the updates to the secondary cluster. The configuration can be modified. After forcible synchronization is enabled, the index metadata of the primary cluster is forcibly synchronized to the secondary cluster in each synchronization cycle.

The following is an example of enabling forcible synchronization:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "remote_sync.force_synchronize": true
     }
   }

.. _css_01_0410__section94973244119:

Changing the Synchronization Interval
-------------------------------------

The default synchronization interval between the primary and secondary clusters is 30 seconds and can be changed.

The example request below changes the synchronization interval to 2 seconds:

.. code-block:: text

   PUT {index_name}/_settings
   {
     "index.remote_sync.sync_interval": "2s"
   }

Changing the Synchronization Speed
----------------------------------

You can change the data synchronization speed between the primary and secondary clusters by configuring cluster-level settings.

The following is an example request: set the block size to 2 MB, the number of blocks to 20, and the maximum synchronization traffic to 100 MB per second.

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "remote_sync.chunk_size": "2MB",
       "remote_sync.max_concurrent_file_chunks": 20,
       "remote_sync.max_bytes_per_sec": "100MB"
     }
   }

.. table:: **Table 4** Request body parameters

   +----------------------------------------+--------------------------------------------------------+
   | Parameter                              | Description                                            |
   +========================================+========================================================+
   | remote_sync.chunk_size                 | Block size for index synchronization.                  |
   |                                        |                                                        |
   |                                        | Default value: 1 MB                                    |
   |                                        |                                                        |
   |                                        | Format: a string of characters                         |
   +----------------------------------------+--------------------------------------------------------+
   | remote_sync.max_concurrent_file_chunks | Number of blocks for concurrent index synchronization. |
   |                                        |                                                        |
   |                                        | Default value: **10**                                  |
   |                                        |                                                        |
   |                                        | Format: a number                                       |
   +----------------------------------------+--------------------------------------------------------+
   | remote_sync.max_bytes_per_sec          | Maximum data synchronization traffic per second.       |
   |                                        |                                                        |
   |                                        | Default value: 40 MB                                   |
   |                                        |                                                        |
   |                                        | Format: a string of characters                         |
   +----------------------------------------+--------------------------------------------------------+

Querying Index Synchronization Status
-------------------------------------

-  **Obtaining the auto synchronization status of a specified index**

   An example request is as follows:

   .. code-block:: text

      GET {index_name}/sync_stats

   An example response is as follows:

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

Switching the Roles of the Primary and Secondary Clusters
---------------------------------------------------------

When the primary cluster becomes faulty, perform a primary/secondary switchover to have the secondary cluster take over services. The steps are as follows:

#. Determine the index synchronization method between the primary and secondary clusters. Check whether pattern-matching index synchronization policies have been configured in the secondary cluster. For the command to use, see :ref:`Querying and Deleting Created Patterns <css_01_0410__section1147716276219>`.

   -  If there are no such policies, synchronization is performed for specified indexes between the primary and secondary clusters. In this case, go to :ref:`3 <css_01_0410__li20906161442213>`.
   -  If there are such policies, index synchronization between the primary and secondary clusters is based on index patterns. In this case, go to :ref:`2 <css_01_0410__li077084319314>`.

#. .. _css_01_0410__li077084319314:

   Delete pattern-matching index synchronization policies in the secondary cluster. For the command to use, see :ref:`Querying and Deleting Created Patterns <css_01_0410__section1147716276219>`.

#. .. _css_01_0410__li20906161442213:

   Perform :ref:`Stopping Index Synchronization <css_01_0410__section1012905085616>` in the secondary cluster. Then redirect read and write traffic to it. If the primary and secondary clusters synchronize indexes based on index patterns, use a wildcard to match indexes when running the command that stops index synchronization.

#. After the primary cluster recovers, configure information about the secondary cluster in the primary cluster, and connect the primary and secondary clusters again. For details, see :ref:`Connecting the Primary and Secondary Clusters <css_01_0410__section1023014371242>`.

#. Under the primary cluster, perform :ref:`Index Synchronization <css_01_0410__section97051931358>` to synchronize data from the secondary cluster to the primary cluster, and then perform a primary/secondary switchover to switch back.
