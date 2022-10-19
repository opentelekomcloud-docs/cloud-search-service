:original_name: css_04_0004.html

.. _css_04_0004:

Related Services
================

This section describes the relationship between CSS and other services.

-  Virtual Private Cloud (VPC)

   CSS clusters are created in the subnets of a VPC. VPCs provide a secure, isolated, and logical network environment for your clusters.

-  Elastic Cloud Server (ECS)

   In a CSS cluster, each node represents an ECS. When you create a cluster, ECSs are automatically created.

-  Elastic Volume Service (EVS)

   CSS uses EVS to store index data. When you create a cluster, EVSs are automatically created for cluster data storage.

-  Object Storage Service (OBS)

   Snapshots of CSS clusters are stored in OBS buckets.

-  Identity and Access Management (IAM)

   IAM authenticates access to CSS.

-  Cloud Eye

   CSS uses Cloud Eye to monitor cluster metrics in real time. The supported CSS metrics include the disk usage and cluster health status. You can learn about the disk usage of the cluster based on the disk usage metric. You can learn about the health status of a cluster based on the cluster health status metric.

-  Cloud Trace Service (CTS)

   With CTS, you can record operations associated with CSS for query, audit, and backtrack operations.

-  Key Management Service (KMS)

   If disk encryption is enabled on CSS clusters, you need to obtain the key provided by KMS to encrypt and decrypt the disk data.
