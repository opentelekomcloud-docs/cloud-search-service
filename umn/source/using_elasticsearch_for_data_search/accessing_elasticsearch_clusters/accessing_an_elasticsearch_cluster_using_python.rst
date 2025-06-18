:original_name: css_01_0390.html

.. _css_01_0390:

Accessing an Elasticsearch Cluster Using Python
===============================================

You can access an Elasticsearch cluster created in CSS using Python.

Prerequisites
-------------

-  The CSS cluster is available.
-  Ensure that the server running Python can communicate with the CSS cluster.

Accessing a Cluster
-------------------

#. Install the Elasticsearch Python client. You are advised to use the client version that matches the Elasticsearch version. For example, if the cluster version is 7.6.2, install the Elasticsearch Python client 7.6.

   ::

      pip install Elasticsearch==7.6

#. Create an Elasticsearch client and check whether the **test** index exists. The examples for clusters in different security modes are as follows:

   -  Cluster in non-security mode

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

         es = ElasticFactory(["xxx.xxx.xxx.xxx"], "9200", None, None).create()
         print(es.indices.exists(index='test'))

   -  Cluster in security mode + HTTP

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

   -  Cluster in security mode + HTTPS

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

   .. table:: **Table 1** Variables

      +-----------+------------------------------------------------------------------------------------------------------------------------+
      | Parameter | Description                                                                                                            |
      +===========+========================================================================================================================+
      | host      | IP address for accessing the Elasticsearch cluster. If there are multiple IP addresses, separate them with commas (,). |
      +-----------+------------------------------------------------------------------------------------------------------------------------+
      | port      | Access port of the Elasticsearch cluster. Enter **9200**.                                                              |
      +-----------+------------------------------------------------------------------------------------------------------------------------+
      | username  | Username for accessing the cluster.                                                                                    |
      +-----------+------------------------------------------------------------------------------------------------------------------------+
      | password  | Password of the user.                                                                                                  |
      +-----------+------------------------------------------------------------------------------------------------------------------------+

#. Create a cluster index through the Elasticsearch client.

   ::

      mappings = {
          "settings": {
              "index": {
                  "number_of_shards": number_of_shards,
                  "number_of_replicas": 1,
              },
          },
          "mappings": {
              properties
          }
      }
      result = es.indices.create(index=index, body=mappings)

#. Query the index created in the previous step through the Elasticsearch client.

   ::

      body = {
          "query": {
              "match": {
                  "Query field": "Query content"
              }
          }
      }
      result = es.search(index=index, body=body)
