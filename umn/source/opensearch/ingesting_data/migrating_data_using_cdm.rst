:original_name: css_01_0089.html

.. _css_01_0089:

Migrating Data Using CDM
========================

Enterprises often operate heterogeneous platforms, with data distributed across traditional relational databases such as Oracle and storage systems like Object Storage Service (OBS). To enable high-performance full-text search and analytics, this data often needs to be migrated into OpenSearch. However, migrating large volumes of heterogeneous data using custom scripts is costly and often hindered by complex network configurations and low transfer efficiency. The Cloud Data Migration (CDM) service simplifies this process with a no-code, managed service that supports high concurrency and resumable transfers. Using CDM, you can quickly and securely migrate data from Oracle databases or OBS to CSS OpenSearch clusters.

.. table:: **Table 1** Ingesting data into CSS using CDM

   +-------------------------------------------------+----------------------------------------+---------------------+
   | Scenario                                        | Data Source                            | Destination Cluster |
   +=================================================+========================================+=====================+
   | Ingesting data from an Oracle database into CSS | A local or third-party Oracle database | OpenSearch 1.3.6    |
   +-------------------------------------------------+----------------------------------------+---------------------+
   | Ingesting data from OBS to CSS                  | JSON/CSV files in OBS buckets          | OpenSearch 1.3.6    |
   +-------------------------------------------------+----------------------------------------+---------------------+

Preparations
------------

#. Connect the network.

   -  Ensure the CDM cluster, CSS cluster, and OBS bucket reside in the same VPC. This enables data transmission over the internal network for optimal speed.
   -  If the source is an on-premises Oracle database, make sure CDM can access it through a VPN, Direct Connect, or public IP address.

#. Obtain connection information

   -  Obtain the private network address (for example, **192.168.xxx.xxx:9200**), username, and password of the CSS cluster. (The username and password are required only for a security-mode cluster.)
   -  If the source is an Oracle database, you need to obtain the database's IP address, port, database name, username, and password.
   -  If the source is OBS, obtain the OBS bucket name, domain name, port, AK, and SK.

Migrating Data
--------------

#. Log in to OpenSearch Dashboards and go to the command execution page.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.

   c. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. (Optional) Create the destination index in the OpenSearch cluster. CDM can automatically create destination indexes. However, to ensure optimal query performance, you are advised to define the index mappings in the destination OpenSearch cluster in advance.

   For example, run the following command to create index **demo**:

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

   The command is successfully executed if the following information is displayed.

   .. code-block::

      {
        "acknowledged" : true,
        "shards_acknowledged" : true,
        "index" : "demo"
      }

#. Ingest data from Oracle or OBS to the OpenSearch cluster using CDM.

   -  If the data source is an Oracle database, see section "Migrating Data from Oracle to CSS" in the *Cloud Data Migration User Guide* for an operation guide.
   -  If the data source is OBS, see "Migrating Data from OBS to CSS" in the *Cloud Data Migration User Guide* for an operation guide.

   .. note::

      If the data source is MySQL, see "Creating a MySQL Connector" in the *Cloud Data Migration User Guide* for how to connect to a MySQL database.

#. After the migration is complete, verify data integrity.

   a. Log in to the OpenSearch cluster via OpenSearch Dashboards, and navigate to the **Dev Tools** page.

   b. Run the following command to check the newly ingested data:

      .. code-block:: text

         GET demo/_count         # Check the number of records ingested.
         GET demo/_search        # Check the content of the ingested data.

      If the results are consistent with the source, data ingestion is successful.
