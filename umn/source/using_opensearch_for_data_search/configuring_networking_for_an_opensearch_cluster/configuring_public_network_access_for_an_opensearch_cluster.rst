:original_name: css_01_0290.html

.. _css_01_0290:

Configuring Public Network Access for an OpenSearch Cluster
===========================================================

When public network access is enabled for an OpenSearch cluster, the cluster is automatically assigned a public IP address with dedicated dynamic BGP bandwidth, making it accessible from the Internet via HTTPS. You can configure access control from the public network by IP addresses or IP address ranges.

When enabling public network access for an OpenSearch cluster, a shared load balancer is typically used for load balancing. If your workloads require quicker access, you are advised to use a dedicated load balancer to connect your cluster. For details, see :ref:`Configuring a Dedicated Load Balancer for an OpenSearch Cluster <css_01_0182>`.

Constraints
-----------

-  Enabling public network access for a CSS cluster may incur fees, as it will need to use EIP and bandwidth resources.
-  To enable public network access for an OpenSearch cluster, two conditions must be met: the security mode and HTTPS access are both enabled.
-  Public network access and the VPC Endpoint service share a load balancer. If you configure a whitelist for public network access, this whitelist is deployed to the shared load balancer. As such, it will control access not only from the public network but also from private IP addresses through VPCEP. In this case, you need to add IP address **198.19.128.0/17** to the public network access whitelist to allow traffic through VPCEP.

Enabling Public Network Access
------------------------------

To enable public network access for an existing cluster, perform the following steps:

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. On the **Overview** tab, check whether **Security Mode** and **HTTPS Access** are enabled in the **Configuration** area.

   -  If they are enabled, go to the next step to enable public network access.
   -  If either one is disabled, public network access cannot be enabled for the cluster.

#. Click **Enable** next to **Public Network Access**. In the displayed dialog box, configure the necessary settings.

   .. table:: **Table 1** Enabling public network access

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                      |
      +===================================+==================================================================================================================================================================================================================================================================================================================================================================================================================================+
      | Bandwidth                         | Cluster bandwidth for public network access.                                                                                                                                                                                                                                                                                                                                                                                     |
      |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      |                                   | Value range: 1 Mbit/s to 200 Mbit/s                                                                                                                                                                                                                                                                                                                                                                                              |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Configure Whitelist               | Control public network access to the cluster using a whitelist.                                                                                                                                                                                                                                                                                                                                                                  |
      |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      |                                   | -  If a whitelist is configured, only IP addresses that are on this whitelist can access the cluster over the public network.                                                                                                                                                                                                                                                                                                    |
      |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      |                                   |    Click **+Add**. In the displayed text box, enter IP addresses or CIDR blocks that are allowed to access the cluster from the public network. Separate them using commas (,). Each value must be unique. An example of valid values: **192.168.1.1,10.0.0.0/24**. Examples of invalid values: **0.0.0.0**, **xx.xx.xx.xx/0**, **172.16.0.0-172.16.255.255**, non-standard formats (e.g., **192.168.1**), and duplicate values. |
      |                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                  |
      |                                   | -  If no whitelist is configured, all public IP addresses can access the cluster. However, this can be a security risk and should be avoided.                                                                                                                                                                                                                                                                                    |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **OK** to enable public network access.

   After public network access is enabled, the public IP address, public network access control, and bandwidth information is displayed.

Managing Public Network Access
------------------------------

When public network access is enabled, you can check the public IP address, and modify the bandwidth and access control settings.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. On the **Overview** tab, manage public network access settings in the **Configuration** area.

   -  **Checking the public IP address**

      Record the IP address and port number displayed next to **Public Network Access**.

   -  **Modifying public network access control settings**

      Click **Modify** next to **Public Network Access Control**. In the displayed dialog box, add or remove IP addresses or CIDR blocks to or from the whitelist. Click **OK** to save the change.

   -  **Modifying public network bandwidth**

      Click **Modify** next to **Bandwidth**. In the displayed dialog box, change the bandwidth. Click **OK** to save the change.

Disabling Public Network Access
-------------------------------

If public network access is no longer required for a cluster, disable it to release resources.

.. warning::

   After the public IP address is disassociated, the cluster can no longer be accessed from the Internet through this IP address. If you disable public network access for a cluster and then re-enable it, the public IP address for accessing the cluster may change. Exercise caution.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. On the **Overview** tab, find **Public Network Access** in the **Configuration** area, and click **Disable** next to it. In the displayed dialog box, enter **CONFIRM** and click **OK**.

   After public network access is disabled, the public IP address and the **Public Network Access Control** and **Bandwidth** parameters disappear.

Accessing a Cluster Through a Public IP Address
-----------------------------------------------

After public network access is enabled, the cluster is assigned a public IP address. You can use this IP address plus a port number to access this cluster.

For example, if the public IP address is **10.62.xxx.xxx** and the port number is **9200**, run the following cURL command to view indexes in the cluster.

.. code-block::

   curl -u username:password -k 'https://10.62.xxx.xxx:9200/_cat/indices'

where, **username** and **password** indicate the username and password of the HTTPS-enabled security-mode cluster.
