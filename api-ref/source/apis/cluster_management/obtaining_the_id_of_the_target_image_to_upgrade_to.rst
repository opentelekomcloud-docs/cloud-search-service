:original_name: ListImages.html

.. _ListImages:

Obtaining the ID of the Target Image to Upgrade To
==================================================

Function
--------

This API is used to obtain the ID of an image that can be upgraded in the current cluster.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/target/{upgrade_type}/images

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | ID of the cluster to be upgraded.                                                                                                    |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | upgrade_type    | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Upgrade type.                                                                                                                        |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | -  **same**: same-version upgrade.                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | -  **cross**: cross-version upgrade.                                                                                                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | -  **cross-engine**: cross-engine upgrade.                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 |    **Default value**:                                                                                                                |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 |    N/A                                                                                                                               |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

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
   | needUploadUpgradePlugin | Boolean                                                                                      | **Parameter description**:                           |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | Whether to upload the plug-in of the target version. |
   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+
   | imageInfoList           | Array of :ref:`GetTargetImageIdDetail <listimages__response_gettargetimageiddetail>` objects | **Parameter description**:                           |
   |                         |                                                                                              |                                                      |
   |                         |                                                                                              | Image details.                                       |
   +-------------------------+----------------------------------------------------------------------------------------------+------------------------------------------------------+

.. _listimages__response_gettargetimageiddetail:

.. table:: **Table 3** GetTargetImageIdDetail

   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                               |
   +=======================+=======================+===========================================================================+
   | id                    | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | ID of an image that can be upgraded.                                      |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | displayName           | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Name of an image that can be upgraded.                                    |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | imageDesc             | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Image description.                                                        |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | datastoreType         | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Image engine type.                                                        |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | datastoreVersion      | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Image engine version.                                                     |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | priority              | Integer               | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Priority of the target image. A larger value indicates a higher priority. |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+

Example Requests
----------------

Obtain the target image for a cross-version upgrade of the cluster.

.. code-block:: text

   GET https://{Endpoint}/v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/target/cross/images

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
