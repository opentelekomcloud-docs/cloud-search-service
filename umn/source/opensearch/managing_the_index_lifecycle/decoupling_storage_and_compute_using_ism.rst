:original_name: css_01_0211.html

.. _css_01_0211:

Decoupling Storage and Compute Using ISM
========================================

In log analytics and monitoring scenarios, storage costs for historical data accumulate over time. However, most cold data is accessed only occasionally for auditing or backtracking purposes. Storing such data on expensive local SSDs over extended periods does not make economic sense. To balance storage costs with long-term retention requirements, CSS provides a storage-compute decoupling feature for OpenSearch clusters. By configuring an index state management (ISM) policy, coupled with index freezing, you can have eligible indexes automatically transitioned from local SSDs to lower-cost object storage. The data remains searchable, although query latency may increase.

Solution
--------

This topic describes how to configure an ISM policy to decouple storage and compute.

-  Hot phase: Data is stored on high-performance local disks to support high-concurrency read and write operations.
-  Warm phase: The index is frozen, and data is dumped to OBS. Local disks only retain necessary metadata, and query requests are directly sent to OBS. (Initial queries may experience higher latency, but subsequent queries can accelerate with the use of a cache.)
-  Delete phase: When the data retention period expires, the index is automatically deleted to reclaim storage space.

In this example, an ISM policy is created for an OpenSearch cluster. According to this policy, a newly created index is automatically frozen in three days, with data dumped to OBS; and deleted in seven days.


.. figure:: /_static/images/en-us_image_0000002061403354.png
   :alt: **Figure 1** Storage-compute decoupling

   **Figure 1** Storage-compute decoupling

Constraints
-----------

Only OpenSearch 1.3.6 and 2.19.0 clusters support decoupled storage and compute.

Configuring an ISM Policy
-------------------------

#. Log in to OpenSearch Dashboards and go to the command execution page.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.

   c. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. Define an ISM policy and associate it with an index template to automate storage-compute decoupling for new indexes created using that template.

   For example, create a policy named *hot_warm_policy*. According to this policy, a newly created index is automatically frozen in three days, with data dumped to OBS; and deleted permanently in seven days. Associate the policy with an index template so that new indexes whose name starts with **data** will automatically inherit this policy.

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
                  "freeze_low_cost": {} // Freeze the index.
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
          "ism_template": {      // Associate with an index template.
            "index_patterns": [
              "data*"
            ],
            "priority": 100
          }
        }
      }

#. Write data to an index.

   For example, create an index named data-2022-06-06 and write data to it in batches.

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

   The index will automatically apply the ISM policy **hot_warm_policy**.

#. Query data and check whether the ISM policy is automatically applied.

   a. Three days after index creation, query the list of frozen indexes and check whether indexes created three days ago have been frozen.

      .. code-block:: text

         GET _cat/freeze_indices?s=i&v

      If the returned result contains **data-2022-06-06**, the index has been dumped to OBS.

      .. code-block::

         health status index                  uuid                   pri rep docs.count docs.deleted store.size pri.store.size
         green  open   data-2022-06-06  x8ab5NX6T3Ox_xoGUanogQ    1   1          6            0      7.6kb          3.8kb

   b. Seven days after index creation, query the index list and check whether indexes created seven days ago have been deleted.

      .. code-block:: text

         GET /_cat/indices?expand_wildcards=open,closed

      If the returned result does not contain **data-2022-06-06**, the index has been deleted.
