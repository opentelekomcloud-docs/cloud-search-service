:original_name: en-us_topic_0000001528379273.html

.. _en-us_topic_0000001528379273:

Creating a User and Granting Permissions by Using Kibana
========================================================

CSS uses the opendistro_security plug-in to provide security cluster capabilities. The opendistro_security plug-in is built based on the RBAC model. RBAC involves three core concepts: user, action, and role. RBAC simplifies the relationship between users and actions, simplifies permission management, and facilitates permission expansion and maintenance. The following figure shows the relationship between the three.


.. figure:: /_static/images/en-us_image_0000001705958261.png
   :alt: **Figure 1** User, action, and role

   **Figure 1** User, action, and role

.. table:: **Table 1** Parameters

   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   +==============+==============================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | User         | A user can send operation requests to Elasticsearch clusters. The user has credentials such as username and password, and zero or multiple backend roles and custom attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                              |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Role         | A role is a combination of permissions and action groups, including operation permissions on clusters, indexes, documents, or fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Permission   | Single permission, for example, creating an index (for example, **indices:admin/create**)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Role mapping | A user will be assigned a role after successful authentication. Role mapping is to map a role to a user (or a backend role). For example, the mapping from **kibana_user** (role) to **jdoe** (user) means that John Doe obtains all permissions of **kibana_user** after being authenticated by **kibana_user**. Similarly, the mapping from **all_access** (role) to **admin** (backend role) means that any user with the backend role **admin** (from the LDAP/Active Directory server) has all the permissions of role **all_access** after being authenticated. You can map a role to multiple users or backend roles. |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Action group | A group of permissions. For example, the predefined **SEARCH** action group grants roles to use **\_search** and **\_msearchAPI**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   +--------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

In addition to the RBAC model, Elasticsearch has an important concept called tenant. RBAC is used to manage user authorization, and tenants are used for information sharing across tenants. In a tenant space, IAM users can share information such as dashboard data and index patterns.

This section describes how to use Kibana to create a user and grant permissions to the user. Kibana can be used to create users and grant permissions only when the security mode is enabled for the cluster.

.. note::

   -  The Kibana UI varies depending on the Kibana version, but their operations are similar. This section takes Kibana 7.6.2 as an example to describe the procedure.
   -  You can customize the username, role name, and tenant name in Kibana.

-  Step 1: :ref:`Logging in to Kibana <en-us_topic_0000001528379273__en-us_topic_0000001223434440_section12163507442>`
-  Step 2: :ref:`Creating a User <en-us_topic_0000001528379273__section111313114129>`
-  Step 3: :ref:`Creating a Role and Granting Permissions <en-us_topic_0000001528379273__section1028814911138>`
-  Step 4: :ref:`Configuring a Role for a User <en-us_topic_0000001528379273__section1997772813158>`

.. _en-us_topic_0000001528379273__en-us_topic_0000001223434440_section12163507442:

Logging in to Kibana
--------------------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

   Enter the administrator username and password to log in to Kibana.

   -  Username: **admin** (default administrator account name)
   -  Password: Enter the administrator password you set when creating the cluster in security mode.


   .. figure:: /_static/images/en-us_image_0000001575635862.png
      :alt: **Figure 2** Login page

      **Figure 2** Login page

.. _en-us_topic_0000001528379273__section111313114129:

Creating a User
---------------

Log in to Kibana and create a user on the **Security** page.

#. After a successful login, choose **Security** in the navigation tree on the left of the Kibana operation page. The **Security** page is displayed.


   .. figure:: /_static/images/en-us_image_0000001656902246.png
      :alt: **Figure 3** Accessing the **Security** page

      **Figure 3** Accessing the **Security** page

#. Choose **Authentication Backends** > **Internal Users Database**.


   .. figure:: /_static/images/en-us_image_0000001657061586.png
      :alt: **Figure 4** Adding a user (1)

      **Figure 4** Adding a user (1)

#. On the **Internal Users Database** page, choose |image1|. The page for adding user information is displayed.


   .. figure:: /_static/images/en-us_image_0000001705220953.png
      :alt: **Figure 5** Adding a user (2)

      **Figure 5** Adding a user (2)

#. On the user creation page, specify **Username**, **Password**, and **Repeatpassword**, and click **Submit**.

The user will be displayed in the user list.

.. _en-us_topic_0000001528379273__section1028814911138:

Creating a Role and Granting Permissions
----------------------------------------

Create a role and grant permissions to the role.

#. Click **Roles**.


   .. figure:: /_static/images/en-us_image_0000001656902250.png
      :alt: **Figure 6** Adding a role

      **Figure 6** Adding a role

#. On the **Open Distro Security Roles** page, click |image2|.

   a. On the **Overview** tab page, set the role name.


      .. figure:: /_static/images/en-us_image_0000001705061717.png
         :alt: **Figure 7** Entering a role name

         **Figure 7** Entering a role name

   b. On the **Cluster Permissions** tab page, set CSS cluster permissions. Set cluster permissions based on service requirements. If this parameter is not specified for a role, the role has no cluster-level permissions.

      -  **Permissions: Action Groups**: You can click **Add Action Group** to set cluster permissions. For example, if you select the **read** permission for a cluster, you can only view information such as the cluster status and cluster nodes.
      -  **Permissions: Single Permissions**: Select **Show Advanced** and click **Add Single Permission** to set more refined permissions for the cluster. For example, if this parameter is set to **indices:data/read**, you can only read specified indexes.


      .. figure:: /_static/images/en-us_image_0000001705220957.png
         :alt: **Figure 8** **Cluster Permissions** tab page

         **Figure 8** **Cluster Permissions** tab page

   c. Configure index permissions on the **Index Permissions** page.

      -  **Index patterns**: Set this parameter to the name of the index whose permission needs to be configured. For example, my_store.

         .. note::

            Use different names for the index and the user.

      -  **Permissions: Action Groups**: Click **Add Action Group** and set the permission as required. For example, select the read-only permission **Search**.

   d. On the **Tenant Permissions** page, set role permissions based on service requirements.

      -  **Global permissions**: Click **Add Field** to set the kibana read and write permissions of a role, for example, kibana_all_read or kibana_all_write.

      -  **Tenant permissions**: Click **Add tenant pattern** to add a tenant mode and set the **kibana_all_read** or **kibana_all_write** permission for a new tenant mode.


         .. figure:: /_static/images/en-us_image_0000001656902254.png
            :alt: **Figure 9** **Tenant Permissions** tab

            **Figure 9** **Tenant Permissions** tab

#. Click **Save Role Definition** and you can view the configured role.

.. _en-us_topic_0000001528379273__section1997772813158:

Configuring a Role for a User
-----------------------------

After creating a role and granting permissions to the role, you need to map the role to a user so that the user can obtain the permissions of the mapped role.

#. Click **Role Mappings**. On the displayed **Role Mappings** page, map the roles.


   .. figure:: /_static/images/en-us_image_0000001657061594.png
      :alt: **Figure 10** Role mapping

      **Figure 10** Role mapping

#. On the **Role Mappings** page, click |image3| to select a role and add users.

   -  **Role**: Select the name of the role to be mapped.
   -  **Users**: Click **Add User** and enter the name of the user whose role is mapped.


   .. figure:: /_static/images/en-us_image_0000001705227645.png
      :alt: **Figure 11** Users and roles

      **Figure 11** Users and roles

#. Click **Submit**.

#. Verify that the configuration takes effect in Kibana.

.. |image1| image:: /_static/images/en-us_image_0000001705061721.png
.. |image2| image:: /_static/images/en-us_image_0000001657061590.png
.. |image3| image:: /_static/images/en-us_image_0000001705061713.png
