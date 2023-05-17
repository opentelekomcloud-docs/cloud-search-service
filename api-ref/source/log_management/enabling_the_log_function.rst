:original_name: css_03_0094.html

.. _css_03_0094:

Enabling the Log Function
=========================

Function
--------

This API is used to enable the log function.

URI
---

POST /v1.0/{project_id}/clusters/{cluster_id}/logs/open

.. table:: **Table 1** Path Parameters

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster whose log function you want to enable.                           |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +-------------+-----------+--------+----------------------------------------------------------------------------------+
   | Parameter   | Mandatory | Type   | Description                                                                      |
   +=============+===========+========+==================================================================================+
   | agency      | Yes       | String | Agency name. You can create an agency to allow CSS to call other cloud services. |
   +-------------+-----------+--------+----------------------------------------------------------------------------------+
   | logBasePath | Yes       | String | Storage path of backed up logs in the OBS bucket.                                |
   +-------------+-----------+--------+----------------------------------------------------------------------------------+
   | logBucket   | Yes       | String | Name of the OBS bucket for storing logs.                                         |
   +-------------+-----------+--------+----------------------------------------------------------------------------------+

Response Parameters
-------------------

None

Example Requests
----------------

.. code-block::

   {
     "agency" : "css_obs_agency",
     "logBasePath" : "css/log",
     "logBucket" : "000-words"
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                        |
+===================================+====================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                   |
|                                   |                                                                                                                                    |
|                                   | Modify the request before retry.                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                       |
|                                   |                                                                                                                                    |
|                                   | The resource that the client attempts to create already exists, or the update request fails to be processed because of a conflict. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
