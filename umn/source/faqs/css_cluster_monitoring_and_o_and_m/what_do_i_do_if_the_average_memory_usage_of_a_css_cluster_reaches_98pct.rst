:original_name: css_02_0131.html

.. _css_02_0131:

What Do I Do If the Average Memory Usage of a CSS Cluster Reaches 98%?
======================================================================

Symptom
-------

The cluster monitoring result shows that the average memory usage of a cluster is 98%. Does it affect cluster performance?

Possible Cause
--------------

In an Elasticsearch cluster, 50% of the memory is occupied by Elasticsearch and the other 50% is used by Lucene to cache files. It is normal that the average memory usage reaches 98%.

Solution
--------

You can monitor the cluster memory usage by checking the maximum JVM heap usage and average JVM heap usage.
