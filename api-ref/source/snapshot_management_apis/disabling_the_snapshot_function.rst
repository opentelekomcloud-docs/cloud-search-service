:original_name: css_03_0039.html

.. _css_03_0039:

Disabling the Snapshot Function
===============================

Function
--------

This API is used to disable the snapshot function.

URI
---

.. code-block:: text

   DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+--------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                      |
   +============+===========+========+==================================================+
   | project_id | Yes       | String | Project ID.                                      |
   +------------+-----------+--------+--------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to which the snapshot belongs. |
   +------------+-----------+--------+--------------------------------------------------+

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

   DELETE /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshots

Status Code
-----------

:ref:`Table 2 <css_03_0039__table15824192510361>` describes the status code.

.. _css_03_0039__table15824192510361:

.. table:: **Table 2** Status code

   +-------------+----------------+------------------------------------------------------------------------------------------------+
   | Status Code | Code           | Status Code Description                                                                        |
   +=============+================+================================================================================================+
   | 200         | OK             | The request is processed successfully.                                                         |
   +-------------+----------------+------------------------------------------------------------------------------------------------+
   | 406         | Not Acceptable | The server cannot fulfill the request according to the content characteristics of the request. |
   +-------------+----------------+------------------------------------------------------------------------------------------------+
