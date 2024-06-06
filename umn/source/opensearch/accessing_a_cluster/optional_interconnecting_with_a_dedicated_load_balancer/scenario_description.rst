:original_name: en-us_topic_0000001640645481.html

.. _en-us_topic_0000001640645481:

Scenario Description
====================

CSS integrates shared load balancers and allows you to bind public network access and enable the VPC Endpoint service. Dedicated load balancers provide more functions and higher performance than shared load balancers. This section describes how to connect a cluster to a dedicated load balancer.

Advantages of connecting a cluster to a dedicated load balancer:

-  A non-security cluster can also use capabilities of the Elastic Load Balance (ELB) service.
-  You can use customized certificates for HTTPS bidirectional authentication.
-  Seven-layer traffic monitoring and alarm configuration are supported, allowing you to view the cluster status at any time.

There are eight service forms for clusters in different security modes to connect to dedicated load balancers. :ref:`Table 1 <en-us_topic_0000001640645481__en-us_topic_0000001477739400_en-us_topic_0000001463358273_table4446327845>` describes the ELB capabilities for the eight service forms. :ref:`Table 2 <en-us_topic_0000001640645481__en-us_topic_0000001477739400_en-us_topic_0000001463358273_table1537163912019>` describes the configurations for the eight service forms.

.. important::

   You are not advised connecting a load balancer that has been bound to a public IP address to a non-security cluster. Access from the public network using such a load balancer may bring security risks because non-security clusters can be accessed over HTTP without security authentication.

.. _en-us_topic_0000001640645481__en-us_topic_0000001477739400_en-us_topic_0000001463358273_table4446327845:

.. table:: **Table 1** ELB capabilities for different clusters

   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security Mode         | Service Form Provided by ELB for External Systems | ELB Load Balancing | ELB Traffic Monitoring | ELB Two-way Authentication |
   +=======================+===================================================+====================+========================+============================+
   | Non-security          | No authentication                                 | Supported          | Supported              | Not supported              |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   |                       | One-way authentication                            | Supported          | Supported              | Supported                  |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication                            |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security mode + HTTP  | Password authentication                           | Supported          | Supported              | Not supported              |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   |                       | One-way authentication + Password authentication  | Supported          | Supported              | Supported                  |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication + Password authentication  |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security mode + HTTPS | One-way authentication + Password authentication  | Supported          | Supported              | Supported                  |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication + Password authentication  |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+

.. _en-us_topic_0000001640645481__en-us_topic_0000001477739400_en-us_topic_0000001463358273_table1537163912019:

.. table:: **Table 2** Configuration for interconnecting different clusters with ELB

   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   | **Security Mode**     | **Service Form Provided by ELB for External Systems** | **ELB Listener**      |          |                        | **Backend Server Group** |                       |                               |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   |                       |                                                       | **Frontend Protocol** | **Port** | **SSL Parsing Mode**   | **Backend Protocol**     | **Health Check Port** | **Health Check Path**         |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   | Non-security          | No authentication                                     | HTTP                  | 9200     | No authentication      | HTTP                     | 9200                  | /                             |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   |                       | One-way authentication                                | HTTPS                 | 9200     | One-way authentication | HTTP                     | 9200                  |                               |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   |                       | Two-way authentication                                | HTTPS                 | 9200     | Two-way authentication | HTTP                     | 9200                  |                               |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   | Security mode + HTTP  | Password authentication                               | HTTP                  | 9200     | No authentication      | HTTP                     | 9200                  | /_opendistro/_security/health |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   |                       | One-way authentication + Password authentication      | HTTPS                 | 9200     | One-way authentication | HTTP                     | 9200                  |                               |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   |                       | Two-way authentication + Password authentication      | HTTPS                 | 9200     | Two-way authentication | HTTP                     | 9200                  |                               |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   | Security mode + HTTPS | One-way authentication + Password authentication      | HTTPS                 | 9200     | One-way authentication | HTTPS                    | 9200                  |                               |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
   |                       | Two-way authentication + Password authentication      | HTTPS                 | 9200     | Two-way authentication | HTTPS                    | 9200                  |                               |
   +-----------------------+-------------------------------------------------------+-----------------------+----------+------------------------+--------------------------+-----------------------+-------------------------------+
