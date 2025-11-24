:original_name: StopSnapshot.html

.. _StopSnapshot:

Disabling the Snapshot Function
===============================

Function
--------

This API is used to disable the snapshot function.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                     |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | Project ID of the account.                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | ID of the cluster for which snapshots are disabled. For details about how to obtain the cluster ID, see :ref:`Obtaining a Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | Cluster ID.                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

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

Disable snapshots.

.. code-block:: text

   DELETE https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshots

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
