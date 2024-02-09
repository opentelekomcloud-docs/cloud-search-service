:original_name: css_01_0135.html

.. _css_01_0135:

Context
=======

CSS monitors various metrics of the running status and change trend of cluster indexes to measure service usage and handle potential risks in a timely manner, ensuring that clusters can run stably.

During index monitoring, the **stats** information about indexes is collected and saved to the monitoring index (**monitoring-eye-css-**\ *[yyyy-mm-dd]*) of the cluster, and retained for one week by default.

Currently, only clusters of the version 7.6.2 and 7.10.2 support index monitoring.
