:original_name: css_03_0078.html

.. _css_03_0078:

Querying Tags of a Specified Cluster
====================================

Function
--------

This API is used to query the tag information about a specified cluster.

URI
---

.. code-block:: text

   GET /v1.0/{project_id}/css-cluster/{cluster_id}/tags

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be queried.                                                   |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request
-------

None

Response
--------

:ref:`Table 2 <css_03_0078__table12361175012485>` describes the response parameters.

.. _css_03_0078__table12361175012485:

.. table:: **Table 2** Response

   +-----------+---------------------------------------------------------------+--------------------+
   | Parameter | Type                                                          | Description        |
   +===========+===============================================================+====================+
   | tags      | Array of :ref:`tag <css_03_0078__table0621135181710>` objects | Tags in a cluster. |
   +-----------+---------------------------------------------------------------+--------------------+

.. _css_03_0078__table0621135181710:

.. table:: **Table 3** **tags** field description

   ========= ====== ===========
   Parameter Type   Description
   ========= ====== ===========
   key       String Tag key.
   value     String Tag value.
   ========= ====== ===========

Examples
--------

Example request

.. code-block:: text

   GET v1.0/458d905f22da49c39f609e3347d65723/css-cluster/4f3deec3-efa8-4598-bf91-560aad1377a3/tags

Example response

.. code-block::

   {
       "tags": [
           {
               "key": "key1",
               "value": "value1"
           },
           {
               "key": "key2",
               "value": "value3"
           }
       ]
   }

Status Code
-----------

:ref:`Table 4 <css_03_0078__table12321369178>` describes the status code.

.. _css_03_0078__table12321369178:

.. table:: **Table 4** Status code

   +-----------------------+-----------------------+-----------------------------------------------------------------+
   | Status Code           | Message               | Description                                                     |
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
