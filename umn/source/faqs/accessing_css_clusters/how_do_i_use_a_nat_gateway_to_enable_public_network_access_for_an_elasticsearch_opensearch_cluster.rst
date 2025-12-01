:original_name: css_02_0033.html

.. _css_02_0033:

How Do I Use a NAT Gateway to Enable Public Network Access for an Elasticsearch/OpenSearch Cluster?
===================================================================================================

Perform the following operations:

1. :ref:`Obtaining Cluster Information <en-us_topic_0000001933318494__en-us_topic_0182065775_section9324115816273>`

2. :ref:`Configuring a NAT Gateway <en-us_topic_0000001933318494__en-us_topic_0182065775_section13091155184816>`

3. :ref:`Modifying Security Group Rules for the Cluster <en-us_topic_0000001933318494__en-us_topic_0182065775_section8868104118811>`

4. :ref:`Accessing a Cluster over the Public Network <en-us_topic_0000001933318494__en-us_topic_0182065775_section1474433184620>`

.. caution::

   If your CSS clusters do not have the security mode enabled, do not allow public network access to them via the NAT gateway. Otherwise, your data will be exposed to the Internet.

.. _en-us_topic_0000001933318494__en-us_topic_0182065775_section9324115816273:

Obtaining Cluster Information
-----------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters** > **Elasticsearch** or **Clusters** > **OpenSearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Click the **Overview** tab.
#. In the **Configuration** area, obtain the cluster's **Region**, **VPC**, **Current Subnet**, and **Private IPv4 Address**.

.. _en-us_topic_0000001933318494__en-us_topic_0182065775_section13091155184816:

Configuring a NAT Gateway
-------------------------

#. Create a public NAT gateway to enable public network access for the current cluster.

   For details, see *NAT Gateway User Guide*. :ref:`Table 1 <en-us_topic_0000001933318494__table7995546662>` describes the key parameters. Set other parameters based on service requirements.

   .. _en-us_topic_0000001933318494__table7995546662:

   .. table:: **Table 1** Configuring a public NAT gateway

      ========= =======================================================
      Parameter Description
      ========= =======================================================
      Region    Use the region of the Elasticsearch/OpenSearch cluster.
      VPC       Use the VPC of the Elasticsearch/OpenSearch cluster.
      Subnet    Use the subnet of the Elasticsearch/OpenSearch cluster.
      ========= =======================================================

#. After a public NAT gateway is created, add DNAT rules to allow the cluster in your VPC to provide services accessible from the Internet.

   For details, see *NAT Gateway User Guide*. :ref:`Table 2 <en-us_topic_0000001933318494__table1366892773110>` describes the key parameters. Set other parameters based on service requirements.

   .. _en-us_topic_0000001933318494__table1366892773110:

   .. table:: **Table 2** Adding a DNAT rule

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                         |
      +===================================+=====================================================================================================================================================================+
      | Public IP Address Type            | Select **EIP**.                                                                                                                                                     |
      |                                   |                                                                                                                                                                     |
      |                                   | Remember the configured IP address, which will be needed for accessing the cluster from the public network.                                                         |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Public Port                       | A custom port can be configured.                                                                                                                                    |
      |                                   |                                                                                                                                                                     |
      |                                   | Remember the configured port, which will be needed for accessing the cluster from the public network.                                                               |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Private IP Address                | Enter the cluster's private IPv4 address obtained :ref:`Obtaining Cluster Information <en-us_topic_0000001933318494__en-us_topic_0182065775_section9324115816273>`. |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Private Port                      | Enter 9200.                                                                                                                                                         |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. caution::

      If the cluster has multiple private IPv4 addresses, add multiple DNAT rules.

.. _en-us_topic_0000001933318494__en-us_topic_0182065775_section8868104118811:

Modifying Security Group Rules for the Cluster
----------------------------------------------

#. Log in to the CSS management console.
#. In the navigation pane, choose **Clusters** > **Elasticsearch** or **Clusters** > **OpenSearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Click the **Overview** tab.
#. In the **Configuration** area, find **Security Group**, and click the security group name to go to the details page.
#. Click the **Inbound Rules** tab.
#. Click **Add Rule** to add an inbound rule to allow port 9200.
#. Click **OK**.

.. _en-us_topic_0000001933318494__en-us_topic_0182065775_section1474433184620:

Accessing a Cluster over the Public Network
-------------------------------------------

Enter **https://{IP}:{port}** or **http://{IP}:{port}** in the browser address box to access the Elasticsearch or OpenSearch cluster.

-  **IP** and **port** are the EIP and port you set when you added DNAT rules.
-  If you have enabled **Security Mode** for the cluster, enter **https://{IP}:{port}** and then enter the username and password for the cluster.
-  If you have not enabled **Security Mode** for the cluster, enter **http://{IP}:{port}**.
