:original_name: css_03_0083.html

.. _css_03_0083:

Adding Tags to a Cluster
========================

Function
--------

This API is used to add tags to a cluster. A cluster can have a maximum of 10 tags.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/css-cluster/{cluster_id}/tags

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+-----------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                       |
   +============+===========+========+===================================================================================+
   | project_id | Yes       | String | Project ID For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+-----------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to which a tag is to be added                                   |
   +------------+-----------+--------+-----------------------------------------------------------------------------------+

Request
-------

.. table:: **Table 2** **tag** field description

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                 |
   +=================+=================+=================+=============================================================================================================+
   | key             | Yes             | String          | Tag key. The value can contain up to 36 characters.                                                         |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------+
   | value           | Yes             | String          | Tag value. The value contains up to 43 characters.                                                          |
   |                 |                 |                 |                                                                                                             |
   |                 |                 |                 | If **value** is not empty, delete tags by **key**/**value**. If **value** is empty, delete tags by **key**. |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------+

Response
--------

None

Example
-------

-  Example request

   .. code-block:: text

      POST /v1.0/458d905f22da49c39f609e3347d65723/css-cluster/4f3deec3-efa8-4598-bf91-560aad1377a3/tags
      {
          "tag": {
              "key": "DEV",
              "value": "DEV1"
          }
      }

-  Example response

   None

Status Codes
------------

:ref:`Table 3 <css_03_0083__en-us_topic_0000001341910209_table12321369178>` describes the status code.

.. _css_03_0083__en-us_topic_0000001341910209_table12321369178:

.. table:: **Table 3** Status codes

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
   | 204                   | OK                    | The request is processed.               |
   +-----------------------+-----------------------+-----------------------------------------+
