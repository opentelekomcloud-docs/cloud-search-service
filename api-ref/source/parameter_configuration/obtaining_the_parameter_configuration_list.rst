:original_name: css_03_0118.html

.. _css_03_0118:

Obtaining the Parameter Configuration List
==========================================

Function
--------

This API is used to obtain the parameter configuration list of the current cluster.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ymls/template

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to query.                                                                                             |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                           |
   +=======================+=======================+=======================================================================================================================================================+
   | configurations        | Object                | Cluster parameter configuration list. The **key** value in the object is subject to the actual situation. The **value** has the following attributes: |
   |                       |                       |                                                                                                                                                       |
   |                       |                       | -  **id**: parameter ID.                                                                                                                              |
   |                       |                       | -  **key**: parameter name.                                                                                                                           |
   |                       |                       | -  **value**: parameter value.                                                                                                                        |
   |                       |                       | -  **defaultValue**: parameter default value.                                                                                                         |
   |                       |                       | -  **regex**: parameter constraint.                                                                                                                   |
   |                       |                       | -  **desc**: parameter description.                                                                                                                   |
   |                       |                       | -  **type**: parameter type description.                                                                                                              |
   |                       |                       | -  **moduleDesc**: parameter function description.                                                                                                    |
   |                       |                       | -  **modifyEnable**: whether a parameter can be modified. **true**: The value can be changed. **false**: The value cannot be changed.                 |
   |                       |                       | -  **enableValue**: parameter value that can be changed.                                                                                              |
   |                       |                       | -  **fileName**: name of the file where parameters exist. The default value is **elasticsearch.yml**.                                                 |
   |                       |                       | -  **version**: version information.                                                                                                                  |
   |                       |                       | -  **descENG**: parameter description.                                                                                                                |
   |                       |                       | -  **moduleDescENG**: parameter function description.                                                                                                 |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

None

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "configurations" : {
       "http.cors.allow-credentials" : {
         "id" : "b462d13c-294b-4e0f-91d3-58be2ad02b99",
         "key" : "http.cors.allow-credentials",
         "value" : "false",
         "defaultValue" : "false",
         "regex" : "^(true|false)$",
         "desc" : "Indicates whether to return **Access-Control-Allow-Credentials** in the header during cross-domain access. The value is of the Boolean type and can be **true** or **false**.",
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
