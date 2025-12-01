:original_name: ListImages.html

.. _ListImages:

Obtaining the ID of the Target Image to Upgrade To
==================================================

Function
--------

This API is used to obtain the IDs of target images the current cluster can be upgraded to. The upgrade types are as follows:

-  During a same-version upgrade, kernel patches are updated for a cluster. The cluster is upgraded to the latest image of the current version to fix known issues or optimize performance. For example, if the current cluster version is 7.10.2(7.10.2_24.3.3_0102), upon a same-version upgrade, the cluster will be upgraded to the latest image 7.10.2(7.10.2_24.3.4_0109) of version 7.10.2. (The version numbers used here are examples only.)

-  Cross-version upgrade: Upgrade the cluster version. The cluster will be upgraded to the latest image of the target version to enhance functions or incorporate versions. For example, if the current cluster version is 7.6.2(7.6.2_24.3.3_1224), upon a cross-version upgrade, the cluster will be upgraded to the latest image 7.10.2(7.10.2_24.3.4_0109) of version 7.10.2. (The version numbers used here are examples only.)

-  Cross-engine upgrade: Change an Elasticsearch cluster to an OpenSearch cluster. Cross-engine upgrade means to upgrade an Elasticsearch cluster to the latest image of the target OpenSearch version. For example, if the Elasticsearch cluster version is 7.10.2(7.10.2_24.3.3_0102), upon a cross-engine upgrade, the Elasticsearch cluster will be upgraded to the latest image 1.3.6(1.3.6_24.3.4_0109) of OpenSearch 1.3.6. (The version numbers used here are examples only.) This feature is not supported currently.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/target/{upgrade_type}/images

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Project ID of the account.                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | ID of the cluster to be upgraded. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Cluster ID.                                                                                                                          |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | upgrade_type    | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Upgrade type.                                                                                                                        |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | -  **same**: same-version upgrade.                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | -  **cross**: cross-version upgrade.                                                                                                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | -  **cross-engine**: cross-engine upgrade.                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                   |
   +=================+=================+=================+===============================================================================================================+
   | offset          | No              | Integer         | **Definition**:                                                                                               |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | Start value of the query. The default value is 0.                                                             |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                              |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | N/A                                                                                                           |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                              |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | 0-1000                                                                                                        |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                            |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | 0                                                                                                             |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | **Definition**:                                                                                               |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | Number of images to be queried. The default value is **10**, indicating that 10 images are queried at a time. |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                              |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | N/A                                                                                                           |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                              |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | 1-1000                                                                                                        |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                            |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | 10                                                                                                            |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+
   | Parameter               | Type                                                                                         | Description                                          |
   +=========================+==============================================================================================+======================================================+
   | needUploadUpgradePlugin | Boolean                                                                                      | **Definition**:                                      |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | Whether to upload the plug-in of the target version. |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | **Value range**:                                     |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | N/A                                                  |
   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+
   | imageInfoList           | Array of :ref:`GetTargetImageIdDetail <listimages__response_gettargetimageiddetail>` objects | **Definition**:                                      |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | Image details.                                       |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | **Value range**:                                     |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | N/A                                                  |
   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+
   | totalSize               | Integer                                                                                      | **Definition**:                                      |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | Number of target images.                             |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | **Value range**:                                     |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | N/A                                                  |
   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+

.. _listimages__response_gettargetimageiddetail:

.. table:: **Table 4** GetTargetImageIdDetail

   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                                          |
   +=======================+=======================+======================================================================================================================================================================================+
   | id                    | String                | **Definition**:                                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | ID of an image that can be upgraded.                                                                                                                                                 |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | **Value range**:                                                                                                                                                                     |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | N/A                                                                                                                                                                                  |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | displayName           | String                | **Definition**:                                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | Name of an image that can be upgraded.                                                                                                                                               |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | **Value range**:                                                                                                                                                                     |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | N/A                                                                                                                                                                                  |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | imageDesc             | String                | **Definition**:                                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | Image description.                                                                                                                                                                   |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | **Value range**:                                                                                                                                                                     |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | N/A                                                                                                                                                                                  |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | datastoreType         | String                | **Definition**:                                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | Cluster engine type.                                                                                                                                                                 |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | **Value range**:                                                                                                                                                                     |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | -  elasticsearch: Cloud Search Service (CSS) provides distributed search capabilities, log analytics, reporting, and semantic search based on open-source Elasticsearch.             |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | -  logstash: Provides functions such as data ingestion, transformation, cleaning, and parsing based on open-source Logstash.                                                         |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | -  opensearch: Provides distributed search, log analytics, reporting, and semantic search based on open-source OpenSearch. It is the future version of CSS's Elasticsearch clusters. |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | datastoreVersion      | String                | **Definition**:                                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | Image engine version.                                                                                                                                                                |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | **Value range**:                                                                                                                                                                     |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | N/A                                                                                                                                                                                  |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | priority              | Integer               | **Definition**:                                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | Priority of the target image. A larger value indicates a higher priority.                                                                                                            |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | **Value range**:                                                                                                                                                                     |
   |                       |                       |                                                                                                                                                                                      |
   |                       |                       | N/A                                                                                                                                                                                  |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

Obtain the target image for a cross-version upgrade of the cluster.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/target/cross/images

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "needUploadUpgradePlugin" : false,
     "imageInfoList" : [ ],
     "totalSize" : 0
   }

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                     |
+===================================+=================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                |
|                                   |                                                                                                                                                                 |
|                                   | The client should not repeat the request without modifications.                                                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.                                                                                                                                               |
|                                   |                                                                                                                                                                 |
|                                   | The server has received the request and understood it, but the server refuses to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
