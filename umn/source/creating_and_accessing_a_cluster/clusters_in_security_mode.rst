:original_name: css_04_0019.html

.. _css_04_0019:

Clusters in Security Mode
=========================

When creating an Elasticsearch cluster, you can enable the security mode for it. Identity authentication is required when users access a security cluster. You can also authorize and encrypt security clusters.

Context
-------

You can create clusters in multiple security modes. For details about the differences between security modes, see :ref:`Table 1 <css_04_0019__en-us_topic_0000001410060261_table198661437165914>`.

.. _css_04_0019__en-us_topic_0000001410060261_table198661437165914:

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

Identity Verification
---------------------

To access a security cluster, you need to enter the username and password. The identity verification is required for the following two types of users:

-  Administrator: The default administrator username is **admin**, and the password is the one specified during cluster creation.
-  Users: Enter the username and password created through Kibana.

Authorization
-------------

On the **Kibana** console, click **Security** to control user permissions in Elasticsearch clusters. You can configure hierarchical user permissions by cluster, index, document, and field.

You can add or delete users, and map users to different roles for permissions control.


.. figure:: /_static/images/en-us_image_0000001503817384.png
   :alt: **Figure 1** Configuring users

   **Figure 1** Configuring users

You can use role mapping to configure roles and map a user's username, backend role, and host name to a role.


.. figure:: /_static/images/en-us_image_0000001554897033.png
   :alt: **Figure 2** Role mapping

   **Figure 2** Role mapping

You can set permissions for each role to access clusters, indices and documents and assign Kibana tenants different roles.


.. figure:: /_static/images/en-us_image_0000001503977284.png
   :alt: **Figure 3** Configuring role permissions

   **Figure 3** Configuring role permissions

You can set action groups, assign the groups to roles, and configure the roles' permission for accessing indices and documents.


.. figure:: /_static/images/en-us_image_0000001503657480.png
   :alt: **Figure 4** Configuring action groups

   **Figure 4** Configuring action groups

You can view the parameters of authentication and authorization for the current cluster. You can also run the **securityadmin** command to modify the configuration.


.. figure:: /_static/images/en-us_image_0000001503817392.png
   :alt: **Figure 5** Viewing cluster parameters

   **Figure 5** Viewing cluster parameters

You can also clear the security cache.


.. figure:: /_static/images/en-us_image_0000001554577133.png
   :alt: **Figure 6** Clearing the security cache

   **Figure 6** Clearing the security cache

Encryption
----------

When key data is transferred between nodes or over HTTP, SSL/TLS encryption is used to ensure data security.

You can perform the preceding functions on Kibana, using **.yml** files (not recommended), or by calling RESTful APIs. For more information about the security mode, see `Security <https://opendistro.github.io/for-elasticsearch-docs/docs/security/>`__.

Resetting Passwords
-------------------

If you want to change the login password of a cluster with the security mode enabled or you have forgotten the password, reset the cluster password.

#. On the **Clusters** page, locate the target cluster whose password you want to reset and click the cluster name. The **Basic Information** page is displayed.
#. On the **Basic Information** page, click **Reset** next to **Reset Password** to reset the password.

   .. note::

      -  The password can contain 8 to 32 characters.
      -  It must include letters, digits, and special characters. No spaces and backslashes (\\) are allowed.
      -  It cannot be the username or the username spelled backwards.
      -  It is good practice to change the password periodically.
