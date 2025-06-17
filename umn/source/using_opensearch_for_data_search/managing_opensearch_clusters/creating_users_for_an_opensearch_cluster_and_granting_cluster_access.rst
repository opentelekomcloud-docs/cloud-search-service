:original_name: css_01_0329.html

.. _css_01_0329:

Creating Users for an OpenSearch Cluster and Granting Cluster Access
====================================================================

CSS limits access to security-mode clusters to authorized users only. When creating a security-mode cluster, an administrator account must be created. This administrator account can use OpenSearch Dashboards to add new users for the cluster and grant them the required permissions.

Context
-------

CSS uses the opendistro_security plug-in to provide security cluster capabilities. The opendistro_security plug-in is built based on the RBAC model. RBAC involves three core concepts: user, action, and role. RBAC simplifies the relationship between users and actions, simplifies permission management, and facilitates permission expansion and maintenance. The following figure shows the relationship between the three.


.. figure:: /_static/images/en-us_image_0000001963190104.png
   :alt: **Figure 1** User, action, and role

   **Figure 1** User, action, and role

.. table:: **Table 1** Parameters for creating and authorizing a user on OpenSearch Dashboards

   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   +==============+====================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | Permission   | A single permission, for example, creating an index (for example, **indices:admin/create**).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Action group | An action group is a group of permissions. For example, the predefined **SEARCH** action group grants roles permissions to use **\_search** and **\_msearchAPI**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Role         | A role is a combination of permissions or action groups, including operation permissions on clusters, indexes, documents, or fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | User         | A user can send operation requests to an OpenSearch cluster. The user has credentials such as username and password, and zero or multiple backend roles and custom attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Role mapping | A user will be assigned a role after successful authentication. Role mapping means to map a role to a user (or a backend role). For example, the mapping from **kibana_user** (role) to **jdoe** (user) means that John Doe obtains all permissions of **kibana_user** after being authenticated by **kibana_user**. Similarly, the mapping from **all_access** (role) to **admin** (backend role) means that any user with the backend role **admin** (from the LDAP/Active Directory server) has all the permissions of role **all_access** after being authenticated. You can map each role to multiple users or backend roles. |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

On OpenSearch Dashboards, you can configure user permissions on the OpenSearch cluster under **Security** to implement fine-grained access control at four levels: cluster, index, document, and field.

Users can be added or deleted for a cluster, and mapped to roles. This way, you assign roles to users.

With role mapping, you can configure the members of each role and assign roles to users based on usernames, backend roles, and host names. For each role, you can configure cluster, index, and document access permissions, as well as the permission to use OpenSearch Dashboards.

For more about security configuration for a security-mode cluster and the detailed guide, see the official OpenSearch document `About Security in OpenSearch <https://opendistro.github.io/for-elasticsearch-docs/docs/security/>`__.

Constraints
-----------

You can customize the username, role name, and tenant name in the **OpenSearch Dashboards**.

Creating a User and Granting Permissions
----------------------------------------

#. Log in to the OpenSearch Dashboards.

   a. Log in to the CSS management console.
   b. In the navigation pane, choose **Clusters** > **OpenSearch**.
   c. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
   d. Enter the administrator username and password to log in to the OpenSearch Dashboards.

      -  Username: **admin** (default administrator account name)

      -  Password: Enter the administrator password you set when creating the cluster in security mode.


         .. figure:: /_static/images/en-us_image_0000001938378000.png
            :alt: **Figure 2** Logging in to OpenSearch

            **Figure 2** Logging in to OpenSearch

#. Creating a user.

   a. On the **OpenSearch Dashboards** page, choose **Security**. The **Security** page is displayed.


      .. figure:: /_static/images/en-us_image_0000001965417001.png
         :alt: **Figure 3** Going to the Security page

         **Figure 3** Going to the Security page

   b. Choose **Internal users** on the left. The user creation page is displayed.


      .. figure:: /_static/images/en-us_image_0000001965416993.png
         :alt: **Figure 4** Creating a user

         **Figure 4** Creating a user

   c. Click **Create internal user**. The user information configuration page is displayed.

   d. In the **Credentials** area, enter the username and password.


      .. figure:: /_static/images/en-us_image_0000001965497221.png
         :alt: **Figure 5** Entering the username and password

         **Figure 5** Entering the username and password

   e. Click **Create**. After the user is created, it is displayed in the user list.


      .. figure:: /_static/images/en-us_image_0000001965497225.png
         :alt: **Figure 6** User information

         **Figure 6** User information

#. Create a role and grant permissions to the role.

   a. Select **Roles** from the **Security** drop-down list box.

   b. On the **Roles** page, click **Create role**. The role creation page is displayed.

   c. In the **Name** area, set the role name.


      .. figure:: /_static/images/en-us_image_0000001938218636.png
         :alt: **Figure 7** Setting a role name

         **Figure 7** Setting a role name

   d. On the **Cluster Permissions** page, set the cluster permission. Set cluster permissions based on service requirements. If this parameter is not specified for a role, the role has no cluster-level permissions.


      .. figure:: /_static/images/en-us_image_0000001938377996.png
         :alt: **Figure 8** Assigning cluster-level permissions

         **Figure 8** Assigning cluster-level permissions

   e. In the **Index Permissions** area, set the index permission.


      .. figure:: /_static/images/en-us_image_0000001938218644.png
         :alt: **Figure 9** Setting index permissions

         **Figure 9** Setting index permissions

   f. On the **Tenant Permissions** page, set role permissions.


      .. figure:: /_static/images/en-us_image_0000001938218648.png
         :alt: **Figure 10** Role permissions

         **Figure 10** Role permissions

      After the setting is complete, you can view the created role on the **Roles** page.

#. Map a user with a role to bind them.

   a. Select **Roles** from the **Security** drop-down list box.

   b. On the **Roles** page, select the role to be mapped. The role mapping page is displayed.

      |image1|

   c. On the **Mapped users** tab page, click **Map users** and select the user to be mapped from the **users** drop-down list box.

      |image2|

   d. Click **Map**.

   e. After the configuration is complete, you can check whether the configuration has taken effect in OpenSearch Dashboards.

.. |image1| image:: /_static/images/en-us_image_0000001938218640.png
.. |image2| image:: /_static/images/en-us_image_0000001965497217.png
