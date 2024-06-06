:original_name: en-us_topic_0000001528379253.html

.. _en-us_topic_0000001528379253:

Overview
========

You can scale in or out a cluster and change cluster specifications. In this way, you can improve cluster efficiency and reduce O&M costs.

:ref:`Scaling Out a Cluster <en-us_topic_0000001477899164>`

-  If a data node (ess) processes many data writing and querying requests and responds slowly, you can expand its storage capacity to improve its efficiency. If some nodes turn unavailable due to the excessive data volume or misoperations, you can add new nodes to ensure the cluster availability.
-  **Cold data nodes** (ess-cold) are used to share the workload of data nodes. To prevent cold data loss, you can expand the storage capacity of the cold data node or add new ones.

:ref:`Changing Specifications <en-us_topic_0000001477739368>`

-  If the allocation of new indexes or shards takes too long or the node coordination and scheduling are inefficient, you can change the master node (ess-master) specifications.
-  If too many tasks need to be distributed or too many results have been aggregated, you can change the client node (ess-client) specifications.
-  If the speed of data writing and query decreases suddenly, you can change the data node (ess) specifications.
-  If cold data query becomes slow, you can change the cold node (ess-cold) specifications.

:ref:`Scaling in a Cluster <en-us_topic_0000001528299597>`

-  If a cluster can process existing data without fully using its resources, you can scale in the cluster to reduce costs.

:ref:`Removing Specified Nodes <en-us_topic_0000001477899184>`

-  If a cluster can process existing data without fully using its nodes, you can remove one or more specified nodes from the cluster to reduce costs.

:ref:`Replacing a Specified Node <en-us_topic_0000001477579404>`

-  If a node in the cluster is faulty, you can create a new node with the same specifications to replace it.

:ref:`Adding Master/Client Nodes <en-us_topic_0000001477899188>`

-  If the workloads on the data plane of a cluster increase, you can dynamically scale the cluster by adding master/client nodes.

:ref:`Changing the Security Mode <en-us_topic_0000001528379285>`

After a cluster is created, its security mode can be changed using the following methods:

-  Change a non-security cluster to a security cluster that uses HTTP or HTTPS protocol.
-  Change a security cluster that uses HTTP or HTTPS protocol to a non-security cluster.
-  Change the protocol of a security cluster.

:ref:`Changing AZs <en-us_topic_0000001528299585>`

You can **Add AZ** or **Migrate AZ**.

-  **Add AZ**: Add one or two AZs to a single-AZ cluster, or add an AZ to a dual-AZ cluster to improve cluster availability.
-  **Migrate AZ**: Completely migrate data from the current AZ to another AZ that has sufficient resources.
