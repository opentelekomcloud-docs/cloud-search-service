:original_name: CreateAiOps.html

.. _CreateAiOps:

Creating a Cluster Detection Task
=================================

Function
--------

This API is used to create a cluster detection task.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/ai-ops

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the target cluster                                                                                                         |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request header parameters

   ========== ========= ====== ===========
   Parameter  Mandatory Type   Description
   ========== ========= ====== ===========
   X-Language No        String Language
   ========== ========= ====== ===========

.. table:: **Table 3** Request body parameters

   +-------------+-----------+--------------------------------------------------+---------------------------------------------------------------------+
   | Parameter   | Mandatory | Type                                             | Description                                                         |
   +=============+===========+==================================================+=====================================================================+
   | name        | Yes       | String                                           | Detection task name                                                 |
   +-------------+-----------+--------------------------------------------------+---------------------------------------------------------------------+
   | description | No        | String                                           | Detection task description                                          |
   +-------------+-----------+--------------------------------------------------+---------------------------------------------------------------------+
   | alarm       | No        | :ref:`alarm <createaiops__request_alarm>` object | After the detection task is complete, an SMN alarm message is sent. |
   +-------------+-----------+--------------------------------------------------+---------------------------------------------------------------------+

.. _createaiops__request_alarm:

.. table:: **Table 4** alarm

   +-----------------+-----------------+-----------------+--------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                          |
   +=================+=================+=================+======================================+
   | level           | Yes             | String          | Sensitivity of an SMN alarm message. |
   |                 |                 |                 |                                      |
   |                 |                 |                 | -  **high**                          |
   |                 |                 |                 |                                      |
   |                 |                 |                 | -  **medium**                        |
   |                 |                 |                 |                                      |
   |                 |                 |                 | -  **suggestion**                    |
   |                 |                 |                 |                                      |
   |                 |                 |                 | -  **norisk**                        |
   +-----------------+-----------------+-----------------+--------------------------------------+
   | smn_topic       | Yes             | String          | SMN topic name                       |
   +-----------------+-----------------+-----------------+--------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Create a cluster detection task.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/ai-ops

   {
       "name": " aiops-test ",
   "description": "Create a cluster detection task.
    ",
       "alarm":{
           "level":"high",
           "smn_topic":"aiops-test"
       }
   }

Example Responses
-----------------

None

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
