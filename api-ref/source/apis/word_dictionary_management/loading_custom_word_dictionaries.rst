:original_name: CreateLoadIkThesaurus.html

.. _CreateLoadIkThesaurus:

Loading Custom Word Dictionaries
================================

Function
--------

This API is used to load a custom word dictionary stored in OBS.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/thesaurus

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                                      |
   +============+===========+========+==================================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster where a custom word dictionary you want to configure.                                                          |
   +------------+-----------+--------+----------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter          | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                         |
   +====================+=================+=================+=====================================================================================================================================================================================================================================================================================================================+
   | bucketName         | Yes             | String          | OBS bucket where the word dictionary file is stored. (The bucket type must be **Standard** or **Infrequent Access**. **Archive** is not supported).                                                                                                                                                                 |
   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | mainObject         | No              | String          | Main word dictionary file, which must be a text file encoded in UTF-8 without BOM. Each line contains one word. The maximum file size is 100 MB.                                                                                                                                                                    |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | Modify the parameters of at least one of the seven word dictionaries. Note: Passing an empty "" character string will clear the word dictionary. Passing nothing or null will leave the word dictionary unchanged.                                                                                                  |
   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | stopObject         | No              | String          | Stop word dictionary file, which must be a text file encoded in UTF-8 without BOM. Each line contains one sub-word. The maximum file size is 100 MB.                                                                                                                                                                |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | At least one of the seven word dictionary parameters must be modified. Note: Passing an empty "" character string will clear the word dictionary. Passing nothing or null will leave the word dictionary unchanged.                                                                                                 |
   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | synonymObject      | No              | String          | Synonym dictionary file, which must be a text file encoded in UTF-8 without BOM. Each line contains one group of synonyms. The maximum file size is 100 MB.                                                                                                                                                         |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | At least one of the seven word dictionary parameters must be modified. Note: Passing an empty "" character string will clear the word dictionary. Passing nothing or null will leave the word dictionary unchanged.                                                                                                 |
   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | static_main_object | No              | String          | Static main word dictionary file, which must be a text file encoded in UTF-8 without BOM. Each line contains one word. The maximum file size is 100 MB.                                                                                                                                                             |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | Modify the parameters of at least one of the seven word dictionaries. Note: Passing an empty "" character string will clear the word dictionary. Passing nothing or null will leave the word dictionary unchanged. Only new clusters created after this word dictionary function was brought online are supported.  |
   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | static_stop_object | No              | String          | Static stop word dictionary file, which must be a text file encoded in UTF-8 without BOM. Each line contains one word. The maximum file size is 100 MB.                                                                                                                                                             |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | Modify the parameters of at least one of the seven word dictionaries. Note: Passing an empty "" character string will clear the word dictionary. Passing nothing or null will leave the word dictionary unchanged. Only new clusters created after this word dictionary function was brought online are supported.  |
   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | extra_main_object  | No              | String          | Extra main word dictionary file, which must be a text file encoded in UTF-8 without BOM. Each line contains one word. The maximum file size is 100 MB.                                                                                                                                                              |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | At least one of the seven word dictionary parameters must be modified. Note: Passing an empty "" character string will clear the word dictionary. Passing nothing or null will leave the word dictionary unchanged. Only new clusters created after this word dictionary function was brought online are supported. |
   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | extra_stop_object  | No              | String          | Extra stop word dictionary file, which must be a text file encoded in UTF-8 without BOM. Each line contains one word. The maximum file size is 100 MB.                                                                                                                                                              |
   |                    |                 |                 |                                                                                                                                                                                                                                                                                                                     |
   |                    |                 |                 | At least one of the seven word dictionary parameters must be modified. Note: Passing an empty "" character string will clear the word dictionary. Passing nothing or null will leave the word dictionary unchanged. Only new clusters created after this word dictionary function was brought online are supported. |
   +--------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

Enable and configure the word dictionary.

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/thesaurus

   {
     "bucketName" : "test-bucket",
     "mainObject" : "word/main.txt",
     "stopObject" : "word/stop.txt",
     "synonymObject" : "word/synonym.txt",
     "static_main_object" : "word/staticMain.txt",
     "static_stop_object" : "word/staticStop.txt",
     "extra_main_object" : "word/extraMain.txt",
     "extra_stop_object" : "word/extraStop.txt"
   }

Example Responses
-----------------

None

Status Codes
------------

+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                           |
+=============+=======================================================================================================================================================================+
| 200         | Request succeeded.                                                                                                                                                    |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403         | Request rejected.The server has received the request and understood it, but refused to respond to it. The client should not repeat the request without modifications. |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 500         | The server is able to receive the request but unable to understand the request.                                                                                       |
+-------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
