:original_name: css_01_0063.html

.. _css_01_0063:

Connecting to a Cluster Using cURL Commands
===========================================

To query or analyze data in Elasticsearch, you often need to connect to your cluster from an external client (such as an ECS). This topic describes how to use cURL commands to access an Elasticsearch cluster.

Prerequisites
-------------

-  The target Elasticsearch cluster is available.
-  An ECS has been created, and it is in the same VPC and security group as the CSS cluster.

   -  If they are not in the same security group, modify the ECS security group, or configure the inbound and outbound rules of the group to allow all access from the cluster. For details, see `Configuring Security Group Rules <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0030878383.html>`__.
   -  For details about how to use an ECS, see `Creating and Logging In to a Linux ECS <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0092494193.html>`__.

Accessing a Cluster
-------------------

#. Obtain the private network address of the cluster. It is used to access the cluster.

   This topic uses a private IP address as an example to describe how to access a cluster. The cluster access address varies with the network configurations used. For details, see :ref:`Obtaining the Cluster Access Address <en-us_topic_0000001975823337__section855085010198>`.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, obtain the target cluster's internal network address from the **Internal Network Address** column. Typical address format: *<host>*:*<port>* or *<host>*:*<port>*,\ *<host>*:*<port>*. Example: **10.62.179.32:9200,10.62.179.33:9200**.

      If the cluster has client nodes, only the IP addresses and ports of all the client nodes are displayed. Otherwise, the IP addresses and ports of all data nodes and cold data nodes are displayed.

#. Run one of the following commands on the ECS to access the cluster. The access command varies according to the security mode of the cluster.

   -  Cluster in non-security mode

      .. code-block::

         curl "http://<host>:<port>"

   -  Cluster in security mode + HTTP

      .. code-block::

         curl -u <user>:<password> "http://<host>:<port>"

   -  Cluster in security mode + HTTPS

      .. code-block::

         curl -u <user>:<password> -k "https://<host>:<port>"

   .. table:: **Table 1** Variables

      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Variable                          | Description                                                                                                                                                                 |
      +===================================+=============================================================================================================================================================================+
      | host                              | IP address of each node in the cluster. If the cluster contains multiple nodes, there will be multiple IP addresses. You can use any of them.                               |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | port                              | Port number for accessing a cluster node. Generally, the port number is 9200.                                                                                               |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | user                              | Username for accessing the cluster.                                                                                                                                         |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | password                          | Password of the user.                                                                                                                                                       |
      |                                   |                                                                                                                                                                             |
      |                                   | If the password contains special characters, enclose the username and password in single quotation marks, for example, **curl -u "user:password!" "http://<host>:<port>"**. |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   An access example is as follows:

   .. code-block::

      curl "http://10.62.176.32:9200"

   Information similar to the following is displayed:

   .. code-block::

      HTTP/1.1 200 OK
      content-type: application/json; charset=UTF-8
      content-length: 513

      {
          "name" : "xxx-1",
          "cluster_name" : "xxx",
          "cluster_uuid" : "xxx_uuid",
          "version" : {
              "number" : "7.10.2",
              "build_flavor" : "oss",
              "build_type" : "tar",
              "build_hash" : "unknown",
              "build_date" : "unknown",
              "build_snapshot" : true,
              "lucene_version" : "8.7.0",
              "minimum_wire_compatibility_version" : "6.7.0",
              "minimum_index_compatibility_version" : "6.0.0-beta1"
          },
          "tagline" : "You Know, for Search"
      }

   For more commands, see the `Elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html?spm=a2c4g.11186623.0.0.18211315kMUlbd>`__.
