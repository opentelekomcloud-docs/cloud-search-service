:original_name: CreateAgency.html

.. _CreateAgency:

Automatically create an agency.
===============================

Function
--------

If the built-in CSS agency does not exist, the system automatically creates an agency and grants the permissions required by CSS to it.

If the built-in CSS agency exists, the system removes high-risk permissions and sets the minimal permissions.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/agency/create

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID of the account.                                                                                                       |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                             |
   +=================+=================+=================+=========================================================================================================+
   | domain_id       | Yes             | String          | **Definition**                                                                                          |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | Account ID. For details, see :ref:`Querying Projects Based on Specified Criteria <css_03_0071>`.        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Constraints**                                                                                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Range**                                                                                               |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Default Value**                                                                                       |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+
   | domain_name     | Yes             | String          | **Definition**                                                                                          |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | Account name. For details, see :ref:`Authentication <css_03_0079>`.                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Constraints**                                                                                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Range**                                                                                               |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Default Value**                                                                                       |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A                                                                                                     |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+
   | type            | Yes             | String          | **Definition**:                                                                                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | Type of the agency to be created.                                                                       |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A.                                                                                                    |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                        |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | -  **obs**: agency permissions required for creating snapshots and log backups.                         |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | -  **vpc**: agency permissions required for version upgrade, AZ change, scale-in, and node replacement. |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | -  **smn**: agency permissions required for using the alerting plug-in.                                 |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | -  **elb**: agency permissions required for using load balancing.                                       |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                      |
   |                 |                 |                 |                                                                                                         |
   |                 |                 |                 | N/A.                                                                                                    |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Example of the request for creating an agency used to create snapshots and log backups.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/agency/create

   {
     "domain_id" : "id",
     "domain_name" : "name",
     "type" : "obs"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                     |
+===================================+=================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | The request is invalid.                                                                                                                                         |
|                                   |                                                                                                                                                                 |
|                                   | Modify the request and then try again.                                                                                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | The request is rejected.                                                                                                                                        |
|                                   |                                                                                                                                                                 |
|                                   | The server has received the request and understood it, but the server refuses to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
