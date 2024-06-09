:original_name: en-us_topic_0000001528379257.html

.. _en-us_topic_0000001528379257:

Context
=======

Feature Description
-------------------

CSS can control traffic at the node level. You can configure the blacklist and whitelist, the maximum concurrent HTTP connections, and the maximum HTTP connections for a node. You can also configure backpressure based on client traffic in the node memory and block access in one click. CSS can also collect statistics on node access IP addresses and URIs. Each function has an independent control switch, which is disabled by default. To restore default values of parameters, set them to **null**.

After the client write traffic backpressure and control is enabled, large requests will be rejected when too much node heap memory has been occupied. This function prevents nodes from being suspended and reduces the risk of node unavailability.

-  **HTTP/HTTPS flow control:**

   -  You can control client IP address access by setting IP addresses and subnets in HTTP/HTTPS blacklist or whitelist. If an IP address is in the blacklist, the client is disconnected and all its request are rejected. Whitelist rules take precedence over blacklist rules. If a client IP address exists in both the blacklist and whitelist, the client request will not be rejected.
   -  HTTP/HTTPS concurrent connection flow control limits the total number of HTTP connections to a node per second.
   -  HTTP/HTTPS new connection flow control limits the number of new connections to a node.

-  **Memory flow control**

   Memory flow control limits the write traffic based on the node heap memory. You can back pressure requests to the client, trigger resource recycling as much as possible, and then accept requests based on the available heap memory.

-  **Request sampling**

   Request sampling can record the access of client IP addresses and the type of requests from the client. Based on the statistics, you can identify the access traffic of client IP addresses and analyze the client write and query requests.

-  **One-click traffic blocking**

   One-click access blocking can block all the access traffic of a node, excluding the traffic from Kibana and CSS O&M and monitoring APIs.

-  **Flow control**

   Flow control provides an independent API for viewing traffic statistics and records the number of current client connections and client backpressure connections. You can evaluate the flow control threshold and analyze the cluster loads based on the statistics.

-  **Access logs**

   Access logs record the URLs and bodies of HTTP/HTTPS requests received by nodes within a period of time. You can analyze the current traffic pressure based on the access logs.

Constraints
-----------

-  Currently, only Elasticsearch clusters of versions 7.6.2 and 7.10.2 support the traffic control feature.
-  Elasticsearch clusters of versions 7.6.2 and 7.10.2 created after February 2023 support only traffic control 2.0. Clusters created before February 2023 support only traffic control 1.0. For details, see :ref:`Flow Control 1.0 <en-us_topic_0000001477899152>`.
