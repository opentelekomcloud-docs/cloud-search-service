:original_name: EnableOrDisableElb.html

.. _EnableOrDisableElb:

Enabling or Disabling Load Balancers for a Cluster
==================================================

Function
--------

This API is used to enable or disable load balancers for a cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/loadbalancers/es-switch

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Project ID of the account.                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                      |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | ID of the cluster to be modified. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | Cluster ID.                                                                                                                          |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                          |
   +=================+=================+=================+======================================================================================================================+
   | enable          | Yes             | Boolean         | **Definition**:                                                                                                      |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | Enable or disable the ES load balancer.                                                                              |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | -  **true**: Yes                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | -  **false**: This option will be disabled.                                                                          |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                   |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
   | agency          | No              | String          | **Definition**:                                                                                                      |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | Name of the agency used to configure load balancing. This parameter is mandatory when **enable** is set to **true**. |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                   |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
   | elb_id          | No              | String          | **Definition**:                                                                                                      |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | Load balancer ID. This parameter is mandatory when **enable** is set to **true**.                                    |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                   |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------+
   | type            | No              | String          | **Definition**:                                                                                                      |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | Load balancer type. This parameter is not required for an observability cluster.                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                  |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                     |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | -  searchTool: Enable or disable an Elasticsearch/OpenSearch load balancer.                                          |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | -  viewTool: Enable or disable the Kibana/OpenSearch Dashboards load balancer.                                       |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                   |
   |                 |                 |                 |                                                                                                                      |
   |                 |                 |                 | searchTool                                                                                                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   ========= ====== =================
   Parameter Type   Description
   ========= ====== =================
   elb_id    String Load balancer ID.
   ========= ====== =================

Example Requests
----------------

Enable the load balancer.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/58ee0f27-70b3-47e0-ac72-9e3df6cd15cd/loadbalancers/es-switch

   {
     "enable" : true,
     "elb_id" : "5d45faad-6cb3-479b-96b8-3e2de0cc6268",
     "agency" : "css_elb_agency"
   }

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "elb_id" : "5d45faad-6cb3-479b-96b8-3e2de0cc6268"
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
