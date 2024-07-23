:original_name: ListImages.html

.. _ListImages:

Obtaining a Target Image ID
===========================

Function
--------

This API is used to obtain the ID of an image that can be upgraded in the current cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0137>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/target/{upgrade_type}/images

.. table:: **Table 1** Path parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                         |
   +=================+=================+=================+=====================================================================================================================+
   | project_id      | Yes             | String          | Project ID. For details about how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | ID of the cluster to be upgraded.                                                                                   |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------+
   | upgrade_type    | Yes             | String          | Version type. The value can be:                                                                                     |
   |                 |                 |                 |                                                                                                                     |
   |                 |                 |                 | -  **same**: upgrade to the same version.                                                                           |
   |                 |                 |                 | -  **cross**: upgrade to a different version.                                                                       |
   |                 |                 |                 | -  **crossEngine**: cross-engine upgrade.                                                                           |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------+
   | Parameter               | Type                                                                                         | Description                                                    |
   +=========================+==============================================================================================+================================================================+
   | needUploadUpgradePlugin | Boolean                                                                                      | Indicates whether to upload the plug-in of the target version. |
   +-------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------+
   | imageInfoList           | Array of :ref:`GetTargetImageIdDetail <listimages__response_gettargetimageiddetail>` objects | Image details.                                                 |
   +-------------------------+----------------------------------------------------------------------------------------------+----------------------------------------------------------------+

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
   priority         Integer Priority
   ================ ======= ======================================

Request Example
---------------

.. code-block:: text

   GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/target/cross/images

   {
     "needUploadUpgradePlugin" : false,
     "imageInfoList" : [ ]
   }

Response Example
----------------

**Status code: 200**

The request is processed.

.. code-block::

   {
     "needUploadUpgradePlugin" : false,
     "imageInfoList" : [ ]
   }

Status Codes
------------

+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                            |
+=============+========================================================================================================================================================================+
| 200         | The request is processed.                                                                                                                                              |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400         | Invalid request. Modify the request directly and do not attempt to retry it.                                                                                           |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403         | The request is rejected. The server has received and understood the request, but refused to respond to it. Modify the request directly and do not attempt to retry it. |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

For details, see :ref:`Error Code <css_03_0076>`.
