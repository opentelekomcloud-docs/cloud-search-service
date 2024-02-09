:original_name: css_03_0079.html

.. _css_03_0079:

Querying All Tags
=================

Function
--------

This API is used to query all tags in a specified region.

URI
---

.. code-block:: text

   GET /v1.0/{project_id}/css-cluster/tags

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request
-------

None

Response
--------

:ref:`Table 2 <css_03_0079__table0621135181710>` describes the response parameters.

.. _css_03_0079__table0621135181710:

.. table:: **Table 2** Response parameters

   +-----------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+
   | Parameter | Type                                                          | Description                                                                           |
   +===========+===============================================================+=======================================================================================+
   | tags      | Array of :ref:`tag <css_03_0079__table4597205181712>` objects | Tags in a cluster. For details, see :ref:`Table 3 <css_03_0079__table4597205181712>`. |
   +-----------+---------------------------------------------------------------+---------------------------------------------------------------------------------------+

.. _css_03_0079__table4597205181712:

.. table:: **Table 3** **tags** field description

   ========= ================ ===========
   Parameter Type             Description
   ========= ================ ===========
   key       String           Tag key.
   values    Array of strings Tag value.
   ========= ================ ===========

Examples
--------

Example request

.. code-block:: text

   GET v1.0/458d905f22da49c39f609e3347d65723/css-cluster/tags

Example response

.. code-block::

   {
       "tags": [
           {
               "key": "key1",
               "values": [
                   "value1",
                   "value2"
               ]
           },
           {
               "key": "key2",
               "values": [
                   "value1",
                   "value2"
               ]
           }
       ]
   }

Status Code
-----------

:ref:`Table 4 <css_03_0079__table12321369178>` describes the status code.

.. _css_03_0079__table12321369178:

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
