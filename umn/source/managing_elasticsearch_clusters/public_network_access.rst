:original_name: css_01_0076.html

.. _css_01_0076:

Public Network Access
=====================

You can access a cluster that has the security mode enabled through the public IP address provided by the system.

.. note::

   If public access is enabled for CSS, then EIP and bandwidth resources will be used and billed.

Configuring Public Network Access
---------------------------------

#. Log in to the CSS management console.

#. On the **Create Cluster** page, enable **Security Mode**.

   You can enable **Security Mode** for clusters in Version 6.5.4 and later versions.

#. Select **Automatically assign** for **Public IP Address** and set related parameters.

   .. table:: **Table 1** Public network access parameters

      +----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter      | Description                                                                                                                                                                                                                  |
      +================+==============================================================================================================================================================================================================================+
      | Bandwidth      | Bandwidth of the public network access                                                                                                                                                                                       |
      +----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Access Control | If you disable access control, all IP addresses can access the cluster through the public IP address. If you enable access control, only IP addresses in the whitelist can access the cluster through the public IP address. |
      +----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Whitelist      | IP address or IP address range allowed to access a cluster. Use commas (,) to separate multiple addresses.                                                                                                                   |
      +----------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Managing Public Network Access
------------------------------

You can configure, modify, view the public network access of, or disassociate the public IP address from a cluster.

#. Log in to the CSS management console.
#. On the **Clusters** page that is displayed, click the name of the target cluster.

   -  Configuring public network access

      If you do not configure the public network access during cluster creation, you can configure it on the **Basic Information** page after configuring the cluster.

      Click **Associate** next to **Public IP Address**, set the access bandwidth, and click **OK**.

      If the association fails, wait for several minutes and try again.

   -  Modifying public network access

      For a cluster for which you have configured public network access, you can click **Edit** next to **Bandwidth** to modify the bandwidth, or you can click **Set** next to **Access Control** to set the access control function and the whitelist for access.

   -  Viewing public network access

      On the **Basic Information** page, you can view the public IP address associated with the current cluster.

   -  Disassociating a public IP address from a cluster

      To disassociate the public IP address, click **Disassociate** next to **Public IP Address**.

Accessing a Cluster Through the Public IP Address
-------------------------------------------------

After configuring the public IP address, you can use it to access the cluster. The access address is **https://public IP address:9200/interface URL**.
