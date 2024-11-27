:original_name: EnableOrDisableElb.html

.. _EnableOrDisableElb:

Enabling or Disabling the Elasticsearch Load Balancer
=====================================================

Function
--------

This API is used to enable or disable the Elasticsearch load balancer.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/loadbalancers/es-switch

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be modified                                                                                                 |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+---------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                 |
   +=================+=================+=================+=============================================+
   | enable          | Yes             | Boolean         | Enable or disable the ES load balancer.     |
   |                 |                 |                 |                                             |
   |                 |                 |                 | -  **true**: enable the ES load balancer.   |
   |                 |                 |                 |                                             |
   |                 |                 |                 | -  **false**: disable the ES load balancer. |
   +-----------------+-----------------+-----------------+---------------------------------------------+
   | agency          | No              | String          | Agency name                                 |
   +-----------------+-----------------+-----------------+---------------------------------------------+
   | elb_id          | No              | String          | Load balancer ID                            |
   +-----------------+-----------------+-----------------+---------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   ========= ====== ================
   Parameter Type   Description
   ========= ====== ================
   elb_id    String Load balancer ID
   ========= ====== ================

Example Requests
----------------

Enable the load balancer.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/58ee0f27-70b3-47e0-ac72-9e3df6cd15cd/loadbalancers/es-switch

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
