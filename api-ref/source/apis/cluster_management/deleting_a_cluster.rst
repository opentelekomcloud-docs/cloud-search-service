:original_name: DeleteCluster.html

.. _DeleteCluster:

Deleting a Cluster
==================

Function
--------

This API is used to delete a cluster. All resources of the deleted cluster, including customer data, will be released. If you want to retain the data in a customer cluster, create a snapshot before deleting the cluster.

.. note::

   This API can also be used to unsubscribe from yearly/monthly clusters. Clusters frozen for public security reasons cannot be deleted. Deleting a cluster will also clear its data. Exercise caution.

URI
---

DELETE /v1.0/{project_id}/clusters/{cluster_id}

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster you want to delete.                                                                                            |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Example Requests
----------------

None

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+--------------------------------------------+
| Status Code                       | Description                                |
+===================================+============================================+
| 200                               | Request succeeded.                         |
+-----------------------------------+--------------------------------------------+
| 400                               | Invalid request.                           |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+
| 404                               | The requested resource could not be found. |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
