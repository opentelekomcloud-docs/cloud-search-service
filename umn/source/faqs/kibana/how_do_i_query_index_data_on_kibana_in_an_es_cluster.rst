:original_name: css_02_0099.html

.. _css_02_0099:

How Do I Query Index Data on Kibana in an ES Cluster?
=====================================================

Run the following command to query index data through an API on Kibana:

.. code-block:: text

   GET indexname/_search

The returned data is shown in the following figure.


.. figure:: /_static/images/en-us_image_0000001528097325.png
   :alt: **Figure 1** Returned data

   **Figure 1** Returned data

.. note::

   -  **took**: How many milliseconds the query cost.
   -  **time_out**: Whether a timeout occurred.
   -  **\_shard**: Data is split into five shards. All of the five shards have been searched and data is returned successfully. No query result fails to be returned. No data is skipped.
   -  **hits.total**: Number of query results. Three documents are returned in this example.
   -  **max_score**: Score of the returned documents. The document that is more relevant to your search criteria would have a higher score.
   -  **hits.hits**: Detailed information of the returned documents.
