:original_name: en-us_topic_0000001528499125.html

.. _en-us_topic_0000001528499125:

Context
=======

CSS monitors various metrics of the running status and change trend of cluster indexes to measure service usage and handle potential risks in a timely manner, ensuring that clusters can run stably.

During index monitoring, the **stats** information about indexes is collected and saved to the monitoring index (**monitoring-eye-css-**\ *[yyyy-mm-dd]*) of the cluster, and retained for one week by default.

Currently, only the Elasticsearch clusters of the versions 7.6.2 and 7.10.2 support the index monitoring.
