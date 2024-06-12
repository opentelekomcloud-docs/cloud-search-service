:original_name: css_03_0088.html

.. _css_03_0088:

Scaling in a Cluster By Removing Specified Nodes
================================================

Function
--------

This API is used to scale in a cluster by removing specified nodes. Yearly/Monthly clusters do not support the removal of specified nodes by calling this API.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/node/offline

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to scale in                                             |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-----------------+-----------------+------------------+---------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type             | Description                                                                                                   |
   +=================+=================+==================+===============================================================================================================+
   | shrinkNodes     | Yes             | Array of strings | ID of the node you want to remove.                                                                            |
   |                 |                 |                  |                                                                                                               |
   |                 |                 |                  | Obtain the **ID** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`. |
   +-----------------+-----------------+------------------+---------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

.. code-block::

   {
     "shrinkNodes" : [ "2077bdf3-b90d-412e-b460-635b9b159c11" ]
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
