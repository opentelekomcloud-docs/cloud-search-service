:original_name: ShowVpcepConnection.html

.. _ShowVpcepConnection:

Obtaining an Endpoint Connection
================================

Function
--------

The VPC endpoint service enables secure and reliable access across VPCs through a dedicated gateway, without exposing the network information of servers. The VPC endpoint address can be an IPv4 address (automatically allocated when the VPC endpoint service is enabled), an IPv6 address (allocated when a professional VPC endpoint is created and dual-stack networking is enabled), or an internal domain name (allocated when DNS is enabled). This API is used to obtain the VPCEP connection of a cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/connections

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                             |
   +=================+=================+=================+=========================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Project ID of the account.                                                                                                              |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | ID of the cluster you want to query. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Constraints**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Value range**:                                                                                                                        |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | Cluster ID.                                                                                                                             |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | **Default value**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                         |
   |                 |                 |                 | N/A                                                                                                                                     |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                              |
   +=================+=================+=================+==========================================================================+
   | offset          | No              | Integer         | **Definition**:                                                          |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | Start value for querying VPC endpoint connections.                       |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | **Constraints**:                                                         |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | N/A                                                                      |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | **Value range**:                                                         |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | 0-1000                                                                   |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | **Default value**:                                                       |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | 0                                                                        |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------+
   | limit           | No              | Integer         | **Definition**:                                                          |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | The number of VPC endpoint connections to be queried.                    |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | **Constraints**:                                                         |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | N/A                                                                      |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | **Value range**:                                                         |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | 1-1000                                                                   |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | **Default value**:                                                       |
   |                 |                 |                 |                                                                          |
   |                 |                 |                 | The default value is 10, indicating that 10 tasks are queried at a time. |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+---------------------------------------------------------------------------------+----------------------------------------------------+
   | Parameter             | Type                                                                            | Description                                        |
   +=======================+=================================================================================+====================================================+
   | connections           | Array of :ref:`connections <showvpcepconnection__response_connections>` objects | **Definition**:                                    |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | Cluster VPC endpoint connection information.       |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | **Value range**:                                   |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | N/A                                                |
   +-----------------------+---------------------------------------------------------------------------------+----------------------------------------------------+
   | vpcServiceName        | String                                                                          | **Definition**:                                    |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | Name of the VPC endpoint service.                  |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | **Value range**:                                   |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | N/A                                                |
   +-----------------------+---------------------------------------------------------------------------------+----------------------------------------------------+
   | permissions           | Array of :ref:`permissions <showvpcepconnection__response_permissions>` objects | **Definition**:                                    |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | Permissions of the cluster VPC endpoint whitelist. |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | **Value range**:                                   |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | N/A                                                |
   +-----------------------+---------------------------------------------------------------------------------+----------------------------------------------------+
   | vpcepUpdateSwitch     | Boolean                                                                         | **Definition**:                                    |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | Whether to enable VPC endpoint.                    |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | **Value range**:                                   |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | -  **true**: The VPC endpoint is enabled.          |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | -  **false**: The VPC endpoint is disabled.        |
   +-----------------------+---------------------------------------------------------------------------------+----------------------------------------------------+
   | total_count           | Integer                                                                         | **Definition**:                                    |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | Number of cluster VPC endpoints.                   |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | **Value range**:                                   |
   |                       |                                                                                 |                                                    |
   |                       |                                                                                 | N/A                                                |
   +-----------------------+---------------------------------------------------------------------------------+----------------------------------------------------+

.. _showvpcepconnection__response_connections:

.. table:: **Table 4** connections

   +-----------------------+-----------------------+-----------------------------------------------------------+
   | Parameter             | Type                  | Description                                               |
   +=======================+=======================+===========================================================+
   | id                    | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Cluster VPC endpoint ID.                                  |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | N/A                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | status                | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Cluster VPC endpoint status.                              |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | -  **accepted**: The VPC endpoint connection is enabled.  |
   |                       |                       |                                                           |
   |                       |                       | -  **rejected**: The VPC endpoint connection is disabled. |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | maxSession            | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Maximum number of connections to a VPC endpoint.          |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | N/A                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | specificationName     | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Cluster VPC endpoint name.                                |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | N/A                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | created_at            | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Creation time.                                            |
   |                       |                       |                                                           |
   |                       |                       | **Value range**                                           |
   |                       |                       |                                                           |
   |                       |                       | The format is CCYY-MM-DDThh:mm:ss (ISO 8601).             |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | update_at             | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Update time. The default value is null.                   |
   |                       |                       |                                                           |
   |                       |                       | **Value range**                                           |
   |                       |                       |                                                           |
   |                       |                       | The format is CCYY-MM-DDThh:mm:ss (ISO 8601).             |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | domain_id             | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Account ID of the owner.                                  |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | N/A                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | vpcepIp               | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | IPv4 address of a cluster VPC endpoint.                   |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | N/A                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | vpcepIpv6Address      | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | IPv6 address of a cluster VPC endpoint.                   |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | N/A                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------+
   | vpcepDnsName          | String                | **Definition**:                                           |
   |                       |                       |                                                           |
   |                       |                       | Private domain name of a cluster VPC endpoint.            |
   |                       |                       |                                                           |
   |                       |                       | **Value range**:                                          |
   |                       |                       |                                                           |
   |                       |                       | N/A                                                       |
   +-----------------------+-----------------------+-----------------------------------------------------------+

.. _showvpcepconnection__response_permissions:

.. table:: **Table 5** permissions

   +-----------------------+-----------------------+--------------------------------------------------------+
   | Parameter             | Type                  | Description                                            |
   +=======================+=======================+========================================================+
   | id                    | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Unique ID of the permission.                           |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | permission            | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Permission details for the VPCEP connection whitelist. |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | permission_type       | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | VPC endpoint permission type.                          |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | domainId: user account ID.                             |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | created_at            | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Specifies when the VPC endpoint was created.           |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | The format is CCYY-MM-DDThh:mm:ss (ISO 8601).          |
   +-----------------------+-----------------------+--------------------------------------------------------+

Example Requests
----------------

Obtain the VPCEP connection of a cluster.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/vpcepservice/connections

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
       "created_at" : "2024-06-11T09:36:24Z",
       "domain_id" : "db9b76a0d9ae431f8e85e89da2ca867c"
     }, {
       "id" : "e88ad0bc-c2c7-419c-bd9b-a961111f0a42",
       "status" : "accepted",
       "maxSession" : "3000",
       "specificationName" : "default",
       "vpcepIp" : "192.168.0.133",
       "created_at" : "2023-10-12T07:33:16Z",
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
