:original_name: css_01_0176.html

.. _css_01_0176:

Low-cardinality and High-cardinality Field Mixing
=================================================

In the scenario where low-cardinality and high-cardinality fields are mixed, assume that the following query statement exists:

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

Group the low-cardinality fields and create a histogram using the high-cardinality fields. To use the enhanced aggregation for the preceding query, set the parameters as follows:

.. note::

   -  A clustering key is the prefix subset of a sorting key.
   -  High-cardinality fields must be in the sorting key, and high-cardinality fields must follow the last low-cardinality field.

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
                   "region",
                   "host",
                   "timestamp",
                   "other"
               ]
           },
           "cluster" : {
               "field" : [ // Specify a clustering key
                   "region",
                   "host"
               ]
           }
       }
   }
