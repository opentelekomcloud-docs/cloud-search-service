:original_name: css_01_0327.html

.. _css_01_0327:

Connecting to Cluster Through OpenSearch Dashboards
===================================================

OpenSearch Dashboards is the data visualization and exploration platform for OpenSearch. It enables in-depth data analysis and interactive visualization. In CSS, OpenSearch Dashboards is pre-built for each OpenSearch cluster. You can start OpenSearch Dashboards with one click, without installing anything. OpenSearch Dashboards offers a comprehensive suite of dashboard features and visualization tools. It seamlessly integrates OpenSearch's analytical capabilities, supporting the full analytics process from data exploration to actionable business insights.

OpenSearch Dashboards supports multiple access methods. Steps needed to log in to an OpenSearch cluster vary depending on the access method you choose. See :ref:`Table 1 <en-us_topic_0000001955726458__en-us_topic_0000001965497073_table123121443185113>`.

.. _en-us_topic_0000001955726458__en-us_topic_0000001965497073_table123121443185113:

.. table:: **Table 1** Methods for logging in to an OpenSearch cluster through OpenSearch Dashboards

   +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | OpenSearch Dashboards Access Method                                | Constraints                                                                                                           | Details                                                                                                                                                                                                       |
   +====================================================================+=======================================================================================================================+===============================================================================================================================================================================================================+
   | One-click access to OpenSearch Dashboards from the service console | N/A                                                                                                                   | :ref:`Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Through the Console <en-us_topic_0000001955726458__en-us_topic_0000001965497073_en-us_topic_0000001428595166_section3544291266>` |
   +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Accessing OpenSearch Dashboards using a public IP address          | -  Only clusters in security mode support OpenSearch Dashboards access through a public IP address.                   | :ref:`Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Using a Public IP Address <en-us_topic_0000001955726458__en-us_topic_0000001965497073_section311713401714>`                      |
   +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Accessing OpenSearch Dashboards using a private IP address         | The client that accesses OpenSearch Dashboards must be able to reach the private IP address of OpenSearch Dashboards. | :ref:`Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Using a Private Network Address <en-us_topic_0000001955726458__en-us_topic_0000001965497073_section207611526916>`                |
   +--------------------------------------------------------------------+-----------------------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Constraints Concerning the Use of OpenSearch Dashboards
-------------------------------------------------------

You can customize the username, role name, and tenant name in OpenSearch Dashboards.

.. _en-us_topic_0000001955726458__en-us_topic_0000001965497073_en-us_topic_0000001428595166_section3544291266:

Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Through the Console
------------------------------------------------------------------------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

   -  Non-security mode cluster: The OpenSearch Dashboards console is displayed.
   -  Security-mode cluster: Enter the username and password on the login page and click **Log In** to go to the OpenSearch Dashboards console. The default username is **admin** and the password is the one specified during cluster creation.

#. After logging in, you can use OpenSearch Dashboards to manage the cluster.

.. _en-us_topic_0000001955726458__en-us_topic_0000001965497073_section311713401714:

Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Using a Public IP Address
------------------------------------------------------------------------------------------------

.. warning::

   -  Only clusters in security mode support OpenSearch Dashboards access through a public IP address.

   -  The whitelist that controls OpenSearch Dashboards public network access depends on whitelist support by the ELB service. After you update the whitelist, the new settings take effect immediately for new connections. For existing persistent connections using the IP addresses that have been removed from the whitelist, the new settings take effect in approximately 1 minute after these connections are disconnected.
   -  If you disable OpenSearch Dashboards public network access and then re-enable it, the public IP address for accessing OpenSearch Dashboards may change. Exercise caution.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Cluster Access** > **Dashboards Public Network Access** to check whether OpenSearch Dashboards public network access is enabled for the cluster.

   -  Yes: Go to :ref:`6 <en-us_topic_0000001955726458__en-us_topic_0000001965497073_li2493238175917>`.
   -  No: Go to the next step.

#. Enable OpenSearch Dashboards public network access for the OpenSearch cluster.

   a. On the **Dashboards Public Network Access** page, toggle on the **Dashboards Public Network Access** button.
   b. In the displayed dialog box, set the parameters.

      .. table:: **Table 2** Configuring public network access for OpenSearch Dashboards

         +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
         +===================================+===================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
         | Bandwidth                         | Bandwidth for accessing OpenSearch Dashboards from the public network.                                                                                                                                                                                                                                                                                                                                                                                            |
         |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
         |                                   | Value range: 1 Mbit/s to 200 Mbit/s                                                                                                                                                                                                                                                                                                                                                                                                                               |
         +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Configure Whitelist               | Control OpenSearch Dashboards public network access using a whitelist.                                                                                                                                                                                                                                                                                                                                                                                            |
         |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
         |                                   | -  If a whitelist is configured, only IP addresses that are on this whitelist can access the cluster's OpenSearch Dashboards over the public network.                                                                                                                                                                                                                                                                                                             |
         |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
         |                                   |    Click **+ Add**. In the displayed text box, enter IP addresses or CIDR blocks that are allowed to access the cluster's OpenSearch Dashboards console from the public network. Separate them using commas (,). Each value must be unique. An example of valid values: **192.168.1.1,10.0.0.0/24**. Examples of invalid values: **0.0.0.0**, **xx.xx.xx.xx/0**, **172.16.0.0-172.16.255.255**, non-standard formats (e.g., **192.168.1**), and duplicate values. |
         |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
         |                                   | -  If no whitelist is configured, all public IP addresses can access the cluster's OpenSearch Dashboards console. However, this can be a security risk and should be avoided.                                                                                                                                                                                                                                                                                     |
         +-----------------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   c. Click **OK** to confirm the settings.

   If OpenSearch Dashboards public network access is already enabled, you can modify relevant settings.

#. .. _en-us_topic_0000001955726458__en-us_topic_0000001965497073_li2493238175917:

   After OpenSearch Dashboards public network access is enabled, obtain **Dashboards Public IP Address** on the **Dashboards Public Network Access** page.

#. Enter the OpenSearch Dashboards public IP address in the browser address box to go to the OpenSearch Dashboards login page.

   Enter the username and password on the login page and click **Log In** to log in to the OpenSearch Dashboards console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access the OpenSearch cluster through OpenSearch Dashboards.

.. _en-us_topic_0000001955726458__en-us_topic_0000001965497073_section207611526916:

Logging In to an OpenSearch Cluster by Accessing OpenSearch Dashboards Using a Private Network Address
------------------------------------------------------------------------------------------------------

.. caution::

   The client that accesses OpenSearch Dashboards must be able to reach the private IP address of OpenSearch Dashboards.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Click the **Overview** tab. In the **Network Information** area, record **Private IPv4 Address**.

#. Obtain the private IP address of OpenSearch Dashboards.

   By changing the port number in the cluster's private IP address from **9200** to **5601**, you get the private IP address of OpenSearch Dashboards. For example, if the cluster's private IPv4 address is **xx.xx.xx.xx:9200**, the private IP address of OpenSearch Dashboards is **xx.xx.xx.xx:5601**.

#. (Optional) Configure a return route. To enable a client to access the cluster's OpenSearch Dashboards console across different VPCs, configure a route for the OpenSearch cluster.

   a. Connect the client and OpenSearch Dashboards through a Direct Connect or VPC peering connection.

   b. Configure the route connecting the OpenSearch cluster and the client.

      On the **Overview** tab, find **Cluster Route** in the **Network Information** area, and click **Add Route** under it. In the displayed dialog box, set **IP Address** and **Subnet Mask**.

#. Access OpenSearch Dashboards.

   -  If the security mode is enabled for an OpenSearch cluster, the OpenSearch Dashboards access address is **https://{Dashboards private network address}**, for example, **https://xx.xx.xx.xx:5601**.
   -  If the security mode is disabled, the OpenSearch Dashboards access address is **http://{Dashboards private network address}**, for example, **http://xx.xx.xx.xx:5601**.

Configuring a Custom OpenSearch Dashboards Base Path
----------------------------------------------------

For multi-cluster management, the default root path access method of OpenSearch Dashboards may not meet security authentication and request verification requirements. CSS allows you to configure a custom Base Path for OpenSearch Dashboards through the console. This allows you to set a dedicated access path for each cluster to implement fine-grained access control, simplify multi-cluster management, and improve overall system security.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Cluster Settings** > **Parameter Settings** > **Dashboards**.

#. Click **Edit**, and set the parameters.

   .. table:: **Table 3** Configuring Base Path

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                                                                                                             |
      +===================================+=========================================================================================================================================================================================================================================================================================================================================================+
      | server.basePath                   | Custom value for Base Path.                                                                                                                                                                                                                                                                                                                             |
      |                                   |                                                                                                                                                                                                                                                                                                                                                         |
      |                                   | When you need to access OpenSearch Dashboards through a reverse proxy (such as Nginx), this value is appended to the proxy address as a subpath. For example, if the reverse proxy address is **http://example.com** and **server.basePath** is set to **/test**, you can access OpenSearch Dashboards through the address **http://example.com/test**. |
      |                                   |                                                                                                                                                                                                                                                                                                                                                         |
      |                                   | The value:                                                                                                                                                                                                                                                                                                                                              |
      |                                   |                                                                                                                                                                                                                                                                                                                                                         |
      |                                   | -  Must start with **/**.                                                                                                                                                                                                                                                                                                                               |
      |                                   | -  Must not contain consecutive slashes (for example, **//**).                                                                                                                                                                                                                                                                                          |
      |                                   | -  Can only contain letters, digits, hyphens (**-**), underscores (**\_**), periods (**.**), and slashes (**/**).                                                                                                                                                                                                                                       |
      |                                   | -  Can contain multi-level paths, but its length cannot exceed 254 characters.                                                                                                                                                                                                                                                                          |
      |                                   | -  Must not end with a slash (/).                                                                                                                                                                                                                                                                                                                       |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | server.rewriteBasePath            | Whether OpenSearch Dashboards or a reverse proxy will remove the server.basePath prefix from the request path.                                                                                                                                                                                                                                          |
      |                                   |                                                                                                                                                                                                                                                                                                                                                         |
      |                                   | This parameter is optional. If no reverse proxy is used, ignore this parameter.                                                                                                                                                                                                                                                                         |
      |                                   |                                                                                                                                                                                                                                                                                                                                                         |
      |                                   | The value can be:                                                                                                                                                                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                                                                                                                         |
      |                                   | -  **true**: OpenSearch Dashboards will automatically remove the server.basePath prefix from the request path.                                                                                                                                                                                                                                          |
      |                                   | -  **false** (default): The reverse proxy (such as Nginx) will remove the server.basePath prefix from the request path. In this case, you can only access OpenSearch Dashboards through the reverse proxy.                                                                                                                                              |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. After the change is complete, click **Save**. In the displayed dialog box, confirm the settings, and select "Modifying Dashboards settings will restart Dashboards, making it temporarily inaccessible." Then click **OK**.

   If **Job Status** is **Succeeded** in the parameter settings task list below, the change is successful. Up to 1000 modification records can be displayed.

#. Access OpenSearch Dashboards.

   -  Access OpenSearch Dashboards through the **Dashboards private network address**.

      -  When the security mode is enabled for the OpenSearch cluster, and **server.rewriteBasePath** is **true**, the internal and external addresses of OpenSearch Dashboards are **https://{Dashboards private network address}{server.basePath}**, for example, **https://xx.xx.xx.xx:5601/test**.
      -  When the security mode is enabled for the OpenSearch cluster, and **server.rewriteBasePath** is **false**, OpenSearch Dashboards can only be accessed through a reverse proxy.
      -  When the security mode is disabled for the OpenSearch cluster, and **server.rewriteBasePath** is **true**, OpenSearch Dashboards can only be accessed from the internal network, and its address is **http://{Dashboards private network address}{server.basePath}**, for example, **http://xx.xx.xx.xx:5601/test**.
      -  When the security mode is disabled for the OpenSearch cluster, and **server.rewriteBasePath** is **false**, OpenSearch Dashboards can only be accessed through a reverse proxy.

   -  Access OpenSearch Dashboards through the **Dashboards public network address** (when Dashboards public network access is enabled).

      -  When **server.rewriteBasePath** is set to **true**, the public network address of OpenSearch Dashboards is **https://{Dashboards public network address}{server.basePath}**, for example, **https://xx.xx.xx.xx:5601/test**.
      -  When **server.rewriteBasePath** is set to **false**, OpenSearch Dashboards can only be accessed through a reverse proxy.

   -  Access OpenSearch Dashboards through the **reverse proxy server address**.

      The OpenSearch Dashboards address is **http://{reverse proxy server address}{server.basePath}**, for example, **http://xx.xx.xx.xx:port/test**. Support for public network access depends on whether the reverse proxy server uses a public IP address. This solution depends on the reverse proxy server configuration..
