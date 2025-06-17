:original_name: css_01_0421.html

.. _css_01_0421:

Decoupling Index Storage and Compute in an Elasticsearch Cluster Through Index Lifecycle Management
===================================================================================================

Overview
--------

CSS supports decoupled storage and compute. That is, indexes can be frozen and their data can be dumped to OBS to reduce the storage cost of cold data. This document describes how to use index lifecycle management to automatically freeze indexes at a specific time to decouple storage and compute.

In this example, a lifecycle policy is created for an Elasticsearch 7.10.2 cluster. According to this policy, a newly created index is automatically frozen in three days, with data dumped to OBS; closed in six days; archived in seven days (its data is moved from OBS to archive storage to further cut storage cost); and deleted in 30 days.


.. figure:: /_static/images/en-us_image_0000002060255410.png
   :alt: **Figure 1** Storage-compute decoupling

   **Figure 1** Storage-compute decoupling

Constraints
-----------

Only Elasticsearch 7.6.2, Elasticsearch 7.10.2, and OpenSearch 1.3.6 support storage-compute decoupling. Archive storage is available only for Elasticsearch 7.10.2 clusters whose image version is 24.3.0.C001 or later.

Prerequisites
-------------

An Elasticsearch 7.10.2 cluster is available.

Decoupling Index Storage and Compute Through Index Lifecycle Management
-----------------------------------------------------------------------

#. Log in to the CSS management console.

#. In the navigation tree on the left, choose **Clusters** > **Elasticsearch**. The cluster list is displayed.

#. Click **Access Kibana** in the **Operation** column of a cluster.

#. In the navigation tree on the left of Kibana, choose **Dev Tools**. The command execution page is displayed.

#. Create a lifecycle policy named **hot_warm_policy**.

   According to the policy, in three days of index creation, the API used for freezing indexes is automatically called to dump index data to OBS. In six days, the index is closed. In seven days, the index is archived. In 30 days, the index is deleted.

   .. code-block:: text

      PUT _opendistro/_ism/policies/hot_warm_policy
      {
        "policy": {
          "description": "hot warm archive delete workflow",
          "error_notification": null,
          "default_state": "hot",
          "states": [
            {
              "name": "hot",
              "actions": [],
              "transitions": [
                {
                  "state_name": "warm",
                  "conditions": {
                    "min_index_age": "3d"
                  }
                }
              ]
            },
            {
              "name": "warm",
              "actions": [
                {
                  "freeze_low_cost": {}
                }
              ],
              "transitions": [
                {
                  "state_name": "close",
                  "conditions": {
                    "min_index_age": "6d"
                  }
                }
              ]
            },
            {
              "name": "close",
              "actions": [
                {
                  "close": {}
                }
              ],
              "transitions": [
                {
                  "state_name": "archive",
                  "conditions": {
                    "min_index_age": "7d"
                  }
                }
              ]
            },
            {
              "name": "archive",
              "actions": [
                {
                  "freeze_archive": {}
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
              ],
              "transitions": []
            }
          ]
        }
      }

#. Create the index template **template_hot_warm**.

   Template description: All the new indexes starting with **data** are automatically associated with the lifecycle policy **hot_warm_policy**.

   .. code-block:: text

      PUT _template/template_hot_warm
      {
        "index_patterns": "data*",
        "settings": {
          "number_of_replicas": 5,
          "number_of_shards": 1,
          "opendistro.index_state_management.policy_id": "hot_warm_policy"
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

      +---------------------------------------------+--------------------------------+
      | Parameter                                   | Description                    |
      +=============================================+================================+
      | number_of_shards                            | Number of index shards         |
      +---------------------------------------------+--------------------------------+
      | number_of_replicas                          | Number of index shard replicas |
      +---------------------------------------------+--------------------------------+
      | opendistro.index_state_management.policy_id | Lifecycle policy name          |
      +---------------------------------------------+--------------------------------+

#. Create the **data-2022-06-06** index. The index automatically uses the **template_hot_warm** template and associates the index template with the lifecycle policy **hot_warm_policy**. According to the policy, the index will be frozen in three days, closed in six days, archived in seven days, and deleted in 30 days.

   .. code-block:: text

      POST data-2022-06-06/_bulk
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

#. Query data and check whether storage and compute is automatically decoupled.

   -  Three days after the index is created, check the frozen index.

      .. code-block:: text

         GET _cat/freeze_indices?s=i&v

      The index generated three days ago is expected to be frozen.

      .. code-block::

         health status index                  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
         green  open   data-2022-06-06  x8ab5NX6T3Ox_xoGUanogQ    1   1          6            0      7.6kb          3.8kb

   -  Seven days after the index is created, check the index status.

      .. code-block:: text

         GET _cat/archive_indices?v

      The index generated seven days ago is expected to have been archived.

      .. code-block::

         health status index   uuid                   pri rep docs.count docs.deleted store.size pri.store.size
                close  data-2022-06-06 M0uRAWj_SKydjg0dFzyJow

   -  30 days after the index is created, check the index. The index is expected to be deleted.
