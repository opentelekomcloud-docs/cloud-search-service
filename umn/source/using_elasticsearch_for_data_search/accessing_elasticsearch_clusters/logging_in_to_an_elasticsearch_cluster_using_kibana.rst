:original_name: css_01_0382.html

.. _css_01_0382:

Logging In to an Elasticsearch Cluster Using Kibana
===================================================

Kibana is the official data visualization and exploration platform for Elasticsearch. It enables in-depth data analysis and interactive visualization. In CSS, Kibana is pre-built for each Elasticsearch cluster. You can start Kibana with one click, without installing anything. Kibana offers a comprehensive suite of dashboard features and visualization tools. It seamlessly integrates Elasticsearch's analytical capabilities, supporting the full analytics process, from data exploration to actionable business insights.

CSS's Kibana supports multiple access methods. Steps needed to log in to an Elasticsearch cluster vary depending on the access method you choose. For details, see :ref:`Table 1 <css_01_0382__table123121443185113>`.

.. _css_01_0382__table123121443185113:

.. table:: **Table 1** Methods for logging in to an Elasticsearch cluster through Kibana

   +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Kibana Access Method                                | Constraints                                                                                                                                                                                                                                                                                                                                                                                                       | Details                                                                                                                                             |
   +=====================================================+===================================================================================================================================================================================================================================================================================================================================================================================================================+=====================================================================================================================================================+
   | One-click access to Kibana from the service console | N/A                                                                                                                                                                                                                                                                                                                                                                                                               | :ref:`Logging In to an Elasticsearch Cluster by Accessing Kibana Through the Console <css_01_0382__en-us_topic_0000001428595166_section3544291266>` |
   +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Accessing Kibana using a public IP address          | -  Only clusters in security mode support Kibana access through a public IP address.                                                                                                                                                                                                                                                                                                                              | :ref:`Logging In to an Elasticsearch Cluster by Accessing Kibana Using a Public IP Address <css_01_0382__section311713401714>`                      |
   |                                                     | -  Kibana public network access cannot be enabled for Elasticsearch security-mode clusters created before June 2020, that is, when the feature first became available.                                                                                                                                                                                                                                            |                                                                                                                                                     |
   |                                                     | -  The whitelist that controls Kibana public network access depends on whitelist support by the ELB service. After you update the whitelist, the new settings take effect immediately for new connections. For existing persistent connections using the IP addresses that have been removed from the whitelist, the new settings take effect in approximately 1 minute after these connections are disconnected. |                                                                                                                                                     |
   +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+
   | Accessing Kibana using a private network address    | Only servers in the same VPC can access Kibana using a private network address of the Elasticsearch cluster.                                                                                                                                                                                                                                                                                                      | :ref:`Logging In to an Elasticsearch Cluster by Accessing Kibana Using a Private Network Address <css_01_0382__section207611526916>`                |
   +-----------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------+

Constraints on Kibana Usage
---------------------------

-  You can customize the username, role name, and tenant name in Kibana.

.. _css_01_0382__en-us_topic_0000001428595166_section3544291266:

Logging In to an Elasticsearch Cluster by Accessing Kibana Through the Console
------------------------------------------------------------------------------

#. Log in to the CSS management console.
#. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column to go to the Kibana login page.

   -  Non-security cluster: The Kibana console is displayed without asking for a username and password.
   -  Security cluster: Enter the username and password on the login page and click **Log In** to log in to the Kibana console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access clusters through Kibana.

.. _css_01_0382__section311713401714:

Logging In to an Elasticsearch Cluster by Accessing Kibana Using a Public IP Address
------------------------------------------------------------------------------------

.. note::

   -  Only clusters in security mode support Kibana access through a public IP address.
   -  Kibana public network access cannot be enabled for Elasticsearch security-mode clusters created before June 2020, that is, when the feature first became available.
   -  The whitelist that controls Kibana public network access depends on whitelist support by the ELB service. After you update the whitelist, the new settings take effect immediately for new connections. For existing persistent connections using the IP addresses that have been removed from the whitelist, the new settings take effect in approximately 1 minute after these connections are disconnected.

   -  If you disable Kibana public network access and then re-enable it, the public IP address for accessing Kibana may change. Exercise caution.

#. Log in to the CSS management console.

#. Enable Kibana public network access for the Elasticsearch cluster. You can do that either when creating an Elasticsearch cluster or afterwards.

   -  For how to enable Kibana public network access when creating an Elasticsearch cluster, see :ref:`Creating an Elasticsearch Cluster <css_01_0380>`.
   -  To enable public network access for Kibana for an existing cluster, perform the following steps:

      a. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster.
      b. Click the **Kibana Public Access** tab, and enable **Kibana Public Access**.
      c. On the displayed page, set parameters. If Kibana public network access is already enabled, you can modify relevant settings.

         .. table:: **Table 2** Configuring public network access for Kibana

            +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
            | Parameter                         | Description                                                                                                                                                                                                                                                                                                                                                                                                       |
            +===================================+===================================================================================================================================================================================================================================================================================================================================================================================================================+
            | Bandwidth                         | Bandwidth for accessing Kibana through a public IP address                                                                                                                                                                                                                                                                                                                                                        |
            |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
            |                                   | Value range: 1 to 100.                                                                                                                                                                                                                                                                                                                                                                                            |
            |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
            |                                   | Unit: Mbit/s                                                                                                                                                                                                                                                                                                                                                                                                      |
            +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
            | Access Control                    | If you disable this function, all IP addresses can access Kibana through the public IP address. If you enable this function, only IP addresses or IP address ranges in the whitelist can access Kibana through the public IP address.                                                                                                                                                                             |
            +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
            | Whitelist                         | IP addresses or IP address ranges allowed to access the cluster. Use commas (,) to separate multiple IP addresses or ranges. This parameter can be configured only when **Access Control** is enabled.                                                                                                                                                                                                            |
            |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
            |                                   | You are advised to enable the whitelist.                                                                                                                                                                                                                                                                                                                                                                          |
            |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
            |                                   | .. note::                                                                                                                                                                                                                                                                                                                                                                                                         |
            |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                   |
            |                                   |    The whitelist that controls Kibana public network access depends on whitelist support by the ELB service. After you update the whitelist, the new settings take effect immediately for new connections. For existing persistent connections using the IP addresses that have been removed from the whitelist, the new settings take effect in approximately 1 minute after these connections are disconnected. |
            +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

      d. Click **OK**.

#. After Kibana public network access is enabled, obtain the Kibana public IP address on the **Kibana Public Access** page.

#. Enter the public IP address for Kibana in the browser address box to go to the Kibana login page.

   Enter the username and password on the login page and click **Log In** to log in to the Kibana console. The default username is **admin** and the password is the administrator password you specified during cluster creation.

#. After the login is successful, you can access the Elasticsearch cluster through Kibana.

.. _css_01_0382__section207611526916:

Logging In to an Elasticsearch Cluster by Accessing Kibana Using a Private Network Address
------------------------------------------------------------------------------------------

.. note::

   Only servers in the same VPC can access Kibana using a private network address of the Elasticsearch cluster.

#. Log in to the CSS management console.

#. On the **Clusters** page, click the name of a cluster. The **Cluster Information** page is displayed.

#. On the **Cluster Information** page, obtain the cluster's private network address.


   .. figure:: /_static/images/en-us_image_0000001975979129.png
      :alt: **Figure 1** Obtaining the private IP address

      **Figure 1** Obtaining the private IP address

#. Change the port number in the cluster's private network address from **9200** to **5601**, which becomes the private network address of Kibana. For example, if the cluster's private network IPv4 address is **192.168.0.***:9200**, the private network address of Kibana is **192.168.0.***:5601**.

#. On the server, enter the private network address of Kibana to go to the Kibana login page.

   -  Non-security cluster: The Kibana console is displayed without asking for a username and password.
   -  Security cluster: Enter the username and password on the login page and click **Log In** to log in to the Kibana console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access the Elasticsearch cluster through Kibana.

More: Configuring a Custom Kibana Base Path for Public Network Access
---------------------------------------------------------------------

With Elasticsearch 7.10.2, you can configure a custom Base Path for Kibana access after Kibana public network access is enabled. Or you can use the default Kibana Base Path instead.

.. important::

   -  This feature is available for Elasticsearch 7.10.2 clusters (the image version is no earlier than 7.10.2_24.3.3_x.x.x) for which Kibana public network access is enabled.
   -  Only the cluster administrator **admin** under Global Tenant has the permission to configure a custom Kibana Base Path, which applies globally.

#. Log in to the CSS management console.

#. Choose **Clusters** > **Elasticsearch** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. Log in to Kibana using an administrator account.

   -  Username: **admin** (default administrator account)
   -  Password: Enter the administrator password you set when creating the cluster in security mode.

#. After a successful login, choose **Stack Management** in the left navigation pane of the Kibana console.

#. Choose **Advanced Settings** on the left of the **Stack Management** page.

#. On the **Settings** page, set **Base Path Alias**. The value must start with a slash (/) and must not end with one. A multi-layer path is allowed, but its length cannot exceed 255 characters.


   .. figure:: /_static/images/en-us_image_0000002120318316.png
      :alt: **Figure 2** Custom Base Path

      **Figure 2** Custom Base Path

#. Click **Save changes**. The saved changes take effect in approximately 10 seconds.

#. Access Kibana using the Kibana public network address plus *Base Path Alias*.

   For example, if the Kibana public network address of the Elasticsearch cluster is **https://xx.xx.xx.xx:5601** and the configured **Base Path Alias** is **/test**, you can access Kibana via **https://xx.xx.xx.xx:5601/test** from the public network.

Related Documents
-----------------

-  For details about how to use in-house developed Kibana to access Elasticsearch clusters in CSS, see
-  For routine O&M tasks (such as shard adjustment, index management, and performance monitoring), you are advised to use Cerebro for cluster login. For details, see :ref:`Logging In to an Elasticsearch Cluster Through Cerebro <css_01_0383>`.
