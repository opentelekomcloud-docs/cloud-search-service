:original_name: RollingRestart.html

.. _RollingRestart:

Rolling Restart (Deprecated)
============================

Function
--------

This API is used to perform a rolling restart on a specific type of nodes in an Elasticsearch or OpenSearch cluster.

Constraints
-----------

-  Rolling restart is supported only when there are more than three nodes (including Master nodes, Client nodes, and cold data nodes) in the cluster. When the cluster is available, ensure that the cluster has stopped processing service data (such as importing and searching for data). Otherwise, data may be lost during cluster restart. During the rolling restart, you need to wait until the restarted nodes are added to the cluster and the index status changes to green. If there are a large number of indexes, the restart takes a long time.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v2.0/{project_id}/clusters/{cluster_id}/rolling_restart

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                           |
   +=================+=================+=================+=======================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.      |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Constraints**                                                                                                                       |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Range**                                                                                                                             |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                               |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Default Value**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | ID of the cluster to be restarted. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Constraints**                                                                                                                       |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                         |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Range**                                                                                                                             |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | Cluster ID.                                                                                                                           |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | **Default Value**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                   |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                            |
   +=================+=================+=================+========================================================================+
   | type            | Yes             | String          | **Definition**                                                         |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | Rolling restart type. Only **role** is supported.                      |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | **Constraints**                                                        |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | N/A                                                                    |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | **Range**                                                              |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | **role**: Restart by role.                                             |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | **Default Value**                                                      |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | N/A                                                                    |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------+
   | value           | Yes             | String          | **Definition**                                                         |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | Role type. Use commas (,) to separate multiple types.                  |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | **Constraints**                                                        |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | Select at least one node type from **ess**, **ess-cold**, and **all**. |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | **Range**                                                              |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | -  **ess**: data node                                                  |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | -  **ess-cold**: cold data node                                        |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | -  **ess-client**: client node                                         |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | -  **ess-master**: master node                                         |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | -  **all**: all nodes                                                  |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | **Default Value**                                                      |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | N/A                                                                    |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Restart a node.

.. code-block:: text

   POST https://{Endpoint}/v2.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/rolling_restart

   {
     "type" : "role",
     "value" : "ess"
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
