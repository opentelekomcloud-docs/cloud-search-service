:original_name: en-us_topic_0000001528659105.html

.. _en-us_topic_0000001528659105:

Checking the Index Read and Write Traffic
=========================================

You can call an API to query the index read and write traffic within a period of time.

Prerequisites
-------------

A cluster has been created and :ref:`index monitoring <en-us_topic_0000001477579408>` has been enabled.

Procedure
---------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. Choose **Dev Tools** in the navigation pane on the left and run the following commands to query the index read and write traffic:

   -  Check read and write traffic of all the indexes.

      .. code-block:: text

         GET  /_cat/monitoring

   -  Check read and write traffic of a specific index.

      .. code-block:: text

         GET  /_cat/monitoring/{indexName}

      {indexName} indicates the name of the index whose read and write traffic you want to check.

   -  Check the read and write traffic of indexes for different periods.

      .. code-block:: text

         GET _cat/monitoring?begin=1650099461000
         GET _cat/monitoring?begin=2022-04-16T08:57:41
         GET _cat/monitoring?begin=2022-04-16T08:57:41&end=2022-04-17T08:57:41

      .. table:: **Table 1** Parameter description

         +-----------------------+-----------------------+-----------------------------------------------------------------+
         | Parameter             | Mandatory             | Description                                                     |
         +=======================+=======================+=================================================================+
         | begin                 | No                    | Start time (UTC time) of the monitoring data you want to view.  |
         |                       |                       |                                                                 |
         |                       |                       | Time format: strict_date_optional_time|epoch_millis             |
         |                       |                       |                                                                 |
         |                       |                       | The default start time is five minutes before the current time. |
         +-----------------------+-----------------------+-----------------------------------------------------------------+
         | end                   | No                    | End time (UTC time) of the monitoring data you want to view.    |
         |                       |                       |                                                                 |
         |                       |                       | Time format: strict_date_optional_time|epoch_millis             |
         |                       |                       |                                                                 |
         |                       |                       | The default end time is the current time.                       |
         +-----------------------+-----------------------+-----------------------------------------------------------------+

   .. note::

      These parameters cannot be used for system indexes, whose names start with a dot (.).

   Information similar to the following is displayed:

   .. code-block::

      index   begin               end                 status pri rep init unassign docs.count docs.deleted store.size pri.store.size delete.rate indexing.rate search.rate
      test 2022-03-25T09:46:53.765Z 2022-03-25T09:51:43.767Z yellow  1   1  0    1     9         0      5.9kb        5.9kb         0/s           0/s         0/s

   .. table:: **Table 2** Parameters in the returned information

      +----------------+------------------------------------------------------------------------------+
      | Parameter      | Description                                                                  |
      +================+==============================================================================+
      | index          | Index name                                                                   |
      +----------------+------------------------------------------------------------------------------+
      | begin          | Start time of the monitoring data you queried.                               |
      +----------------+------------------------------------------------------------------------------+
      | end            | End time of the monitoring data you queried.                                 |
      +----------------+------------------------------------------------------------------------------+
      | status         | Index status within the queried monitoring interval.                         |
      +----------------+------------------------------------------------------------------------------+
      | pri            | The number of index shards within the queried monitoring interval.           |
      +----------------+------------------------------------------------------------------------------+
      | rep            | The number of index replicas within the queried monitoring interval.         |
      +----------------+------------------------------------------------------------------------------+
      | init           | The number of initialized indexes within the queried monitoring interval.    |
      +----------------+------------------------------------------------------------------------------+
      | unassign       | The number of unallocated indexes within the queried monitoring interval.    |
      +----------------+------------------------------------------------------------------------------+
      | docs.count     | The number of documents within the queried monitoring interval.              |
      +----------------+------------------------------------------------------------------------------+
      | docs.deleted   | The number of deleted documents within the queried monitoring interval.      |
      +----------------+------------------------------------------------------------------------------+
      | store.size     | Index storage size within the queried monitoring interval.                   |
      +----------------+------------------------------------------------------------------------------+
      | pri.store.size | Size of the primary index shard within the queried monitoring interval.      |
      +----------------+------------------------------------------------------------------------------+
      | delete.rate    | Number of indexes deleted per second within the queried monitoring interval. |
      +----------------+------------------------------------------------------------------------------+
      | indexing.rate  | Number of indexes wrote per second within the queried monitoring interval.   |
      +----------------+------------------------------------------------------------------------------+
      | search.rate    | Number of indexes queried per second within the queried monitoring interval. |
      +----------------+------------------------------------------------------------------------------+
