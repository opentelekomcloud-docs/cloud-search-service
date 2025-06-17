:original_name: css_01_0024.html

.. _css_01_0024:

Using Open Source Elasticsearch APIs to Import Data to Elasticsearch
====================================================================

With CSS, you can use open-source Elasticsearch APIs on Kibana or an ECS server to import data to an Elasticsearch cluster. JSON files are supported.

-  :ref:`Using an Open-Source Elasticsearch API to Import Data on Kibana <css_01_0024__en-us_topic_0000001223594412_section1430231820400>`: Run POST commands to import data.
-  :ref:`Using an Open-Source Elasticsearch API to Import Data on an ECS Server <css_01_0024__en-us_topic_0000001223594412_section239718062912>`: Run cURL commands to import data.

.. _css_01_0024__en-us_topic_0000001223594412_section1430231820400:

Using an Open-Source Elasticsearch API to Import Data on Kibana
---------------------------------------------------------------

On Kibana, you can run POST commands to import single pieces of data using an open-source Elasticsearch API.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters** > **Elasticsearch** to switch to the **Clusters** page.

#. Locate the target cluster, and click **Access Kibana** in the **Operation** column to log in to Kibana.

#. Click **Dev Tools** in the navigation tree on the left.

#. Run the following command on the console to check whether the cluster has indexes:

   .. code-block:: text

      GET _cat/indices?v

   -  If indexes are available in the cluster to which you want to import data, you do not need to create an index. Go to :ref:`7 <css_01_0024__en-us_topic_0000001223594412_li599201141619>`.
   -  If no indexes are available in the cluster, go to the next step to create an index.

#. Run the following command to create an index for storing imported data and create a custom mapping to define the data type.

   For example, run the following command to create index **my_store**:

   Run the following command for Elasticsearch earlier than 7.x:

   .. code-block:: text

      PUT /my_store
      {
          "settings": {
              "number_of_shards": 1
          },
          "mappings": {
              "products": {
                  "properties": {
                      "productName": {
                          "type": "text"
                      },
                      "size": {
                          "type": "keyword"
                      }
                  }
              }
          }
      }

   Run the following command for Elasticsearch 7.x or later:

   .. code-block:: text

      PUT /my_store
      {
          "settings": {
              "number_of_shards": 1
          },
          "mappings": {
              "properties": {
                  "productName": {
                      "type": "text"
                  },
                  "size": {
                      "type": "keyword"
                  }
              }
          }
      }

#. .. _css_01_0024__en-us_topic_0000001223594412_li599201141619:

   Run commands on Kibana to import data. In the example below, only a single piece of data is imported:

   Run the following command for Elasticsearch earlier than 7.x:

   .. code-block:: text

      POST /my_store/products/_bulk
      {"index":{}}
      {"productName":"Latest art shirts for women in 2017 autumn","size":"L"}

   Run the following command for Elasticsearch 7.x or later:

   .. code-block:: text

      POST /my_store/_bulk
      {"index":{}}
      {"productName":"Latest art shirts for women in 2017 autumn","size":"L"}

   The command output is similar to that shown in :ref:`Figure 1 <css_01_0024__en-us_topic_0000001223594412_fig86351225133018>`. If the value of the **errors** field in the result is **false**, the data is successfully imported.

   .. _css_01_0024__en-us_topic_0000001223594412_fig86351225133018:

   .. figure:: /_static/images/en-us_image_0000001938378084.png
      :alt: **Figure 1** Response message

      **Figure 1** Response message

.. _css_01_0024__en-us_topic_0000001223594412_section239718062912:

Using an Open-Source Elasticsearch API to Import Data on an ECS Server
----------------------------------------------------------------------

On an ECS server, you can run cURL commands to use an open-source Elasticsearch API to import JSON files.

In the example below, a cluster in non-security mode is used to describe how to import data using cURL commands. For the commands for a security cluster, see :ref:`Accessing an Elasticsearch Cluster Using cURL Commands <css_01_0384>`.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters** > **Elasticsearch** to switch to the **Clusters** page.

#. In the cluster list, obtain the IP address of the target cluster from the **Private Network Address** column. Generally, the IP address format is *<host>*\ **:**\ *<port>* or *<host>*\ **:**\ *<port>*\ **,**\ *<host>*\ **:**\ *<port>*.

   If the cluster has only one node, the IP address and port number of this one node are displayed, for example, **10.62.179.32:9200**. If the cluster has multiple nodes, the IP addresses and port numbers of all nodes are displayed, for example, **10.62.179.32:9200,10.62.179.33:9200**.

#. Log in to the ECS that you are going to use to import data.

#. Upload a JSON file to the ECS.

   For example, save the following data as a JSON file and upload the file to the ECS:

   For Elasticsearch earlier than 7.x:

   .. code-block::

      {"index": {"_index":"my_store","_type":"products"}}
      {"productName":"Autumn new woman blouses 2019","size":"M"}
      {"index": {"_index":"my_store","_type":"products"}}
      {"productName":"Autumn new woman blouses 2019","size":"L"}

   For Elasticsearch 7.x or later:

   .. code-block::

      {"index": {"_index":"my_store"}}
      {"productName":"Autumn new woman blouse 2019","size":"M"}
      {"index": {"_index":"my_store"}}
      {"productName":"Autumn new woman blouses 2019","size":"L"}

#. Run the following command in the path where the JSON file is stored in the ECS to import the JSON file to an Elasticsearch cluster.

   .. code-block::

      curl -X PUT "http://{Private network address and port number of the node} /_bulk" -H 'Content-Type: application/json' --data-binary @test.json

   If communication encryption is enabled for the cluster where you are importing data, you need to send HTTPS requests by add **-k** to the cURL commands.

   .. code-block::

      curl -X PUT -k "https://{Private network address and port number of the node} /_bulk" -H 'Content-Type: application/json' --data-binary @test.json

   Replace **{Private network address and port number of the node}** with the private network address and port number of a node in the cluster. In the case the failure of a cluster node, if the cluster contains multiple nodes, you can replace {*Private network address and port number of the node*} with the private network address and port number of any available node in the cluster; if the cluster contains only one node, restore this node and execute the command again. **test.json** indicates the JSON file to be imported.

   .. note::

      The value of the **-X** parameter is a command and that of the **-H** parameter is a message header. In the preceding command, **PUT** is the value of the **-X** parameter and **'Content-Type: application/json' --data-binary @test.json** is the value of the **-H** parameter. Do not add **-k** between a parameter and its value.

   **Example 1:** In this example, assume that you need to import data in the **test.json** file to an Elasticsearch cluster, where communication encryption is disabled and the private network address and port number of one node are **192.168.0.90** and **9200** respectively.

   a. Run the following command to create an index named **my_store**:

      Run the following command for Elasticsearch earlier than 7.x:

      .. code-block::

         curl -X PUT http://192.168.0.90:9200/my_store -H 'Content-Type: application/json' -d '
          {
            "settings": {
              "number_of_shards": 1
            },
            "mappings": {
              "products": {
                "properties": {
                  "productName": {
                    "type": "text"
                    },
                  "size": {
                    "type": "keyword"
                  }
                }
              }
            }
          }'

      Run the following command for Elasticsearch 7.x or later:

      .. code-block::

         curl -X PUT http://192.168.0.90:9200/my_store -H 'Content-Type: application/json' -d '
         {
             "settings": {
                 "number_of_shards": 1
             },
             "mappings": {
                 "properties": {
                     "productName": {
                         "type": "text"
                     },
                     "size": {
                         "type": "keyword"
                     }
                 }
             }
         }'

   b. Run the following command to import the **test.json** file:

      .. code-block::

         curl -X PUT "http://192.168.0.90:9200/_bulk" -H 'Content-Type: application/json' --data-binary @test.json

      In this case, if the following information is displayed, the data is successfully imported:

      .. code-block::

         {"took":204,"errors":false,"items":[{"index":{"_index":"my_store","_type":"_doc","_id":"DJQkBIwBbJvUd2769Wi-","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1,"status":201}},{"index":{"_index":"my_store","_type":"_doc","_id":"DZQkBIwBbJvUd2769Wi_","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":1,"_primary_term":1,"status":201}}]}

   **Example 2:** In this example, assume that you need to import data in the **test.json** file to an Elasticsearch cluster, where communication encryption has been enabled The private network address and port of one node are **192.168.0.90** and **9200**, respectively.

   a. Run the following command to create an index named **my_store**:

      .. code-block::

         curl -X PUT -k https://192.168.0.90:9200/my_store -H 'Content-Type: application/json' -d '
          {
            "settings": {
              "number_of_shards": 1
            },
            "mappings": {
              "products": {
                "properties": {
                  "productName": {
                    "type": "text"
                    },
                  "size": {
                    "type": "keyword"
                  }
                }
              }
            }
          }'

   b. Run the following command to import the **test.json** file:

      .. code-block::

         curl -X PUT -k "https://192.168.0.90:9200/_bulk" -H 'Content-Type: application/json' --data-binary @test.json

      In this case, if the following information is displayed, the data is successfully imported:

      .. code-block::

         {"took":204,"errors":false,"items":[{"index":{"_index":"my_store","_type":"_doc","_id":"DJQkBIwBbJvUd2769Wi-","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1,"status":201}},{"index":{"_index":"my_store","_type":"_doc","_id":"DZQkBIwBbJvUd2769Wi_","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":1,"_primary_term":1,"status":201}}]}
