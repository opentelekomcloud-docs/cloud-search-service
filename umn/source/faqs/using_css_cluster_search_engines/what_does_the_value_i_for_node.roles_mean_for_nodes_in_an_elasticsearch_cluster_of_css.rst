:original_name: css_02_0127.html

.. _css_02_0127:

What Does the Value i for node.roles Mean for Nodes in an Elasticsearch Cluster of CSS?
=======================================================================================

Function
--------

If the value of **node.roles** of a client node is **i**, then is this client node an ingest node?

-  Are there coordinating only nodes in clusters? Are the client requests distributed to coordinating nodes?
-  Are ingest nodes in idle state when there are no ingest requests?

Solution
--------

If the value of **node.roles** of a client node is **i**, the ingest node mode is enabled.

-  The coordinating only nodes of Elasticsearch are called client nodes in CSS. If a cluster has no client nodes, client requests will be distributed to all nodes.
-  An ingest node functions as a set of ELK for data conversion. If there is no ingest requests, ingest nodes are not in the idle state.
