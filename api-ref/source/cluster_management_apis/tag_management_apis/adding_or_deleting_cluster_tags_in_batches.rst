:original_name: css_03_0081.html

.. _css_03_0081:

Adding or Deleting Cluster Tags in Batches
==========================================

Function
--------

This API is used to add or delete tags to or from a specified cluster in batches. Tag Management Service (TMS) uses this API to batch manage tags of a cluster. A cluster can have a maximum of 10 tags.

.. note::

   -  This API is an idempotent API. If the request body contains duplicate keys during tag creation, an error is reported.
   -  When a tag is added:

      -  The key cannot be left blank or be an empty string. It cannot contain the following characters: Non-printable ASCII characters (0-31), =, \*, <, >, \\, ,, \|, /, letters, digits, hyphens (-), and underscores (_).
      -  The value cannot be left blank but can be an empty string. It cannot contain the following characters: Non-printable ASCII characters (0-31), =, \*, <, >, \\, ,, \|, /, letters, digits, hyphens (-), and underscores (_).
      -  The key cannot be duplicate. If the key already exists in the database, the value will be overwritten.

   -  When a tag is deleted:

      -  If a to-be-deleted tag does not exist, the operation is considered successful by default. The value range of the tag character set is not verified.
      -  The tag structure body cannot be missing, and the key cannot be left blank or be an empty string.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/css-cluster/{cluster_id}/tags/action

.. table:: **Table 1** Parameters

   +------------+-----------+--------+---------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                         |
   +============+===========+========+=====================================================================+
   | project_id | Yes       | String | Project ID                                                          |
   +------------+-----------+--------+---------------------------------------------------------------------+
   | cluster_id | Yes       | String | IDs of clusters to which tags are to be added or deleted in batches |
   +------------+-----------+--------+---------------------------------------------------------------------+

Request
-------

.. table:: **Table 2** Request parameters

   +-----------+-----------+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type                                                          | Description                                                                       |
   +===========+===========+===============================================================+===================================================================================+
   | tags      | No        | Array of :ref:`tag <css_03_0081__table2440821133810>` objects | Tag list                                                                          |
   +-----------+-----------+---------------------------------------------------------------+-----------------------------------------------------------------------------------+
   | action    | Yes       | String                                                        | Operation to be performed. The value can be set to **create** or **delete** only. |
   +-----------+-----------+---------------------------------------------------------------+-----------------------------------------------------------------------------------+

.. _css_03_0081__table2440821133810:

.. table:: **Table 3** **resource_tag** field description

   +-----------------+---------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory                                                                                                           | Type            | Description                                                                                                 |
   +=================+=====================================================================================================================+=================+=============================================================================================================+
   | key             | Yes                                                                                                                 | String          | Tag key. The value can contain up to 36 characters.                                                         |
   +-----------------+---------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------+
   | value           | This parameter is mandatory when **action** is set to **create** and optional when **action** is set to **delete**. | String          | Tag value. The value contains up to 43 characters.                                                          |
   |                 |                                                                                                                     |                 |                                                                                                             |
   |                 |                                                                                                                     |                 | If **value** is not empty, delete tags by **key**/**value**. If **value** is empty, delete tags by **key**. |
   +-----------------+---------------------------------------------------------------------------------------------------------------------+-----------------+-------------------------------------------------------------------------------------------------------------+

Response
--------

None

Example
-------

-  Example request

.. code-block:: text

   POST /v1.0/458d905f22da49c39f609e3347d65723/css-cluster/4f3deec3-efa8-4598-bf91-560aad1377a3/tags/action

This API is used to add tags in batches.

.. code-block::

   {
       "action": "create",
       "tags": [
           {
               "key": "key1",
               "value": "value1"
           }
       ]
   }

This API is used to delete tags in batches.

.. code-block::

   {
       "action": "delete",
       "tags": [
           {
               "key": "key1"
           }
       ]
   }

-  Response example

   None

Status Code
-----------

:ref:`Table 4 <css_03_0081__table12321369178>` describes status codes.

.. _css_03_0081__table12321369178:

.. table:: **Table 4** Status code

   +-----------------------+-----------------------+-----------------------------------------------+
   | Status Code           | Encoding              | Description                                   |
   +=======================+=======================+===============================================+
   | 400                   | BadRequest            | Invalid request.                              |
   |                       |                       |                                               |
   |                       |                       | Do not retry the request before modification. |
   +-----------------------+-----------------------+-----------------------------------------------+
   | 404                   | NotFound              | The requested resource cannot be found.       |
   |                       |                       |                                               |
   |                       |                       | Do not retry the request before modification. |
   +-----------------------+-----------------------+-----------------------------------------------+
   | 204                   | OK                    | The request is processed successfully.        |
   +-----------------------+-----------------------+-----------------------------------------------+
