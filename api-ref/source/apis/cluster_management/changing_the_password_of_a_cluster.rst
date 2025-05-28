:original_name: ResetPassword.html

.. _ResetPassword:

Changing the Password of a Cluster
==================================

Function
--------

This API is used to change the password of a cluster.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/password/reset

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose password you want to change.                                                                             |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                |
   +=================+=================+=================+============================================================================================================================================================================+
   | newpassword     | Yes             | String          | Password of the cluster user **admin** in security mode. This API is available only if **authorityEnable** is set to **true**.                                             |
   |                 |                 |                 |                                                                                                                                                                            |
   |                 |                 |                 | -  Must contain 8 to 32 characters.                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                            |
   |                 |                 |                 | -  Must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters (``~!@#$%^&*()-_=+\|[{}];:,<.>/?``). |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Change the administrator password of the current cluster.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/password/reset

   {
     "newpassword" : "xxxxxx"
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
