:original_name: css_04_0019.html

.. _css_04_0019:

Clusters in Security Mode
=========================

Security mode is supported for Elasticsearch 7.1.1 and later versions. After you enable security mode, identity verification, authorization, and encryption are required.

This section describes the security mode using Kibana as an example.

.. note::

   You can enable security mode only during cluster creation and not after the cluster is created.

Key Terms
---------

.. table:: **Table 1** Key terms of security mode

   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Term         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   +==============+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | Permission   | Single action, for example, creating an index (for example, **indices:admin/create**)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Action group | A group of permissions. For example, the predefined **SEARCH** action group grants roles permissions to use **\_search** and **\_msearchAPI**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Role         | A role is a combination of permissions and action groups, including operation permissions on clusters, indices, documents, or fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Backend role | (Optional) Other external roles from the backend such as LDAP/Active Directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | User         | A user can send operation requests to the Elasticsearch cluster. The user has credentials such as username and password, zero or more backend roles, and zero or more custom attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Role mapping | A user will be assigned a role after successful authentication. Role mapping is to map a role to a user (or a backend role). For example, the mapping from **kibana_user** (role) to **jdoe** (user) means that John Doe obtains all permissions of **kibana_user** after being authenticated by **kibana_user**. Similarly, the mapping from **all_access** (role) to **admin** (backend role) means that any user with the backend role **admin** (from the LDAP/Active Directory server) has all the permissions of role **all_access** after being authenticated. You can map each role to multiple users or backend roles. |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Identity Verification
---------------------

After enabling the security mode, you need to log in to the cluster with the username and password that you set when you create the cluster. You can perform other operations after you log in successfully.


.. figure:: /_static/images/en-us_image_0000001338716501.png
   :alt: **Figure 1** Login for identity verification

   **Figure 1** Login for identity verification

Authorization
-------------

On the **Kibana** console, click **Security** to control user permissions in Elasticsearch clusters. You can configure hierarchical user permissions by cluster, index, document, and field.

You can add or delete users, and map users to different roles for permissions control.


.. figure:: /_static/images/en-us_image_0000001339036237.png
   :alt: **Figure 2** Configuring users

   **Figure 2** Configuring users

You can use role mapping to configure roles and map a user's username, backend role, and host name to a role.


.. figure:: /_static/images/en-us_image_0000001286276514.png
   :alt: **Figure 3** Role mapping

   **Figure 3** Role mapping

You can set permissions for each role to access clusters, indices and documents and assign Kibana tenants different roles.


.. figure:: /_static/images/en-us_image_0000001338716505.png
   :alt: **Figure 4** Configuring role permissions

   **Figure 4** Configuring role permissions

You can set action groups, assign the groups to roles, and configure the roles' permission for accessing indices and documents.


.. figure:: /_static/images/en-us_image_0000001286116602.png
   :alt: **Figure 5** Configuring action groups

   **Figure 5** Configuring action groups

You can view the parameters of authentication and authorization for the current cluster. You can also run the **securityadmin** command to modify the configuration.


.. figure:: /_static/images/en-us_image_0000001338836353.png
   :alt: **Figure 6** Viewing cluster parameters

   **Figure 6** Viewing cluster parameters

You can also clear the security cache.


.. figure:: /_static/images/en-us_image_0000001286276518.png
   :alt: **Figure 7** Clearing the security cache

   **Figure 7** Clearing the security cache

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
      -  It must include letters, digits, and special characters. No spaces and backslashes (\) are allowed.
      -  It cannot be the username or the username spelled backwards.
      -  It is good practice to change the password periodically.
