:original_name: GetRoutes.html

.. _GetRoutes:

Obtaining a Cluster Route
=========================

Function
--------

By default, a CSS Elasticsearch cluster cannot directly access services in a different VPC, such as client applications or a Lightweight Directory Access Protocol (LDAP) service. To enable cross-VPC access, you must configure cluster routes. This API is used to retrieve cluster route information, including route IP addresses and the total number of routes.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/route

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

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                   |
   +=================+=================+=================+===============================================================================================================+
   | offset          | No              | Integer         | **Definition**:                                                                                               |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | The start value of the query. The default value is 1, indicating that the query starts from the first route.  |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                              |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | N/A                                                                                                           |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Value range**:                                                                                              |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | Greater than or equal to 1.                                                                                   |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                            |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | 1                                                                                                             |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------+
   | limit           | No              | Integer         | **Parameter description**:                                                                                    |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | Number of routes to be queried. The default value is **10**, indicating that 10 routes are queried at a time. |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Constraints**:                                                                                              |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | N/A                                                                                                           |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Options**:                                                                                                  |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | 1-1000                                                                                                        |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | **Default value**:                                                                                            |
   |                 |                 |                 |                                                                                                               |
   |                 |                 |                 | 10                                                                                                            |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
   | Parameter             | Type                                                                                | Description                                                                                    |
   +=======================+=====================================================================================+================================================================================================+
   | routeResps            | Array of :ref:`RouteRespsResource <getroutes__response_routerespsresource>` objects | **Definition**                                                                                 |
   |                       |                                                                                     |                                                                                                |
   |                       |                                                                                     | Route response information list, including the route IP address, subnet mask, and update time. |
   +-----------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+
   | totalSize             | Integer                                                                             | **Definition**:                                                                                |
   |                       |                                                                                     |                                                                                                |
   |                       |                                                                                     | Total number of routes.                                                                        |
   |                       |                                                                                     |                                                                                                |
   |                       |                                                                                     | **Value range**:                                                                               |
   |                       |                                                                                     |                                                                                                |
   |                       |                                                                                     | N/A                                                                                            |
   +-----------------------+-------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------+

.. _getroutes__response_routerespsresource:

.. table:: **Table 4** RouteRespsResource

   +-----------------------+-----------------------+--------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                        |
   +=======================+=======================+====================================================================+
   | ipAddress             | String                | **Definition**:                                                    |
   |                       |                       |                                                                    |
   |                       |                       | IP address.                                                        |
   |                       |                       |                                                                    |
   |                       |                       | **Value range**:                                                   |
   |                       |                       |                                                                    |
   |                       |                       | N/A                                                                |
   +-----------------------+-----------------------+--------------------------------------------------------------------+
   | ipNetMask             | String                | **Definition**:                                                    |
   |                       |                       |                                                                    |
   |                       |                       | Subnet mask.                                                       |
   |                       |                       |                                                                    |
   |                       |                       | **Value range**:                                                   |
   |                       |                       |                                                                    |
   |                       |                       | N/A                                                                |
   +-----------------------+-----------------------+--------------------------------------------------------------------+
   | updateAt              | String                | **Definition**                                                     |
   |                       |                       |                                                                    |
   |                       |                       | Route IP address update time, in the yyyy-MM-dd'T'HH:mm:ss format. |
   |                       |                       |                                                                    |
   |                       |                       | **Range**                                                          |
   |                       |                       |                                                                    |
   |                       |                       | N/A                                                                |
   +-----------------------+-----------------------+--------------------------------------------------------------------+

Example Requests
----------------

Obtain cluster routes.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/route

Example Responses
-----------------

**Status code: 200**

.. code-block::

   {
     "routeResps" : [ {
       "ipAddress" : "1.2.3.65",
       "ipNetMask" : "255.255.255.255",
       "updateAt" : "2023-07-17T08:09:20"
     }, {
       "ipAddress" : "1.1.1.1",
       "ipNetMask" : "255.255.255.255",
       "updateAt" : "2023-07-17T08:08:50"
     } ],
     "totalSize" : 2
   }

Status Codes
------------

+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                          |
+===================================+======================================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                                                   |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                     |
|                                   |                                                                                                                                                                                      |
|                                   | Modify the request and then try again.                                                                                                                                               |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be processed due to a conflict.                                                                                                                                |
|                                   |                                                                                                                                                                                      |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request failed to be processed because of the update of the conflict request. |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                                                             |
+-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
