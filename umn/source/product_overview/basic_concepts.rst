:original_name: en-us_topic_0000001715624649.html

.. _en-us_topic_0000001715624649:

Basic Concepts
==============

Cluster
-------

CSS provides functions on a per cluster basis. A cluster represents an independent search service that consists of multiple nodes.

Index
-----

An index stores Elasticsearch data. It is a logical space in which one or more shards are grouped.

Shard
-----

An index can potentially store a large amount of data that can exceed the hardware limits of a single node. To solve this problem, Elasticsearch provides the ability to subdivide your index into multiple pieces called shards. When you create an index, you can simply define the number of shards that you want. Each shard is in itself a fully-functional and independent "index" that can be hosted on any node in the cluster.

You need to specify the number of shards before creating an index and cannot change the number after the index is successfully created.

Replica
-------

A replica is a copy of the actual storage index in a shard. It can be understood as a backup of the shard. Replicas help prevent single point of failures (SPOFs). You can increase or decrease the number of replicas based on your service requirements.

Document
--------

An entity for Elasticsearch storage. Equivalent to the row in the RDB, the document is the basic unit that can be indexed.

Document Type
-------------

Similar to a table in the RDB, type is used to distinguish between different data.

In versions earlier than Elasticsearch 7.\ *x*, each index can contain multiple document types. Elasticsearch defines a type for each document.

Elasticsearch 7.\ *x* and later versions only support documents of the .doc type.

Mapping
-------

A mapping is used to restrict the type of a field and can be automatically created based on data. It is similar to the schema in the database.

Field
-----

The field is the minimum unit of a document. It is similar to the column in the database.
