:original_name: css_03_0025.html

.. _css_03_0025:

Scaling Out a Cluster with only Common Nodes
============================================

Function
--------

This API is used to scale out a cluster with only common nodes. Clusters with master, client, or cold data nodes cannot use this API.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/extend

.. table:: **Table 1** Parameter description

   ========== ========= ====== ===================================
   Parameter  Mandatory Type   Description
   ========== ========= ====== ===================================
   project_id Yes       String Project ID.
   cluster_id Yes       String ID of the cluster to be scaled out.
   ========== ========= ====== ===================================

Request
-------

:ref:`Table 2 <css_03_0025__table82481020121413>` describes the request parameters.

.. _css_03_0025__table82481020121413:

.. table:: **Table 2** Parameter description

   +-----------+-----------+--------+--------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type   | Description                                                                                                                    |
   +===========+===========+========+================================================================================================================================+
   | grow      | Yes       | Object | Detailed description about the cluster scale-out request. For details, see :ref:`Table 3 <css_03_0025__table198051725112115>`. |
   +-----------+-----------+--------+--------------------------------------------------------------------------------------------------------------------------------+

.. _css_03_0025__table198051725112115:

.. table:: **Table 3** **grow** field description

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                        |
   +=================+=================+=================+====================================================================================================+
   | modifySize      | Yes             | Integer         | Number of instances in a cluster after a scale-out.                                                |
   |                 |                 |                 |                                                                                                    |
   |                 |                 |                 | .. note::                                                                                          |
   |                 |                 |                 |                                                                                                    |
   |                 |                 |                 |    The total number of existing instances and newly added instances in a cluster cannot exceed 32. |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------+

Response
--------

None

Examples
--------

Example request

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/extend
   {
       "grow":
           {
               "modifySize": 4
           }
   }

Example response

.. code-block::

   {}

Status Code
-----------

:ref:`Table 4 <css_03_0025__table12321369178>` describes the status code.

.. _css_03_0025__table12321369178:

.. table:: **Table 4** Status code

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
