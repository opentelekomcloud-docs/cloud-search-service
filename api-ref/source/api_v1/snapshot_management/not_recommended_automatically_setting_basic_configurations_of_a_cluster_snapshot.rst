:original_name: StartAutoSetting.html

.. _StartAutoSetting:

(Not Recommended) Automatically Setting Basic Configurations of a Cluster Snapshot
==================================================================================

Function
--------

This API is used to configure basic settings for automatic cluster snapshot creation, including automatically creating an IAM agency and the OBS bucket and file path used for storing snapshots. This API also enables cluster snapshots. Cluster snapshots enhance data protection and restoration capabilities for clusters.

Constraints
-----------

-  This API automatically creates an OBS bucket and agency for the snapshot. If there are multiple clusters, an OBS bucket will be created for each cluster via this API. As a result, the OBS quota may be insufficient, and many OBS buckets are difficult to maintain. You are advised to use the API :ref:`Enabling or Modifying the Cluster Snapshot Function <updatesnapshotsetting>`.

-  When snapshots are enabled for a cluster, the API will use the previous configuration to ensure consistency. If snapshots are enabled for the first, the system automatically creates an OBS bucket and file path and preferentially uses an existing agency. If there are no agencies, the system automatically creates an agency named css-obs-agency.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/auto_setting

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                               |
   +=================+=================+=================+===========================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                          |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | **Constraints**:                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | **Value range**:                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | Project ID of the account.                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | **Default value**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                       |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | ID of the cluster where snapshots you want to back up. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | **Constraints**:                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | **Value range**:                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | Cluster ID.                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | **Default value**:                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                                       |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Automatically configure basic settings of a cluster snapshot.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/auto_setting

Example Responses
-----------------

None

Status Codes
------------

+-------------+---------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                       |
+=============+===================================================================================================+
| 200         | Request succeeded.                                                                                |
+-------------+---------------------------------------------------------------------------------------------------+
| 406         | The server could not fulfill the request according to the content characteristics of the request. |
+-------------+---------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
