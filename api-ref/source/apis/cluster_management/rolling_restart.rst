:original_name: RollingRestart.html

.. _RollingRestart:

Rolling Restart
===============

Function
--------

This API is used to restart nodes one by one, which requires a long time when the nodes have a large number of indexes.

URI
---

POST /v2.0/{project_id}/clusters/{cluster_id}/rolling_restart

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

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                    |
   +=================+=================+=================+================================================================================================================================================+
   | type            | Yes             | String          | Operation role. Its type can only be **role**.                                                                                                 |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+
   | value           | Yes             | String          | Instance type. (At least one data node is required when you configure instance types.) Use commas (,) to separate multiple types. For example: |
   |                 |                 |                 |                                                                                                                                                |
   |                 |                 |                 | -  **ess-master** indicates a master node.                                                                                                     |
   |                 |                 |                 |                                                                                                                                                |
   |                 |                 |                 | -  **ess-client** indicates a client node.                                                                                                     |
   |                 |                 |                 |                                                                                                                                                |
   |                 |                 |                 | -  **ess-cold** indicates a cold data node.                                                                                                    |
   |                 |                 |                 |                                                                                                                                                |
   |                 |                 |                 | -  **ess** indicates a data node.                                                                                                              |
   |                 |                 |                 |                                                                                                                                                |
   |                 |                 |                 | -  **all** indicates all nodes.                                                                                                                |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Restart a node.

.. code-block:: text

   POST /v2.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/rolling_restart

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
