:original_name: css_01_0076.html

.. _css_01_0076:

Configuring Public Network Access for an Elasticsearch Cluster
==============================================================

Public network access is supported only when **Security Mode** and **HTTPS Access** are enabled for a cluster. When **Public IP Address** is enabled, a public IP address is automatically assigned, which will enable access to the security cluster from the public network. Additionally, you can configure access control from the public network by IP addresses or IP address ranges.

To enable public network access for Elasticsearch or OpenSearch clusters, a shared load balancer is typically used for load balancing. If your workloads require quicker access, you are advised to use a dedicated load balancer to connect to your clusters. For details about its configuration, see :ref:`Configuring a Dedicated Load Balancer for an Elasticsearch Cluster <css_01_0413>`.

Constraints
-----------

-  Enabling public network access for a CSS cluster may incur some fees, as it will need to use EIP and bandwidth resources.
-  The security mode can be enabled only for Elasticsearch 6.5.4 clusters or later and OpenSearch clusters.
-  Public network access and the VPC Endpoint service share a load balancer. If you configure a whitelist for public network access, and because this whitelist is deployed to the shared load balancer, it will control not only access from the public network, but also access using private IP addresses through VPCEP. In this case, you need to add IP address **198.19.128.0/17** to the public network access whitelist to allow traffic through VPCEP.

Configuring Public Network Access
---------------------------------

#. Log in to the CSS management console.
#. On the **Create Cluster** page, enable **Security Mode**. Set the administrator password and enable HTTPS access.
#. Select **Automatically assign** for **Public IP Address** and set related parameters.

   .. table:: **Table 1** Public network access parameters

      +----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter      | Description                                                                                                                                                                                                                 |
      +================+=============================================================================================================================================================================================================================+
      | Bandwidth      | Bandwidth for accessing Kibana with the public IP address                                                                                                                                                                   |
      +----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Access Control | If you disable this function, all IP addresses can access the cluster through the public IP address. If you enable access control, only IP addresses in the whitelist can access the cluster through the public IP address. |
      +----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Whitelist      | IP address or IP address range allowed to access a cluster. Use commas (,) to separate multiple addresses. This parameter can be configured only when **Access Control** is enabled.                                        |
      +----------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Configuring Public Network Access for an Existing Cluster
---------------------------------------------------------

You can configure, modify, view the public network access of, or disassociate the public IP address from a cluster.

#. Log in to the CSS management console.
#. On the **Clusters** page, click the name of the target cluster. On the **Basic Information** page that is displayed, manage the public network access configurations.

   -  Configuring public network access

      If you enabled HTTPS but did not configure the public network access during security cluster creation, you can configure it on the **Basic Information** page after configuring the cluster.

      Click **Associate** next to **Public IP Address**, set the access bandwidth, and click **OK**.

      If the association fails, wait for a few minutes and try again.

   -  Modifying public network access

      For a cluster for which you have configured public network access, you can click **Edit** next to **Bandwidth** to modify the bandwidth, or you can click **Set** next to **Access Control** to set the access control function and the whitelist for access.

   -  Checking public network access settings

      On the **Basic Information** page, you can see the public IP address associated with the current cluster.

   -  Disassociating a public IP address from a cluster

      To disassociate a public IP address, click **Disassociate** next to **Public IP Address**.

      .. note::

         After the public IP address is disassociated, the cluster can no longer be accessed through this IP address. If you disable public network access for a cluster and then re-enable it, the public IP address for accessing the cluster may change. Exercise caution.

Accessing a Cluster Through the Public IP Address
-------------------------------------------------

After configuring the public IP address, you can use it to access the cluster.

For example, if the public IP address is **10.62.179.32** and the port number is **9200**, run the following cURL command to view indexes in the cluster.

.. code-block::

   curl -u username:password -k 'https://10.62.179.32:9200/_cat/indices'

where, **username** and **password** indicate the username and password of the HTTPS-enabled security-mode cluster.
