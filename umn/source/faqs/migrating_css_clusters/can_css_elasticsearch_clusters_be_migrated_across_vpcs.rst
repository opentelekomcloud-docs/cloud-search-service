:original_name: css_02_0058.html

.. _css_02_0058:

Can CSS Elasticsearch Clusters Be Migrated Across VPCs?
=======================================================

Use either of the following methods to migrate Elasticsearch clusters across different VPCs:

Method 1
--------

Use the backup and restoration function to migrate cluster data.

Method 2
--------

#. Connect the VPC network and establish a VPC peering connection.
#. After the network is connected, use Logstash to migrate data.
