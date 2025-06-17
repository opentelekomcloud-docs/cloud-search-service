:original_name: css_01_0493.html

.. _css_01_0493:

Changing the Security Mode of an OpenSearch Cluster
===================================================

This topic describes how to change the security mode of an existing cluster.

Scenario
--------

You can create a cluster by choosing its security mode and web protocol (HTTP or HTTPS). For details about the differences between clusters of different security mode settings (including HTTP/HTTPS), see :ref:`Table 1 <css_01_0493__css_01_0158_en-us_topic_0000001410060261_table198661437165914>`.

.. _css_01_0493__css_01_0158_en-us_topic_0000001410060261_table198661437165914:

.. table:: **Table 1** Cluster security modes

   +---------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Cluster Type              |                                                 | Description                                                                                                                                                                                                                                                                    | Characteristics                                                                                                                              |
   +===========================+=================================================+================================================================================================================================================================================================================================================================================+==============================================================================================================================================+
   | Non-security mode cluster | Cluster for which the security mode is disabled | With such a cluster, access to the cluster will require no user authentication, and data will be transmitted in plaintext using HTTP. Make sure the customer is in a secure environment, and do not expose the cluster access interface to the public network.                 | This type of cluster is mostly used for internal services and testing.                                                                       |
   |                           |                                                 |                                                                                                                                                                                                                                                                                |                                                                                                                                              |
   |                           |                                                 |                                                                                                                                                                                                                                                                                | -  Advantage: simple and easy to access.                                                                                                     |
   |                           |                                                 |                                                                                                                                                                                                                                                                                | -  Disadvantage: poor security as anyone can access it.                                                                                      |
   +---------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   | Security-mode cluster     | Cluster in security mode + HTTP                 | A security-mode cluster requires user authentication. It supports access control and data encryption, and it uses HTTP to transmit data in plaintext. Make sure the customer is in a secure environment, and do not expose the cluster access interface to the public network. | Access control by user permissions is supported. This type of cluster is suitable for workloads that are particularly performance-demanding. |
   |                           |                                                 |                                                                                                                                                                                                                                                                                |                                                                                                                                              |
   |                           |                                                 |                                                                                                                                                                                                                                                                                | -  Advantage: User authentication improves cluster security. HTTP-based access ensures high performance of the cluster.                      |
   |                           |                                                 |                                                                                                                                                                                                                                                                                | -  Disadvantage: The cluster cannot be accessed from the public network.                                                                     |
   +---------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+
   |                           | Cluster in security mode + HTTPS                | A security-mode cluster requires user authentication. It supports access control and data encryption, and it uses HTTPS to encrypt communication and enhance data security.                                                                                                    | This type of cluster is suitable where there is a high security standard and public network access is required.                              |
   |                           |                                                 |                                                                                                                                                                                                                                                                                |                                                                                                                                              |
   |                           |                                                 |                                                                                                                                                                                                                                                                                | -  Advantage: User authentication improves cluster security, and HTTPS-based secure communication allows for secure public network access.   |
   |                           |                                                 |                                                                                                                                                                                                                                                                                | -  Disadvantage: HTTPS encrypts nearly all information sent between server and client, causing a read performance loss of around 20%.        |
   +---------------------------+-------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+----------------------------------------------------------------------------------------------------------------------------------------------+

:ref:`Table 2 <css_01_0493__css_01_0158_table11800123345617>` lists the options you have when it comes to changing the security model of a cluster.

.. _css_01_0493__css_01_0158_table11800123345617:

.. table:: **Table 2** Security mode change scenarios

   +----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Scenario                                                             | Details                                                                                                                                    |
   +======================================================================+============================================================================================================================================+
   | Change a cluster from non-security mode to security mode + HTTP.     | :ref:`Switching from the Non-Security Mode to Security Mode <css_01_0493__css_01_0158_en-us_topic_0000001410060261_section17593143823914>` |
   +----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Change a cluster from non-security mode to security mode + HTTPS.    |                                                                                                                                            |
   +----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Change a cluster from security mode + HTTP to non-security mode.     | :ref:`Switching from the Security to Non-Security Mode <css_01_0493__css_01_0158_en-us_topic_0000001410060261_section93951219134016>`      |
   +----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Change a cluster from security mode + HTTPS to non-security mode.    |                                                                                                                                            |
   +----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Change a cluster from security mode + HTTP to security mode + HTTPS. | :ref:`Switching the Protocol of Security Clusters <css_01_0493__css_01_0158_en-us_topic_0000001410060261_section672993904118>`             |
   +----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+
   | Change a cluster from security mode + HTTPS to security mode + HTTP. |                                                                                                                                            |
   +----------------------------------------------------------------------+--------------------------------------------------------------------------------------------------------------------------------------------+

Prerequisites
-------------

-  You are advised to back up data before changing the cluster security mode.
-  The target cluster is available and has no tasks in progress.
-  Check whether load balancing is enabled for the cluster. If yes, disable load balancing for the cluster. Enable load balancing again after the security mode is changed. This prevents errors in accessing the cluster through the load balancer during the change.

Constraints
-----------

-  Only clusters (whose version is 6.5.4 or later) created after November 2022 support security mode changing.
-  A cluster automatically restarts when its security mode is being changed. Services are interrupted during the restart. The authentication mode for invoking the cluster will change after the restart, and client configurations need to be adjusted accordingly.
-  If a cluster has already opened the Kibana session box, a session error message will be displayed after you change the cluster security mode. In this case, clear the cache and open Kibana again.
-  Disabling security mode for a cluster clears the security account. The cleared account cannot be restored.

.. _css_01_0493__css_01_0158_en-us_topic_0000001410060261_section17593143823914:

Switching from the Non-Security Mode to Security Mode
-----------------------------------------------------

You can change a non-security cluster to a security cluster that uses HTTP or HTTPS. After a cluster's security mode is enabled, security authentication is required for accessing the cluster.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters** > **Elasticsearch**. The Elasticsearch cluster management page is displayed.

#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.

#. Choose the **Configure Security Mode** tab.

#. Enable the security mode. Enter and confirm the administrator password of the cluster.


   .. figure:: /_static/images/en-us_image_0000001965497265.png
      :alt: **Figure 1** Enabling the security mode

      **Figure 1** Enabling the security mode

#. Enable or disable **HTTPS Access**.

   -  If you enable **HTTPS Access**: The HTTPS protocol is used to encrypt cluster communication and you can configure public networks to access the cluster.
   -  If you disable **HTTPS Access**: The HTTP protocol is used and you cannot configure public networks to access the cluster.

#. Click **Submit**. Confirm the information and the cluster list page is displayed.

   The **Task Status** of the cluster is **The security mode is changing**. When the cluster status changes to **Available**, the security mode has been successfully changed.

.. _css_01_0493__css_01_0158_en-us_topic_0000001410060261_section93951219134016:

Switching from the Security to Non-Security Mode
------------------------------------------------

You can change a security cluster that uses HTTP or HTTPS to a non-security cluster. After a cluster's security mode is disabled, security authentication is no longer required for accessing the cluster.

.. important::

   -  Clusters in non-security mode can be accessed without security authentication, and HTTP protocol is used to transmit data. Ensure the security of the cluster access environment and do not expose the access interface to the public network.
   -  During the switchover from the security mode to the non-security mode, the indexes of the original security cluster will be deleted. Back up data before disabling the security mode.
   -  If a security cluster has been bound to a public IP address, unbind it before changing the security mode.
   -  If a security cluster has enabled Kibana public network access, disable it before changing the security mode.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters**. On the displayed **Clusters** page, locate the target cluster and choose **More** > **Modify Configuration** in the **Operation** column.

#. Choose the **Configure Security Mode** tab.

#. Disable the security mode.


   .. figure:: /_static/images/en-us_image_0000001938378044.png
      :alt: **Figure 2** Disabling the security mode

      **Figure 2** Disabling the security mode

#. Click **Submit**. In the displayed dialog box, confirm the information. The cluster list page is displayed.

   The **Task Status** of the cluster is **The security mode is changing**. When the cluster status changes to **Available**, the security mode has been successfully changed.

.. _css_01_0493__css_01_0158_en-us_topic_0000001410060261_section672993904118:

Switching the Protocol of Security Clusters
-------------------------------------------

You can change the protocol of a security cluster.

.. important::

   If a security cluster has been bound to a public IP address, you need to unbind it before changing HTTPS protocol to HTTP.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters**. On the displayed **Clusters** page, locate the target cluster and choose **More** > **Modify Configuration** in the **Operation** column.

#. Choose the **Configure Security Mode** tab.

#. Enable or disable **HTTPS Access**.


   .. figure:: /_static/images/en-us_image_0000001938218688.png
      :alt: **Figure 3** Configuring the protocol

      **Figure 3** Configuring the protocol

   -  If you enable **HTTPS Access**:

      HTTPS protocol is used to encrypt cluster communication and you can configure public network access.

   -  If you disable **HTTPS Access**: An alarm message is displayed. Click **OK** to disable the function.

      Cluster communication is no longer encrypted and the public network access function cannot be enabled.

#. Click **Submit**. Confirm the information and the cluster list page is displayed.

   The **Task Status** of the cluster is **The security mode is changing**. When the cluster status changes to **Available**, the security mode has been successfully changed.
