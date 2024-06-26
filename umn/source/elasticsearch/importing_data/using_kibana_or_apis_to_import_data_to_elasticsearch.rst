:original_name: en-us_topic_0000001477899200.html

.. _en-us_topic_0000001477899200:

Using Kibana or APIs to Import Data to Elasticsearch
====================================================

You can import data in various formats, such as JSON, to Elasticsearch in CSS by using Kibana or APIs.

Importing Data Using Kibana
---------------------------

Before importing data, ensure that you can use Kibana to access the cluster. The following procedure illustrates how to use the **POST** command to import data.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters** > **Elasticsearch** to switch to the **Clusters** page.

#. Choose **Clusters** in the navigation pane. Locate the target cluster and click **Access Kibana** in the **Operation** column to log in to Kibana.

#. Click **Dev Tools** in the navigation tree on the left.

#. (Optional) On the **Console** page, run the related command to create an index for storing data and specify a custom mapping to define the data type.

   If there is an available index in the cluster where you want to import data, skip this step. If there is no available index, create an index by referring to the following sample code.

   For example, on the **Console** page of Kibana, run the following command to create an index named **my_store** and specify a user-defined mapping to define the data type:

   Versions earlier than 7.\ *x*

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

   Versions 7.\ *x* and later

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

#. Run commands to import data. For example, run the following command to import a piece of data:

   Versions earlier than 7.\ *x*

   .. code-block:: text

      POST /my_store/products/_bulk
      {"index":{}}
      {"productName":"Latest art shirts for women in 2017 autumn","size":"L"}

   Versions 7.\ *x* and later

   .. code-block:: text

      POST /my_store/_bulk
      {"index":{}}
      {"productName":"Latest art shirts for women in 2017 autumn","size":"L"}

   The command output is similar to that shown in :ref:`Figure 1 <en-us_topic_0000001477899200__en-us_topic_0000001223594412_fig86351225133018>`. If the value of the **errors** field in the result is **false**, the data is successfully imported.

   .. _en-us_topic_0000001477899200__en-us_topic_0000001223594412_fig86351225133018:

   .. figure:: /_static/images/en-us_image_0000001575802426.png
      :alt: **Figure 1** Response message

      **Figure 1** Response message

Importing Data Using APIs
-------------------------

You can call the bulk API using the cURL command to import a JSON data file.

.. note::

   -  You are advised to import a file smaller than 50 MB.
   -  This section uses a cluster in non-security mode as an example to describe how to run the cURL command to import data..

#. Log in to the ECS that you use to access the cluster.

#. Upload the JSON data file to the ECS.

#. Run the following commands in the path where the JSON data file is stored in the ECS to import the JSON data to an Elasticsearch cluster.

   In the command, replace the value of {*Private network address and port number of the node*} with the private network address and port number of a node in the cluster. If the node fails to work, the command will fail to be executed. If the cluster contains multiple nodes, you can replace the value of {*Private network address and port number of the node*} with the private network address and port number of any available node in the cluster. If the cluster contains only one node, restore the node and execute the command again. **test.json** indicates the JSON file whose data is to be imported.

   .. code-block::

      curl -X PUT "http://{Private network address and port number of the node} /_bulk" -H 'Content-Type: application/json' --data-binary @test.json

   If communication encryption has been enabled on the cluster where you will import data, you need to send HTTPS requests and add **-k** to the cURL command.

   .. code-block::

      curl -X PUT -k "https://{Private network address and port number of the node} /_bulk" -H 'Content-Type: application/json' --data-binary @test.json

   .. note::

      The value of the **-X** parameter is a command and that of the **-H** parameter is a message header. In the preceding command, **PUT** is the value of the **-X** parameter and **'Content-Type: application/json' --data-binary @test.json** is the value of the **-H** parameter. Do not add **-k** between a parameter and its value.

   **Example 1:** In this example, assume that you need to import data in the **test.json** file to an Elasticsearch cluster, where communication encryption is disabled and the private network address and port number of one node are **192.168.0.90** and **9200** respectively. The data in the **test.json** file is as follows:

   Versions earlier than 7.\ *x*

   .. code-block::

      {"index": {"_index":"my_store","_type":"products"}}
      {"productName":"Autumn new woman blouses 2019","size":"M"}
      {"index": {"_index":"my_store","_type":"products"}}
      {"productName":"Autumn new woman blouses 2019","size":"L"}

   Versions 7.\ *x* and later

   .. code-block::

      {"index": {"_index":"my_store"}}
      {"productName":"Autumn new woman blouse 2019","size":"M"}
      {"index": {"_index":"my_store"}}
      {"productName":"Autumn new woman blouse 2019","size":"L"}

   Perform the following steps to import the data:

   a. Run the following command to create an index named **my_store**:

      Versions earlier than 7.\ *x*

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

      Versions 7.\ *x* and later

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

   b. Run the following command to import the data in the **test.json** file:

      .. code-block::

         curl -X PUT "http://192.168.0.90:9200/_bulk" -H 'Content-Type: application/json' --data-binary @test.json

      In this case, if the following information is displayed, the data is successfully imported:

      .. code-block::

         {"took":204,"errors":false,"items":[{"index":{"_index":"my_store","_type":"_doc","_id":"DJQkBIwBbJvUd2769Wi-","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1,"status":201}},{"index":{"_index":"my_store","_type":"_doc","_id":"DZQkBIwBbJvUd2769Wi_","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":1,"_primary_term":1,"status":201}}]}

   **Example 2:** In this example, assume that you need to import data in the **test.json** file to an Elasticsearch cluster, where communication encryption has been enabled and the node access address and content in the **testdata.json** are the same as those in example 1. Perform the following steps to import the data:

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

   b. Run the following command to import the data in the **test.json** file:

      .. code-block::

         curl -X PUT -k "https://192.168.0.90:9200/_bulk" -H 'Content-Type: application/json' --data-binary @test.json

      In this case, if the following information is displayed, the data is successfully imported:

      .. code-block::

         {"took":204,"errors":false,"items":[{"index":{"_index":"my_store","_type":"_doc","_id":"DJQkBIwBbJvUd2769Wi-","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":0,"_primary_term":1,"status":201}},{"index":{"_index":"my_store","_type":"_doc","_id":"DZQkBIwBbJvUd2769Wi_","_version":1,"result":"created","_shards":{"total":2,"successful":1,"failed":0},"_seq_no":1,"_primary_term":1,"status":201}}]}
