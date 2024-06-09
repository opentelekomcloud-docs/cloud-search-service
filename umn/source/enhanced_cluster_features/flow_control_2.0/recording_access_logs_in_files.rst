:original_name: en-us_topic_0000001832788405.html

.. _en-us_topic_0000001832788405:

Recording Access Logs in Files
==============================

The traffic control function can record cluster access logs and write the logs to background log files. You can back up the logs to OBS for viewing. You can run the following command to enable the function of recording access logs to files:

.. code-block:: text

   PUT /_cluster/settings
   {
     "persistent": {
       "flowcontrol.log.file.enabled": true
     }
   }

.. table:: **Table 1** Parameters

   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+
   | Parameter                    | Type                  | Description                                                                                               |
   +==============================+=======================+===========================================================================================================+
   | flowcontrol.log.file.enabled | Boolean               | Indicates whether to record the log details of each request to the background log file. The value can be: |
   |                              |                       |                                                                                                           |
   |                              |                       | -  true                                                                                                   |
   |                              |                       | -  **false** (default value)                                                                              |
   +------------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------+

.. note::

   -  After the function of recording access logs to files is enabled, access from a client to a cluster node is recorded in the **{Cluster name\ \_access_log.log}** file. You can use the log backup function to view detailed access logs.
   -  After the fault is located, you are advised to disable this function.
