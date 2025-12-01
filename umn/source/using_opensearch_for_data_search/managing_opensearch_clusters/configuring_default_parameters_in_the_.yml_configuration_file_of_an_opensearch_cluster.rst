:original_name: css_01_0316.html

.. _css_01_0316:

Configuring Default Parameters in the .yml Configuration File of an OpenSearch Cluster
======================================================================================

You can modify an OpenSearch cluster's configuration file for purposes like accelerating queries, modifying cross-domain access configuration, adjusting the internal cache size, and managing the task queue size. The core configuration information of an OpenSearch cluster is stored in a named **opensearch.yml**. You can modify specific parameters in this file on the CSS management console.

Configuring the .yml File
-------------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Cluster Settings** > **Parameter Settings**.

#. Click **Edit** to modify module parameters as required.

   .. table:: **Table 1** Module parameters

      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Module Name                 | Parameter                    | Description                                                                                                                                                               |
      +=============================+==============================+===========================================================================================================================================================================+
      | Cross-domain Access         | http.cors.allow-credentials  | Whether to carry authentication information in cross-domain requests, that is, whether to contain the Access-Control-Allow-Credentials field in the response header.      |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | The value can be:                                                                                                                                                         |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | -  **true**: The response header contains the Access-Control-Allow-Credentials field.                                                                                     |
      |                             |                              | -  **false** (default value): The response header does not contain the Access-Control-Allow-Credentials field.                                                            |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-origin       | Source IP addresses or domain names allowed for cross-domain access. When there are multiple values, separate them with commas (,).                                       |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Example: **192.168.122.122:9200** or **192.168.1.1:9200, 192.168.1.2:9200**                                                                                               |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-headers      | Request header fields for cross-domain access. When there are multiple values, separate them using a comma (,) and a space.                                               |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Example: **X-Requested-With, Content-Type, Content-Length**                                                                                                               |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | The value can contain a maximum of 1024 characters. It can only contain letters, digits, hyphens (-), underscores (_), colons (:), and slashes (/).                       |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.max-age            | Maximum retention duration of pre-check responses in the browser cache.                                                                                                   |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Unit: s                                                                                                                                                                   |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Value range: 0 to 31,536,000 (0 to 1 year)                                                                                                                                |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Default value: 1,728,000 (20 days)                                                                                                                                        |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.enabled            | Whether to enable cross-domain access.                                                                                                                                    |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | The value can be:                                                                                                                                                         |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | -  **true**: Enable cross-domain access.                                                                                                                                  |
      |                             |                              | -  **false** (default): Disable cross-domain access.                                                                                                                      |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-methods      | HTTP methods allowed for cross-domain access. When there are multiple values, separate them using a comma (,) and a space.                                                |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Example: **OPTIONS, GET, POST**                                                                                                                                           |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Value range: OPTIONS, HEAD, GET, POST, PUT, and DELETE                                                                                                                    |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Reindexing                  | reindex.remote.whitelist     | Which remote hosts are allowed for remote reindexing operations. Use commas (,) to separate multiple values.                                                              |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Example: **192.168.122.122:9200** or **192.168.1.1:9200, 192.168.1.2:9200**                                                                                               |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Custom Cache                | indices.queries.cache.size   | Maximum heap space allocated to the query cache.                                                                                                                          |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Unit: percentage (%)                                                                                                                                                      |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Value range: 1 to 100                                                                                                                                                     |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Default value: 10%                                                                                                                                                        |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Queue Size in a Thread Pool | thread_pool.force_merge.size | Size of the thread pool used for force merge operations.                                                                                                                  |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Value range: a positive integer                                                                                                                                           |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | Default value: 1                                                                                                                                                          |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Custom                      | Custom parameters            | You can add any custom parameters supported by Elasticsearch.                                                                                                             |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | The parameter values must meet the following requirements:                                                                                                                |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | -  If a custom parameter has multiple values, use a comma (,) and a space to separate them. The input format is [value1, value1, value1...].                              |
      |                             |                              | -  Colons (:) are not allowed.                                                                                                                                            |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              | .. warning::                                                                                                                                                              |
      |                             |                              |                                                                                                                                                                           |
      |                             |                              |    Set the values of any custom parameters to those supported by OpenSearch. Otherwise, the cluster may fail to restart. Exercise caution when performing this operation. |
      +-----------------------------+------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. After the modification is complete, click **Submit**. In the displayed **Submit Configuration** dialog box, select the box indicating "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

   If the **Status** is **Succeeded** in the parameter modification list, the modification has been saved. Up to 20 modification records can be displayed.

#. Click **Restart** in the upper right corner to restart the cluster, thus applying the changes.

   -  You need to restart the cluster after modification, or **Configuration not updated** will be displayed in the **Task Status** column in the cluster list.
   -  If you restart the cluster after the modification, and **Task Status** displays **Configuration error** in the cluster list, the parameter configuration file has failed to be modified.
