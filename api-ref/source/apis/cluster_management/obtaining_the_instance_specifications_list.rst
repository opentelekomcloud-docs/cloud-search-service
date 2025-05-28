:original_name: ListFlavors.html

.. _ListFlavors:

Obtaining the Instance Specifications List
==========================================

Function
--------

This API is used to query and display the IDs of supported instance specifications.

URI
---

GET /v1.0/{project_id}/es-flavors

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================+
   | project_id      | Yes             | String          | **Parameter description**:                                                                                                           |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | The project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`. |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                     |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Options**:                                                                                                                         |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                 |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                   |
   |                 |                 |                 |                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                  |
   +-----------------+-----------------+-----------------+--------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

.. table:: **Table 2** Response body parameters

   +-----------------------+---------------------------------------------------------------------------------------------+----------------------------+
   | Parameter             | Type                                                                                        | Description                |
   +=======================+=============================================================================================+============================+
   | versions              | Array of :ref:`EsflavorsVersionsResp <listflavors__response_esflavorsversionsresp>` objects | **Parameter description**: |
   |                       |                                                                                             |                            |
   |                       |                                                                                             | Flavor version list.       |
   +-----------------------+---------------------------------------------------------------------------------------------+----------------------------+

.. _listflavors__response_esflavorsversionsresp:

.. table:: **Table 3** EsflavorsVersionsResp

   +-----------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                                                                                                      | Description                                                                                                     |
   +=======================+===========================================================================================================+=================================================================================================================+
   | version               | String                                                                                                    | **Parameter description**:                                                                                      |
   |                       |                                                                                                           |                                                                                                                 |
   |                       |                                                                                                           | Elasticsearch engine version. For details, see the supported versions in :ref:`Before You Start <css_03_0001>`. |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | flavors               | Array of :ref:`EsflavorsVersionsFlavorsResp <listflavors__response_esflavorsversionsflavorsresp>` objects | **Parameter description**:                                                                                      |
   |                       |                                                                                                           |                                                                                                                 |
   |                       |                                                                                                           | Flavor list.                                                                                                    |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+
   | type                  | String                                                                                                    | **Parameter description**:                                                                                      |
   |                       |                                                                                                           |                                                                                                                 |
   |                       |                                                                                                           | Instance type.                                                                                                  |
   |                       |                                                                                                           |                                                                                                                 |
   |                       |                                                                                                           | **Options**:                                                                                                    |
   |                       |                                                                                                           |                                                                                                                 |
   |                       |                                                                                                           | -  **ess**: data node                                                                                           |
   |                       |                                                                                                           |                                                                                                                 |
   |                       |                                                                                                           | -  **ess-cold**: cold data node                                                                                 |
   |                       |                                                                                                           |                                                                                                                 |
   |                       |                                                                                                           | -  **ess-master**: master node.                                                                                 |
   |                       |                                                                                                           |                                                                                                                 |
   |                       |                                                                                                           | -  **ess-client**: client node                                                                                  |
   +-----------------------+-----------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------+

.. _listflavors__response_esflavorsversionsflavorsresp:

.. table:: **Table 4** EsflavorsVersionsFlavorsResp

   +-----------------------+-----------------------+--------------------------------------+
   | Parameter             | Type                  | Description                          |
   +=======================+=======================+======================================+
   | cpu                   | Integer               | **Parameter description**:           |
   |                       |                       |                                      |
   |                       |                       | Number of CPU cores of an instance.  |
   +-----------------------+-----------------------+--------------------------------------+
   | ram                   | Integer               | **Parameter description**:           |
   |                       |                       |                                      |
   |                       |                       | Memory size of an instance. Unit: GB |
   +-----------------------+-----------------------+--------------------------------------+
   | name                  | String                | **Parameter description**:           |
   |                       |                       |                                      |
   |                       |                       | Flavor name.                         |
   +-----------------------+-----------------------+--------------------------------------+
   | region                | String                | **Parameter description**:           |
   |                       |                       |                                      |
   |                       |                       | Available region                     |
   +-----------------------+-----------------------+--------------------------------------+
   | diskrange             | String                | **Parameter description**:           |
   |                       |                       |                                      |
   |                       |                       | Disk capacity range of an instance.  |
   +-----------------------+-----------------------+--------------------------------------+
   | availableAZ           | String                | **Parameter description**:           |
   |                       |                       |                                      |
   |                       |                       | The AZ.                              |
   +-----------------------+-----------------------+--------------------------------------+
   | flavor_id             | String                | **Parameter description**:           |
   |                       |                       |                                      |
   |                       |                       | Flavor ID.                           |
   +-----------------------+-----------------------+--------------------------------------+

Example Requests
----------------

Obtain the specifications of all instances.

.. code-block:: text

   GET https://{Endpoint}/v1.0/{project_id}/es-flavors

Example Responses
-----------------

**Status code: 200**

Request succeeded.

.. code-block::

   {
     "versions" : [ {
       "flavors" : [ {
         "cpu" : 4,
         "ram" : 32,
         "name" : "ess.spec-4u32g",
         "region" : "xx-xxx-xx",
         "diskrange" : "40,2560",
         "availableAZ" : "xx-xxx-xx,xx-xxx-xx",
         "flavor_id" : "2d8daf1b-873f-4c2e-a7b9-2f9cbcf2f213"
       }, {
         "cpu" : 8,
         "ram" : 64,
         "name" : "ess.spec-8u64g",
         "region" : "xx-xxx-xx",
         "diskrange" : "80,5120",
         "availableAZ" : "xx-xxx-xx,xx-xxx-xx",
         "flavor_id" : "b3d33ec6-d58a-40f0-aa51-4f671ce64b2a"
       }, {
         "cpu" : 16,
         "ram" : 128,
         "name" : "ess.spec-16u128g",
         "region" : "xx-xxx-xx",
         "diskrange" : "160,10240",
         "availableAZ" : "xx-xxx-xx,xx-xxx-xx",
         "flavor_id" : "f74419ca-bc91-4558-b4e2-90eeefb37c6e"
       } ],
       "type" : "ess",
       "version" : "x.x.x"
     } ]
   }

Status Codes
------------

+-----------------------------------+--------------------------------------------+
| Status Code                       | Description                                |
+===================================+============================================+
| 200                               | Request succeeded.                         |
+-----------------------------------+--------------------------------------------+
| 400                               | Invalid request.                           |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+
| 404                               | The requested resource could not be found. |
|                                   |                                            |
|                                   | Modify the request before retry.           |
+-----------------------------------+--------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
