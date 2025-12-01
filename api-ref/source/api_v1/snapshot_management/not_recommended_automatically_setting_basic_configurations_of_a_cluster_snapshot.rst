:original_name: StartAutoSetting.html

.. _StartAutoSetting:

(Not Recommended) Automatically Setting Basic Configurations of a Cluster Snapshot
==================================================================================

Function
--------

This API is used to automatically set basic configurations for a cluster snapshot, including configuring OBS buckets and IAM agency.

-  **OBS Bucket**: Enter the location of the OBS bucket used for storing snapshots.

-  **Backup Path**: Enter the storage path of the snapshot in the OBS bucket.

-  **IAM Agency**: Authorize you to use OBS in IAM so that snapshots must be stored in OBS.

.. note::

   The API will automatically create an OBS bucket and an agency for automatic snapshot creation. If there are multiple clusters, each cluster will create a different OBS bucket using this API, which may exhaust the OBS quota and create the inconvenience of maintaining a large number of OBS buckets. You are advised to use the API for :ref:`Modifying Basic Settings of Cluster Snapshots <updatesnapshotsetting>`.

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
