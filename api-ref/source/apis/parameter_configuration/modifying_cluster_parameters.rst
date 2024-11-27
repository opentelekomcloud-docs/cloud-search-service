:original_name: UpdateYmls.html

.. _UpdateYmls:

Modifying Cluster Parameters
============================

Function
--------

This API is used to modify the parameter settings of a cluster.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/ymls/update

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose parameter settings you want to be modify.                                                                |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+-------------------------------------------------------------------------+---------------------------------+
   | Parameter | Mandatory | Type                                                                    | Description                     |
   +===========+===========+=========================================================================+=================================+
   | edit      | Yes       | :ref:`UpdateYmlsReqEdit <updateymls__request_updateymlsreqedit>` object | Configuration file information. |
   +-----------+-----------+-------------------------------------------------------------------------+---------------------------------+

.. _updateymls__request_updateymlsreqedit:

.. table:: **Table 3** UpdateYmlsReqEdit

   +-----------------+-----------------+-------------------------------------------------------------------------------------+-------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                                | Description                               |
   +=================+=================+=====================================================================================+===========================================+
   | modify          | Yes             | :ref:`UpdateYmlsReqEditModify <updateymls__request_updateymlsreqeditmodify>` object | Operations on the configuration file.     |
   |                 |                 |                                                                                     |                                           |
   |                 |                 |                                                                                     | -  **modify**: Modify parameter settings. |
   |                 |                 |                                                                                     |                                           |
   |                 |                 |                                                                                     | -  **delete**: Delete parameter settings. |
   |                 |                 |                                                                                     |                                           |
   |                 |                 |                                                                                     | -  **reset**: Reset parameter settings.   |
   +-----------------+-----------------+-------------------------------------------------------------------------------------+-------------------------------------------+

.. _updateymls__request_updateymlsreqeditmodify:

.. table:: **Table 4** UpdateYmlsReqEditModify

   +-------------------+-----------+--------+------------------------------------------------------------------------------+
   | Parameter         | Mandatory | Type   | Description                                                                  |
   +===================+===========+========+==============================================================================+
   | elasticsearch.yml | Yes       | Object | Parameter configuration list. The value is the JSON data you want to modify. |
   +-------------------+-----------+--------+------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 5** Response body parameters

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                  |
   +=======================+=======================+==============================================================================================+
   | acknowledged          | Boolean               | Whether the modification is successful.                                                      |
   |                       |                       |                                                                                              |
   |                       |                       | -  **true**: The modification succeeded.                                                     |
   |                       |                       |                                                                                              |
   |                       |                       | -  **false**: The modification failed.                                                       |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------+
   | externalMessage       | String                | Error message. If **acknowledged** was set to **true**, **null** is returned for this field. |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------+
   | httpErrorResponse     | String                | HTTP error information. The default value is **null**.                                       |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------+

Example Requests
----------------

Modify parameter settings.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ymls/update

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
