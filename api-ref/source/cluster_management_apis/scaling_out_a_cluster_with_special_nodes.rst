:original_name: css_03_0038.html

.. _css_03_0038:

Scaling Out a Cluster with Special Nodes
========================================

Function
--------

This API is used to scale out a cluster with special nodes. That is, if a cluster has master, client, or cold data nodes, this API is used for scale-out.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/role_extend

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be scaled out.                                                |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request
-------

:ref:`Table 2 <css_03_0038__table758918551711>` describes the request parameters.

.. _css_03_0038__table758918551711:

.. table:: **Table 2** Parameter description

   +-----------+-----------+-----------------+------------------------------------------------------------------------------------------------------------------------------+
   | Parameter | Mandatory | Type            | Description                                                                                                                  |
   +===========+===========+=================+==============================================================================================================================+
   | grow      | Yes       | Array of object | Detailed description about the cluster scale-out request. For details, see :ref:`Table 3 <css_03_0038__table4597205181712>`. |
   +-----------+-----------+-----------------+------------------------------------------------------------------------------------------------------------------------------+

.. _css_03_0038__table4597205181712:

.. table:: **Table 3** **grow** field description

   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                        |
   +=================+=================+=================+====================================================================================================================================================================================================================================================================================================================================+
   | type            | Yes             | String          | Type of the instance to be scaled out. Select at least one from **ess**, **ess-cold**, **ess-master**, and **ess-client**.                                                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | You can only add instances, rather than increase storage capacity, on nodes of the **ess-master** and **ess-client** types.                                                                                                                                                                                                        |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | nodesize        | Yes             | Integer         | Number of instances to be scaled out. The total number of existing instances and newly added instances in a cluster cannot exceed 32.                                                                                                                                                                                              |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | disksize        | Yes             | Integer         | Storage capacity of the instance to be expanded. The total storage capacity of existing instances and newly added instances in a cluster cannot exceed the maximum instance storage capacity allowed when a cluster is being created. In addition, you can expand the instance storage capacity for a cluster for up to six times. |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                    |
   |                 |                 |                 | Unit: GB                                                                                                                                                                                                                                                                                                                           |
   +-----------------+-----------------+-----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response Parameters
-------------------

:ref:`Table 4 <css_03_0038__table0621135181710>` describes the response parameters.

.. _css_03_0038__table0621135181710:

.. table:: **Table 4** Parameter description

   ========= ====== ===========
   Parameter Type   Description
   ========= ====== ===========
   id        String Cluster ID.
   ========= ====== ===========

Examples
--------

Example request

.. code-block:: text

   POST v1.0/458d905f22da49c39f609e3347d65723/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/role_extend
   {
       "grow": [
           {
               "type": "ess-master",
               "nodesize": 2,
               "disksize": 0
           },
           {
               "type": "ess",
               "nodesize": 0,
               "disksize": 50
           },
           {
               "type": "ess-client",
               "nodesize": 1,
               "disksize": 0
           }
       ]
   }

Example response

.. code-block::

   {
       "id": "4f3deec3-efa8-4598-bf91-560aad1377a3"
   }

Status Code
-----------

:ref:`Table 5 <css_03_0038__table12321369178>` describes the status code.

.. _css_03_0038__table12321369178:

.. table:: **Table 5** Status codes

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
