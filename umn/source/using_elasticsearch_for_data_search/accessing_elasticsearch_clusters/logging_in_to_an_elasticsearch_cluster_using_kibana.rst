:original_name: css_01_0108.html

.. _css_01_0108:

Logging In to an Elasticsearch Cluster Using Kibana
===================================================

Kibana is the official data visualization and exploration platform for Elasticsearch. It enables in-depth data analysis and interactive visualization. In CSS, Kibana is pre-built for each Elasticsearch cluster. You can start Kibana in one click, without installing anything. Kibana offers a comprehensive suite of dashboard features and visualization tools. It seamlessly integrates Elasticsearch's analytical capabilities, supporting the full analytics process from data exploration to actionable business insights.

CSS's Kibana supports multiple access methods. Steps needed to log in to an Elasticsearch cluster vary depending on the access method you choose. See :ref:`Table 1 <en-us_topic_0000001965497073__table123121443185113>`.

.. _en-us_topic_0000001965497073__table123121443185113:

.. table:: **Table 1** Methods for logging in to an Elasticsearch cluster through Kibana

   +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Kibana Access Method                                | Constraints                                                                                                                                                            | Details                                                                                                                                                              |
   +=====================================================+========================================================================================================================================================================+======================================================================================================================================================================+
   | One-click access to Kibana from the service console | N/A                                                                                                                                                                    | :ref:`Logging In to an Elasticsearch Cluster by Accessing Kibana Through the Console <en-us_topic_0000001965497073__en-us_topic_0000001428595166_section3544291266>` |
   +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Accessing Kibana using a public IP address          | -  Only clusters in security mode support Kibana access through a public IP address.                                                                                   | :ref:`Logging In to an Elasticsearch Cluster by Accessing Kibana Using a Public IP Address <en-us_topic_0000001965497073__section311713401714>`                      |
   |                                                     | -  Kibana public network access cannot be enabled for Elasticsearch security-mode clusters created before June 2020, that is, when the feature first became available. |                                                                                                                                                                      |
   +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Accessing Kibana using a private network address    | The client that accesses Kibana must be able to reach Kibana's private IP address.                                                                                     | :ref:`Logging In to an Elasticsearch Cluster by Accessing Kibana Using a Private Network Address <en-us_topic_0000001965497073__section207611526916>`                |
   +-----------------------------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Constraints on Kibana Usage
---------------------------

-  You can customize the username, role name, and tenant name in Kibana.

.. _en-us_topic_0000001965497073__en-us_topic_0000001428595166_section3544291266:

Logging In to an Elasticsearch Cluster by Accessing Kibana Through the Console
------------------------------------------------------------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.
#. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console.

   -  Non-security cluster: The Kibana console is displayed without asking for a username and password.
   -  Security cluster: Enter the username and password on the login page and click **Log In** to log in to the Kibana console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access the cluster through Kibana.

.. _en-us_topic_0000001965497073__section311713401714:

Logging In to an Elasticsearch Cluster by Accessing Kibana Using a Public IP Address
------------------------------------------------------------------------------------

.. warning::

   -  Only clusters in security mode support Kibana access through a public IP address.
   -  Kibana public network access cannot be enabled for Elasticsearch security-mode clusters created before June 2020, that is, when the feature first became available.

   -  The whitelist that controls Kibana public network access depends on whitelist support by the ELB service. After you update the whitelist, the new settings take effect immediately for new connections. For existing persistent connections using the IP addresses that have been removed from the whitelist, the new settings take effect in approximately 1 minute after these connections are disconnected.
   -  If you disable Kibana public network access and then re-enable it, the public IP address for accessing Kibana may change. Exercise caution.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Cluster Access** > **Kibana Public Network Access** to check whether Kibana public network access is enabled for the cluster.

   -  Yes: Go to :ref:`6 <en-us_topic_0000001965497073__li2493238175917>`.
   -  No: Go to the next step.

#. Enable Kibana public network access for the Elasticsearch cluster.

   a. On the **Kibana Public Network Access** page, toggle on the **Kibana Public Network Access** button.
   b. In the displayed **Kibana Public Network Access** dialog box, set the parameters.

      .. table:: **Table 2** Configuring public network access for Kibana

         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                        |
         +===================================+====================================================================================================================================================================================================================================================================================================================================================================================================================================================+
         | Bandwidth                         | Bandwidth for accessing Kibana from the public network                                                                                                                                                                                                                                                                                                                                                                                             |
         |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
         |                                   | Value range: 1 Mbit/s to 200 Mbit/s                                                                                                                                                                                                                                                                                                                                                                                                                |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Configure Whitelist               | Control Kibana public network access using a whitelist.                                                                                                                                                                                                                                                                                                                                                                                            |
         |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
         |                                   | -  If a whitelist is configured, only IP addresses that are on this whitelist can access the cluster's Kibana console over the public network.                                                                                                                                                                                                                                                                                                     |
         |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
         |                                   |    Click **+ Add**. In the displayed text box, enter IP addresses or CIDR blocks that are allowed to access the cluster's Kibana console from the public network. Separate them using commas (,). Each value must be unique. An example of valid values: **192.168.1.1,10.0.0.0/24**. Examples of invalid values: **0.0.0.0**, **xx.xx.xx.xx/0**, **172.16.0.0-172.16.255.255**, non-standard formats (e.g., **192.168.1**), and duplicate values. |
         |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
         |                                   | -  If no whitelist is configured, all public IP addresses can access the cluster's Kibana console. However, this can be a security risk and should be avoided.                                                                                                                                                                                                                                                                                     |
         +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   c. Click **OK** to confirm the settings.

   If Kibana public network access is already enabled, you can modify relevant settings.

#. .. _en-us_topic_0000001965497073__li2493238175917:

   After Kibana public network access is enabled, obtain the Kibana public IP address on the **Kibana Public Network Access** page.

#. Enter the public IP address for Kibana in the browser address box to go to the Kibana login page.

   Enter the username and password on the login page and click **Log In** to log in to the Kibana console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access the Elasticsearch cluster through Kibana.

.. _en-us_topic_0000001965497073__section207611526916:

Logging In to an Elasticsearch Cluster by Accessing Kibana Using a Private Network Address
------------------------------------------------------------------------------------------

.. caution::

   The client that accesses Kibana must be able to reach Kibana's private IP address.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Click the **Overview** tab. In the **Configuration** area, record **Private IPv4 Address**.

#. Obtain Kibana's private IP address.

   By changing the port number in the cluster's private IP address from **9200** to **5601**, you get Kibana's private IP address. For example, if the cluster's private IPv4 address is **192.168.0.xx:9200**, the private IP address of Kibana is **192.168.0.xx:5601**.

#. (Optional) Configure a return route. To enable a client to access the cluster's Kibana console across different VPCs, configure a route for the Elasticsearch cluster.

   a. Connect the client and Kibana through a Direct Connect or VPC peering connection.

   b. Configure the route connecting the Elasticsearch cluster and the client.

      On the **Cluster Information** page, find **Cluster Route**, and click **Add Route** on the right. In the displayed dialog box, set **IP Address** and **Subnet Mask**.

   For details, see :ref:`Configuring Routes for an Elasticsearch Cluster <css_01_0279>`.

#. On the client, enter the private network address of Kibana (for example, **https://192.168.0.xx:5601**) to go to the Kibana login page.

   -  Non-security cluster: The Kibana console is displayed without asking for a username and password.
   -  Security cluster: Enter the username and password on the login page and click **Log In** to log in to the Kibana console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access the Elasticsearch cluster through Kibana.

More: Configuring a Custom Kibana Base Path for Public Network Access
---------------------------------------------------------------------

With Elasticsearch 7.10.2, you can configure a custom Base Path for Kibana access after Kibana public network access is enabled. Or you can use the default Kibana Base Path instead.

.. warning::

   -  This feature is available for Elasticsearch 7.10.2 clusters (the image version is no earlier than 7.10.2_24.3.3_x.x.x) for which Kibana public network access is enabled.
   -  Only the cluster administrator **admin** under Global Tenant has the permission to configure a custom Kibana Base Path, which applies globally.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, find the target cluster, and click **Kibana** in the **Operation** column to log in to the Kibana console using the administrator account.

   -  Username: **admin** (default administrator account)
   -  Password: Enter the administrator password you set when creating the cluster in security mode.

#. After a successful login, choose **Stack Management** in the left navigation pane of the Kibana console.

#. Choose **Advanced Settings** on the left of the **Stack Management** page.

#. On the **Settings** page, set **Base Path Alias**. The value must start with a slash (/) and must not end with one. A multi-layer path is allowed, but its length cannot exceed 255 characters.


   .. figure:: /_static/images/en-us_image_0000002120318316.png
      :alt: **Figure 1** Custom Base Path

      **Figure 1** Custom Base Path

#. Click **Save changes**. The saved changes take effect in approximately 10 seconds.

#. Access Kibana using the Kibana public network address plus *Base Path Alias*.

   For example, if the Kibana public network address of the Elasticsearch cluster is **https://xx.xx.xx.xx:5601** and the configured **Base Path Alias** is **/test**, you can access Kibana via **https://xx.xx.xx.xx:5601/test** from the public network.
