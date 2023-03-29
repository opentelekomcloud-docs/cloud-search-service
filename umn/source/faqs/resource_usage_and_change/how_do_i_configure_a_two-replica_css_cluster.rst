:original_name: css_02_0068.html

.. _css_02_0068:

How Do I Configure a Two-Replica CSS Cluster?
=============================================

#. Run **GET \_cat/indices?v** in Kibana to check the number of cluster replicas. If the value of **rep** is **1**, the cluster has two replicas.

   |image1|

#. If the value of **rep** is not **1**, run the following command to set the number of replicas:

   PUT /index/_settings

   {

   "number_of_replicas" : 1 //Number of replicas

   }

   .. note::

      **index** specifies the index name. Set this parameter based on site requirements.

.. |image1| image:: /_static/images/en-us_image_0000001528097321.png
