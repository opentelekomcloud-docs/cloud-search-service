:original_name: en-us_topic_0000001640658701.html

.. _en-us_topic_0000001640658701:

Accessing a Cluster from a Kibana Public Network
================================================

For CSS clusters that have security mode enabled, you can enable Kibana public access. After the configuration is complete, an IP address will be provided to access Kibana of this cluster over the Internet.

You can configure Kibana public access during cluster creation, or after a cluster in security mode is created.

.. note::

   The whitelist for Kibana public network access depends on the ELB whitelist. After you updated the whitelist, the new settings take effect immediately for new connections. For existing persistent connections using the IP addresses that have been removed from the whitelist, the new settings take effect about 1 minute after these connections are stopped.

Configuring Kibana Public Access When Creating a Cluster
--------------------------------------------------------

#. Log in to the CSS management console.

#. Click **Create Cluster** in the upper right corner. The **Create Cluster** page is displayed.

#. On the **Create Cluster** page, enable **Security Mode**.

#. Set **Advanced Settings** to **Custom**, enable **Kibana Public Access**, and set parameters.

   .. table:: **Table 1** Kibana public access parameters

      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                    |
      +===================================+================================================================================================================================================================================================================================+
      | Bandwidth                         | Bandwidth for accessing Kibana with the public IP address                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                |
      |                                   | Value range: 1 to 100                                                                                                                                                                                                          |
      |                                   |                                                                                                                                                                                                                                |
      |                                   | Unit: Mbit/s                                                                                                                                                                                                                   |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Access Control                    | If you disable this function, all IP addresses can access Kibana through the public IP address. If you enable this function, only IP addresses or IP address in the whitelist can access Kibana through the public IP address. |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Whitelist                         | IP address or IP address range allowed to access a cluster. Use commas (,) to separate multiple addresses. This parameter can be configured only when **Access Control** is enabled.                                           |
      |                                   |                                                                                                                                                                                                                                |
      |                                   | You are advised to enable this function.                                                                                                                                                                                       |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   After the cluster is created, click the cluster name to go to the **Basic Information** page. On the **Kibana Public Access** page, you can view the Kibana public IP address.

Configuring Kibana Public Access for an Existing Cluster
--------------------------------------------------------

You can enable, disable, modify, and view Kibana public access for an existing cluster that has security mode enabled.

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters** > **OpenSearch**.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster.
#. Click the **Kibana Public Access** tab. Turn on the **Kibana Public Access** switch to enable the Kibana public access function.
#. On the displayed page, set parameters.

   .. table:: **Table 2** Kibana public access parameters

      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                    |
      +===================================+================================================================================================================================================================================================================================+
      | Bandwidth                         | Bandwidth for accessing Kibana with the public IP address                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                |
      |                                   | Value range: 1 to 100                                                                                                                                                                                                          |
      |                                   |                                                                                                                                                                                                                                |
      |                                   | Unit: Mbit/s                                                                                                                                                                                                                   |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Access Control                    | If you disable this function, all IP addresses can access Kibana through the public IP address. If you enable this function, only IP addresses or IP address in the whitelist can access Kibana through the public IP address. |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Whitelist                         | IP address or IP address range allowed to access a cluster. Use commas (,) to separate multiple addresses. This parameter can be configured only when **Access Control** is enabled.                                           |
      |                                   |                                                                                                                                                                                                                                |
      |                                   | You are advised to enable this function.                                                                                                                                                                                       |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. After you set the parameters, click **OK**.

Modifying Kibana Public Access
------------------------------

For clusters configured Kibana public access, you can modify its bandwidth and access control or disable this function.

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters** > **OpenSearch**.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster.
#. Click the **Kibana Public Access** tab to modify the Kibana public access configuration.

   -  Modifying bandwidth

      Click **Modify** on the right of **Bandwidth**. On the **Modify Bandwidth** page, modify the bandwidth and click **OK**.

   -  Modifying access control

      Click **Modify** on the right of **Access Control**. On the **Modify Access Control** page, set **Access Control** and **Whitelist**, and click **OK**.

   -  Disabling Kibana public access

      Toggle off the **Kibana Public Access** switch.

Accessing OpenSearch Dashboard with the Public IP Address
---------------------------------------------------------

After configuring Kibana public access, you will obtain a public IP address that you can use to access OpenSearch Dashboard of this cluster.

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters** > **OpenSearch**.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster.
#. Click the **Kibana Public Access** tab to obtain the Kibana public IP address.
#. Use this IP address to access OpenSearch Dashboard of this cluster through the Internet.
