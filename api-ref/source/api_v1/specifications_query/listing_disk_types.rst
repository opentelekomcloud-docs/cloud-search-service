:original_name: ListDiskType.html

.. _ListDiskType:

Listing Disk Types
==================

Function
--------

Obtain the disk types supported by each AZ.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/disktypes

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
   |                 |                 |                 | Project ID of the account.                                                                                                       |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | **Default value**:                                                                                                               |
   |                 |                 |                 |                                                                                                                                  |
   |                 |                 |                 | N/A                                                                                                                              |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+--------------------------------------------------------------------+-----------------------+
   | Parameter             | Type                                                               | Description           |
   +=======================+====================================================================+=======================+
   | diskTypes             | Array of :ref:`DiskType <listdisktype__response_disktype>` objects | **Definition**:       |
   |                       |                                                                    |                       |
   |                       |                                                                    | Disk type list.       |
   |                       |                                                                    |                       |
   |                       |                                                                    | **Value range**:      |
   |                       |                                                                    |                       |
   |                       |                                                                    | N/A                   |
   +-----------------------+--------------------------------------------------------------------+-----------------------+

.. _listdisktype__response_disktype:

.. table:: **Table 3** DiskType

   +-----------------------+-----------------------+----------------------------+
   | Parameter             | Type                  | Description                |
   +=======================+=======================+============================+
   | availabilityZone      | String                | **Definition**:            |
   |                       |                       |                            |
   |                       |                       | Availability zone (AZ).    |
   |                       |                       |                            |
   |                       |                       | **Value range**:           |
   |                       |                       |                            |
   |                       |                       | N/A                        |
   +-----------------------+-----------------------+----------------------------+
   | volumeNames           | Array of strings      | **Definition**:            |
   |                       |                       |                            |
   |                       |                       | Storage type.              |
   |                       |                       |                            |
   |                       |                       | **Value range**:           |
   |                       |                       |                            |
   |                       |                       | -  **SAS**: high I/O       |
   |                       |                       |                            |
   |                       |                       | -  **SSD**: ultra-high I/O |
   |                       |                       |                            |
   |                       |                       | -  **ESSD**: extreme SSD   |
   +-----------------------+-----------------------+----------------------------+

Example Requests
----------------

Query the disk types supported in each availability zone (AZ).

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/disktypes

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "diskTypes" : [ {
       "availabilityZone" : "xx-north-1a",
       "volumeNames" : [ "SATA" ]
     }, {
       "availabilityZone" : "azcode-1",
       "volumeNames" : [ "SATA", "SAS" ]
     }, {
       "availabilityZone" : "azcode-1",
       "volumeNames" : [ "SATA", "SAS", "SSD" ]
     } ]
   }

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                          |
+===================================+======================================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | The request is invalid.                                                                                                                              |
|                                   |                                                                                                                                                      |
|                                   | The client should modify the request instead of re-initiating it.                                                                                    |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403                               | The request is rejected.                                                                                                                             |
|                                   |                                                                                                                                                      |
|                                   | The server has received the request and understood it, but refuses to respond to it. The client should not repeat the request without modifications. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
