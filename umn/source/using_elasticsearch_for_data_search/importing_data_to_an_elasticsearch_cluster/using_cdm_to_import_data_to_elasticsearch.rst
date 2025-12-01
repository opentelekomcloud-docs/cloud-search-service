:original_name: css_01_0046.html

.. _css_01_0046:

Using CDM to Import Data to Elasticsearch
=========================================

With CSS, you can use the web user interface of the Cloud Data Migration (CDM) service to import data from an Oracle database or OBS to an Elasticsearch cluster. Only JSON files are supported.

.. table:: **Table 1** Using CDM to import data to CSS

   +-----------------------------------------------+----------------------------------------+-----------------------------------------------------+
   | Scenario                                      | Source Data                            | Target Cluster                                      |
   +===============================================+========================================+=====================================================+
   | Importing data from an Oracle database to CSS | A local or third-party Oracle database | Elasticsearch 5.5, 6.2, 6.5, 7.1, 7.6, 7.9, or 7.10 |
   +-----------------------------------------------+----------------------------------------+-----------------------------------------------------+
   | Importing data from OBS to CSS                | JSON files in OBS buckets              | Elasticsearch 5.5, 6.2, 6.5, 7.1, 7.6, 7.9, or 7.10 |
   +-----------------------------------------------+----------------------------------------+-----------------------------------------------------+

Preparations
------------

#. Confirm the source data.

   For example, the source data can be the following JSON files:

   For Elasticsearch 7.x or later:

   .. code-block::

      {"index": {"_index":"my_store"}}
      {"productName":"Autumn new woman blouses 2019","size":"M"}
      {"index": {"_index":"my_store"}}
      {"productName":"Autumn new woman blouses 2019","size":"L"}

   For Elasticsearch earlier than 7.x:

   .. code-block::

      {"index": {"_index":"my_store","_type":"products"}}
      {"productName":"Autumn new woman blouses 2019","size":"M"}
      {"index": {"_index":"my_store","_type":"products"}}
      {"productName":"Autumn new woman blouses 2019","size":"L"}

#. Obtain data source information.

   -  If the data source is an Oracle database, you need to obtain the IP address, database name, username, and password of the database.
   -  If the data source is JSON files in an OBS bucket, you need to obtain its domain name, port, AK, and SK.

#. If the data source is an Oracle database, make sure the Oracle database can be accessed using a public IP address, or a VPN or Direct Connect connection has been established between the customer's data center and the cloud service.

Importing Data
--------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, obtain the target cluster's private IP address from the **Private IP Address** column. Generally, the IP address format is *<host>*:*<port>* or *<host>*:*<port>*,\ *<host>*:*<port>*.

   If the cluster has only one node, the IP address and port number of this one node are displayed, for example, **10.62.179.32:9200**. If the cluster has multiple nodes, the IP addresses and port numbers of all nodes are displayed, for example, **10.62.179.32:9200,10.62.179.33:9200**.

#. In the cluster list, locate the destination cluster, and click **Access Kibana** in the **Operation** column to log in to the Kibana console.

#. In the Kibana navigation pane on the left, choose **Dev Tools**.

#. Run the following command on the console to check whether the cluster has indexes:

   .. code-block:: text

      GET _cat/indices?v

   -  If indexes are available in the cluster to which you want to import data, you do not need to create an index. Go to :ref:`8 <en-us_topic_0000001948561400__en-us_topic_0000001268314481_li10195124192412>`.
   -  If no indexes are available in the cluster, go to the next step to create an index.

#. Run the following command to create an index for storing imported data and create a custom mapping to define the data type.

   For example, run the following command to create index **demo**:

   For Elasticsearch 7.x or later:

   .. code-block:: text

      PUT /demo
      {
        "settings": {
          "number_of_shards": 1
        },
        "mappings": {
            "properties": {
              "productName": {
                "type": "text",
                "analyzer": "ik_smart"
              },
              "size": {
                "type": "keyword"
              }
            }
          }
        }

   For Elasticsearch earlier than 7.x:

   .. code-block:: text

      PUT /demo
      {
        "settings": {
          "number_of_shards": 1
        },
        "mappings": {
          "products": {
            "properties": {
              "productName": {
                "type": "text",
                "analyzer": "ik_smart"
              },
              "size": {
                "type": "keyword"
              }
            }
          }
        }
      }

   The command is successfully executed if the following information is displayed.

   .. code-block::

      {
        "acknowledged" : true,
        "shards_acknowledged" : true,
        "index" : "demo"
      }

#. .. _en-us_topic_0000001948561400__en-us_topic_0000001268314481_li10195124192412:

   Use CDM to import data from Oracle or OBS to the Elasticsearch cluster.

#. After the data migration is complete, go to the Kibana console of the Elasticsearch cluster again, and search for the imported data.

   Run the following command to search for data. If the imported data is consistent with the source data, data importing is successful.

   .. code-block:: text

      GET demo/_search

   **demo** is the name of the created index. Replace it if another index is used.

   The command is successfully executed if the following information is displayed.

   .. code-block::

      {
        "took": 18,
        "timed_out": false,
        "_shards": {
          "total": 1,
          "successful": 1,
          "skipped": 0,
          "failed": 0
        },
        "hits": {
          "total": 2,
          "max_score": 1,
          "hits": [
            {
              "_index": "demo",
              "_type": "products",
              "_id": "g6UepnEBuvdFwWkRmn4V",
              "_score": 1,
              "_source": {
                "size": """"size":"L"}""",
                "productName": """{"productName":"Latest art shirts for women in autumn 2019""""
              }
            },
            {
              "_index": "demo",
              "_type": "products",
              "_id": "hKUepnEBuvdFwWkRmn4V",
              "_score": 1,
              "_source": {
                "size": """"size":"M"}""",
                "productName": """{"productName":"Latest art shirts for women in autumn 2019""""
              }
            }
          ]
        }
      }
