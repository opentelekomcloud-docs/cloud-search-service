:original_name: css_01_0167.html

.. _css_01_0167:

Matching Index Synchronization
==============================

The request URL and request body parameters are as follows:

.. code-block:: text

   PUT auto_sync/pattern/{pattern_name}

.. table:: **Table 1** Request body parameters

   +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Description                                                                                                                                                                                                                        |
   +=======================+====================================================================================================================================================================================================================================+
   | remote_cluster        | Name of the primary cluster. The default name is **leader1**. You can change the name by configuring the primary cluster information.                                                                                              |
   +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | remote_index_patterns | Mode of the index to be synchronized in the primary cluster. The wildcard (``*``) is supported.                                                                                                                                    |
   +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | local_index_pattern   | Mode of the index being synchronized in the secondary cluster. The template can be replaced. For example, if this parameter is set to **{{remote_index}}-sync**, the index **log1** change to **log1-sync** after synchronization. |
   +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | apply_exist_index     | Whether to synchronize existing indexes in the primary cluster. The default value is **true**.                                                                                                                                     |
   +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | settings              | Index settings of the index being synchronized                                                                                                                                                                                     |
   +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following are two examples:

1. Synchronize a single index from the primary cluster to the secondary cluster.

.. code-block:: text

   PUT auto_sync/pattern/pattern1
   {
    "remote_cluster": "leader1",
    "remote_index_patterns": "log*",
    "local_index_pattern": "{{remote_index}}-sync",
    "apply_exist_index": true
   }

2. Synchronize a single index from the primary cluster to the secondary cluster and modify the index configurations.

.. code-block:: text

   PUT auto_sync/pattern/pattern1
   {
    "remote_cluster": "leader1",
    "remote_index_patterns": "log*",
    "local_index_pattern": "{{remote_index}}-sync",
    "apply_exist_index": true,
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
