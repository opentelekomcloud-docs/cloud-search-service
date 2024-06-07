:original_name: css_03_0020.html

.. _css_03_0020:

Deleting a Cluster
==================

Function
--------

This API is used to delete a cluster. All resources, including customer data, of the deleted cluster will be released. For data security reasons, create a snapshot for the cluster that you want to delete.

URI
---

.. code-block:: text

   DELETE /v1.0/{project_id}/clusters/{cluster_id}

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be deleted.                                                   |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request
-------

None

Response
--------

None

Examples
--------

Delete the cluster whose ID is **2a197c4d-5467-4003-931d-83ec49939cf**.

Example request

.. code-block:: text

   DELETE /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/2a197c4d-5467-4003-931d-83ec49939cf

Example response

The return value is empty.

Status Code
-----------

:ref:`Table 2 <css_03_0020__table12321369178>` describes the status code.

.. _css_03_0020__table12321369178:

.. table:: **Table 2** Status codes

   +-----------------------+-----------------------+-----------------------------------------+
   | Status Code           | Message               | Description                             |
   +=======================+=======================+=========================================+
   | 400                   | BadRequest            | Invalid request.                        |
   |                       |                       |                                         |
   |                       |                       | Modify the request instead of retrying. |
   +-----------------------+-----------------------+-----------------------------------------+
   | 404                   | NotFound              | The requested resource cannot be found. |
   |                       |                       |                                         |
   |                       |                       | Modify the request instead of retrying. |
   +-----------------------+-----------------------+-----------------------------------------+
   | 200                   | OK                    | The request is processed successfully.  |
   +-----------------------+-----------------------+-----------------------------------------+
