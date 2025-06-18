:original_name: css_02_0097.html

.. _css_02_0097:

How Do I Connect In-house Developed Kibana to an Elasticsearch Cluster in CSS?
==============================================================================

Constraints
-----------

Only Kibana images of the OSS version can be connected to Elasticsearch clusters in CSS.

Procedure
---------

#. Create an ECS.

   -  The ECS must be within the same VPC as the CSS cluster.
   -  Port 5601 must be allowed by the security group associated with the ECS.
   -  An EIP must be allocated to the ECS.

   For details, see *Elastic Cloud Server (ECS) User Guide*.

#. Obtain the address for accessing the Elasticsearch cluster of CSS.

   a. In the navigation pane on the left, choose **Clusters**.

   b. In the cluster list, obtain the IP address of the cluster you want to access from the **Private Network Address** column. Generally, the IP address format is *<host>*\ **:**\ *<port>* or *<host>*\ **:**\ *<port>*\ **,**\ *<host>*\ **:**\ *<port>*.

      If the cluster has only one node, the IP address and port number of this one node are displayed, for example, **10.62.179.32:9200**. If the cluster has multiple nodes, the IP addresses and port numbers of all nodes are displayed, for example, **10.62.179.32:9200,10.62.179.33:9200**.

#. Install Kibana on the ECS and modify the configuration file.

   -  The following is an example of the configuration file for a security-mode cluster:

      .. code-block::

         elasticsearch.username: "***"   //Username of the security cluster
         elasticsearch.password: "***"   //Password of the security cluster
         elasticsearch.ssl.verificationMode: none
         server.ssl.enabled: false
         server.rewriteBasePath: false
         server.port: 5601
         logging.dest: /home/Ruby/log/kibana.log
         pid.file: /home/Ruby/run/kibana.pid
         server.host: 192.168.xxx.xxx   //IP address or DNS name of the Kibana server. localhost is recommended.
         elasticsearch.hosts: http://10.0.0.xxx:9200   //Address for accessing the Elasticsearch cluster
         elasticsearch.requestHeadersWhitelist: ["securitytenant","Authorization"]
         opendistro_security.multitenancy.enabled: true
         opendistro_security.multitenancy.tenants.enable_global: true
         opendistro_security.multitenancy.tenants.enable_private: true
         opendistro_security.multitenancy.tenants.preferred: ["Private", "Global"]
         opendistro_security.multitenancy.enable_filter: false

      .. note::

         -  In security mode, the opendistro_security_kibana plug-in must be installed. For details, see `security-kibana-plugin <https://github.com/opendistro-for-elasticsearch/security-kibana-plugin/tags?after=v1.3.0.0>`__.
         -  The version of the installed plug-in must be the same as that of the cluster. To check the plug-in version, run the **GET \_cat/plugins** command.

   -  The following is an example of the configuration file for a non-security mode cluster:

      .. code-block::

         server.port: 5601
         logging.dest: /home/Ruby/log/kibana.log
         pid.file: /home/Ruby/run/kibana.pid
         server.host: 192.168.xxx.xxx   //IP address or DNS name of the Kibana server. localhost is recommended.
         elasticsearch.hosts: http://10.0.0.xxx:9200   //Address for accessing the Elasticsearch cluster

#. Use a browser on your local PC to access the EIP bound to the ECS. The URL is **http://EIP:5601**. Log in to Kibana to access the Elasticsearch cluster.
