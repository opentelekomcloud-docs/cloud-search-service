:original_name: RestartCluster.html

.. _RestartCluster:

Restarting a Cluster (Deprecated)
=================================

Function
--------

This API is used to restart a data node in a cluster, which will interrupt services. To restart all nodes in a cluster, you are advised to use [Restart Cluster V2] (RestartClusterMultiRole.xml).

.. note::

   When the cluster is available, ensure that the cluster has stopped processing service data (such as importing data and searching for data). Otherwise, data may be lost when the cluster is restarted.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/restart

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                               |
   +=================+=================+=================+===========================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.          |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | **Constraints**:                                                                                                                          |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | **Value range**:                                                                                                                          |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | Project ID of the account.                                                                                                                |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | **Default value**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                       |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                           |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | ID of the cluster you want to restart. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | **Constraints**:                                                                                                                          |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | **Value range**:                                                                                                                          |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | Cluster ID.                                                                                                                               |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | **Default value**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                           |
   |                 |                 |                 | N/A                                                                                                                                       |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------+

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

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/47e49a5e-8ced-4d0d-ae15-2af62ac468e3/restart

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
