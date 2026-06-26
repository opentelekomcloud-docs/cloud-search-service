:original_name: StartAutoCreateSnapshots.html

.. _StartAutoCreateSnapshots:

Enabling Automatic Snapshot Creation
====================================

Function
--------

This API is used to enable automatic snapshot creation for clusters. A snapshot saves a point-in-time copy of a cluster in an OBS bucket. Using this snapshot you can restore the cluster to a previous state.

When automatic snapshot creation is enabled, snapshots are automatically created daily or weekly based on a preset time schedule, ensuring ongoing data protection.

Only Elasticsearch and OpenSearch clusters support automatic snapshot creation.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v2.0/{project_id}/clusters/{cluster_id}/snapshots/policy/open

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
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Cluster ID. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Cluster ID.                                                                                                                      |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                        |
   +=================+=================+=================+====================================================================================================================================================================================================================================================================+
   | indices         | No              | String          | **Definition**:                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Name of the index to be backed up.                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  If no index is specified, snapshots will be created for all indexes in the cluster.                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  Or you can back up indexes by specifying their names, for example, index1,index2,index3.                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  The value can contain a maximum of 1024 characters and cannot contain uppercase letters, spaces, or "<|>/?.                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | You can use an asterisk (*) to match multiple indexes. For example, index* indicates that all indexes with the prefix index will be backed up.                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | The value can contain 0 to 1,024 characters. It cannot contain uppercase letters, spaces, or the following special characters: "<|>/?                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | The default value is empty, indicating that all indexes will be backed up.                                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | keepday         | Yes             | Integer         | **Definition**:                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Set the number of snapshots to be retained. Expired snapshots will be automatically deleted on the half hour. The deletion policy applies only to auto snapshots that are executed at the same frequency as the current automatic snapshot creation policy.        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | If the snapshot creation interval is short or if the data size of indexes is large, the number of automatic snapshots retained may not reach the value set using this parameter.                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | 1~90                                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | frequency       | No              | String          | **Definition**:                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Frequency of automatically creating snapshots.                                                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  HOUR: Execute once every hour on the hour.                                                                                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  DAY: Execute once every day.                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | -  SUN, MON, TUE, WED, THU, FRI, and SAT: Execute the task at the specified day of every week. For example, SUN indicates that the task is executed once every Sunday.                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | DAY                                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | period          | No              | String          | **Definition**:                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Time when a snapshot is created every day.                                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | When frequency is set to HOUR, you do not need to specify period. By default, snapshot creation starts from the next hour after the settings are successful.                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Snapshots can only be created on the hour. The time format is the time followed by the time zone, specifically, **HH:mm z**. In the format, **HH:mm** refers to the hour time and **z** refers to the time zone. For example, 00:00 GMT+08:00 and 01:00 GMT+08:00. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | 00:00 GMT+08:00                                                                                                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | prefix          | Yes             | String          | **Definition**:                                                                                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Prefix of the name of an automatically created snapshot. A snapshot name consists of the snapshot name prefix and timestamp, for example, snapshot-1566921603720.                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Value range**:                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Enter up to 32 characters and start with a lowercase letter. Lowercase letters, digits, hyphens (-), and underscores (_) are allowed.                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | **Default value**:                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Enable automatic backup. Seven snapshots are automatically created every day at 16:00. The snapshot name prefix is snapshot.XXXX.

.. code-block:: text

   POST https://{Endpoint}/v2.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/snapshots/policy/open

   {
     "indices" : "*",
     "keepday" : 7,
     "frequency" : "DAY",
     "period" : "16:00 GMT+08:00",
     "prefix" : "snapshot"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                           |
+===================================+=======================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                                    |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                      |
|                                   |                                                                                                                                                                       |
|                                   | Modify the request before retry.                                                                                                                                      |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
