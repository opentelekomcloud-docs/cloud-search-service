:original_name: css_01_0077.html

.. _css_01_0077:

Querying Logs
=============

During routine O&M, when an Elasticsearch cluster becomes sluggish, returns an error for a query request, or shows a yellow status, the O&M team must be able to obtain relevant information immediately. CSS provides a log query feature that aggregates underlying server logs to the console, where you can query them by node and log level in seconds. By analyzing run logs, slow query logs, and deprecation logs, you can quickly locate the root causes of faults and issues. Additionally, you can dynamically adjust log levels and enable trace logging for debugging, allowing you to obtain the most detailed log records without restarting your cluster.

Querying Recent Logs
--------------------

Query recently generated logs that are not yet archived.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Logs > Log Search**. The **Log Search** page is displayed.

   You can search records by log type, node, log level, or keyword. For a detailed description of each type of logs, see :ref:`Log Types <en-us_topic_0000001965416649__section132041636163218>`.

   .. caution::

      When a log file reaches 128 MB or when the time reaches 00:00 UTC, the system automatically compresses and archives it. Only unarchived logs appear on the log search page, while archived logs remain accessible through the log backup function. For more information, see :ref:`Backing Up Logs to OBS <css_01_0164>`.

Adjusting Log Levels Dynamically
--------------------------------

Log4j2 is used as the log component in Elasticsearch clusters. Multiple log levels (ERROR, WARN, INFO, DEBUG, and TRACE) are supported. The default log level is INFO. To facilitate troubleshooting and debugging, you can dynamically adjust the log levels.

-  INFO is the default log level. The levels, in order of increasing detail, are: ERROR, WARN, INFO, DEBUG, and TRACE. When INFO is set, you will see logs for itself and all higher-severity levels (ERROR and WARN), while more verbose levels (DEBUG and TRACE) are excluded.
-  You can change the log level of a specified module in real time via an Elasticsearch API.

#. Log in to Kibana and go to the command execution page. Elasticsearch clusters support multiple access methods. This topic uses Kibana as an example to describe the operation procedures.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

   c. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   d. In the left navigation pane, choose **Dev Tools**.

      The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

#. Run the following command to change the log level, for example, to DEBUG:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "logger": {
            "org.elasticsearch.action": "DEBUG"
          }
        }
      }

#. Refresh the log query page and check whether DEBUG logs have been generated. You should always restore the log level to the default setting once you finish the task at hand.

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

Enabling Trace Logging
----------------------

To analyze communication details on the HTTP or transport layer, you can enable trace logging for the HTTP or Transport module to obtain detailed log records.

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

   .. caution::

      Enabling trace logging is a non-persistent configuration and will be disabled upon a cluster restart. It is typically used for emergency packet capture and analysis during troubleshooting.

#. Go to the log details page to view trace logs.

   a. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
   b. Choose **Logs > Log Search**. The **Log Search** page is displayed.
   c. Select all log levels (mandatory) and view trace logs.

.. _en-us_topic_0000001965416649__section132041636163218:

Log Types
---------

.. table:: **Table 1** Introducing different log types

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

   Run logs record the cluster status and key information about write and query operations. For example, the log record below indicates that an index named **test** was created and later the cluster status changed from **YELLOW** to **GREEN**.


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
   -  4. Log level, which can be DEBUG, INFO, WARN, or ERROR
   -  5. Log request method
   -  6. Request path
   -  7. Source and destination addresses of the request

Related Documents
-----------------

:ref:`How Do I Set Slow Query Log Thresholds for an Elasticsearch Cluster of CSS? <css_02_0096>`
