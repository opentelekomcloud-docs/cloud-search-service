:original_name: css_02_0152.html

.. _css_02_0152:

How Do I Connect In-house Developed OpenSearch Dashboards to an OpenSearch Cluster in CSS?
==========================================================================================

Constraints
-----------

Only OpenSearch Dashboards images of the OSS version can be connected to OpenSearch clusters in CSS.

Procedure
---------

#. Create an ECS.

   -  The ECS must be within the same VPC as the CSS cluster.
   -  Port 5601 must be allowed by the security group associated with the ECS.
   -  An EIP must be allocated to the ECS.

   For details, see Elastic Cloud Server User Guide.

#. Obtain the address for accessing the OpenSearch cluster of CSS.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.

   c. In the cluster list, obtain the target cluster's private IP address from the **Private IP Address** column. Generally, the IP address format is *<host>*:*<port>* or *<host>*:*<port>*,\ *<host>*:*<port>*.

      If the cluster has only one node, the IP address and port number of this single node are displayed, for example, **10.62.179.32:9200**. If the cluster has multiple nodes and all of them are data nodes, the IP addresses and port numbers of all these nodes are displayed; if some of them are client nodes, only the IP addresses and port numbers of these client nodes are displayed; for example, **10.62.179.32:9200,10.62.179.33:9200**.

#. Install OpenSearch Dashboards on the ECS and modify the **opensearch_dashboards.yml** configuration file.

   -  The following is an example of the configuration file for a security-mode cluster:

      .. code-block::

         opensearch.username: "***" //Username of the security cluster
         opensearch.password: "***" //Password of the security cluster
         opensearch.ssl.verificationMode: none
         server.ssl.enabled: false
         server.rewriteBasePath: false
         server.port: 5601
         logging.dest: /home/Ruby/log/kibana.log
         pid.file: /home/Ruby/run/kibana.pid
         server.host: 192.168.xxx.xxx  //IP address or DNS name of the OpenSearch Dashboards server. localhost is recommended.
         opensearch.hosts: http://10.0.0.xxx:9200   //Address for accessing the OpenSearch cluster
         opensearch.requestHeadersWhitelist: ["securitytenant","Authorization"]
         opensearch_security.multitenancy.enabled: true
         opensearch_security.multitenancy.tenants.enable_global: true
         opensearch_security.multitenancy.tenants.enable_private: true
         opensearch_security.multitenancy.tenants.preferred: ["Private", "Global"]
         opensearch_security.multitenancy.enable_filter: false

      .. note::

         To access a security-mode cluster, the opendistro_security_kibana plug-in must be installed. For details, see `security-kibana-plugin <https://github.com/opendistro-for-elasticsearch/security-kibana-plugin/tags?after=v1.3.0.0>`__. The plug-in version must be the same as that of the cluster. To check the plug-in version, run the **GET \_cat/plugins** command.

   -  The following is an example of the configuration file for a non-security mode cluster:

      .. code-block::

         server.port: 5601
         logging.dest: /home/Ruby/log/opensearch-dashboards.log
         pid.file: /home/Ruby/run/opensearch-dashboards.pid
         server.host: 192.168.xxx.xxx  //IP address or DNS name of the OpenSearch Dashboards server. localhost is recommended.
         opensearch.hosts: http://10.0.0.xxx:9200   //Address for accessing the OpenSearch cluster

#. Use a browser on your local PC to connect to the EIP associated with the ECS. The URL is **http://EIP:5601**. Log in to OpenSearch Dashboards to access the OpenSearch cluster.
