:original_name: css_01_0080.html

.. _css_01_0080:

Configuring Parameters
======================

CSS allows you to modify configurations in the **elasticsearch.yml** file on the CSS console. You need to restart the cluster for the modifications to take effect.

Modifying Parameter Configurations
----------------------------------

#. Log in to the CSS management console.

#. On the **Clusters** page, click the name of the cluster for which you want to modify parameter configurations. The **Basic Information** page is displayed.

#. Click **Parameter Configurations** and modify parameters of the corresponding module based on your needs.

   .. table:: **Table 1** Module parameters

      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Module Name                 | Parameter                                   | Description                                                                                                                                                          |
      +=============================+=============================================+======================================================================================================================================================================+
      | Cross-domain Access         | http.cors.allow-credentials                 | Whether to return the Access-Control-Allow-Credentials of the header during cross-domain access                                                                      |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Value: **true** and **false**                                                                                                                                        |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Default value: **false**                                                                                                                                             |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-origin                      | Origin IP address allowed for cross-domain access, for example, **122.122.122.122:9200**                                                                             |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.max-age                           | Cache duration of the browser. The cache is automatically cleared after the time range you specify.                                                                  |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Unit: s                                                                                                                                                              |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Default value: **1,728,000**                                                                                                                                         |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-headers                     | Headers allowed for cross-domain access, including **X-Requested-With**, **Content-Type**, and **Content-Length**. Use commas (,) and spaces to separate headers.    |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.enabled                           | Whether to allow cross-domain access                                                                                                                                 |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Value: **true** and **false**                                                                                                                                        |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Default value: **false**                                                                                                                                             |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | http.cors.allow-methods                     | Methods allowed for cross-domain access, including **OPTIONS**, **HEAD**, **GET**, **POST**, **PUT**, and **DELETE**. Use commas (,) and spaces to separate methods. |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Reindexing                  | reindex.remote.whitelist                    | Configured for migrating data from the current cluster to the target cluster through the reindex API. The example value is 122.122.122.122:9200.                     |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Custom Cache                | indices.queries.cache.size                  | Cache size in the query phase                                                                                                                                        |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Value range: 1 to 100                                                                                                                                                |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Unit: %                                                                                                                                                              |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Default value: **10%**                                                                                                                                               |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Queue Size in a Thread Pool | thread_pool.bulk.queue_size                 | Queue size in the bulk thread pool. The value is an integer.                                                                                                         |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Default value: **200**                                                                                                                                               |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | thread_pool.write.queue_size                | Queue size in the write thread pool. The value is an integer.                                                                                                        |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Default value: **200**                                                                                                                                               |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      |                             | thread_pool.force_merge.size                | Queue size in the force merge thread pool. The value is an integer.                                                                                                  |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | Default value: **1**                                                                                                                                                 |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Customize                   | You can add parameters based on your needs. | Customized parameters                                                                                                                                                |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             | .. note::                                                                                                                                                            |
      |                             |                                             |                                                                                                                                                                      |
      |                             |                                             |    -  Enter multiple values in the format as **[value1, value2, value3...]**.                                                                                        |
      |                             |                                             |    -  Separate values by commas (,) and spaces.                                                                                                                      |
      |                             |                                             |    -  Colons (:) are not allowed.                                                                                                                                    |
      +-----------------------------+---------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **Submit**.

   In the displayed **Submit Configuration** dialog box, select the box indicating "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

   You can view the modification records on the displayed page. The system displays a maximum of 20 records.

   .. note::

      You need to restart the cluster after modification. If you do not restart the cluster after modifying the parameter configurations, **Configuration unupdated** is displayed in the **Task Status** column on the **Clusters** page.

      If you restart the cluster after the modification, **Task Status** displays **Configuration error**, the parameter configuration file fails to be modified.
