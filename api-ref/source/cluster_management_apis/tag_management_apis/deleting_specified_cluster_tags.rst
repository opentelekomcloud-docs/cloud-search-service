:original_name: css_03_0082.html

.. _css_03_0082:

Deleting Specified Cluster Tags
===============================

Function
--------

This API is used to delete specified cluster tags.

URI
---

.. code-block:: text

   DELETE /v1.0/{project_id}/css-cluster/{cluster_id}/tags/{key}

.. table:: **Table 1** Parameters

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                            |
   +=================+=================+=================+========================================================================+
   | project_id      | Yes             | String          | Project ID.                                                            |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | ID of the cluster to which a tag is to be deleted.                     |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------+
   | key             | Yes             | String          | Tag key                                                                |
   |                 |                 |                 |                                                                        |
   |                 |                 |                 | The field cannot be left blank or be an empty character string.        |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------+

Request
-------

None

Response
--------

None

Example
-------

-  Example request

   .. code-block:: text

      DELETE /v1.0/458d905f22da49c39f609e3347d65723/css-cluster/4f3deec3-efa8-4598-bf91-560aad1377a3/tags/key1

-  Response example

   None

Status Code
-----------

:ref:`Table 2 <css_03_0082__en-us_topic_0000001341910209_table12321369178>` describes status codes.

.. _css_03_0082__en-us_topic_0000001341910209_table12321369178:

.. table:: **Table 2** Status code

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
