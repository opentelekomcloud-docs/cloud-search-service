:original_name: ShowResizeFlavors.html

.. _ShowResizeFlavors:

Querying Available Node Specifications for a Cluster
====================================================

Function
--------

This API is used to query available alternative node specifications for a specified cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/resize-flavors

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Constraints**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Value range**:                                                                                                                 |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`.                                                           |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                         |
   +=================+=================+=================+=====================================================================================================================================+
   | clusterId       | Yes             | String          | **Definition**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | ID of the cluster to be queried. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Value range**:                                                                                                                    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Cluster ID.                                                                                                                         |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default value**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+
   | type            | No              | String          | **Definition**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Cluster node type.                                                                                                                  |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Constraints**                                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Range**                                                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | -  **ess**: data node.                                                                                                              |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | -  **ess-cold**: cold data node.                                                                                                    |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | -  **ess-client**: client node.                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | -  **ess-master**: master node.                                                                                                     |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | -  **lgs**: Logstash node.                                                                                                          |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | **Default Value**                                                                                                                   |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Elasticsearch/OpenSearch cluster: **ess**                                                                                           |
   |                 |                 |                 |                                                                                                                                     |
   |                 |                 |                 | Logstash cluster: **lgs**                                                                                                           |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 3** Response body parameters

   +-----------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
   | Parameter             | Type                                                                                                        | Description           |
   +=======================+=============================================================================================================+=======================+
   | id                    | String                                                                                                      | **Definition**:       |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | Engine type ID.       |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | **Value range**:      |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | N/A                   |
   +-----------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
   | dbname                | String                                                                                                      | **Definition**:       |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | Engine name.          |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | **Value range**:      |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | N/A                   |
   +-----------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+
   | versions              | Array of :ref:`ResizeFlavorRspVersionBody <showresizeflavors__response_resizeflavorrspversionbody>` objects | **Definition**:       |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | Version list.         |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | **Value range**:      |
   |                       |                                                                                                             |                       |
   |                       |                                                                                                             | N/A                   |
   +-----------------------+-------------------------------------------------------------------------------------------------------------+-----------------------+

.. _showresizeflavors__response_resizeflavorrspversionbody:

.. table:: **Table 4** ResizeFlavorRspVersionBody

   +-----------------------+---------------------------------------------------------------------------------+------------------------------+
   | Parameter             | Type                                                                            | Description                  |
   +=======================+=================================================================================+==============================+
   | id                    | String                                                                          | **Definition**:              |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | Engine version ID.           |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | **Value range**:             |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | N/A                          |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------+
   | name                  | String                                                                          | **Definition**:              |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | Engine version name.         |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | **Value range**:             |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | N/A                          |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------+
   | flavors               | Array of :ref:`ResizeFlavor <showresizeflavors__response_resizeflavor>` objects | **Definition**:              |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | Target flavor of the change. |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | **Value range**:             |
   |                       |                                                                                 |                              |
   |                       |                                                                                 | N/A                          |
   +-----------------------+---------------------------------------------------------------------------------+------------------------------+

.. _showresizeflavors__response_resizeflavor:

.. table:: **Table 5** ResizeFlavor

   +-----------------------+-----------------------+--------------------------------------------------------+
   | Parameter             | Type                  | Description                                            |
   +=======================+=======================+========================================================+
   | str_id                | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Flavor ID.                                             |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | cpu                   | Integer               | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Number of vCPUs available with an instance.            |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | ram                   | Integer               | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Memory size of an instance. Unit: GB.                  |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | name                  | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Flavor name.                                           |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | region                | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Regions where the node flavor is available.            |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | diskrange             | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Disk capacity of an instance, in GB.                   |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | N/A                                                    |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | typename              | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Node type.                                             |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | -  **ess**: data node                                  |
   |                       |                       |                                                        |
   |                       |                       | -  **ess-cold**: cold data node                        |
   |                       |                       |                                                        |
   |                       |                       | -  **ess-client**: client node                         |
   |                       |                       |                                                        |
   |                       |                       | -  **ess-master**: master node                         |
   |                       |                       |                                                        |
   |                       |                       | -  **lgs**: Logstash node                              |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | condOperationStatus   | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Flavor sales status.                                   |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | -  **normal**: The flavor is in normal commercial use. |
   |                       |                       |                                                        |
   |                       |                       | -  **sellout**: The flavor has been sold out.          |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | localdisk             | String                | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Whether the node uses local disks.                     |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | -  **false**: non-local disk flavor.                   |
   |                       |                       |                                                        |
   |                       |                       | -  **true**: local disk flavor.                        |
   +-----------------------+-----------------------+--------------------------------------------------------+
   | edge                  | Boolean               | **Definition**:                                        |
   |                       |                       |                                                        |
   |                       |                       | Whether this is a node flavor for edge deployments.    |
   |                       |                       |                                                        |
   |                       |                       | **Value range**:                                       |
   |                       |                       |                                                        |
   |                       |                       | -  **false**: central AZ flavor.                       |
   |                       |                       |                                                        |
   |                       |                       | -  **true**: edge AZ flavor.                           |
   +-----------------------+-----------------------+--------------------------------------------------------+

Example Requests
----------------

Querying Available Node Specifications for a Cluster

.. code-block:: text

   GET /v1.0/{project_id}/resize-flavors?clusterId=xxx

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "id" : "cf7e2c8f-096c-4fcf-b174-1ebe060679fb",
     "dbname" : "elasticsearch",
     "versions" : [ {
       "id" : "01f53413-0a58-4b0c-848a-f625846bae23",
       "name" : "7.10.2",
       "flavors" : [ {
         "cpu" : 2,
         "ram" : 8,
         "name" : "ess.spec-2u8g",
         "region" : "azcode-1",
         "typename" : "ess",
         "diskrange" : "40,800",
         "condOperationStatus" : "normal",
         "localdisk" : "false",
         "edge" : false,
         "str_id" : "b58dfcfb-5f73-4f05-8c06-5171b12fd618="
       } ]
     } ]
   }

Status Codes
------------

+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                     |
+===================================+=================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                              |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | The request is invalid.                                                                                                                                         |
|                                   |                                                                                                                                                                 |
|                                   | Modify the request and then try again.                                                                                                                          |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | The request is rejected.                                                                                                                                        |
|                                   |                                                                                                                                                                 |
|                                   | The server has received the request and understood it, but the server refuses to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
