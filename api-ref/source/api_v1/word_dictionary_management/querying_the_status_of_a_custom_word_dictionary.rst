:original_name: ShowIkThesaurus.html

.. _ShowIkThesaurus:

Querying the Status of a Custom Word Dictionary
===============================================

Function
--------

You can configure custom word dictionaries to support word segmentation. This gives the search engine enhanced performance when searching by keywords such as company names, for example, and buzzwords from social media. You can also search text data based on a synonym dictionary. CSS uses the IK and synonym analyzers. The IK analyzer uses a main word dictionary and a stop word dictionary. The synonym analyzer uses a synonym word dictionary. The IK analyzer uses the ik_max_word and ik_smart word segmentation policies. The synonym analyzer uses the ik_synonym word segmentation policy. This API is used to query the loading status of a custom word dictionary.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

GET /v1.0/{project_id}/clusters/{cluster_id}/thesaurus

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                         |
   +=================+=================+=================+=====================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                    |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | **Constraints**:                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | **Value range**:                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | Project ID of the account.                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | **Default value**:                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                                                 |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | ID of the cluster whose word dictionary status you want to query For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | **Constraints**:                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | **Value range**:                                                                                                                                                    |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | Cluster ID.                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | **Default value**:                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                     |
   |                 |                 |                 | N/A                                                                                                                                                                 |
   +-----------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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
   | status                | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Custom word dictionary loading status.                                    |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
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
   | bucket                | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | The OBS bucket that stores the word dictionary file that is last updated. |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | mainObj               | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Main word dictionary file.                                                |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | stopObj               | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Stop word dictionary file.                                                |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | synonymObj            | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Synonym dictionary file.                                                  |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | staticMainObj         | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Static main word dictionary file.                                         |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | staticStopObj         | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Static main word dictionary file.                                         |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | extraMainObj          | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Extra main word dictionary file.                                          |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | extraStopObj          | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Extra stop word dictionary.                                               |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | updateTime            | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Latest update time of a dictionary.                                       |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | updateDetails         | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | Word dictionary update details.                                           |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | clusterId             | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | ID of the cluster where a custom word dictionary you want to configure.   |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+
   | id                    | String                | **Definition**:                                                           |
   |                       |                       |                                                                           |
   |                       |                       | ID of the word dictionary.                                                |
   |                       |                       |                                                                           |
   |                       |                       | **Value range**:                                                          |
   |                       |                       |                                                                           |
   |                       |                       | N/A                                                                       |
   +-----------------------+-----------------------+---------------------------------------------------------------------------+

Example Requests
----------------

Query the loading status of a custom word dictionary.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/thesaurus

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "status" : "Loaded",
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
