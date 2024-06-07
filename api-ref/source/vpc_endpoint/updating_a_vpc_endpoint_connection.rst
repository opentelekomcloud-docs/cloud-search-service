:original_name: css_03_0113.html

.. _css_03_0113:

Updating a VPC Endpoint Connection
==================================

Function
--------

This API is used to update a VPC endpoint connection.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/vpcepservice/connections

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to update the VPC endpoint                         |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------------+-----------------+------------------+----------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                        |
   +=================+=================+==================+====================================================+
   | action          | Yes             | String           | Expected operation.                                |
   |                 |                 |                  |                                                    |
   |                 |                 |                  | -  **receive**: accept the VPC endpoint connection |
   |                 |                 |                  | -  **reject**: reject the VPC endpoint connection  |
   +-----------------+-----------------+------------------+----------------------------------------------------+
   | endpointIdList  | Yes             | Array of strings | VPC endpoint IDs list                              |
   +-----------------+-----------------+------------------+----------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

.. code-block::

   {
     "action" : "receive",
     "endpointIdList" : [ "f132bb14-e1d5-4f25-9f7c-a29e4c8effd4" ]
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
