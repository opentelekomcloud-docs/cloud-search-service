:original_name: UpdateYmls.html

.. _UpdateYmls:

Modifying Cluster Parameters
============================

Function
--------

This API is used to modify the parameter settings of a cluster. Before calling this API, obtain the parameter configuration list, check the parameter settings, and modify them as required.

.. note::

   Set the values of any custom parameters to those that are supported by Elasticsearch. Otherwise, the cluster will fail to be restarted. Exercise caution when performing this operation.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/ymls/update

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Project ID of the account.                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | ID of the cluster whose parameter settings you want to be modify. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Cluster ID.                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-------------------------------------------------------------------------+---------------------------------+
   | Parameter       | Mandatory       | Type                                                                    | Description                     |
   +=================+=================+=========================================================================+=================================+
   | edit            | Yes             | :ref:`UpdateYmlsReqEdit <updateymls__request_updateymlsreqedit>` object | **Definition**:                 |
   |                 |                 |                                                                         |                                 |
   |                 |                 |                                                                         | Configuration file information. |
   |                 |                 |                                                                         |                                 |
   |                 |                 |                                                                         | **Constraints**:                |
   |                 |                 |                                                                         |                                 |
   |                 |                 |                                                                         | N/A                             |
   +-----------------+-----------------+-------------------------------------------------------------------------+---------------------------------+

.. _updateymls__request_updateymlsreqedit:

.. table:: **Table 3** UpdateYmlsReqEdit

   +-----------------+-----------------+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                                | Description                                                                                                    |
   +=================+=================+=====================================================================================+================================================================================================================+
   | modify          | No              | :ref:`UpdateYmlsReqEditModify <updateymls__request_updateymlsreqeditmodify>` object | **Definition**:                                                                                                |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | Modify parameter settings.                                                                                     |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | **Constraints**:                                                                                               |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  modify, delete, and reset: at least one of them will take effect, and each operation can be used only once. |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  Cannot perform multiple operations on the same parameter at the same time.                                  |
   +-----------------+-----------------+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   | delete          | No              | :ref:`UpdateYmlsReqEditModify <updateymls__request_updateymlsreqeditmodify>` object | **Definition**:                                                                                                |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | Delete custom parameter settings.                                                                              |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | **Constraints**:                                                                                               |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  Irrelevant to the input parameter value.                                                                    |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  modify, delete, and reset: at least one of them will take effect, and each operation can be used only once. |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  Cannot perform multiple operations on the same parameter at the same time.                                  |
   +-----------------+-----------------+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+
   | reset           | No              | :ref:`UpdateYmlsReqEditModify <updateymls__request_updateymlsreqeditmodify>` object | **Definition**:                                                                                                |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | Reset parameter settings.                                                                                      |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | **Constraints**:                                                                                               |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  Irrelevant to the input parameter value.                                                                    |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  Custom parameters cannot be reset.                                                                          |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  modify, delete, and reset: at least one of them will take effect, and each operation can be used only once. |
   |                 |                 |                                                                                     |                                                                                                                |
   |                 |                 |                                                                                     | -  Cannot perform multiple operations on the same parameter at the same time.                                  |
   +-----------------+-----------------+-------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------+

.. _updateymls__request_updateymlsreqeditmodify:

.. table:: **Table 4** UpdateYmlsReqEditModify

   +-------------------+-----------------+-----------------+--------------------------------------------------------------------------+
   | Parameter         | Mandatory       | Type            | Description                                                              |
   +===================+=================+=================+==========================================================================+
   | elasticsearch.yml | Yes             | Object          | **Definition**:                                                          |
   |                   |                 |                 |                                                                          |
   |                   |                 |                 | Parameter configuration list. The value is the JSON data to be modified. |
   |                   |                 |                 |                                                                          |
   |                   |                 |                 | **Constraints**:                                                         |
   |                   |                 |                 |                                                                          |
   |                   |                 |                 | N/A                                                                      |
   |                   |                 |                 |                                                                          |
   |                   |                 |                 | **Value range**:                                                         |
   |                   |                 |                 |                                                                          |
   |                   |                 |                 | N/A                                                                      |
   |                   |                 |                 |                                                                          |
   |                   |                 |                 | **Default value**:                                                       |
   |                   |                 |                 |                                                                          |
   |                   |                 |                 | N/A                                                                      |
   +-------------------+-----------------+-----------------+--------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 5** Response body parameters

   +-----------------------+-----------------------+-------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                   |
   +=======================+=======================+===============================================================================+
   | acknowledged          | Boolean               | **Definition**:                                                               |
   |                       |                       |                                                                               |
   |                       |                       | Parameter settings modified successfully or not.                              |
   |                       |                       |                                                                               |
   |                       |                       | **Value range**:                                                              |
   |                       |                       |                                                                               |
   |                       |                       | -  **true**: The modification is successful.                                  |
   |                       |                       |                                                                               |
   |                       |                       | -  **false**: The modification fails.                                         |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------+
   | externalMessage       | String                | **Definition**:                                                               |
   |                       |                       |                                                                               |
   |                       |                       | Error description.                                                            |
   |                       |                       |                                                                               |
   |                       |                       | **Value range**:                                                              |
   |                       |                       |                                                                               |
   |                       |                       | If **acknowledged** was set to **true**, **null** is returned for this field. |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------+
   | httpErrorResponse     | String                | **Definition**:                                                               |
   |                       |                       |                                                                               |
   |                       |                       | HTTP error information. The default value is null.                            |
   |                       |                       |                                                                               |
   |                       |                       | **Value range**:                                                              |
   |                       |                       |                                                                               |
   |                       |                       | N/A                                                                           |
   +-----------------------+-----------------------+-------------------------------------------------------------------------------+

Example Requests
----------------

Modify parameter settings.

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

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "acknowledged" : true
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
