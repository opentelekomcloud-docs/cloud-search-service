:original_name: UpdateVpcepConnection.html

.. _UpdateVpcepConnection:

Updating an Endpoint Connection
===============================

Function
--------

This API is used to update the VPCEP connection of a cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/connections

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Project ID of the account.                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                         |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | ID of the cluster whose VPC endpoint you want to update. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | Cluster ID.                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                         |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +------------------+-----------------+------------------+--------------------------------------+
   | Parameter        | Mandatory       | Type             | Description                          |
   +==================+=================+==================+======================================+
   | action           | Yes             | String           | Expected behavior.                   |
   |                  |                 |                  |                                      |
   |                  |                 |                  | -  receive: Accept the VPC endpoint. |
   |                  |                 |                  |                                      |
   |                  |                 |                  | -  reject: Reject the VPC endpoint.  |
   +------------------+-----------------+------------------+--------------------------------------+
   | endpoint_id_list | Yes             | Array of strings | Lists VPC endpoint IDs.              |
   +------------------+-----------------+------------------+--------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Update an endpoint connection.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/vpcepservice/connections

   {
     "action" : "receive",
     "endpoint_id_list" : [ "f132bb14-e1d5-4f25-9f7c-a29e4c8effd4" ]
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
