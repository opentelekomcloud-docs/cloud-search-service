:original_name: ShowAiOpsDetector.html

.. _ShowAiOpsDetector:

Viewing Intelligent O&M Diagnostics Items
=========================================

Function
--------

CSS provides intelligent O&M to check potential risks in clusters. This API is used to obtain intelligent diagnostic items.

It is available for Elasticsearch and OpenSearch.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/ai-ops/detector

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

   +--------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                | Type                                                                              | Description                                                                                                                      |
   +==========================+===================================================================================+==================================================================================================================================+
   | full_detection           | Array of :ref:`AiOpsDetector <showaiopsdetector__response_aiopsdetector>` objects | **Definition**:                                                                                                                  |
   |                          |                                                                                   |                                                                                                                                  |
   |                          |                                                                                   | Full check items. The IDs, names, and descriptions of full check items will be returned.                                         |
   +--------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+
   | unavailability_detection | Array of :ref:`AiOpsDetector <showaiopsdetector__response_aiopsdetector>` objects | **Definition**:                                                                                                                  |
   |                          |                                                                                   |                                                                                                                                  |
   |                          |                                                                                   | Cluster unavailability check items. The IDs, names, and descriptions of all cluster unavailability check items will be returned. |
   +--------------------------+-----------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------+

.. _showaiopsdetector__response_aiopsdetector:

.. table:: **Table 3** AiOpsDetector

   +-----------------------+-----------------------+-------------------------------+
   | Parameter             | Type                  | Description                   |
   +=======================+=======================+===============================+
   | id                    | String                | **Definition**:               |
   |                       |                       |                               |
   |                       |                       | ID of a supported check item. |
   |                       |                       |                               |
   |                       |                       | **Value range**:              |
   |                       |                       |                               |
   |                       |                       | N/A                           |
   +-----------------------+-----------------------+-------------------------------+
   | name                  | String                | **Definition**:               |
   |                       |                       |                               |
   |                       |                       | Check item name.              |
   |                       |                       |                               |
   |                       |                       | **Value range**:              |
   |                       |                       |                               |
   |                       |                       | N/A                           |
   +-----------------------+-----------------------+-------------------------------+
   | desc                  | String                | **Definition**:               |
   |                       |                       |                               |
   |                       |                       | Check item description.       |
   |                       |                       |                               |
   |                       |                       | **Value range**:              |
   |                       |                       |                               |
   |                       |                       | N/A                           |
   +-----------------------+-----------------------+-------------------------------+

Example Requests
----------------

Viewing Intelligent O&M Check Items

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops/detector

Example Responses
-----------------

**Status code: 200**

.. code-block::

   {
     "full_detection" : [ {
       "id" : "nodeDiskCheck",
       "name" : "Data Node Disk Usage Check",
       "desc" : "Identify data nodes (including cold data nodes) with the highest disk usage in the cluster. Excessive disk usage can affect cluster stability. [N]High risk: When a node's disk usage reaches 85%, no new index replicas will be allocated to it. [N]Medium risk: When a node's disk usage exceeds 80%, take immediate action to prevent further increase."
     } ],
     "unavailability_detection" : [ {
       "id" : "dataNodeDiskBalanceCheck",
       "name" : "Data Node Disk Usage Balance Check",
       "desc" : "Check whether disk usage is balanced across all regular data nodes and cold data nodes. Unbalanced disk usage may cause performance issues. [N]Risk levels: [N]High risk: Maximum disk usage difference between nodes >= 40% [N]Medium risk: 25% <= Maximum disk usage difference between nodes < 40%."
     } ]
   }

Status Codes
------------

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                                                                                             |
+=============+=========================================================================================================================================================================================================================================+
| 200         | Intelligent O&M check items                                                                                                                                                                                                             |
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
