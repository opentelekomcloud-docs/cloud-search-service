:original_name: css_01_0173.html

.. _css_01_0173:

Features
========

The enhanced aggregation is an optimization feature for service awareness. With this feature, you can optimize the aggregation analysis capability of observable services.

Currently, the enhanced aggregation is supported by only clusters of version 7.10.2.

Working Principles
------------------

In large-scale dataset aggregation and analysis scenarios, data grouping and aggregation takes a lot of time. Improving the grouping aggregation capability depends on the following key features:

-  Sorting key: Data is stored in sequence based on the sorting key.
-  Clustering key: It is contained in the sorting key. Data is clustered based on the clustering key.

In the case of data clustering, enhanced aggregation uses the vectorization technology to process data in batches, improving aggregation performance.

.. table:: **Table 1** Feature parameters

   +----------------------------+-------------------------------------------------------------------------+
   | Parameter                  | Description                                                             |
   +============================+=========================================================================+
   | index.search.turbo.enabled | Indicates whether to enable the feature. The default value is **true**. |
   +----------------------------+-------------------------------------------------------------------------+
   | index.sort.field           | Sorting key                                                             |
   +----------------------------+-------------------------------------------------------------------------+
   | index.cluter.field         | Clustering key                                                          |
   +----------------------------+-------------------------------------------------------------------------+


Features
--------

Based on different service requirements, enhanced aggregation can be used in the following three scenarios:

-  :ref:`Grouping and Aggregation of Low-cardinality Fields <css_01_0174>`
-  :ref:`High-cardinality Field Histogram Aggregation <css_01_0175>`
-  :ref:`Low-cardinality and High-cardinality Field Mixing <css_01_0176>`
