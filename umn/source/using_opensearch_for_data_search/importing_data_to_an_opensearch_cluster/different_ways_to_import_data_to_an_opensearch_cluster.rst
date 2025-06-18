:original_name: css_01_0454.html

.. _css_01_0454:

Different Ways to Import Data to an OpenSearch Cluster
======================================================

Introduction
------------

OpenSearch clusters support multiple data import methods, as listed in :ref:`Table 1 <css_01_0454__css_01_0394_en-us_topic_0000001961259049_table114913297713>`. Select one that fits your needs the best. Before starting to import data, determine whether to enhance the data import performance of OpenSearch clusters first. For details, see :ref:`Enhancing the Data Import Performance of OpenSearch Clusters <css_01_0458>`.

.. _css_01_0454__css_01_0394_en-us_topic_0000001961259049_table114913297713:

.. table:: **Table 1** Different ways to import data to an OpenSearch cluster

   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+---------------------------------------------------------------------------------------------------------------+
   | Data Import Method                | Scenario                                                                                                                                                                                                                | Supported Data Formats            | Details                                                                                                       |
   +===================================+=========================================================================================================================================================================================================================+===================================+===============================================================================================================+
   | Logstash data processing pipeline | Open-source Logstash offers a server-side, real-time data processing pipeline, which supports data ingestion from multiple sources. It can be used to collect various data, such as logs, monitoring data, and metrics. | JSON, CSV, and text               | :ref:`Using In-house Built Logstash to Import Data to an OpenSearch Cluster <css_01_0455>`                    |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+---------------------------------------------------------------------------------------------------------------+
   | Open-source OpenSearch API        | Open-source Elasticsearch APIs can be used to import data. This method is flexible, as you can write your own application code.                                                                                         | JSON                              | :ref:`Using Open Source OpenSearch APIs to Import Data to an OpenSearch Cluster <css_01_0456>`                |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+---------------------------------------------------------------------------------------------------------------+
   | Cloud Data Migration (CDM)        | You can use CDM for batch data migration. For example, if data is stored in OBS or an Oracle database, CDM is recommended.                                                                                              | JSON                              | :ref:`Using CDM to Import Data to an OpenSearch Cluster <css_01_0457>`                                        |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+---------------------------------------------------------------------------------------------------------------+
   | Data Replication Service (DRS)    | DRS can be used for online database migration and real-time data synchronization.                                                                                                                                       | Relational Database Service (RDS) | :ref:`Using DRS to Import Data from a Database to OpenSearch <css_01_0454__css_01_0394_section1896852904516>` |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+---------------------------------------------------------------------------------------------------------------+

.. _css_01_0454__css_01_0394_section1896852904516:

Using DRS to Import Data from a Database to OpenSearch
------------------------------------------------------

DRS is an easy-to-use, stable, and efficient cloud service for online database migration and real-time database synchronization. Real-time data synchronization refers to the real-time replication of data from one source to another while ensuring data consistency.

DRS can be used to import data from multiple types of relational databases to OpenSearch clusters. For details about the supported software versions for source databases and destination clusters, see :ref:`Table 2 <css_01_0454__css_01_0394_table1099912411111>`.

.. _css_01_0454__css_01_0394_table1099912411111:

.. table:: **Table 2** Using DRS to import data from a database to an OpenSearch cluster

   +----------------------------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------------+
   | Scenario                                                                         | Source DB                                                             | Destination OpenSearch Cluster |
   +==================================================================================+=======================================================================+================================+
   | Importing data from an RDS for MySQL database to a CSS OpenSearch cluster        | RDS for MySQL 5.5, 5.6, 5.7, or 8.0                                   | OpenSearch 1.3.6               |
   +----------------------------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------------+
   | Importing data from a TaurusDB database to a CSS Elasticsearch cluster           | Primary/standby TaurusDB instances                                    | OpenSearch 1.3.6               |
   +----------------------------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------------+
   | Importing data from an in-house built MySQL database to a CSS OpenSearch cluster | MySQL database 5.5, 5.6, 5.7, or 8.0 created on a local server or ECS | OpenSearch 1.3.6               |
   +----------------------------------------------------------------------------------+-----------------------------------------------------------------------+--------------------------------+
