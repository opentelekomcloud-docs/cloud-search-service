:original_name: en-us_topic_0000001527697797.html

.. _en-us_topic_0000001527697797:

How Do I Check the Numbers of Shards and Replicas in a Cluster on the CSS Console?
==================================================================================

#. Log in to the console.

#. On the **Clusters** page, click **Access Kibana** in the **Operation** column of a cluster.

#. Log in to Kibana and choose **Dev Tools**.

   |image1|

#. On the **Console** page, run the **GET \_cat/indices?v** command query the number of shards and replicas in a cluster. In the following figure, the **pri** column indicates the number of index shards, and the **rep** column indicates the number of replicas. After an index is created, its **pri** value cannot be modified. Its **rep** value can be modified.

   |image2|

.. |image1| image:: /_static/images/en-us_image_0000001477137554.png
.. |image2| image:: /_static/images/en-us_image_0000001476977570.png
