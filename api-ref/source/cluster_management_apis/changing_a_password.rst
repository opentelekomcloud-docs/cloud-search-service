:original_name: ResetPassword.html

.. _ResetPassword:

Changing a Password
===================

Function
--------

This API is used to change the password of a cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0137>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/password/reset

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                         |
   +============+===========+========+=====================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose password you want to change.                                                                |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                  |
   +=================+=================+=================+==============================================================================================================================================================================+
   | newpassword     | Yes             | String          | Password of the cluster user **admin** in security mode. This API is available only when **authorityEnable** is set to **true**.                                             |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | -  The value can contain 8 to 32 characters.                                                                                                                                 |
   |                 |                 |                 | -  The value must contain at least 3 of the following character types: uppercase letters, lowercase letters, numbers, and special characters\ ``~!@#$%&*()-_=|[{}];:,<.>/?`` |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

Change the administrator password of the current cluster.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/password/reset

   {
     "newpassword" : "xxxxxx"
   }

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                   |
+===================================+===============================================================================================================================================================================+
| 200                               | The request is processed.                                                                                                                                                     |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                              |
|                                   |                                                                                                                                                                               |
|                                   | Modify the request instead of retrying.                                                                                                                                       |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                                                            |
|                                   |                                                                                                                                                                               |
|                                   | This status code indicates that the resource the client is attempting to create already exists, or that the update operation requested cannot be completed due to a conflict. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not satisfy one of the preconditions set by the requester in the request.                                                                                      |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

For details, see :ref:`Error Code <css_03_0076>`.
