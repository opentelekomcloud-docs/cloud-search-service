:original_name: en-us_topic_0000001591294758.html

.. _en-us_topic_0000001591294758:

Changing the Security Mode
==========================

After a cluster is created, its security mode can be changed in the following methods:

-  :ref:`Switching from the Non-Security Mode to Security Mode <en-us_topic_0000001591294758__en-us_topic_0000001528379285_en-us_topic_0000001410060261_section17593143823914>`
-  :ref:`Switching from the Security to Non-Security Mode <en-us_topic_0000001591294758__en-us_topic_0000001528379285_en-us_topic_0000001410060261_section93951219134016>`
-  :ref:`Switching the Protocol of Security Clusters <en-us_topic_0000001591294758__en-us_topic_0000001528379285_en-us_topic_0000001410060261_section672993904118>`

Context
-------

You can create clusters in multiple security modes. For details about the differences between security modes, see :ref:`Table 1 <en-us_topic_0000001591294758__en-us_topic_0000001528379285_en-us_topic_0000001410060261_table198661437165914>`.

.. _en-us_topic_0000001591294758__en-us_topic_0000001528379285_en-us_topic_0000001410060261_table198661437165914:

.. table:: **Table 1** Cluster security modes

   +--------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | Security Mode                  | Scenario                                                                                             | Advantage                                                                                                                                                                                   | Disadvantage                                                                  |
   +================================+======================================================================================================+=============================================================================================================================================================================================+===============================================================================+
   | Non-Security Mode              | Intranet services and test scenarios                                                                 | Simple. Easy to access.                                                                                                                                                                     | Poor security. Anyone can access such clusters.                               |
   +--------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | Security Mode + HTTP Protocol  | User permissions can be isolated, which is applicable to scenarios sensitive to cluster performance. | Security authentication is required for accessing such clusters, which improves cluster security. Accessing a cluster through HTTP protocol can retain the high performance of the cluster. | Cannot be accessed from the public network.                                   |
   +--------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+
   | Security Mode + HTTPS Protocol | Scenarios that require high security and public network access.                                      | Security authentication is required for accessing such clusters, which improves cluster security. HTTPS protocol allows public network to access such clusters.                             | The performance of clusters using HTTPS is 20% lower than that of using HTTP. |
   +--------------------------------+------------------------------------------------------------------------------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-------------------------------------------------------------------------------+

Prerequisites
-------------

-  You are advised to back up data before changing the cluster security mode.
-  The target cluster is available and has no tasks in progress.

Constraints
-----------

-  A cluster automatically restarts when its security mode is being changed. Services are interrupted during the restart. The authentication mode for calling the cluster will change after the restart, and client configurations need to be adjusted accordingly.
-  If a cluster has already opened the Kibana session box, a session error message will be displayed after you change the cluster security mode. In this case, clear the cache and open Kibana again.

.. _en-us_topic_0000001591294758__en-us_topic_0000001528379285_en-us_topic_0000001410060261_section17593143823914:

Switching from the Non-Security Mode to Security Mode
-----------------------------------------------------

You can change a non-security cluster to a security cluster that uses HTTP or HTTPS. After a cluster's security mode is enabled, security authentication is required for accessing the cluster.

#. Log in to the CSS management console.

#. In the navigation pane, choose a cluster type. The cluster management page is displayed.

#. Choose **More** > **Modify Configuration** in the **Operation** column of the target cluster. The **Modify Configuration** page is displayed.

#. Choose the **Configure Security Mode** tab.

#. Enable the security mode. Enter and confirm the administrator password of the cluster.

#. Enable or disable **HTTPS Access**.

   -  If you enable **HTTPS Access**: The HTTPS protocol is used to encrypt cluster communication and you can configure public networks to access the cluster.
   -  If you disable **HTTPS Access**: The HTTP protocol is used and you cannot configure public networks to access the cluster.

#. Click **Submit**. Confirm the information and the cluster list page is displayed.

   The **Task Status** of the cluster is **The security mode is changing**. When the cluster status changes to **Available**, the security mode has been successfully changed.

.. _en-us_topic_0000001591294758__en-us_topic_0000001528379285_en-us_topic_0000001410060261_section93951219134016:

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

#. Click **Submit**. Confirm the information and the cluster list page is displayed.

   The **Task Status** of the cluster is **The security mode is changing**. When the cluster status changes to **Available**, the security mode has been successfully changed.

.. _en-us_topic_0000001591294758__en-us_topic_0000001528379285_en-us_topic_0000001410060261_section672993904118:

Switching the Protocol of Security Clusters
-------------------------------------------

You can change the protocol of a security cluster.

.. important::

   If a security cluster has been bound to a public IP address, you need to unbind it before changing HTTPS protocol to HTTP.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters**. On the displayed **Clusters** page, locate the target cluster and choose **More** > **Modify Configuration** in the **Operation** column.

#. Choose the **Configure Security Mode** tab.

#. Enable or disable **HTTPS Access**.

   -  If you enable **HTTPS Access**:

      HTTPS protocol is used to encrypt cluster communication and you can configure public network access.

   -  If you disable **HTTPS Access**: An alarm message is displayed. Click **OK** to disable the function.

      When the HTTP protocol is used, cluster communication is no longer encrypted and the public network access function cannot be enabled.

#. Click **Submit**. Confirm the information and the cluster list page is displayed.

   The **Task Status** of the cluster is **The security mode is changing**. When the cluster status changes to **Available**, the security mode has been successfully changed.
