:original_name: css_02_0125.html

.. _css_02_0125:

How Do I Change the Maximum Number of Results Returned for Searches to an Index in an Elasticsearch Cluster of CSS?
===================================================================================================================

Solution
--------

-  Method 1

   Open Kibana and run the following commands on the **DevTools** page:

   .. code-block:: text

      PUT _all/_settings?preserve_existing=true
      {
      "index.max_result_window" : "10000000"
      }

-  Method 2

   Run the following command on a server (a non-security mode cluster is used as an example here):

   .. code-block::

      curl -k -XPUT 'http://localhost:9200/_all/_setting?preserve_existing=true'-d
      {
      "index.max_result_window":"1000000"
      }

   **localhost** indicates the address of the Elasticsearch cluster.

.. caution::

   This configuration consumes memory and CPU resources. Exercise caution when setting this parameter.
