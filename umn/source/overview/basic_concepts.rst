:original_name: css_04_0003.html

.. _css_04_0003:

Basic Concepts
==============

Cluster
-------

CSS provides functions on a per cluster basis. A cluster represents an independent search service that contains multiple nodes.

Index
-----

Index is similar to "database" in the relational database (RDB) and stores Elasticsearch data. It refers to a logical space that consists of one or more shards.

.. table:: **Table 1** Mapping between Elasticsearch and RDB

   ============= ======== ===== ======== ====== =======
   Elasticsearch Index    Type  Document Field  Mapping
   RDB           Database Table Row      Column Schema
   ============= ======== ===== ======== ====== =======

Shard
-----

An index can potentially store a large amount of data that exceeds the hardware limits of a single node. To solve this problem, Elasticsearch subdivides your index into multiple pieces called shards. When you create an index, you can simply define the number of shards that you want. Each shard is in itself a fully-functional and independent "index" that can be hosted on any node in the cluster.

You need to specify the number of shards before creating an index and cannot change the number of shards after the index is created.

Replica
-------

A replica is a copy of the actual storage index in a shard. It can be understood as a backup of the shard. Replicas help prevent single point of failures (SPOFs). You can increase or decrease the number of replicas based on your service requirements.

Document
--------

An entity for Elasticsearch storage. Equivalent to a row in the RDB, the document is the basic unit that can be indexed.

Type
----

Similar to a table in the RDB, type is used to distinguish between different data. One index can contain multiple document types. A document must be indexed to a document type inside an index.

Mapping
-------

A mapping is used to restrict the type of a field and is automatically created based on data. It is similar to a schema in the database.

Field
-----

Minimum unit of a document. A field is similar to a column in a database.
