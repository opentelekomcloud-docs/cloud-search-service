:original_name: css_01_0443.html

.. _css_01_0443:

Accessing an OpenSearch Cluster Using cURL Commands
===================================================

Open-source Elasticsearch provides a series of RESTful APIs. You can run cURL commands to access these APIs using tools such as Kibana and Postman. This topic describes how to use cURL commands to access an Elasticsearch or OpenSearch cluster.

Prerequisites
-------------

-  CSS has an Elasticsearch or OpenSearch cluster that is available.
-  An ECS has been created, and it is in the same VPC and security group as the CSS cluster.

   -  If they are not in the same security group, modify the ECS security group, or configure the inbound and outbound rules of the group to allow all access from the cluster. For details, see `Configuring Security Group Rules <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0030878383.html>`__.
   -  For details about how to use an ECS, see `Creating and Logging In to a Linux ECS <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0092494193.html>`__.

Accessing a Cluster
-------------------

#. Obtain the private network address of the cluster. It is used to access the cluster.

   This topic uses a private IP address as an example to describe how to access a cluster. The cluster access address varies with the network configurations used. For details, see :ref:`Network Configuration <css_01_0381__section855085010198>`.

   a. In the navigation pane on the left, choose **Clusters**.

   b. In the cluster list, obtain the IP address of the cluster you want to access from the **Private Network Address** column. Generally, the IP address format is *<host>*\ **:**\ *<port>* or *<host>*\ **:**\ *<port>*\ **,**\ *<host>*\ **:**\ *<port>*.

      If the cluster has only one node, the IP address and port number of this one node are displayed, for example, **10.62.179.32:9200**. If the cluster has multiple nodes, the IP addresses and port numbers of all nodes are displayed, for example, **10.62.179.32:9200,10.62.179.33:9200**.

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
      | <host>                            | IP address of each node in the cluster. If the cluster contains multiple nodes, there will be multiple IP addresses. You can use any of them.                               |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | <port>                            | Port number for accessing a cluster node. Generally, the port number is 9200.                                                                                               |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | <user>                            | Username for accessing the cluster.                                                                                                                                         |
      +-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | <password>                        | Password of the user.                                                                                                                                                       |
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

   .. note::

      For more commands, see the `Elasticsearch documentation <https://www.elastic.co/guide/en/elasticsearch/reference/current/rest-apis.html?spm=a2c4g.11186623.0.0.18211315kMUlbd>`__.
