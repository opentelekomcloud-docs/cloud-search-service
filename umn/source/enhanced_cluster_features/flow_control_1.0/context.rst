:original_name: en-us_topic_0000001477739408.html

.. _en-us_topic_0000001477739408:

Context
=======

Feature Description
-------------------

CSS can control traffic at the node level. You can configure the blacklist and whitelist, the maximum concurrent HTTP connections, and the maximum HTTP connections for a node. You can also configure the maximum heap memory used by specific request paths, the maximum CPU usage, and block access in one click, and collect statistics on node access IP addresses and URIs. Each function has an independent control switch, which is disabled by default. To restore default values of parameters, set them to **null**.

If flow control is enabled, requests will be blocked at the entry, which relieves the cluster pressure in high-concurrency scenario and avoids unavailability issues.

-  **HTTP/HTTPS Flow Control**

   -  You can control client IP address access by setting IP addresses and subnets in HTTP/HTTPS blacklist or whitelist. If an IP address is in the blacklist, the client is disconnected and all its request are rejected. Whitelist rules take precedence over blacklist rules. If a client IP address exists in both the blacklist and whitelist, the client request will not be rejected.
   -  HTTP/HTTPS concurrent connection flow control limits the total number of HTTP connections to a node per second.
   -  HTTP/HTTPS new connection flow control limits the number of new connections to a node.

-  **Memory Flow Control**

   Memory flow control limits request paths based on the node heap memory. You can configure memory flow control whitelist, global memory usage threshold, and heap memory threshold for a single path. Global memory flow control threshold takes precedence over the memory threshold of a single path. Paths in the whitelist will not be blocked in memory flow control.

-  **Global Path Whitelist for Flow Control**

   You can configure the global path whitelist for flow control as required when you need to use custom plug-ins.

-  **Request Sampling**

   Request sampling can record the number of access requests from client IP addresses and the request paths of sampled users. Based on the statistics, you can identify the access traffic of client IP addresses and analyze the access traffic of request paths.

-  **Flow Control**

   Flow control provides an independent API for viewing traffic statistics and records the number of times the API is triggered. You can evaluate the flow control threshold and analyze the cluster load based on the statistics.

-  **Access Logs**

   Access logs record the URLs and bodies of HTTP/HTTPS requests received by nodes within a period of time. You can analyze the current traffic pressure based on the access logs.

-  **CPU Flow Control**

   You can configure the node CPU usage threshold to limit the accessed traffic on a single node.

-  **One-click Traffic Blocking**

   One-click access blocking can block all the access traffic of a node, excluding the traffic from Kibana and Elasticsearch monitor APIs.

Constraints
-----------

-  Currently, only versions 7.6.2 and 7.10.2 support the flow control feature.
-  Flow control may affect the performance of some nodes.

-  If flow control is enabled, user requests that exceed the flow control threshold will be rejected.
-  Memory flow control and CPU flow control are based on request paths. The length and number of paths cannot be too large, or the cluster performance will be affected.
