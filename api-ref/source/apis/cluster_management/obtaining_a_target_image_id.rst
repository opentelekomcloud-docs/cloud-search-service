:original_name: ListImages.html

.. _ListImages:

Obtaining a Target Image ID
===========================

Function
--------

This API is used to obtain the ID of an image that can be upgraded in the current cluster.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/target/{upgrade_type}/images

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | ID of the cluster to be upgraded.                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | upgrade_type    | Yes             | String          | Version type:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **same**: upgrade to the same version.                                                                                        |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **cross**: upgrade to a different version.                                                                                    |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **cross-engine**: cross-engine upgrade.                                                                                       |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+
   | Parameter               | Type                                                                                         | Description                                          |
   +=========================+==============================================================================================+======================================================+
   | needUploadUpgradePlugin | Boolean                                                                                      | Whether to upload the plug-in of the target version. |
   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+
   | imageInfoList           | Array of :ref:`GetTargetImageIdDetail <listimages__response_gettargetimageiddetail>` objects | Image details.                                       |
   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+

.. _listimages__response_gettargetimageiddetail:

.. table:: **Table 3** GetTargetImageIdDetail

   ================ ======= ======================================
   Parameter        Type    Description
   ================ ======= ======================================
   id               String  ID of an image that can be upgraded.
   displayName      String  Name of an image that can be upgraded.
   imageDesc        String  Image description.
   datastoreType    String  Image engine type.
   datastoreVersion String  Image engine version.
   priority         Integer Priority.
   ================ ======= ======================================

Example Requests
----------------

.. code-block:: text

   GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/target/cross/images

   {
     "needUploadUpgradePlugin" : false,
     "imageInfoList" : [ ]
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "needUploadUpgradePlugin" : false,
     "imageInfoList" : [ ]
   }

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                     |
+===================================+=================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                |
|                                   |                                                                                                                                                                 |
|                                   | The client should not repeat the request without modifications.                                                                                                 |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | Request rejected.                                                                                                                                               |
|                                   |                                                                                                                                                                 |
|                                   | The server has received the request and understood it, but the server refuses to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
