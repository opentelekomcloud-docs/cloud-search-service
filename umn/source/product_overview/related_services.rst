:original_name: css_04_0004.html

.. _css_04_0004:

Related Services
================

:ref:`Figure 1 <en-us_topic_0000001981310425__fig1895417182444>` shows the relationships between CSS and other services.

.. _en-us_topic_0000001981310425__fig1895417182444:

.. figure:: /_static/images/en-us_image_0000001981470325.png
   :alt: **Figure 1** Relationships between CSS and other services

   **Figure 1** Relationships between CSS and other services

.. table:: **Table 1** Relationships between CSS and other services

   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Service Name                         | Relationship with CSS                                                                                                                                                                                                      |
   +======================================+============================================================================================================================================================================================================================+
   | Virtual Private Cloud (VPC)          | CSS clusters are created in the subnets of a VPC. VPCs provide secure, isolated logical network environments for your clusters.                                                                                            |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elastic Cloud Server (ECS)           | In a CSS cluster, each node is an ECS. When you create a cluster, ECSs are automatically created.                                                                                                                          |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elastic Volume Service (EVS)         | CSS can use EVS disks to store data. When you create a cluster, EVSs are automatically created for cluster data storage.                                                                                                   |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Object Storage Service (OBS)         | CSS cluster snapshots and log backups can be stored in OBS buckets.                                                                                                                                                        |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Identity and Access Management (IAM) | CSS uses IAM for user authentication.                                                                                                                                                                                      |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Cloud Eye (CES)                      | CSS uses Cloud Eye to monitor cluster metrics in real time to ensure service health.                                                                                                                                       |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Cloud Trace Service (CTS)            | With CTS, you can record, query, and audit all operations performed on your CSS clusters.                                                                                                                                  |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Key Management Service (KMS)         | If disk encryption is enabled for a CSS cluster, you need to obtain the key provided by KMS to encrypt and decrypt data stored on disks.                                                                                   |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Simple Message Notification (SMN)    | CSS uses SMN to provide one-to-multiple message subscription and notification via a variety of protocols. It automatically alerts users to cluster issues and sends diagnostic reports following an intelligent diagnosis. |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Elastic Load Balance (ELB)           | CSS uses dedicated load balancers to distribute requests to backend servers. This increases the system's overall capacity and throughput and improves fault tolerance.                                                     |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | VPC Endpoint (VPCEP)                 | VPCEP enables secure and reliable access across VPCs for CSS through a dedicated gateway.                                                                                                                                  |
   +--------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
