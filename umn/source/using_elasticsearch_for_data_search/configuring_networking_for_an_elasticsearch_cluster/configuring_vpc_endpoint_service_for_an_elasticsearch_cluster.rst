:original_name: css_01_0412.html

.. _css_01_0412:

Configuring VPC Endpoint Service for an Elasticsearch Cluster
=============================================================

VPC Endpoint Service enables you to access resources across Virtual Private Clouds (VPCs) using a dedicated gateway, without exposing the network information of servers. When VPC Endpoint Service is enabled, a VPC endpoint will be created by default. You can select Private Domain Name Creation if necessary. Users will be able to access this cluster across VPCs through node IP addresses or a private domain name.

VPC Endpoint uses a shared load balancer for intranet access. If your workloads require quicker access, you are advised to use a dedicated load balancer to connect to your cluster. For details about its configuration, see :ref:`Configuring a Dedicated Load Balancer for an Elasticsearch Cluster <css_01_0413>`.

Constraints
-----------

-  VPC endpoint creation requires specific permissions. For details, see the "Permissions" section in the *VPC Endpoint User Guide*.
-  Public network access and the VPC Endpoint service share a load balancer. If you configure a whitelist for public network access, and because this whitelist is deployed to the shared load balancer, it will control not only access from the public network, but also access using private IP addresses through VPCEP. In this case, you need to add IP address **198.19.128.0/17** to the public network access whitelist to allow traffic through VPCEP.
-  After VPCEP is enabled, access to CSS through a VPCEP IP address or private domain name is not controlled by any cluster security group rules. Rather, you need to configure a VPCEP whitelist to implement access control.

Enabling the VPC Endpoint Service
---------------------------------

#. Log in to the CSS management console.
#. Click **Create Cluster** in the upper right corner.
#. On the **Create Cluster** page, set **Advanced Settings** to **Custom**. Enable the VPC endpoint service.

   .. table:: **Table 1** Configuring VPC Endpoint Service

      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                                    |
      +===================================+================================================================================================================================================================================================================================================================================+
      | Private Domain Name Creation      | If **Private Domain Name Creation** is selected, the system generates a node IP address and also automatically creates a private domain name, which enables users to access this cluster from within the same VPC. If it is not selected, only a node IP address is generated. |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Create professional endpoints     | Choose whether to create professional endpoints.                                                                                                                                                                                                                               |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   | -  If unselected, a basic endpoint will be created.                                                                                                                                                                                                                            |
      |                                   | -  If selected, a professional endpoint will be created.                                                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   | .. note::                                                                                                                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   |    If the region where the cluster is located does not support professional endpoints, this option is unavailable. By default, a basic endpoint is created.                                                                                                                    |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | IPv4/IPv6 dual stack network      | Whether to enable IPv4/IPv6 dual-stack networking. This option is available only when IPv6 is enabled for the VPC subnet of the cluster and you have selected **Create professional endpoints** earlier.                                                                       |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | VPC Endpoint Service Whitelist    | In **VPC Endpoint Service Whitelist**, you can add accounts that are allowed to access the cluster using a node IP address or private domain name.                                                                                                                             |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   | -  Click **Add** to add accounts in **Authorized Account ID**. If the authorized account ID is set to **\***, all users are allowed to access the cluster.                                                                                                                     |
      |                                   | -  Click **Delete** in the **Operation** column to delete accounts.                                                                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   | .. note::                                                                                                                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   |    To obtain your authorized account ID, point to your username in the upper right corner, and choose **My Credentials**. Copy the value of **Account ID**.                                                                                                                    |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Enabling the VPC Endpoint Service for an Existing Cluster
---------------------------------------------------------

You can enable the VPC endpoint service while creating a cluster. Alternatively, you can do that by performing the following steps after cluster creation.

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster.

#. Click the **VPC Endpoint Service** tab, and turn on the button next to **VPC Endpoint Service**.

   .. table:: **Table 2** Configuring VPC Endpoint Service

      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                                    |
      +===================================+================================================================================================================================================================================================================================================================================+
      | Private Domain Name Creation      | If **Private Domain Name Creation** is selected, the system generates a node IP address and also automatically creates a private domain name, which enables users to access this cluster from within the same VPC. If it is not selected, only a node IP address is generated. |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Create professional endpoints     | Choose whether to create professional endpoints.                                                                                                                                                                                                                               |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   | -  If unselected, a basic endpoint will be created.                                                                                                                                                                                                                            |
      |                                   | -  If selected, a professional endpoint will be created.                                                                                                                                                                                                                       |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   | .. note::                                                                                                                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   |    If the region where the cluster is located does not support professional endpoints, this option is unavailable. By default, a basic endpoint is created.                                                                                                                    |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | IPv4/IPv6 dual stack network      | Whether to enable IPv4/IPv6 dual-stack networking. This option is available only when IPv6 is enabled for the VPC subnet of the cluster and you have selected **Create professional endpoints** earlier.                                                                       |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | VPC Endpoint Service Whitelist    | In **VPC Endpoint Service Whitelist**, you can add accounts that are allowed to access the cluster using a node IP address or private domain name.                                                                                                                             |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   | -  Click **Add** to add accounts in **Authorized Account ID**. If the authorized account ID is set to **\***, all users are allowed to access the cluster.                                                                                                                     |
      |                                   | -  Click **Delete** in the **Operation** column to delete accounts.                                                                                                                                                                                                            |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   | .. note::                                                                                                                                                                                                                                                                      |
      |                                   |                                                                                                                                                                                                                                                                                |
      |                                   |    To obtain your authorized account ID, point to your username in the upper right corner, and choose **My Credentials**. Copy the value of **Account ID**.                                                                                                                    |
      +-----------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Manage VPC endpoints.

   The **VPC Endpoint Service** page displays all VPC endpoints connected to the current cluster. You can obtain the service address and private domain name of VPC endpoints.


   .. figure:: /_static/images/en-us_image_0000001965497373.png
      :alt: **Figure 1** Managing VPC endpoints

      **Figure 1** Managing VPC endpoints

   Click **Accept** or **Reject** in the **Operation** column to change the node status. If you reject the connection with a VPC endpoint, you cannot access the cluster through the private domain name generated by that VPC endpoint.

Disabling the VPC Endpoint Service
----------------------------------

.. note::

   After the VPC endpoint service is disabled, the cluster can no longer be accessed through the VPCEP IP address or a private domain name. If you disable the VPC endpoint service and then re-enable it, the VPCEP IP address or private domain name for accessing the cluster may change. Exercise caution.

#. Log in to the CSS management console.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster.
#. Choose **VPC Endpoint Service** in the navigation pane, and toggle off the button next to **VPC Endpoint Service**.

Accessing a Cluster Using a Node IP Address or Private Domain Name
------------------------------------------------------------------

#. Obtain the cluster's private domain name or node IP address.

   Log in to the CSS console, click the target cluster name and go to the **Cluster Information** page. Click the **VPC Endpoint Service** tab and check the service address and private domain name.

#. On an ECS, run a cURL command to access the cluster by calling an API.

   The ECS must meet the following requirements:

   -  Sufficient disk space is allocated for the ECS.

   -  The ECS and the cluster must be in the same VPC. After enabling the VPC endpoint service, you can access the cluster from the ECS even when the cluster is not in the same VPC as the ECS.

   -  The security group of the ECS must be the same as that of the cluster.

      If this requirement is not met, modify the ECS security group or configure the inbound and outbound rules of the ECS security group to allow the ECS security group to be accessed by all security groups of the cluster. For details, see `Configuring Security Group Rules <https://docs.otc.t-systems.com/en-us/usermanual/ecs/en-us_topic_0030878383.html>`__.

   -  Configure security group rule settings of the target CSS cluster. Set **Protocol** to **TCP** and **Port Range** to **9200** or a port range including port **9200** for both the outbound and inbound directions.

   -  If the cluster you access does not have the security mode enabled, run the following command:

      .. code-block::

         curl 'http://vpcep-7439f7f6-2c66-47d4-b5f3-790db4204b8d.region01.example.com:9200/_cat/indices'

   -  If the cluster you access has the security mode enabled and uses HTTP, access the cluster using HTTP and provide the username and password by using **-u** in the cURL command.

      .. code-block::

         curl -u username:password  'http:// vpcep-7439f7f6-2c66-47d4-b5f3-790db4204b8d.region01.example.com:9200/cat/indices'

   -  If the cluster you access has the security mode enabled and uses HTTPS, access the cluster using HTTPS and provide the username and password by using **-u** in the cURL command.

      .. code-block::

         curl -u username:password -k 'https://vpcep-7439f7f6-2c66-47d4-b5f3-790db4204b8d.region01.example.com:9200/_cat/indices'
