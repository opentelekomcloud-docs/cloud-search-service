:original_name: css_03_0031.html

.. _css_03_0031:

Setting the Automatic Snapshot Creation Policy
==============================================

Function
--------

This API is used to set parameters related to automatic snapshot creation. By default, a snapshot is created per day.

URI
---

.. code-block:: text

   POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy

.. table:: **Table 1** Parameter description

   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                        |
   +============+===========+========+====================================================================================+
   | project_id | Yes       | String | Project ID. For details, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster where automatic snapshot creation is enabled.                    |
   +------------+-----------+--------+------------------------------------------------------------------------------------+

Request
-------

:ref:`Table 2 <css_03_0031__request_setrdsbackupcnfreq>` describes the request parameters.

.. _css_03_0031__request_setrdsbackupcnfreq:

.. table:: **Table 2** Request body parameters

   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                                                                                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================================================================================================================================================================================================================================+
   | indices         | No              | String          | Name of the index to be backed up. \* indicates all indexes.                                                                                                                                                                                                                                                                                                |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | prefix          | No              | String          | Prefix of a snapshot that is automatically created, which is manually entered. Enter up to 32 characters and start with a lowercase letter. Lowercase letters, digits, hyphens (-), and underscores (_) are allowed.                                                                                                                                        |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |    This parameter is mandatory when enable is set to true.                                                                                                                                                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | period          | No              | String          | Time when a snapshot is created every day. Snapshots can only be created on the hour. The time format is the time followed by the time zone, specifically, **HH:mm z**. In the format, **HH:mm** refers to the hour time and **z** refers to the time zone, for example, **00:00 GMT+08:00** and **01:00 GMT+02:00**.                                       |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | .. note::                                                                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 |    This parameter is mandatory when enable is set to true.                                                                                                                                                                                                                                                                                                  |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | keepday         | No              | Integer         | Snapshot retention period. The value ranges from 1 to 90. Expired snapshots will be automatically deleted on the half hour. This parameter is mandatory when enable is set to true.                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | enable          | Yes             | String          | Whether to enable the automatic snapshot creation policy.                                                                                                                                                                                                                                                                                                   |
   |                 |                 |                 |                                                                                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  **true**: The automatic snapshot creation policy is enabled.                                                                                                                                                                                                                                                                                             |
   |                 |                 |                 | -  **false**:The automatic snapshot creation policy is disabled, and other parameters do not need to be delivered.                                                                                                                                                                                                                                          |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | deleteAuto      | No              | String          | Whether to clear all the automatically created snapshots when the automatic snapshot creation policy is disabled. The default value is **false**, indicating that automatically created snapshots will not be deleted. If this parameter is set to **true**, all created snapshots will be deleted when the automatic snapshot creation policy is disabled. |
   +-----------------+-----------------+-----------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Response
--------

None

Examples
--------

Example request

.. code-block:: text

   POST /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/index_snapshot/policy
   {
       "prefix":"snapshot",
       "period":"16:00 GMT+02:00",
       "keepday":7,
       "enable":"true"
   }

Status Code
-----------

:ref:`Table 3 <css_03_0031__table209491933101317>` describes the status code.

.. _css_03_0031__table209491933101317:

.. table:: **Table 3** Status code

   +-------------+----------------+------------------------------------------------------------------------------------------------+
   | Status Code | Code           | Status Code Description                                                                        |
   +=============+================+================================================================================================+
   | 200         | OK             | The request is processed successfully.                                                         |
   +-------------+----------------+------------------------------------------------------------------------------------------------+
   | 406         | Not Acceptable | The server cannot fulfill the request according to the content characteristics of the request. |
   +-------------+----------------+------------------------------------------------------------------------------------------------+
