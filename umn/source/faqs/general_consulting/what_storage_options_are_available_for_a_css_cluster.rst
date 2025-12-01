:original_name: css_02_0008.html

.. _css_02_0008:

What Storage Options Are Available for a CSS Cluster?
=====================================================

CSS uses EVS and local disks to store your indexes. During cluster creation, you can specify the EVS disk type and specifications (the EVS disk size).

-  EVS disk types include common I/O, high I/O, ultra-high I/O, and extreme SSD.
-  The EVS disk size varies depending on the node specifications you selected during cluster creation.

During cluster creation, a certain number of EVS disks can be attached to each node (corresponding to an ECS). You can calculate the total storage capacity of a CSS cluster based on the sizes of EVS disks attached to different ECSs. The EVS disk size is determined by the node specifications you selected when creating the cluster.
