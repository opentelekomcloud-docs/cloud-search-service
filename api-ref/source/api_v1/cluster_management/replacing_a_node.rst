:original_name: UpdateInstance.html

.. _UpdateInstance:

Replacing a Node
================

Function
--------

This API is used to replace a failed node.

If a node in an Elasticsearch cluster is faulty, you can replace it to restore services.

The node replacement process is as follows:

#. Migrate data from the node that needs to be replaced to other available nodes.

#. Rebuild the node using the original ID, IP address, specifications, and AZ.

#. Add the new node into the cluster. The system automatically triggers a shard reallocation, migrating some of the shards

to the new node

This process does not interrupt services because data is migrated from the replaced node to other available nodes.

.. note::

   All mission-critical data has been backed up before a node replacement. This is to prevent data loss.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/instance/{instance_id}/replace

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
   |                 |                 |                 | ID of the cluster where nodes are to be replaced. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
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
   | instance_id     | Yes             | String          | **Definition**:                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | ID of the node to be replaced.                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | Node ID. Obtain the **ID** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`.                               |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================================================+
   | migrateData     | No              | String          | **Definition**:                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | Whether to migrate data.                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **Constraints**:                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **Value range**:                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | -  true: Migrate data.                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | -  false: Do not migrate data.                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **Default value**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | true                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | agency          | No              | String          | **Definition**:                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | Agency name. You can create an agency to allow CSS to call other cloud services.                                                                                       |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **Constraints**:                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | -  VPC permissions required by the agency: "``vpc:subnets:get``","``vpc:ports:*``".                                                                                    |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | -  This parameter is mandatory when the new IAM plane is connected. This parameter is optional when the old IAM plane is connected.                                    |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | -  The value can contain only letters (a-z and A-Z), digits (0-9), hyphens (-), and underscores (_). It cannot contain Chinese characters or other special characters. |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **Value range**:                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | **Default value**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                                                    |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

Replace a node.

.. code-block:: text

   PUT https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/instance/43e63449-339c-4280-a6e9-da36b0685995/replace?migrateData=true

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------+
| Status Code                       | Description                                                       |
+===================================+===================================================================+
| 200                               | Request succeeded.                                                |
+-----------------------------------+-------------------------------------------------------------------+
| 400                               | Invalid request.                                                  |
|                                   |                                                                   |
|                                   | The client should modify the request instead of re-initiating it. |
+-----------------------------------+-------------------------------------------------------------------+
| 404                               | The requested resource could not be found.                        |
|                                   |                                                                   |
|                                   | The client should modify the request instead of re-initiating it. |
+-----------------------------------+-------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
