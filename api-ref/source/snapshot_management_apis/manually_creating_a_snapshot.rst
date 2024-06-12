:original_name: css_03_0033.html

.. _css_03_0033:

Manually Creating a Snapshot
============================

Function
--------

This API is used to manually create a snapshot.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster where index data is to be backed up.                             |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request
-------

:ref:`Table 2 <css_03_0033__table82481020121413>` describes the request parameters.

.. _css_03_0033__table82481020121413:

.. table:: **Table 2** Parameter description

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                  |
   +=================+=================+=================+==============================================================================================================================================================================================================================================================================================================================+
   | name            | Yes             | String          | Snapshot name. The snapshot name must start with a letter and contains 4 to 64 characters consisting of only lowercase letters, digits, hyphens (-), and underscores (_).                                                                                                                                                    |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | description     | No              | String          | Description of a snapshot. The value contains 0 to 256 characters, and angle brackets (<) and (>) are not allowed.                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | indices         | No              | String          | Name of the index to be backed up. Multiple index names are separated by commas (,). By default, data of all indices is backed up. You can use the asterisk (``*``) to back up data of certain indices. For example, if you enter **2018-06\***, then data of indices with the name prefix of **2018-06** will be backed up. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                              |
   |                 |                 |                 | The value contains 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?)`` are not allowed.                                                                                                                                                                                 |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response
--------

:ref:`Table 3 <css_03_0033__table4974113513176>` describes the response parameters.

.. _css_03_0033__table4974113513176:

.. table:: **Table 3** Parameter description

   +-----------+--------+-------------------------------------------------------------------------------------+
   | Parameter | Type   | Description                                                                         |
   +===========+========+=====================================================================================+
   | backup    | Object | Snapshot object. For details, see :ref:`Table 4 <css_03_0033__table6630232153613>`. |
   +-----------+--------+-------------------------------------------------------------------------------------+

.. _css_03_0033__table6630232153613:

.. table:: **Table 4** **backup** field data structure description

   ========= ====== ===================
   Parameter Type   Description
   ========= ====== ===================
   id        String ID of the snapshot.
   name      String Snapshot name.
   ========= ====== ===================

Examples
--------

Example request

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot
   {
       "name":"snapshot_001",
       "indices":"myindex1,myindex2",
       "description":""
   }

Example response

.. code-block::

   {
       "backup":{
          "id" : "9dc4f5c9-33c0-45c7-9378-ae35ae350682",
          "name": "snapshot_101"
       }
   }

Status Code
-----------

:ref:`Table 5 <css_03_0033__table1728411482811>` describes the status code.

.. _css_03_0033__table1728411482811:

.. table:: **Table 5** Status code

   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------+
   | Status Code           | Code                  | Status Code Description                                                                        |
   +=======================+=======================+================================================================================================+
   | 201                   | Created               | The request for creating a resource has been fulfilled.                                        |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------+
   | 500                   | InternalServerError   | The server is able to receive the request but it could not understand the request.             |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------+
   | 406                   | Not Acceptable        | The server cannot fulfill the request according to the content characteristics of the request. |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------+
   | 501                   | Not Implemented       | The server does not support the requested function.                                            |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------+
   | 403                   | Forbidden             | The server understood the request, but is refusing to fulfill it.                              |
   |                       |                       |                                                                                                |
   |                       |                       | The client should not repeat the request without modifications.                                |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------+
   | 400                   | BadRequest            | Invalid request.                                                                               |
   |                       |                       |                                                                                                |
   |                       |                       | Modify the request instead of retrying.                                                        |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------+
