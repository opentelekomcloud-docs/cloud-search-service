:original_name: en-us_topic_0000001528659093.html

.. _en-us_topic_0000001528659093:

Clusters in Security Mode
=========================

When creating an Elasticsearch cluster, you can enable the security mode for it. Identity authentication is required when users access a security cluster. You can also authorize and encrypt security clusters.

Identity Verification
---------------------

To access a security cluster, you need to enter the username and password. The identity verification is required for the following two types of users:

-  Administrator: The default administrator username is **admin**, and the password is the one specified during cluster creation.
-  Users: Enter the username and password created through Kibana.

Authorization
-------------

On the **Kibana** console, click **Security** to control user permissions in Elasticsearch clusters. You can configure hierarchical user permissions by cluster, index, document, and field. For details, see :ref:`Creating a User and Granting Permissions by Using Kibana <en-us_topic_0000001528379273>`.

You can add or delete users, and map users to different roles for permissions control.


.. figure:: /_static/images/en-us_image_0000001625991489.png
   :alt: **Figure 1** Configuring users

   **Figure 1** Configuring users

You can use role mapping to configure roles and map a user, backend role, and host name to a role.


.. figure:: /_static/images/en-us_image_0000001575631554.png
   :alt: **Figure 2** Role mapping

   **Figure 2** Role mapping

You can set permissions for each role to access clusters, indexes and documents and assign Kibana tenants different roles.


.. figure:: /_static/images/en-us_image_0000001625871637.png
   :alt: **Figure 3** Configuring role permissions

   **Figure 3** Configuring role permissions

You can set action groups, assign the groups to roles, and configure the roles' permission for accessing indexes and documents.


.. figure:: /_static/images/en-us_image_0000001575471938.png
   :alt: **Figure 4** Configuring action groups

   **Figure 4** Configuring action groups

You can view the parameters of authentication and authorization for the current cluster. You can also run the **securityadmin** command to modify the configuration.


.. figure:: /_static/images/en-us_image_0000001625991493.png
   :alt: **Figure 5** Viewing cluster parameters

   **Figure 5** Viewing cluster parameters

You can also clear the security cache.


.. figure:: /_static/images/en-us_image_0000001575312654.png
   :alt: **Figure 6** Clearing the security cache

   **Figure 6** Clearing the security cache

Encryption
----------

When key data is transferred between nodes or through the HTTP protocol, SSL/TLS encryption is used to ensure data security.

You can perform the preceding functions on Kibana, using **.yml** files (not recommended), or by calling RESTful APIs. For more information about the security mode, see `Security <https://opendistro.github.io/for-elasticsearch-docs/docs/security/>`__.

Resetting the Administrator Password
------------------------------------

If you want to change the administrator password of a security cluster or you have forgotten the password, reset the password.

#. On the **Clusters** page, locate the target cluster whose password you want to reset and click the cluster name. The **Cluster Information** page is displayed.
#. In the **Configuration** area, click **Reset** next to **Reset Password**.

   .. note::

      -  The password can contain 8 to 32 characters.
      -  The password must contain at least three of the following character types: uppercase letters, lowercase letters, digits, and special characters. The following special characters are supported: ``~!@#$%^&*()-_=+\|[{}];:,<.>/?``
      -  Do not use the administrator name, or the administrator name spelled backwards.
      -  You are advised to change the password periodically.
