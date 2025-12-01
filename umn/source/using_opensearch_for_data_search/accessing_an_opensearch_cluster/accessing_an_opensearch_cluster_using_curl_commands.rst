:original_name: css_01_0030.html

.. _css_01_0030:

Accessing an OpenSearch Cluster Using cURL Commands
===================================================

Open-source OpenSearch provides a series of RESTful APIs. You can run cURL commands to access these APIs using tools such as OpenSearch Dashboards and Postman. This topic describes how to run cURL commands to access an OpenSearch cluster.

Prerequisites
-------------

-  The target CSS OpenSearch cluster is available.
-  An ECS has been created, and it is in the same VPC and security group as the CSS cluster.

   -  If they are not in the same security group, modify the ECS security group, or configure its inbound and outbound rules to allow all access from the cluster. For details, see `Configuring Security Group Rules <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0030878383.html>`__.
   -  For details about how to use an ECS, see `Creating and Logging In to a Linux ECS <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0092494193.html>`__.

Accessing a Cluster
-------------------

#. Obtain the private network address of the cluster. It is used to access the cluster.

   This topic uses a private IP address as an example to describe how to access a cluster. The cluster access address varies depending on the network configurations used. For details, see :ref:`Network Configuration <en-us_topic_0000001975823337__section855085010198>`.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.

   c. In the cluster list, obtain the target cluster's private IP address from the **Private IP Address** column. Generally, the IP address format is *<host>*:*<port>* or *<host>*:*<port>*,\ *<host>*:*<port>*.

      If the cluster has only one node, the IP address and port number of this single node are displayed, for example, **10.62.179.32:9200**. If the cluster has multiple nodes and all of them are data nodes, the IP addresses and port numbers of all these nodes are displayed; if some of them are client nodes, only the IP addresses and port numbers of these client nodes are displayed; for example, **10.62.179.32:9200,10.62.179.33:9200**.

#. Run one of the following commands on the ECS to access the cluster. The access command varies depending on the security mode of the cluster.

   -  For a cluster with the security mode disabled:

      .. code-block::

         curl "http://<host>:<port>"

   -  For a security-mode cluster that uses HTTP:

      .. code-block::

         curl -u <user>:<password> "http://<host>:<port>"

   -  For a security-mode cluster that uses HTTPS:

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

   Example command:

   .. code-block::

      curl "http://10.62.176.32:9200"

   Example response:

   .. code-block::

      HTTP/1.1 200 OK
      content-type: application/json; charset=UTF-8
      content-length: 513

      {
        "name" : "css-xxx-ess-esn-3-1",
        "cluster_name" : "css-xxx",
        "cluster_uuid" : "xxx_uuid",
        "version" : {
          "number" : "7.10.2",
          "build_type" : "tar",
          "build_hash" : "unknown",
          "build_date" : "unknown",
          "build_snapshot" : true,
          "lucene_version" : "9.12.1",
          "minimum_wire_compatibility_version" : "7.10.0",
          "minimum_index_compatibility_version" : "7.0.0"
        },
        "tagline" : "The OpenSearch Project: https://opensearch.org/"
      }

   .. note::

      For more commands, see the `OpenSearch documentation <https://docs.opensearch.org/latest/>`__.
