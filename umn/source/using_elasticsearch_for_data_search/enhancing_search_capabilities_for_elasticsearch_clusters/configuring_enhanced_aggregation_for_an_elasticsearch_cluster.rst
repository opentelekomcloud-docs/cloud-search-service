:original_name: css_01_0409.html

.. _css_01_0409:

Configuring Enhanced Aggregation for an Elasticsearch Cluster
=============================================================

Scenario
--------

In the case of data clustering, enhanced aggregation uses the vectorization technology to process data in batches, improving aggregation performance and facilitating aggregated analysis for faster time to insight.

In large-scale dataset aggregation and analysis scenarios, a major chunk of the time is spent on data grouping and aggregation.

Enhancing data grouping and aggregation relies on two things:

-  Sorting key: Data is sorted based on the sorting key.
-  Cluster key: It is contained in the sorting key. Data is clustered based on the clustering key.

:ref:`Table 1 <css_01_0409__table4445153814017>` describes common scenarios that involve enhanced aggregation.

.. _css_01_0409__table4445153814017:

.. table:: **Table 1** Common scenarios for enhanced aggregation

   +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
   | Scenario                                               | Description                                                                                                                                 | Details                                                                                       |
   +========================================================+=============================================================================================================================================+===============================================================================================+
   | Aggregation of low-cardinality fields                  | Aggregates fields that have a small number of unique values, for example, a field that indicates storage classes.                           | :ref:`Grouping and Aggregation of Low-cardinality Fields <css_01_0409__section1023014371242>` |
   +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
   | Aggregation of high-cardinality fields                 | Aggregates fields that have a large number of unique values, for example, a field that indicates storage time, which can aggregated by day. | :ref:`High-cardinality Field Histogram Aggregation <css_01_0409__section189669435249>`        |
   +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+
   | Hybrid aggregation of low- and high-cardinality fields | Groups and aggregates low-cardinality fields first, and then creates a histogram using high-cardinality fields.                             | :ref:`Low-cardinality and High-cardinality Field Mixing <css_01_0409__section10515934174813>` |
   +--------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------+

Constraints
-----------

Only Elasticsearch 7.10.2 clusters support aggregation enhancement.

.. _css_01_0409__section1023014371242:

Grouping and Aggregation of Low-cardinality Fields
--------------------------------------------------

Generally, low-cardinality fields use grouping as a way of aggregation. With an appropriate sorting key, grouping prepares the data for batch vectorization.

For example, the query statement is as follows:

.. code-block:: text

   POST testindex/_search
   {
     "size": 0,
     "aggs": {
       "groupby_region": {
         "terms": {
           "field": "region"
         },
         "aggs": {
           "groupby_host": {
             "terms": {
               "field": "host"
             },
             "aggs": {
               "avg_cpu_usage": {
                 "avg": {
                   "field": "cpu_usage"
                 }
               }
             }
           }
         }
       }
     }
   }

Assume that **region** and **host** are low-cardinality fields. To use enhanced aggregation, set parameters as follows:

.. code-block::

   //Configure an index
   "settings" : {
       "index" : {
           "search" : {
               "turbo" : {
                   "enabled" : "true" //Enable optimization
               }
           },
           "sort" : { //Specify a sorting key
               "field" : [
                   "region",
                   "host",
                   "other"
               ]
           },
           "cluster" : {
               "field" : [ //Specify a clustering key
                   "region",
                   "host"
               ]
           }
       }
   }

.. note::

   The clustering key must be a subset of the sorting key.

.. _css_01_0409__section189669435249:

High-cardinality Field Histogram Aggregation
--------------------------------------------

High-cardinality fields commonly use histogram aggregation, which facilitates data processing per range.

For example, the query statement is as follows: This query groups the field timestamp using a histogram and calculates the average score.

.. code-block:: text

   POST testindex/_search?pretty
   {
     "size": 0,
     "aggs": {
       "avg_score": {
         "avg": {
           "field": "score"
         },
         "aggs": {
           "groupbytime": {
             "date_histogram": {
               "field": "timestamp",
               "calendar_interval": "day"
             }
           }
         }
       }
     }
   }

**timestamp** is a typical high-cardinality field. To apply enhanced aggregation to such a field, set parameters as follows:

.. code-block::

   //Configure an index
   "settings" : {
       "index" : {
           "search" : {
               "turbo" : {
                   "enabled" : "true" //Enable optimization
               }
           },
           "sort" : { //Specify a sorting key
               "field" : [
                   "timestamp"
               ]
           }
       }
   }

.. _css_01_0409__section10515934174813:

Low-cardinality and High-cardinality Field Mixing
-------------------------------------------------

Where low-cardinality and high-cardinality fields are mixed, first groups and aggregates low-cardinality fields, and then aggregates high-cardinality fields using histograms.

For example, the query statement is as follows:

.. code-block:: text

   POST testindex/_search
   {
     "size": 0,
     "aggs": {
       "groupby_region": {
         "terms": {
           "field": "region"
         },
         "aggs": {
           "groupby_host": {
             "terms": {
               "field": "host"
             },
             "aggs": {
               "groupby_timestamp": {
                 "date_histogram": {
                   "field": "timestamp",
                   "interval": "day"
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
         }
       }
     }
   }

To first group the low-cardinality field **region**, and then the low-cardinality field **host**, and then cluster the high-cardinality field **timestamp** using a histogram, set the parameters as follows:

.. code-block::

   //Configure an index
   "settings" : {
       "index" : {
           "search" : {
               "turbo" : {
                   "enabled" : "true" //Enable optimization
               }
           },
           "sort" : { //Specify a sorting key
               "field" : [
                   "region",
                   "host",
                   "timestamp",
                   "other"
               ]
           },
           "cluster" : {
               "field" : [ //Specify a clustering key
                   "region",
                   "host"
               ]
           }
       }
   }

.. note::

   -  The clustering key must be a subset of the sorting key.
   -  High-cardinality fields must be in the sorting key, and high-cardinality fields must follow the last low-cardinality field.

Performance Testing
-------------------

**Test environment**

-  Dataset: esrally nyc_taxis
-  Cluster specifications: 4U16G, 100 GB, high I/O x 3 nodes

**Test Procedure**

#. Create an index template in the cluster, specify sorting keys, and disable enhanced aggregation.

   .. code-block:: text

      PUT /_template/nyc_taxis
      {
        "template": "nyc_taxis*",
        "settings": {
          "index.search.turbo.enabled": false,
          "index.sort.field": "dropoff_datetime",
          "number_of_shards": 3,
          "number_of_replicas": 0
        }
      }

#. Use esrally to test the nyc_taxis dataset and obtain the result when enhanced aggregation is disabled.

#. Create another index template in the same cluster, specify sorting keys, and enable enhanced aggregation.

   .. code-block:: text

      PUT /_template/nyc_taxis
      {
        "template": "nyc_taxis*",
        "settings": {
          "index.search.turbo.enabled": true,
          "index.sort.field": "dropoff_datetime",
          "number_of_shards": 3,
          "number_of_replicas": 0
        }
      }

#. Use esrally to test the nyc_taxis dataset and obtain the result when enhanced aggregation is enabled.

**Test Result**

This test focuses on the query result of **dropoff_datetime** aggregation, that is, the results of tasks **autohisto_agg** and **date_histogram_agg**. The following table compares the test results between when enhanced aggregation is disabled and when it is enabled.

+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Metric                        | Task               | Unit  | Enhanced Aggregation Disabled |              |              | Enhanced Aggregation Enabled |              |              | Enhanced Aggregation Disabled | Enhanced Aggregation Enabled | open/close | Conclusion                               |
+===============================+====================+=======+===============================+==============+==============+==============================+==============+==============+===============================+==============================+============+==========================================+
|                               |                    |       | Test Round 1                  | Test Round 2 | Test Round 3 | Test Round 1                 | Test Round 2 | Test Round 3 | Mean Value                    | Mean Value                   |            |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Min Throughput                | autohisto_agg      | ops/s | 4.42                          | 4.44         | 4.43         | 11.66                        | 11.94        | 11.96        | 4.43                          | 11.85                        | 2.68       | Throughput improves more than 2.5 times. |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Mean Throughput               | autohisto_agg      | ops/s | 4.50                          | 4.46         | 4.44         | 11.81                        | 11.99        | 12.00        | 4.47                          | 11.93                        | 2.67       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Median Throughput             | autohisto_agg      | ops/s | 4.51                          | 4.46         | 4.44         | 11.83                        | 11.98        | 12.00        | 4.47                          | 11.94                        | 2.67       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Max Throughput                | autohisto_agg      | ops/s | 4.54                          | 4.48         | 4.45         | 11.90                        | 12.07        | 12.02        | 4.49                          | 12.00                        | 2.67       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| 100th percentile latency      | autohisto_agg      | ms    | 216.30                        | ``-``        | ``-``        | ``-``                        | 84.56        | 80.38        | 216.30                        | 82.47                        | 0.38       | Latency decreases by more than 60%.      |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| 100th percentile service time | autohisto_agg      | ms    | 216.30                        | ``-``        | ``-``        | ``-``                        | 84.56        | 80.38        | 216.30                        | 82.47                        | 0.38       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| error rate                    | autohisto_agg      | %     | 0                             | 0            | 0            | 0                            | 0            | 0            | 0                             | 0                            | 0          | ``-``                                    |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Min Throughput                | date_histogram_agg | ops/s | 4.72                          | 4.67         | 4.65         | 12.57                        | 12.40        | 12.59        | 4.68                          | 12.52                        | 2.68       | Throughput improves more than 2.5 times. |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Mean Throughput               | date_histogram_agg | ops/s | 4.73                          | 4.67         | 4.67         | 12.61                        | 12.46        | 12.61        | 4.69                          | 12.56                        | 2.68       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Median Throughput             | date_histogram_agg | ops/s | 4.73                          | 4.67         | 4.67         | 12.62                        | 12.46        | 12.60        | 4.69                          | 12.56                        | 2.68       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| Max Throughput                | date_histogram_agg | ops/s | 4.74                          | 4.67         | 4.67         | 12.64                        | 12.49        | 12.63        | 4.69                          | 12.59                        | 2.68       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| 50th percentile latency       | date_histogram_agg | ms    | 202.61                        | 218.09       | 213.43       | 77.64                        | 76.02        | 82.63        | 211.38                        | 78.77                        | 0.37       | Latency decreases by more than 60%.      |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| 100th percentile latency      | date_histogram_agg | ms    | 207.35                        | 223.88       | 246.63       | 77.99                        | ``-``        | ``-``        | 225.95                        | 77.99                        | 0.35       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| 50th percentile service time  | date_histogram_agg | ms    | 202.61                        | 218.09       | 213.43       | 77.64                        | 76.02        | 82.63        | 211.38                        | 78.77                        | 0.37       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| 100th percentile service time | date_histogram_agg | ms    | 207.35                        | 223.88       | 246.63       | 77.99                        | ``-``        | ``-``        | 225.95                        | 77.99                        | 0.35       |                                          |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+
| error rate                    | date_histogram_agg | %     | 0                             | 0            | 0            | 0                            | 0            | 0            | 0                             | 0                            | 0          | ``-``                                    |
+-------------------------------+--------------------+-------+-------------------------------+--------------+--------------+------------------------------+--------------+--------------+-------------------------------+------------------------------+------------+------------------------------------------+

**Test Conclusion**

Given the same cluster configuration, aggregation performance improves significantly when enhanced aggregation is enabled. Query throughput improves by more than 2.5 times, and latency decreases by more than 60%.
