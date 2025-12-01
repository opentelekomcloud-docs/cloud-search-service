:original_name: UpdateCloseKibana.html

.. _UpdateCloseKibana:

Disabling Kibana Public Access
==============================

Function
--------

This API is used to disable public network access to Kibana.

.. note::

   If you disable Kibana public network access and then re-enable it, the public IP address for accessing Kibana may change. Exercise caution.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/publickibana/close

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                          |
   +=================+=================+=================+======================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Project ID of the account.                                                                                                                                           |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                      |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | ID of the cluster whose Kibana public access you want to disable. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Constraints**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Value range**:                                                                                                                                                     |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | Cluster ID.                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | **Default value**:                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                      |
   |                 |                 |                 | N/A                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

.. table:: **Table 2** Request body parameters

   +----------------+-----------+--------------------------------------------------------------------------------------------------------------+-------------------------+
   | Parameter      | Mandatory | Type                                                                                                         | Description             |
   +================+===========+==============================================================================================================+=========================+
   | eip_size       | No        | Integer                                                                                                      | Bandwidth. Unit: Mbit/s |
   +----------------+-----------+--------------------------------------------------------------------------------------------------------------+-------------------------+
   | elb_white_list | No        | :ref:`StartKibanaPublicReqElbWhitelist <updateclosekibana__request_startkibanapublicreqelbwhitelist>` object | ELB whitelist.          |
   +----------------+-----------+--------------------------------------------------------------------------------------------------------------+-------------------------+

.. _updateclosekibana__request_startkibanapublicreqelbwhitelist:

.. table:: **Table 3** StartKibanaPublicReqElbWhitelist

   +-------------------+-----------------+-----------------+-------------------------------------------+
   | Parameter         | Mandatory       | Type            | Description                               |
   +===================+=================+=================+===========================================+
   | enable_white_list | Yes             | Boolean         | Whether to enable the whitelist function. |
   |                   |                 |                 |                                           |
   |                   |                 |                 | -  **true**: The whitelist is enabled.    |
   |                   |                 |                 |                                           |
   |                   |                 |                 | -  **false**: The whitelist is disabled.  |
   +-------------------+-----------------+-----------------+-------------------------------------------+
   | white_list        | Yes             | String          | Whitelist.                                |
   +-------------------+-----------------+-----------------+-------------------------------------------+

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Disable Kibana public access.

.. code-block:: text

   PUT https://{Endpoint}/v1.0/{project_id}/clusters/4f3deec3-efa8-4598-bf91-560aad1377a3/publickibana/close

   {
     "eip_size" : 5,
     "elb_white_list" : {
       "enable_white_list" : true,
       "white_list" : "192.168.0.xx"
     }
   }

Example Responses
-----------------

None

Status Codes
------------

+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| Status Code                       | Description                                                                                                                        |
+===================================+====================================================================================================================================+
| 200                               | Request succeeded.                                                                                                                 |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 400                               | Invalid request.                                                                                                                   |
|                                   |                                                                                                                                    |
|                                   | Modify the request before retry.                                                                                                   |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 409                               | The request could not be completed due to a conflict with the current state of the resource.                                       |
|                                   |                                                                                                                                    |
|                                   | The resource that the client attempts to create already exists, or the update request fails to be processed because of a conflict. |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+
| 412                               | The server did not meet one of the preconditions contained in the request.                                                         |
+-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

See :ref:`Error Codes <css_03_0076>`.
