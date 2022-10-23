:original_name: css_01_0088.html

.. _css_01_0088:

Kibana Public Access
====================

For CSS clusters that have security mode enabled, you can access Kibana through the Internet after configuring Kibana public access. For a cluster that has security mode enabled, CSS allows you to enable Kibana public access and configure access bandwidth. After the configuration is complete, the cluster obtains a Kibana public IP address that you can use to access Kibana of this cluster.

You can configure Kibana public access when creating a cluster or configure this function after enabling security mode for a cluster.

.. note::

   Clusters purchased before rollout of this feature do not support this function.

Configuring Kibana Public Access When Creating a Cluster
--------------------------------------------------------

#. Log in to the CSS management console.

#. Click **Create Cluster** in the upper right corner. The **Create Cluster** page is displayed.

#. On the **Create Cluster** page, enable **Security Mode**.

   You can enable **Security Mode** for clusters of version 6.5.4 and later versions.

#. Set **Advanced Settings** to **Custom**, enable **Kibana Public Access**, and set parameters.

   .. table:: **Table 1** Kibana public access parameters

      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                     |
      +===================================+=================================================================================================================================================================================================================================================+
      | Bandwidth                         | Bandwidth for accessing Kibana with the public IP address                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                 |
      |                                   | Value range: 1 to 100                                                                                                                                                                                                                           |
      |                                   |                                                                                                                                                                                                                                                 |
      |                                   | Unit: Mbit/s                                                                                                                                                                                                                                    |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Access Control                    | If you disable this function, any IP addresses can access the cluster through the public IP address. If you enable this function, only IP addresses or IP address ranges in the whitelist can access the cluster through the public IP address. |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Whitelist                         | IP address or IP address range allowed to access a cluster. Use commas (,) to separate multiple addresses.                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                                 |
      |                                   | You are advised to enable this function.                                                                                                                                                                                                        |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   After the cluster is created, click the cluster name to go to the **Basic Information** page. On the **Kibana Public Access** page, you can view the Kibana public IP address.

Configuring Kibana Public Access for an Existing Cluster
--------------------------------------------------------

You can enable, disable, modify, and view Kibana public access for an existing cluster that has security mode enabled.

#. Log in to the CSS management console.

#. On the **Clusters** page, click the name of the target cluster.

#. Click the **Kibana Public Access** tab. Turn on the **Kibana Public Access** switch to enable the Kibana public access function.

   |image1| indicates that Kibana public access is disabled. |image2| indicates that Kibana public access is enabled.

#. On the displayed page, set parameters.

   .. table:: **Table 2** Kibana public access parameters

      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                     |
      +===================================+=================================================================================================================================================================================================================================================+
      | Bandwidth                         | Bandwidth for accessing Kibana with the public IP address                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                 |
      |                                   | Value range: 1 to 100                                                                                                                                                                                                                           |
      |                                   |                                                                                                                                                                                                                                                 |
      |                                   | Unit: Mbit/s                                                                                                                                                                                                                                    |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Access Control                    | If you disable this function, any IP addresses can access the cluster through the public IP address. If you enable this function, only IP addresses or IP address ranges in the whitelist can access the cluster through the public IP address. |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Whitelist                         | IP address or IP address range allowed to access a cluster. Use commas (,) to separate multiple addresses.                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                                 |
      |                                   | You are advised to enable this function.                                                                                                                                                                                                        |
      +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. After you set the parameters, click **OK**.

Modifying Kibana Public Access
------------------------------

CSS allows you to modify bandwidth and access control of clusters configured with Kibana public access.

#. Log in to the CSS management console.
#. On the **Clusters** page, click the name of the target cluster.
#. Click the **Kibana Public Access** tab and modify the Kibana public access parameters.

   -  Modifying bandwidth

      Click **Modify** on the right of **Bandwidth**. On the **Modify Bandwidth** page, modify the bandwidth and click **OK**.

   -  Modifying access control

      Click **Modify** on the right of **Access Control**. On the **Modify Access Control** page, set **Access Control** and **Whitelist**, and click **OK**.

Accessing Kibana with the Public IP Address
-------------------------------------------

After configuring Kibana public access, you will obtain a public IP address that you can use to access Kibana of this cluster.

#. Log in to the CSS management console.
#. On the **Clusters** page, click the name of the target cluster.
#. Click the **Kibana Public Access** tab to obtain the Kibana public IP address.
#. Use this IP address to access Kibana of this cluster through the Internet.

.. |image1| image:: /_static/images/en-us_image_0000001286116734.png
.. |image2| image:: /_static/images/en-us_image_0000001338836489.png
