:original_name: en-us_topic_0000001584708761.html

.. _en-us_topic_0000001584708761:

Performance Data
================

-  Test environment

   -  Cluster: 3 Cloud M6 ECSs (8 vCPUs \| 64 GB memory)
   -  Data: `open-source web server access logs <https://www.kaggle.com/datasets/eliasdabbas/web-server-access-logs>`__ and internal service dataset (dns_logs)
   -  Configuration: 120 shards, no replicas, and all the enhanced features enabled

-  Test result

   =================== ==================== =================== ===========
   Type                Performance (Before) Performance (After) Improved By
   =================== ==================== =================== ===========
   Open-source dataset 85 Mbit/s            131 Mbit/s          54%
   Service dataset     124 Mbit/s           218 Mbit/s          76%
   =================== ==================== =================== ===========
