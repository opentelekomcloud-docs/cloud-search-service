:original_name: css_03_0035.html

.. _css_03_0035:

Restoring a Snapshot
====================

Function
--------

This API is used to manually restore a snapshot.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}/restore

.. table:: **Table 1** Parameter description

   +-------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter   | Mandatory | Type   | Description                                                                        |
   +=============+===========+========+====================================================================================+
   | project_id  | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +-------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id  | Yes       | String | ID of the cluster to which the snapshot belongs.                                   |
   +-------------+-----------+--------+------------------------------------------------------------------------------------+
   | snapshot_id | Yes       | String | ID of the snapshot.                                                                |
   +-------------+-----------+--------+------------------------------------------------------------------------------------+

Request
-------

:ref:`Table 2 <css_03_0035__table82481020121413>` describes the request parameters.

.. _css_03_0035__table82481020121413:

.. table:: **Table 2** Parameter description

   +-------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter         | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                               |
   +===================+=================+=================+===========================================================================================================================================================================================================================================================================================================================+
   | targetCluster     | Yes             | String          | ID of the cluster, to which the snapshot is to be restored.                                                                                                                                                                                                                                                               |
   +-------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | indices           | No              | String          | Name of the index to be restored. Multiple index names are separated by commas (,). By default, data of all indices is restored. You can use the asterisk (``*``) to back up data of certain indices. For example, if you enter **2018-06\***, then data of indices with the name prefix of **2018-06** will be restored. |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                           |
   |                   |                 |                 | The value contains 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?)`` are not allowed.                                                                                                                                                                              |
   +-------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | renamePattern     | No              | String          | Rule for defining the indices to be restored. The value contains a maximum of 1,024 characters.                                                                                                                                                                                                                           |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                           |
   |                   |                 |                 | Indices that meet the filtering condition specified by this parameter are restored. The filtering condition must be specified using regular expressions. The value contains 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?,)`` are not allowed.                    |
   +-------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | renameReplacement | No              | String          | Rule for renaming an index. The value contains 0 to 1,024 characters. Uppercase letters, spaces, and certain special characters (including ``"\<|>/?,)`` are not allowed. For example, value **restored_index_$1** indicates that **restored\_** is added in front of the names of all restored indices.                  |
   |                   |                 |                 |                                                                                                                                                                                                                                                                                                                           |
   |                   |                 |                 | The **renamePattern** and **renameReplacement** parameters must be both configured.                                                                                                                                                                                                                                       |
   +-------------------+-----------------+-----------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response
--------

None

Examples
--------

Example request

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/29a2254e-947f-4463-b65a-5f0b17515fae/restore
   {
       "targetCluster":"ea244205-d641-45d9-9dcb-ab2236bcd07e",
       "indices":"myindex1,myindex2"
   }

Example response

The return value is empty.

Status Code
-----------

:ref:`Table 3 <css_03_0035__table1130545163319>` describes the status code.

.. _css_03_0035__table1130545163319:

.. table:: **Table 3** Status code

   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | Status Code           | Code                  | Status Code Description                                           |
   +=======================+=======================+===================================================================+
   | 201                   | Created               | The request for creating a resource has been fulfilled.           |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | 400                   | BadRequest            | Invalid request.                                                  |
   |                       |                       |                                                                   |
   |                       |                       | Modify the request instead of retrying.                           |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | 403                   | Forbidden             | The server understood the request, but is refusing to fulfill it. |
   |                       |                       |                                                                   |
   |                       |                       | The client should not repeat the request without modifications.   |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
