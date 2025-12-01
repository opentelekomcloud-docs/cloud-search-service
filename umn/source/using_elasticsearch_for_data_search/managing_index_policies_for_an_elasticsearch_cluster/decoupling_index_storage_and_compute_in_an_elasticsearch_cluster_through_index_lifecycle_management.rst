:original_name: css_01_0022.html

.. _css_01_0022:

Decoupling Index Storage and Compute in an Elasticsearch Cluster Through Index Lifecycle Management
===================================================================================================

Overview
--------

CSS supports decoupled storage and compute. That is, indexes can be frozen and their data can be dumped to OBS to reduce the storage cost of cold data. This document describes how to use index lifecycle management to automatically freeze indexes at a specific time to decouple storage and compute.

In this example, a lifecycle policy is created for an Elasticsearch 7.10.2 cluster. According to this policy, a newly created index is automatically frozen in three days, with data dumped to OBS; and deleted in seven days.


.. figure:: /_static/images/en-us_image_0000002061403354.png
   :alt: **Figure 1** Storage-compute decoupling

   **Figure 1** Storage-compute decoupling

Constraints
-----------

Only Elasticsearch 7.6.2 and 7.10.2 clusters support decoupled storage and compute.

Prerequisites
-------------

The Elasticsearch cluster is available.

Decoupling Index Storage and Compute Through Index Lifecycle Management
-----------------------------------------------------------------------

#. Log in to Kibana.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. Create a lifecycle policy named **hot_warm_policy**.

   Policy description: Three days after an index is created, the API for freezing indexes is automatically called to dump data to OBS. Seven days after index creation, the index is deleted.

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
                  "state_name": "delete",
                  "conditions": {
                    "min_index_age": "7d"
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

#. Create the **data-2022-06-06** index. The index automatically uses the **template_hot_warm** template and associates the index template with the lifecycle policy **hot_warm_policy**. As such, the index is automatically frozen in three days, and deleted in seven days after creation.

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

   -  Seven days after index creation, check the index. The index is expected to be deleted.
