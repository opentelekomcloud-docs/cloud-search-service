:original_name: ShowElbDetail.html

.. _ShowElbDetail:

Obtain information about the load balancers of a cluster.
=========================================================

Function
--------

CSS integrates shared load balancers and allows you to bind public network access and enable the VPC Endpoint service. Dedicated load balancers provide more functions and higher performance than shared load balancers.

This API is used to obtain the ELB load balancer information of a cluster, including the server certificate name, server certificate ID, ELB switch information, load balancers, listeners, and health check results.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/es-listeners

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

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                       |
   +=================+=================+=================+===================================================================================================+
   | type            | No              | String          | **Definition**:                                                                                   |
   |                 |                 |                 |                                                                                                   |
   |                 |                 |                 | Search type.                                                                                      |
   |                 |                 |                 |                                                                                                   |
   |                 |                 |                 | **Constraints**:                                                                                  |
   |                 |                 |                 |                                                                                                   |
   |                 |                 |                 | N/A                                                                                               |
   |                 |                 |                 |                                                                                                   |
   |                 |                 |                 | **Value range**:                                                                                  |
   |                 |                 |                 |                                                                                                   |
   |                 |                 |                 | -  searchTool: Query details about the load balancers of an Elasticsearch/OpenSearch cluster.     |
   |                 |                 |                 |                                                                                                   |
   |                 |                 |                 | [- viewTool: Query details about the load balancers of Kibana/OpenSearch Dashboards.] (tag:white) |
   |                 |                 |                 |                                                                                                   |
   |                 |                 |                 | **Default value**:                                                                                |
   |                 |                 |                 |                                                                                                   |
   |                 |                 |                 | searchTool                                                                                        |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | Parameter             | Type                                                                | Description                        |
   +=======================+=====================================================================+====================================+
   | serverCertName        | String                                                              | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | Server certificate name.           |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | N/A                                |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | serverCertId          | String                                                              | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | Server certificate ID.             |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | N/A                                |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | cacertName            | String                                                              | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | The name of the CA certificate.    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | N/A                                |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | cacertId              | String                                                              | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | ID of the CA certificate.          |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | N/A                                |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | elb_enable            | Boolean                                                             | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | Whether ELB is enabled.            |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | -  true: ELB is enabled.           |
   |                       |                                                                     |                                    |
   |                       |                                                                     | -  false: ELB is disabled.         |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | authentication_type   | String                                                              | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | Authentication mode.               |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | -  single: one-way authentication. |
   |                       |                                                                     |                                    |
   |                       |                                                                     | -  double: two-way authentication. |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | loadBalancer          | :ref:`LoadBalancer <showelbdetail__response_loadbalancer>` object   | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | Load balancer information.         |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | N/A                                |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | listener              | :ref:`Elbv3Listener <showelbdetail__response_elbv3listener>` object | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | Listener object information.       |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | N/A                                |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+
   | healthmonitors        | Array of :ref:`Member <showelbdetail__response_member>` objects     | **Definition**:                    |
   |                       |                                                                     |                                    |
   |                       |                                                                     | Health check result set.           |
   |                       |                                                                     |                                    |
   |                       |                                                                     | **Value range**:                   |
   |                       |                                                                     |                                    |
   |                       |                                                                     | N/A                                |
   +-----------------------+---------------------------------------------------------------------+------------------------------------+

.. _showelbdetail__response_loadbalancer:

.. table:: **Table 4** LoadBalancer

   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | Parameter             | Type                                                                          | Description                                                                   |
   +=======================+===============================================================================+===============================================================================+
   | id                    | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | Load balancer ID.                                                             |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | name                  | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | Load balancer name.                                                           |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | guaranteed            | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | Whether a dedicated load balancer is used.                                    |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | -  **false**: The load balancer is a shared load balancer.                    |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | -  **true**: The load balancer is a dedicated load balancer.                  |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | billing_info          | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | Specifies the resource billing information.                                   |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | -  If the value is left blank, the resource is billed on a pay-per-use basis. |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | description           | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | Description.                                                                  |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | vpc_id                | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | ID of the VPC to which the ELB instance belongs.                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | provisioning_status   | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | Provisioning status of the load balancer                                      |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | -  **ACTIVE**: in use                                                         |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | -  **PENDING_DELETE**: deleting                                               |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | listeners             | Array of :ref:`IdListWrapper <showelbdetail__response_idlistwrapper>` objects | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | Associated listener list.                                                     |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | vip_address           | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | IPv4 virtual IP address bound to the load balancer.                           |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | vip_port_id           | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | Port ID bound to the private IPv4 IP address of the load balancer.            |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | ipv6_vip_address      | String                                                                        | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | IPv6 address of the load balancer.                                            |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | publicips             | Array of :ref:`PublicIpInfo <showelbdetail__response_publicipinfo>` objects   | **Definition**:                                                               |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | The EIP bound to the load balancer                                            |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | **Value range**:                                                              |
   |                       |                                                                               |                                                                               |
   |                       |                                                                               | N/A                                                                           |
   +-----------------------+-------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

.. _showelbdetail__response_idlistwrapper:

.. table:: **Table 5** IdListWrapper

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | id                    | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Listener ID.          |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+

.. _showelbdetail__response_publicipinfo:

.. table:: **Table 6** PublicIpInfo

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | publicip_id           | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | EIP configuration ID. |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+
   | publicip_address      | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Specifies the EIP.    |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+
   | ip_version            | Integer               | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | IP address version.   |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | -  **4**: IPv4.       |
   |                       |                       |                       |
   |                       |                       | -  **6**: IPv6.       |
   +-----------------------+-----------------------+-----------------------+

.. _showelbdetail__response_elbv3listener:

.. table:: **Table 7** Elbv3Listener

   +-----------------------+-------------------------------------------------------------------------+---------------------------------------------+
   | Parameter             | Type                                                                    | Description                                 |
   +=======================+=========================================================================+=============================================+
   | id                    | String                                                                  | **Definition**:                             |
   |                       |                                                                         |                                             |
   |                       |                                                                         | Listener ID.                                |
   |                       |                                                                         |                                             |
   |                       |                                                                         | **Value range**:                            |
   |                       |                                                                         |                                             |
   |                       |                                                                         | N/A                                         |
   +-----------------------+-------------------------------------------------------------------------+---------------------------------------------+
   | name                  | String                                                                  | **Definition**:                             |
   |                       |                                                                         |                                             |
   |                       |                                                                         | Listener name.                              |
   |                       |                                                                         |                                             |
   |                       |                                                                         | **Value range**:                            |
   |                       |                                                                         |                                             |
   |                       |                                                                         | N/A                                         |
   +-----------------------+-------------------------------------------------------------------------+---------------------------------------------+
   | protocol              | String                                                                  | **Definition**:                             |
   |                       |                                                                         |                                             |
   |                       |                                                                         | Protocol used by the listener.              |
   |                       |                                                                         |                                             |
   |                       |                                                                         | **Value range**:                            |
   |                       |                                                                         |                                             |
   |                       |                                                                         | N/A                                         |
   +-----------------------+-------------------------------------------------------------------------+---------------------------------------------+
   | protocol_port         | Integer                                                                 | **Definition**:                             |
   |                       |                                                                         |                                             |
   |                       |                                                                         | Port used by the listener.                  |
   |                       |                                                                         |                                             |
   |                       |                                                                         | **Value range**:                            |
   |                       |                                                                         |                                             |
   |                       |                                                                         | N/A                                         |
   +-----------------------+-------------------------------------------------------------------------+---------------------------------------------+
   | ipgroup               | :ref:`ListenerIpGroup <showelbdetail__response_listeneripgroup>` object | **Definition**:                             |
   |                       |                                                                         |                                             |
   |                       |                                                                         | ipgroup information in the listener object. |
   |                       |                                                                         |                                             |
   |                       |                                                                         | **Value range**:                            |
   |                       |                                                                         |                                             |
   |                       |                                                                         | N/A                                         |
   +-----------------------+-------------------------------------------------------------------------+---------------------------------------------+

.. _showelbdetail__response_listeneripgroup:

.. table:: **Table 8** ListenerIpGroup

   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                             |
   +=======================+=======================+=========================================================================================================================================+
   | ipgroup_id            | String                | **Definition**:                                                                                                                         |
   |                       |                       |                                                                                                                                         |
   |                       |                       | ID of the access control group associated with the listener. This parameter is mandatory during creation and is optional during update. |
   |                       |                       |                                                                                                                                         |
   |                       |                       | **Value range**:                                                                                                                        |
   |                       |                       |                                                                                                                                         |
   |                       |                       | N/A                                                                                                                                     |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------+
   | enable_ipgroup        | Boolean               | **Definition**:                                                                                                                         |
   |                       |                       |                                                                                                                                         |
   |                       |                       | Status of an access control group.                                                                                                      |
   |                       |                       |                                                                                                                                         |
   |                       |                       | **Value range**:                                                                                                                        |
   |                       |                       |                                                                                                                                         |
   |                       |                       | -  True: Access control is enabled.                                                                                                     |
   |                       |                       |                                                                                                                                         |
   |                       |                       | -  False: Access control is disabled.                                                                                                   |
   +-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------+

.. _showelbdetail__response_member:

.. table:: **Table 9** Member

   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                    |
   +=======================+=======================+================================================================================================================+
   | name                  | String                | **Definition**:                                                                                                |
   |                       |                       |                                                                                                                |
   |                       |                       | Specifies the backend server name.                                                                             |
   |                       |                       |                                                                                                                |
   |                       |                       | **Value range**:                                                                                               |
   |                       |                       |                                                                                                                |
   |                       |                       | N/A                                                                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
   | address               | String                | **Definition**:                                                                                                |
   |                       |                       |                                                                                                                |
   |                       |                       | Specifies the IP address bound to the backend server.                                                          |
   |                       |                       |                                                                                                                |
   |                       |                       | **Value range**:                                                                                               |
   |                       |                       |                                                                                                                |
   |                       |                       | N/A                                                                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
   | protocol_port         | Integer               | **Definition**:                                                                                                |
   |                       |                       |                                                                                                                |
   |                       |                       | Specifies the port used by the backend server.                                                                 |
   |                       |                       |                                                                                                                |
   |                       |                       | **Value range**:                                                                                               |
   |                       |                       |                                                                                                                |
   |                       |                       | N/A                                                                                                            |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
   | operating_status      | String                | **Definition**:                                                                                                |
   |                       |                       |                                                                                                                |
   |                       |                       | Specifies the operating status of the backend server.                                                          |
   |                       |                       |                                                                                                                |
   |                       |                       | **Value range**:                                                                                               |
   |                       |                       |                                                                                                                |
   |                       |                       | -  ONLINE: The backend server is running normally.                                                             |
   |                       |                       |                                                                                                                |
   |                       |                       | -  NO_MONITOR: No health check is configured for the backend server group to which the backend server belongs. |
   |                       |                       |                                                                                                                |
   |                       |                       | -  OFFLINE: The cloud server used as the backend server is stopped or does not exist.                          |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+
   | instance_id           | String                | **Definition**:                                                                                                |
   |                       |                       |                                                                                                                |
   |                       |                       | ID of the instance used as the backend server.                                                                 |
   |                       |                       |                                                                                                                |
   |                       |                       | **Value range**:                                                                                               |
   |                       |                       |                                                                                                                |
   |                       |                       | An empty value indicates that the instance associated with the member is not a real device.                    |
   +-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------+

Example Requests
----------------

Obtain information about the load balancers of a cluster.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/es-listeners

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "loadBalancer" : {
       "id" : "5d45faad-6cb3-479b-96b8-3e2de0cc6268",
       "name" : "elb-css",
       "guaranteed" : "true",
       "description" : "",
       "listeners" : [ {
         "id" : "011d14fa-908b-4cd9-b0d6-0768ddc6cb71"
       }, {
         "id" : "04b86029-c281-4490-a3bd-5ea1266658ba"
       } ],
       "publicips" : [ {
         "publicip_id" : "f678e23c-96a5-49e8-8ea2-bd8b47d41e78",
         "publicip_address" : "100.1.1.1",
         "ip_version" : 4
       } ],
       "vpc_id" : "4f3deec3-efa8-4598-bf91-560aad1377a3",
       "provisioning_status" : "ACTIVE",
       "vip_address" : "10.0.0.1",
       "ipv6_vip_address" : "2409:27ff:2003:3e:1fd::f3"
     },
     "listener" : {
       "id" : "41ff041d-c7b9-4142-9167-fa93d54f97da",
       "name" : "css-searchServer",
       "protocol" : "HTTPS",
       "protocol_port" : 9265
     },
     "healthmonitors" : [ {
       "instance_id" : "bac86342-2222-43e6-817f-57f040a174a6",
       "name" : "",
       "address" : "10.0.0.87",
       "protocol_port" : 9200,
       "operating_status" : "ONLINE"
     }, {
       "instance_id" : "d935b82c-f94b-4ae0-9997-ddc90885d8c6",
       "name" : "",
       "address" : "10.0.0.61",
       "protocol_port" : 9200,
       "operating_status" : "ONLINE"
     } ],
     "serverCertName" : "server1",
     "serverCertId" : "82375af01c0d40f6a44c15962c570625",
     "elb_enable" : true,
     "authentication_type" : "single"
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
