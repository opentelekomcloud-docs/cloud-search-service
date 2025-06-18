:original_name: css_02_0133.html

.. _css_02_0133:

Do CSS Elasticsearch Clusters Support script dotProduct?
========================================================

The Elasticsearch-native vector search function is provided via an X-Pack plugin, which is currently not integrated in CSS. This is why the native **script dotProduct** cannot be executed in Elasticsearch clusters created in CSS.

You are advised to use the vector search service provided by CSS. Based on an in-house developed vector search engine, CSS's vector search service is deeply integrated with the Elasticsearch plug-in architecture, featuring high-performance, high-precision, low-cost, and multi-modality. It offers an efficient, cost-effective solution to meet diversified, high-dimensional vector search needs. For more information, see :ref:`Vector Search <css_01_0117>`.

.. note::

   Only Elasticsearch 7.6.2, Elasticsearch 7.10.2, and OpenSearch 1.3.6 clusters support the vector search engine of CSS.
