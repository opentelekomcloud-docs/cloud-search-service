:original_name: en-us_topic_0000002098813645.html

.. _en-us_topic_0000002098813645:

Using Elasticsearch for Data Search
===================================

This section provides an example of how an e-commerce website uses a CSS Elasticsearch cluster to implement a product search function, including creating indexes, importing data, and searching for data.

Scenario Description
--------------------

A women's clothing brand runs an e-commerce website. It has been using traditional databases to power a product search function for customers. However, as the website traffic increases, these traditional databases are struggling to keep up, leading to slow responses and low search accuracy. To improve shopping experience for customers, the e-commerce website plans to use Cloud Search Service (CSS) to provide the product search function.

Assume that the e-commerce website has the following data:

.. code-block::

   {
   "products":[
   {"productName":"Latest elegant shirts in autumn 2017","size":"L"}
   {"productName":"Latest elegant shirts in autumn 2017","size":"M"}
   {"productName":"Latest elegant shirts in autumn 2017","size":"S"}
   {"productName":"Latest jeans in spring 2018","size":"M"}
   {"productName":"Latest jeans in spring 2018","size":"S"}
   {"productName":"Latest casual pants in spring 2017","size":"L"}
   {"productName":"Latest casual pants in spring 2017","size":"S"}
   ]
   }

Procedure
---------

The following describes how to use an Elasticsearch cluster to implement a website search function.

#. :ref:`Step 1: Creating a Cluster <en-us_topic_0000002098813645__en-us_topic_0000001995777894_en-us_topic_0000001223434400_section96881833619>`: Create a non-security mode Elasticsearch cluster for data search.
#. :ref:`Step 2: Importing Data <en-us_topic_0000002098813645__en-us_topic_0000001995777894_en-us_topic_0000001223434400_section398512163445>`: Use an open-source Elasticsearch API to import data on Kibana.
#. :ref:`Step 3: Searching for Data <en-us_topic_0000002098813645__en-us_topic_0000001995777894_en-us_topic_0000001223434400_section167624221443>`: Perform full-text search and result aggregation and display on data in the Elasticsearch cluster.
#. :ref:`Step 4: Deleting Indexes <en-us_topic_0000002098813645__en-us_topic_0000001995777894_section342432816441>`: Delete indexes that you no longer need to reclaim resources.

.. _en-us_topic_0000002098813645__en-us_topic_0000001995777894_en-us_topic_0000001223434400_section96881833619:

Step 1: Creating a Cluster
--------------------------

Create a non-security mode Elasticsearch cluster for data search.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters** > **Elasticsearch**.

#. Click **Create Cluster** in the upper right corner. The **Create Cluster** page is displayed.

#. Configure Billing Mode and AZ for the cluster.

   .. table:: **Table 1** Billing mode and AZ parameters

      +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Parameter             | Description                                                                                                                                                      | Example Value         |
      +=======================+==================================================================================================================================================================+=======================+
      | Region                | Select the region where the cluster is located.                                                                                                                  | xxx                   |
      |                       |                                                                                                                                                                  |                       |
      |                       | ECSs in different regions cannot communicate with each other over an intranet. For lower network latency and quicker resource access, select the nearest region. |                       |
      +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+
      | AZ                    | Select AZs associated with the cluster region. A maximum of three AZs can be configured.                                                                         | AZ 1                  |
      +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------+

#. Configure basic cluster information.


   .. figure:: /_static/images/en-us_image_0000001995777910.png
      :alt: **Figure 1** Configuring cluster information

      **Figure 1** Configuring cluster information

   .. table:: **Table 2** Basic configuration parameters

      +--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+
      | Parameter    | Description                                                                                                                                                  | Example Value    |
      +==============+==============================================================================================================================================================+==================+
      | Cluster Type | Select **Elasticsearch**.                                                                                                                                    | Elasticsearch    |
      +--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+
      | Version      | Select a cluster version from the drop-down list box.                                                                                                        | 7.10.2           |
      +--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+
      | Name         | Cluster name, which contains 4 to 32 characters. Only letters, numbers, hyphens (-), and underscores (_) are allowed and the value must start with a letter. | Sample-ESCluster |
      +--------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------+

#. Configure the cluster's node specifications.

   .. table:: **Table 3** Specification parameters

      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+
      | Parameter             | Description                                                                                                                 | Example Value |
      +=======================+=============================================================================================================================+===============+
      | Nodes                 | Set the number of nodes in the cluster. Select a number from 1 to 32.                                                       | 1             |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+
      | CPU Architecture      | The CPU architectures actually supported vary depending on the regional environment.                                        | x86           |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+
      | Node Specifications   | Select the specifications of cluster nodes.                                                                                 | css.medium.8  |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+
      | Node Storage Type     | Select the storage type of cluster nodes.                                                                                   | High I/O      |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+
      | Node Storage Capacity | Node storage capacity. Its value range varies with node specifications. The node storage capacity must be a multiple of 20. | 40GB          |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+
      | Master node           | The Master node manages all node tasks in the cluster.                                                                      | Unselect it.  |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+
      | Client node           | Client nodes receive and coordinate external requests, such as search and write requests.                                   | Unselect it.  |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+
      | Cold data node        | Cold data nodes are used to store data that is not particularly sensitive to query latency in large quantities.             | Unselect it.  |
      +-----------------------+-----------------------------------------------------------------------------------------------------------------------------+---------------+

#. Set the enterprise project.

   When creating a CSS cluster, you can bind an enterprise project to the cluster if you have enabled the enterprise project function. In this example, **default**, the default enterprise project, is selected.

#. Click **Next: Network** to configure the cluster network.


   .. figure:: /_static/images/en-us_image_0000002032217241.png
      :alt: **Figure 2** Configuring networking

      **Figure 2** Configuring networking

   .. table:: **Table 4** Network configuration parameters

      +-----------------------+------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Parameter             | Description                                                                                                      | Example Value         |
      +=======================+==================================================================================================================+=======================+
      | VPC                   | Specify a VPC to isolate the cluster's network.                                                                  | vpc-default           |
      |                       |                                                                                                                  |                       |
      |                       | .. note::                                                                                                        |                       |
      |                       |                                                                                                                  |                       |
      |                       |    The VPC must contain CIDRs. Otherwise, cluster creation will fail. By default, a VPC will contain CIDRs.      |                       |
      +-----------------------+------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Subnet                | A subnet provides dedicated network resources that are isolated from other networks, improving network security. | subnet-default        |
      +-----------------------+------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Security Group        | A security group serves as a virtual firewall that provides access control policies for clusters.                | default               |
      |                       |                                                                                                                  |                       |
      |                       | .. note::                                                                                                        |                       |
      |                       |                                                                                                                  |                       |
      |                       |    For enable cluster access, ensure that port 9200 is allowed by the security group.                            |                       |
      +-----------------------+------------------------------------------------------------------------------------------------------------------+-----------------------+
      | Security Mode         | After the security mode is enabled, communication will be encrypted and authentication required for the cluster. | Disable               |
      +-----------------------+------------------------------------------------------------------------------------------------------------------+-----------------------+

#. Click **Next: Advanced Settings**. Configure automatic snapshot creation and other functions.

   This cluster is used only for getting started. Cluster snapshots and advanced functions are not required.

#. Click **Next: Confirm**. Check the configuration and click **Next** to create a cluster.

#. Click **Back to Cluster List** to switch to the **Clusters** page. The cluster you created is now in the cluster list and its status is **Creating**. If the cluster is successfully created, its status changes to **Available**.


   .. figure:: /_static/images/en-us_image_0000001995618190.png
      :alt: **Figure 3** Creating a cluster

      **Figure 3** Creating a cluster

.. _en-us_topic_0000002098813645__en-us_topic_0000001995777894_en-us_topic_0000001223434400_section398512163445:

Step 2: Importing Data
----------------------

There are several ways to import data to an Elasticsearch cluster. In this example, we use an open-source Elasticsearch API to import data on Kibana.

#. On the Elasticsearch cluster management page, select the created **Sample-ESCluster** cluster and click **Access Kibana** in the **Operation** column to access the Kibana console.

#. In the Kibana navigation pane on the left, choose **Dev Tools**.

   The text box on the left is the input box. The triangle icon in the upper right corner of the input box is the command execution button. The text box on the right area is the result output box.


   .. figure:: /_static/images/en-us_image_0000001995777914.png
      :alt: **Figure 4** Console page

      **Figure 4** Console page

#. On the **Console** page, run the following command to create an index named **my_store**:

   .. code-block:: text

      PUT /my_store
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

   The command output is similar to the following:

   .. code-block::

      {
        "acknowledged" : true,
        "shards_acknowledged" : true,
        "index" : "my_store"
      }

#. On the **Console** page, run the following command to import data to the index named **my_store**:

   .. code-block:: text

      POST /my_store/_doc/_bulk
      {"index":{}}
      {"productName":"Latest elegant shirts in autumn 2017","size":"L"}
      {"index":{}}
      {"productName":"Latest elegant shirts in autumn 2017","size":"M"}
      {"index":{}}
      {"productName":"Latest elegant shirts in autumn 2017","size":"S"}
      {"index":{}}
      {"productName":"Latest jeans in spring 2018","size":"M"}
      {"index":{}}
      {"productName":"Latest jeans in spring 2018","size":"S"}
      {"index":{}}
      {"productName":"Latest casual pants in spring 2017","size":"L"}
      {"index":{}}
      {"productName":"Latest casual pants in spring 2017","size":"S"}

   If the value of the **errors** field in the command output is **false**, the data is imported successfully.

.. _en-us_topic_0000002098813645__en-us_topic_0000001995777894_en-us_topic_0000001223434400_section167624221443:

Step 3: Searching for Data
--------------------------

Perform full-text search and result aggregation and display on data in the Elasticsearch cluster.

-  **Full-text search**

   If you access the e-commerce website and want to search for items whose names include "spring jeans", enter "spring jeans" to begin your search.

   Run the following command on Kibana:

   .. code-block:: text

      GET /my_store/_search
      {
        "query": {"match": {
          "productName": "spring jeans"
        }}
      }

   The command output is similar to the following:

   .. code-block::

      {
        "took" : 3,
        "timed_out" : false,
        "_shards" : {
          "total" : 1,
          "successful" : 1,
          "skipped" : 0,
          "failed" : 0
        },
        "hits" : {
          "total" : {
            "value" : 4,
            "relation" : "eq"
          },
          "max_score" : 1.7965372,
          "hits" : [
            {
              "_index" : "my_store",
              "_type" : "_doc",
              "_id" : "9xf6VHIBfClt6SDjw7H5",
              "_score" : 1.7965372,
              "_source" : {
                "productName": "Latest jeans in spring 2018",
                "size" : "M"
              }
            },
            {
              "_index" : "my_store",
              "_type" : "_doc",
              "_id" : "-Bf6VHIBfClt6SDjw7H5",
              "_score" : 1.7965372,
              "_source" : {
                "productName": "Latest jeans in spring 2018",
                "size" : "S"
              }
            },
            {
              "_index" : "my_store",
              "_type" : "_doc",
              "_id" : "-Rf6VHIBfClt6SDjw7H5",
              "_score" : 0.5945667,
              "_source" : {
                "productName": "Latest casual pants in spring 2017",
                "size" : "L"
              }
            },
            {
              "_index" : "my_store",
              "_type" : "_doc",
              "_id" : "-hf6VHIBfClt6SDjw7H5",
              "_score" : 0.5945667,
              "_source" : {
                "productName": "Latest casual pants in spring 2017",
                "size" : "S"
              }
            }
          ]
        }
      }

   -  Elasticsearch supports IK word segmentation. The preceding command segments "spring jeans" into "spring" and "jeans".
   -  Elasticsearch supports full-text search. The preceding command searches for the information about all items whose names include "spring" or "jeans".
   -  Unlike traditional databases, Elasticsearch can return results in milliseconds by using inverted indexes.
   -  Elasticsearch supports sorting by score. In the command output, information about the first two items contains both "spring" and "jeans", while that about the last two items contain only "spring". Therefore, the first two items rank higher than the last two due to high keyword match.

-  **Aggregated result display**

   The e-commerce website displays aggregated results. For example, it classifies items corresponding to "spring" based on sizes so that you can count the number of items of different sizes.

   Run the following result aggregation command on Kibana:

   .. code-block:: text

      GET /my_store/_search
      {
      "query": {
      "match": { "productName": "spring" }
      },
      "size": 0,
      "aggs": {
      "sizes": {
      "terms": { "field": "size" }
      }
      }
      }

   The command output is similar to the following:

   .. code-block::

      {
        "took" : 3,
        "timed_out" : false,
        "_shards" : {
          "total" : 1,
          "successful" : 1,
          "skipped" : 0,
          "failed" : 0
        },
        "hits" : {
          "total" : {
            "value" : 4,
            "relation" : "eq"
          },
          "max_score" : null,
          "hits" : [ ]
        },
        "aggregations" : {
          "sizes" : {
            "doc_count_error_upper_bound" : 0,
            "sum_other_doc_count" : 0,
            "buckets" : [
              {
                "key" : "S",
                "doc_count" : 2
              },
              {
                "key" : "L",
                "doc_count" : 1
              },
              {
                "key" : "M",
                "doc_count" : 1
              }
            ]
          }
        }
      }

.. _en-us_topic_0000002098813645__en-us_topic_0000001995777894_section342432816441:

Step 4: Deleting Indexes
------------------------

If an index is no longer used, run the following command on Kibana to delete the index to reclaim resources:

.. code-block:: text

   DELETE /my_store

The command output is similar to the following:

.. code-block::

   {
     "acknowledged" : true
   }

Follow-up Operations
--------------------

You can delete the cluster if you no longer need it.

.. note::

   After you delete a cluster, its data cannot be restored. Exercise caution when deleting a cluster.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters** > **Elasticsearch**.
#. In the cluster list, locate the **Sample-ESCluster** cluster, and choose **More** > **Delete** in the **Operation** column.
#. In the confirmation dialog box, type in **DELETE**, and click **OK**.
