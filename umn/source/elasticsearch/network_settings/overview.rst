:original_name: css_01_0168.html

.. _css_01_0168:

Overview
========

This topic introduces the four networking modes supported by CSS Elasticsearch clusters. Choose the configuration that best suits your connectivity needs, for example, whether you require intra-VPC, cross-VPC, or public network access.

Comparing Different Networking Modes
------------------------------------

.. table:: **Table 1** Comparing different networking modes

   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+
   | Dimension              | **Private Network Access**                          | **Public Network Access**               | **Dedicated Load Balancer**                                               | **VPC Endpoint**                                |
   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+
   | Intra-VPC access       | Supported                                           | Supported                               | Supported                                                                 | Supported                                       |
   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+
   | Cross-VPC access       | VPC peering connections and cluster routes required | Supported (automatic traversal)         | VPC peering connections and cluster routes required                       | Supported (automatic traversal)                 |
   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+
   | Internet accessibility | No                                                  | Yes                                     | Depends on whether a public IP address is allocated to the load balancer. | No                                              |
   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+
   | Security               | VPC isolation                                       | Public network access control policy    | ELB access control policy                                                 | VPCEP access control policy                     |
   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+
   | Data transfer costs    | N/A                                                 | Public network bandwidth fees           | ELB resource fees                                                         | VPCEP resource fees                             |
   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+
   | Advantage              | Low latency, low cost, and high security            | All-domain Internet accessibility       | Powerful load balancing, two-way authentication via custom certificates   | Private connections, network topology decoupled |
   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+
   | When to Use            | Internal service systems on the cloud               | Ad hoc testing, public network services | High availability + load balancing                                        | Cross-account/Cross-VPC services                |
   +------------------------+-----------------------------------------------------+-----------------------------------------+---------------------------------------------------------------------------+-------------------------------------------------+

Choosing a Networking Mode
--------------------------

#. Do clients access our service from a public network environment?

   -  Yes: Use **Dedicated Load Balancer**, but the load balancers must be allocated public IP addresses.
   -  No: Go to :ref:`2 <en-us_topic_0000002527663056__li4932857192412>`.

#. .. _en-us_topic_0000002527663056__li4932857192412:

   Since the clients are on the internal network, do they share the same VPC as our cluster?

   -  Yes: This is intra-VPC access. Does our cluster need load balancers to enhance throughput and stability?

      -  Yes: Use **Dedicated Load Balancer**.
      -  No: Use **Private Network Access**.

   -  No: This is cross-VPC access. Do the VPCs have overlapping CIDR blocks?

      -  Yes: Use **VPC Endpoint**.
      -  No: Use **Dedicated Load Balancer**. VPC peering connections or cluster routes are required.
