:original_name: en-us_topic_0000001477579408.html

.. _en-us_topic_0000001477579408:

Enabling Index Monitoring
=========================

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. Choose **Dev Tools** in the navigation pane on the left and run the following command to enable index monitoring:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "css.monitoring.index.enabled": "true"
        }
      }

#. (Optional) To monitor a specific index, run the following command on the **Dev Tools** page of Kibana:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "css.monitoring.index.enabled": "true",
          "css.monitoring.index.interval": "30s",
          "css.monitoring.index.indices": ["index_name"],
          "css.monitoring.history.duration": "3d"
        }
      }

   .. table:: **Table 1** Parameter description

      +---------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                       | Data Type             | Description                                                                                                                                  |
      +=================================+=======================+==============================================================================================================================================+
      | css.monitoring.index.enabled    | Boolean               | Whether to enable index monitoring. If this parameter is set to **true**, the monitoring will be enabled.                                    |
      |                                 |                       |                                                                                                                                              |
      |                                 |                       | Default value: **false**                                                                                                                     |
      +---------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
      | css.monitoring.index.interval   | Time                  | Interval for collecting index monitoring data.                                                                                               |
      |                                 |                       |                                                                                                                                              |
      |                                 |                       | Minimum value: **1s**                                                                                                                        |
      |                                 |                       |                                                                                                                                              |
      |                                 |                       | Default value: **10s**                                                                                                                       |
      +---------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
      | css.monitoring.index.indices    | String                | Name of an index to be monitored. By default, all indexes are monitored. You can configure specific indexes or a type of indexes to monitor. |
      |                                 |                       |                                                                                                                                              |
      |                                 |                       | Example:                                                                                                                                     |
      |                                 |                       |                                                                                                                                              |
      |                                 |                       | -  **""css.monitoring.index.indices": ["**\ *index_name*\ **"]"** indicates only *index_name* is monitored.                                  |
      |                                 |                       | -  **"css.monitoring.index.indices": ["log_*"]** indicates that only indexes starting with **log\_** are monitored.                          |
      |                                 |                       | -  **"css.monitoring.index.indices": ["index1", "index2"]** indicates that **index1** and **index2** are monitored.                          |
      |                                 |                       |                                                                                                                                              |
      |                                 |                       | Default value: **\*** (indicating that all indexes are monitored)                                                                            |
      +---------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
      | css.monitoring.history.duration | Time                  | Retention period of monitoring data storage. The default period is a week.                                                                   |
      |                                 |                       |                                                                                                                                              |
      |                                 |                       | Minimum value: **1d**                                                                                                                        |
      |                                 |                       |                                                                                                                                              |
      |                                 |                       | Default value: **7d**                                                                                                                        |
      +---------------------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

   .. important::

      Indexes starting with **monitoring-eye-css-\*** are regarded as monitoring indexes and will not be monitored.
