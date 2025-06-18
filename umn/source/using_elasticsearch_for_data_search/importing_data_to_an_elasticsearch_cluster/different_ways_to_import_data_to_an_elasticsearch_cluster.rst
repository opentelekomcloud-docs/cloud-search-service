:original_name: css_01_0394.html

.. _css_01_0394:

Different Ways to Import Data to an Elasticsearch Cluster
=========================================================

Introduction
------------

Elasticsearch clusters support multiple data ingestion methods, as listed in :ref:`Table 1 <css_01_0394__en-us_topic_0000001961259049_table114913297713>`. Select one that fits your needs the best. Before starting to import data, determine whether to enhance the data import performance of Elasticsearch clusters first. For details, see :ref:`Enhancing the Data Import Performance of Elasticsearch Clusters <css_01_0397>`.

.. _css_01_0394__en-us_topic_0000001961259049_table114913297713:

.. table:: **Table 1** Different ways to import data to an Elasticsearch cluster

   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
   | Data Import Method                | Scenario                                                                                                                                                                                                                | Supported Data Formats            | Details                                                                                              |
   +===================================+=========================================================================================================================================================================================================================+===================================+======================================================================================================+
   | Logstash data processing pipeline | Open-source Logstash offers a server-side, real-time data processing pipeline, which supports data ingestion from multiple sources. It can be used to collect various data, such as logs, monitoring data, and metrics. | JSON, CSV, and text               | :ref:`Using In-house Built Logstash to Import Data to Elasticsearch <css_01_0048>`                   |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
   | Open-source Elasticsearch API     | Open-source Elasticsearch APIs can be used to import data. This method is flexible, as you can write your own application code.                                                                                         | JSON                              | :ref:`Using Open Source Elasticsearch APIs to Import Data to Elasticsearch <css_01_0024>`            |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
   | Cloud Data Migration (CDM)        | You can use CDM for batch data migration. For example, if data is stored in OBS or an Oracle database, CDM is recommended.                                                                                              | JSON                              | :ref:`Using CDM to Import Data to Elasticsearch <css_01_0396>`                                       |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+
   | Data Replication Service (DRS)    | DRS can be used for online database migration and real-time data synchronization.                                                                                                                                       | Relational Database Service (RDS) | :ref:`Using DRS to Import Data from a Database to Elasticsearch <css_01_0394__section1896852904516>` |
   +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------+------------------------------------------------------------------------------------------------------+

.. _css_01_0394__section1896852904516:

Using DRS to Import Data from a Database to Elasticsearch
---------------------------------------------------------

DRS is an easy-to-use, stable, and efficient cloud service for online database migration and real-time database synchronization. Real-time data synchronization refers to the real-time replication of data from one source to another while ensuring data consistency.

DRS can be used to import data from multiple types of relational databases to Elasticsearch clusters. For details about the supported software versions for source databases and destination clusters, see :ref:`Table 2 <css_01_0394__table1099912411111>`.

.. _css_01_0394__table1099912411111:

.. table:: **Table 2** Supported versions for using DRS to import data from a database to Elasticsearch

   +-------------------------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------+
   | Scenario                                                                            | Source DB                                                             | Destination Elasticsearch Cluster                   |
   +=====================================================================================+=======================================================================+=====================================================+
   | Importing data from an RDS for MySQL database to a CSS Elasticsearch cluster        | RDS for MySQL 5.5, 5.6, 5.7, or 8.0                                   | Elasticsearch 5.5, 6.2, 6.5, 7.1, 7.6, 7.9, or 7.10 |
   +-------------------------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------+
   | Importing data from a TaurusDB database to a CSS Elasticsearch cluster              | Primary/standby TaurusDB instances                                    | Elasticsearch 5.5, 6.2, 6.5, 7.1, 7.6, 7.9, or 7.10 |
   +-------------------------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------+
   | Importing data from an in-house built MySQL database to a CSS Elasticsearch cluster | MySQL database 5.5, 5.6, 5.7, or 8.0 created on a local server or ECS | Elasticsearch 5.5, 6.2, 6.5, 7.1, 7.6, 7.9, or 7.10 |
   +-------------------------------------------------------------------------------------+-----------------------------------------------------------------------+-----------------------------------------------------+
