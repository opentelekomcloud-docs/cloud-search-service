:original_name: css_01_0174.html

.. _css_01_0174:

Grouping and Aggregation of Low-cardinality Fields
==================================================

Low-cardinality fields have high data clustering performance when being sorted, which facilitates vectorized optimization. Assume that the following query statement exists:

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

Assume that the **region** and **host** are low-cardinality fields. To use the enhanced aggregation, set the parameters as follows:

.. note::

   The clustering key must be a prefix subset of the sorting key.

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
