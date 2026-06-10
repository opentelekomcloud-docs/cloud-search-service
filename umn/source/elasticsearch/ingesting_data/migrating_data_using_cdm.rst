:original_name: css_01_0046.html

.. _css_01_0046:

Migrating Data Using CDM
========================

Enterprises often operate heterogeneous platforms, with data distributed across traditional relational databases such as Oracle and storage systems like Object Storage Service (OBS). To enable high-performance full-text search and analytics, this data often needs to be migrated into Elasticsearch. However, migrating large volumes of heterogeneous data using custom scripts is costly and often hindered by complex network configurations and low transfer efficiency. The Cloud Data Migration (CDM) service simplifies this process with a no-code, managed service that supports high concurrency and resumable transfers. Using CDM, you can quickly and securely migrate data from Oracle databases or OBS to CSS Elasticsearch clusters.

.. table:: **Table 1** Ingesting data into CSS using CDM

   +-------------------------------------------------+----------------------------------------+-----------------------------------------------------+
   | Scenario                                        | Source Data                            | Target Cluster                                      |
   +=================================================+========================================+=====================================================+
   | Ingesting data from an Oracle database into CSS | A local or third-party Oracle database | Elasticsearch 5.5, 6.2, 6.5, 7.1, 7.6, 7.9, or 7.10 |
   +-------------------------------------------------+----------------------------------------+-----------------------------------------------------+
   | Ingesting data from OBS to CSS                  | JSON/CSV files in OBS buckets          | Elasticsearch 5.5, 6.2, 6.5, 7.1, 7.6, 7.9, or 7.10 |
   +-------------------------------------------------+----------------------------------------+-----------------------------------------------------+

Preparations
------------

#. Connect the network.

   -  Ensure the CDM cluster, CSS cluster, and OBS bucket reside in the same VPC. This enables data transmission over the internal network for optimal speed.
   -  If the source is an on-premises Oracle database, make sure CDM can access it through a VPN, Direct Connect, or public IP address.

#. Obtain connection information

   -  Obtain the private network address (for example, **192.168.xxx.xxx:9200**), username, and password of the CSS cluster. (The username and password are required only for a security-mode cluster.)
   -  If the source is an Oracle database, obtain the database's IP address, port, database name, username, and password.
   -  If the source is OBS, obtain the OBS bucket name, domain name, port, AK, and SK.

Migrating Data
--------------

#. Log in to Kibana and go to the command execution page.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. (Optional) Create the destination index in an Elasticsearch cluster. CDM can automatically create destination indexes. However, to ensure optimal query performance, you are advised to define the index mappings in the destination Elasticsearch cluster in advance.

   For example, run the following command to create index **demo**:

   -  For Elasticsearch 7.x or later:

      .. code-block:: text

         PUT /demo
         {
           "settings": {
             "number_of_shards": 1
           },
           "mappings": {
               "properties": {
                 "productName": {
                   "type": "text",
                   "analyzer": "ik_smart"
                 },
                 "size": {
                   "type": "keyword"
                 }
               }
             }
           }

   -  For Elasticsearch earlier than 7.x:

      .. code-block:: text

         PUT /demo
         {
           "settings": {
             "number_of_shards": 1
           },
           "mappings": {
             "products": {
               "properties": {
                 "productName": {
                   "type": "text",
                   "analyzer": "ik_smart"
                 },
                 "size": {
                   "type": "keyword"
                 }
               }
             }
           }
         }

   The command is successfully executed if the following information is displayed.

   .. code-block::

      {
        "acknowledged" : true,
        "shards_acknowledged" : true,
        "index" : "demo"
      }

#. Ingest data from Oracle or OBS to the Elasticsearch cluster using CDM.

   -  If the data source is an Oracle database, see section "Migrating Data from Oracle to CSS" in the *Cloud Data Migration User Guide* for an operation guide.
   -  If the data source is OBS, see "Migrating Data from OBS to CSS" in the *Cloud Data Migration User Guide* for an operation guide.

   .. note::

      If the data source is MySQL, see "Creating a MySQL Connector" in the *Cloud Data Migration User Guide* for how to connect to a MySQL database.

#. After the migration is complete, verify data integrity.

   a. Log in to the Elasticsearch cluster via Kibana, and navigate to the **Dev Tools** page.

   b. Run the following command to check the newly ingested data:

      .. code-block:: text

         GET demo/_count         # Check the number of records ingested.
         GET demo/_search        # Check the content of the ingested data.

      If the results are consistent with the source, data ingestion is successful.
