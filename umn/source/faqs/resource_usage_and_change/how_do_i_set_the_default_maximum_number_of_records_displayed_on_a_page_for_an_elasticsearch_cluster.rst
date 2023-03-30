:original_name: css_02_0125.html

.. _css_02_0125:

How Do I Set the Default Maximum Number of Records Displayed on a Page for an Elasticsearch Cluster
===================================================================================================

Solution
--------

-  Method 1

   Open Kibana and run the following commands on the **Dev Tools** page:

   .. code-block:: text

      PUT _all/_settings?preserve_existing=true
      {
      "index.max_result_window" : "10000000"
      }

-  Method 2

   Run the following commands in the background:

   .. code-block::

      curl -XPUT 'http://localhost:9200/_all/_setting?preserve_existing=true'-d
      {
      "index.max_result_window":"1000000"
      }

.. caution::

   This configuration consumes memory and CPU resources. Exercise caution when setting this parameter.
