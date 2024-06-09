:original_name: en-us_topic_0000001477899224.html

.. _en-us_topic_0000001477899224:

Stopping Index Synchronization
==============================

You can specify multiple indexes or use wildcard to match the target indexes and terminate their synchronization tasks. Subsequent modifications to the indexes in the primary cluster will not be synchronized to the secondary cluster. The read-only state of the indexes in the secondary cluster is cancelled, and new data can be written to the secondary cluster.

An example request is as follows:

.. code-block:: text

   PUT log*/stop_remote_sync
