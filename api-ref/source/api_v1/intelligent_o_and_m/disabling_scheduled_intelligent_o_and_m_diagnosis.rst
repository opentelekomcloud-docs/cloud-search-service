:original_name: CloseAiOpsSetting.html

.. _CloseAiOpsSetting:

Disabling Scheduled Intelligent O&M Diagnosis
=============================================

Function
--------

CSS provides scheduled diagnostic capabilities as part of intelligent O&M and supports daily diagnosis of potential cluster risks. This API is used to disable scheduled intelligent O&M diagnosis.

Applicable to Elasticsearch and OpenSearch engines.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/ai-ops/close

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                        |
   +=================+=================+=================+====================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                   |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Constraints**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Range**                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                            |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Default Value**                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | Specifies the ID of the cluster to be disabled. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Constraints**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Range**                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | UUID format, 36 characters.                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | **Default Value**                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                    |
   |                 |                 |                 | N/A                                                                                                                                                |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Disabling Scheduled Checks for Intelligent O&M

.. code-block:: text

   PUT https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops/close

Example Responses
-----------------

None

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
