:original_name: ListElbs.html

.. _ListElbs:

Querying ELB V3 Load Balancers Supported by a Cluster
=====================================================

Function
--------

Query the ELB V3 load balancers supported by a cluster.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/loadbalancers

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | ID of the cluster you want to query.                                                                                                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+------------------------------------------------------------------------------------------+----------------------------+
   | Parameter             | Type                                                                                     | Description                |
   +=======================+==========================================================================================+============================+
   | loadbalancers         | Array of :ref:`LoadbalancersResource <listelbs__response_loadbalancersresource>` objects | **Parameter description**: |
   |                       |                                                                                          |                            |
   |                       |                                                                                          | Load balancer list.        |
   +-----------------------+------------------------------------------------------------------------------------------+----------------------------+

.. _listelbs__response_loadbalancersresource:

.. table:: **Table 3** LoadbalancersResource

   +-----------------------+-----------------------+----------------------------------------------------+
   | Parameter             | Type                  | Description                                        |
   +=======================+=======================+====================================================+
   | id                    | String                | **Parameter description**:                         |
   |                       |                       |                                                    |
   |                       |                       | Specifies the load balancer ID.                    |
   +-----------------------+-----------------------+----------------------------------------------------+
   | name                  | String                | **Parameter description**:                         |
   |                       |                       |                                                    |
   |                       |                       | Load balancer name                                 |
   +-----------------------+-----------------------+----------------------------------------------------+
   | l7_flavor_id          | String                | **Parameter description**:                         |
   |                       |                       |                                                    |
   |                       |                       | Layer 7 protocol ID.                               |
   +-----------------------+-----------------------+----------------------------------------------------+
   | ip_target_enable      | Boolean               | **Parameter description**:                         |
   |                       |                       |                                                    |
   |                       |                       | Indicates whether to enable the cross-VPC backend. |
   +-----------------------+-----------------------+----------------------------------------------------+

Example Requests
----------------

Query ELB V3 load balancers supported by a cluster.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/{cluster_id}/loadbalancers

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "loadbalancers" : [ {
       "id" : "5d45faad-6cb3-479b-96b8-3e2de0cc6268",
       "name" : "elb-css",
       "l7_flavor_id" : "9c8c2425-e061-4bf8-ac65-cd1db92b18e1",
       "ip_target_enable" : true
     }, {
       "id" : "5d45faad-6cb3-479b-96b8-3e2de0cc6269",
       "name" : "elb-b832",
       "l7_flavor_id" : "9c8c2425-e061-4bf8-ac65-cd1db92b18e1",
       "ip_target_enable" : true
     } ]
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
