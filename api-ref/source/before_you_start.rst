:original_name: css_03_0001.html

.. _css_03_0001:

Before You Start
================

Overview
--------

Welcome to *Cloud Search Service (CSS) API Reference*. CSS is a fully managed, distributed search service that enables you to perform quick, real-time search on both structured and unstructured data. It is fully compatible with open-source Elasticsearch and provides you search, statistical analysis, and reporting capabilities.

This document provides CSS API description, syntax, parameters, and examples. CSS provides APIs for cluster management and snapshot management. You can call these APIs to easily create, query, delete, restart, and scale clusters.

You can search for information you need according to :ref:`Table 1 <css_03_0001__en-us_topic_0171541464_table2042812316524>`.

.. _css_03_0001__en-us_topic_0171541464_table2042812316524:

.. table:: **Table 1** Overview

   +-------------------------+--------------------------------------------------------------------------------------+
   | Chapter                 | Description                                                                          |
   +=========================+======================================================================================+
   | API Overview            | An overview of the API and a list                                                    |
   +-------------------------+--------------------------------------------------------------------------------------+
   | Environment Preparation | Prerequisites for using the APIs.                                                    |
   +-------------------------+--------------------------------------------------------------------------------------+
   | API Calling             | Representational State Transfer (REST) message bodies, calling methods, and examples |
   +-------------------------+--------------------------------------------------------------------------------------+
   | APIs for each module    | APIs provided by CSS                                                                 |
   +-------------------------+--------------------------------------------------------------------------------------+
   | Common Parameters       | Common parameters, status codes, and error codes of CSS APIs                         |
   +-------------------------+--------------------------------------------------------------------------------------+

Supported versions
------------------

In CSS, Elasticsearch 7.6.2, 7.9.3, and 7.10.2 and Kibana 7.6.2, 7.9.3, and 7.10.2 are supported.

Restrictions and Limitations
----------------------------

-  For more constraints, see the API descriptions.

.. _css_03_0001__section889174472415:

Regions and Endpoints
---------------------

An endpoint is the **request address** for calling an API. Endpoints vary depending on services and regions. For more information, see `Regions and Endpoints <https://docs.otc.t-systems.com/en-us/endpoint/index.html>`__.

Concepts
--------

-  Account

   An account is created upon successful registration with the cloud system. The account has full access permissions for all of its cloud services and resources. It can be used to reset user passwords and grant user permissions. The account is a payment entity, which should not be used directly to perform routine management. For security purposes, create Identity and Access Management (IAM) users and grant them permissions for routine management.

-  User

   An IAM user is created under an account to use cloud services. Each user has its own identity credentials (password and access keys).

   API authentication requires information such as the account name, username, and password.

-  Region

   A region is a geographic area in which cloud resources are deployed. Availability zones (AZs) in the same region can communicate with each other over an intranet, while AZs in different regions are isolated from each other. By creating cloud resources in different regions, you can design applications to better meet customer requirements and comply with local laws and regulations.

-  AZ

   An AZ comprises of one or multiple physical data centers equipped with independent ventilation, fire, water, and electricity facilities. Computing, network, storage, and other resources in an AZ are logically divided into multiple clusters. AZs within a region are interconnected using high-speed optical fibers to allow you to build cross-AZ high-availability systems.

-  Project

   A project corresponds to a region. Default projects are defined to group and physically isolate resources (including compute, storage, and network resources) between different regions. Users can be granted permissions in a default project to access all resources under their accounts in the region associated with the project. If you need more refined access control, create sub-projects under a default project and purchase resources in sub-projects. Then you can assign users the permissions required to access only the resources in the specific sub-projects.


   .. figure:: /_static/images/en-us_image_0000002083557630.png
      :alt: **Figure 1** Isolation by project

      **Figure 1** Isolation by project

-  Checkpoint: When an application consumes data, the latest SN of the consumed data is recorded as a checkpoint. When the data is consumed again, the consumption can be continued based on this checkpoint.

-  APP: Multiple applications can access data in the same stream. Checkpoints generated for each application are used to record the consumed data in the stream by each application.
