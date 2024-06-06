:original_name: en-us_topic_0000001528499145.html

.. _en-us_topic_0000001528499145:

High-cardinality Field Histogram Aggregation
============================================

High-cardinality fields are usually used for histogram grouping and aggregation instead of single-point grouping and aggregation. For example, collecting the statistics of logs at a certain period. Assume that the following query statement exists:

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

This query groups the field **timestamp** using a histogram and calculates the average score. **timestamp** is a typical high-cardinality field. To use the enhanced aggregation for the preceding query, set parameters as follows:

.. code-block::

   // Configure an index
   "settings" : {
       "index" : {
           "search" : {
               "turbo" : {
                   "enabled" : "true" // Enable optimization
               }
           },
           "sort" : { // Specify a sorting key
               "field" : [
                   "timestamp"
               ]
           }
       }
   }
