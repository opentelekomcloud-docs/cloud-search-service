:original_name: en-us_topic_0000001477739356.html

.. _en-us_topic_0000001477739356:

Best Practices
==============

This section describes how to switch from the primary cluster to the secondary cluster when the primary cluster is faulty.

1. If the synchronization of specified indexes has been configured between the primary and secondary clusters.

(1) Call the API for stopping index synchronization in the secondary cluster. In this case, the read and write traffic can be switched to the secondary cluster.

(2) After the primary cluster recovers, call the index synchronization API to synchronize data from the secondary cluster to the primary cluster.

2. If the matching pattern for index synchronization has been established between the primary and secondary clusters.

(1) Call the API for deleting the created matching pattern for index synchronization in the secondary cluster.

(2) Call the API for stopping index synchronization on the secondary cluster (using **\*** for matching). In this case, the read and write traffic can be switched to the secondary cluster.

(3) After the primary cluster recovers, call the index synchronization API to synchronize data from the secondary cluster to the primary cluster.
