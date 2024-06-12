:original_name: css_03_0122.html

.. _css_03_0122:

Modifying the Kibana Public Network Bandwidth
=============================================

Function
--------

This API is used to modify the Kibana public network bandwidth.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/publickibana/bandwidth

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to modify the Kibana public network bandwidth.     |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------+-----------+----------------------------------------------------------------------------------------------------------------------+-------------+
   | Parameter | Mandatory | Type                                                                                                                 | Description |
   +===========+===========+======================================================================================================================+=============+
   | bandWidth | Yes       | :ref:`UpdatePublicKibanaBandwidthReqBandWidth <css_03_0122__request_updatepublickibanabandwidthreqbandwidth>` object | Bandwidth   |
   +-----------+-----------+----------------------------------------------------------------------------------------------------------------------+-------------+

.. _css_03_0122__request_updatepublickibanabandwidthreqbandwidth:

.. table:: **Table 3** UpdatePublicKibanaBandwidthReqBandWidth

   ========= ========= ======= ==================
   Parameter Mandatory Type    Description
   ========= ========= ======= ==================
   size      Yes       Integer New bandwidth size
   ========= ========= ======= ==================

Response Parameters
-------------------

None

Request Example
---------------

-  .. code-block::

      {
        "bandWidth" : {
          "size" : 5
        },
        "isAutoPay" : 1
      }

-  .. code-block::

      {
        "bandWidth" : {
          "size" : 5
        }
      }

Response Example
----------------

None

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
