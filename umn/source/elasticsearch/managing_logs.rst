:original_name: css_01_0077.html

.. _css_01_0077:

Managing Logs
=============

CSS provides log backup and search functions to help you locate faults. You can back up cluster logs to OBS buckets and download required log files to analyze and locate faults.

Log Query
---------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster. The cluster information page is displayed.

#. In the navigation pane on the left, choose **Log Management**.

#. Query logs on the log management page.

   Select the node, log type, and log level you want to query, and then click |image1|. The query result is displayed.

   When you search for logs, the latest 10,000 logs are matched. A maximum of 100 logs are displayed.

Enabling Log Backup
-------------------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster. The cluster information page is displayed.

#. Click the **Logs** tab and toggle on the **Log Management** switch.

#. In the **Edit Log Backup Configuration** dialog box, set the parameters.

   In the displayed dialog box, **OBS Bucket** and **IAM Agency** are automatically created for log backup. You can change the default value by referring to :ref:`Table 1 <css_01_0077__en-us_topic_0000001223434432_table109611127114919>`.

   If the **Log Management** function has been enabled for the cluster, you can click |image2| on the right of **Log Backup Configuration** and modify the configuration in the displayed **Edit Log Backup Configuration** dialog box. For details, see :ref:`Table 1 <css_01_0077__en-us_topic_0000001223434432_table109611127114919>`.

   .. _css_01_0077__en-us_topic_0000001223434432_table109611127114919:

   .. table:: **Table 1** Parameters for configuring log backup

      +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter             | Description                                                                                                                                                                              | Remarks                                                                                                                                                                |
      +=======================+==========================================================================================================================================================================================+========================================================================================================================================================================+
      | **OBS Bucket**        | Select an OBS bucket from the drop-down list for storing logs. You can also click **Create Bucket** on the right to create an OBS bucket.                                                | The OBS bucket and the cluster must be in the same region.                                                                                                             |
      |                       |                                                                                                                                                                                          |                                                                                                                                                                        |
      |                       |                                                                                                                                                                                          | .. note::                                                                                                                                                              |
      |                       |                                                                                                                                                                                          |                                                                                                                                                                        |
      |                       |                                                                                                                                                                                          |    To let an IAM user access an OBS bucket, you need to grant the GetBucketStoragePolicy, GetBucketLocation, ListBucket, and ListAllMyBuckets permissions to the user. |
      +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | **Backup Path**       | Storage path of logs in the OBS bucket                                                                                                                                                   | The backup path configuration rules are as follows:                                                                                                                    |
      |                       |                                                                                                                                                                                          |                                                                                                                                                                        |
      |                       |                                                                                                                                                                                          | -  The backup path cannot contain the following characters: ``\:*?"<>|``                                                                                               |
      |                       |                                                                                                                                                                                          | -  The backup path cannot start with a slash (/).                                                                                                                      |
      |                       |                                                                                                                                                                                          | -  The backup path cannot start or end with a period (.).                                                                                                              |
      |                       |                                                                                                                                                                                          | -  The total length of the backup path cannot exceed 1,023 characters.                                                                                                 |
      +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | **IAM Agency**        | IAM agency authorized by the current account for CSS to access or maintain data stored in the OBS bucket. You can also click **Create IAM Agency** on the right to create an IAM agency. | The IAM agency must meet the following requirements:                                                                                                                   |
      |                       |                                                                                                                                                                                          |                                                                                                                                                                        |
      |                       |                                                                                                                                                                                          | -  **Agency Type** must be **Cloud service**.                                                                                                                          |
      |                       |                                                                                                                                                                                          | -  Set **Cloud Service** to **CSS**.                                                                                                                                   |
      |                       |                                                                                                                                                                                          | -  Mandatory policies: **Tenant Administrator**                                                                                                                        |
      +-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Back up logs.

   -  Automatically backing up logs

      Click the icon on the right of **Auto Backup** to enable the auto backup function.

      After the automatic backup function is enabled, set the backup start time in the **Configure Auto Backup** dialog box. When the scheduled time arrives, the system will back up logs automatically.

      After the **Automatic Snapshot Creation** function is enabled, you can click |image3| on the right of the parameter to change the backup start time.

   -  Manually backing up logs

      On the **Log Backup** tab page, click **Back Up**. On the displayed page, click **Yes** to start backup.

      If **Task Status** in the log backup list is **Successful**, the backup is successful.

      .. note::

         All logs in the cluster are copied to a specified OBS path. You can view or download log files from the path of the OBS bucket.

#. Search for logs.

   On the **Log Search** page, select the target node, log type, and log level, and click |image4|. The search results are displayed.

   When you search for logs, the latest 10,000 logs are matched. A maximum of 100 logs are displayed.

Viewing Logs
------------

After backing up logs, you can click **Backup Path** to go to the OBS console and view the logs.

Backed up logs mainly include deprecation logs, run logs, index slow logs, and search slow logs. :ref:`Table 2 <css_01_0077__en-us_topic_0000001223434432_table19918142319532>` lists the storage types of the OBS bucket.

.. _css_01_0077__en-us_topic_0000001223434432_table19918142319532:

.. table:: **Table 2** Log types

   ====================================== =====================
   Log Name                               Description
   ====================================== =====================
   clustername_deprecation.log            Deprecation log
   clustername_index_indexing_slowlog.log Search slow log
   clustername_index_search_slowlog.log   Index slow log
   clustername.log                        Elasticsearch run log
   clustername_access.log                 Access log
   clustername_audit.log                  Audit log
   ====================================== =====================

.. |image1| image:: /_static/images/en-us_image_0000001714921993.png
.. |image2| image:: /_static/images/en-us_image_0000001666842674.png
.. |image3| image:: /_static/images/en-us_image_0000001667002374.png
.. |image4| image:: /_static/images/en-us_image_0000001667002402.png
