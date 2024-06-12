:original_name: css_03_0098.html

.. _css_03_0098:

Modifying Basic Log Configurations
==================================

Function
--------

This API is used to modify basic log configurations.

Debugging
---------

You can debug this API in . Automatic authentication is supported.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/logs/settings

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster that you want to change the basic log configurations             |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameter

   +-------------+-----------+--------+----------------------------------------------------------------------------------+
   | Parameter   | Mandatory | Type   | Description                                                                      |
   +=============+===========+========+==================================================================================+
   | agency      | Yes       | String | Agency name. You can create an agency to allow CSS to call other cloud services. |
   +-------------+-----------+--------+----------------------------------------------------------------------------------+
   | logBasePath | Yes       | String | Storage path of backup logs in the OBS bucket                                    |
   +-------------+-----------+--------+----------------------------------------------------------------------------------+
   | logBucket   | Yes       | String | Name of the OBS bucket for storing logs                                          |
   +-------------+-----------+--------+----------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Request Example
---------------

.. code-block::

   {
     "agency" : "css_obs_agency",
     "logBasePath" : "css/log",
     "logBucket" : "000-words"
   }

Response Example
----------------

None

Status Codes
------------

+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                                                                         |
+===================================+=====================================================================================================================================================================================+
| 200                               | The request is processed successfully.                                                                                                                                              |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                                                                    |
|                                   |                                                                                                                                                                                     |
|                                   | Modify the request instead of retrying.                                                                                                                                             |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request cannot be processed due to a conflict.                                                                                                                                  |
|                                   |                                                                                                                                                                                     |
|                                   | This status code indicates that the resource that the client attempts to create already exists, or the request fails to be processed because of the update of the conflict request. |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server does not meet one of the requirements that the requester puts on the request.                                                                                            |
+-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
