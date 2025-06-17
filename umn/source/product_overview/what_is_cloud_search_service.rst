:original_name: css_04_0001.html

.. _css_04_0001:

What Is Cloud Search Service?
=============================

CSS
---

CSS is a fully managed, distributed search service based on open source Elasticsearch and OpenSearch. You can use it for structured and unstructured data search, and enable vector-based composite search, statistics generation, and reporting. CSS is a fully hosted cloud service of the ELK Stack and is compatible with open-source Elasticsearch, Logstash, Kibana, and Cerebro.

-  Elasticsearch and OpenSearch

   Elasticsearch and OpenSearch are open-source distributed search engines that can be deployed in standalone or cluster mode. As the heart of the ELK Stack, Elasticsearch clusters support multi-condition search, statistical analysis, and create visualized reports of structured and unstructured text. For details about Elasticsearch, see the `Elasticsearch: The Definitive Guide <https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html>`__. For details about the OpenSearch search engine, see `OpenSearch Documentation <https://opensearch.org/docs/latest/>`__.

   CSS enables automatic deployment, allowing you to quickly provision Elasticsearch and OpenSearch clusters with zero O&M burdens. It offers built-in search engine optimization, helping to easily achieve optimal search performance. Additionally, its robust monitoring system tracks key metrics—such as cluster health and query performance—so you can manage your clusters effortlessly.

   Elasticsearch and OpenSearch clusters created in CSS can be accessed through Kibana, OpenSearch Dashboards, and Cerebro. For in-depth analysis and visualization of data, choose Kibana, as it provides rich visualization features and powerful analytical capabilities. For cluster management and monitoring, choose Cerebro, as it provides intuitive cluster status views and convenient management functions.

-  Logstash

   Logstash is an open-source data processing pipeline that ingests data from a multitude of sources, transforms it, and then sends it to your desired destination.

   CSS Logstash is a fully managed data ingestion and processing service that is completely compatible with open-source Logstash. You can quickly create Logstash clusters in CSS. Data is scattered across many different systems in different formats. CSS Logstash helps you get insights by easily processing data from a variety of data sources and dumping it to CSS's Elasticsearch clusters or other systems.

Introduction Video
------------------

Functions
---------

-  Open-source compatibility

   Freely use native Elasticsearch and OpenSearch APIs and other software in the ecosystem, such as Logstash, Beats, and Kibana.

-  Support for a variety of data sources

   A few simple configurations allow you to smoothly connect to multiple data sources, such as FTP, OBS, HBase, and Kafka. No extra coding is required.

-  One-click operation

   One-click cluster application, capacity expansion, and restart from small-scale testing to large-scale rollout

-  User-defined snapshot policies

   Trigger backup snapshots manually or configure an automated schedule.
