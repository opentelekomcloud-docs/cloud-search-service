:original_name: css_04_0005.html

.. _css_04_0005:

Constraints
===========

This topic describes limits on the node quantity and resource quotas of a CSS cluster. For details about the limits and constraints of different features provided by CSS, see relevant topics in the CSS User Guide.

Maximum and Minimum Numbers of Nodes in a Cluster
-------------------------------------------------

The following tables provide the maximum and minimum numbers of nodes each CSS cluster can have.

.. table:: **Table 1** Maximum and minimum numbers of nodes in an Elasticsearch or OpenSearch cluster

   +-----------------------------------+-------------------------------------+
   | Node Type                         | Limit                               |
   +===================================+=====================================+
   | Data nodes                        | Mandatory node type.                |
   |                                   |                                     |
   |                                   | -  Max:                             |
   |                                   |                                     |
   |                                   |    -  200 with master nodes         |
   |                                   |    -  32 without master nodes       |
   |                                   |                                     |
   |                                   | -  Min: 1                           |
   +-----------------------------------+-------------------------------------+
   | Master nodes                      | Optional node type.                 |
   |                                   |                                     |
   |                                   | -  Max: 9                           |
   |                                   | -  Min: 3                           |
   |                                   |                                     |
   |                                   | The quantity must be an odd number. |
   +-----------------------------------+-------------------------------------+
   | Client nodes                      | Optional node type.                 |
   |                                   |                                     |
   |                                   | -  Max: 64                          |
   |                                   | -  Min: 1                           |
   +-----------------------------------+-------------------------------------+
   | Cold data nodes                   | Optional node type.                 |
   |                                   |                                     |
   |                                   | -  Max: 32                          |
   |                                   | -  Min: 1                           |
   +-----------------------------------+-------------------------------------+

Quotas
------

CSS uses the following resource quotas:

-  Number of instances
-  CPUs
-  Memory capacity in GB
-  Number of disks
-  Disk size (GB)
