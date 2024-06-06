:original_name: en-us_topic_0000001590963076.html

.. _en-us_topic_0000001590963076:

Accessing a Cluster from a Public Network
=========================================

You can access a security cluster that has the HTTPS access enabled through the public IP address provided by the system.

By default, CSS uses a shared load balancer for public network access. You can use a dedicated load balancer to improve performance. For details about its configuration, see :ref:`Connecting to a Dedicated Load Balancer <en-us_topic_0000001640645481>`.

.. note::

   If public network access is enabled for CSS, then EIP and bandwidth resources will be used and billed.

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

Managing Public Network Access
------------------------------

You can configure, modify, view the public network access of, or disassociate the public IP address from a cluster.

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters** > **OpenSearch**.
#. On the **Clusters** page, click the name of the target cluster. On the **Basic Information** page that is displayed, manage the public network access configurations.

   -  Configure public network access

      If you did not configure the public network access during cluster creation, you can configure it on the cluster details page after configuring the cluster.

      Click **Associate** next to **Public IP Address**, set the access bandwidth, and click **OK**.

      If the association fails, wait for several minutes and try again.

   -  Modify public network access

      For a cluster for which you have configured public network access, you can click **Edit** next to **Bandwidth** to modify the bandwidth, or you can click **Set** next to **Access Control** to set the access control function and the whitelist for access.

   -  View the associated public IP address

      On the basic information page of a cluster, you can view the public IP address associated with the cluster.

   -  Disassociate a public IP address from a cluster

      To disassociate the public IP address, click **Disassociate** next to **Public IP Address**.

Accessing a Cluster Through the Public IP Address
-------------------------------------------------

After configuring the public IP address, you can use it to access the cluster.

For example, run the following cURL commands to view the index information in the cluster. In this example, the public access IP address of one node in the cluster is **10.62.179.32** and the port number is **9200**.

-  If the cluster you access does not have the security mode enabled, run the following command:

   .. code-block::

      curl 'http://10.62.179.32:9200/_cat/indices'

-  If the cluster you access has the security mode enabled, access the cluster using HTTPS and add the username, password and **-u** to the cURL command.

   .. code-block::

      curl -u username:password -k 'https://10.62.179.32:9200/_cat/indices'
