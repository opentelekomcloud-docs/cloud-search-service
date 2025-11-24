:original_name: StartTargetClusterConnectivityTest.html

.. _StartTargetClusterConnectivityTest:

Test connectivity.
==================

Function
--------

This API is used to test the connectivity between two clusters. CSS clusters provide a log collection function, allowing users to collect clusters' run logs in real time and save them to a specified index of a specified CSS cluster. The target cluster can be the current cluster or another cluster. If logs are to be saved to another cluster, you need to use the connectivity testing API to test connectivity to the target cluster. If the target cluster cannot be reached, you need to select another cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/logs/connectivity

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID of the account.                                                                                                       |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Cluster ID. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Cluster ID.                                                                                                                      |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-------------------+-----------------+-----------------+---------------------------------+
   | Parameter         | Mandatory       | Type            | Description                     |
   +===================+=================+=================+=================================+
   | target_cluster_id | Yes             | String          | **Definition**:                 |
   |                   |                 |                 |                                 |
   |                   |                 |                 | Target cluster ID.              |
   |                   |                 |                 |                                 |
   |                   |                 |                 | **Constraints**:                |
   |                   |                 |                 |                                 |
   |                   |                 |                 | Only cluster IDs are supported. |
   |                   |                 |                 |                                 |
   |                   |                 |                 | **Value range**:                |
   |                   |                 |                 |                                 |
   |                   |                 |                 | N/A                             |
   |                   |                 |                 |                                 |
   |                   |                 |                 | **Default value**:              |
   |                   |                 |                 |                                 |
   |                   |                 |                 | N/A                             |
   +-------------------+-----------------+-----------------+---------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Test connectivity to the target cluster.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/logs/connectivity

   {
     "target_cluster_id" : "4f3deec3-efa8-4598-bf91-560aad1377a4"
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
| 400                               | The request could not be understood by the server due to malformed syntax.                                                                       |
|                                   |                                                                                                                                                  |
|                                   | Modify the request instead of retrying.                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | This status code indicates that the resource that the client attempts to create already exits, or the requested update failed due to a conflict. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
