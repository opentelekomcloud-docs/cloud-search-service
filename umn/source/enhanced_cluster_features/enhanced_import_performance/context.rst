:original_name: en-us_topic_0000001533829376.html

.. _en-us_topic_0000001533829376:

Context
=======

Feature Description
-------------------

CSS provides enhanced data import function. It optimizes bulk route, and speeds up processing through indexes and word segmentation, improving import performance and reduces bulk rejection. This function applies to clusters that contain a large number of index shards and text indexes, and have high import throughput.

Constraints
-----------

Currently, only Elasticsearch clusters of version 7.10.2 and OpenSearch clusters of version 1.3.6 support the import performance enhancement.

Prerequisites
-------------

An Elasticsearch cluster of version 7.10.2 or OpenSearch cluster has been created on the CSS console.

Precautions
-----------

-  After the local shard preferential bulk routing optimization and bulk routing optimization are enabled, data writing is not routed based on IDs, and routing-related functions are restricted. For example, ID-based GET requests may fail. The optimization of local shard preferential bulk routing depends on the random distribution of client bulk requests and the balanced distribution of primary shards.
-  If **index.native_speed_up** (the text index acceleration function) is enabled, **index_sorting** is not supported.
-  Prerequisites for enabling **index.native_analyzer**:

   #. The **index.native_speed_up** function has been enabled.
