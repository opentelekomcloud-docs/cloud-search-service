:original_name: css_01_0144.html

.. _css_01_0144:

Request Sampling
================

Context
-------

Request sampling can record the access IP addresses, the number of accessed nodes, request paths, request URLs, and request bodies, which can be used to obtain the IP addresses and paths of clients that have sent a large number of access requests.

The following table describes request sampling parameters.

.. table:: **Table 1** Request sampling parameters

   +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                            | Type                  | Description                                                                                                                                                                                            |
   +======================================+=======================+========================================================================================================================================================================================================+
   | flowcontrol.statics.enabled          | Boolean               | Whether to enable request sampling. Request sampling may affect node performance.                                                                                                                      |
   |                                      |                       |                                                                                                                                                                                                        |
   |                                      |                       | Value: **true** or **false**                                                                                                                                                                           |
   |                                      |                       |                                                                                                                                                                                                        |
   |                                      |                       | Default value: **false**                                                                                                                                                                               |
   +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.statics.threshold        | Integer               | Number of recent access requests whose statistics are collected. The value **100** indicates that statistics will be collected on the 100 IP addresses and 100 URLs that are most frequently accessed. |
   |                                      |                       |                                                                                                                                                                                                        |
   |                                      |                       | Minimum value: **10**                                                                                                                                                                                  |
   |                                      |                       |                                                                                                                                                                                                        |
   |                                      |                       | Maximum value: **1000**                                                                                                                                                                                |
   |                                      |                       |                                                                                                                                                                                                        |
   |                                      |                       | Default value: **100**                                                                                                                                                                                 |
   +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.statics.sample_frequency | Integer               | Path sampling frequency. If this parameter is set to **100**, samples are collected from every 100 requests.                                                                                           |
   |                                      |                       |                                                                                                                                                                                                        |
   |                                      |                       | Minimum value: **50**                                                                                                                                                                                  |
   |                                      |                       |                                                                                                                                                                                                        |
   |                                      |                       | Default value: **100**                                                                                                                                                                                 |
   +--------------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   -  The IP address statistics and URL sampling statistics are cached based on their access time. If the cache space reaches the threshold (**flowcontrol.statics.threshold**), the records of the earliest access will be deleted.
   -  In URL sampling, an access path is uniquely identified by its URL hash.

Procedure
---------

#. Log in to the CSS management console.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
#. In the navigation pane on the left, choose **Dev Tools** and run commands to enable or disable sampling.

   -  Enabling sampling

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.statics.enabled": true,
             "flowcontrol.statics.threshold": 100,
             "flowcontrol.statics.sample_frequency": 50
           }
         }

   -  Disabling sampling

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.statics.enabled": false
           }
         }
