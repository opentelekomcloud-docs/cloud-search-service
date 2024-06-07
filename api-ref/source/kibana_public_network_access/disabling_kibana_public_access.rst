:original_name: css_03_0121.html

.. _css_03_0121:

Disabling Kibana Public Access
==============================

Function
--------

This API is used to disable Kibana public network access.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/publickibana/close

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to disable Kibana public access                    |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +--------------+-----------+--------------------------------------------------------------------------------------------------------+-------------------------+
   | Parameter    | Mandatory | Type                                                                                                   | Description             |
   +==============+===========+========================================================================================================+=========================+
   | eipSize      | No        | Integer                                                                                                | Bandwidth. Unit: Mbit/s |
   +--------------+-----------+--------------------------------------------------------------------------------------------------------+-------------------------+
   | elbWhiteList | No        | :ref:`StartKibanaPublicReqElbWhitelist <css_03_0121__request_startkibanapublicreqelbwhitelist>` object | ELB whitelist           |
   +--------------+-----------+--------------------------------------------------------------------------------------------------------+-------------------------+

.. _css_03_0121__request_startkibanapublicreqelbwhitelist:

.. table:: **Table 3** StartKibanaPublicReqElbWhitelist

   +-----------------+-----------------+-----------------+--------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                |
   +=================+=================+=================+============================================+
   | enableWhiteList | Yes             | Boolean         | Indicates whether to enable the whitelist. |
   |                 |                 |                 |                                            |
   |                 |                 |                 | -  **true**: The whitelist is enabled.     |
   |                 |                 |                 | -  **false**: The whitelist is disabled.   |
   +-----------------+-----------------+-----------------+--------------------------------------------+
   | whiteList       | Yes             | String          | Whitelist                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

.. code-block:: text

   PUT /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/publickibana/close

   {
     "eipSize" : 5,
     "elbWhiteList" : {
       "enableWhiteList" : true,
       "whiteList" : "192.168.0.xx"
     }
   }

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                         |
+===================================+=====================================================================================================================================================================================+
| 200                               | The request is processed successfully.                                                                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                    |
|                                   |                                                                                                                                                                                     |
|                                   | Modify the request instead of retrying.                                                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                                                                  |
|                                   |                                                                                                                                                                                     |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request fails to be processed because of the update of the conflict request. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
