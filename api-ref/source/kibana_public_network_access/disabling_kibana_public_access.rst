:original_name: css_03_0121.html

.. _css_03_0121:

Disabling Kibana Public Access
==============================

Function
--------

This API is used to disable public network access to Kibana.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/publickibana/close

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose Kibana public access you want to disable.                  |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +--------------+-----------+--------------------------------------------------------------------------------------------------------+-------------------------+
   | Parameter    | Mandatory | Type                                                                                                   | Description             |
   +==============+===========+========================================================================================================+=========================+
   | eipSize      | No        | Integer                                                                                                | Bandwidth. Unit: Mbit/s |
   +--------------+-----------+--------------------------------------------------------------------------------------------------------+-------------------------+
   | elbWhiteList | No        | :ref:`StartKibanaPublicReqElbWhitelist <css_03_0121__request_startkibanapublicreqelbwhitelist>` object | ELB whitelist.          |
   +--------------+-----------+--------------------------------------------------------------------------------------------------------+-------------------------+

.. _css_03_0121__request_startkibanapublicreqelbwhitelist:

.. table:: **Table 3** StartKibanaPublicReqElbWhitelist

   +-----------------+-----------------+-----------------+-------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                               |
   +=================+=================+=================+===========================================+
   | enableWhiteList | Yes             | Boolean         | Whether to enable the whitelist function. |
   |                 |                 |                 |                                           |
   |                 |                 |                 | -  **true**: The whitelist is enabled.    |
   |                 |                 |                 | -  **false**: The whitelist is disabled.  |
   +-----------------+-----------------+-----------------+-------------------------------------------+
   | whiteList       | Yes             | String          | Whitelist.                                |
   +-----------------+-----------------+-----------------+-------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

.. code-block:: text

   PUT /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/publickibana/close

   {
     "eipSize" : 5,
     "elbWhiteList" : {
       "enableWhiteList" : true,
       "whiteList" : "192.168.0.xx"
     }
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
