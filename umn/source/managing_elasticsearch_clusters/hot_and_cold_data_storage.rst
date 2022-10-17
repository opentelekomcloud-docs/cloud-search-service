:original_name: css_01_0079.html

.. _css_01_0079:

Hot and Cold Data Storage
=========================

CSS provides you with cold data nodes. You can store data that requires query response in seconds on high-performance nodes and store data that requires query response in minutes on cold data nodes with large capacity and low specifications.

.. note::

   -  When creating a cluster, you need to configure nodes as data nodes. When you enable the cold data node function, data nodes become hot nodes.
   -  You can enable the cold data node, master node, and client node functions at the same time.
   -  You can increase nodes and expand storage capacity of cold data nodes. The maximum storage capacity is determined by the node specifications. Local disks do not support storage capacity expansion.

Hot and Cold Data Node Switchover
---------------------------------

After you enable the cold data node function, the cold data node is labeled with **cold**. In addition, data nodes are labeled with **hot** and become hot nodes. You can specify indices to distribute data to cold or hot nodes.

You can configure a template to store indices on the specified cold or hot node.

The following figure shows this process. Log in to the **Kibana** **Console** page of the cluster, modify the template by configuring the index starting with **myindex**, and store the indices on the cold node. In this case, the **myindex\*** date is stored on the cold data node by modifying the template.

-  For the 5.\ *x* version, run the following command to create a template:

   .. code-block:: text

      PUT _template/test
      {
          "order": 1,
          "template": "myindex*",
          "settings": {
              "index": {
                  "refresh_interval": "30s",
                  "number_of_shards": "3",
                  "number_of_replicas": "1",
                  "routing.allocation.require.box_type": "cold"
              }
          }
      }

-  For the 6.\ *x* and later versions, run the following command to create a template:

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
