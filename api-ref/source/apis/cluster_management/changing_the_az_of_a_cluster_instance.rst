:original_name: UpdateAzByInstanceType.html

.. _UpdateAzByInstanceType:

Changing the AZ of a Cluster Instance
=====================================

Function
--------

This API is used to change the AZ by specifying node types.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/inst-type/{inst_type}/azmigrate

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                      |
   +=================+=================+=================+==================================================================================================================================+
   | project_id      | Yes             | String          | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | Cluster ID.                                                                                                                      |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+
   | inst_type       | Yes             | String          | Types of nodes whose AZ is to be changed. Supported values:                                                                      |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **all**: all node types                                                                                                       |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **ess**: data node                                                                                                            |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **ess-cold**: cold data node                                                                                                  |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **ess-client**: client node                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | -  **ess-master**: master node                                                                                                   |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | .. note::                                                                                                                        |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 |    All mission-critical data has been backed up before an AZ switchover. This is to prevent data loss.                           |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | Parameter            | Mandatory       | Type            | Description                                                                      |
   +======================+=================+=================+==================================================================================+
   | source_az            | Yes             | String          | AZ where the node is located.                                                    |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | target_az            | Yes             | String          | Destination AZ of nodes.                                                         |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | migrate_type         | Yes             | String          | AZ migration mode:                                                               |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **multi_az_change**: HA reconstruction                                        |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | -  **az_migrate**: AZ migration                                                  |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | agency               | Yes             | String          | Agency name. You can create an agency to allow CSS to call other cloud services. |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+
   | indices_backup_check | No              | Boolean         | Indicates whether to perform full index snapshot backup check.                   |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | true: Check full index snapshot backup.                                          |
   |                      |                 |                 |                                                                                  |
   |                      |                 |                 | false: Do not perform full index snapshot backup check.                          |
   +----------------------+-----------------+-----------------+----------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Switch the AZ of the current cluster.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/inst-type/all/azmigrate

   {
     "source_az" : "cn-north-4c",
     "target_az" : "cn-north-4a",
     "migrate_type" : "az_migrate",
     "agency" : "css-test-agency"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                                  |
+===================================+==============================================================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                                                           |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                             |
|                                   |                                                                                                                                                                                              |
|                                   | The client should not repeat the request without modifications.                                                                                                                              |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | The request is rejected. The server has received the request and understood it, but the server is refusing to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
