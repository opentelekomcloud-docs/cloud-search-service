:original_name: css_02_0033.html

.. _css_02_0033:

How Do I Use a NAT Gateway to Access CSS from the Internet?
===========================================================

Perform the following operations:

1.\ :ref:`Obtaining CSS Information <css_02_0033__en-us_topic_0182065775_section9324115816273>`

2.\ :ref:`Configuring a NAT Gateway <css_02_0033__en-us_topic_0182065775_section13091155184816>`

3.\ :ref:`Modifying Security Group Rules <css_02_0033__en-us_topic_0182065775_section8868104118811>`

4.\ :ref:`Accessing CSS from the Internet <css_02_0033__en-us_topic_0182065775_section1474433184620>`

.. caution::

   If your CSS clusters do not have the security mode enabled, do not access CSS through the NAT gateway. Otherwise, the cluster data will be exposed to the Internet.

.. _css_02_0033__en-us_topic_0182065775_section9324115816273:

Obtaining CSS Information
-------------------------

#. Log in to the CSS management console.

#. On the **Clusters** page, click the name of a cluster. The **Basic Information** page is displayed by default.

#. In the **Configuration Information** area, view the **Private Network Address**, **VPC**, and **Subnet** information.


   .. figure:: /_static/images/en-us_image_0000001933318582.png
      :alt: **Figure 1** Required information

      **Figure 1** Required information

.. _css_02_0033__en-us_topic_0182065775_section13091155184816:

Configuring a NAT Gateway
-------------------------

#. Create a NAT gateway.

   a. Log in to the console and choose **Service List** > **Networking** >\ **NAT Gateway**. The **Network Console** page is displayed.
   b. Click **Create Public NAT Gateway**. On the displayed page, configure related parameters.

      .. note::

         Set **VPC** and **Subnet** to the values you obtained in :ref:`Obtaining CSS Information <css_02_0033__en-us_topic_0182065775_section9324115816273>`.

   c. Click **Next**, confirm the configurations, and click **Create Now**.

#. Add DNAT rules.

   a. On the **Public NAT Gateways** page, click the name of the NAT gateway you purchased. The details page is displayed.
   b. Choose **DNAT Rules** > **Add DNAT Rule**. For details, see section "Adding a DNAT Rule" in the *NAT Gateway User Guide*. When configuring DNAT rules, use the following settings:

      .. note::

         -  **EIP**: Create an EIP on the **EIPs** page based on your service requirements.
         -  **Outside Port**: Custom.
         -  **Private IP Address**: private network IP address of CSS, which is the **Private Network Address** you obtained in :ref:`Obtaining CSS Information <css_02_0033__en-us_topic_0182065775_section9324115816273>`.
         -  **Inside Port**: 9200.
         -  If your cluster contains multiple private IP addresses, add one DNAT rule for each address.

   c. Click **OK**.

.. _css_02_0033__en-us_topic_0182065775_section8868104118811:

Modifying Security Group Rules
------------------------------

#. Log in to the CSS management console. In the navigation pane, click **Clusters**. On the displayed **Clusters** page, click the name of the target cluster to go to the **Basic Information** page
#. On the **Basic Information** page, click **Security Group**.
#. On the **Basic Information** page of the security group, click the **Inbound Rules** tab.
#. Click **Add Rule** to add an inbound rule for port 9200.
#. Click **OK**.

.. _css_02_0033__en-us_topic_0182065775_section1474433184620:

Accessing CSS from the Internet
-------------------------------

Enter **https://IP:port** or **http://IP:port** in the address box of the browser.

-  **IP** and **port** are an EIP and port you set when you added DNAT rules.
-  If you have enabled **Security Mode** for the cluster, enter **https://IP:port** and then enter the username and password that you set for security mode on the displayed page.
-  If you have not enabled **Security Mode** for the cluster, just enter **http://IP:port**.
