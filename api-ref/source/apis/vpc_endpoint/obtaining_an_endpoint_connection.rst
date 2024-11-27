:original_name: ShowVpcepConnection.html

.. _ShowVpcepConnection:

Obtaining an Endpoint Connection
================================

Function
--------

This API is used to obtain a VPC endpoint connection.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/connections

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to query.                                                                                             |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type    | Description                                                                                                                 |
   +===========+===========+=========+=============================================================================================================================+
   | start     | No        | Integer | The start value of the query. The default value is 1, indicating that the query starts from the first task.                 |
   +-----------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------+
   | limit     | No        | Integer | Number of task to be queried. The default value is 10, indicating that the information about 10 tasks is queried at a time. |
   +-----------+-----------+---------+-----------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+---------------------------------------------------------------------------------+---------------------------------------------+
   | Parameter             | Type                                                                            | Description                                 |
   +=======================+=================================================================================+=============================================+
   | connections           | Array of :ref:`connections <showvpcepconnection__response_connections>` objects | Connection information                      |
   +-----------------------+---------------------------------------------------------------------------------+---------------------------------------------+
   | vpcServiceName        | String                                                                          | VPC endpoint service name                   |
   +-----------------------+---------------------------------------------------------------------------------+---------------------------------------------+
   | permissions           | Array of :ref:`permissions <showvpcepconnection__response_permissions>` objects | Permission list                             |
   +-----------------------+---------------------------------------------------------------------------------+---------------------------------------------+
   | vpcepUpdateSwitch     | Boolean                                                                         | Whether to update endpoints.                |
   |                       |                                                                                 |                                             |
   |                       |                                                                                 | -  **true**: The VPC endpoint is enabled.   |
   |                       |                                                                                 |                                             |
   |                       |                                                                                 | -  **false**: The VPC endpoint is disabled. |
   +-----------------------+---------------------------------------------------------------------------------+---------------------------------------------+
   | total_count           | Integer                                                                         | Number of endpoints.                        |
   +-----------------------+---------------------------------------------------------------------------------+---------------------------------------------+

.. _showvpcepconnection__response_connections:

.. table:: **Table 4** connections

   +-----------------------+-----------------------+----------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                    |
   +=======================+=======================+================================================================+
   | id                    | String                | Endpoint ID.                                                   |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | status                | String                | Endpoint status.                                               |
   |                       |                       |                                                                |
   |                       |                       | -  **accepted**: The VPC endpoint connection is enabled.       |
   |                       |                       |                                                                |
   |                       |                       | -  **rejected**: The VPC endpoint connection is disabled.      |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | maxSession            | String                | Maximum number of connections.                                 |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | specificationName     | String                | Endpoint name.                                                 |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | created_at            | String                | Creation time. The format is **ISO8601: CCYY-MM-DDThh:mm:ss**. |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | update_at             | String                | Update time. The default value is **null**.                    |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | domain_id             | String                | Owner.                                                         |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | vpcepIp               | String                | IPv4 address of the VPC endpoint.                              |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | vpcepIpv6Address      | String                | IPv6 address of the VPC endpoint.                              |
   +-----------------------+-----------------------+----------------------------------------------------------------+
   | vpcepDnsName          | String                | Private domain name for accessing the VPC endpoint.            |
   +-----------------------+-----------------------+----------------------------------------------------------------+

.. _showvpcepconnection__response_permissions:

.. table:: **Table 5** permissions

   =============== ====== ===============
   Parameter       Type   Description
   =============== ====== ===============
   id              String id
   permission      String Permissions
   permission_type String Permission type
   created_at      String Creation time
   =============== ====== ===============

Example Requests
----------------

None

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "connections" : [ {
       "id" : "54b7f739-31a1-40d0-862b-ac85b83ab2da",
       "status" : "accepted",
       "maxSession" : "3000",
       "specificationName" : "default",
       "vpcepIp" : "192.168.0.122",
       "vpcepIpv6Address" : null,
       "vpcepDnsName" : null,
       "created_at" : "2024-06-11T09:36:24Z",
       "update_at" : null,
       "domain_id" : "db9b76a0d9ae431f8e85e89da2ca867c"
     }, {
       "id" : "e88ad0bc-c2c7-419c-bd9b-a961111f0a42",
       "status" : "accepted",
       "maxSession" : "3000",
       "specificationName" : "default",
       "vpcepIp" : "192.168.0.133",
       "vpcepIpv6Address" : null,
       "vpcepDnsName" : null,
       "created_at" : "2023-10-12T07:33:16Z",
       "update_at" : null,
       "domain_id" : "db9b76a0d9ae431f8e85e89da2ca867c"
     } ],
     "vpcepUpdateSwitch" : false,
     "total_count" : 2,
     "vpcServiceName" : "cn-north-4.css-op-no-delete.cf072729-b076-49db-83d3-020dc9f589bd",
     "permissions" : [ {
       "id" : "432a6429-f377-4168-8b24-feb5885af08c",
       "permission" : "iam:domain::db9b76a0d9ae431f8e85e89da2ca867c",
       "permission_type" : "domainId",
       "created_at" : "2023-10-12T07:33:11Z"
     } ]
   }

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                        |
+===================================+====================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                   |
|                                   |                                                                                                                                    |
|                                   | Modify the request before retry.                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                       |
|                                   |                                                                                                                                    |
|                                   | The resource that the client attempts to create already exists, or the update request fails to be processed because of a conflict. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
