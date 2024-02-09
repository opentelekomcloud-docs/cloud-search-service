:original_name: css_01_0181.html

.. _css_01_0181:

Scenario
========

CSS integrates shared load balancers and allows you to bind public network access and enable the VPC Endpoint service. Dedicated load balancers provide more functions and higher performance than shared load balancers. This section describes how to connect a cluster to a dedicated load balancer.

Advantages of connecting a cluster to a dedicated load balancer:

-  A non-security cluster can also use capabilities of the Elastic Load Balance (ELB) service.
-  You can use customized certificates for HTTPS bidirectional authentication.
-  Seven-layer traffic monitoring and alarm configuration are supported, allowing you to view the cluster status at any time.

There are eight service forms for clusters in different security modes to connect to dedicated load balancers. :ref:`Table 1 <css_01_0181__en-us_topic_0000001463358273_table4446327845>` describes the load balancer capabilities for the eight service forms. :ref:`Table 2 <css_01_0181__en-us_topic_0000001463358273_table1537163912019>` describes the configurations for the eight service forms.

.. important::

   You are not advised to connect an ELB that has bound the public network to a non-security cluster. Non-security clusters can be accessed over HTTP without security authentication. A load balancer with an EIP allows access to such clusters over the Internet, which may bring security risks.

.. _css_01_0181__en-us_topic_0000001463358273_table4446327845:

.. table:: **Table 1** ELB capabilities for different clusters

   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security Mode         | Service Form Provided by ELB for External Systems | ELB Load Balancing | ELB Traffic Monitoring | ELB Two-way Authentication |
   +=======================+===================================================+====================+========================+============================+
   | Non-security          | No authentication                                 | Yes                | Yes                    | No                         |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   |                       | One-way authentication                            | Yes                | Yes                    | Yes                        |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication                            |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security mode + HTTP  | Password authentication                           | Yes                | Yes                    | No                         |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   |                       | One-way authentication + Password authentication  | Yes                | Yes                    | Yes                        |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication + Password authentication  |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+
   | Security mode + HTTPS | One-way authentication + Password authentication  | Yes                | Yes                    | Yes                        |
   |                       |                                                   |                    |                        |                            |
   |                       | Two-way authentication + Password authentication  |                    |                        |                            |
   +-----------------------+---------------------------------------------------+--------------------+------------------------+----------------------------+

.. _css_01_0181__en-us_topic_0000001463358273_table1537163912019:

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
