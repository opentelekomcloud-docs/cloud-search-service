:original_name: en-us_topic_0000001477419776.html

.. _en-us_topic_0000001477419776:

Connecting User-Built Kibana to an Elasticsearch Cluster
========================================================

To interconnect user-built Kibana with CSS Elasticsearch clusters, the following conditions must be met:

-  The local environment must support access from external networks.
-  Kibana is built using ECS in the same VPC as Elasticsearch. Kibana can be accessed from the local public network.
-  Only Kibana images of the OSS version can be connected to Elasticsearch on CSS.

Example of a Kibana configuration file:

-  Security mode:

   .. code-block::

      elasticsearch.username: "***"
      elasticsearch.password: "***"
      elasticsearch.ssl.verificationMode: none
      server.ssl.enabled: false
      server.rewriteBasePath: false
      server.port: 5601
      logging.dest: /home/Ruby/log/kibana.log
      pid.file: /home/Ruby/run/kibana.pid
      server.host: 192.168.xxx.xxx
      elasticsearch.hosts: https://10.0.0.xxx:9200
      elasticsearch.requestHeadersWhitelist: ["securitytenant","Authorization"]
      opendistro_security.multitenancy.enabled: true
      opendistro_security.multitenancy.tenants.enable_global: true
      opendistro_security.multitenancy.tenants.enable_private: true
      opendistro_security.multitenancy.tenants.preferred: ["Private", "Global"]
      opendistro_security.multitenancy.enable_filter: false

   .. note::

      -  In security mode, the **opendistro_security_kibana** plug-in must be installed. For details, see https://github.com/opendistro-for-elasticsearch/security-kibana-plugin/tags?after=v1.3.0.0.
      -  The version of the installed plug-in must be the same as that of the cluster. To check the version of the plug-in version, run the **GET \_cat/plugins** command.

-  Non-security mode

   .. code-block::

      server.port: 5601
      logging.dest: /home/Ruby/log/kibana.log
      pid.file: /home/Ruby/run/kibana.pid
      server.host: 192.168.xxx.xxx
      elasticsearch.hosts: http://10.0.0.xxx:9200
