:original_name: css_01_0077.html

.. _css_01_0077:

Managing Logs
=============

CSS provides log backup and search functions to help you locate faults. You can back up cluster logs to OBS buckets and download required log files to analyze and locate faults.

Enabling Log Management
-----------------------

#. Log in to the CSS management console.

#. On the **Clusters** page, click the name of the cluster whose logs you want to back up. The **Basic Information** page is displayed.

#. Click the **Logs** tab and enable **Log Management**.

   |image1| indicates that the log management function is disabled. |image2| indicates that it is enabled.

#. Enable the **Log Management** function. In the **Edit Log Backup Configuration** dialog box, set the parameters.

   In the displayed dialog box, **OBS Bucket**, **Backup Path**, and **IAM Agency** are automatically created for log backup. You can modify the default value by referring to :ref:`Table 1 <css_01_0077__table109611127114919>`.

   .. _css_01_0077__table109611127114919:

   .. table:: **Table 1** Parameter description

      +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter             | Description                                                                                                                                                                                 | Remarks                                                                                                                                                                |
      +=======================+=============================================================================================================================================================================================+========================================================================================================================================================================+
      | **OBS Bucket**        | Select an OBS bucket from the drop-down list for storing logs. You can also click **Create Bucket** on the right to create a new OBS bucket.                                                | The OBS bucket and the cluster must be in the same region.                                                                                                             |
      |                       |                                                                                                                                                                                             |                                                                                                                                                                        |
      |                       |                                                                                                                                                                                             | .. note::                                                                                                                                                              |
      |                       |                                                                                                                                                                                             |                                                                                                                                                                        |
      |                       |                                                                                                                                                                                             |    To let an IAM user access an OBS bucket, you need to grant the GetBucketStoragePolicy, GetBucketLocation, ListBucket, and ListAllMyBuckets permissions to the user. |
      +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | **IAM Agency**        | IAM agency authorized by the current account for CSS to access or maintain data stored in the OBS bucket. You can also click **Create IAM Agency** on the right to create a new IAM agency. | The IAM agency must meet the following requirements:                                                                                                                   |
      |                       |                                                                                                                                                                                             |                                                                                                                                                                        |
      |                       |                                                                                                                                                                                             | -  **Agency Type** must be **Cloud service**.                                                                                                                          |
      |                       |                                                                                                                                                                                             | -  Set **Cloud Service** to **CSS**.                                                                                                                                   |
      |                       |                                                                                                                                                                                             | -  Mandatory policies: **Tenant Administrator**                                                                                                                        |
      +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. (Optional) If the **Log Management** function has been enabled for the cluster, you can modify the log backup parameters.

   Click |image3| on the right of **Log Backup Configuration**. The **Edit Log Backup Configuration** dialog box is displayed. You can modify the log backup parameters.

#. Back up logs.

   -  Automatically backing up logs

      Click the icon on the right of **Auto Backup** to enable the auto backup function.

      |image4| indicates that the auto backup function is enabled, and |image5| indicates that it is disabled.

      After the automatic backup function is enabled, set the backup start time in the **Modify Log Backup Policy** dialog box. When the scheduled time arrives, the system will back up logs automatically. Click |image6| on the right of the switch to change **Backup Start Time**.

   -  Manually backing up logs

      On the **Log Backup** tab page, click **Back Up**. On the displayed page, click **Yes** to start backup.

      If **Task Status** in the log backup list is **Successful**, the backup is successful.

      .. note::

         All logs in the cluster are copied to a specified OBS path. You can view or download log files from the path of the OBS bucket.

#. Search for logs.

   On the **Log Search** page, select the desired node, log type, and log level, and click |image7|. The search results are displayed.

   When you search for logs, the latest 10,000 logs are matched. A maximum of 100 logs are displayed.

Viewing Logs
------------

After backing up logs, you can click **Backup Path** to go to the OBS console and view the logs.

Backed up logs mainly include deprecation logs, run logs, index slow logs, and search slow logs. :ref:`Table 2 <css_01_0077__table19918142319532>` lists the storage types of the OBS bucket.

.. _css_01_0077__table19918142319532:

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

.. |image1| image:: /_static/images/en-us_image_0000001474565996.png
.. |image2| image:: /_static/images/en-us_image_0000001524925961.png
.. |image3| image:: /_static/images/en-us_image_0000001524925965.png
.. |image4| image:: /_static/images/en-us_image_0000001525205857.png
.. |image5| image:: /_static/images/en-us_image_0000001474565996.png
.. |image6| image:: /_static/images/en-us_image_0000001474246372.png
.. |image7| image:: /_static/images/en-us_image_0000001524766285.png
