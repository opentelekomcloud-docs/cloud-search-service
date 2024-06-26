:original_name: en-us_topic_0000001477739384.html

.. _en-us_topic_0000001477739384:

Context
=======

You can store hot data on SSD to achieve the optimal query performance, and store historical data in OBS to reduce data storage costs.

Application Scenarios
---------------------

A large volume of data is written to and stored in SSDs. If historical data is no longer updated (is turned into cold data) and its QPS decreases, you can call CSS APIs to dump hot data from SSDs to OBS buckets. This operation freezes indexes, decoupling compute from storage.

Constraints
-----------

-  Currently, only Elasticsearch clusters of versions 7.6.2 and 7.10.2 and OpenSearch clusters of version 1.3.6 support decoupled storage and computing.
-  The storage-compute decoupling feature depends on OBS. Therefore, you must comply with the restrictions on OBS bandwidth and QPS. If these restrictions are violated, the performance of queries on OBS will deteriorate. For example, the speed of restoring shards and querying data will become slow.
