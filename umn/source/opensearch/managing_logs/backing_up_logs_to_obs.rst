:original_name: css_01_0166.html

.. _css_01_0166:

Backing Up Logs to OBS
======================

During routine O&M, querying logs in real-time through the web console is a commonly used method for diagnosing issues. However, due to limited local storage capacity, the system automatically archives historical logs when they exceed 128 MB or at 00:00 UTC. Long-term log retention is essential for compliance and operational purposes, but it must also be cost-effective. To address this, CSS provides a log backup feature that incrementally synchronizes run logs, slow query logs, and deprecation logs to OBS based on predefined policies. This solution takes advantage of OBS's vast, low-cost storage for long-term retention while also allowing users to download historical log files at any time for detailed offline analysis.

Impact on Billing
-----------------

Standard storage is used for storing log backups in OBS. For pricing details, see section "Billing" in *Object Storage Service User Guide*.

Prerequisites
-------------

You have created an OBS bucket for storing log backups. The OBS bucket must meet the following requirements:

-  **Storage Class**: **Standard** or **Warm**.
-  **Region**: the same as that of your CSS cluster.

Enabling Log Backup
-------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Logs > Log Backup**. The **Log Backup** page is displayed.

   Check whether log backup is enabled for the cluster.

   -  Yes: No further action is required.
   -  No: Go to the next step.

#. On the **Log Backup** page, click **Enable Backup**. In the displayed dialog box, configure the necessary settings.

   .. table:: **Table 1** Log backup settings

      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                                              |
      +===================================+==========================================================================================================================================================================================================================================================================================+
      | OBS Bucket                        | Select an OBS bucket for storing log backups from the drop-down list box.                                                                                                                                                                                                                |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | If no OBS buckets meet your requirements, click **Create Bucket** to go to the OBS console and create one. For details, see `Creating a Bucket <https://docs.otc.t-systems.com/en-us/usermanual/obs/en-us_topic_0045853662.html>`__.                                                     |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | To grant an IAM user access to an OBS bucket, you need to grant the **GetBucketStoragePolicy**, **GetBucketLocation**, **ListBucket**, and **ListAllMyBuckets** permissions to that user.                                                                                                |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Backup Path                       | Set the log storage location in the OBS bucket.                                                                                                                                                                                                                                          |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | The backup path cannot:                                                                                                                                                                                                                                                                  |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | -  Contain the following characters: **\\:*?"<>|'{}**                                                                                                                                                                                                                                    |
      |                                   | -  Start with a slash (/).                                                                                                                                                                                                                                                               |
      |                                   | -  Start or end with a period (.).                                                                                                                                                                                                                                                       |
      |                                   | -  Contain more than two consecutive slashes (/) or periods (.).                                                                                                                                                                                                                         |
      |                                   | -  Exceed 512 characters.                                                                                                                                                                                                                                                                |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | IAM Agency                        | To back up data to an OBS bucket, you must have the write permission to it. By configuring an IAM agency, you can authorize CSS to access its OBS resources through an associated account.                                                                                               |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | -  If you are configuring an agency for the first time, click **Automatically Create IAM Agency** to create **css-obs-agency**.                                                                                                                                                          |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | -  If there is an IAM agency automatically created earlier, you can click **One-click authorization** to have the OBS Administrator permissions deleted automatically, and have the following custom policies added automatically instead to implement more refined permissions control. |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |    .. code-block::                                                                                                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |       "obs:bucket:GetBucketLocation",                                                                                                                                                                                                                                                    |
      |                                   |       "obs:object:GetObjectVersion",                                                                                                                                                                                                                                                     |
      |                                   |       "obs:object:GetObject",                                                                                                                                                                                                                                                            |
      |                                   |       "obs:object:DeleteObject",                                                                                                                                                                                                                                                         |
      |                                   |       "obs:bucket:HeadBucket",                                                                                                                                                                                                                                                           |
      |                                   |       "obs:bucket:GetBucketStoragePolicy",                                                                                                                                                                                                                                               |
      |                                   |       "obs:object:DeleteObjectVersion",                                                                                                                                                                                                                                                  |
      |                                   |       "obs:bucket:ListBucketVersions",                                                                                                                                                                                                                                                   |
      |                                   |       "obs:bucket:ListBucket",                                                                                                                                                                                                                                                           |
      |                                   |       "obs:object:PutObject"                                                                                                                                                                                                                                                             |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | -  When OBS buckets use SSE-KMS encryption, the IAM agency must be granted KMS permissions. You can click **Automatically Create IAM Agency** and **One-click authorization** to have the following custom policies created automatically.                                               |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |    .. code-block::                                                                                                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |       "kms:cmk:create",                                                                                                                                                                                                                                                                  |
      |                                   |       "kms:dek:create",                                                                                                                                                                                                                                                                  |
      |                                   |       "kms:cmk:get",                                                                                                                                                                                                                                                                     |
      |                                   |       "kms:dek:decrypt",                                                                                                                                                                                                                                                                 |
      |                                   |       "kms:cmk:list"                                                                                                                                                                                                                                                                     |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | -  To use **Automatically Create IAM Agency** and **One-click authorization**, the following minimum permissions are required:                                                                                                                                                           |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |    .. code-block::                                                                                                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |       "iam:agencies:listAgencies",                                                                                                                                                                                                                                                       |
      |                                   |       "iam:roles:listRoles",                                                                                                                                                                                                                                                             |
      |                                   |       "iam:agencies:getAgency",                                                                                                                                                                                                                                                          |
      |                                   |       "iam:agencies:createAgency",                                                                                                                                                                                                                                                       |
      |                                   |       "iam:permissions:listRolesForAgency",                                                                                                                                                                                                                                              |
      |                                   |       "iam:permissions:grantRoleToAgency",                                                                                                                                                                                                                                               |
      |                                   |       "iam:permissions:listRolesForAgencyOnProject",                                                                                                                                                                                                                                     |
      |                                   |       "iam:permissions:revokeRoleFromAgency",                                                                                                                                                                                                                                            |
      |                                   |       "iam:roles:createRole"                                                                                                                                                                                                                                                             |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | -  To use an IAM agency, the following minimum permissions are required:                                                                                                                                                                                                                 |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |    .. code-block::                                                                                                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |       "iam:agencies:listAgencies",                                                                                                                                                                                                                                                       |
      |                                   |       "iam:agencies:getAgency",                                                                                                                                                                                                                                                          |
      |                                   |       "iam:permissions:listRolesForAgencyOnProject",                                                                                                                                                                                                                                     |
      |                                   |       "iam:permissions:listRolesForAgency"                                                                                                                                                                                                                                               |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   | .. warning::                                                                                                                                                                                                                                                                             |
      |                                   |                                                                                                                                                                                                                                                                                          |
      |                                   |    The agency name can contain only letters (case-sensitive), digits, underscores (_), and hyphens (-). Otherwise, the backup will fail.                                                                                                                                                 |
      +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   Determine whether to enable **Automatic backup** based on service needs.

   -  To enable automatic, periodic log backup, select **Automatic backup**, and set the backup policy. For more, see :ref:`Configuring Automatic Log Backup <en-us_topic_0000002558466153__section1869210353211>`.
   -  If manual log backup is sufficient, deselect **Automatic backup**.

#. Click **OK** to enable log backup.

   The configuration information will be displayed on the **Log Backup** tab.

.. _en-us_topic_0000002558466153__section1869210353211:

Configuring Automatic Log Backup
--------------------------------

After enabling log backup for a cluster, you can configure an auto backup policy to periodically back up logs based on a preset schedule.

#. On the **Log Backup** page, click **Modify Settings** on the right.

#. In the **Modify Settings** dialog box, select **Automatic backup**, and configure the backup policy.

   .. table:: **Table 2** Automatic backup settings

      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                    |
      +===================================+================================================================================================================================+
      | Time Zone                         | Select a time zone for the backup start time.                                                                                  |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+
      | Backup Start Time                 | Specify the start time of auto backup.                                                                                         |
      |                                   |                                                                                                                                |
      |                                   | Select a value from the drop-down list. The value range is from **00:00** to **23:00**. The backup always happens on the hour. |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------+

#. Click **OK** to enable automatic log backup.

   Automatic log backup tasks are displayed in the task list. When **Task Status** in the task list changes to **Succeeded**, the backup is successful.

   If log backup fails, click **Failed Tasks** to learn the failure causes. A maximum of 10 failed tasks can be displayed. When log backup is disabled or the cluster is deleted, the failure records are also cleared.

#. If automatic log backup is no longer required, click **Modify Settings**. In the displayed dialog box, deselect **Automatic backup**, and click **OK**. In the displayed confirmation dialog box, click **OK**.

   Disabling log backup does not automatically delete log backups automatically generated earlier. Instead, you need to manually delete them on the OBS console.

Manually Backing Up Logs
------------------------

After enabling log backup for a cluster, you can manually back up its logs at any time.

#. On the **Log Backup** page, click **Back Up Manually** under **Log Backup Tasks**.

#. In the displayed dialog box, confirm the log backup path and click **OK**.

   The log backup task is displayed in the task list. When **Task Status** in the task list changes to **Succeeded**, the backup is successful.

   If log backup fails, click **Failed Tasks** to learn the failure causes. A maximum of 10 failed tasks can be displayed. When log backup is disabled or the cluster is deleted, the failure records are also cleared.

Checking Log Backup Files
-------------------------

Logs are backed up incrementally. After the backup is successful, you can access the target OBS bucket to obtain the full log files by clicking **Log Path**.

:ref:`Table 3 <en-us_topic_0000002558466153__en-us_topic_0000002558581145_table11352134814319>` lists the log types, where **clustername** indicates the cluster name.

.. _en-us_topic_0000002558466153__en-us_topic_0000002558581145_table11352134814319:

.. table:: **Table 3** Log types

   =========================================== ======================
   Log Name                                    Description
   =========================================== ======================
   *clustername*\ \_deprecation.log            Deprecation log file
   *clustername*\ \_index_indexing_slowlog.log Slow indexing log file
   *clustername*\ \_index_search_slowlog.log   Slow query log file
   *clustername*.log                           Run log file
   *clustername*\ \_access.log                 Access log file
   =========================================== ======================

Disabling Log Backup
--------------------

Disable log backup if it is no longer needed.

On the **Log Backup** page, click **Disable Backup**. In the displayed dialog box, click **OK**.

.. caution::

   Disabling log backup does not automatically delete existing backups. Instead, you need to manually delete them on the OBS console.
