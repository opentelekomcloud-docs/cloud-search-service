:original_name: css_03_0091.html

.. _css_03_0091:

Configuring the Security Mode.
==============================

Function
--------

This API is used to configure the security mode of a cluster.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/mode/change

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | Cluster ID.                                                                        |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+----------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                            |
   +=================+=================+=================+========================================+
   | authorityEnable | Yes             | Boolean         | Security mode. Its value can be:       |
   |                 |                 |                 |                                        |
   |                 |                 |                 | -  true: enabled                       |
   |                 |                 |                 | -  false: disabled Default value: true |
   +-----------------+-----------------+-----------------+----------------------------------------+
   | adminPwd        | No              | String          | Cluster password in security mode.     |
   +-----------------+-----------------+-----------------+----------------------------------------+
   | httpsEnable     | Yes             | Boolean         | Enable HTTPS. Its value can be:        |
   |                 |                 |                 |                                        |
   |                 |                 |                 | -  true: enabled                       |
   |                 |                 |                 | -  false: disabled Default value: true |
   +-----------------+-----------------+-----------------+----------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/mode/change

   {
     "authorityEnable" : true,
     "adminPwd" : "xxxx1234",
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
