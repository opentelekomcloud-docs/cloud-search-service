:original_name: css_01_0503.html

.. _css_01_0503:

Decoupling Index Storage and Compute in an OpenSearch Cluster Through Index Lifecycle Management
================================================================================================

Overview
--------

CSS supports decoupled storage and compute. That is, indexes can be frozen in OBS to reduce the storage cost of cold data. This document describes how to use index lifecycle management to automatically freeze indexes at a specific time to decouple storage and compute.

In this section, a lifecycle policy is configured to automatically freeze an index three days after it is created and dump data to OBS. The index will be deleted seven days after it is created.


.. figure:: /_static/images/en-us_image_0000002061403354.png
   :alt: **Figure 1** Storage-compute decoupling

   **Figure 1** Storage-compute decoupling

Prerequisites
-------------

-  There are available CSS clusters.
-  OpenSearch 1.3.6 is used.

Decoupling Index Storage and Compute Through Index Lifecycle Management
-----------------------------------------------------------------------

#. Log in to the CSS management console.

#. In the navigation tree on the left, choose **Clusters** > **OpenSearch**. The cluster list is displayed.

#. Click **Access Kibana** in the **Operation** column of a cluster, and log in to OpenSearch Dashboards.

#. In the navigation tree on the left of OpenSearch Dashboards, choose **Dev Tools**. The command execution page is displayed.

#. Create a lifecycle policy named **hot_warm_policy**.

   Policy description: Three days after an index is created, the API for freezing indexes is automatically called to dump data to OBS. Seven days after index creation, the index is deleted.

   .. code-block:: text

      PUT _plugins/_ism/policies/hot_warm_policy
      {
        "policy": {
          "description": "hot warm delete workflow",
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
          ],
          "ism_template": {
            "index_patterns": [
              "data*"
            ],
            "priority": 100
          }
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
          "index.plugins.index_state_management.policy_id": "hot_warm_policy"
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

      +------------------------------------------------+--------------------------------+
      | Parameter                                      | Description                    |
      +================================================+================================+
      | number_of_shards                               | Number of index shards         |
      +------------------------------------------------+--------------------------------+
      | number_of_replicas                             | Number of index shard replicas |
      +------------------------------------------------+--------------------------------+
      | index.plugins.index_state_management.policy_id | Lifecycle policy name          |
      +------------------------------------------------+--------------------------------+

#. Create the **data-2022-06-06** index. The index automatically uses the **template_hot_warm** template and associates the index template with the lifecycle policy **hot_warm_policy**. As such, the index is frozen three days after creation and is deleted seven days after creation.

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

   -  Seven days after the index is created, check the frozen index. The index is expected to be deleted.
