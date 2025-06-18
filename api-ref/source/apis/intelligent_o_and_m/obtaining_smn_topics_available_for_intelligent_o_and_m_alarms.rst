:original_name: ListSmnTopics.html

.. _ListSmnTopics:

Obtaining SMN Topics Available for Intelligent O&M Alarms
=========================================================

Function
--------

This API is used to obtain SMN topics available for intelligent O&M alarms.

URI
---

GET /v1.0/{project_id}/domains/{domain_id}/ai-ops/smn-topics

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | domain_id  | Yes       | String | Domain account ID                                                                                                                |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   ========== ================ ============
   Parameter  Type             Description
   ========== ================ ============
   topicsName Array of strings Subject name
   ========== ================ ============

Example Requests
----------------

Obtain the intelligent O&M task list and details.

.. code-block:: text

   GET /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "topicsName" : [ "aiops-test" ]
   }

Status Codes
------------

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                      |
+===================================+==================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                 |
|                                   |                                                                                                                                                  |
|                                   | Modify the request instead of retrying.                                                                                                          |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                               |
|                                   |                                                                                                                                                  |
|                                   | This status code indicates that the resource that the client attempts to create already exits, or the requested update failed due to a conflict. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                         |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
