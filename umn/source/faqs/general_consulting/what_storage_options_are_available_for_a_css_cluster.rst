:original_name: css_02_0008.html

.. _css_02_0008:

What Storage Options Are Available for a CSS Cluster?
=====================================================

CSS uses EVS and local disks to store your indices. During cluster creation, you can specify the EVS disk type and specifications (the EVS disk size).

-  EVS disk types include common I/O, high I/O, and ultra-high I/O.
-  The EVS disk size varies depending on the node specifications you selected when creating a cluster.

You can configure up to 200 nodes for a cluster (each node is an ECS). The maximum storage capacity of an ECS is the total capacity of EVS disks attached to the ECS. You can calculate the total storage capacity of a CSS cluster based on the sizes of EVS disks attached to different ECSs. The EVS disk size is determined by the node specifications you selected when creating the cluster.
