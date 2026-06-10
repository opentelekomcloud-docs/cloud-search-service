:original_name: css_01_0136.html

.. _css_01_0136:

Configuring Query Traffic Isolation
===================================

In distributed search and data analytics scenarios, faulty cluster nodes—with memory faults or sustained high CPU usage—may lead to increased query response times or service availability issues. To address this, we need a quick and effective way to route query traffic away from faulty nodes and redirect it to other healthy nodes, thus ensuring service continuity and stability. CSS OpenSearch clusters provide a query traffic isolation feature for this purpose. With it, you can configure specific nodes as low-priority nodes or isolated nodes and define an index whitelist for exceptions. For shard query requests to indexes that are not on this whitelist, the system preferentially or completely bypass these nodes, ensuring that faulty nodes won't affect services.

How the Feature Works
---------------------


.. figure:: /_static/images/en-us_image_0000002510821514.png
   :alt: **Figure 1** How query traffic isolation works

   **Figure 1** How query traffic isolation works

Here is how query traffic isolation works:

#. When a node in your cluster experiences issues, you configure it as either a low-priority node or an isolated node.
#. Query requests are broken down into per-shard queries.
#. Per-shard queries are preferentially allocated to healthy nodes, bypassing isolated nodes completely, and bypassing low-priority nodes when possible.

   -  A per-shard query is allocated to a low-priority node only if this shard is not available elsewhere.
   -  If the target shard of a query exists only on an isolated node, the query fails.

This way, CSS keeps query traffic away from problematic cluster nodes, ensuring query performance and service availability.

Constraints
-----------

-  Query traffic isolation is supported only when the OpenSearch cluster version is 2.19.0 and the image version is 2.19.0_25.9.0_xxx or later.
-  By default, indexes prefixed with **.kibana** and **.opendistro** are exempted from query traffic isolation settings.

Logging In to OpenSearch Dashboards
-----------------------------------

Log in to OpenSearch Dashboards and go to the command execution page. OpenSearch clusters support multiple access methods. This topic uses OpenSearch Dashboards as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.


Configuring Query Traffic Isolation
-----------------------------------

Run the following command to configure low-priority nodes, isolated nodes, and the index whitelist (or allow-list).

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "cluster.routing.css.preference.query.low_priority_nodes": "node1,node2",
       "cluster.routing.css.preference.query.isolated_nodes": "node3,node4",
       "cluster.routing.css.preference.query.allow_list": "index1,index2,test-index.*"
     }
   }

.. table:: **Table 1** Parameter description

   +---------------------------------------------------------+-----------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                                               | Type            | Default Value                 | Description                                                                                                                                                                                                                                                      |
   +=========================================================+=================+===============================+==================================================================================================================================================================================================================================================================+
   | cluster.routing.css.preference.query.low_priority_nodes | String          | Empty (no low-priority nodes) | Configure low-priority nodes. For per-shard query requests to indexes that are not on the whitelist, the system preferentially bypasses low-priority nodes. A per-shard query is allocated to a low-priority node only if this shard is not available elsewhere. |
   |                                                         |                 |                               |                                                                                                                                                                                                                                                                  |
   |                                                         |                 |                               | When configuring multiple nodes, use a comma (**,**) to separate them.                                                                                                                                                                                           |
   +---------------------------------------------------------+-----------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster.routing.css.preference.query.isolated_nodes     | String          | Empty (no isolated nodes)     | Configure isolated nodes. With the exception of whitelisted indexes, per-shard query requests bypass isolated nodes completely. If the target shard exists only on an isolated node, the query fails.                                                            |
   |                                                         |                 |                               |                                                                                                                                                                                                                                                                  |
   |                                                         |                 |                               | When configuring multiple nodes, use a comma (**,**) to separate them.                                                                                                                                                                                           |
   +---------------------------------------------------------+-----------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster.routing.css.preference.query.allow_list         | String          | Empty                         | Configure indexes that are exempted from the above settings.                                                                                                                                                                                                     |
   |                                                         |                 |                               |                                                                                                                                                                                                                                                                  |
   |                                                         |                 |                               | Use a comma (**,**) to separate different index names. Regular expression matching is supported.                                                                                                                                                                 |
   |                                                         |                 |                               |                                                                                                                                                                                                                                                                  |
   |                                                         |                 |                               | By default, indexes prefixed with **.kibana** and **.opendistro** are exempted from query traffic isolation settings. This means the whitelist (or allow-list) will include the indexes you configure here, as well as these default ones.                       |
   +---------------------------------------------------------+-----------------+-------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
