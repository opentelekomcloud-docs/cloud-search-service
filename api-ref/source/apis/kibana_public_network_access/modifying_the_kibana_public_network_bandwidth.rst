:original_name: UpdateAlterKibana.html

.. _UpdateAlterKibana:

Modifying the Kibana Public Network Bandwidth
=============================================

Function
--------

This API is used to modify the public network bandwidth of Kibana.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/publickibana/bandwidth

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose Kibana public network bandwidth you want to modify.                                                      |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+----------------------------------------------------------------------------------------------------------------------------+-------------+
   | Parameter | Mandatory | Type                                                                                                                       | Description |
   +===========+===========+============================================================================================================================+=============+
   | bandWidth | Yes       | :ref:`UpdatePublicKibanaBandwidthReqBandWidth <updatealterkibana__request_updatepublickibanabandwidthreqbandwidth>` object | Bandwidth.  |
   +-----------+-----------+----------------------------------------------------------------------------------------------------------------------------+-------------+

.. _updatealterkibana__request_updatepublickibanabandwidthreqbandwidth:

.. table:: **Table 3** UpdatePublicKibanaBandwidthReqBandWidth

   ========= ========= ======= ===================
   Parameter Mandatory Type    Description
   ========= ========= ======= ===================
   size      Yes       Integer New bandwidth size.
   ========= ========= ======= ===================

Response Parameters
-------------------

None

Example Requests
----------------

Modify the Kibana public network bandwidth.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/publickibana/bandwidth

   {
     "bandWidth" : {
       "size" : 5
     },
     "isAutoPay" : 1
   }

Example Responses
-----------------

None

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
