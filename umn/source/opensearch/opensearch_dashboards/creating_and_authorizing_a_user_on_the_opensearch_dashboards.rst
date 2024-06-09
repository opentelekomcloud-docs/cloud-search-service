:original_name: en-us_topic_0000001591298682.html

.. _en-us_topic_0000001591298682:

Creating and Authorizing a User on the OpenSearch Dashboards
============================================================

Prerequisites
-------------

The security mode has been enabled for the OpenSearch cluster.

Parameters
----------

.. table:: **Table 1** Parameters for creating and authorizing a user on Kibana

   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter    | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
   +==============+=================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================================+
   | Permission   | Single permission, for example, creating an index (for example, **indices:admin/create**)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Action group | A group of permissions. For example, the predefined **SEARCH** action group grants roles permissions to use **\_search** and **\_msearchAPI**.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Role         | A role is a combination of permissions and action groups, including operation permissions on clusters, indexes, documents, or fields.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Backend role | (Optional) Other external roles from the backend such as LDAP/Active Directory                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | User         | A user can send operation requests to Elasticsearch clusters. The user has credentials such as username and password, and zero or multiple backend roles and custom attributes.                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Role mapping | A user will be assigned a role after successful authentication. Role mapping is to map a role to a user (or a backend role). For example, the mapping from **kibana_user** (role) to **jdoe** (user) means that John Doe obtains all permissions of **kibana_user** after being authenticated by **kibana_user**. Similarly, the mapping from **all_access** (role) to **admin** (backend role) means that any user with the backend role **admin** (from the LDAP/Active Directory server) has all the permissions of role **all_access** after being authenticated. You can map each role to multiple users or backend roles. |
   +--------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   You can customize the username, role name, and tenant name in the **OpenSearch Dashboards**.

Procedure
---------

#. Log in to the OpenSearch Dashboards.

   a. Log in to the CSS management console.
   b. In the navigation pane, choose **Clusters** > **OpenSearch**.
   c. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
   d. Enter the administrator username and password to log in to the OpenSearch Dashboards.

      -  Username: **admin** (default administrator account name)

      -  Password: Enter the administrator password you set when creating the cluster in security mode.


         .. figure:: /_static/images/en-us_image_0000001657091853.png
            :alt: **Figure 1** Logging in to OpenSearch

            **Figure 1** Logging in to OpenSearch

#. Creating a user.

   a. On the **OpenSearch Dashboards** page, choose **Security**. The **Security** page is displayed.


      .. figure:: /_static/images/en-us_image_0000001656851577.png
         :alt: **Figure 2** Going to the Security page

         **Figure 2** Going to the Security page

   b. Choose **Internal users** on the left. The user creation page is displayed.


      .. figure:: /_static/images/en-us_image_0000001657244165.png
         :alt: **Figure 3** Creating a user

         **Figure 3** Creating a user

   c. Click **Create internal user**. The user information configuration page is displayed.

   d. In the **Credentials** area, enter the username and password.


      .. figure:: /_static/images/en-us_image_0000001607766004.png
         :alt: **Figure 4** Entering the username and password

         **Figure 4** Entering the username and password

   e. Click **Create**. After the user is created, it is displayed in the user list.


      .. figure:: /_static/images/en-us_image_0000001607447036.png
         :alt: **Figure 5** User information

         **Figure 5** User information

#. Create a role and grant permissions to the role.

   a. Select **Roles** from the **Security** drop-down list box.

   b. On the **Roles** page, click **Create role**. The role creation page is displayed.

   c. In the **Name** area, set the role name.


      .. figure:: /_static/images/en-us_image_0000001656848929.png
         :alt: **Figure 6** Setting a role name

         **Figure 6** Setting a role name

   d. On the **Cluster Permissions** page, set the cluster permission. Set cluster permissions based on service requirements. If this parameter is not specified for a role, the role has no cluster-level permissions.


      .. figure:: /_static/images/en-us_image_0000001657249665.png
         :alt: **Figure 7** Assigning cluster-level permissions

         **Figure 7** Assigning cluster-level permissions

   e. In the **Index Permissions** area, set the index permission.


      .. figure:: /_static/images/en-us_image_0000001656931909.png
         :alt: **Figure 8** Setting index permissions

         **Figure 8** Setting index permissions

   f. On the **Tenant Permissions** page, set role permissions.


      .. figure:: /_static/images/en-us_image_0000001657091157.png
         :alt: **Figure 9** Role permissions

         **Figure 9** Role permissions

      After the setting is complete, you can view the created role on the **Roles** page.

#. Map a user with a role to bind them.

   a. Select **Roles** from the **Security** drop-down list box.

   b. On the **Roles** page, select the role to be mapped. The role mapping page is displayed.

      |image1|

   c. On the **Mapped users** tab page, click **Map users** and select the user to be mapped from the **users** drop-down list box.

      |image2|

   d. Click **Map**.

   e. After the configuration is complete, you can check whether the configuration takes effect in OpenSearch Dashboards.

.. |image1| image:: /_static/images/en-us_image_0000001607933650.png
.. |image2| image:: /_static/images/en-us_image_0000001607935630.png
