:original_name: css_03_0122.html

.. _css_03_0122:

Modifying the Kibana Public Network Bandwidth
=============================================

Function
--------

This API is used to modify the public network bandwidth of Kibana.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/publickibana/bandwidth

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose Kibana public network bandwidth you want to modify.        |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------+-----------+----------------------------------------------------------------------------------------------------------------------+-------------+
   | Parameter | Mandatory | Type                                                                                                                 | Description |
   +===========+===========+======================================================================================================================+=============+
   | bandWidth | Yes       | :ref:`UpdatePublicKibanaBandwidthReqBandWidth <css_03_0122__request_updatepublickibanabandwidthreqbandwidth>` object | Bandwidth.  |
   +-----------+-----------+----------------------------------------------------------------------------------------------------------------------+-------------+

.. _css_03_0122__request_updatepublickibanabandwidthreqbandwidth:

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

.. code-block::

   {
     "bandWidth" : {
       "size" : 5
     }
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
