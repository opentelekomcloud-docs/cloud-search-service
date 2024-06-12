:original_name: css_03_0021.html

.. _css_03_0021:

Restarting a Cluster
====================

Function
--------

This API is used to restart a cluster. Restarting the cluster will interrupt ongoing services.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/restart

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be restarted.                                                 |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request
-------

None

Response
--------

None

Examples
--------

None

Status Code
-----------

:ref:`Table 2 <css_03_0021__table12321369178>` describes the status code.

.. _css_03_0021__table12321369178:

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
