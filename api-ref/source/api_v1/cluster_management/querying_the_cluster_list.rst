:original_name: ListClustersDetails.html

.. _ListClustersDetails:

Querying the Cluster List
=========================

Function
--------

This API is used to query the cluster list and cluster status, including cluster nodes, Kibana public network access information, public network IP address, and IPv4 address and port number for private network access. After a cluster is created, check the cluster information and update the cluster in a timely manner.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID of the account.                                                                                                       |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================================================+
   | offset          | No              | Integer         | **Definition**:                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | The start value of the query.                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | 1-1000                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | The default value is 1, indicating that the query starts from the first cluster.                                                                                                     |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | **Definition**:                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | Number of clusters to be queried.                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | 1-1000                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | The default value is 10, indicating that 10 clusters are queried at a time.                                                                                                          |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | datastoreType   | No              | String          | **Definition**:                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | Cluster engine type.                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | -  elasticsearch: Provides distributed search capabilities, log analytics, reporting, and semantic search based on open-source Elasticsearch.                                        |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | -  logstash: Provides functions such as data ingestion, transformation, cleaning, and parsing based on open-source Logstash.                                                         |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | -  opensearch: Provides distributed search, log analytics, reporting, and semantic search based on open-source OpenSearch. It is the future version of CSS's Elasticsearch clusters. |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | -  When this parameter is left blank, all types of clusters are queried.                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                      |
   |                 |                 |                 | The default value is empty.                                                                                                                                                          |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                                                                            | Description                                                                                                                                                       |
   +=======================+=================================================================================+===================================================================================================================================================================+
   | totalSize             | Integer                                                                         | **Definition**:                                                                                                                                                   |
   |                       |                                                                                 |                                                                                                                                                                   |
   |                       |                                                                                 | Number of clusters. If datastoreType is specified, the number of clusters of the specified type is displayed. Otherwise, the number of all clusters is displayed. |
   |                       |                                                                                 |                                                                                                                                                                   |
   |                       |                                                                                 | **Value range**:                                                                                                                                                  |
   |                       |                                                                                 |                                                                                                                                                                   |
   |                       |                                                                                 | N/A                                                                                                                                                               |
   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | clusters              | Array of :ref:`ClusterList <listclustersdetails__response_clusterlist>` objects | **Definition**:                                                                                                                                                   |
   |                       |                                                                                 |                                                                                                                                                                   |
   |                       |                                                                                 | Cluster object list.                                                                                                                                              |
   |                       |                                                                                 |                                                                                                                                                                   |
   |                       |                                                                                 | **Value range**:                                                                                                                                                  |
   |                       |                                                                                 |                                                                                                                                                                   |
   |                       |                                                                                 | N/A                                                                                                                                                               |
   +-----------------------+---------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _listclustersdetails__response_clusterlist:

.. table:: **Table 4** ClusterList

   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                                                                                              | Description                                                                                                                                                                                                                         |
   +=======================+===================================================================================================+=====================================================================================================================================================================================================================================+
   | datastore             | :ref:`ClusterListDatastore <listclustersdetails__response_clusterlistdatastore>` object           | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster data search engine type.                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | snapshotPolicy        | :ref:`SnapshotPolicyResp <listclustersdetails__response_snapshotpolicyresp>` object               | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Information about an automatic snapshot creation policy.                                                                                                                                                                            |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | instances             | Array of :ref:`ClusterListInstances <listclustersdetails__response_clusterlistinstances>` objects | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster node list.                                                                                                                                                                                                                  |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | publicKibanaResp      | :ref:`publicKibanaRespBody <listclustersdetails__response_publickibanarespbody>` object           | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Kibana public network access information.                                                                                                                                                                                           |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | elbWhiteList          | :ref:`elbWhiteListResp <listclustersdetails__response_elbwhitelistresp>` object                   | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Public network access control information.                                                                                                                                                                                          |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | updated               | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Time when the cluster was last modified.                                                                                                                                                                                            |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | The format is CCYY-MM-DDThh:mm:ss (ISO 8601).                                                                                                                                                                                       |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | name                  | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster name.                                                                                                                                                                                                                       |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | publicIp              | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Public IP address information.                                                                                                                                                                                                      |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | created               | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster creation time. The returned cluster list is sorted by creation time in descending order. The latest cluster is displayed at the top.                                                                                        |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | The format is CCYY-MM-DDThh:mm:ss (ISO 8601).                                                                                                                                                                                       |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | id                    | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster ID.                                                                                                                                                                                                                         |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | status                | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster status.                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  **100**: creating                                                                                                                                                                                                                |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  **200**: available                                                                                                                                                                                                               |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  **300**: unavailable                                                                                                                                                                                                             |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  **303**: creation failed                                                                                                                                                                                                         |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | endpoint              | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | IPv4 address and port number accessed from the cluster's private network. [If the cluster type is KooSearch, this field indicates the internal address and port number for accessing the knowledge management service.] (tag:white) |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | vpcId                 | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | VPC ID.                                                                                                                                                                                                                             |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | subnetId              | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Current subnet of a cluster. The subnet is used for adding nodes, including scaling, adding dedicated master/client nodes, and enabling VPC Endpoint. IP addresses will be allocated to newly added nodes from the new subnet.      |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | securityGroupId       | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Security group ID.                                                                                                                                                                                                                  |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | bandwidthSize         | Integer                                                                                           | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Public network bandwidth. Unit (Mbit/s).                                                                                                                                                                                            |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | httpsEnable           | Boolean                                                                                           | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Whether HTTPS access is enabled.                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  false: HTTPS access is disabled.                                                                                                                                                                                                 |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  true: HTTPS access is enabled.                                                                                                                                                                                                   |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | authorityEnable       | Boolean                                                                                           | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Whether to enable security mode-based authentication for the cluster.                                                                                                                                                               |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  true: Enable security mode-based authentication.                                                                                                                                                                                 |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  false: Disable security mode-based authentication.                                                                                                                                                                               |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | diskEncrypted         | Boolean                                                                                           | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Whether disk encryption is enabled. To enable it, submit a service ticket.                                                                                                                                                          |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  **true**: Disks are encrypted.                                                                                                                                                                                                   |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  **false**: Disk are not encrypted.                                                                                                                                                                                               |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | backupAvailable       | Boolean                                                                                           | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Whether to enable cluster snapshots.                                                                                                                                                                                                |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  true: Cluster snapshots are enabled.                                                                                                                                                                                             |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  false: Cluster snapshots are disabled.                                                                                                                                                                                           |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | actionProgress        | Object                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster behavior progress, which shows the progress of cluster creation and scaling in percentage. **CREATING** indicates the progress of creation.                                                                                 |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | actions               | Array of strings                                                                                  | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Current behavior of a cluster.                                                                                                                                                                                                      |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  REBOOTING                                                                                                                                                                                                                        |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  GROWING                                                                                                                                                                                                                          |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  RESTORING: The cluster is being restored.                                                                                                                                                                                        |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | -  SNAPSHOTTING: A snapshot is being created.                                                                                                                                                                                       |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | enterpriseProjectId   | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | ID of the enterprise project that a cluster belongs.                                                                                                                                                                                |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | If the user of the cluster has not enabled the enterprise project, the setting of this parameter is not returned.                                                                                                                   |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | tags                  | Array of :ref:`ClusterListTags <listclustersdetails__response_clusterlisttags>` objects           | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster tags.                                                                                                                                                                                                                       |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | failedReason          | :ref:`ClusterListFailedReasons <listclustersdetails__response_clusterlistfailedreasons>` object   | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster failure cause. If the cluster status is available, this parameter is not returned.                                                                                                                                          |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | bandwidthResourceId   | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | ID of the Elasticsearch resource accessible from the public network.                                                                                                                                                                |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | ipv6Endpoint          | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | IPv6 address and port number accessed from the cluster's private network.                                                                                                                                                           |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cmkId                 | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Encryption key ID used by the current cluster.                                                                                                                                                                                      |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | currentSubnetIds      | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Subnets used by all nodes in the cluster. If there are multiple subnets (two at most), separate them with a comma (,).                                                                                                              |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | desc                  | String                                                                                            | **Definition**:                                                                                                                                                                                                                     |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | Cluster description.                                                                                                                                                                                                                |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Constraints**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | The value can contain up to 128 characters. display_name and desc cannot be null at the same time.                                                                                                                                  |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Value range**:                                                                                                                                                                                                                    |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | **Default value**:                                                                                                                                                                                                                  |
   |                       |                                                                                                   |                                                                                                                                                                                                                                     |
   |                       |                                                                                                   | N/A                                                                                                                                                                                                                                 |
   +-----------------------+---------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _listclustersdetails__response_clusterlistdatastore:

.. table:: **Table 5** ClusterListDatastore

   +-----------------------+-----------------------+-----------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                       |
   +=======================+=======================+===================================================================================+
   | type                  | String                | **Definition**:                                                                   |
   |                       |                       |                                                                                   |
   |                       |                       | Cluster engine type.                                                              |
   |                       |                       |                                                                                   |
   |                       |                       | **Value range**:                                                                  |
   |                       |                       |                                                                                   |
   |                       |                       | -  elasticsearch: Elasticsearch cluster.                                          |
   |                       |                       |                                                                                   |
   |                       |                       | -  logstash: Logstash cluster.                                                    |
   |                       |                       |                                                                                   |
   |                       |                       | -  opensearch: OpenSearch cluster.                                                |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------+
   | version               | String                | **Definition**:                                                                   |
   |                       |                       |                                                                                   |
   |                       |                       | Cluster engine version.                                                           |
   |                       |                       |                                                                                   |
   |                       |                       | **Value range**:                                                                  |
   |                       |                       |                                                                                   |
   |                       |                       | For details, see the supported versions in :ref:`Before You Start <css_03_0001>`. |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------+
   | supportSecuritymode   | Boolean               | **Definition**:                                                                   |
   |                       |                       |                                                                                   |
   |                       |                       | Whether the cluster supports the security mode.                                   |
   |                       |                       |                                                                                   |
   |                       |                       | **Value range**:                                                                  |
   |                       |                       |                                                                                   |
   |                       |                       | -  **true**: supported.                                                           |
   |                       |                       |                                                                                   |
   |                       |                       | -  **false**: not supported.                                                      |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------+
   | subVersion            | String                | **Definition**:                                                                   |
   |                       |                       |                                                                                   |
   |                       |                       | Cluster image version.                                                            |
   |                       |                       |                                                                                   |
   |                       |                       | **Value range**:                                                                  |
   |                       |                       |                                                                                   |
   |                       |                       | N/A                                                                               |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------+
   | isEosCluster          | Boolean               | **Definition**:                                                                   |
   |                       |                       |                                                                                   |
   |                       |                       | Whether the cluster image version has reached EOS.                                |
   |                       |                       |                                                                                   |
   |                       |                       | **Value range**:                                                                  |
   |                       |                       |                                                                                   |
   |                       |                       | -  true: yes.                                                                     |
   |                       |                       |                                                                                   |
   |                       |                       | -  false: no.                                                                     |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------+

.. _listclustersdetails__response_snapshotpolicyresp:

.. table:: **Table 6** SnapshotPolicyResp

   +-----------------------+-----------------------+--------------------------------------------------------+
   | Parameter             | Type                  | Description                                            |
   +=======================+=======================+========================================================+
   | backupEnable          | Boolean               | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Whether to enable automatic snapshots for the cluster. |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | -  **true**: Yes                                       |
   |                       |                       |                                                        |
   |                       |                       | -  **false**: No                                       |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | bakPeriod             | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Snapshot creation time.                                |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | bakFrequency          | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Snapshot creation interval.                            |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | -  DAY: every day                                      |
   |                       |                       |                                                        |
   |                       |                       | -  MON: every Monday                                   |
   |                       |                       |                                                        |
   |                       |                       | -  TUR: every Tuesday                                  |
   |                       |                       |                                                        |
   |                       |                       | -  WED: every Wednesday                                |
   |                       |                       |                                                        |
   |                       |                       | -  THU: every Thursday                                 |
   |                       |                       |                                                        |
   |                       |                       | -  FRI: every Friday                                   |
   |                       |                       |                                                        |
   |                       |                       | -  SAT: every Saturday                                 |
   |                       |                       |                                                        |
   |                       |                       | -  SUN: every Sunday                                   |
   |                       |                       |                                                        |
   |                       |                       | -  HOUR: every hour                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | bakKeepDay            | Integer               | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Number of retained snapshots.                          |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+

.. _listclustersdetails__response_clusterlistinstances:

.. table:: **Table 7** ClusterListInstances

   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | Parameter             | Type                                                                            | Description                                                      |
   +=======================+=================================================================================+==================================================================+
   | status                | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Cluster node status.                                             |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | -  **100**: creating                                             |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | -  **200**: available                                            |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | -  **303**: unavailable, for example, due to a creation failure. |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | type                  | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Type of the current node.                                        |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | id                    | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Instance ID.                                                     |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | name                  | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Instance name.                                                   |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | specCode              | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Node flavor name.                                                |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | azCode                | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | AZ of the node.                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | ip                    | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Instance IP address.                                             |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | volume                | :ref:`ClusterVolumeRsp <listclustersdetails__response_clustervolumersp>` object | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Instance disk information.                                       |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | resourceId            | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Instance resource ID.                                            |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+
   | subnetId              | String                                                                          | **Definition**:                                                  |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | Subnet ID of the current node.                                   |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | **Value range**:                                                 |
   |                       |                                                                                 |                                                                  |
   |                       |                                                                                 | N/A                                                              |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------------------------------------------+

.. _listclustersdetails__response_clustervolumersp:

.. table:: **Table 8** ClusterVolumeRsp

   +-----------------------+-----------------------+----------------------------+
   | Parameter             | Type                  | Description                |
   +=======================+=======================+============================+
   | type                  | String                | **Definition**:            |
   |                       |                       |                            |
   |                       |                       | Instance disk type.        |
   |                       |                       |                            |
   |                       |                       | **Value range**:           |
   |                       |                       |                            |
   |                       |                       | N/A                        |
   +-----------------------+-----------------------+----------------------------+
   | size                  | Integer               | **Definition**:            |
   |                       |                       |                            |
   |                       |                       | Instance disk size.        |
   |                       |                       |                            |
   |                       |                       | **Value range**:           |
   |                       |                       |                            |
   |                       |                       | N/A                        |
   +-----------------------+-----------------------+----------------------------+
   | resourceIds           | Array of strings      | **Definition**:            |
   |                       |                       |                            |
   |                       |                       | Instance disk resource ID. |
   |                       |                       |                            |
   |                       |                       | **Value range**:           |
   |                       |                       |                            |
   |                       |                       | N/A                        |
   +-----------------------+-----------------------+----------------------------+

.. _listclustersdetails__response_publickibanarespbody:

.. table:: **Table 9** publicKibanaRespBody

   +-----------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------+
   | Parameter             | Type                                                                                        | Description                                             |
   +=======================+=============================================================================================+=========================================================+
   | eipSize               | Integer                                                                                     | **Definition**:                                         |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | The bandwidth size in Mbit/s.                           |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | **Value range**:                                        |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | N/A                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------+
   | elbWhiteListResp      | :ref:`kibanaElbWhiteListResp <listclustersdetails__response_kibanaelbwhitelistresp>` object | **Definition**:                                         |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | Kibana public network access control information.       |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | **Value range**:                                        |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | N/A                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------+
   | publicKibanaIp        | String                                                                                      | **Definition**:                                         |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | Specifies the IP address for accessing Kibana.          |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | **Value range**:                                        |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | N/A                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------+
   | bandwidthResourceId   | String                                                                                      | **Definition**:                                         |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | Resource ID corresponding to the Kibana public network. |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | **Value range**:                                        |
   |                       |                                                                                             |                                                         |
   |                       |                                                                                             | N/A                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------+---------------------------------------------------------+

.. _listclustersdetails__response_kibanaelbwhitelistresp:

.. table:: **Table 10** kibanaElbWhiteListResp

   +-----------------------+-----------------------+---------------------------------------------+
   | Parameter             | Type                  | Description                                 |
   +=======================+=======================+=============================================+
   | enableWhiteList       | Boolean               | **Definition**:                             |
   |                       |                       |                                             |
   |                       |                       | Whether to enable Kibana access control.    |
   |                       |                       |                                             |
   |                       |                       | **Value range**:                            |
   |                       |                       |                                             |
   |                       |                       | -  **true**: Access control is enabled.     |
   |                       |                       |                                             |
   |                       |                       | -  **false**: Access control is disabled.   |
   +-----------------------+-----------------------+---------------------------------------------+
   | whiteList             | String                | **Definition**:                             |
   |                       |                       |                                             |
   |                       |                       | Whitelist for Kibana public network access. |
   |                       |                       |                                             |
   |                       |                       | **Value range**:                            |
   |                       |                       |                                             |
   |                       |                       | N/A                                         |
   +-----------------------+-----------------------+---------------------------------------------+

.. _listclustersdetails__response_elbwhitelistresp:

.. table:: **Table 11** elbWhiteListResp

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                                                                 |
   +=======================+=======================+=============================================================================================================================================================================================================+
   | enableWhiteList       | Boolean               | **Definition**:                                                                                                                                                                                             |
   |                       |                       |                                                                                                                                                                                                             |
   |                       |                       | Whether to enable public network access control via ELB. If a whitelist is set, only IP addresses on the whitelist can access the cluster. If no whitelist is set, all IP addresses can access the cluster. |
   |                       |                       |                                                                                                                                                                                                             |
   |                       |                       | **Value range**:                                                                                                                                                                                            |
   |                       |                       |                                                                                                                                                                                                             |
   |                       |                       | -  **true**: Public network access control is enabled.                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                                             |
   |                       |                       | -  **false**: Public network access control is disabled.                                                                                                                                                    |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | whiteList             | String                | **Definition**:                                                                                                                                                                                             |
   |                       |                       |                                                                                                                                                                                                             |
   |                       |                       | Whitelist for public network access.                                                                                                                                                                        |
   |                       |                       |                                                                                                                                                                                                             |
   |                       |                       | **Value range**:                                                                                                                                                                                            |
   |                       |                       |                                                                                                                                                                                                             |
   |                       |                       | N/A                                                                                                                                                                                                         |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _listclustersdetails__response_clusterlisttags:

.. table:: **Table 12** ClusterListTags

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | key                   | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Tag key.              |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+
   | value                 | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Tag value.            |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+

.. _listclustersdetails__response_clusterlistfailedreasons:

.. table:: **Table 13** ClusterListFailedReasons

   +-----------------------+-----------------------+-----------------------------------------------------------+
   | Parameter             | Type                  | Description                                               |
   +=======================+=======================+===========================================================+
   | errorCode             | String                | **Parameter description**:                                |
   |                       |                       |                                                           |
   |                       |                       | Error code.                                               |
   |                       |                       |                                                           |
   |                       |                       | **Options**:                                              |
   |                       |                       |                                                           |
   |                       |                       | -  **CSS.6000**: A cluster fails to be created.           |
   |                       |                       |                                                           |
   |                       |                       | -  **CSS.6001**: A cluster fails to be scaled out.        |
   |                       |                       |                                                           |
   |                       |                       | -  **CSS.6002**: A cluster fails to be restarted.         |
   |                       |                       |                                                           |
   |                       |                       | -  **CSS.6004**: A node fails to be created in a cluster. |
   |                       |                       |                                                           |
   |                       |                       | -  **CSS.6005**: A service fails to be initialized.       |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | errorMsg              | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Error details.                                            |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | N/A                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------+

Example Requests
----------------

-  Querying the First Two Clusters

   .. code-block::

      - Method 1: GET https://{Endpoint}/v1.0/{project_id}/clusters?start=1&limit=2
      - Method 2: GET https://{Endpoint}/v1.0/{project_id}/clusters?limit=2

-  Querying the First 10 Clusters

   .. code-block::

      - Method 1: GET https://{Endpoint}/v1.0/{project_id}/clusters?start=1&limit=10
      - Method 2: GET https://{Endpoint}/v1.0/{project_id}/clusters?limit=10

Example Responses
-----------------

**Status code: 200**

Request succeeded. This is only an example. The responses to the four requests are similar. In the example, there is only one cluster list.

.. code-block::

   {
     "totalSize" : 1,
     "clusters" : [ {
       "datastore" : {
         "type" : "elasticsearch",
         "version" : "7.10.2",
         "subVersion" : "7.10.2_24.3.0_0827",
         "isEosCluster" : false,
         "supportSecuritymode" : false
       },
       "instances" : [ {
         "status" : "200",
         "type" : "ess",
         "id" : "{INSTANCE_ID}",
         "name" : "css-8bc5-ess-esn-1-1",
         "specCode" : "ess.spec-4u8g",
         "azCode" : "{AZ_CODE}",
         "volume" : {
           "type" : "ULTRAHIGH",
           "size" : 40,
           "resourceIds" : [ "{RESOURCE_ID}" ]
         },
         "ip" : "192.168.0.122",
         "resourceId" : "{RESOURCE_ID}",
         "subnetId" : "{SUBNET_ID}"
       } ],
       "publicKibanaResp" : {
         "eipSize" : 10,
         "publicKibanaIp" : "100.95.152.28:9200",
         "bandwidthResourceId" : "18bec13f-5cc1-4631-867f-33505d15be12"
       },
       "elbWhiteList" : {
         "whiteList" : "",
         "enableWhiteList" : false
       },
       "updated" : "2023-10-09T02:07:13",
       "name" : "css-8bc5",
       "publicIp" : "100.85.222.202",
       "created" : "2023-10-09T02:07:13",
       "id" : "{CLUSTER_ID}",
       "status" : "200",
       "endpoint" : "192.168.0.122:9200",
       "vpcId" : "{VPC_ID}",
       "subnetId" : "{SUBNET_ID}",
       "currentSubnetIds" : "{SUBNET_ID}",
       "securityGroupId" : "{SECURITY_GROUP_ID}",
       "bandwidthResourceId" : "{BANDWIDTH_RESOURCE_ID}",
       "bandwidthSize" : 3,
       "httpsEnable" : true,
       "authorityEnable" : true,
       "diskEncrypted" : false,
       "backupAvailable" : false,
       "actionProgress" : { },
       "actions" : [ ],
       "enterpriseProjectId" : "0",
       "tags" : [ ],
       "period" : true
     } ]
   }

Status Codes
------------

+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                 |
+===================================+=============================================================================================================================================+
| 200                               | Request succeeded. This is only an example. The responses to the four requests are similar. In the example, there is only one cluster list. |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                            |
|                                   |                                                                                                                                             |
|                                   | Modify the request before retry.                                                                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+
| 404                               | The requested resource could not be found.                                                                                                  |
|                                   |                                                                                                                                             |
|                                   | Modify the request before retry.                                                                                                            |
+-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
