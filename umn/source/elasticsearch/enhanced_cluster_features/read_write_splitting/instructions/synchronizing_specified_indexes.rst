:original_name: css_01_0166.html

.. _css_01_0166:

Synchronizing Specified Indexes
===============================

**Synchronize a single index**.

The request URL and request body parameters are as follows:

.. code-block:: text

   PUT start_remote_sync

.. table:: **Table 1** Request body parameters

   +----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter      | Description                                                                                                                           |
   +================+=======================================================================================================================================+
   | remote_cluster | Name of the primary cluster. The default name is **leader1**. You can change the name by configuring the primary cluster information. |
   +----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | remote_index   | Name of the index to be synchronized in the primary cluster                                                                           |
   +----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | local_index    | Name of the index being synchronized to the secondary cluster                                                                         |
   +----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | settings       | Index settings of the index being synchronized                                                                                        |
   +----------------+---------------------------------------------------------------------------------------------------------------------------------------+

After the synchronization function is enabled, indexes in the secondary cluster become read-only and are periodically synchronized with indexes in the primary cluster.

The following are two examples:

#. Synchronize a single index from the primary cluster to the secondary cluster.

   .. code-block:: text

      PUT start_remote_sync
      {
        "remote_cluster": "leader1",
        "remote_index": "data1_leader",
        "local_index": "data1_follower"
      }

#. Synchronize a single index from the primary cluster to the secondary cluster and modify the index configurations.

   .. code-block:: text

      PUT start_remote_sync
      {
        "remote_cluster": "leader1",
        "remote_index": "data1_leader",
        "local_index": "data1_follower",
        "settings": {
          "number_of_replicas": 4
        }
      }

   .. note::

      The following index configurations cannot be modified:

      -  number_of_shards
      -  version.created
      -  uuid
      -  creation_date
      -  soft_deletes.enabled
