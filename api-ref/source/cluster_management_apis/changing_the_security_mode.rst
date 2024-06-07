:original_name: css_03_0091.html

.. _css_03_0091:

Changing the Security Mode
==========================

Function
--------

This API is used to change the security mode of a cluster.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/mode/change

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to change the security mode                        |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------------+-----------------+-----------------+--------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                            |
   +=================+=================+=================+========================================================+
   | authorityEnable | Yes             | Boolean         | Indicates whether to enable the security mode.         |
   |                 |                 |                 |                                                        |
   |                 |                 |                 | -  **true**: enabled.                                  |
   |                 |                 |                 | -  **false**: disabled. The default value is **true**. |
   +-----------------+-----------------+-----------------+--------------------------------------------------------+
   | adminPwd        | No              | String          | Cluster password in security mode                      |
   +-----------------+-----------------+-----------------+--------------------------------------------------------+
   | httpsEnable     | Yes             | Boolean         | Indicates whether to enable HTTPS. Its value can be:   |
   |                 |                 |                 |                                                        |
   |                 |                 |                 | -  **true**: enabled.                                  |
   |                 |                 |                 | -  **false**: disabled. The default value is **true**. |
   +-----------------+-----------------+-----------------+--------------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/mode/change

   {
     "authorityEnable" : true,
     "adminPwd" : "xxxx1234",
     "httpsEnable" : true
   }

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-----------------------------------------+
| Status Code                       | Description                             |
+===================================+=========================================+
| 200                               | The request is processed successfully.  |
+-----------------------------------+-----------------------------------------+
| 400                               | Invalid request.                        |
|                                   |                                         |
|                                   | Modify the request instead of retrying. |
+-----------------------------------+-----------------------------------------+
| 404                               | The requested resource cannot be found. |
|                                   |                                         |
|                                   | Modify the request instead of retrying. |
+-----------------------------------+-----------------------------------------+
