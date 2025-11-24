:original_name: UpgradeCore.html

.. _UpgradeCore:

Upgrading a Cluster Kernel
==========================

Function
--------

This API is used to upgrade Elasticsearch from an earlier version to a later version or the same version.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/inst-type/{inst_type}/image/upgrade

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
   | inst_type       | Yes             | String          | **Definition**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Types of nodes to be upgraded.                                                                                                       |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Currently, only **all** is supported, indicating all nodes.                                                                          |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | Parameter            | Mandatory       | Type            | Description                                                                      |
   +======================+=================+=================+==================================================================================+
   | target_image_id      | Yes             | String          | **Definition**:                                                                  |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | ID of the target image version.                                                  |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Constraints**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Value range**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Default value**:                                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | upgrade_type         | Yes             | String          | **Definition**:                                                                  |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | Upgrade type.                                                                    |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Constraints**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Value range**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **same**: same-version upgrade.                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **cross**: cross-version upgrade.                                             |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **cross-engine**: cross-engine upgrade.                                       |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Default value**:                                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | indices_backup_check | Yes             | Boolean         | **Definition**:                                                                  |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | Whether to perform backup verification.                                          |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Constraints**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Value range**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  true: Verify the load.                                                        |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **false**: Do not verify the load.                                            |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Default value**:                                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | true                                                                             |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | agency               | Yes             | String          | **Definition**:                                                                  |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | Agency name. You can create an agency to allow CSS to call other cloud services. |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Constraints**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Value range**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Default value**:                                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | cluster_load_check   | No              | Boolean         | **Definition**:                                                                  |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | Indicates whether to verify the load.                                            |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Constraints**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Value range**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  true: Verify the load.                                                        |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **false**: Do not verify the load.                                            |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Default value**:                                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | true                                                                             |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | batch_size           | No              | Integer         | **Definition**:                                                                  |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | Data migration concurrency in terms of the number of data nodes.                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Constraints**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Value range**:                                                                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | **Default value**:                                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | N/A                                                                              |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Update a cluster version.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/inst-type/all/image/upgrade

   {
     "target_image_id" : "{target_image_id}",
     "upgrade_type" : "same",
     "indices_backup_check" : true,
     "agency" : "css-test-agency",
     "cluster_load_check" : true
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                      |
+===================================+==================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | The client should not repeat the request without modifications.                                                                                  |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | This status code indicates that the resource that the client attempts to create already exits, or the requested update failed due to a conflict. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                                       |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
