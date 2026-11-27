:original_name: UpdateInstance.html

.. _UpdateInstance:

Replacing a Node
================

Function
--------

This API is used to replace a failed node.

If a node in an Elasticsearch or OpenSearch cluster is faulty, you can replace it to restore services.

The node replacement process is as follows:

#. Migrate data from the node that needs to be replaced to other available nodes.

#. Rebuild the node using the original ID, IP address, specifications, and AZ.

#. Add the new node into the cluster. The system automatically triggers a shard reallocation, migrating some of the shards to the new node.

This process does not interrupt services because data is migrated from the replaced node to other available nodes.

.. note::

   All mission-critical data has been backed up before a node replacement. This is to prevent data loss.

Constraints
-----------

-  Only one node can be replaced at a time. Each new node is rebuilt using the ID, IP address, specifications, and AZ of the node it is replacing.

-  The configurations you modified manually will not be retained after node replacement. For example, if you have manually added a return route for the original node, you need to add it again for the new node after the node replacement is complete.

-  If the node you want to replace is a data node or cold data node, pay attention to the following precautions:

-  When a data node or cold data node is replaced, its data is first migrated to other data nodes. This means the total number of data nodes and cold data nodes must be greater than the maximum number of index replicas plus 1.

-  Elasticsearch clusters whose version is earlier than 7.6.2 cannot have closed indexes. Otherwise, their data nodes or cold data nodes cannot be replaced.

-  In the AZ that contains the data node or cold data node to be replaced, there has to be at least another data node or cold data node.

-  If the cluster has not master nodes, the total number of data nodes plus cold data nodes must be at least three.

-  The precautions above do not apply if you are replacing a faulty node, regardless of its type. This is because faulty nodes are not included in **\_cat/nodes**.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/instance/{instance_id}/replace

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                     |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Constraints**                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Range**                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | Project ID of an account. The value contains 32 characters, consisting of lowercase letters and digits.                                              |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Default Value**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | ID of the cluster where nodes are to be replaced. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Constraints**                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Range**                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | The value is a UUID containing 36 characters.                                                                                                        |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Default Value**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
   | instance_id     | Yes             | String          | **Definition**                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | ID of the node to be replaced. Obtain the **ID** attribute in instances by referring to :ref:`Querying Cluster Details <showclusterdetail>`.         |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Constraints**                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Range**                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | **Default Value**                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                  |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                  |
   +=================+=================+=================+==============================================================================================================================================================================================+
   | migrateData     | No              | String          | **Definition**:                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | Whether to migrate data.                                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | **Constraints**:                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | **Value range**:                                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | -  true: Migrate data.                                                                                                                                                                       |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | -  false: Do not migrate data.                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | **Default value**:                                                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | true                                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | agency          | No              | String          | **Definition**                                                                                                                                                                               |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | Agency name. To store snapshots to an OBS bucket, you must have the required OBS access permissions. Select an IAM agency to grant the current account the permission to access and use OBS. |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | **Constraints**                                                                                                                                                                              |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | -  VPC permissions required by the agency: "``vpc:subnets:get``","``vpc:ports:*``".                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | -  This parameter is mandatory when the new IAM plane is connected, and is optional when the old IAM plane is connected.                                                                     |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | **Range**                                                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | The agency name can contain at most 64 characters. Only letters, digits, underscores (_), and hyphens (-) are allowed.                                                                       |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | **Default Value**                                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                                              |
   |                 |                 |                 | N/A                                                                                                                                                                                          |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

None

Example Requests
----------------

Replace a node.

.. code-block:: text

   PUT https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/instance/43e63449-339c-4280-a6e9-da36b0685995/replace?migrateData=true

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------+
| Status Code                       | Description                                                       |
+===================================+===================================================================+
| 200                               | Request succeeded.                                                |
+-----------------------------------+-------------------------------------------------------------------+
| 400                               | Invalid request.                                                  |
|                                   |                                                                   |
|                                   | The client should modify the request instead of re-initiating it. |
+-----------------------------------+-------------------------------------------------------------------+
| 404                               | The requested resource could not be found.                        |
|                                   |                                                                   |
|                                   | The client should modify the request instead of re-initiating it. |
+-----------------------------------+-------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
