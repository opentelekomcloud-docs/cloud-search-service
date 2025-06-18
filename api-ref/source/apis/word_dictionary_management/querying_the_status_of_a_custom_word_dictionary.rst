:original_name: ShowIkThesaurus.html

.. _ShowIkThesaurus:

Querying the Status of a Custom Word Dictionary
===============================================

Function
--------

This API is used to query the loading status of a custom word dictionary.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/thesaurus

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | ID of the cluster whose word dictionary status you want to query                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`.                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                               |
   +=======================+=======================+===========================================================================+
   | status                | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Loading status.                                                           |
   |                       |                       |                                                                           |
   |                       |                       | **Options**:                                                              |
   |                       |                       |                                                                           |
   |                       |                       | -  **Init** indicates initialization is in progress.                      |
   |                       |                       |                                                                           |
   |                       |                       | -  **Loaded** indicates that the loading succeeded.                       |
   |                       |                       |                                                                           |
   |                       |                       | -  **Loading** indicates that the loading is in progress.                 |
   |                       |                       |                                                                           |
   |                       |                       | -  **Failed** indicates that the loading failed.                          |
   |                       |                       |                                                                           |
   |                       |                       | -  **NeedReboot** indicates that a cluster restart is required.           |
   |                       |                       |                                                                           |
   |                       |                       | -  **Undefined** indicates an undefined state.                            |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | bucket                | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | The OBS bucket that stores the word dictionary file that is last updated. |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | mainObj               | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Main word dictionary file                                                 |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | stopObj               | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Stop word dictionary file.                                                |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | synonymObj            | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Synonym dictionary file.                                                  |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | staticMainObj         | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Static main word dictionary file                                          |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | staticStopObj         | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Static main word dictionary file                                          |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | extraMainObj          | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Extra main word dictionary file                                           |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | extraStopObj          | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Extra stop word dictionary                                                |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | updateTime            | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Latest update time of a dictionary.                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | updateDetails         | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Update details.                                                           |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | clusterId             | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | ID of the cluster where a custom word dictionary you want to configure.   |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | operateStatus         | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | Operation status.                                                         |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | id                    | String                | **Parameter description**:                                                |
   |                       |                       |                                                                           |
   |                       |                       | ID of the word dictionary.                                                |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+

Example Requests
----------------

Query the loading status of a custom word dictionary.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/{cluster_id}/thesaurus

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "status" : "Loaded",
     "operateStatus" : "success",
     "id" : "e766bd5a-79b0-4d1a-8402-fdeb017a36d1",
     "bucket" : "test-bucket",
     "mainObj" : "word/main.txt",
     "stopObj" : "word/stop.txt",
     "synonymObj" : "word/synonym.txt",
     "staticMainObj" : "Unused",
     "staticStopObj" : "Unused",
     "extraMainObj" : "Unused",
     "extraStopObj" : "Unused",
     "updateTime" : 1521184757000,
     "updateDetails" : "allinstancesareloadedsuccessfully.",
     "clusterId" : "ea244205-d641-45d9-9dcb-ab2236bcd07e"
   }

Status Codes
------------

+-------------+---------------------------------------------------------------------+
| Status Code | Description                                                         |
+=============+=====================================================================+
| 200         | Request succeeded.                                                  |
+-------------+---------------------------------------------------------------------+
| 500         | The server is able to receive but unable to understand the request. |
+-------------+---------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
