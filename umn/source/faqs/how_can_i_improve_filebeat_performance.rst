:original_name: css_02_0018.html

.. _css_02_0018:

How Can I Improve Filebeat Performance?
=======================================

Symptom
-------

Filebeat is a high-performance file collection tool. By default, one core is allocated to Filebeat, and it writes 1 MB data to Elasticsearch per second. However, in practice, when a large number of service logs are generated, Filebeat cannot promptly collect and write them to Elasticsearch. In this case, you can optimize parameter settings in the **filebeat.yml** file to improve the Filebeat performance.

Procedure
---------

#. Optimize the parameters involved in **input** of the **filebeat.yml** configuration file.

   Increase the value of **harvester_buffer_size** based on actual requirements. This parameter defines the buffer size used by every **harvester**.

   **harvester_buffer_size**: **40,960,000**

   Increase the value of **filebeat.spool_size** based on actual requirements. This parameter defines the number of log records that can be uploaded by the **spooler** at a time.

   **filebeat.spool_size**: **250,000**

   Adjust the value of **filebeat.idle_timeout** based on actual requirements. This parameter defines how often the **spooler** is flushed. After the **idle_timeout** is reached, the **spooler** is flushed regardless of whether the **spool_size** has been reached.

   **filebeat.idle_timeout**: **1s**

#. Optimize the parameters involved in **output.elasticsearch** in the **filebeat.yml** configuration file.

   Set the value of **worker** to the number of Elasticsearch clusters based on actual requirements. This parameter indicates the number of Elasticsearch clusters. The default value is **1**.

   **worker**: **1**

   Increase the value of **bulk_max_size** based on actual requirements. This parameter defines the maximum number of events to bulk in a single Elasticsearch bulk API index request. The default is **50**.

   **bulk_max_size**: **15,000**

   Adjust the value of **flush_interval** based on the actual requirements. This parameter defines the number of seconds to wait for new events between two bulk API index requests. If **bulk_max_size** is reached before this interval expires, additional bulk index requests are made.

   **flush_interval**: **1s**
