:original_name: en-us_topic_0000001527937341.html

.. _en-us_topic_0000001527937341:

Can Elasticsearch Data Be Migrated Between VPCs?
================================================

Elasticsearch does not support direct data migration between different VPCs. You can use either of the following methods to migrate data.

Method 1
--------

Use the backup and restoration function to migrate cluster data.

Method 2
--------

#. Connect the VPC network and establish a VPC peering connection.
#. After the network is connected, use Logstash to migrate data.
