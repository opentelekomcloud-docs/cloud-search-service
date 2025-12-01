:original_name: css_01_0211.html

.. _css_01_0211:

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
-  OpenSearch 1.3.6 or 2.19.0 is used.

Decoupling Index Storage and Compute Through Index Lifecycle Management
-----------------------------------------------------------------------

#. Log in to the OpenSearch Dashboards.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.

   c. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

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

#. Create an index named data-2022-06-06. The index is automatically associated with the lifecycle policy **hot_warm_policy**, which freezes the index three days after it is created and deletes it seven days after creation.

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
