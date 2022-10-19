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

   ========== ========= ====== ==================================
   Parameter  Mandatory Type   Description
   ========== ========= ====== ==================================
   project_id Yes       String Project ID.
   cluster_id Yes       String ID of the cluster to be restarted.
   ========== ========= ====== ==================================

Request
-------

None

Response
--------

.. table:: **Table 2** Parameter description

   ========= ====== =======================
   Parameter Type   Description
   ========= ====== =======================
   jobId     String ID of the restart task.
   ========= ====== =======================

Examples
--------

Example request

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/47e49a5e-8ced-4d0d-ae15-2af62ac468e3/restart

Example response

.. code-block::

   {
    "jobId": [
   "ff8080815fa0fa5e015fa365b6300007"
    ]
    }

Status Code
-----------

:ref:`Table 3 <css_03_0021__table12321369178>` describes the status code.

.. _css_03_0021__table12321369178:

.. table:: **Table 3** Status code

   +-----------------------+-----------------------+-----------------------------------------------------------------+
   | Status Code           | Code                  | Status Code Description                                         |
   +=======================+=======================+=================================================================+
   | 400                   | BadRequest            | Invalid request.                                                |
   |                       |                       |                                                                 |
   |                       |                       | The client should not repeat the request without modifications. |
   +-----------------------+-----------------------+-----------------------------------------------------------------+
   | 404                   | NotFound              | The requested resource cannot be found.                         |
   |                       |                       |                                                                 |
   |                       |                       | The client should not repeat the request without modifications. |
   +-----------------------+-----------------------+-----------------------------------------------------------------+
   | 200                   | OK                    | The request is processed successfully.                          |
   +-----------------------+-----------------------+-----------------------------------------------------------------+
