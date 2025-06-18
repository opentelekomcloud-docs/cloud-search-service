:original_name: css_01_0080.html

.. _css_01_0080:

Configuring Default Parameters in the .yml Configuration File of an Elasticsearch Cluster
=========================================================================================

CSS allows you to modify the **elasticsearch.yml** file, which is the Elasticsearch configuration file that is used to set and manage various parameters and behavior of an Elasticsearch cluster. By properly configuring the parameters in this file, you may be able to optimize cluster performance and improve system stability and security.

Configuring the .yml File
-------------------------

#. Log in to the CSS management console.

#. Choose **Clusters** from the navigation pane. On the **Clusters** page, click the name of the target cluster. The cluster information page is displayed.

#. Click **Parameter Configurations** and click **Edit** to modify module parameters as required.

   .. table:: **Table 1** Module parameters

      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Module Name                 | Parameter                                   | Description                                                                                                                                                                     |
      +=============================+=============================================+=================================================================================================================================================================================+
      | Cross-domain Access         | http.cors.allow-credentials                 | Whether to return the Access-Control-Allow-Credentials of the header during cross-domain access                                                                                 |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Value: **true** or **false**                                                                                                                                                    |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Default value: **false**                                                                                                                                                        |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-origin                      | Origin IP address allowed for cross-domain access, for example, **122.122.122.122:9200**                                                                                        |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.max-age                           | Cache duration of the browser. The cache is automatically cleared after the time range you specify.                                                                             |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Unit: s                                                                                                                                                                         |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Default value: **1,728,000**                                                                                                                                                    |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-headers                     | Headers allowed for cross-domain access, including **X-Requested-With**, **Content-Type**, and **Content-Length**. Use commas (,) and spaces to separate headers.               |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.enabled                           | Whether to allow cross-domain access                                                                                                                                            |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Value: **true** or **false**                                                                                                                                                    |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Default value: **false**                                                                                                                                                        |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-methods                     | Methods allowed for cross-domain access, including **OPTIONS**, **HEAD**, **GET**, **POST**, **PUT**, and **DELETE**. Use commas (,) and spaces to separate methods.            |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Reindexing                  | reindex.remote.whitelist                    | Configure this parameter to migrate data from the current cluster to the destination cluster through the reindex API. The example value is **122.122.122.122:9200**.            |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Custom Cache                | indices.queries.cache.size                  | Cache size in the query phase                                                                                                                                                   |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Value range: 1 to 100                                                                                                                                                           |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Unit: %                                                                                                                                                                         |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Default value: **10%**                                                                                                                                                          |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Queue Size in a Thread Pool | thread_pool.force_merge.size                | Queue size in the force merge thread pool. The value is an integer.                                                                                                             |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | Default value: **1**                                                                                                                                                            |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Customize                   | You can add parameters based on your needs. | Customized parameters                                                                                                                                                           |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             | .. note::                                                                                                                                                                       |
      |                             |                                             |                                                                                                                                                                                 |
      |                             |                                             |    -  Enter multiple values in the format as **[value1, value2, value3...]**.                                                                                                   |
      |                             |                                             |    -  Separate values by commas (,) and spaces.                                                                                                                                 |
      |                             |                                             |    -  Colons (:) are not allowed.                                                                                                                                               |
      |                             |                                             |    -  Set the values of any custom parameters to those supported by Elasticsearch. Otherwise, the cluster may fail to restart. Exercise caution when performing this operation. |
      +-----------------------------+---------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. After the modification is complete, click **Submit**. In the displayed **Submit Configuration** dialog box, select the box indicating "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

   If the **Status** is **Succeeded** in the parameter modification list, the modification has been saved. Up to 20 modification records can be displayed.

#. Return to the cluster list and choose **More** > **Restart** in the **Operation** column to restart the cluster and make the modification take effect.

   -  You need to restart the cluster after modification, or **Configuration not updated** will be displayed in the **Task Status** column on the **Clusters** page.
   -  If you restart the cluster after the modification, and **Task Status** displays **Configuration error**, the parameter configuration file fails to be modified.
