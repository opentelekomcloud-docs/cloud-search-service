:original_name: en-us_topic_0000001477739364.html

.. _en-us_topic_0000001477739364:

Request Sampling
================

Context
-------

Request sampling can record the access of client IP addresses and the type of requests from the client. Based on the statistics, you can identify the access traffic of client IP addresses and analyze the client write and query requests.

.. table:: **Table 1** Request statistics parameters

   +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                      | Type                  | Description                                                                                                                                      |
   +================================+=======================+==================================================================================================================================================+
   | flowcontrol.log.access.enabled | Boolean               | Whether to collect statistics on the IP addresses of clients that accessed the ES cluster recently and the number of requests. The value can be: |
   |                                |                       |                                                                                                                                                  |
   |                                |                       | -  **true**                                                                                                                                      |
   |                                |                       | -  **false** (default value)                                                                                                                     |
   +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
   | flowcontrol.log.access.count   | Integer               | Number of client IP addresses that accessed a cluster recently.                                                                                  |
   |                                |                       |                                                                                                                                                  |
   |                                |                       | Value range: 0-100                                                                                                                               |
   |                                |                       |                                                                                                                                                  |
   |                                |                       | Default value: **10**                                                                                                                            |
   +--------------------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   -  IP address statistics switches control whether to collect request type statistics and whether to enable logging.
   -  **flowcontrol.log.access.enabled** controls whether to collect statistics on client requests, including the number of bulk write, search, and msearch requests.
