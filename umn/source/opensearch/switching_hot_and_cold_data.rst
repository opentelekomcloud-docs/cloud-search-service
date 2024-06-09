:original_name: en-us_topic_0000001591776270.html

.. _en-us_topic_0000001591776270:

Switching Hot and Cold Data
===========================

CSS provides you with cold data nodes. You can store data that requires query response in seconds on hot data nodes with high performance and store historical data that requires query response in minutes on cold data nodes with large capacity and low specifications.

.. note::

   -  When creating a cluster, you need to configure data nodes. After cold data nodes are selected, the original data nodes become hot data nodes.
   -  You can enable the cold data node, master node, and client node functions at the same time.
   -  You can increase nodes and expand storage capacity of cold data nodes. The maximum storage capacity is determined by the node specifications. Local disks do not support storage capacity expansion.

Switching Between Hot and Cold Data
-----------------------------------

If you enable cold data nodes when creating a cluster, the cold data nodes are labeled with **cold**. Other data nodes become hot nodes and are labeled with **hot**. You can specify indexes to allocate data to cold or hot nodes.

You can configure a template to store indexes on the specified cold or hot node.

Log in to the **Kibana** **Console** page of the cluster, store the indexes starting with **myindex** on the cold node. In this way, you can use a template to store the **myindex\*** date on the cold data node.

Run the following command to create a template:

.. code-block:: text

   PUT _template/test
   {
     "order": 1,
     "index_patterns": "myindex*",
     "settings": {
       "refresh_interval": "30s",
       "number_of_shards": "3",
       "number_of_replicas": "1",
       "routing.allocation.require.box_type": "cold"
     }
   }

You can perform operations on the created index.

.. code-block:: text

   PUT myindex/_settings
    {
           "index.routing.allocation.require.box_type": "cold"
       }

You can cancel the configurations of hot and cold data nodes.

.. code-block:: text

   PUT myindex/_settings
   {
           "index.routing.allocation.require.box_type": null
       }
