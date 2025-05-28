:original_name: UpgradeCore.html

.. _UpgradeCore:

Upgrading a Cluster Kernel
==========================

Function
--------

This API is used to upgrade Elasticsearch from an earlier version to a later version or the same version.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/inst-type/{inst_type}/image/upgrade

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be upgraded.                                                                                                |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | inst_type  | Yes       | String | Type of the node to be upgraded. Currently, its value can only be **all**.                                                       |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | Parameter            | Mandatory       | Type            | Description                                                                      |
   +======================+=================+=================+==================================================================================+
   | target_image_id      | Yes             | String          | ID of the target image version.                                                  |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | upgrade_type         | Yes             | String          | Upgrade type.                                                                    |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **same**: same-version upgrade.                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **cross**: cross-version upgrade.                                             |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **cross-engine**: cross-engine upgrade.                                       |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | indices_backup_check | Yes             | Boolean         | Whether to perform backup verification.                                          |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **true**                                                                      |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **false**                                                                     |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | agency               | Yes             | String          | Agency name. You can create an agency to allow CSS to call other cloud services. |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | cluster_load_check   | No              | Boolean         | Indicates whether to verify the load. The default value is true.                 |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  true: Verify the load.                                                        |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  false: Do not verify the load.                                                |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | batch_size           | No              | Integer         | Data migration concurrency in terms of the number of data nodes.                 |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Update a cluster version.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/inst-type/all/image/upgrade

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
