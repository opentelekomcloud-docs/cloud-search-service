:original_name: css_01_0043.html

.. _css_01_0043:

Accessing an OpenSearch Cluster with the Python Client
======================================================

You can access and manage data in a CSS OpenSearch cluster using the official OpenSearch Python client (opensearch-py) or Elasticsearch Python client (elasticsearch-py). Both client libraries are compatible with OpenSearch REST APIs, though version compatibility needs to be verified for elasticsearch-py. Developers can use Python APIs to manage indexes; create, read, update, and delete (CRUD) documents; and search data.

You are advised to use the OpenSearch Python client (opensearch-py) to access complete OpenSearch features. For details, see `OpenSearch Python Client Documentation <https://docs.opensearch.org/latest/clients/python-low-level/>`__ or `Elasticsearch Python Client Documentation <https://www.elastic.co/docs/reference/elasticsearch/clients/python>`__.

Prerequisites
-------------

-  The target OpenSearch cluster is available.
-  The server that runs the Python code can communicate with the OpenSearch cluster.
-  Depending on the network configuration method used, obtain the cluster access address. For details, see :ref:`Network Configuration <en-us_topic_0000001992165561__en-us_topic_0000001975823337_section855085010198>`.
-  Python 3 has been installed on the server.

Installing the Python Client Library
------------------------------------

Install the Python client library on the server that runs the Python code.

CSS allows you to use the Elasticsearch 7.10 Python client to connect to OpenSearch clusters. To ensure better compatibility, however, you are advised to use a Python client library that has the same version as the target OpenSearch cluster.

Select a reference example based on the Python client you use.

-  Scenario 1 (recommended): Use the OpenSearch Python client to access an OpenSearch cluster and install the OpenSearch Python client library.

   .. code-block::

      pip install opensearch-py

-  Scenario 2: Use the Elasticsearch 7.10 Python client to access an OpenSearch cluster and install the Elasticsearch 7.10 Python client library.

   .. code-block::

      pip install Elasticsearch==7.10

Cluster Access Scenarios
------------------------

The sample code varies depending on the Python client and the security mode settings of the target OpenSearch cluster. Select the right reference document based on your service scenario.

.. table:: **Table 1** Cluster access scenarios

   +----------------------+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Python Client Type   | OpenSearch Cluster Security-Mode Settings | Reference Document                                                                                                                           |
   +======================+===========================================+==============================================================================================================================================+
   | OpenSearch           | Non-security mode                         | :ref:`Connecting to a Non-Security Mode Cluster with the OpenSearch Python Client <en-us_topic_0000001992165573__section12544103941817>`     |
   +----------------------+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   |                      | Security mode + HTTP                      | :ref:`Connecting to a Security-Mode+HTTP Cluster with the OpenSearch Python Client <en-us_topic_0000001992165573__section5657637173211>`     |
   +----------------------+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   |                      | Security mode + HTTPS                     | :ref:`Connecting to a Security-Mode+HTTPS Cluster with the OpenSearch Python Client <en-us_topic_0000001992165573__section819316143350>`     |
   +----------------------+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Elasticsearch 7.10.2 | Non-security mode                         | :ref:`Connecting to a Non-Security Mode Cluster with the Elasticsearch Python Client <en-us_topic_0000001992165573__section64071057163511>`  |
   +----------------------+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   |                      | Security mode + HTTP                      | :ref:`Connecting to a Security-Mode+HTTP Cluster with the Elasticsearch Python Client <en-us_topic_0000001992165573__section47791925143714>` |
   +----------------------+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   |                      | Security mode + HTTPS                     | :ref:`Connecting to a Security-Mode+HTTPS Cluster with the Elasticsearch Python Client <en-us_topic_0000001992165573__section984185711374>`  |
   +----------------------+-------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

.. _en-us_topic_0000001992165573__section12544103941817:

Connecting to a Non-Security Mode Cluster with the OpenSearch Python Client
---------------------------------------------------------------------------

Use the OpenSearch Python client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

::

   from opensearchpy import OpenSearch

   class OpenSearchFactory(object):

       def __init__(self, host: list, port: str, username: str, password: str):
           self.port = port
           self.host = host
           self.username = username
           self.password = password

       def create(self) -> OpenSearch:
           addrs = []
           for host in self.host:
               addr = {'host': host, 'port': self.port}
               addrs.append(addr)

           if self.username and self.password:
               opensearch = OpenSearch(addrs, http_auth=(self.username, self.password))
           else:
               opensearch = OpenSearch(addrs)
           return opensearch
   os = OpenSearchFactory(["{cluster address}"], "9200", None, None).create()
   print(os.indices.exists(index='test'))

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165573__section5657637173211:

Connecting to a Security-Mode+HTTP Cluster with the OpenSearch Python Client
----------------------------------------------------------------------------

Use the OpenSearch Python client to connect to a security-mode OpenSearch cluster that uses HTTP, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

::

   from opensearchpy import OpenSearch

   class OpenSearchFactory(object):

       def __init__(self, host: list, port: str, username: str, password: str):
           self.port = port
           self.host = host
           self.username = username
           self.password = password

       def create(self) -> OpenSearch:
           addrs = []
           for host in self.host:
               addr = {'host': host, 'port': self.port}
               addrs.append(addr)

           if self.username and self.password:
               opensearch = OpenSearch(addrs, http_auth=(self.username, self.password))
           else:
               opensearch = OpenSearch(addrs)
           return opensearch
   os = OpenSearchFactory(["xxx.xxx.xxx.xxx"], "9200", "username", "password").create()
   print(os.indices.exists(index='test'))

.. table:: **Table 2** Variables

   +-----------+----------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                              |
   +===========+==========================================================================================================+
   | host      | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | port      | Access port of the cluster. Enter **9200**.                                                              |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | username  | Username for accessing the cluster.                                                                      |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | password  | Password of the user.                                                                                    |
   +-----------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165573__section819316143350:

Connecting to a Security-Mode+HTTPS Cluster with the OpenSearch Python Client
-----------------------------------------------------------------------------

Use the OpenSearch Python client to connect to a security-mode OpenSearch cluster that uses HTTPS, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

::

   from opensearchpy import OpenSearch
   import ssl

   class OpenSearchFactory(object):

       def __init__(self, host: list, port: str, username: str, password: str):
           self.port = port
           self.host = host
           self.username = username
           self.password = password

       def create(self) -> OpenSearch:
           context = ssl._create_unverified_context()

           addrs = []
           for host in self.host:
               addr = {'host': host, 'port': self.port}
               addrs.append(addr)

           if self.username and self.password:
               opensearch = OpenSearch(addrs, http_auth=(self.username, self.password), scheme="https", ssl_context=context)
           else:
               opensearch = OpenSearch(addrs)
           return opensearch
   os = OpenSearchFactory(["xxx.xxx.xxx.xxx"], "9200", "username", "password").create()
   print(os.indices.exists(index='test'))

.. table:: **Table 3** Variables

   +-----------+----------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                              |
   +===========+==========================================================================================================+
   | host      | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | port      | Access port of the cluster. Enter **9200**.                                                              |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | username  | Username for accessing the cluster.                                                                      |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | password  | Password of the user.                                                                                    |
   +-----------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165573__section64071057163511:

Connecting to a Non-Security Mode Cluster with the Elasticsearch Python Client
------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 Python client to connect to an OpenSearch cluster for which the security mode is disabled, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

.. code-block::

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

.. _en-us_topic_0000001992165573__section47791925143714:

Connecting to a Security-Mode+HTTP Cluster with the Elasticsearch Python Client
-------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 Python client to connect to a security-mode OpenSearch cluster that uses HTTP, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

.. code-block::

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

.. table:: **Table 4** Variables

   +-----------+----------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                              |
   +===========+==========================================================================================================+
   | host      | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | port      | Access port of the cluster. Enter **9200**.                                                              |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | username  | Username for accessing the cluster.                                                                      |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | password  | Password of the user.                                                                                    |
   +-----------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.

.. _en-us_topic_0000001992165573__section984185711374:

Connecting to a Security-Mode+HTTPS Cluster with the Elasticsearch Python Client
--------------------------------------------------------------------------------

Use the Elasticsearch 7.10.2 Python client to connect to a security-mode OpenSearch cluster that uses HTTPS, and query whether the **test** index exists.

The following is an example of the code for creating a client instance using the cluster connection information:

.. code-block::

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

.. table:: **Table 5** Variables

   +-----------+----------------------------------------------------------------------------------------------------------+
   | Parameter | Description                                                                                              |
   +===========+==========================================================================================================+
   | host      | IP address for accessing the cluster. If there are multiple IP addresses, separate them with commas (,). |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | port      | Access port of the cluster. Enter **9200**.                                                              |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | username  | Username for accessing the cluster.                                                                      |
   +-----------+----------------------------------------------------------------------------------------------------------+
   | password  | Password of the user.                                                                                    |
   +-----------+----------------------------------------------------------------------------------------------------------+

This piece of code checks whether the **test** index exists in the cluster. If **true** (the index exists) or **false** (the index does not exist) is returned, it indicates that the cluster is connected.
