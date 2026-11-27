:original_name: UpdateRoute.html

.. _UpdateRoute:

Updating Cluster Routes
=======================

Function
--------

This API is used to update cluster routes.

.. note::

   Modifying cluster routes may cause service network issues and affect connectivity between clients and the cluster. Proceed with caution.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/route

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Range**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                          |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default Value**                                                                                                                |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | ID of the target cluster. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.     |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Range**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                    |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default Value**                                                                                                                |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                  |
   +=================+=================+=================+==============================================================================================================================================================================+
   | configtype      | Yes             | String          | **Definition**:                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | Operation type.                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Constraints**:                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Value range**:                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | -  add_ip: Add a cluster route.                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | -  del_ip: Delete a cluster route.                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Default value**:                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                          |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | configkey       | Yes             | String          | **Definition**                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | Route IP address, that is, the IP address of the server where the public network data source is located.                                                                     |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Constraints**                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | The value must be a valid IP address and cannot start with 0.                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Range**                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Default Value**                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                          |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | configvalue     | Yes             | String          | **Definition**                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | Route subnet mask. If the IP address contains 16 bits, set the subnet mask to **255.255.0.0**. If the IP address contains 24 bits, set the subnet mask to **255.255.255.0**. |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Constraints**                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | The value must be a valid subnet mask and cannot start with 0.                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Range**                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | **Default Value**                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                          |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Update cluster routes.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/route

   {
     "configtype" : "add_ip",
     "configkey" : "10.5.2.1",
     "configvalue" : "255.255.255.255"
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
