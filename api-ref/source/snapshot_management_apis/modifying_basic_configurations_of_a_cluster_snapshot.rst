:original_name: css_03_0030.html

.. _css_03_0030:

Modifying Basic Configurations of a Cluster Snapshot
====================================================

.. note::

   Using this API will automatically enable the snapshot function.

Function
--------

This API is used to modify the basic configurations of a cluster snapshot. The basic configurations include the OBS bucket and IAM agency.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/setting

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+--------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                            |
   +============+===========+========+========================================================+
   | project_id | Yes       | String | Project ID.                                            |
   +------------+-----------+--------+--------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster where index data is to be backed up. |
   +------------+-----------+--------+--------------------------------------------------------+

Request
-------

:ref:`Table 2 <css_03_0030__table82481020121413>` describes the request parameters.

.. _css_03_0030__table82481020121413:

.. table:: **Table 2** Parameter description

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | bucket          | Yes             | String          | OBS bucket used for index data backup. If there is snapshot data in an OBS bucket, only the OBS bucket is used and cannot be changed.                                                                                                                                                                                                                                                                                                                       |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | agency          | Yes             | String          | IAM agency used to access OBS.                                                                                                                                                                                                                                                                                                                                                                                                                              |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | snapshotCmkId   | No              | String          | Key ID used for snapshot encryption.                                                                                                                                                                                                                                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  The Default Master Keys cannot be used to create grants. Specifically, you cannot use Default Master Keys whose aliases end with **/default** in KMS to encrypt snapshots.                                                                                                                                                                                                                                                                               |
   |                 |                 |                 | -  If a snapshot has been stored in the OBS bucket, you cannot modify the parameters for encrypting the snapshot.                                                                                                                                                                                                                                                                                                                                           |
   |                 |                 |                 | -  If the key used for encryption is in the **Pending deletion** or **disable** state, you cannot perform backup and restoration operations on the cluster. Specifically, new snapshots cannot be created for the cluster, and existing snapshots cannot be used for restoration. In this case, switch to the KMS management console and change the state of the target key to **enable** so that backup and restore operations are allowed on the cluster. |
   |                 |                 |                 | -  If the key used for encryption is deleted, backup and restore operations are not allowed on the cluster. In addition, the deleted key cannot be restored. Therefore, exercise caution when deleting a key.                                                                                                                                                                                                                                               |
   |                 |                 |                 | -  You are advised to disable the automatic snapshot creation function if the key is deleted or is in the **Pending deletion** or **disable** state. In this condition, automatic snapshot creation is allowed based on the configured snapshot policy. However, all automatic snapshot creation tasks will fail, and the failed tasks are displayed in the failed task list in the **Failed Tasks** dialog box.                                            |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response
--------

None

Examples
--------

Example request

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/setting
   {
       "bucket":"test-bucket",
       "agency":"usearch",
       "snapshotCmkId":"42546bb1-8025-4ad1-868f-600729c341aea"
   }

Status Code
-----------

:ref:`Table 3 <css_03_0030__table209491933101317>` describes the status code.

.. _css_03_0030__table209491933101317:

.. table:: **Table 3** Status code

   +-------------+---------------------+------------------------------------------------------------------------------------------------+
   | Status Code | Code                | Status Code Description                                                                        |
   +=============+=====================+================================================================================================+
   | 200         | OK                  | The request is processed successfully.                                                         |
   +-------------+---------------------+------------------------------------------------------------------------------------------------+
   | 406         | Not Acceptable      | The server cannot fulfill the request according to the content characteristics of the request. |
   +-------------+---------------------+------------------------------------------------------------------------------------------------+
   | 412         | Precondition Failed | The server does not meet one of the preconditions that the requester puts on the request.      |
   +-------------+---------------------+------------------------------------------------------------------------------------------------+
   | 504         | Gateway Timeout     | A gateway timeout error occurred.                                                              |
   +-------------+---------------------+------------------------------------------------------------------------------------------------+
