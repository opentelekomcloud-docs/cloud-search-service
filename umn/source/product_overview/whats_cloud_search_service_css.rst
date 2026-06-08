:original_name: css_04_0001.html

.. _css_04_0001:

What's Cloud Search Service (CSS)?
==================================

About CSS
---------

Cloud Search Service (CSS) is a suite of fully managed search and analytics solutions from Cloud Service, built on the ELK stack (Elasticsearch, Logstash, Kibana) and OpenSearch. Designed for scalability and performance, CSS enables flexible search and analytical capabilities across both structured and unstructured data. It supports advanced features such as vector-based multi-condition search, statistical analysis, and customizable reporting. Fully compatible with open-source tools including Elasticsearch, OpenSearch, Logstash, OpenSearch Dashboards, Cerebro and Kibana, CSS supports automated deployment and quick cluster creation. It is easy to use, O&M-free, and offers a comprehensive monitoring system, allowing you to concentrate on core business applications, such as log analytics, intelligent customer service, knowledge base Q&A, and personalized product recommendations, without the burden of managing infrastructure or any technical complexity.

-  **Elasticsearch**

   CSS offers is a fully managed, distributed search engine built on open-source Elasticsearch. CSS Elasticsearch supports multi-condition search, statistical analysis, and reporting on both structured and unstructured data. While fully compatible with the native ELK (Elasticsearch, Logstash, Kibana) stack and toolchain, CSS features an enhanced kernel for superior performance. It is ideally suited for log analytics, enterprise search, and real-time data visualization, particularly where a robust analytics ecosystem and strong community support are required. For a deeper understanding of Elasticsearch, see `Elasticsearch: The Definitive Guide <https://www.elastic.co/guide/en/elasticsearch/guide/current/index.html>`__.

-  **OpenSearch**

   CSS offers a fully managed, distributed search engine built on open-source OpenSearch. As the future version of CSS Elasticsearch, CSS OpenSearch inherits its core capabilities while continuously evolving to support new features. CSS OpenSearch features an enhanced kernel and remains fully compatible with the native OpenSearch toolchain, guaranteeing access to the latest innovations in the ecosystem. It is the ideal choice for customers who require elastic scalability, continuous feature iteration, and long-term technology evolution. For a deeper understanding of OpenSearch, see `OpenSearch Documentation <https://opensearch.org/docs/latest/>`__.

-  **Vector database**

   CSS vector database is a high-performance vector search service. With a proprietary vector search engine, it delivers industry-leading performance in searching through hundreds of billions of vectorized records. The CSS vector database enables high-performance, high-accuracy nearest neighbor or approximate nearest neighbor search over unstructured data, such as images, video, and language corpuses. Typical use cases include image search, video search, similar item recommendations on e-commerce platforms, semantic search, and cross-modal search (for example, searching for images using text).

-  **Kibana**

   Kibana is the official data visualization and exploration platform for Elasticsearch. It enables in-depth data analysis and interactive visualization. In CSS, Kibana is pre-built for each Elasticsearch cluster. You can start Kibana in one click, without installing anything. Kibana offers a comprehensive suite of dashboard features and visualization tools. It seamlessly integrates Elasticsearch's analytical capabilities, supporting the full analytics process from data exploration to actionable business insights.

-  **OpenSearch Dashboards**

   OpenSearch Dashboards is the data visualization and exploration platform for OpenSearch. It enables in-depth data analysis and interactive visualization. In CSS, OpenSearch Dashboards is pre-built for each OpenSearch cluster. You can start OpenSearch Dashboards with one click, without installing anything. OpenSearch Dashboards offers a comprehensive suite of dashboard features and visualization tools. It seamlessly integrates OpenSearch's analytical capabilities, supporting the full analytics process from data exploration to actionable business insights.

-  **Cerebro**

   Cerebro is an open-source Elasticsearch/OpenSearch web admin tool, designed for real-time monitoring and efficient cluster operations. In CSS, Cerebro is pre-built for each Elasticsearch and OpenSearch cluster. You can start Cerebro with one click, without installing anything. Cerebro allows you to quickly check a cluster's health status, node distribution, and index details. For routine O&M tasks, including shard adjustment, index management, and performance monitoring, we recommend using Cerebro. Its intuitive cluster topology views and comprehensive management features streamline O&M workflows, reducing complexity while improving efficiency. Cerebro is suitable for different roles, including developers, O&M teams, and data analysts.

Advantages
----------

-  Robust ecosystem compatibility

   CSS offers full compatibility with both Elasticsearch and OpenSearch ecosystems, supporting their native APIs for seamless integration and migration.

-  Seamless multi-source data ingestion

   CSS can seamlessly ingest data from diverse data sources, such as FTP, OBS, HBase, and Kafka.

-  Auto scaling

   CSS provides on-demand, scalable resources to meet changing demands while ensuring service continuity.

-  Backup and restoration

   CSS supports automatic snapshot creation for data durability. You can back up and restore snapshots to the current or other clusters as needed.

For more information, see :ref:`Features <css_04_0003>`.

Architecture
------------

:ref:`Figure 1 <en-us_topic_0000001981470313__fig1689810315118>` shows the CSS product architecture. CSS integrates three search engines: Elasticsearch, OpenSearch, and vector databases. With an enhanced kernel and enhanced management capabilities, it delivers an enterprise search service featuring high performance, high availability, and high cost-effectiveness.

.. _en-us_topic_0000001981470313__fig1689810315118:

.. figure:: /_static/images/en-us_image_0000002473930140.png
   :alt: **Figure 1** CSS product architecture

   **Figure 1** CSS product architecture

Access Methods
--------------

Cloud Service provides a web-based service management console. You can work with CSS in either of the following ways:

-  Using APIs

   If you need to integrate CSS into a third-party system for secondary development, you can use APIs to access CSS clusters. For details, see *Cloud Search Service API Reference*.

-  Web-based console

   If no secondary development is involved, the CSS management console is a convenient way to access CSS. If you have registered with Cloud Service, log in to the management console and search for **Cloud Search Service** in the service list.

Getting Started with CSS
------------------------

-  :ref:`Using Elasticsearch for Data Search <index>`
