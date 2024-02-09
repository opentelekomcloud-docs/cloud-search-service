:original_name: css_01_0162.html

.. _css_01_0162:

Features
========

CSS supports read/write splitting. Data written to the primary cluster (**Leader**) can be automatically synchronized to the secondary cluster (**Follower**). In this way, data is written to the primary cluster and queried in the secondary cluster. The read and write can be separated to improve the query performance (as shown in the left part of :ref:`Figure 1 <css_01_0162__en-us_topic_0000001268154533_fig165871420101917>`). When the primary cluster is unavailable, the secondary cluster can provide data write and query services (as shown in the right part of :ref:`Figure 1 <css_01_0162__en-us_topic_0000001268154533_fig165871420101917>`).

.. _css_01_0162__en-us_topic_0000001268154533_fig165871420101917:

.. figure:: /_static/images/en-us_image_0000001666842902.jpg
   :alt: **Figure 1** Two application scenarios of read/write splitting

   **Figure 1** Two application scenarios of read/write splitting

Currently, only clusters of versions 7.6.2 and 7.10.2 support read/write isolation.
