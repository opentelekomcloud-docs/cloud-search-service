:original_name: css_03_0023.html

.. _css_03_0023:

Obtaining the List of Instance Flavors
======================================

Function
--------

This API is used to query and display the IDs of supported instance flavors.

URI
---

.. code-block:: text

   GET /v1.0/{project_id}/flavors

.. table:: **Table 1** Parameter description

   ========== ========= ====== ===========
   Parameter  Mandatory Type   Description
   ========== ========= ====== ===========
   project_id Yes       String Project ID.
   ========== ========= ====== ===========

Request
-------

None

Response
--------

:ref:`Table 2 <css_03_0023__table347318359446>` describes the response parameters.

.. _css_03_0023__table347318359446:

.. table:: **Table 2** Parameter description

   +-----------+---------------------------------------------------------------------+--------------------------+
   | Parameter | Type                                                                | Description              |
   +===========+=====================================================================+==========================+
   | versions  | Array of :ref:`versions <css_03_0023__table25411438165118>` objects | List of engine versions. |
   +-----------+---------------------------------------------------------------------+--------------------------+

.. _css_03_0023__table25411438165118:

.. table:: **Table 3** **versions** field description

   +-----------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
   | Parameter | Type                                                              | Description                                                                               |
   +===========+===================================================================+===========================================================================================+
   | version   | String                                                            | Engine version.                                                                           |
   +-----------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
   | type      | String                                                            | Instance type. The options are **ess**, **ess-cold**, **ess-master**, and **ess-client**. |
   +-----------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------+
   | flavors   | Array of :ref:`flavors <css_03_0023__table5319191204412>` objects | Flavor list                                                                               |
   +-----------+-------------------------------------------------------------------+-------------------------------------------------------------------------------------------+

.. _css_03_0023__table5319191204412:

.. table:: **Table 4** **flavors** field description

   ========= ======= ====================================
   Parameter Type    Description
   ========= ======= ====================================
   ram       Integer Memory size of an instance. Unit: GB
   cpu       Integer Number of vCPUs of an instance.
   name      String  Flavor name.
   region    String  AZ
   diskrange String  Disk capacity range of an instance.
   flavor_id String  ID of a flavor.
   ========= ======= ====================================

Examples
--------

Example request

.. code-block:: text

   GET /v1.0/6204a5bd270343b5885144cf9c8c158d/flavors

Example response

.. code-block::

   {
     "versions": [
       {
         "version": "6.2.3",
         "flavors": [
           {
             "cpu": 1,
             "ram": 8,
             "name": "css.medium.8",
             "region": "eu-de",
             "diskrange": "40,640",
             "flavor_id": "6b6c0bcf-750d-4f8a-b6f5-c45a143f5198"

           },
           {
             "cpu": 2,
             "ram": 16,
             "name": "css.large.8",
             "region": "eu-de",
             "diskrange": "40,1280",
             "flavor_id": "d373e339-3cf4-4c00-9739-2259e9f3ec16"

           },
           {
             "cpu": 4,
             "ram": 32,
             "name": "css.xlarge.8",
             "region": "eu-de",
             "diskrange": "40,2560",
             "flavor_id": "2d8daf1b-873f-4c2e-a7b9-2f9cbcf2f213"

           },
           {
             "cpu": 8,
             "ram": 64,
             "name": "css.2xlarge.8",
             "region": "eu-de",
             "diskrange": "80,5120",
             "flavor_id": "b3d33ec6-d58a-40f0-aa51-4f671ce64b2a"

           },
           {
             "cpu": 16,
             "ram": 128,
             "name": "css.4xlarge.8",
             "region": "eu-de",
             "diskrange": "160,10240",
             "flavor_id": "f74419ca-bc91-4558-b4e2-90eeefb37c6e"
           }
         ]
       }
     ]
   }

Status Code
-----------

:ref:`Table 5 <css_03_0023__table12321369178>` describes the status code.

.. _css_03_0023__table12321369178:

.. table:: **Table 5** Status code

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
