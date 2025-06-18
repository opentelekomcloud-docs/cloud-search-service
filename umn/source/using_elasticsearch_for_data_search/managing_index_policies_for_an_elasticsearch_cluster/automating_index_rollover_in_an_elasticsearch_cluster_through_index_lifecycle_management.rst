:original_name: css_01_0420.html

.. _css_01_0420:

Automating Index Rollover in an Elasticsearch Cluster Through Index Lifecycle Management
========================================================================================

As time series data is continuously written into Elasticsearch and the index size keeps growing, you can configure Index Lifecycle Management (ISM) to periodically roll over data to new indexes and delete old indexes.

In this example, a lifecycle policy is created for an Elasticsearch cluster. According to this policy, when the size of an index reaches 1 TB or the index is one day old, a new index will be automatically generated; seven days after the index is created, data duplicates will be disabled; 30 days after the index is created, the index will be deleted.

Assume that an index generates approximately 2.4 TB of data each day. The index alias is **log-alias**. The following figure illustrates the data format in the cluster. During reads, it points to all indexes whose name starts with **test**. During writes, it points to the latest index.


.. figure:: /_static/images/en-us_image_0000002209172477.png
   :alt: **Figure 1** log-alias format

   **Figure 1** log-alias format

.. note::

   The one day in the rollover time refers to 24 hours following the index creation time, not a calendar day.

Prerequisites
-------------

The target Elasticsearch cluster is available.

Automating Index Rollover Through Index Lifecycle Management
------------------------------------------------------------

.. important::

   The Elasticsearch cluster version must be 7.6.2 or later.

#. Log in to the CSS management console.

#. In the navigation tree on the left, choose **Clusters** > **Elasticsearch**. The cluster list is displayed.

#. Click **Access Kibana** in the **Operation** column of a cluster.

#. In the navigation tree on the left of Kibana, choose **Dev Tools**. The command execution page is displayed.

#. Create a rollover lifecycle policy named **rollover_workflow**.

   Policy description: When the size of an index reaches 1 TB or the index has been created for more than one day, the index rollover is performed. When the index has been created for seven days, the data copy is disabled. When the index has been created for 30 days, the index is deleted.

   .. code-block:: text

      PUT _opendistro/_ism/policies/rollover_workflow
      {
        "policy": {
          "description": "rollover test",
          "default_state": "hot",
          "states": [
            {
              "name": "hot",
              "actions": [
                {
                  "rollover": {
                    "min_size": "1tb",
                    "min_index_age": "1d"
                  }
                }
              ],
              "transitions": [
                {
                  "state_name": "warm",
                  "conditions": {
                    "min_index_age": "7d"
                  }
                }
              ]
            },
            {
              "name": "warm",
              "actions": [
                {
                  "replica_count": {
                    "number_of_replicas": 0
                  }
                }
              ],
              "transitions": [
                {
                  "state_name": "delete",
                  "conditions": {
                    "min_index_age": "30d"
                  }
                }
              ]
            },
            {
              "name": "delete",
              "actions": [
                {
                  "delete": {}
                }
              ]
            }
          ]
        }
      }

   After a lifecycle policy is created, run the following command to query the policy details:

   .. code-block:: text

      GET _opendistro/_ism/policies/rollover_workflow

#. Create the index template **template_test**.

   Template description: All the new indexes starting with **test** are automatically associated with the rollover lifecycle policy **rollover_workflow**. The alias **log_alias** is used during rollover.

   .. code-block:: text

      PUT _template/template_test
      {
        "index_patterns": "test*",
        "settings": {
          "number_of_replicas": 1,
          "number_of_shards": 1,
          "opendistro.index_state_management.policy_id": "rollover_workflow",
          "index.opendistro.index_state_management.rollover_alias": "log_alias"
        },
        "mappings": {
          "properties": {
            "name": {
              "type": "text"
            }
          }
        }
      }

   .. table:: **Table 1** Parameter description

      +--------------------------------------------------------+--------------------------------+
      | Parameter                                              | Description                    |
      +========================================================+================================+
      | number_of_shards                                       | Number of index shards         |
      +--------------------------------------------------------+--------------------------------+
      | number_of_replicas                                     | Number of index shard replicas |
      +--------------------------------------------------------+--------------------------------+
      | opendistro.index_state_management.policy_id            | Lifecycle policy name          |
      +--------------------------------------------------------+--------------------------------+
      | index.opendistro.index_state_management.rollover_alias | Index alias for rollover       |
      +--------------------------------------------------------+--------------------------------+

   After an index template is created, you can run the following command to query the template details:

   .. code-block:: text

      GET _template/template_test

#. .. _css_01_0420__en-us_topic_0000001961259029_li5274918111415:

   Create an index, specify **aliases**, and set **is_write_index** to **true**. The index template **template_test** is automatically used for the index and is associated with the lifecycle policy **rollover_workflow** based on the index template configuration. In this way, when the index size reaches 1 TB or the index is created for more than one day, the rollover automatically starts. After an index is created for seven days, the data copy is disabled. After an index is created for 30 days, the index is deleted.

   The following index is the URL code of **<test-{now/d}-000001>**. By default, an index name contains the creation date. For example, if an index is created on 2022-06-02, the index name is **test-2022.06.02-000001**.

   .. code-block:: text

      PUT %3Ctest-%7Bnow%2Fd%7D-000001%3E
      {
        "aliases": {
          "log_alias": {
            "is_write_index": true
          }
        }
      }

#. The alias **log_alias** is used to during data write, and **log_alias** always points to the last index.

   .. code-block:: text

      POST log_alias/_bulk
      {"index":{}}
      {"name":"name1"}
      {"index":{}}
      {"name":"name2"}
      {"index":{}}
      {"name":"name3"}
      {"index":{}}
      {"name":"name4"}
      {"index":{}}
      {"name":"name5"}
      {"index":{}}
      {"name":"name6"}

#. Query data and check whether the rollover takes effect.

   -  One day after the indexes are created, check the indexes starting with **test**.

      .. code-block:: text

         GET _cat/indices/test*?s=i

      There are supposed to be at least two indexes, for example:

      .. code-block::

         green open test-<Date>-000001 r8ab5NX6T3Ox_hoGUanogQ 1 1 6 0 416b 208b
         green open test-<Date>-000002 sfwkVgy8RSSEw7W-xYjM2Q 1 1 0 0 209b 209b

      In the preceding information, **test-<Date>-000001** is the index created in :ref:`7 <css_01_0420__en-us_topic_0000001961259029_li5274918111415>`, and **test-<Date>-000002** is the index generated through rollover.

   -  To query the index associated with the alias **log_alias**, run the following command:

      .. code-block:: text

         GET _cat/aliases/log_alias?v

      The alias is supposed to point to multiple indexes, for example:

      .. code-block::

         alias     index                  filter routing.index routing.search is_write_index
         log_alias test-<Date>-000001      -      -             -              false
         log_alias test-<Date>-000002      -      -             -              true

FAQ: How Do I Skip Rollover for an Index?
-----------------------------------------

**Scenarios**

-  A manual rollover is performed: A time-based ISM policy was configured to automate index rollover. Before the rollover criteria were met, however, a manual rollover was performed. When the auto rollover time configured by ISM was reached, an automatic rollover was attempted but failed because the index had already been rolled over manually. As a result, the ISM task stopped. To solve this problem, you need to skip the index rollover and then retry the ISM task to resume automatic index rollover.
-  For an index that has already been rolled over automatically, a remove or add policy operation is performed: After the rollover policy is modified (through the remove policy or add policy operation), the ISM task restarts from the beginning. When rollover starts, the task fails. To solve this, you also need to skip index rollover and then retry the ISM task to resume automatic index rollover.

.. warning::

   After rollover is skipped for an index, ISM will no longer attempt rollover or generate rolled-over indexes. This means skipping index rollover may lead to data loss. Please exercise caution.

**Constraints**

To skip index rollover, the Elasticsearch cluster version must be 7.6.2 or 7.10.2, and the cluster image version must not be earlier than 7.x.2_25.1.0_x.x.x.

**Procedure**

#. If an ISM task stops due to an index rollover failure, run the following command to skip index rollover:

   .. code-block:: text

      PUT index_name/_settings
      {
        "index.plugins.index_state_management.rollover_skip": true
      }

   If **true** is returned, the configuration is successful.

#. After index rollover is skipped, run the following command to retry the ISM task:

   .. code-block:: text

      POST _opendistro/_ism/retry/index_name

   If the following information is returned, the retry is successful:

   .. code-block::

      {
        "updated_indices": 1,
        "failures": false,
        "failed_indices": []
      }
