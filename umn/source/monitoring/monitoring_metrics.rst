:original_name: en-us_topic_0000001599872681.html

.. _en-us_topic_0000001599872681:

Monitoring Metrics
==================

Function
--------

This topic describes CSS metrics that can be monitored by Cloud Eye as well as their namespaces and dimensions. You can search for the monitoring metrics and alarms generated for CSS by using the Cloud Eye console or calling APIs.

Namespace
---------

SYS.ES


Monitoring Metrics
------------------

-  :ref:`Table 1 <en-us_topic_0000001599872681__table197512917274>` describes the monitoring metrics of CSS clusters.
-  Monitored object: Cloud service nodes of CSS clusters
-  Monitoring period (original metric): 1 minute

.. note::

   Accumulated value: The value is accumulated from the time when a node is started. After the node is restarted, the value is reset to zero and accumulated again.

.. _en-us_topic_0000001599872681__table197512917274:

.. table:: **Table 1** CSS metrics

   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | Metric ID                        | Metric                                  | Description                                          | Value Range | Monitored Target                 | Monitoring Interval (Raw Data) |
   +==================================+=========================================+======================================================+=============+==================================+================================+
   | jvm_heap_usage                   | JVM Heap Usage                          | JVM heap memory usage of a node.                     | 0-100%      | CSS cluster - cloud service node | 1 minute                       |
   |                                  |                                         |                                                      |             |                                  |                                |
   |                                  |                                         | Unit: %                                              |             |                                  |                                |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | cpu_usage                        | CPU Usage                               | CPU usage.                                           | 0-100%      | CSS cluster - cloud service node | 1 minute                       |
   |                                  |                                         |                                                      |             |                                  |                                |
   |                                  |                                         | Unit: %                                              |             |                                  |                                |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | load_average                     | Average Load                            | Average number of queuing tasks per minute on a node | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | open_file_descriptors            | Open File Descriptors                   | Number of opened file descriptors on a node          | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | max_file_descriptors             | Max. Allowed File Descriptors           | Maximum number of allowed file descriptors           | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_write_queue          | Tasks in Write Queue                    | Number of job queues in a write thread pool          | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_search_queue         | Tasks in Search Queue                   | Number of job queues in a search thread pool         | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_force_merge_queue    | Tasks in ForceMerge Queue               | Number of job queues in a force merge thread pool    | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_write_rejected       | Rejected Tasks in Write Queue           | Number of rejected jobs in a write thread pool       | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_search_rejected      | Rejected Tasks in Search Queue          | Number of rejected jobs in a search thread pool      | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_force_merge_rejected | Rejected Tasks in ForceMerge Queue      | Number of rejected jobs in a force merge thread pool | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_write_threads        | Size of Write Thread Pool               | Size of a write thread pool                          | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_search_threads       | Size of Search Thread Pool              | Size of a search thread pool                         | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | thread_pool_force_merge_threads  | Size of ForceMerge Thread Pool          | Size of a force merge thread pool                    | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | free_fs_size                     | Available Size of File Systems          | Available size of file systems in a CSS cluster      | >= 0 bytes  | CSS cluster - cloud service node | 1 minute                       |
   |                                  |                                         |                                                      |             |                                  |                                |
   |                                  |                                         | Unit: byte                                           |             |                                  |                                |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | total_fs_size                    | Total Size of File Systems              | Total size of file systems in a CSS cluster          | >= 0 bytes  | CSS cluster - cloud service node | 1 minute                       |
   |                                  |                                         |                                                      |             |                                  |                                |
   |                                  |                                         | Unit: byte                                           |             |                                  |                                |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | jvm_old_gc_count                 | Total GCs of Old-Generation JVM         | Number of old-generation garbage collection times    | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | jvm_old_gc_time                  | Total GC Duration of Old-Generation JVM | Old-generation garbage collection duration.          | >= 0 ms     | CSS cluster - cloud service node | 1 minute                       |
   |                                  |                                         |                                                      |             |                                  |                                |
   |                                  |                                         | Unit: ms                                             |             |                                  |                                |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | jvm_young_gc_count               | Total GCs of Young-Generation JVM       | Number of young-generation garbage collection times  | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | jvm_young_gc_time                | GC Duration of Young-Generation JVM     | Young-generation garbage collection duration.        | >= 0 ms     | CSS cluster - cloud service node | 1 minute                       |
   |                                  |                                         |                                                      |             |                                  |                                |
   |                                  |                                         | Unit: ms                                             |             |                                  |                                |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | mem_free_in_bytes                | Available Memory                        | Unused memory space of a node.                       | >= 0 bytes  | CSS cluster - cloud service node | 1 minute                       |
   |                                  |                                         |                                                      |             |                                  |                                |
   |                                  |                                         | Unit: byte                                           |             |                                  |                                |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | mem_free_percent                 | Available Memory Percentage             | Percentage of unused memory space on a node.         | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | mem_used_in_bytes                | Used Memory                             | Used memory space of a node.                         | >= 0 bytes  | CSS cluster - cloud service node | 1 minute                       |
   |                                  |                                         |                                                      |             |                                  |                                |
   |                                  |                                         | Unit: byte                                           |             |                                  |                                |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | current_opened_http_count        | Currently Open HTTP Connections         | Number of HTTP connections on a node                 | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+
   | total_opened_http_count          | Total Open HTTP Connections             | Total number of HTTP connections on a node           | >= 0        | CSS cluster - cloud service node | 1 minute                       |
   +----------------------------------+-----------------------------------------+------------------------------------------------------+-------------+----------------------------------+--------------------------------+

Dimension
---------

.. table:: **Table 2** Dimension description

   ========== ===========
   Key        Value
   ========== ===========
   cluster_id CSS cluster
   ========== ===========
