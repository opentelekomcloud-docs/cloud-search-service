:original_name: UpdateShrinkNodes.html

.. _UpdateShrinkNodes:

Scaling In a Cluster by Removing a Specific Node
================================================

Function
--------

This API is used to scale in a cluster by removing a specified node. Yearly/Monthly clusters do not support the removal of specified nodes by calling this API.

.. note::

   All mission-critical data has been backed up before a cluster scale-in. This is to prevent data loss.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/node/offline

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Specifies the ID of the cluster to be scaled in. For details, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                                                                                                      |
   +=================+=================+==================+==================================================================================================================================+
   | migrate_data    | No              | String           | **Parameter description**:                                                                                                       |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | Whether to migrate data.                                                                                                         |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Options**:                                                                                                                     |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | -  "true": Migrate data.                                                                                                         |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | -  "false": Do not migrate data.                                                                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Default value**:                                                                                                               |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | "true"                                                                                                                           |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | shrinkNodes     | Yes             | Array of strings | **Parameter description**:                                                                                                       |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | ID of the node you want to remove.                                                                                               |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | Obtain the **ID** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`.                    |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | agency_name     | No              | String           | **Parameter description**:                                                                                                       |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | Agency name. You can create an agency to allow CSS to call other cloud services.                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Constraints**:                                                                                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | This parameter is mandatory when the new IAM plane is connected. This parameter is optional when the old IAM plane is connected. |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Options**:                                                                                                                     |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | VPC permissions required by the agency: "``vpc:subnets:get``","``vpc:ports:*``".                                                 |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | **Default value**:                                                                                                               |
   |                 |                 |                  |                                                                                                                                  |
   |                 |                 |                  | N/A                                                                                                                              |
   +-----------------+-----------------+------------------+----------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Scale in a cluster by scaling in specified nodes.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/node/offline

   {
     "shrinkNodes" : [ "2077bdf3-b90d-412e-b460-635b9b159c11" ],
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
