:original_name: css_01_0082.html

.. _css_01_0082:

Configuring VPC Endpoints for an Elasticsearch Cluster
======================================================

VPC Endpoint enables you to access resources across VPCs using a dedicated gateway, without exposing the network information of servers. A VPC endpoint can be accessed via an IPv4 address or private domain name.

-  An IPv4 address is automatically allocated when VPC Endpoint is enabled.
-  A private domain name is allocated only when you enable private domain names.

VPC Endpoint uses a shared load balancer for internal network access. If your workloads require faster access, we recommend that you use a dedicated load balancer to handle access to your cluster. For details, see :ref:`Configuring a Dedicated Load Balancer for an Elasticsearch Cluster <css_01_0181>`.

Impact on Billing
-----------------

VPC endpoints, if created for the cluster, will incur extra fees, depending on the resource usage. For details, see section "Billing" in *VPC Endpoint User Guide*.

Constraints
-----------

-  You need specific permissions to create VPC endpoints. For details, see the "Permissions" section in the *VPC Endpoint User Guide*.
-  Public network access and the VPC Endpoint service share a load balancer. If you configure a whitelist for public network access, and because this whitelist is deployed to the shared load balancer, it will control not only access from the public network, but also access using private IP addresses through VPCEP. In this case, you need to add IP address **198.19.128.0/17** to the public network access whitelist to allow traffic through VPCEP.
-  After VPCEP is enabled, access to CSS through a VPCEP IP address or private domain name from within the internal network is not controlled by any cluster security group rules. Rather, you need to configure a VPCEP whitelist to implement access control. For details, see section "Configuring Access Control for an Interface VPC Endpoint" in *VPC Endpoint User Guide*.

Enabling VPC Endpoint
---------------------

If VPC Endpoint was not enabled when the cluster was created, you can enable it as follows:

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. On the **Overview** tab, check the cluster's subnet information in the **Configuration** area. When you add a VPC endpoint, an IP address that belongs to the current subnet of the cluster is automatically assigned to it.


   .. figure:: /_static/images/en-us_image_0000002272216364.png
      :alt: **Figure 1** Checking the current subnet

      **Figure 1** Checking the current subnet

   If you want to use another subnet, switch the subnet first, and then enable VPC Endpoint. For details, see :ref:`Can I Expand the Subnet for an Elasticsearch or OpenSearch Cluster? <css_02_0081>`

#. Choose **Cluster Access** > **VPC Endpoint**.

#. Toggle on **VPC Endpoint**. In the displayed dialog box, select relevant options.

   .. table:: **Table 1** Options for enabling VPC Endpoint

      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Option                            | Description                                                                                                                                                                                                    |
      +===================================+================================================================================================================================================================================================================+
      | Create Private Domain Name        | Whether to create a private domain name for the VPC endpoint.                                                                                                                                                  |
      |                                   |                                                                                                                                                                                                                |
      |                                   | -  Enable: The system automatically assigns a private domain name to the VPC endpoint. After cluster creation, you can check this private domain name on the **VPC Endpoint** tab of the cluster details page. |
      |                                   | -  Disable: No private domain name will be configured for the VPC endpoint. The cluster can only be accessed through an IP address assigned to the VPC endpoint.                                               |
      +-----------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Click **OK** to enable VPC Endpoint. After the VPC endpoint is enabled, its information is displayed below. When its status changes to **Accepted**, the current cluster can be accessed through the VPC endpoint.

Managing VPC Endpoints
----------------------

After VPC Endpoint is enabled for a cluster, you can set access control, check VPC endpoint information, and deny access from specific VPC endpoints.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

#. Choose **Cluster Access** > **VPC Endpoint**.

#. **Configure access control for a VPC endpoint.**

   a. Click **Modify** on the right of **VPC Endpoint Whitelist**. In the displayed dialog box, add accounts that are allowed to access the cluster through the VPC endpoint. If no account is added or the account ID is set to **\***, all users are allowed to access the cluster through the VPC endpoint.

      -  Click **Add** to add accounts in **Account ID**. To obtain your authorized account ID, point to your username in the upper right corner, and choose **My Credentials**. Copy the value of **Account ID**.
      -  Click **Delete** in the **Operation** column to delete an authorized account.

   b. Click **OK**.

#. **Check VPC endpoint information.**

   The VPC endpoint list shows the VPC endpoints created for the current cluster. You can obtain their **Status**, **Service Address**, and **Private Domain Name**.


   .. figure:: /_static/images/en-us_image_0000002306895117.png
      :alt: **Figure 2** Managing VPC endpoints

      **Figure 2** Managing VPC endpoints

#. .. _en-us_topic_0000001938377836__li1433652424013:

   **Modify VPC endpoint status** to make the cluster accessible or inaccessible through specific endpoints.

   -  In the VPC endpoint list, select the target endpoint and click **Reject** in the **Operation** column. If the endpoint status changes to **Rejected**, it means the cluster is no longer accessible through this endpoint.
   -  Select an endpoint whose status is **Rejected**. Click **Accept** in the **Operation** column. If the endpoint status changes to **Accepted**, it means the cluster is accessible again through this endpoint.

Disabling VPC Endpoint
----------------------

If the cluster no longer requires cross-VPC access via VPC endpoints, disable VPC Endpoint to release resources.

.. warning::

   After VPC Endpoint is disabled, the cluster is no longer accessible through a VPCEP IP address or private domain name. If you disable VPC Endpoint and then re-enable it, the VPCEP IP address or private domain name for accessing the cluster may change. When it happens, you may need to update the client connection. If you just need to temporarily disable VPC Endpoint (rather than permanently releasing its resources), do so by rejecting specific VPC endpoints. For details, see :ref:`7 <en-us_topic_0000001938377836__li1433652424013>`.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Choose **Cluster Access** > **VPC Endpoint**.
#. Toggle off **VPC Endpoint**. In the displayed dialog box, enter **CONFIRM** and click **OK**.

Accessing a Cluster Through a VPC Endpoint
------------------------------------------

#. Obtain the private domain name or IP address of a VPC endpoint.

   In the VPC endpoint list, check **Service Address** or **Private Domain Name**.

#. On the client (e.g., an ECS), run the curl command to access the cluster.

   For example, run the following command to check the cluster's index information:

   -  For a cluster with the security mode disabled:

      .. code-block::

         curl "http://<host>:9200/_cat/indices"

   -  For a security-mode cluster that uses HTTP:

      .. code-block::

         curl -u <user>:<password> "http://<host>:9200/_cat/indices"

   -  For a security-mode cluster that uses HTTPS:

      .. code-block::

         curl -u <user>:<password> -k "https://<host>:9200/_cat/indices"

   where, **user** and **password** are the username and password used for access the cluster, and **host** indicates the VPC endpoint's private domain name or IP address.
