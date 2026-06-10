:original_name: css_01_0110.html

.. _css_01_0110:

Configuring Enhanced Aggregation
================================

Low aggregation query performance often slows down analysis when large datasets are involved. CSS OpenSearch clusters leverage vectorization and optimized clustering to accelerate aggregation queries, enabling faster analytics and decision-making.

How the Feature Works
---------------------

Enhanced aggregation works by pre-sorting and physically clustering data using carefully selected sorting and clustering keys upon ingestion, thereby minimizing data scanning and computational overheads during aggregation.

-  Sorting key: A field (such as timestamps) used to physically order documents on disk, ensuring that documents with identical or similar sorting key values are stored contiguously.
-  Clustering key: A subset of fields from the sorting key that groups related documents into contiguous physical blocks. This way, aggregations can process contiguous data blocks, instead of scattered documents.

For example, for an index that contains the **region**, **host**, and **value** fields, documents can be sorted by these three fields upon ingestion, and then clustered and stored based on the **region** and **host** fields. In this case, documents with the same **region** or **host** are stored together, and are then sorted by the **value** field within each cluster.

When an aggregation query is performed, data is queried by clustering key (**region** and **host**), or by the **value** field within each cluster. This improves query efficiency.


.. figure:: /_static/images/en-us_image_0000002510653374.png
   :alt: **Figure 1** An example of enhanced aggregation

   **Figure 1** An example of enhanced aggregation

.. table:: **Table 1** Common scenarios for enhanced aggregation

   +--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Scenario                                               | Description                                                                                                                                                                                                                                                                         |
   +========================================================+=====================================================================================================================================================================================================================================================================================+
   | Aggregation of low-cardinality fields                  | Aggregates fields that have a small number of unique values. In this case, grouping is used. One example is counting the number of orders per city. A clustering operation can easily achieve this purpose.                                                                         |
   +--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Aggregation of high-cardinality fields                 | Aggregates fields that have a large number of unique values. Histogram aggregation is typically used. One example is counting the hourly visits. A sorting key can be used to accelerate data aggregation by a specified scope or range.                                            |
   +--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Hybrid aggregation of low- and high-cardinality fields | First groups and aggregates low-cardinality fields (for example, orders per city) using a clustering key, and then creates a histogram for high-cardinality fields (for example, timestamps) using a sorting key. Multi-level clustering improves the efficiency of hybrid queries. |
   +--------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Constraints
-----------

Only OpenSearch 2.19.0 clusters support this feature.

Logging In to OpenSearch Dashboards
-----------------------------------

Log in to OpenSearch Dashboards and go to the command execution page. OpenSearch clusters support multiple access methods. This topic uses OpenSearch Dashboards as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

Aggregation of Low-Cardinality Fields
-------------------------------------

Generally, low-cardinality fields use grouping as a way of aggregation. With appropriate sorting keys, grouping prepares the data for batch processing.

For example, to aggregate two low-cardinality fields **city** and **product**, perform the following steps:

#. Run the following command to set the index **testindex**:

   .. code-block:: text

      PUT testindex
      {
        "mappings": {
          "properties": {
            "date": {
              "type": "date",
              "format": "yyyy-MM-dd"
            },
            "city": {
              "type": "keyword"
            },
            "product": {
              "type": "keyword"
            },
            "trade": {
              "type": "double"
            }
          }
        },
        "settings": {
          "index": {
            "search": {
              "turbo": {
                "enabled": "true"
              }
            },
            "sort": {
              "field": [
                "city",
                "product"
              ]
            },
            "cluster": {
              "field": [
                "city",
                "product"
              ]
            }
          }
        }
      }

   .. table:: **Table 2** Parameters for low-cardinality field aggregation

      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                  | Type             | Default Value   | Description                                                                                                                                                                                                                                                                   |
      +============================+==================+=================+===============================================================================================================================================================================================================================================================================+
      | index.search.turbo.enabled | Boolean          | false           | Whether to enable enhanced aggregation. Normally, enhanced aggregation must be enabled where aggregations are used.                                                                                                                                                           |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | The value can be:                                                                                                                                                                                                                                                             |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | -  **false**: Disable enhanced aggregation.                                                                                                                                                                                                                                   |
      |                            |                  |                 | -  **true**: Enable enhanced aggregation.                                                                                                                                                                                                                                     |
      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | index.sort.field           | Array of strings | N/A             | Specify sorting keys. Sorting keys are fields used to sequence or rank documents.                                                                                                                                                                                             |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | You can specify one or multiple fields as sorting keys. When multiple fields are specified, they will apply in the sequence in which they are specified. Documents are first ranked by the first field, then the initial result set is ranked by the second field, and so on. |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | Value range: The value must be fields contained in the index.                                                                                                                                                                                                                 |
      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | index.cluster.field        | Array of strings | N/A             | Specify clustering keys. Clustering keys determine which documents are collected into the same clusters.                                                                                                                                                                      |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | During an aggregation operation, documents in the same cluster can be processed in batches, significantly enhancing aggregation performance.                                                                                                                                  |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | Constraint: The clustering keys must be a subset of the sorting keys.                                                                                                                                                                                                         |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | Value range: The value must be fields contained in the index.                                                                                                                                                                                                                 |
      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Run the following command to import sample data.

   .. code-block:: text

      PUT /_bulk
      { "index": { "_index": "testindex", "_id": "1" } }
      { "date": "2025-01-01", "city": "cityA", "product": "books", "trade": 3000.0}
      { "index": { "_index": "testindex", "_id": "2" } }
      { "date": "2025-01-02", "city": "cityA", "product": "books", "trade": 1000.0}
      { "index": { "_index": "testindex", "_id": "3" } }
      { "date": "2025-01-01", "city": "cityA", "product": "bottles", "trade": 100.0}
      { "index": { "_index": "testindex", "_id": "4" } }
      { "date": "2025-01-02", "city": "cityA", "product": "bottles", "trade": 300.0}
      { "index": { "_index": "testindex", "_id": "5" } }
      { "date": "2025-01-01", "city": "cityB", "product": "books", "trade": 7000.0}
      { "index": { "_index": "testindex", "_id": "6" } }
      { "date": "2025-01-02", "city": "cityB", "product": "books", "trade": 1000.0}

#. Run the following query command to aggregate low-cardinality fields.

   For example, query the average **trade** value for each product in different cities.

   .. code-block:: text

      POST testindex/_search
      {
        "size": 0,
        "aggs": {
          "groupby_city": {
            "terms": {
              "field": "city"
            },
            "aggs": {
              "groupby_product": {
                "terms": {
                  "field": "product"
                },
                "aggs": {
                  "avg_trade": {
                    "avg": {
                      "field": "trade"
                    }
                  }
                }
              }
            }
          }
        }
      }

Aggregation of High-Cardinality Fields
--------------------------------------

High-cardinality fields commonly use sorting keys for histogram aggregation, which facilitates data processing per range or scope.

For example, to aggregate the typical high-cardinality field **date**, perform the following steps:

#. Run the following command to set the index **testindex**:

   .. code-block:: text

      PUT testindex
      {
        "mappings": {
          "properties": {
            "date": {
              "type": "date",
              "format": "yyyy-MM-dd"
            },
            "score": {
              "type": "double"
            }
          }
        },
        "settings": {
          "index": {
            "search": {
              "turbo": {
                "enabled": "true"
              }
            },
            "sort": {
              "field": [
                "date"
              ]
            }
          }
        }
      }

   .. table:: **Table 3** Parameters for high-cardinality field aggregation

      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                  | Type             | Default Value   | Description                                                                                                                                                                                                                                                                   |
      +============================+==================+=================+===============================================================================================================================================================================================================================================================================+
      | index.search.turbo.enabled | Boolean          | false           | Whether to enable enhanced aggregation. Normally, enhanced aggregation must be enabled where aggregations are used.                                                                                                                                                           |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | The value can be:                                                                                                                                                                                                                                                             |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | -  **false**: Disable enhanced aggregation.                                                                                                                                                                                                                                   |
      |                            |                  |                 | -  **true**: Enable enhanced aggregation.                                                                                                                                                                                                                                     |
      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | index.sort.field           | Array of strings | N/A             | Specify sorting keys. Sorting keys are fields used to sequence or rank documents.                                                                                                                                                                                             |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | You can specify one or multiple fields as sorting keys. When multiple fields are specified, they will apply in the sequence in which they are specified. Documents are first ranked by the first field, then the initial result set is ranked by the second field, and so on. |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | Value range: The value must be fields contained in the index.                                                                                                                                                                                                                 |
      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Run the following command to import sample data.

   .. code-block:: text

      PUT /_bulk
      { "index": { "_index": "testindex", "_id": "1" } }
      { "date": "2025-01-01", "score": "12.0"}
      { "index": { "_index": "testindex", "_id": "2" } }
      { "date": "2025-01-02","score": "24.0"}
      { "index": { "_index": "testindex", "_id": "3" } }
      { "date": "2025-01-01","score": "53.0"}
      { "index": { "_index": "testindex", "_id": "4" } }
      { "date": "2025-01-02", "score": "22.0"}
      { "index": { "_index": "testindex", "_id": "5" } }
      { "date": "2025-01-01", "score": "99.0"}
      { "index": { "_index": "testindex", "_id": "6" } }
      { "date": "2025-01-02","score": "26.0"}

#. Run the following query command to aggregate high-cardinality fields.

   This query groups the **date** field using a histogram and then calculates the average score.

   .. code-block:: text

      POST testindex/_search?pretty
      {
        "size": 0,
        "aggs": {
          "groupbytime": {
            "date_histogram": {
              "field": "date",
              "calendar_interval": "day"
            },
            "aggs": {
              "avg_score": {
                "avg": {
                  "field": "score"
                }
              }
            }
          }
        }
      }

Hybrid Aggregation of Low- and High-Cardinality Fields
------------------------------------------------------

Where low-cardinality and high-cardinality fields are mixed, first group and aggregate low-cardinality fields using a clustering key, then create a histogram for high-cardinality fields using a sorting key.

For example, to first group the low-cardinality field **city**, then group the low-cardinality field **product**, and then group the high-cardinality field **date** into a histogram, perform the following steps:

#. Run the following command to set the index **testindex**:

   .. code-block:: text

      PUT testindex
      {
        "mappings": {
          "properties": {
            "date": {
              "type": "date",
              "format": "yyyy-MM-dd"
            },
            "city": {
              "type": "keyword"
            },
            "product": {
              "type": "keyword"
            },
            "trade": {
              "type": "double"
            }
          }
        },
        "settings": {
          "index": {
            "search": {
              "turbo": {
                "enabled": "true"
              }
            },
            "sort": {
              "field": [
                "city",
                "product",
                "date"
              ]
            },
            "cluster": {
              "field": [
                "city",
                "product"
              ]
            }
          }
        }
      }

   .. table:: **Table 4** Parameters for hybrid aggregation of low- and high-cardinality fields

      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                  | Type             | Default Value   | Description                                                                                                                                                                                                                                                                   |
      +============================+==================+=================+===============================================================================================================================================================================================================================================================================+
      | index.search.turbo.enabled | Boolean          | false           | Whether to enable enhanced aggregation. Normally, enhanced aggregation must be enabled where aggregations are used.                                                                                                                                                           |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | The value can be:                                                                                                                                                                                                                                                             |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | -  **false**: Disable enhanced aggregation.                                                                                                                                                                                                                                   |
      |                            |                  |                 | -  **true**: Enable enhanced aggregation.                                                                                                                                                                                                                                     |
      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | index.sort.field           | Array of strings | N/A             | Specify sorting keys. Sorting keys are fields used to sequence or rank documents.                                                                                                                                                                                             |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | You can specify one or multiple fields as sorting keys. When multiple fields are specified, they will apply in the sequence in which they are specified. Documents are first ranked by the first field, then the initial result set is ranked by the second field, and so on. |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | Constraint: High-cardinality fields must be among the sorting keys, and must follow the last low-cardinality field.                                                                                                                                                           |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | Value range: The value must be fields contained in the index.                                                                                                                                                                                                                 |
      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | index.cluster.field        | Array of strings | N/A             | Specify clustering keys. Clustering keys determine which documents are collected into the same clusters.                                                                                                                                                                      |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | During an aggregation operation, documents in the same cluster can be processed in batches, significantly enhancing aggregation performance.                                                                                                                                  |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | Constraint: The clustering keys must be a subset of the sorting keys.                                                                                                                                                                                                         |
      |                            |                  |                 |                                                                                                                                                                                                                                                                               |
      |                            |                  |                 | Value range: The value must be fields contained in the index.                                                                                                                                                                                                                 |
      +----------------------------+------------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Run the following command to import sample data.

   .. code-block:: text

      PUT /_bulk
      { "index": { "_index": "testindex", "_id": "1" } }
      { "date": "2025-01-01", "city": "cityA", "product": "books", "trade": 3000.0}
      { "index": { "_index": "testindex", "_id": "2" } }
      { "date": "2025-01-02", "city": "cityA", "product": "books", "trade": 1000.0}
      { "index": { "_index": "testindex", "_id": "3" } }
      { "date": "2025-01-01", "city": "cityA", "product": "bottles", "trade": 100.0}
      { "index": { "_index": "testindex", "_id": "4" } }
      { "date": "2025-01-02", "city": "cityA", "product": "bottles", "trade": 300.0}
      { "index": { "_index": "testindex", "_id": "5" } }
      { "date": "2025-01-01", "city": "cityB", "product": "books", "trade": 7000.0}
      { "index": { "_index": "testindex", "_id": "6" } }
      { "date": "2025-01-02", "city": "cityB", "product": "books", "trade": 1000.0}

#. Run the following query command to perform a hybrid aggregation of low- and high-cardinality fields.

   For example, query the average **trade** value of each product in different cities on each day specified by the **date** field.

   .. code-block:: text

      POST testindex/_search
      {
        "size": 0,
        "aggs": {
          "groupby_region": {
            "terms": {
              "field": "city"
            },
            "aggs": {
              "groupby_host": {
                "terms": {
                  "field": "product"
                },
                "aggs": {
                  "groupby_timestamp": {
                    "date_histogram": {
                      "field": "date",
                      "interval": "day"
                    },
                    "aggs": {
                      "avg_score": {
                        "avg": {
                          "field": "trade"
                        }
                      }
                    }
                  }
                }
              }
            }
          }
        }
      }
