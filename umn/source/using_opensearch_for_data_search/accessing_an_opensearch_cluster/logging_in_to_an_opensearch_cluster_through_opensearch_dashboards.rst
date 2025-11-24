:original_name: css_01_0327.html

.. _css_01_0327:

Logging In to an OpenSearch Cluster Through OpenSearch Dashboards
=================================================================

OpenSearch Dashboards is the data visualization and exploration platform for OpenSearch. It enables in-depth data analysis and interactive visualization. In CSS, OpenSearch Dashboards is pre-built for each OpenSearch cluster. You can start OpenSearch Dashboards with one click, without installing anything. OpenSearch Dashboards offers a comprehensive suite of dashboard features and visualization tools. It seamlessly integrates OpenSearch's analytical capabilities, supporting the full analytics process from data exploration to actionable business insights.

OpenSearch Dashboards supports multiple access methods. Steps needed to log in to an OpenSearch cluster vary depending on the access method you choose. See :ref:`Table 1 <en-us_topic_0000001955726458__en-us_topic_0000001965497073_table123121443185113>`.

.. _en-us_topic_0000001955726458__en-us_topic_0000001965497073_table123121443185113:

.. table:: **Table 1** Methods for logging In to an OpenSearch cluster through OpenSearch Dashboards

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

#. Click the **Overview** tab. In the **Configuration** area, record **Private IPv4 Address**.

#. Obtain the private IP address of OpenSearch Dashboards.

   By changing the port number in the cluster's private IP address from **9200** to **5601**, you get the private IP address of OpenSearch Dashboards. For example, if the cluster's private IPv4 address is **192.168.0.***:9200**, the private IP address of OpenSearch Dashboards is **192.168.0.***:5601**.

#. (Optional) Configure a return route. To enable a client to access the cluster's OpenSearch Dashboards console across different VPCs, configure a route for the OpenSearch cluster.

   a. Connect the client and OpenSearch Dashboards through a Direct Connect or VPC peering connection.

   b. Configure the route connecting the OpenSearch cluster and the client.

      On the **Cluster Information** page, find **Cluster Route**, and click **Add Route** on the right. In the displayed dialog box, set **IP Address** and **Subnet Mask**.

   For details, see :ref:`Configuring Routes for an OpenSearch Cluster <css_01_0280>`.

#. On the client, enter the private network address of OpenSearch Dashboards (for example, **https://192.168.0.xx:5601**) to go to the OpenSearch Dashboards login page.

   -  Non-security mode cluster: The OpenSearch Dashboards console is displayed.
   -  Security-mode cluster: Enter the username and password on the login page and click **Log In** to go to the OpenSearch Dashboards console. The default username is **admin** and the password is the one specified during cluster creation.

#. After the login is successful, you can access the OpenSearch cluster through OpenSearch Dashboards.
