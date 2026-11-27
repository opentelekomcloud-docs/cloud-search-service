:original_name: UpdateExtendInstanceStorage.html

.. _UpdateExtendInstanceStorage:

Adding Instances and Expanding Instance Storage Capacity
========================================================

Function
--------

If a cluster struggles to maintain performance in the face of rapid data growth or sustained high memory usage, you can add more nodes to it or increase the storage capacity of its existing nodes.

Constraints
-----------

-  The node storage capacity of a cluster can only be increased—not decreased. Select an appropriate node storage capacity based on the data volume and projected data growth.

-  For a pay-per-use cluster, you cannot increase the number of nodes and node storage capacity at the same time. .

-  The storage capacity of the master and client nodes in a cluster cannot be expanded.

-  The storage capacity of data nodes that use local disks cannot be expanded.

-  For a Logstash cluster, you can only add more nodes, but cannot increase the storage capacity of its nodes.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/role_extend

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                            |
   +=================+=================+=================+========================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                         |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.       |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Constraints**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Range**                                                                                                                              |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Default Value**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                         |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | ID of the cluster to be scaled out. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Constraints**                                                                                                                        |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Range**                                                                                                                              |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                          |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | **Default Value**                                                                                                                      |
   |                 |                 |                 |                                                                                                                                        |
   |                 |                 |                 | N/A                                                                                                                                    |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type                                                                                               | Description                                                                                                                                                                                                      |
   +=================+=================+====================================================================================================+==================================================================================================================================================================================================================+
   | grow            | Yes             | Array of :ref:`RoleExtendGrowReq <updateextendinstancestorage__request_roleextendgrowreq>` objects | **Definition**                                                                                                                                                                                                   |
   |                 |                 |                                                                                                    |                                                                                                                                                                                                                  |
   |                 |                 |                                                                                                    | Detailed description of the cluster scale-out request, including fields such as **type**, **nodesize**, and **disksize**, used to specify the node type, number of instances, and storage capacity to be scaled. |
   |                 |                 |                                                                                                    |                                                                                                                                                                                                                  |
   |                 |                 |                                                                                                    | **Constraints**                                                                                                                                                                                                  |
   |                 |                 |                                                                                                    |                                                                                                                                                                                                                  |
   |                 |                 |                                                                                                    | N/A                                                                                                                                                                                                              |
   |                 |                 |                                                                                                    |                                                                                                                                                                                                                  |
   |                 |                 |                                                                                                    | **Range**                                                                                                                                                                                                        |
   |                 |                 |                                                                                                    |                                                                                                                                                                                                                  |
   |                 |                 |                                                                                                    | N/A                                                                                                                                                                                                              |
   |                 |                 |                                                                                                    |                                                                                                                                                                                                                  |
   |                 |                 |                                                                                                    | **Default Value**                                                                                                                                                                                                |
   |                 |                 |                                                                                                    |                                                                                                                                                                                                                  |
   |                 |                 |                                                                                                    | N/A                                                                                                                                                                                                              |
   +-----------------+-----------------+----------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. _updateextendinstancestorage__request_roleextendgrowreq:

.. table:: **Table 3** RoleExtendGrowReq

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                     |
   +=================+=================+=================+=================================================================================================================================================================================================================================================================+
   | type            | Yes             | String          | **Definition**                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Type of the node to be added.                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | You can only add instances, rather than increase storage capacity, on nodes of the **ess-master**, **ess-client**, and **lgs** types.                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | The value must be a valid node type and can contain only lowercase letters and hyphens (-).                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ess**: data node                                                                                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  **lgs**: Logstash nodes in Logstash clusters                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | You can select multiple node types, but cannot select the same node for different roles.                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 |    **lgs** cannot be combined with other options.                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | nodesize        | Yes             | Integer         | **Definition**                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Number of instances to be added.                                                                                                                                                                                                                                |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | After scaling, the number of nodes of each type must meet the following requirements:                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  Data nodes: If the cluster does not have master nodes, the value ranges from 1 to 32. Otherwise, the value ranges from 1 to 200.                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  Master nodes: 3, 5, 7, or 9 (must be an odd number from 3 to 9)                                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  Client nodes: 1 to 64                                                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  Cold data nodes: 1 to 32                                                                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  Logstash nodes: 1 to 100                                                                                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | disksize        | Yes             | Integer         | **Definition**                                                                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | Storage capacity to be added, in GB.                                                                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Constraints**                                                                                                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  The sum of the original instance storage capacity plus the expanded instance storage capacity cannot exceed the default upper limit of storage capacity set during cluster creation. If there is no need to add more instances, set this parameter to **0**. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  The scale-out step of **ess** and **ess-cold** nodes is 20.                                                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  The storage capacity of **ess-master** and **ess-client** nodes cannot be expanded.                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | -  Logstash does not support storage capacity expansion.                                                                                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Range**                                                                                                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | **Default Value**                                                                                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                                                                                                 |
   |                 |                 |                 | N/A                                                                                                                                                                                                                                                             |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 4** Response body parameters

   +-----------------------+-----------------------+-----------------------+
   | Parameter             | Type                  | Description           |
   +=======================+=======================+=======================+
   | id                    | String                | **Definition**:       |
   |                       |                       |                       |
   |                       |                       | Cluster ID.           |
   |                       |                       |                       |
   |                       |                       | **Value range**:      |
   |                       |                       |                       |
   |                       |                       | N/A                   |
   +-----------------------+-----------------------+-----------------------+

Example Requests
----------------

Change the number of instances and storage capacity of the current cluster.

.. code-block:: text

   POST https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/role_extend

   {
     "grow" : [ {
       "type" : "ess",
       "nodesize" : 0,
       "disksize" : 40
     } ],
     "is_auto_pay" : 1
   }

Example Responses
-----------------

**Status code: 200**

.. code-block::

   {
     "id" : "4f3deec3-efa8-4598-bf91-560aad1377a3"
   }

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
