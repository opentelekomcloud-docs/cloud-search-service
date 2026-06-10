:original_name: css_01_0069.html

.. _css_01_0069:

Connecting to a Cluster Using Python
====================================

When using CSS's Elasticsearch clusters for data query and management, developers traditionally rely on programming languages. However, directly working with Elasticsearch's HTTP APIs often involves complex and error-prone coding. To simplify development, CSS Elasticsearch supports the official Elasticsearch Python client. The client library (elasticsearch-py) provides comprehensive encapsulation of Elasticsearch APIs, enabling developers to perform index management, CRUD (Create, Read, Update, Delete) operations, and document searches through native Python APIs. For further information, see `Elasticsearch Python Client <https://www.elastic.co/docs/reference/elasticsearch/clients/python>`__.

Prerequisites
-------------

-  The target Elasticsearch cluster is available.
-  The server that runs the Python code can communicate with the Elasticsearch cluster.
-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Obtaining the Cluster Access Address <en-us_topic_0000001975823337__section855085010198>`.
-  Python 3 has been installed on the server.

Installing the Python Client Library
------------------------------------

Install the Python client library on the server that runs the Python code. To ensure better compatibility, use a Python client library that has the same version as the target Elasticsearch cluster.

Replace 7.10 with the actual Python client version.

.. code-block::

   pip install Elasticsearch==7.10

Connecting to a Cluster
-----------------------

The sample code varies depending on the security mode settings of the target Elasticsearch cluster. Select the right reference document based on your service scenario.

.. table:: **Table 1** Cluster access scenarios

   +----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch Cluster Security-Mode Settings | Details                                                                                                                                      |
   +==============================================+==============================================================================================================================================+
   | Non-security mode                            | :ref:`Connecting to a Non-Security Mode Cluster with the Elasticsearch Python Client <en-us_topic_0000001972375893__section64071057163511>`  |
   +----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTP                         | :ref:`Connecting to a Security-Mode+HTTP Cluster with the Elasticsearch Python Client <en-us_topic_0000001972375893__section47791925143714>` |
   +----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Security mode + HTTPS                        | :ref:`Connecting to a Security-Mode+HTTPS Cluster with the Elasticsearch Python Client <en-us_topic_0000001972375893__section984185711374>`  |
   +----------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001972375893__section64071057163511:

Connecting to a Non-Security Mode Cluster with the Elasticsearch Python Client
------------------------------------------------------------------------------

Use the Elasticsearch Python client to connect to an Elasticsearch cluster for which the security mode is disabled, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

::

   from elasticsearch import Elasticsearch

   class ElasticFactory(object):

       def __init__(self, host: list, port: str, username: str, password: str):
           self.port = port
           self.host = host
           self.username = username
           self.password = password

       def create(self) -> Elasticsearch:
           addrs = []
           for host in self.host:
               addr = {'host': host, 'port': self.port}
               addrs.append(addr)

           if self.username and self.password:
               elasticsearch = Elasticsearch(addrs, http_auth=(self.username, self.password))
           else:
               elasticsearch = Elasticsearch(addrs)
           return elasticsearch

   es = ElasticFactory(["{cluster address}"], "9200", None, None).create()
   print(es.indices.exists(index='test'))

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001972375893__section47791925143714:

Connecting to a Security-Mode+HTTP Cluster with the Elasticsearch Python Client
-------------------------------------------------------------------------------

Use the Elasticsearch Python client to connect to a security-mode Elasticsearch cluster that uses HTTP, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

::

   from elasticsearch import Elasticsearch

   class ElasticFactory(object):

       def __init__(self, host: list, port: str, username: str, password: str):
           self.port = port
           self.host = host
           self.username = username
           self.password = password

       def create(self) -> Elasticsearch:
           addrs = []
           for host in self.host:
               addr = {'host': host, 'port': self.port}
               addrs.append(addr)

           if self.username and self.password:
               elasticsearch = Elasticsearch(addrs, http_auth=(self.username, self.password))
           else:
               elasticsearch = Elasticsearch(addrs)
           return elasticsearch

   es = ElasticFactory(["xxx.xxx.xxx.xxx"], "9200", "username", "password").create()
   print(es.indices.exists(index='test'))

.. table:: **Table 2** Variables

   +-----------+------------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                                |
   +===========+============================================================================================================+
   | host      | IP address for accessing the cluster. If there are multiple IP addresses, separate them using a comma (,). |
   +-----------+------------------------------------------------------------------------------------------------------------+
   | port      | Access port of the cluster. Enter **9200**.                                                                |
   +-----------+------------------------------------------------------------------------------------------------------------+
   | username  | Username for accessing the cluster.                                                                        |
   +-----------+------------------------------------------------------------------------------------------------------------+
   | password  | Password of the user.                                                                                      |
   +-----------+------------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001972375893__section984185711374:

Connecting to a Security-Mode+HTTPS Cluster with the Elasticsearch Python Client
--------------------------------------------------------------------------------

Use the Elasticsearch Python client to connect to a security-mode Elasticsearch cluster that uses HTTPS, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

::

   from elasticsearch import Elasticsearch
   import ssl

   class ElasticFactory(object):

       def __init__(self, host: list, port: str, username: str, password: str):
           self.port = port
           self.host = host
           self.username = username
           self.password = password

       def create(self) -> Elasticsearch:
           context = ssl._create_unverified_context()

           addrs = []
           for host in self.host:
               addr = {'host': host, 'port': self.port}
               addrs.append(addr)

           if self.username and self.password:
               elasticsearch = Elasticsearch(addrs, http_auth=(self.username, self.password), scheme="https", ssl_context=context)
           else:
               elasticsearch = Elasticsearch(addrs)
           return elasticsearch

   es = ElasticFactory(["xxx.xxx.xxx.xxx"], "9200", "username", "password").create()
   print(es.indices.exists(index='test'))

.. table:: **Table 3** Variables

   +-----------+------------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                                |
   +===========+============================================================================================================+
   | host      | IP address for accessing the cluster. If there are multiple IP addresses, separate them using a comma (,). |
   +-----------+------------------------------------------------------------------------------------------------------------+
   | port      | Access port of the cluster. Enter **9200**.                                                                |
   +-----------+------------------------------------------------------------------------------------------------------------+
   | username  | Username for accessing the cluster.                                                                        |
   +-----------+------------------------------------------------------------------------------------------------------------+
   | password  | Password of the user.                                                                                      |
   +-----------+------------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.
