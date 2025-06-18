:original_name: css_01_0508.html

.. _css_01_0508:

Querying and Managing OpenSearch Cluster Logs
=============================================

CSS supports log backup and search, so users can analyze logs to locate issues.

You can have cluster logs periodically backed up to OBS buckets and download log files from OBS later.

Querying Logs
-------------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the cluster whose logs you want to query. The cluster information page is displayed.

#. In the navigation pane on the left, choose **Log Management**.

#. Query logs on the log management page.

#. Select the node, log type, and log level you want to query, and then click |image1|. The query result is displayed.

   When you search for logs, the latest 10,000 logs are matched. A maximum of 100 logs are displayed.

Backing Up Logs
---------------

CSS cluster logs can be periodically backed up to specified OBS buckets.

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster. The cluster information page is displayed.

#. Click the **Logs** tab and toggle on the **Log Management** switch.

#. In the **Edit Log Backup Configuration** dialog box, set the parameters.

   In the displayed dialog box, **OBS Bucket** and **IAM Agency** are automatically created for log backup. You can change the default values by referring to :ref:`Table 1 <css_01_0508__css_01_0077_en-us_topic_0000001223434432_table109611127114919>`.

   If **Log Backup** has been enabled for the cluster, you can click the Edit icon on the right of **Log Backup Configuration** and modify the configuration in the displayed **Edit Log Backup Configuration** dialog box. For details, see :ref:`Table 1 <css_01_0508__css_01_0077_en-us_topic_0000001223434432_table109611127114919>`.

   .. _css_01_0508__css_01_0077_en-us_topic_0000001223434432_table109611127114919:

   .. table:: **Table 1** Configuring log backup

      +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter             | Description                                                                                                                               | Remarks                                                                                                                                                                                                                       |
      +=======================+===========================================================================================================================================+===============================================================================================================================================================================================================================+
      | **OBS Bucket**        | Select an OBS bucket from the drop-down list for storing logs. You can also click **Create Bucket** on the right to create an OBS bucket. | The OBS bucket and the cluster must be in the same region.                                                                                                                                                                    |
      |                       |                                                                                                                                           |                                                                                                                                                                                                                               |
      |                       |                                                                                                                                           | .. note::                                                                                                                                                                                                                     |
      |                       |                                                                                                                                           |                                                                                                                                                                                                                               |
      |                       |                                                                                                                                           |    To grant an IAM user access to an OBS bucket, you need to grant the **GetBucketStoragePolicy**, **GetBucketLocation**, **ListBucket**, and **ListAllMyBuckets** permissions to the user.                                   |
      +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | **Backup Path**       | Storage path of logs in the OBS bucket                                                                                                    | The backup path cannot:                                                                                                                                                                                                       |
      |                       |                                                                                                                                           |                                                                                                                                                                                                                               |
      |                       |                                                                                                                                           | -  Contain the following characters: ``\:*?"<>|'{}``                                                                                                                                                                          |
      |                       |                                                                                                                                           | -  Start with a slash (/).                                                                                                                                                                                                    |
      |                       |                                                                                                                                           | -  Start or end with a period (.).                                                                                                                                                                                            |
      |                       |                                                                                                                                           | -  Contain more than two consecutive slashes (/) or periods (.).                                                                                                                                                              |
      |                       |                                                                                                                                           | -  Exceed 512 characters.                                                                                                                                                                                                     |
      +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | **IAM Agency**        | IAM agency authorized by the current account for CSS to access or maintain data stored in OBS buckets.                                    | The IAM agency must meet the following requirements:                                                                                                                                                                          |
      |                       |                                                                                                                                           |                                                                                                                                                                                                                               |
      |                       |                                                                                                                                           | -  **Agency Type** must be **Cloud service**.                                                                                                                                                                                 |
      |                       |                                                                                                                                           | -  Set **Cloud Service** to **CSS**.                                                                                                                                                                                          |
      |                       |                                                                                                                                           | -  Mandatory policies: **Tenant Administrator**                                                                                                                                                                               |
      |                       |                                                                                                                                           | -  If no agency is available, contact the CSS administrator to create one. For details, see `Creating an Agency (by a Delegating Party) <https://docs.otc.t-systems.com/en-us/usermanual/iam/en-us_topic_0046613147.html>`__. |
      |                       |                                                                                                                                           |                                                                                                                                                                                                                               |
      |                       |                                                                                                                                           | .. note::                                                                                                                                                                                                                     |
      |                       |                                                                                                                                           |                                                                                                                                                                                                                               |
      |                       |                                                                                                                                           |    The agency name can contain only letters (case-sensitive), digits, underscores (_), and hyphens (-). Otherwise, the backup will fail.                                                                                      |
      +-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Back up logs.

   -  Automatically backing up logs

      Click the icon on the right of **Auto Backup** to enable the auto backup function.

      After the automatic backup function is enabled, set the backup start time in the **Configure Auto Backup** dialog box. When the scheduled time arrives, the system will back up logs automatically.

      After the **Automatic Snapshot Creation** function is enabled, you can click the Edit icon on the right of the parameter to change the backup start time.

   -  Manually backing up logs

      On the **Log Backup** tab page, click **Back Up**. In the displayed dialog box, click **Yes** to start backup.

      If **Task Status** in the log backup list is **Successful**, the backup is successful.

#. View log files.

   After logs are successfully backed up, you can click OBS Buckets to go to the bucket list, and find the bucket that stores the log files to view log files.

Log Files
---------

Deprecation logs, run logs, index slow logs, and search slow logs are backed up for Elasticsearch and OpenSearch clusters.

.. table:: **Table 2** Log file types

   ====================================== =====================
   Log Name                               Description
   ====================================== =====================
   clustername_deprecation.log            Deprecation log
   clustername_index_indexing_slowlog.log Search slow log
   clustername_index_search_slowlog.log   Index slow log
   clustername.log                        Elasticsearch run log
   clustername_access.log                 Access log
   ====================================== =====================

.. |image1| image:: /_static/images/en-us_image_0000001938377972.png
