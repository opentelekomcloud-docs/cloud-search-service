:original_name: ShowAiOpsSetting.html

.. _ShowAiOpsSetting:

Viewing Scheduled Intelligent O&M Diagnosis Settings
====================================================

Function
--------

CSS provides scheduled diagnostic capabilities as part of intelligent O&M and supports daily diagnosis of potential cluster risks. This API is used to obtain the scheduled intelligent O&M diagnosis settings.

Applicable to Elasticsearch and OpenSearch engines.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ai-ops/setting

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

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                               |
   +=======================+=======================+===========================================================================================================================================================================+
   | check_type            | String                | **Definition**:                                                                                                                                                           |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | Check type.                                                                                                                                                               |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | **Value range**:                                                                                                                                                          |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | -  full_detection: all check items.                                                                                                                                       |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | -  unavailability_detection: cluster unavailability check items.                                                                                                          |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | -  partial_detection: partial check items, select by setting check_items.                                                                                                 |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | check_items           | Array of strings      | **Definition**                                                                                                                                                            |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | Check item name. Select a subset of all check items, and enter the check item list. This parameter is available only when **check_type** is set to **partial_detection**. |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | **Range**                                                                                                                                                                 |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | N/A                                                                                                                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | period                | String                | **Definition**:                                                                                                                                                           |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | Intelligent O&M automatic check time, in the form of time followed by time zone, for example, 00:00 GMT+08:00.                                                            |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | **Value range**:                                                                                                                                                          |
   |                       |                       |                                                                                                                                                                           |
   |                       |                       | N/A                                                                                                                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

Viewing Scheduled Check Settings for Intelligent O&M

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops/setting

Example Responses
-----------------

**Status code: 200**

.. code-block::

   {
     "check_type" : "partial_detection",
     "check_items" : [ "nodeDiskCheck", "dataNodeDiskBalanceCheck" ],
     "period" : "23:00 GMT+08:00"
   }

Status Codes
------------

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                                                                                             |
+=============+=========================================================================================================================================================================================================================================+
| 200         | Request succeeded.                                                                                                                                                                                                                      |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400         | Invalid request. Modify the request directly and do not attempt to retry it.                                                                                                                                                            |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409         | The request cannot be processed due to a conflict. This status code indicates that the resource that the client attempts to create already exists, or the request failed to be processed because of the update of the conflict request. |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412         | The server does not meet one of the preconditions that the client puts on the request.                                                                                                                                                  |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
