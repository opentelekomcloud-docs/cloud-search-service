:original_name: css_01_0005.html

.. _css_01_0005:

Different Ways to Ingest Data into an Elasticsearch Cluster
===========================================================

Introduction
------------

Elasticsearch clusters support multiple data ingestion methods, as listed in :ref:`Table 1 <en-us_topic_0000001945265112__en-us_topic_0000001961259049_table114913297713>`. Select one that fits your needs the best. Before starting to ingest data, determine whether to enhance the data ingestion performance of Elasticsearch clusters first. For details, see :ref:`Enhancing the Data Ingestion Performance of Elasticsearch Clusters <css_01_0228>`.

.. _en-us_topic_0000001945265112__en-us_topic_0000001961259049_table114913297713:

.. table:: **Table 1** Different ways to ingest data into an Elasticsearch cluster

   +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------------------------------------------------------------------------------+
   | Data Ingestion Method         | Scenario                                                                                                                                                                                                                        | Supported Data Formats/Sources | Details                                                                                   |
   +===============================+=================================================================================================================================================================================================================================+================================+===========================================================================================+
   | Open-source Logstash          | Open-source Logstash offers a server-side, real-time data processing pipeline, which supports data ingestion from multiple sources. It can be used to ingest various types of data, such as logs, monitoring data, and metrics. | JSON, CSV, and text            | :ref:`Using In-house Built Logstash to Import Data to Elasticsearch <css_01_0048>`        |
   +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------------------------------------------------------------------------------+
   | Open-source Elasticsearch API | Open-source Elasticsearch APIs can be used to ingest data. This method is flexible, as you can write your own application code.                                                                                                 | JSON                           | :ref:`Using Open Source Elasticsearch APIs to Import Data to Elasticsearch <css_01_0024>` |
   +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------------------------------------------------------------------------------+
   | Cloud Data Migration (CDM)    | You can use CDM for batch data migration. For example, if data is stored in OBS or an Oracle database, CDM is recommended.                                                                                                      | JSON                           | :ref:`Using CDM to Import Data to Elasticsearch <css_01_0046>`                            |
   +-------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+--------------------------------+-------------------------------------------------------------------------------------------+
