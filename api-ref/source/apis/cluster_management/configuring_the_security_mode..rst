:original_name: ChangeMode.html

.. _ChangeMode:

Configuring the Security Mode.
==============================

Function
--------

This API is used to configure the security mode of a cluster.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/mode/change

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | Cluster ID.                                                                                                                      |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                        |
   +=================+=================+=================+====================================+
   | authorityEnable | Yes             | Boolean         | Security mode. Its value can be:   |
   |                 |                 |                 |                                    |
   |                 |                 |                 | -  true: enabled                   |
   |                 |                 |                 |                                    |
   |                 |                 |                 | -  false: disabled                 |
   |                 |                 |                 |                                    |
   |                 |                 |                 |    Default value: true             |
   +-----------------+-----------------+-----------------+------------------------------------+
   | adminPwd        | No              | String          | Cluster password in security mode. |
   +-----------------+-----------------+-----------------+------------------------------------+
   | httpsEnable     | Yes             | Boolean         | Enable HTTPS. Its value can be:    |
   |                 |                 |                 |                                    |
   |                 |                 |                 | -  true: enabled                   |
   |                 |                 |                 |                                    |
   |                 |                 |                 | -  false: disabled                 |
   |                 |                 |                 |                                    |
   |                 |                 |                 |    Default value: true             |
   +-----------------+-----------------+-----------------+------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Change the security mode of the current cluster.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/mode/change

   {
     "authorityEnable" : true,
     "adminPwd" : "admin@1234",
     "httpsEnable" : true
   }

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
