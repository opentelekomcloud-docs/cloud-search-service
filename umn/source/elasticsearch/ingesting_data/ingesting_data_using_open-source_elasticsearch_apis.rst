:original_name: css_01_0024.html

.. _css_01_0024:

Ingesting Data Using Open-Source Elasticsearch APIs
===================================================

During application development, debugging, or small-scale data migration, developers frequently need to quickly write local JSON files, such as test datasets and configuration files, to an Elasticsearch cluster. Compared with data migration tools such as Logstash and CDM, which are complex to configure, open-source Elasticsearch APIs (such as the \_bulk API) provide a more flexible and lightweight alternative, especially for ad hoc tasks. You can write data through Kibana in a highly interactive manner, or run cURL commands on an ECS for batch ingestion. Both methods enable agile and efficient data ingestion into cloud-based Elasticsearch clusters.

Method 1: Ingesting Data in Kibana
----------------------------------

On Kibana, you can run POST commands to import data using an open-source Elasticsearch API.

Applicable scenarios: development and debugging, small ad-hoc data writes, and syntax verification.

#. Log in to Kibana.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. (Optional) Create an index and specify a custom mapping to define field data types.

   For example, run the following command to create index **my_store**:

   -  For Elasticsearch 7.x or later:

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

   -  For Elasticsearch earlier than 7.x:

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

#. Write data to the index.

   For example, run the following command to write a record to the **my_store** index:

   -  For Elasticsearch 7.x or later:

      .. code-block:: text

         POST /my_store/_bulk
         {"index":{}}
         {"productName":"Latest art shirts for women in 2017 autumn","size":"L"}

   -  For Elasticsearch earlier than 7.x:

      .. code-block:: text

         POST /my_store/products/_bulk
         {"index":{}}
         {"productName":"Latest art shirts for women in 2017 autumn","size":"L"}

#. Verify the result.

   Check the result. If the value of **errors** is **false** and the value of **result** in each record in the **items** array is **created**, all records are successfully written.

Method 2: Ingesting Data by Running cURL Commands on an ECS
-----------------------------------------------------------

On an ECS server, you can run cURL commands to import files via an open-source Elasticsearch API.

Applicable scenarios: batch ingestion of local JSON files using an automation script.

#. Prepare an ECS. Buy an ECS located in the same VPC as the destination Elasticsearch cluster.

#. Obtain the private network address of the cluster.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, obtain the target cluster's internal network address from the **Internal Network Address** column. Typical address format: *<host>*:*<port>* or *<host>*:*<port>*,\ *<host>*:*<port>*. Example: **10.62.179.32:9200,10.62.179.33:9200**.

      If the cluster has client nodes, only the IP addresses and ports of all the client nodes are displayed. Otherwise, the IP addresses and ports of all data nodes and cold data nodes are displayed.

#. Verify connectivity. Ping the Elasticsearch cluster's private network address from the ECS. If successful, the two are connected.

#. Prepare documents. Upload JSON files to the ECS.

   For example, save the following data as a **test.json** file and upload it to the ECS:

   -  For Elasticsearch 7.x or later:

      .. code-block::

         {"index": {"_index":"my_store"}}
         {"productName":"Autumn new woman blouses 2019","size":"M"}
         {"index": {"_index":"my_store"}}
         {"productName":"Autumn new woman blouses 2019","size":"L"}

   -  For Elasticsearch earlier than 7.x:

      .. code-block::

         {"index": {"_index":"my_store","_type":"products"}}
         {"productName":"Autumn new woman blouses 2019","size":"M"}
         {"index": {"_index":"my_store","_type":"products"}}
         {"productName":"Autumn new woman blouses 2019","size":"L"}

#. (Optional) Create an index and specify a custom mapping to define field data types.

   For example, run the following command to create index **my_store**:

   Sample code for Elasticsearch 7.x or later:

   -  For a non-security mode cluster (HTTP): no authentication required.

      .. code-block::

         curl -X PUT "http://<host>:<port>/my_store" \
              -H 'Content-Type: application/json' \
              -d '{
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

   -  For a security-mode cluster using HTTP: Authentication is required. If the password contains special characters like **!**, enclose the password with a pair of single quotation marks, for example, **-u 'admin':'Pass!word'**.

      .. code-block::

         curl -X PUT -u <user>:<password> "http://<host>:<port>/my_store" \
              -H 'Content-Type: application/json' \
              -d '{
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

   -  For a security-mode cluster using HTTPS: Authentication is required. If the password contains special characters like **!**, enclose the password with a pair of single quotation marks, for example, **-u 'admin':'Pass!word'**. Furthermore, ignore SSL certificate authentication.

      .. code-block::

         curl -X PUT -k -u <user>:<password> "https://<host>:<port>/my_store" \
              -H 'Content-Type: application/json' \
              -d '{
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

   Sample code for Elasticsearch earlier than 7.x:

   -  For a non-security mode cluster (HTTP): no authentication required.

      .. code-block::

         curl -X PUT "http://<host>:<port>/my_store" \
              -H 'Content-Type: application/json' \
              -d '{
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

   -  For a security-mode cluster using HTTP: Authentication is required. If the password contains special characters like **!**, enclose the password with a pair of single quotation marks, for example, **-u 'admin':'Pass!word'**.

      .. code-block::

         curl -X PUT -u <user>:<password> "http://<host>:<port>/my_store" \
              -H 'Content-Type: application/json' \
              -d '{
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

   -  For a security-mode cluster using HTTPS: Authentication is required. If the password contains special characters like **!**, enclose the password with a pair of single quotation marks, for example, **-u 'admin':'Pass!word'**. Furthermore, ignore SSL certificate authentication.

      .. code-block::

         curl -X PUT -k -u <user>:<password> "https://<host>:<port>/my_store" \
              -H 'Content-Type: application/json' \
              -d '{
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

#. Ingest the JSON file into the Elasticsearch cluster:

   Run the following command in the ECS directory that stores the JSON file:

   -  For a non-security mode cluster (HTTP): no authentication required.

      .. code-block::

         curl -X POST "http://<host>:<port>/_bulk" \
              -H 'Content-Type: application/json' \
              --data-binary @test.json

   -  For a security-mode cluster using HTTP: Authentication is required. If the password contains special characters like **!**, enclose the password with a pair of single quotation marks, for example, **-u 'admin':'Pass!word'**.

      .. code-block::

         curl -X POST -u <user>:<password> "http://<host>:<port>/_bulk" \
              -H 'Content-Type: application/json' \
              --data-binary @test.json

   -  For a security-mode cluster using HTTPS: Authentication is required. If the password contains special characters like **!**, enclose the password with a pair of single quotation marks, for example, **-u 'admin':'Pass!word'**. Furthermore, ignore SSL certificate authentication.

      .. code-block::

         curl -X POST -k -u <user>:<password> "https://<host>:<port>/_bulk" \
              -H 'Content-Type: application/json' \
              --data-binary @test.json

   .. note::

      If the designated cluster node is unavailable, the command will fail. If the cluster contains multiple nodes, replace <host> with the IP address of another node. If the cluster contains only one node, you have to wait until the node recovers.

#. Verify the result.

   After data ingestion, the following information is returned:

   .. code-block::

      {"took":204, "errors":false, "items":[...]}

   If the value of **errors** is **false**, all data has been successfully ingested.
