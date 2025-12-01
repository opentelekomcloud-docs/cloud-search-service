:original_name: css_01_0077.html

.. _css_01_0077:

Managing Elasticsearch Cluster Logs
===================================

CSS provides log query and log backup, enabling you to easily manage and analyze logs to efficiently locate faults, optimize performance, and enhance system security.

-  Log query: On the log management page of the CSS management console, you can query the latest log records by node, log type, and other criteria, so you can quickly locate or diagnose issues.
-  Log backup: Cluster logs are periodically synchronized to OBS buckets. You can download them for in-depth analysis at any time. You can configure custom log backup policies by specifying backup schedules and storage locations. The system backs up all critical logs, including run logs, slow query logs, and deprecation logs. They provide comprehensive data for auditing and troubleshooting purposes.

Impact on Billing
-----------------

When log backup is enabled, the generated log backups are stored in OBS buckets, which will result in additional costs. For details, see .

Prerequisites
-------------

The OBS bucket used for storing log backups has been created. The OBS bucket must meet the following requirements:

-  **Storage Class**: **Standard** or **Warm**.
-  **Region**: the same as that of the cluster.

Querying Logs
-------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Logs > Log Search**. The **Log Search** page is displayed.

   You can search records by log type, node, log level, or keyword. For a detailed description of each type of logs, see :ref:`Log Introduction <en-us_topic_0000001965416649__section132041636163218>`.

   When a log file reaches 128 MB or when the time reaches 00:00 UTC, the system automatically compresses and archives it. Only unarchived logs appear on the log search page, while archived logs remain accessible through the log backup function.

Backing Up Logs
---------------

Cluster logs can be backed up to OBS buckets, where you can download them for in-depth analysis at any time.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Logs > Log Backup**. The **Log Backup** page is displayed.

#. Enable log backup.

   Perform the following steps to enable log backup. If it is already enabled, skip this step.

   a. Click **Enable Backup**. In the displayed dialog box, configure necessary settings.

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

      -  To enable automatic, periodic log backup, select **Automatic backup**, and set the backup policy. For more information, see :ref:`Table 2 <en-us_topic_0000001965416649__table13235122823218>`.
      -  If manual log backup is sufficient, deselect **Automatic backup**.

   b. Click **OK** to enable log backup.

      The configuration information will be displayed on the **Log Backup** tab.

#. Back up logs. Two options are available: automatic or manual.

   Automatic log backup: Logs are backed up periodically based on the preset policy.

   a. On the **Log Backup** page, click **Modify Settings** on the right.

   b. In the **Modify Settings** dialog box, select **Automatic backup**, and configure the automatic backup policy.

      .. _en-us_topic_0000001965416649__table13235122823218:

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

   c. Click **OK** to enable automatic log backup.

      Automatic log backup tasks are displayed in the task list. When **Task Status** in the task list changes to **Succeeded**, the backup is successful.

      If log backup fails, click **Failed Tasks** learn the failure causes. A maximum of 10 failed tasks can be displayed. When log backup is disabled or the cluster is deleted, the failure records are also cleared.

   d. If automatic log backup is not required, click **Modify Settings**. In the displayed dialog box, deselect **Automatic backup**, and click **OK**. In the displayed confirmation dialog box, click **OK**.

      Disabling log backup does not automatically delete log backups automatically generated earlier. Instead, you need to manually delete them on the OBS console.

   Manual log backup: Back up logs right away.

   a. On the **Log Backup** page, click **Back Up Manually** under **Log Backup Tasks**.

   b. In the displayed dialog box, confirm the log backup path and click **OK**.

      The log backup task is displayed in the task list. When **Task Status** in the task list changes to **Succeeded**, the backup is successful.

      If log backup fails, click **Failed Tasks** learn the failure causes. A maximum of 10 failed tasks can be displayed. When log backup is disabled or the cluster is deleted, the failure records are also cleared.

#. Check the backed-up log files.

   Logs are backed up incrementally. After the backup is successful, you can access the target OBS bucket to obtain the full log files by clicking **Log Path**.

   :ref:`Table 3 <en-us_topic_0000001965416649__table11352134814319>` lists the log types, where **clustername** indicates the cluster name.

   .. _en-us_topic_0000001965416649__table11352134814319:

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

#. If the log backup function is no longer needed, you can disable it.

   On the **Log Backup** page, click **Disable Backup**. In the displayed dialog box, click **OK**. Disabling log backup does not automatically delete existing log backups. Instead, you need to manually delete them on the OBS console.

.. _en-us_topic_0000001965416649__section132041636163218:

Log Introduction
----------------

.. table:: **Table 4** Introduction to different log types

   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Log Type              | Description                                                                                                                                                                                                                                                                                | Purpose                                                                                                                                                                       |
   +=======================+============================================================================================================================================================================================================================================================================================+===============================================================================================================================================================================+
   | Run logs              | Run logs, or main logs, record the cluster status and key information about write and query operations. For example, write logs record operations such as index creation, index mapping update, and write queue exhaustion; and query logs record query queue status and query exceptions. | Check the status and write and query operations of each cluster node, including inter-node connectivity, full GC, index creation or deletion, and cluster-level query errors. |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Slow indexing logs    | Slow indexing logs record indexing operations (such as bulk, index, update, and delete) that took a long time to complete, helping you identify performance bottlenecks.                                                                                                                   | In the case of slow write performance, you can query slow indexing logs to locate the cause.                                                                                  |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Slow query logs       | Slow query logs record search requests that took a long time to complete. They help you monitor and analyze time-consuming search requests, so you can identify performance bottlenecks, optimize SQL queries, and improve overall system performance.                                     | In the case of slow query performance, you can query slow query logs to locate the cause.                                                                                     |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Deprecation logs      | Deprecation logs record deprecation warnings. Deprecation warnings are written to this log when you use APIs, configurations, or functions that are marked for removal in future versions.                                                                                                 | Check for APIs or features that are about to expire in future versions.                                                                                                       |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Access logs           | Access logs record cluster access requests, such as the request path and source address.                                                                                                                                                                                                   | If there is a surge in service requests, you can analyze the request sources and paths by checking the access logs.                                                           |
   |                       |                                                                                                                                                                                                                                                                                            |                                                                                                                                                                               |
   |                       | You cannot check access logs on the console. To check them, you need to back them up to an OBS bucket or transfer them to a target cluster first.                                                                                                                                          |                                                                                                                                                                               |
   +-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

-  **Run log description**

   Run logs record the cluster status and key information about write and query operations. For example, the log record below indicates that an index named **test** was created and afterwards the cluster status changed from **YELLOW** to **GREEN**.


   .. figure:: /_static/images/en-us_image_0000002346926270.png
      :alt: **Figure 1** A sample of run logs

      **Figure 1** A sample of run logs

   Log content:

   -  1. Log generation time
   -  2. Log level, which can be DEBUG, INFO, WARN, or ERROR
   -  3. Log-generating module
   -  4. Name of the log-generating node
   -  5. Log content

-  **Slow indexing log description**

   Slow indexing logs record indexing operations that took a long time to complete. For example, the log record below shows an indexing request that lasted longer than the preset threshold. The log contains the index name, duration, and request content.


   .. figure:: /_static/images/en-us_image_0000002346766550.png
      :alt: **Figure 2** A sample of slow indexing logs

      **Figure 2** A sample of slow indexing logs

   Log content:

   -  1. Log generation time

   -  2. Log level, which can be DEBUG, INFO, WARN, or ERROR

   -  3. Log-generating module

   -  4. Name of the log-generating node

   -  5. Index name and ID

   -  6. Log content. In this example, the log recorded the request execution duration, index type, and index request body.

-  **Slow query log description**

   Slow query logs record search requests that took a long time to complete. For example, the log record below shows a search request that lasted longer than the preset threshold. The log contains the index name, duration, and request content.


   .. figure:: /_static/images/en-us_image_0000002380566773.png
      :alt: **Figure 3** A sample of slow query logs

      **Figure 3** A sample of slow query logs

   Log content:

   -  1. Log generation time
   -  2. Log level, which can be DEBUG, INFO, WARN, or ERROR
   -  3. Log-generating module
   -  4. Name of the log-generating node
   -  5. Index name and shard ID
   -  6. Log content. In this example, the log recorded the query duration, number of hits, and query request body.

-  **Deprecation log description**

   Deprecation logs record deprecation warnings. For example, the log record below indicates that **GET /_cat/master** has been deprecated and should be replaced with **GET /_cat/cluster_manager**.


   .. figure:: /_static/images/en-us_image_0000002380607013.png
      :alt: **Figure 4** A sample of deprecation logs

      **Figure 4** A sample of deprecation logs

   Log content:

   -  1. Log generation time
   -  2. Log level, which can only be DEPRECATION.
   -  3. Log-generating module
   -  4. Name of the log-generating node
   -  5. Log content

-  **Access log description**

   Access logs record cluster access requests and source addresses. For example, the log record below has recorded source information for the /_snapshot/my_backup/my_snapshot/_restore?pretty=true operation.


   .. figure:: /_static/images/en-us_image_0000002384639989.png
      :alt: **Figure 5** A sample of access logs

      **Figure 5** A sample of access logs

   Log content:

   -  1. Log generation time
   -  2. Name of the log-generating node
   -  3. Name of the log-generating thread
   -  4. Log level, which can be DEBUG, INFO, WARN, or ERROR.
   -  5. Log request method
   -  6. Request path
   -  7. Source and destination addresses of the request

FAQ: How Do I Change Log Levels?
--------------------------------

Log4j2 is used as the log component in Elasticsearch clusters. Multiple log levels (ERROR, WARN, INFO, DEBUG, and TRACE) are supported. The default log level is INFO. To facilitate troubleshooting and debugging, you can dynamically adjust the log levels.

-  INFO is the default log level. The levels, in order of increasing detail, are: ERROR, WARN, INFO, DEBUG, and TRACE. When INFO is set, you will see logs for itself and all higher-severity levels (ERROR and WARN), while more verbose levels (DEBUG and TRACE) are excluded.
-  You can change the log level of a specified module in real time via an Elasticsearch API.

**Example**

#. Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. Run the following command to change the log level of the action module to **DEBUG**:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "logger": {
            "org.elasticsearch.action": "DEBUG"
          }
        }
      }

#. Run the following command to restore the default log level **INFO**:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "logger": {
            "org.elasticsearch.action": null
          }
        }
      }

FAQ: How Do I Enable Trace Logging?
-----------------------------------

To facilitate troubleshooting, debugging, and performance analysis, you may enable trace logging for the HTTP/Transport module and view detailed trace logs.

Enabling trace logging is a non-persistent configuration and will be disabled upon a cluster restart.

**Operation Guide**

#. Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. Run the following command to enable trace logging:

   .. code-block:: text

      PUT _cluster/settings
      {
        "transient": {
          "logger.org.elasticsearch.transport.TransportService.tracer": "trace",
          "transport.tracer.include": "",
          "http.tracer.include": "",
          "logger.org.elasticsearch.http.HttpTracer": "trace"
        }
      }

#. Go to the log details page to view trace logs.

   a. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
   b. Choose **Logs > Log Search**. The **Log Search** page is displayed.
   c. Select all log levels (mandatory) and view trace logs.

Related Documents
-----------------

:ref:`How Do I Set Slow Query Log Thresholds for an Elasticsearch Cluster of CSS? <css_02_0096>`
