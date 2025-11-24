:original_name: UpdateShrinkNodes.html

.. _UpdateShrinkNodes:

Scaling In a Cluster by Removing a Specific Node
================================================

Function
--------

During a scale-in, the data on the to-be-removed nodes needs to be migrated to the remaining nodes. The timeout for data migration per node is 48 hours. Scale-in will fail if this timeout expires. When the cluster has large quantities of data, you are advised to manually adjust the data migration rate and avoid performing the migration during peak hours.

This API is used to scale in a cluster by removing specified nodes.

.. note::

   All mission-critical data has been backed up before a cluster scale-in. This is to prevent data loss.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/node/offline

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                |
   +=================+=================+=================+============================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.           |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Constraints**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Value range**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | Project ID of the account.                                                                                                                 |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Default value**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                        |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                            |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | ID of the cluster you want to scale in. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Constraints**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Value range**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | Cluster ID.                                                                                                                                |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | **Default value**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                            |
   |                 |                 |                 | N/A                                                                                                                                        |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                                                                                                      |
   +=================+=================+==================+==================================================================================================================================+
   | migrate_data    | No              | String           | **Definition**:                                                                                                                  |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | Whether to migrate data.                                                                                                         |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Value range**:                                                                                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | -  true: Migrate data.                                                                                                           |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | -  false: Do not migrate data.                                                                                                   |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Default value**:                                                                                                               |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | true                                                                                                                             |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | shrink_nodes    | Yes             | Array of strings | **Definition**:                                                                                                                  |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | ID of the node to be removed from the cluster.                                                                                   |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Constraints**:                                                                                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | N/A                                                                                                                              |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Value range**:                                                                                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | Obtain the **ID** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`.                    |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Default value**:                                                                                                               |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | N/A                                                                                                                              |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | agency_name     | No              | String           | **Definition**:                                                                                                                  |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | Agency name. You can create an agency to allow CSS to call other cloud services.                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Constraints**:                                                                                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | VPC permissions required by the agency: "``vpc:subnets:get``","``vpc:ports:*``".                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | This parameter is mandatory when the new IAM plane is connected. This parameter is optional when the old IAM plane is connected. |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Value range**:                                                                                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | N/A                                                                                                                              |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Default value**:                                                                                                               |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | N/A                                                                                                                              |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Scale in a cluster by scaling in specified nodes.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/node/offline

   {
     "shrink_nodes" : [ "2077bdf3-b90d-412e-b460-635b9b159c11" ],
     "migrate_data" : "true"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                        |
+===================================+====================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                   |
|                                   |                                                                                                                                    |
|                                   | Modify the request before retry.                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                       |
|                                   |                                                                                                                                    |
|                                   | The resource that the client attempts to create already exists, or the update request fails to be processed because of a conflict. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
