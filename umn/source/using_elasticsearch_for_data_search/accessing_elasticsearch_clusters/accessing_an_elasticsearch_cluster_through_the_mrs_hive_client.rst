:original_name: css_01_0391.html

.. _css_01_0391:

Accessing an Elasticsearch Cluster Through the MRS Hive Client
==============================================================

The Elasticsearch-Hadoop (ES-Hadoop) connector combines the massive data storage and in-depth processing capabilities of Hadoop with the real-time search and analysis capabilities of Elasticsearch. It allows you to quickly get to know big data and work better in the Hadoop ecosystem.

This topic uses the ES-Hadoop of MRS as an example to describe how to connect to a CSS cluster. You can configure any other applications that need to use the Elasticsearch cluster. Ensure the network connection between the client and the Elasticsearch cluster is normal.

Prerequisites
-------------

-  The CSS cluster is available.
-  The client can communicate with the CSS cluster.

-  The CSS and MRS clusters are in the same region, AZ, VPC, and subnet.


   .. figure:: /_static/images/en-us_image_0000001972384697.png
      :alt: **Figure 1** CSS cluster information

      **Figure 1** CSS cluster information

Accessing a Cluster
-------------------

#. Obtain the private network address of the cluster. It is used to access the cluster.

   This topic uses a private IP address as an example to describe how to access a cluster. The cluster access address varies with the network configurations used. For details, see :ref:`Network Configuration <css_01_0381__section855085010198>`.

   a. In the navigation pane on the left, choose **Clusters**.

   b. In the cluster list, obtain the IP address of the cluster you want to access from the **Private Network Address** column. Generally, the IP address format is *<host>*\ **:**\ *<port>* or *<host>*\ **:**\ *<port>*\ **,**\ *<host>*\ **:**\ *<port>*.

      If the cluster has only one node, the IP address and port number of this one node are displayed, for example, **10.62.179.32:9200**. If the cluster has multiple nodes, the IP addresses and port numbers of all nodes are displayed, for example, **10.62.179.32:9200,10.62.179.33:9200**.

#. Log in to an MRS cluster node.

#. Run the cURL command on an MRS cluster node to check the network connectivity. Ensure every node in the MRS cluster can connect to the CSS cluster.

   -  Cluster in non-security mode

      .. code-block::

         curl -X GET http://<host>:<port>

   -  Cluster in security mode + HTTP

      .. code-block::

         curl -X GET http://<host>:<port> -u <user>:<password>

   -  Cluster in security mode + HTTPS

      .. code-block::

         curl -X GET https://<host>:<port> -u <user>:<password> -ik

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

#. Download the `ES-Hadoop lib package <https://www.elastic.co/downloads/hadoop>`__ and decompress it to obtain the **elasticsearch-hadoop-x.x.x.jar** file. The version must be the same as the CSS cluster version. For example, if the CSS cluster version is 7.6.2, you are advised to download **elasticsearch-hadoop-7.6.2.zip**.

#. Download the httpclient dependency package `commons-httpclient:commons-httpclient-3.1.jar <https://mvnrepository.com/artifact/commons-httpclient/commons-httpclient/3.1>`__. In the package name, **3.1** indicates the version number. Select the package of the version you need.

#. Install the MRS client. If the MRS client has been installed, skip this step.

#. Log in to the MRS client. Upload the JAR dependency packages of ES-Hadoop and httpclient to the MRS client.

#. Create an HDFS directory on the MRS client. Upload the ES-Hadoop lib package and the httpclient dependency package to the directory.

   .. code-block::

      hadoop fs -mkdir /tmp/hadoop-es
      hadoop fs -put elasticsearch-hadoop-x.x.x.jar /tmp/hadoop-es
      hadoop fs -put commons-httpclient-3.1.jar /tmp/hadoop-es

#. Log in to the Hive client from the MRS client.

#. On the Hive client, add the ES-Hadoop lib package and the httpclient dependency package. This command is valid only for the current session.

   Enter **beeline** or **hive** to go to the execution page and run the following commands:

   .. code-block::

      add jar hdfs:///tmp/hadoop-es/commons-httpclient-3.1.jar;
      add jar hdfs:///tmp/hadoop-es/elasticsearch-hadoop-x.x.x.jar;

#. On the Hive client, create a Hive foreign table.

   -  Cluster in non-security mode

      .. code-block::

         CREATE EXTERNAL table IF NOT EXISTS student(
            id BIGINT,
            name STRING,
            addr STRING
         )
         STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
         TBLPROPERTIES(
             'es.nodes' = 'xxx.xxx.xxx.xxx:9200',
             'es.port' = '9200',
             'es.net.ssl' = 'false',
             'es.nodes.wan.only' = 'false',
             'es.nodes.discovery'='false',
             'es.input.use.sliced.partitions'='false',
             'es.resource' = 'student/_doc'
         );

   -  Cluster in security mode + HTTP

      .. code-block::

         CREATE EXTERNAL table IF NOT EXISTS student(
            id BIGINT,
            name STRING,
            addr STRING
         )
         STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
         TBLPROPERTIES(
             'es.nodes' = 'xxx.xxx.xxx.xxx:9200',
             'es.port' = '9200',
             'es.net.ssl' = 'false',
             'es.nodes.wan.only' = 'false',
             'es.nodes.discovery'='false',
             'es.input.use.sliced.partitions'='false',
             'es.nodes.client.only'='true',
             'es.resource' = 'student/_doc',
             'es.net.http.auth.user' = 'username',
             'es.net.http.auth.pass' = 'password'
         );

   -  Cluster in security mode + HTTPS

      a. Obtain the security certificate **CloudSearchService.cer**.

         #. Log in to the CSS management console.
         #. In the navigation pane, choose **Clusters**. The cluster list is displayed.
         #. Click the name of a cluster to go to the cluster details page.
         #. On the **Configuration** page, click **Download Certificate** next to **HTTPS Access**.

      b. Convert the security certificate **CloudSearchService.cer**. Upload the downloaded security certificate to the client and use keytool to convert the .cer certificate into a .jks certificate that can be read by Java.

         -  In Linux, run the following command to convert the certificate:

            .. code-block::

               keytool -import -alias newname -keystore ./truststore.jks -file ./CloudSearchService.cer

         -  In Windows, run the following command to convert the certificate:

            .. code-block::

               keytool -import -alias newname -keystore .\truststore.jks -file .\CloudSearchService.cer

         In the preceding command, *newname* indicates the user-defined certificate name.

         After this command is executed, you will be prompted to set the certificate password and confirm the password. Securely store the password. It will be used for accessing the cluster.

      c. Put the .jks file to the same path of each node in the MRS cluster, for example, **/tmp**. You can run the **scp** command to transfer the file. Ensure user **omm** has the permission to read the file. You can run the following command to set the permission:

         .. code-block::

            chown -R omm truststore.jks

      d. Create a Hive foreign table.

         .. code-block::

            CREATE EXTERNAL table IF NOT EXISTS student(
               id BIGINT,
               name STRING,
               addr STRING
            )
            STORED BY 'org.elasticsearch.hadoop.hive.EsStorageHandler'
            TBLPROPERTIES(
                'es.nodes' = 'https://xxx.xxx.xxx.xxx:9200',
                'es.port' = '9200',
                'es.net.ssl' = 'true',
                'es.net.ssl.truststore.location' = 'cerFilePath',
                'es.net.ssl.truststore.pass' = 'cerPassword',
                'es.nodes.wan.only' = 'false',
                'es.nodes.discovery'='false',
                'es.nodes.client.only'='true',
                'es.input.use.sliced.partitions'='false',
                'es.resource' = 'student/_doc',
                'es.net.http.auth.user' = 'username',
                'es.net.http.auth.pass' = 'password'
            );

   .. table:: **Table 2** ES-Hadoop parameters

      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                      | Default Value         | Description                                                                                                                                                                                                                                                                                       |
      +================================+=======================+===================================================================================================================================================================================================================================================================================================+
      | es.nodes                       | localhost             | Address for accessing the CSS cluster. You can check the private network address in the cluster list.                                                                                                                                                                                             |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.port                        | 9200                  | Port number for accessing a cluster. Generally, the port number is 9200.                                                                                                                                                                                                                          |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.nodes.wan.only              | false                 | Whether to perform node sniffing.                                                                                                                                                                                                                                                                 |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.nodes.discovery             | true                  | Whether to disable node discovery.                                                                                                                                                                                                                                                                |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.input.use.sliced.partitions | true                  | Whether to use slices. Its value can be:                                                                                                                                                                                                                                                          |
      |                                |                       |                                                                                                                                                                                                                                                                                                   |
      |                                |                       | -  **true**                                                                                                                                                                                                                                                                                       |
      |                                |                       | -  **false**                                                                                                                                                                                                                                                                                      |
      |                                |                       |                                                                                                                                                                                                                                                                                                   |
      |                                |                       | .. note::                                                                                                                                                                                                                                                                                         |
      |                                |                       |                                                                                                                                                                                                                                                                                                   |
      |                                |                       |    If this parameter is set to **true**, the index prefetch time may be significantly prolonged, and may even be much longer than the data query time. You are advised to set this parameter to **false** to improve query efficiency.                                                            |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.resource                    | NA                    | Specifies the index and type to be read and written.                                                                                                                                                                                                                                              |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.net.http.auth.user          | NA                    | Username for accessing the cluster. Set this parameter only if the security mode is enabled.                                                                                                                                                                                                      |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.net.http.auth.pass          | NA                    | Password of the user. Set this parameter only if the security mode is enabled.                                                                                                                                                                                                                    |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.net.ssl                     | false                 | Whether to enable SSL. If SSL is enabled, you need to configure the security certificate information.                                                                                                                                                                                             |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.net.ssl.truststore.location | NA                    | Path of the .jks certificate file, for example, **file:///tmp/truststore.jks**.                                                                                                                                                                                                                   |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.nodes.client.only           | false                 | Check whether the IP address of an independent Client node is configured for **es.nodes** (that is, whether the Client node is enabled during Elasticsearch cluster creation). If yes, change the value to **true**, or an error will be reported, indicating that the data node cannot be found. |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | es.net.ssl.truststore.pass     | NA                    | Password of the .jks certificate file.                                                                                                                                                                                                                                                            |
      +--------------------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   For details about ES-Hadoop configuration items, see the `official configuration description <https://www.elastic.co/guide/en/elasticsearch/hadoop/current/configuration.html>`__.

#. On the Hive client, insert data.

   .. code-block::

      INSERT INTO TABLE student VALUES (1, "Lucy", "address1"), (2, "Lily", "address2");

#. On the Hive client, execute a query.

   .. code-block::

      select * from student;

   The query result is as follows:

   .. code-block::

      +-------------+---------------+---------------+
      | student.id  | student.name  | student.addr  |
      +-------------+---------------+---------------+
      | 1           | Lucy          | address1      |
      | 2           | Lily          | address2      |
      +-------------+---------------+---------------+
      2 rows selected (0.116 seconds)

#. Log in to the CSS console and choose **Clusters**. Locate the target cluster and click **Access Kibana** in the **Operation** column.

#. On the **Dev Tools** page of Kibana, run a query and view the result.

   .. code-block:: text

      GET /student/_search


   .. figure:: /_static/images/en-us_image_0000001945226538.png
      :alt: **Figure 2** Kibana query result

      **Figure 2** Kibana query result
