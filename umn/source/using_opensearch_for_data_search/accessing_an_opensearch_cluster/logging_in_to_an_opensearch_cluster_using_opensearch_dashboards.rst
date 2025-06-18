:original_name: css_01_0441.html

.. _css_01_0441:

Logging In to an OpenSearch Cluster Using OpenSearch Dashboards
===============================================================

OpenSearch Dashboards is the data visualization and exploration platform for OpenSearch. It enables in-depth data analysis and interactive visualization. In CSS, OpenSearch Dashboards is pre-built for each OpenSearch cluster. You can start OpenSearch Dashboards with one click, without installing anything. OpenSearch Dashboards offers a comprehensive suite of dashboard features and visualization tools. It seamlessly integrates Elasticsearch's analytical capabilities, supporting the full analytics process, from data exploration to actionable business insights.

OpenSearch Dashboards supports multiple access methods. Steps needed to log in to an OpenSearch cluster vary depending on the access method you choose. For details, see :ref:`Table 1 <css_01_0441__css_01_0382_table123121443185113>`.

.. _css_01_0441__css_01_0382_table123121443185113:

.. table:: **Table 1** Methods for logging In to an OpenSearch cluster through OpenSearch Dashboards

   +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Kibana Access Method                                               | Constraints                                                                                                                                                                                                                                                                                                                                                                                                       | Details                                                                                                                                                                     |
   +====================================================================+===================================================================================================================================================================================================================================================================================================================================================================================================================+=============================================================================================================================================================================+
   | One-click access to OpenSearch Dashboards from the service console | N/A                                                                                                                                                                                                                                                                                                                                                                                                               | :ref:`Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Through the Console <css_01_0441__css_01_0382_en-us_topic_0000001428595166_section3544291266>` |
   +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Accessing OpenSearch Dashboards using a public IP address          | -  Only clusters in security mode support OpenSearch Dashboards access through a public IP address.                                                                                                                                                                                                                                                                                                               | :ref:`Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Using a Public IP Address <css_01_0441__css_01_0382_section311713401714>`                      |
   |                                                                    | -  The whitelist that controls Kibana public network access depends on whitelist support by the ELB service. After you update the whitelist, the new settings take effect immediately for new connections. For existing persistent connections using the IP addresses that have been removed from the whitelist, the new settings take effect in approximately 1 minute after these connections are disconnected. |                                                                                                                                                                             |
   +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Accessing OpenSearch Dashboards using a private IP address         | Only servers in the same VPC as an OpenSearch cluster can access OpenSearch Dashboards using a private network address.                                                                                                                                                                                                                                                                                           | :ref:`Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Using a Private Network Address <css_01_0441__css_01_0382_section207611526916>`                |
   +--------------------------------------------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Constraints Concerning the Use of OpenSearch Dashboards
-------------------------------------------------------

You can customize the username, role name, and tenant name in OpenSearch Dashboards.

.. _css_01_0441__css_01_0382_en-us_topic_0000001428595166_section3544291266:

Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Through the Console
------------------------------------------------------------------------------------------

#. Log in to the CSS management console.
#. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column to go to the OpenSearch Dashboards login page.

   -  Non-security mode cluster: The OpenSearch Dashboards console is displayed.
   -  Security-mode cluster: Enter the username and password on the login page and click **Log In** to go to the OpenSearch Dashboards console. The default username is **admin** and the password is the administrator password you specified during cluster creation.

#. After logging in, you can perform operations on the **OpenSearch Dashboards** page to access the cluster.

.. _css_01_0441__css_01_0382_section311713401714:

Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Using a Public IP Address
------------------------------------------------------------------------------------------------

.. note::

   -  Only clusters in security mode support OpenSearch Dashboards access through a public IP address.
   -  The whitelist that controls Kibana public network access depends on whitelist support by the ELB service. After you update the whitelist, the new settings take effect immediately for new connections. For existing persistent connections using the IP addresses that have been removed from the whitelist, the new settings take effect in approximately 1 minute after these connections are disconnected.

   -  If you disable Kibana public network access and then re-enable it, the public IP address for accessing Kibana may change. Exercise caution.

#. Log in to the CSS management console.

#. Enable Kibana public network access for the OpenSearch cluster. You can do that either when creating an Elasticsearch cluster or afterwards.

   -  For how to enable Kibana public network access when creating an Elasticsearch cluster, see :ref:`Creating an OpenSearch Cluster <css_01_0275>`.
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

#. Enter the Kibana public IP address in the browser address box to go to the OpenSearch Dashboards login page.

   Enter the username and password on the login page and click **Log In** to log in to the OpenSearch Dashboards console. The default username is **admin** and the password is the administrator password you specified during cluster creation.

#. After the login is successful, you can access the OpenSearch cluster through OpenSearch Dashboards.

.. _css_01_0441__css_01_0382_section207611526916:

Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Using a Private Network Address
------------------------------------------------------------------------------------------------------

.. note::

   Only servers in the same VPC as an OpenSearch cluster can access OpenSearch Dashboards using a private network address.

#. Log in to the CSS management console.

#. On the OpenSearch **Clusters** page, click the name of a cluster. The **Cluster Information** page is displayed.

#. On the **Cluster Information** page, obtain the cluster's private network address.


   .. figure:: /_static/images/en-us_image_0000001992938337.png
      :alt: **Figure 1** Obtaining the private IP address

      **Figure 1** Obtaining the private IP address

#. Change the port number in the cluster's private network address from **9200** to **5601**, which becomes the private network address of OpenSearch Dashboards. For example, if the cluster's private network IPv4 address is **192.168.0.***:9200**, the private network address of OpenSearch Dashboards is **192.168.0.***:5601**.

#. On the server, enter the private network address of OpenSearch Dashboards to go to the OpenSearch Dashboards login page.

   -  Non-security mode cluster: The OpenSearch Dashboards console is displayed.
   -  Security-mode cluster: Enter the username and password on the login page and click **Log In** to go to the OpenSearch Dashboards console. The default username is **admin** and the password is the administrator password you specified during cluster creation.

#. After the login is successful, you can access the OpenSearch cluster through OpenSearch Dashboards.

Related Documents
-----------------

For routine O&M tasks (such as shard adjustment, index management, and performance monitoring), you are advised to use Cerebro for cluster login. For details, see :ref:`Logging In to an OpenSearch Cluster Through Cerebro <css_01_0442>`.
