:original_name: StopLogAutoBackupPolicy.html

.. _StopLogAutoBackupPolicy:

Disabling the Automatic Log Backup Policy
=========================================

Function
--------

CSS provides log query and log backup, enabling you to easily manage and analyze logs to efficiently locate faults, optimize performance, and enhance system security.

-  Log query: On the log management page of the CSS management console, you can query the latest 10,000 log records by node type and other criteria. A maximum of 100 results are displayed, enabling you to quickly locate issues.

-  Log backup: Cluster logs are periodically synchronized to OBS buckets. You can download them for in-depth analysis at any time. You can configure custom log backup policies by specifying backup schedules and storage locations. The system backs up all critical logs, including run logs and deprecation logs. They provide comprehensive data for auditing and troubleshooting purposes.

This API is used to disable an automatic log backup policy. If an automatic log backup policy is enabled for a cluster, you can use this API to disable it.

Calling Method
--------------

For details, see :ref:`Calling APIs <css_03_0077>`.

URI
---

PUT /v1.0/{project_id}/clusters/{cluster_id}/logs/policy/close

.. table:: **Table 1** Path Parameters

   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter       | Mandatory       | Type            | Description                                                                                                                                                                 |
   +=================+=================+=================+=============================================================================================================================================================================+
   | project_id      | Yes             | String          | **Definition**:                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | Project ID. For details about how to obtain the project ID and name, see :ref:`Obtaining the Project ID and Name <css_03_0071>`.                                            |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | Project ID of the account.                                                                                                                                                  |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | cluster_id      | Yes             | String          | **Definition**:                                                                                                                                                             |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | ID of the cluster whose automatic log backup policy you want to disable. For details about how to obtain the cluster ID, see :ref:`Obtaining the Cluster ID <css_03_0101>`. |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | **Constraints**:                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                                         |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | **Value range**:                                                                                                                                                            |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | Cluster ID.                                                                                                                                                                 |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | **Default value**:                                                                                                                                                          |
   |                 |                 |                 |                                                                                                                                                                             |
   |                 |                 |                 | N/A                                                                                                                                                                         |
   +-----------------+-----------------+-----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Request Parameters
------------------

None

Response Parameters
-------------------

**Status code: 200**

Request succeeded.

None

Example Requests
----------------

Disable an automatic log backup policy.

.. code-block:: text

   PUT https://{Endpoint}/v1.0/{project_id}/clusters/5c77b71c-5b35-4f50-8984-76387e42451a/logs/policy/close

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
