:original_name: RestartClusterMultiRole.html

.. _RestartClusterMultiRole:

Restarting a Cluster (V2)
=========================

Function
--------

This API is used to restart nodes of all node types or the combination of some node types in the current cluster.

URI
---

POST /v2.0/{project_id}/clusters/{cluster_id}/restart

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to restart.                                                                                           |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================================================================+
   | type            | Yes             | String          | Operation role. Value range:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                                   |
   |                 |                 |                 | -  node                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                   |
   |                 |                 |                 | -  role                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | value           | Yes             | String          | Operation parameter. Parameter description:                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                   |
   |                 |                 |                 | -  If the operation role is **node**, the value is the node ID. You can obtain the ID attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`. |
   |                 |                 |                 |                                                                                                                                                                                   |
   |                 |                 |                 | -  If the operation role is **role**, the value is one or multiple node types (such as ess, ess-master, ess-client, and ess-cold).                                                |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Restart nodes of all or some types in the current cluster.

.. code-block:: text

   POST /v2.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/restart

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
