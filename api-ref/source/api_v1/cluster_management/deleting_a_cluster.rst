:original_name: DeleteCluster.html

.. _DeleteCluster:

Deleting a Cluster
==================

Function
--------

This API is used to delete a cluster. All resources of the deleted cluster, including customer data, will be released. If you want to retain the data in a customer cluster, create a snapshot before deleting the cluster.

.. note::

   Clusters frozen for public security reasons cannot be deleted. Deleting a cluster will also clear its data. Exercise caution.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

DELETE /v1.0/{project_id}/clusters/{cluster_id}

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                              |
   +=================+=================+=================+==========================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                          |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.         |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | **Constraints**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | **Value range**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | Project ID of the account.                                                                                                               |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | **Default value**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                      |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                          |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | ID of the cluster you want to delete. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | **Constraints**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | **Value range**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | Cluster ID.                                                                                                                              |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | **Default value**:                                                                                                                       |
   |                 |                 |                 |                                                                                                                                          |
   |                 |                 |                 | N/A                                                                                                                                      |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------+

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

Delete a cluster.

.. code-block:: text

   DELETE https://{Endpoint}/v1.0/{project_id}/clusters/2a197c4d-5467-4003-931d-83ec49939cf

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+--------------------------------------------+
| Status Code                       | Description                                |
+===================================+============================================+
| 200                               | Request succeeded.                         |
+-----------------------------------+--------------------------------------------+
| 400                               | Invalid request.                           |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+
| 404                               | The requested resource could not be found. |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
