:original_name: css_02_0067.html

.. _css_02_0067:

How Do I Clear Elasticsearch Indexes in CSS?
============================================

.. note::

   Before deleting index data, carefully evaluate any potential impact on services.

-  Have indexes automatically cleared on a regular basis.

   You can create a scheduled task to execute an index deletion request periodically. CSS supports Open Distro Index State Management. For details about how to clear obsolete indexes periodically, see :ref:`Decoupling Index Storage and Compute in an Elasticsearch Cluster Through Index Lifecycle Management <css_01_0421>`.

   For details about Open Distro Index State Management, see https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/.

-  Manually clear indexes.

   -  Log in to Kibana and run the **DELETE / Index name** command in Dev Tools.

   -  Log in to Cerebro, search for the target index name, click the index name, click ****delete index****, and click **Confirm** in the displayed dialog box.


      .. figure:: /_static/images/en-us_image_0000001960517893.png
         :alt: **Figure 1** Deleting an index from Cerebro

         **Figure 1** Deleting an index from Cerebro
