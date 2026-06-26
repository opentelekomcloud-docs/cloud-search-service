:original_name: ShowClusterVolumeUsage.html

.. _ShowClusterVolumeUsage:

Query the disk usage of a cluster.
==================================

Function
--------

Query the disk usage of a cluster.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/volume

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                       |
   +=================+=================+=================+===================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`.                                                |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Constraints**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                               |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Value range**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`.                                                            |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Default value**:                                                                                                                |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                               |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | ID of the cluster to be updated. For details about how to obtain the cluster ID, see :ref:`Obtaining a Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Constraints**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                               |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Value range**:                                                                                                                  |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | To obtain the value, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                                           |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | **Default value**:                                                                                                                |
   |                 |                 |                 |                                                                                                                                   |
   |                 |                 |                 | N/A                                                                                                                               |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+------------------------------------------------------------------------------+--------------------------+
   | Parameter             | Type                                                                         | Description              |
   +=======================+==============================================================================+==========================+
   | diskInfoList          | Array of :ref:`DiskInfo <showclustervolumeusage__response_diskinfo>` objects | **Definition**:          |
   |                       |                                                                              |                          |
   |                       |                                                                              | Disk usage of each node. |
   |                       |                                                                              |                          |
   |                       |                                                                              | **Value range**:         |
   |                       |                                                                              |                          |
   |                       |                                                                              | N/A                      |
   +-----------------------+------------------------------------------------------------------------------+--------------------------+

.. _showclustervolumeusage__response_diskinfo:

.. table:: **Table 3** DiskInfo

   +-----------------------+-----------------------+------------------------------+
   | Parameter             | Type                  | Description                  |
   +=======================+=======================+==============================+
   | id                    | String                | **Definition**:              |
   |                       |                       |                              |
   |                       |                       | Node ID.                     |
   |                       |                       |                              |
   |                       |                       | **Value range**:             |
   |                       |                       |                              |
   |                       |                       | N/A                          |
   +-----------------------+-----------------------+------------------------------+
   | name                  | String                | **Definition**:              |
   |                       |                       |                              |
   |                       |                       | Node name.                   |
   |                       |                       |                              |
   |                       |                       | **Value range**:             |
   |                       |                       |                              |
   |                       |                       | N/A                          |
   +-----------------------+-----------------------+------------------------------+
   | diskCapacity          | String                | **Definition**:              |
   |                       |                       |                              |
   |                       |                       | Total node storage capacity. |
   |                       |                       |                              |
   |                       |                       | **Value range**:             |
   |                       |                       |                              |
   |                       |                       | N/A                          |
   +-----------------------+-----------------------+------------------------------+
   | diskUsed              | String                | **Definition**:              |
   |                       |                       |                              |
   |                       |                       | Used node storage capacity.  |
   |                       |                       |                              |
   |                       |                       | **Value range**:             |
   |                       |                       |                              |
   |                       |                       | N/A                          |
   +-----------------------+-----------------------+------------------------------+
   | percentage            | String                | **Definition**:              |
   |                       |                       |                              |
   |                       |                       | Node storage usage.          |
   |                       |                       |                              |
   |                       |                       | **Value range**:             |
   |                       |                       |                              |
   |                       |                       | N/A                          |
   +-----------------------+-----------------------+------------------------------+

Example Requests
----------------

Query the disk usage of each node in a cluster.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/{cluster_id}/volume

Example Responses
-----------------

**Status code: 200**

Returned value for querying the disk usage of each node in a cluster.

.. code-block::

   {
     "diskInfoList" : [ {
       "percentage" : "5.16",
       "diskCapacity" : "97.86",
       "diskUsed" : "5.05",
       "id" : "700915c3-15da-455f-9a6e-8b853b8665ac",
       "name" : "css-9062-ess-esn-1-1"
     } ]
   }

Status Codes
------------

+-------------+-----------------------------------------------------------------------+
| Status Code | Description                                                           |
+=============+=======================================================================+
| 200         | Returned value for querying the disk usage of each node in a cluster. |
+-------------+-----------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
