:original_name: RetryUpgradeTask.html

.. _RetryUpgradeTask:

Retrying a Failed Upgrade Task
==============================

Function
--------

The upgrade takes a long time and the upgrade may fail due to network problems. You can use this API to retry a task or terminate the impact of a task.

Calling Method
--------------

For details, see :ref:`Calling APIs <iam_01_0023>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/upgrade/{action_id}/retry

.. table:: **Table 1** Path parameters

   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                         |
   +============+===========+========+=====================================================================================================================+
   | project_id | Yes       | String | Project ID. For details about how to obtain a project ID, see :ref:`Obtaining a Project ID and Name <css_03_0071>`. |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | cluster_id | Yes       | String | ID of the cluster to be retried.                                                                                    |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+
   | action_id  | Yes       | String | ID of the task to be retried.                                                                                       |
   +------------+-----------+--------+---------------------------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Query parameters

   +------------+-----------+--------+--------------------------------------------------------------------------------------------------------------------+
   | Parameter  | Mandatory | Type   | Description                                                                                                        |
   +============+===========+========+====================================================================================================================+
   | retry_mode | No        | String | If this parameter is not left blank, the impact of the task is terminated. Currently, only **abort** is supported. |
   +------------+-----------+--------+--------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

None

Request Example
---------------

-  Example request for retrying an upgrade task.

   .. code-block:: text

      PUT /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/bcdb711c-a7f0-4007-b8ee-9f13c05f8326/retry

-  Example request for terminating an upgrade task.

   .. code-block:: text

      PUT /v1.0/6204a5bd270343b5885144cf9c8c158d/clusters/ea244205-d641-45d9-9dcb-ab2236bcd07e/upgrade/bcdb711c-a7f0-4007-b8ee-9f13c05f8326/retry?retry_mode=abort

Response Example
----------------

None

Status Codes
------------

+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Status Code | Description                                                                                                                                                            |
+=============+========================================================================================================================================================================+
| 200         | The request is processed.                                                                                                                                              |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 400         | Invalid request. Modify the request directly and do not attempt to retry it.                                                                                           |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| 403         | The request is rejected. The server has received and understood the request, but refused to respond to it. Modify the request directly and do not attempt to retry it. |
+-------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Error Codes
-----------

For details, see :ref:`Error Code <css_03_0076>`.
