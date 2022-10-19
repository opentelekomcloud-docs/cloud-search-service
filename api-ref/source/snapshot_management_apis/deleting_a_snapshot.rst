:original_name: css_03_0036.html

.. _css_03_0036:

Deleting a Snapshot
===================

Function
--------

This API is used to delete a snapshot.

URI
---

.. code-block:: text

   DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}

.. table:: **Table 1** Parameter description

   +-------------+-----------+--------+--------------------------------------------------+
   | Parameter   | Mandatory | Type   | Description                                      |
   +=============+===========+========+==================================================+
   | project_id  | Yes       | String | Project ID.                                      |
   +-------------+-----------+--------+--------------------------------------------------+
   | cluster_id  | Yes       | String | ID of the cluster to which the snapshot belongs. |
   +-------------+-----------+--------+--------------------------------------------------+
   | snapshot_id | Yes       | String | ID of the snapshot to be deleted.                |
   +-------------+-----------+--------+--------------------------------------------------+

Request
-------

None

Response
--------

None

Examples
--------

Example request

.. code-block:: text

   DELETE /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/29a2254e-947f-4463-b65a-5f0b17515fae

Status Code
-----------

:ref:`Table 2 <css_03_0036__table1130545163319>` describes the status code.

.. _css_03_0036__table1130545163319:

.. table:: **Table 2** Status code

   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | Status Code           | Code                  | Status Code Description                                           |
   +=======================+=======================+===================================================================+
   | 200                   | OK                    | The request is processed successfully.                            |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | 400                   | BadRequest            | Invalid request.                                                  |
   |                       |                       |                                                                   |
   |                       |                       | The client should not repeat the request without modifications.   |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
   | 403                   | Forbidden             | The server understood the request, but is refusing to fulfill it. |
   |                       |                       |                                                                   |
   |                       |                       | The client should not repeat the request without modifications.   |
   +-----------------------+-----------------------+-------------------------------------------------------------------+
