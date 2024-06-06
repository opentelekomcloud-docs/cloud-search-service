:original_name: en-us_topic_0000001528659133.html

.. _en-us_topic_0000001528659133:

Monitoring Metrics of Clusters
==============================

You can use Cloud Eye to monitor cluster metrics of CSS in real time and quickly handle exceptions. For details about Cloud Eye, see the `Cloud Eye User Guide <https://docs.otc.t-systems.com/en-us/usermanual/ces/ces_07_0001.html>`__.

:ref:`Table 1 <en-us_topic_0000001528659133__en-us_topic_0000001223754380_table978532322710>` lists the metrics supported by CSS.

.. _en-us_topic_0000001528659133__en-us_topic_0000001223754380_table978532322710:

.. table:: **Table 1** Supported metrics

   +-----------------------+----------------------------------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
   | Metric                | Description                                  | Formula                                                    | Value Range                                                                                                                                                                            | Monitoring Interval |
   +=======================+==============================================+============================================================+========================================================================================================================================================================================+=====================+
   | Disk Usage            | Calculates the disk usage of a CSS cluster.  | Used disk space of a cluster/Total disk space of a cluster | 0 to 100%                                                                                                                                                                              | 1 minute            |
   |                       |                                              |                                                            |                                                                                                                                                                                        |                     |
   |                       | Unit: %                                      |                                                            |                                                                                                                                                                                        |                     |
   +-----------------------+----------------------------------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
   | Cluster Health Status | Measures the health status of a CSS cluster. | ``-``                                                      | Available values are **0**, **1**, and **2**.                                                                                                                                          | 1 minute            |
   |                       |                                              |                                                            |                                                                                                                                                                                        |                     |
   |                       |                                              |                                                            | -  **0**: The cluster is 100% available.                                                                                                                                               |                     |
   |                       |                                              |                                                            | -  **1**: The data is complete while some replicas are missing. Exceptions may occur because the high availability is compromised. This is a warning that should prompt investigation. |                     |
   |                       |                                              |                                                            | -  **2**: Data is missing and the cluster fails to work.                                                                                                                               |                     |
   +-----------------------+----------------------------------------------+------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+---------------------+
