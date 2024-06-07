:original_name: UpgradeCore.html

.. _UpgradeCore:

Upgrading a Cluster Kernel
==========================

Function
--------

This API is used to upgrade Elasticsearch from an earlier version to a later version or the same version.

Calling Method
--------------

For details, see :ref:`Calling APIs <iam_01_0023>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/inst-type/{inst_type}/image/upgrade

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                         |
   +============+===========+========+=====================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be upgraded.                                                                                   |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | inst_type  | Yes       | String | Type of the node to be upgraded. Currently, its value can only be **all**.                                          |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+

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
   |                      |                 |                 | -  **same**: upgrade to the same version.                                        |
   |                      |                 |                 | -  **cross**: upgrade to a different version.                                    |
   |                      |                 |                 | -  **crossEngine**: cross-engine upgrade.                                        |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | The value can be:                                                                |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **same**                                                                      |
   |                      |                 |                 | -  **cross**                                                                     |
   |                      |                 |                 | -  **crossEngine**                                                               |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | indices_backup_check | Yes             | Boolean         | Indicates whether to perform backup verification.                                |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **true**: Verify the backup.                                                  |
   |                      |                 |                 | -  **false**: Do not verify the backup.                                          |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | The value can be:                                                                |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **true**                                                                      |
   |                      |                 |                 | -  **false**                                                                     |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | agency               | Yes             | String          | Agency name. You can create an agency to allow CSS to call other cloud services. |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | cluster_load_check   | No              | Boolean         | Indicates whether to verify the load. The default value is **true**.             |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **true**: Verify the load.                                                    |
   |                      |                 |                 | -  **false**: Do not verify the load.                                            |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

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

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                   |
+===================================+===============================================================================================================================================================================+
| 200                               | The request is processed.                                                                                                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                              |
|                                   |                                                                                                                                                                               |
|                                   | Modify the request directly and do not attempt to retry it.                                                                                                                   |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                                                            |
|                                   |                                                                                                                                                                               |
|                                   | This status code indicates that the resource the client is attempting to create already exists, or that the update operation requested cannot be completed due to a conflict. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not satisfy one of the preconditions set by the requester in the request.                                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

For details, see :ref:`Error Code <css_03_0076>`.
