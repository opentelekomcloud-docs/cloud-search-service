:original_name: css_03_0118.html

.. _css_03_0118:

Obtaining the Parameter Configuration List
==========================================

Function
--------

This API is used to obtain the parameter configuration list of the current cluster.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ymls/template

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be queried                                                    |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameter

   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                                       |
   +=======================+=======================+===================================================================================================================================================================================+
   | configurations        | Object                | Cluster parameter configuration list. The **key** value in the object is subject to the actual situation. The **value** has the following attributes:                             |
   |                       |                       |                                                                                                                                                                                   |
   |                       |                       | -  **id**: parameter ID.                                                                                                                                                          |
   |                       |                       | -  **key**: parameter name.                                                                                                                                                       |
   |                       |                       | -  **value**: parameter value.                                                                                                                                                    |
   |                       |                       | -  **defaultValue**: parameter default value.                                                                                                                                     |
   |                       |                       | -  **regex**: parameter constraint.                                                                                                                                               |
   |                       |                       | -  **desc**: parameter description in Chinese.                                                                                                                                    |
   |                       |                       | -  **type**: parameter type description.                                                                                                                                          |
   |                       |                       | -  **moduleDesc**: parameter function description in Chinese.                                                                                                                     |
   |                       |                       | -  **modifyEnable**: indicates whether a parameter can be modified. The value can be **true** (parameter value can be changed) and **false** (parameter value cannot be changed). |
   |                       |                       | -  **enableValue**: parameter value that can be changed.                                                                                                                          |
   |                       |                       | -  **fileName**: name of the file where parameters exist. The default value is **elasticsearch.yml**.                                                                             |
   |                       |                       | -  **version**: version information.                                                                                                                                              |
   |                       |                       | -  **descENG**: parameter description in English.                                                                                                                                 |
   |                       |                       | -  **moduleDescENG**: parameter function description in English.                                                                                                                  |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Example
---------------

None

Response Example
----------------

**Status code: 200**

The request is processed successfully.

.. code-block::

   {
     "configurations" : {
       "http.cors.allow-credentials" : {
         "id" : "b462d13c-294b-4e0f-91d3-58be2ad02b99",
         "key" : "http.cors.allow-credentials",
         "value" : "false",
         "defaultValue" : "false",
         "regex" : "^(true|false)$",
         "desc" : "Indicates whether to return Access-Control-Allow-Credentials in the header during cross-domain access. The value is of the Boolean type and can be true or false.
         "type" : "Boolean",
         "moduleDesc" : "Cross-domain access",
         "modifyEnable" : "true",
         "enableValue" : "true,false",
         "fileName" : "elasticsearch.yml",
         "version" : null,
         "descENG" : "Whether to return the Access-Control-Allow-Credentials of the header during cross-domain access. The value is a Boolean value and the options are true and false.",
         "moduleDescENG" : "Cross-domain Access"
       }
     }
   }

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
