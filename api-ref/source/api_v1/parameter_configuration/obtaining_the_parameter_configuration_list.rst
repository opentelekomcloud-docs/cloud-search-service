:original_name: ListYmls.html

.. _ListYmls:

Obtaining the Parameter Configuration List
==========================================

Function
--------

This API is used to obtain the parameter settings list of an Elasticsearch or OpenSearch cluster in the form of a YAML file. The core configuration information of an Elasticsearch cluster is stored in the **elasticsearch.yml** and **kibana.yml** files, while that of an OpenSearch cluster is stored in the **opensearch.yml** and **opensearch_dashboards.yml** files.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ymls/template

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                         |
   +=================+=================+=================+=====================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Range**                                                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                             |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default Value**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | ID of the cluster to be queried. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Range**                                                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                       |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default Value**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                       |
   +=================+=================+=================+===================================================================================+
   | fileName        | No              | String          | **Definition**                                                                    |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | Name of the file to be modified.                                                  |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | **Constraints**                                                                   |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | N/A                                                                               |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | **Range**                                                                         |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | -  **elasticsearch.yml**: Modify the Elasticsearch/OpenSearch configuration file. |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | -  **kibana.yml**: Modify the Kibana/Dashboard configuration file.                |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | **Default Value**                                                                 |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | N/A                                                                               |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------+
   | inst_type       | No              | String          | **Definition**                                                                    |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | Type of the node to be modified.                                                  |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | **Constraints**                                                                   |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | N/A                                                                               |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | **Range**                                                                         |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | N/A                                                                               |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | **Default Value**                                                                 |
   |                 |                 |                 |                                                                                   |
   |                 |                 |                 | N/A                                                                               |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                 |
   +=======================+=======================+=============================================================================================================================================================+
   | configurations        | Object                | **Definition**                                                                                                                                              |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | Cluster parameter configuration list.                                                                                                                       |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | The **key** values in this object depend on the actual query result. Each **value** contains the following attributes:                                      |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **id**: parameter ID.                                                                                                                                    |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **key**: parameter name.                                                                                                                                 |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **value**: parameter value.                                                                                                                              |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **defaultValue**: parameter default value.                                                                                                               |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **regex**: parameter constraints.                                                                                                                        |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **desc**: parameter description in Chinese.                                                                                                              |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **type**: parameter type.                                                                                                                                |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **moduleDesc**: parameter function description in Chinese.                                                                                               |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **modifyEnable**: whether the parameter can be modified. **True** indicates it can be modified; **false** indicates it cannot.                           |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **enableValue**: supported values for modification.                                                                                                      |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **fileName**: name of the file where the parameter is located, such as **elasticsearch.yml** or **kibana.yml**. OpenSearch clusters also use this field. |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **version**: version information.                                                                                                                        |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **unSupportVersion**: unsupported versions.                                                                                                              |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **descENG**: parameter description in English.                                                                                                           |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **moduleDescENG**: parameter function description in English.                                                                                            |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **instType**: node type.                                                                                                                                 |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **moduleDescPTBR**: parameter function description in Portuguese (Brazil).                                                                               |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **descPTBR**: parameter description in Portuguese (Brazil).                                                                                              |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **moduleDescESUS**: parameter function description in Spanish (Latin America).                                                                           |
   |                       |                       |                                                                                                                                                             |
   |                       |                       | -  **descESUS**: parameter description in Spanish (Latin America).                                                                                          |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

Obtain the parameter settings of a cluster in a YAML file.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/ymls/template

Example Responses
-----------------

**Status code: 200**

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
         "unSupportVersion" : null,
         "instType" : null,
         "descENG" : "Whether to return the Access-Control-Allow-Credentials of the header during cross-domain access. The value is a Boolean value and the options are true and false.",
         "moduleDescENG" : "Cross-domain Access",
         "descPTBR" : null,
         "moduleDescPTBR" : null,
         "descESUS" : null,
         "moduleDescESUS" : null
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

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
