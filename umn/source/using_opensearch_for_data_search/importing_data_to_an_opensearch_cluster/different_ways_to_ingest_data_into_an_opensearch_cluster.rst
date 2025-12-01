:original_name: css_01_0084.html

.. _css_01_0084:

Different Ways to Ingest Data into an OpenSearch Cluster
========================================================

Introduction
------------

OpenSearch clusters support multiple data ingestion methods, as listed in :ref:`Table 1 <en-us_topic_0000001992205785__en-us_topic_0000001945265112_en-us_topic_0000001961259049_table114913297713>`. Select one that fits your needs the best. Before starting to ingest data, determine whether to enhance the data ingestion performance of OpenSearch clusters first. For details, see :ref:`Enhancing the Data Ingestion Performance of OpenSearch Clusters <css_01_0090>`.

.. _en-us_topic_0000001992205785__en-us_topic_0000001945265112_en-us_topic_0000001961259049_table114913297713:

.. table:: **Table 1** Different ways to ingest data into an OpenSearch cluster

   +----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------+
   | Data Ingestion Method      | Scenario                                                                                                                                                                                                                        | Supported Data Formats | Details                                                                                        |
   +============================+=================================================================================================================================================================================================================================+========================+================================================================================================+
   | Open-source Logstash       | Open-source Logstash offers a server-side, real-time data processing pipeline, which supports data ingestion from multiple sources. It can be used to ingest various types of data, such as logs, monitoring data, and metrics. | JSON, CSV, and text    | :ref:`Using In-house Built Logstash to Ingest Data into an OpenSearch Cluster <css_01_0085>`   |
   +----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------+
   | Open-source OpenSearch API | Open-source Elasticsearch APIs can be used to ingest data. This method is flexible, as you can write your own application code.                                                                                                 | JSON                   | :ref:`Using Open Source OpenSearch APIs to Import Data to an OpenSearch Cluster <css_01_0087>` |
   +----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------+
   | Cloud Data Migration (CDM) | You can use CDM for batch data migration. For example, if data is stored in OBS or an Oracle database, CDM is recommended.                                                                                                      | JSON                   | :ref:`Using CDM to Import Data to an OpenSearch Cluster <css_01_0089>`                         |
   +----------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------+------------------------------------------------------------------------------------------------+
