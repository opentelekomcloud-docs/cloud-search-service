:original_name: UpdateFlavor.html

.. _UpdateFlavor:

Changing Specifications
=======================

Function
--------

This API is used to modify the specifications of a cluster. Only the nodes of the ESS type can be modified.

.. note::

   All mission-critical data has been backed up before a disk change. This is to prevent data loss.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/flavor

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose specifications you want to change.                                                                       |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter              | Mandatory       | Type            | Description                                                                                                                                                                               |
   +========================+=================+=================+===========================================================================================================================================================================================+
   | newFlavorId            | Yes             | String          | When operationType is set to vm, newFlavorId indicates the node flavor ID after the change.                                                                                               |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | This parameter is obtained by calling the :ref:`Obtaining the Instance Specifications List <listflavors>` API. The API selects a flavor_id based on the values of the **name** attribute. |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | The old and new node specifications must be under the same Elasticsearch engine version.                                                                                                  |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | When operationType is set to volume, newFlavorId indicates the new disk type after the change. The following disk types are supported:                                                    |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  COMMON: common I/O                                                                                                                                                                     |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  HIGH: high I/O                                                                                                                                                                         |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  ULTRAHIGH: ultra-high I/O                                                                                                                                                              |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  ESSD: ultra-fast SSD                                                                                                                                                                   |
   +------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | operationType          | No              | String          | Operation type. The value can be vm or volume. The default value is vm.                                                                                                                   |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  vm: Change the node flavor.                                                                                                                                                            |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  volume: Change the disk type.                                                                                                                                                          |
   +------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | needCheckReplica       | No              | Boolean         | Indicates whether to verify replicas. Its value can be **true** or **false**. This function is enabled by default.                                                                        |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  \*\ *true*: Enable the replicas verification.                                                                                                                                          |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  **false**: Disable the replicas verification.                                                                                                                                          |
   +------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | needCheckClusterStatus | No              | Boolean         | Description: Whether to check the cluster status. The value can be true or false. This function is enabled by default.                                                                    |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  true: Cluster status verification is enabled.                                                                                                                                          |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  false: Cluster status verification is ignored.                                                                                                                                         |
   +------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | clusterLoadCheck       | No              | Boolean         | Whether to check the cluster load. The value can be **true** or **false**. The default value is **true**.                                                                                 |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  **true**: enable cluster load check.                                                                                                                                                   |
   |                        |                 |                 |                                                                                                                                                                                           |
   |                        |                 |                 | -  **true**: skip cluster load check.                                                                                                                                                     |
   +------------------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

-  .. code-block:: text

      POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/flavor

      {
        "needCheckReplica" : false,
        "newFlavorId" : "35b060a4-f152-48ce-8773-36559ceb81f2",
        "isAutoPay" : 1,
        "needCheckClusterStatus" : true
      }

-  .. code-block:: text

      POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/flavor

      {
        "needCheckReplica" : false,
        "newFlavorId" : "ULTRAHIGH",
        "operationType" : "volume",
        "isAutoPay" : 1,
        "clusterLoadCheck" : true
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
