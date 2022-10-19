:original_name: css_01_0032.html

.. _css_01_0032:

Suggestions on Using Elasticsearch
==================================

Elasticsearch is an open-source search engine. This section provides some suggestions on using Elasticsearch to help you better use CSS.

Improving Indexing Efficiency
-----------------------------

-  Sending data to Elasticsearch through multiple processes or threads

   A single thread that sends bulk requests is unlikely to max out the indexing capability of a cluster. However, to maximize utilization of cluster resources and improve data processing efficiency, send data through multiple threads or processes.

   By testing, you can determine the optimal number of threads for bulk requests of the same size. You can progressively increase the number of threads until the CPU is saturated in the cluster. You are advised to use the **nodes stats** API to view the CPU status of a node. View the **os.cpu.percent**, **os.cpu.load_average.1m**, **os.cpu.load_average.5m**, and **os.cpu.load_average.15m** parameter settings for more details. For information on how to use the **nodes stats** API and parameter descriptions, see https://www.elastic.co/guide/en/elasticsearch/reference/6.2/cluster-nodes-stats.html#os-stats.

   For example, check whether the CPU is saturated if two threads are used during execution of bulk requests. If it is not saturated, increase the number of threads. If the load or CPU is saturated when the number of threads reaches *N*, you are advised to use *N* threads (the optimal number according to your testing) to execute bulk requests and improve indexing efficiency.

-  Increasing the refresh interval

   By default, each shard is automatically refreshed once per second. However, the refresh frequency is not applicable to all scenarios. If you use Elasticsearch to index a large number of log files and want to increase the indexing speed instead of obtaining near-real-time search performance, you can reduce the refresh frequency of each index.

   .. code-block:: text

      PUT /my_logs
      {
        "settings": {
          "refresh_interval": "30s"
        }
      }

-  Disabling refresh and replicas for initial loads

   If you need to import a large amount of data at a time, it is recommended that you disable refresh and replicas by setting **refresh_interval** to **-1** and **number_of_replicas** to **0**. After you import the data, set **refresh_interval** and **number_of_replicas** to the original values.

Selecting Appropriate Number of Shards and Replicas
---------------------------------------------------

When you create index data, you are advised to specify the number of shards and replicas. Otherwise, default settings (five shards and one replica) will be used.

The shard quantity is strongly relevant to the indexing speed. Too many or too few shards will lead to slow indexing. If you specify too many shards, numerous files will be opened during retrieval, slowing down the communication between servers. If you specify too few shards, the index size of a single shard may be too large, slowing down the indexing speed.

Specify the shard quantity based on the node quantity, disk quantity, and index size. It is recommended that the size of a single shard not exceed 30 GB. The shard size is calculated using the following formula: Size of a shard = Total amount of data/Shard quantity

.. code-block:: text

   PUT /my_index
   {
     "settings": {
       "number_of_shards":   1,
       "number_of_replicas":  0
     }
   }

Storing Data in Different Indices
---------------------------------

Elasticsearch relies on Lucene to index and store data and it suits dense data, which means that all documents have the same field.

-  Avoiding putting unrelated data in the same index

   Do not put documents that have different data structures into the same index. You can consider creating some smaller indices and use fewer shards to store the documents into the indices.

-  Avoiding putting different types in the same index

   It may save time and efforts to put different types of documents into an index. However, be aware that Elasticsearch does not store documents based on type. Therefore, putting different types into one index will slow down indexing. If your document types do not have similar mappings, put them in the same index.

-  Avoiding field conflicts between different document types in an index

   Avoid two different types that have fields of the same name but different mappings.

Creating Indices by Time Range
------------------------------

You are advised to create indices to store time-related data, such as log data, by time range, instead of storing all data in a super large index.

For example, you can store data in an index named by year (example: logs_2014) or by month (example: logs_2014-10). When the volume of data becomes very large, you can store data in an index named by day (example: logs_2014-10-24).

Creating indices by time range has the following advantages:

-  Specifying a suitable number of shards and replicas based on the current volume of data

   You can flexibly set the number of shards and replicas for each index created by time range so that there is no need to set a large shard at the beginning. After the cluster capacity is expanded, the time range can be set to adapt to the cluster scale.

-  Deleting old data by deleting old indices

   .. code-block:: text

      DELETE /logs_2014-09

-  Switching between indices using the alias mechanism

   The following example illustrates how to delete index **logs_2014-09** from alias mechanism **logs_current** and add index **logs_2014-10**.

   .. code-block:: text

      POST /_aliases
      {
        "actions": [
          { "add":    { "alias": "logs_current",  "index": "logs_2014-10" }},
          { "remove": { "alias": "logs_current",  "index": "logs_2014-09" }}
        ]
      }

-  Optimizing the indices that are no longer updated, such as indices generated last week or month, to increase query efficiency

   Combine multiple segments in the **logs_2014-09-30** index into a shard, improving the query efficiency.

   Versions earlier than 7.\ *x*

   .. code-block:: text

      PUT /logs_2014-09-30/_settings
      { "number_of_replicas": 0 }

      POST /logs_2014-09-30/_forcemerge?max_num_segments=1

      PUT /logs_2014-09-30/_settings
      { "number_of_replicas": 1 }

   Versions later than 7.\ *x*

   .. code-block:: text

      PUT /logs_2014-09-30/_settings
      { "number_of_replicas": 0 }

      POST /logs_2014-09-30/_forcemerge
      {
        "max_num_segments":1
      }

      PUT /logs_2014-09-30/_settings
      { "number_of_replicas": 1 }

Optimizing Index Configurations
-------------------------------

-  Distinguishing between texts and keywords

   In Elasticsearch, the **string** field is divided into two new data types: text used for full-text search and keyword used for keyword search.

   You are advised to configure exact-value fields without word segmentation, such as tags or enumerated values, as the keyword type.

   Versions earlier than 7.\ *x*

   .. code-block:: text

      PUT my_index1
      {
        "mappings": {
          "my_type": {
            "properties": {
              "tags": {
                "type":  "keyword"
              },
              "full_name": {
                "type":  "text"
              }
            }
          }
        }
      }

   Versions later than 7.\ *x*

   .. code-block:: text

      PUT my_index1
      {
        "mappings": {
               "properties": {
              "tags": {
                "type":  "keyword"
              },
              "full_name": {
                "type":  "text"
              }
            }
          }
        }

-  Aggregated statistics based on the text field

   Aggregated statistics based on the text field is not a common requirement. In Elasticsearch, to use aggregated statistics based on the text field, you need to enable fielddata (disabled by default). However, enabling fielddata will consume significant memory.

   You are advised to conduct multifield mapping on the sub-word string to a text field for full-text search and a keyword field for aggregated statistics.

   Versions earlier than 7.\ *x*

   .. code-block:: text

      PUT my_index2
      {
        "mappings": {
          "my_type": {
            "properties": {
              "full_name": {
                "type": "text",
                "fields": {
                  "raw": {
                    "type":  "keyword"
                  }
                }
              }
            }
          }
        }
      }

   Versions later than 7.\ *x*

   .. code-block:: text

      PUT my_index2
      {
          "mappings": {
                  "properties": {
                      "full_name": {
                          "type": "text",
                          "fields": {
                              "raw": {
                                  "type": "keyword"
                              }
                          }
                      }
                  }
              }
        }

Using Index Templates
---------------------

Elasticsearch allows you to use index templates to control settings and mappings of certain created indices, for example, controlling the shard quantity to 1 and disabling the \_all field. You can use the index template to control the settings you want to apply to the created indices.

-  In the index template, you can use the template field to specify a wildcard.
-  If there are multiple index templates, you can use order to specify the overwriting sequence. The greater the value, the higher the priority.

In the following example, the index matching **logstash-\*** uses the **my_logs** template, and the priority value of the **my_logs** template is 1.

Versions earlier than 7.\ *x*

.. code-block:: text

   PUT /_template/my_logs
   {
     "template": "logstash-*",
     "order":    1,
     "settings": {
       "number_of_shards": 1
     },
     "mappings": {
       "_default_": {
         "_all": {
           "enabled": false
         }
       }
     },
     "aliases": {
       "last_3_months": {}
     }
   }

Versions later than 7.\ *x*

.. code-block:: text

   PUT /_template/my_logsa
   {
     "index_patterns": ["logstasaah-*"],
     "order": 1,
     "settings": {
       "number_of_shards": 1
     },
     "mappings": {
       "properties": {
         "_all": {
           "enabled": false
         }
       }
     },
     "aliases": {
       "last_3_months": {}
     }
   }

Data Backup and Restoration
---------------------------

Elasticsearch replicas provide high availability during runtime, which ensures service continuity even when sporadic data loss occurs.

However, replicas do not protect against failures. In case of a failure, you need a backup of your cluster so that you can restore data.

To back up cluster data, create snapshots and save them in OBS buckets. This backup process is "smart". You are advised to use your first snapshot to store a copy of your data. All subsequent snapshots will save the differences between the existing snapshots and the new data. As the number of snapshots increases, backups are added or deleted accordingly. This means that subsequent backups will take a shorter time because only a small volume of data needs to be transferred.

Improving Query Efficiency by Filtering
---------------------------------------

Filters are important because they are fast. They do not calculate relevance (skipping the entire scoring phase) and are easily cached.

Usually, when you look for an exact value, you will not want to score the query. You would want to include/exclude documents, so you will use a constant_score query to execute the term query in a non-scoring mode and apply a uniform score of one.

.. code-block:: text

   GET /my_store/products/_search
   {
       "query" : {
           "constant_score" : {
               "filter" : {
                   "term" : {
                       "city" : "London"
                   }
               }
           }
       }
   }

Retrieving Large Amount of Data Through Scroll API
--------------------------------------------------

In the scenario where a large amount of data is returned, the query-then-fetch process supports pagination with the **from** and **size** parameters, but within limits. Results are sorted on each shard before being returned. However, with larger **from** values, the sorting process can become very heavy, using vast amounts of CPU, memory, and bandwidth. For this reason, deep pagination is not recommended.

You can use a scroll query to retrieve large numbers of documents from Elasticsearch efficiently, without affecting system performance. Scrolling allows you to do an initial search and to keep pulling batches of results from Elasticsearch until there are no more results left.

Differences Between Query and Filter
------------------------------------

In general, a filter will outperform a scoring query.

When used in filtering context, the query is said to be a **non-scoring** or **filtering** query. That is, the query simply asks the question: Does this document match? The answer is always a simple, binary yes|no.

Typical filtering cases are listed as follows:

-  Is the created time in the range from 2013 to 2014?
-  Does the **status** field contain the term "published"?
-  Is the **lat_lon** field within 10 km of a specified point?

When used in a querying context, the query becomes a "**scoring**" query. Similar to the non-scoring query, this query also determines if a document matches and how well the document matches. A typical use for a scoring query is to find documents:

-  Matching the words "full text search"
-  Containing the word "run", but also matching "runs", "running", "jog", or "sprint"
-  Containing the words "quick", "brown", and "fox" – the closer together they are, the more relevant the document
-  Tagged with lucene, search, or java – the more tags, the more relevant the document

Checking Whether a Query Is Valid
---------------------------------

Queries can become quite complex. Especially, when they are combined with different analyzers and field mappings, they can become a little difficult to follow. You can use the **validate-query** API to check whether a query is valid.

For example, on the Kibana Console page, run the following command to check whether the query is valid. In this example, the validate request tells you that the query is invalid.

Versions earlier than 7.\ *x*

.. code-block:: text

   GET /gb/tweet/_validate/query
   {
    "query": {
    "tweet" : {
      "match" : "really powerful"
     }
   }
   }

Versions later than 7.\ *x*

.. code-block:: text

   GET /gb/tweet/_validate/query
   {
   "query": {
      "productName" : {
     "match" : "really powerful"
     }
     }
    }

The response to the preceding validate request tells us that the query is invalid. To find out why it is invalid, add the explain parameter to the query string and execute the following command.

Versions earlier than 7.\ *x*

.. code-block:: text

   GET /gb/tweet/_validate/query?explain
   {
   "query": {
      "tweet" : {
     "match" : "really powerful"
     }
     }
    }

Versions later than 7.\ *x*

.. code-block:: text

   GET /gb/tweet/_validate/query?explain
   {
    "query": {
    "productName" : {
      "match" : "really powerful"
     }
   }
   }

According to the command output shown in the following, the type of query (match) is mixed up with the name of the field (tweet).

.. code-block::

   {
     "valid": false,
     "error": "org.elasticsearch.common.ParsingException: no [query] registered for [tweet]"
   }

Using the explain parameter has the added advantage of returning a human-readable description of the (valid) query, which helps in understanding exactly how CSS interprets your query.
