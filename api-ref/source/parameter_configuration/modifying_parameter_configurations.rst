:original_name: css_03_0116.html

.. _css_03_0116:

Modifying Parameter Configurations
==================================

Function
--------

This API is used to modify parameter configurations.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/ymls/update

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to modify the parameter configurations             |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------+-----------+--------------------------------------------------------------------------+--------------------------------+
   | Parameter | Mandatory | Type                                                                     | Description                    |
   +===========+===========+==========================================================================+================================+
   | edit      | Yes       | :ref:`UpdateYmlsReqEdit <css_03_0116__request_updateymlsreqedit>` object | Configuration file information |
   +-----------+-----------+--------------------------------------------------------------------------+--------------------------------+

.. _css_03_0116__request_updateymlsreqedit:

.. table:: **Table 3** UpdateYmlsReqEdit

   +-----------------+-----------------+--------------------------------------------------------------------------------------+---------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                                 | Description                                                         |
   +=================+=================+======================================================================================+=====================================================================+
   | modify          | Yes             | :ref:`UpdateYmlsReqEditModify <css_03_0116__request_updateymlsreqeditmodify>` object | Operations performed on parameter configurations. The value can be: |
   |                 |                 |                                                                                      |                                                                     |
   |                 |                 |                                                                                      | -  **modify**                                                       |
   |                 |                 |                                                                                      | -  **delete**                                                       |
   |                 |                 |                                                                                      | -  **reset**                                                        |
   +-----------------+-----------------+--------------------------------------------------------------------------------------+---------------------------------------------------------------------+

.. _css_03_0116__request_updateymlsreqeditmodify:

.. table:: **Table 4** UpdateYmlsReqEditModify

   +-------------------+-----------+--------+------------------------------------------------------------------------------+
   | Parameter         | Mandatory | Type   | Description                                                                  |
   +===================+===========+========+==============================================================================+
   | elasticsearch.yml | Yes       | Object | Parameter configuration list. The value is the JSON data you want to modify. |
   +-------------------+-----------+--------+------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 5** Response body parameter

   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                 |
   +=======================+=======================+=============================================================================================+
   | acknowledged          | Boolean               | Indicates whether the modification is successful.                                           |
   |                       |                       |                                                                                             |
   |                       |                       | -  **true**: The modification is successful.                                                |
   |                       |                       | -  **false**: The modification failed.                                                      |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------+
   | externalMessage       | String                | Error message. If **acknowledged** is set to **true**, **null** is returned for this field. |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------+
   | httpErrorResponse     | String                | HTTP error information. The default value is **null**.                                      |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------+

Request Example
---------------

.. code-block::

   {
     "edit" : {
       "modify" : {
         "elasticsearch.yml" : {
           "thread_pool.force_merge.size" : 1
         }
       }
     }
   }

Response Example
----------------

**Status code: 200**

The request is processed successfully.

.. code-block::

   {
     "acknowledged" : true,
     "externalMessage" : null,
     "httpErrorResponse" : null
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
