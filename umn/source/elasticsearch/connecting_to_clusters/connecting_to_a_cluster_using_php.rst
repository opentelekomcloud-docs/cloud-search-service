:original_name: css_01_0139.html

.. _css_01_0139:

Connecting to a Cluster Using PHP
=================================

In big data search and analytics scenarios, developers often need to use programming languages to work with Elasticsearch clusters. However, the direct use of Elasticsearch's HTTP APIs can involve complex and error-prone coding. To simplify development, CSS Elasticsearch supports the official Elasticsearch PHP client. The client library (elasticsearch-php) provides comprehensive encapsulation of Elasticsearch APIs, enabling developers to perform index management, CRUD (Create, Read, Update, Delete) operations, and document searches through native PHP APIs.

Prerequisites
-------------

-  The target Elasticsearch cluster is available.

-  The server that runs the PHP code can communicate with the Elasticsearch cluster.

-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Obtaining the Cluster Access Address <en-us_topic_0000001975823337__section855085010198>`.

-  The Elasticsearch PHP client has been installed on the server. For details, see `Elasticsearch PHP Client <https://www.elastic.co/docs/reference/elasticsearch/clients/php>`__.

   In this document, the installed PHP version is 8.0.30, the Composer version is 2.9.2, the Elasticsearch PHP client version is 7.17.2, and the connected Elasticsearch cluster version is 7.10.2.

Installing the PHP Client Library
---------------------------------

Install the PHP client library on the server that runs the PHP code.

.. code-block::

   yum install -y php

Connecting to a Cluster
-----------------------

The sample code varies depending on the security mode settings of the target Elasticsearch cluster. Select the right reference document based on your service scenario.

.. table:: **Table 1** Cluster access scenarios

   +----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch Cluster Security-Mode Settings | Details                                                                                                                                                          |
   +==============================================+==================================================================================================================================================================+
   | Non-security mode                            | :ref:`Connecting to a Non-Security Mode Cluster with the Elasticsearch PHP Client <en-us_topic_0000002524717937__section64071057163511>`                         |
   +----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTP                         | :ref:`Connecting to a Security-Mode+HTTP Cluster with the Elasticsearch PHP Client <en-us_topic_0000002524717937__section47791925143714>`                        |
   +----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTPS                        | :ref:`Connecting to a Security-Mode+HTTPS Cluster with the Elasticsearch PHP Client (Without a Certificate) <en-us_topic_0000002524717937__section984185711374>` |
   +----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTPS                        | :ref:`Connecting to a Security-Mode+HTTPS Cluster with the Elasticsearch PHP Client (With a Certificate) <en-us_topic_0000002524717937__section1590032810114>`   |
   +----------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000002524717937__section64071057163511:

Connecting to a Non-Security Mode Cluster with the Elasticsearch PHP Client
---------------------------------------------------------------------------

Use the Elasticsearch PHP client to connect to a non-security mode Elasticsearch cluster, and obtain the cluster health status.

The following is an example of the code for creating a client instance using the cluster connection information:

.. code-block::

   <?php
   require 'vendor/autoload.php';

   use Elasticsearch\ClientBuilder;

   class ElasticsearchClient
   {
       private $client;

       public function __construct($config)
       {
           $this->client = ClientBuilder::create()
               ->setHosts($config['hosts'])
               ->setConnectionPool('\Elasticsearch\ConnectionPool\SimpleConnectionPool', [])
               ->setRetries($config['retries'] ?? 3)
               ->setConnectionParams([
                   'client' => [
                       'timeout' => 10,
                       'connect_timeout' => 5
                   ]
               ])
               ->build();
       }

       public function getClusterHealth()
       {
           return $this->client->cluster()->health();
       }
   }

   $config = [
       'hosts' => [
           'http://IP:9200',
           'http://IP:9200'
       ],
       'retries' => 2
   ];

   $es = new ElasticsearchClient($config);
   print_r($es->getClusterHealth());
   ?>

.. table:: **Table 2** Config parameters

   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                                                                                                                      |
   +===========+==================================================================================================================================================================================================+
   | hosts     | Cluster access address, including the protocol (HTTP), cluster IP address, and port 9200, for example, http://xx.xx.xx.xx:9200. If there are multiple addresses, separate them with a comma (,). |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | retries   | Number of retries upon a failure. The SimpleConnectionPool serves as the connection pool, enabling a retry mechanism upon connection failures.                                                   |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The code obtains the cluster health status. If a result similar to the following is returned, the cluster is connected.

::

   Array
   (
       [cluster_name] => css-xxxx-php
       [status] => green
       ...
   )

.. _en-us_topic_0000002524717937__section47791925143714:

Connecting to a Security-Mode+HTTP Cluster with the Elasticsearch PHP Client
----------------------------------------------------------------------------

Use the Elasticsearch PHP client to connect to a security-mode Elasticsearch cluster that uses HTTP, and obtain the cluster health status.

The following is an example of the code for creating a client instance using the cluster connection information:

.. code-block::

   <?php
   require 'vendor/autoload.php';

   use Elasticsearch\ClientBuilder;

   class ElasticsearchClient
   {
       private $client;

       public function __construct($config)
       {
           $this->client = ClientBuilder::create()
               ->setHosts($config['hosts'])
               ->setBasicAuthentication($config['username'], $config['password'])
               ->setConnectionPool('\Elasticsearch\ConnectionPool\SimpleConnectionPool', [])
               ->setRetries($config['retries'] ?? 3)
               ->setConnectionParams([
                   'client' => [
                       'timeout' => 10,
                       'connect_timeout' => 5
                   ]
               ])
               ->build();
       }

       public function getClusterHealth()
       {
           return $this->client->cluster()->health();
       }
   }

   $config = [
       'hosts' => [
           'http://IP:9200',
           'http://IP:9200'
       ],
       'username' => 'USERNAME',
       'password' => 'PASSWORD',
       'retries' => 2
   ];

   $es = new ElasticsearchClient($config);
   print_r($es->getClusterHealth());
   ?>

.. table:: **Table 3** Config parameters

   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                                                                                                                      |
   +===========+==================================================================================================================================================================================================+
   | hosts     | Cluster access address, including the protocol (HTTP), cluster IP address, and port 9200, for example, http://xx.xx.xx.xx:9200. If there are multiple addresses, separate them with a comma (,). |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | username  | Username for accessing the cluster.                                                                                                                                                              |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | password  | Password of the user.                                                                                                                                                                            |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | retries   | Number of retries upon a failure. The SimpleConnectionPool serves as the connection pool, enabling a retry mechanism upon connection failures.                                                   |
   +-----------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The code obtains the cluster health status. If a result similar to the following is returned, the cluster is connected.

::

   Array
   (
       [cluster_name] => css-xxxx-php
       [status] => green
       ...
   )

.. _en-us_topic_0000002524717937__section984185711374:

Connecting to a Security-Mode+HTTPS Cluster with the Elasticsearch PHP Client (Without a Certificate)
-----------------------------------------------------------------------------------------------------

Use the Elasticsearch PHP client to connect to a security-mode Elasticsearch cluster that uses HTTPS without loading a security certificate, and obtain the cluster health status.

The following is an example of the code for creating a client instance using the cluster connection information:

.. code-block::

   <?php
   require 'vendor/autoload.php';

   use Elasticsearch\ClientBuilder;

   class ElasticsearchClient
   {
       private $client;

       public function __construct($config)
       {
           $this->client = ClientBuilder::create()
               ->setHosts($config['hosts'])
               ->setBasicAuthentication($config['username'], $config['password'])
               ->setSSLVerification($config['ssl_verify'] ?? false)
               ->setConnectionPool('\Elasticsearch\ConnectionPool\SimpleConnectionPool', [])
               ->setRetries($config['retries'] ?? 3)
               ->setConnectionParams([
                   'client' => [
                       'timeout' => 10,
                       'connect_timeout' => 5
                   ]
               ])
               ->build();
       }

       public function getClusterHealth()
       {
           return $this->client->cluster()->health();
       }
   }

   $config = [
       'hosts' => [
           'https://IP:9200',
           'https://IP:9200'
       ],
       'username' => 'USERNAME',
       'password' => 'PASSWORD',
       'ssl_verify' => false,
       'retries' => 2
   ];

   $es = new ElasticsearchClient($config);
   print_r($es->getClusterHealth());
   ?>

.. table:: **Table 4** Config parameters

   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Description                                                                                                                                                                                        |
   +============+====================================================================================================================================================================================================+
   | hosts      | Cluster access address, including the protocol (HTTPS), cluster IP address, and port 9200, for example, https://xx.xx.xx.xx:9200. If there are multiple addresses, separate them with a comma (,). |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | username   | Username for accessing the cluster.                                                                                                                                                                |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | password   | Password of the user.                                                                                                                                                                              |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ssl_verify | Whether to load a security certificate.                                                                                                                                                            |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | retries    | Number of retries upon a failure. The SimpleConnectionPool serves as the connection pool, enabling a retry mechanism upon connection failures.                                                     |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The code obtains the cluster health status. If a result similar to the following is returned, the cluster is connected.

::

   Array
   (
       [cluster_name] => css-xxxx-php
       [status] => green
       ...
   )

.. _en-us_topic_0000002524717937__section1590032810114:

Connecting to a Security-Mode+HTTPS Cluster with the Elasticsearch PHP Client (With a Certificate)
--------------------------------------------------------------------------------------------------

Use the Elasticsearch PHP client to connect to a security-mode Elasticsearch cluster that uses HTTPS while loading a security certificate, and obtain the cluster health status.

.. caution::

   For how to obtain and upload a security certificate, see :ref:`Obtaining and Uploading a Security Certificate <en-us_topic_0000002524717937__section16306122401412>`.

The following is an example of the code for creating a client instance using the cluster connection information:

.. code-block::

   <?php
   require 'vendor/autoload.php';

   use Elasticsearch\ClientBuilder;

   class ElasticsearchClient
   {
       private $client;

       public function __construct($config)
       {
           $this->client = ClientBuilder::create()
               ->setHosts($config['hosts'])
               ->setBasicAuthentication($config['username'], $config['password'])
               ->setSSLVerification($config['ssl_verify'] ?? true)
               ->setConnectionPool('\Elasticsearch\ConnectionPool\SimpleConnectionPool', [])
               ->setRetries($config['retries'] ?? 3)
               ->setConnectionParams([
                   'client' => [
                       'timeout' => 10,
                       'connect_timeout' => 5
                   ]
               ])
               ->build();
       }

       public function getClusterHealth()
       {
           return $this->client->cluster()->health();
       }
   }

   $config = [
       'hosts' => [
           'https://IP:9200',
           'https://IP:9200'
       ],
       'username' => 'USERNAME',
       'password' => 'PASSWORD',
       'ssl_verify' => true,
       'retries' => 2
   ];

   $es = new ElasticsearchClient($config);
   print_r($es->getClusterHealth());
   ?>

.. table:: **Table 5** Config parameters

   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Description                                                                                                                                                                                        |
   +============+====================================================================================================================================================================================================+
   | hosts      | Cluster access address, including the protocol (HTTPS), cluster IP address, and port 9200, for example, https://xx.xx.xx.xx:9200. If there are multiple addresses, separate them with a comma (,). |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | username   | Username for accessing the cluster.                                                                                                                                                                |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | password   | Password of the user.                                                                                                                                                                              |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ssl_verify | Whether to load a security certificate.                                                                                                                                                            |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | retries    | Number of retries upon a failure. The SimpleConnectionPool serves as the connection pool, enabling a retry mechanism upon connection failures.                                                     |
   +------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The code obtains the cluster health status. If a result similar to the following is returned, the cluster is connected.

::

   Array
   (
       [cluster_name] => css-xxxx-php
       [status] => green
       ...
   )

.. _en-us_topic_0000002524717937__section16306122401412:

Obtaining and Uploading a Security Certificate
----------------------------------------------

To access a security-mode Elasticsearch cluster that uses HTTPS, perform the following steps to obtain the security certificate if it is required, and upload it to the client.

#. Obtain the security certificate **CloudSearchService.cer**.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

   d. Click the **Overview** tab. In the **Network Information** area, click **Download Certificate** below **HTTPS Access**.


      .. figure:: /_static/images/en-us_image_0000002412557593.png
         :alt: **Figure 1** Downloading a security certificate

         **Figure 1** Downloading a security certificate

#. Upload the downloaded certificate to the server.

#. Find the PHP installation directory on the server and modify the **php.ini** file.

   .. code-block::

      curl.cainfo="/tmp/CloudSearchService" // Replace it with the full absolute path of the security certificate.
