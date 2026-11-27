:original_name: UpdateYmls.html

.. _UpdateYmls:

Modifying Cluster Parameters
============================

Function
--------

The core configuration information of an Elasticsearch cluster is stored in the **elasticsearch.yml** and **kibana.yml** files, while that of an OpenSearch cluster is stored in the **opensearch.yml** and **opensearch_dashboards.yml** files. You can modify a cluster's parameter configuration files for purposes like accelerating queries, modifying cross-domain access configurations, adjusting internal cache sizes, or managing background task queues.

Elasticsearch or OpenSearch supports configuring the SAML authentication metadata descriptor file **descriptor.xml**. In SAML 2.0, SSO configuration information (such as keys and URL endpoints) is typically stored in an XML descriptor file.

Before calling this API, you are advised to call the :ref:`Obtaining the Parameter Configuration List <listymls>` API to confirm the cluster's parameter configuration, so that you can modify parameters as needed.

Constraints
-----------

When the parameter type **UpdateYmlsReqEditModify** is **elasticsearch.yml**, custom parameters must be parameters supported by Elasticsearch or OpenSearch. Otherwise, the cluster restart will fail.

When the parameter type **UpdateYmlsReqEditModify** is **kibana.yml**, custom parameters must be parameters supported by Kibana or Dashboards. Otherwise, the Kibana or Dashboards process restart will fail.

When the parameter type **UpdateYmlsReqEditModify** is **system.config**, a **descriptor.xml** file is generated in the Elasticsearch or OpenSearch **config** directory, and all nodes load this file when the cluster is manually restarted.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/ymls/update

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                           |
   +=================+=================+=================+=======================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                      |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Constraints**                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Range**                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                                               |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Default Value**                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | ID of the cluster whose parameter configuration is to be modified. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Constraints**                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Range**                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | **Default Value**                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                       |
   |                 |                 |                 | N/A                                                                                                                                                                   |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                    | Description                                                                                         |
   +=================+=================+=========================================================================+=====================================================================================================+
   | edit            | Yes             | :ref:`UpdateYmlsReqEdit <updateymls__request_updateymlsreqedit>` object | **Definition**:                                                                                     |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | Configuration file information.                                                                     |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | **Constraints**:                                                                                    |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | N/A                                                                                                 |
   +-----------------+-----------------+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+
   | inst_type       | No              | String                                                                  | **Definition**:                                                                                     |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | Node type.                                                                                          |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | **Constraints**:                                                                                    |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | Different node types used in KooSearch clusters. Other types of clusters do not use this parameter. |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | **Value range**:                                                                                    |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | -  kos: KooSearch central control node                                                              |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | -  kos-doc: KooSearch document parsing node                                                         |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | **Default value**:                                                                                  |
   |                 |                 |                                                                         |                                                                                                     |
   |                 |                 |                                                                         | N/A                                                                                                 |
   +-----------------+-----------------+-------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------+

.. _updateymls__request_updateymlsreqedit:

.. table:: **Table 3** UpdateYmlsReqEdit

   +-----------------+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                                | Description                                                                                                              |
   +=================+=================+=====================================================================================+==========================================================================================================================+
   | modify          | No              | :ref:`UpdateYmlsReqEditModify <updateymls__request_updateymlsreqeditmodify>` object | **Definition**:                                                                                                          |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | Modify parameter settings.                                                                                               |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | **Constraints**:                                                                                                         |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  modify, delete, and reset: at least one of them will take effect, and each operation can only be used once each time. |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  Cannot perform multiple operations on the same parameter at the same time.                                            |
   +-----------------+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
   | delete          | No              | :ref:`UpdateYmlsReqEditModify <updateymls__request_updateymlsreqeditmodify>` object | **Definition**:                                                                                                          |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | Delete custom parameter settings.                                                                                        |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | **Constraints**:                                                                                                         |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  Irrelevant to the input parameter value.                                                                              |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  modify, delete, and reset: at least one of them will take effect, and each operation can be used only once.           |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  Cannot perform multiple operations on the same parameter at the same time.                                            |
   +-----------------+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+
   | reset           | No              | :ref:`UpdateYmlsReqEditModify <updateymls__request_updateymlsreqeditmodify>` object | **Definition**:                                                                                                          |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | Reset parameter settings.                                                                                                |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | **Constraints**:                                                                                                         |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  Irrelevant to the input parameter value.                                                                              |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  Custom parameters cannot be reset.                                                                                    |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  modify, delete, and reset: at least one of them will take effect, and each operation can be used only once.           |
   |                 |                 |                                                                                     |                                                                                                                          |
   |                 |                 |                                                                                     | -  Cannot perform multiple operations on the same parameter at the same time.                                            |
   +-----------------+-----------------+-------------------------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------+

.. _updateymls__request_updateymlsreqeditmodify:

.. table:: **Table 4** UpdateYmlsReqEditModify

   +-------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter         | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                                                        |
   +===================+=================+=================+====================================================================================================================================================================================================================================================================================================================================================================================================+
   | elasticsearch.yml | No              | Object          | **Definition**                                                                                                                                                                                                                                                                                                                                                                                     |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | Parameter configuration list, where the value is the JSON data to be modified. The key is the configuration parameter name supported by Elasticsearch/OpenSearch, and the value is the corresponding configuration parameter value. When modifying parameters of an Elasticsearch cluster (**elasticsearch.yml**) or an OpenSearch cluster (**opensearch.yml**), enter **elasticsearch.yml** here. |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | **Constraints**                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | Custom parameters must be set to parameters supported by Elasticsearch or OpenSearch. Otherwise, the cluster restart will fail. Exercise caution when performing this operation.                                                                                                                                                                                                                   |
   +-------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | kibana.yml        | No              | Object          | **Definition**                                                                                                                                                                                                                                                                                                                                                                                     |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | Parameter configuration list, where the value is the JSON data to be modified. The key is the configuration parameter name supported by Kibana or Dashboards, and the value is the corresponding configuration parameter value. When modifying parameters of an Elasticsearch cluster (**kibana.yml**) or an OpenSearch cluster (**opensearch_dashboards.yml**), enter **kibana.yml** here.        |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | **Constraints**                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | Custom parameters must be set to parameters supported by Kibana or Dashboards. Otherwise, the Kibana or Dashboards process restart will fail. Proceed with caution.                                                                                                                                                                                                                                |
   +-------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | system.config     | No              | Object          | **Definition**                                                                                                                                                                                                                                                                                                                                                                                     |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | Parameter configuration list, where the value is the JSON data to be modified. When **system.config** of the cluster is modified, a **descriptor.xml** file is generated in the **config** directory of the Elasticsearch or OpenSearch cluster.                                                                                                                                                   |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | **Constraints**                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | In the JSON data, the key is **descriptor.xml**. The maximum length of the value is 100 KB (102,400 bytes/characters, including line breaks).                                                                                                                                                                                                                                                      |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                                                                                                    |
   |                   |                 |                 | Modifying **system.config** is supported only for Elasticsearch clusters with version 7.10.2 or OpenSearch clusters with version 2.19.0.                                                                                                                                                                                                                                                           |
   +-------------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 5** Response body parameters

   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                    |
   +=======================+=======================+================================================================================+
   | acknowledged          | Boolean               | **Definition**:                                                                |
   |                       |                       |                                                                                |
   |                       |                       | Parameter settings modified successfully or not.                               |
   |                       |                       |                                                                                |
   |                       |                       | **Value range**:                                                               |
   |                       |                       |                                                                                |
   |                       |                       | -  **true**: The modification is successful.                                   |
   |                       |                       |                                                                                |
   |                       |                       | -  **false**: The modification fails.                                          |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | externalMessage       | String                | **Definition**                                                                 |
   |                       |                       |                                                                                |
   |                       |                       | Error message. When **acknowledged** is **true**, this field returns **null**. |
   |                       |                       |                                                                                |
   |                       |                       | **Range**                                                                      |
   |                       |                       |                                                                                |
   |                       |                       | N/A                                                                            |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+
   | httpErrorResponse     | String                | **Definition**:                                                                |
   |                       |                       |                                                                                |
   |                       |                       | HTTP error information. The default value is null.                             |
   |                       |                       |                                                                                |
   |                       |                       | **Value range**:                                                               |
   |                       |                       |                                                                                |
   |                       |                       | N/A                                                                            |
   +-----------------------+-----------------------+--------------------------------------------------------------------------------+

Example Requests
----------------

-  Modify parameter settings.

   .. code-block:: text

      POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ymls/update

      {
        "edit" : {
          "modify" : {
            "elasticsearch.yml" : {
              "thread_pool.force_merge.size" : 1
            }
          }
        }
      }

-  Delete custom parameter settings.

   .. code-block:: text

      POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ymls/update

      {
        "edit" : {
          "delete" : {
            "elasticsearch.yml" : {
              "thread_pool.force_merge.size" : 1
            }
          }
        }
      }

-  Reset parameter settings

   .. code-block:: text

      POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ymls/update

      {
        "edit" : {
          "reset" : {
            "elasticsearch.yml" : {
              "http.cors.allow-credentials" : "false"
            }
          }
        }
      }

Example Responses
-----------------

**Status code: 200**

.. code-block::

   {
     "acknowledged" : true,
     "externalMessage" : null,
     "httpErrorResponse" : null
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
