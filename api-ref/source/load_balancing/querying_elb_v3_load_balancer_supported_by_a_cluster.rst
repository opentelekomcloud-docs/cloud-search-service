:original_name: css_03_0126.html

.. _css_03_0126:

Querying ELB V3 Load Balancer Supported by a Cluster
====================================================

Function
--------

This API is used to query the ELB V3 load balancers supported by a cluster.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/loadbalancers

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be queried                                                    |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameter

   +---------------+---------------------------------------------------------------------------------------------+--------------------+
   | Parameter     | Type                                                                                        | Description        |
   +===============+=============================================================================================+====================+
   | loadbalancers | Array of :ref:`LoadbalancersResource <css_03_0126__response_loadbalancersresource>` objects | Load balancer list |
   +---------------+---------------------------------------------------------------------------------------------+--------------------+

.. _css_03_0126__response_loadbalancersresource:

.. table:: **Table 3** LoadbalancersResource

   +------------------+---------+---------------------------------------------------+
   | Parameter        | Type    | Description                                       |
   +==================+=========+===================================================+
   | id               | String  | Load balancer ID                                  |
   +------------------+---------+---------------------------------------------------+
   | name             | String  | Load balancer name                                |
   +------------------+---------+---------------------------------------------------+
   | l7_flavor_id     | String  | Layer 7 protocol ID                               |
   +------------------+---------+---------------------------------------------------+
   | ip_target_enable | Boolean | Indicates whether to enable the cross-VPC backend |
   +------------------+---------+---------------------------------------------------+

Request Example
---------------

None

Response Example
----------------

**Status code: 200**

The request is processed successfully.

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

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                         |
+===================================+=====================================================================================================================================================================================+
| 200                               | The request is processed successfully.                                                                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                    |
|                                   |                                                                                                                                                                                     |
|                                   | Modify the request instead of retrying.                                                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                                                                  |
|                                   |                                                                                                                                                                                     |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request fails to be processed because of the update of the conflict request. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
