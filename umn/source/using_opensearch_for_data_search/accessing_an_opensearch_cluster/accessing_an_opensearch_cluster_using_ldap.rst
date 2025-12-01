:original_name: css_01_0248.html

.. _css_01_0248:

Accessing an OpenSearch Cluster Using LDAP
==========================================

The Light Directory Access Protocol (LDAP) is a lightweight version of the directory access protocol based on the X.500 standard. An LDAP service provides user authentication and authorization. Using the Security plugin for Open Distro for Elasticsearch, CSS adds Active Directory as an authentication backend for clusters, connecting them seamlessly to the LDAP service. This topic describes the steps needed to connect a CSS cluster to an LDAP service.

It also describes how to enable LDAP authentication for an OpenSearch cluster to allow access by LDAP users of specific roles.

Preparations
------------

-  A security-mode OpenSearch cluster has been created in CSS and its status is available.
-  The LDAP service that is in the same VPC as the OpenSearch cluster and the necessary user data have been prepared. For details, see `the OpenLDAP document: A Quick-Start Guide <https://www.openldap.org/doc/admin24/quickstart.html>`__.

Accessing a Cluster
-------------------

#. Install an LDAP service on an ECS. If the LDAP service and user data have already been prepared, skip this step.

   a. Create an ECS. The ECS must run a Windows OS and must be in the same VPC and security group as the security-mode Elasticsearch cluster of CSS. The Windows Server running on the ECS provides the built-in Active Directory service that supports the LDAP protocol.
   b. Log in to the ECS, and enable the Active Directory service. Create a domain, administrator, users, and user groups.

#. Modify the parameter settings of the security-mode OpenSearch cluster on CSS. Configure a static parameter in **opensearch.yml** to connect the cluster to the LDAP service.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.

   c. In the cluster list, click the name of the target cluster. The cluster information page is displayed.

   d. Choose **Cluster Settings** > **Parameter Settings**, and click **Edit**. Expand **Custom**, and add the following parameter and value.

      -  **Parameter**: plugins.security.unsupported.restapi.allow_securityconfig_modification
      -  **Value**: true

   e. Click **Submit** above. In the displayed **Submit Configuration** dialog box, select the box that says "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

      If **Status** is **Succeeded** in the parameter change list, the change has been saved. Up to 20 change records can be displayed.

   f. After the changes are saved, click **Restart** in the upper right corner to restart the cluster, thus applying the changes.

      -  You need to restart the cluster after the change, or **Configuration not updated** will be displayed in the **Task Status** column in the cluster list.
      -  If you restart the cluster after the change, and **Task Status** displays **Configuration error** in the cluster list, the parameter configuration file has failed to be modified.

#. Configure a route for an OpenSearch cluster on the CSS console to connect the cluster to the LDAP service.

   a. On the cluster information page, click the **Overview** tab.
   b. In the **Configuration** area, click **Add Route** next to **Cluster Route**.
   c. In the displayed dialog box, configure the route information.

      .. table:: **Table 1** Adding a route

         +-------------+---------------------------------------------------------------------------------------------------------------------+
         | Parameter   | Description                                                                                                         |
         +=============+=====================================================================================================================+
         | IP Address  | Enter the IP address of the LDAP server. If the LDAP service on the ECS is used, enter the IP address of the ECS.   |
         +-------------+---------------------------------------------------------------------------------------------------------------------+
         | Subnet Mask | Enter the subnet mask of the LDAP server. If the LDAP service on the ECS is used, enter the subnet mask of the ECS. |
         +-------------+---------------------------------------------------------------------------------------------------------------------+

   d. Click OK.

#. Configure LDAP authentication for a security-mode OpenSearch cluster.

   a. On the cluster information page, click **Dashboards** in the upper-right corner to log in to OpenSearch Dashboards.

   b. On OpenSearch Dashboards, expand the menu in the upper-left corner, and choose **Dev Tools**.

   c. Run the following commands to configure LDAP authentication.

      .. note::

         -  Concepts used in an X.500 directory access protocol (including LDAP):

            -  CN = Common Name
            -  OU = Organizational Unit
            -  DC = Domain Component
            -  DN = Distinguished Name

            The CN, OU, and DC must be provided in the correct order. Otherwise, authentication will fail.

         -  The configuration file consists of two parts: **authc** and **authz**.

            -  **authc** (authentication): verifies whether a user is truly who they claim they are (password verification).
            -  **authz** (authorization): verifies what the current user has access to.

      .. code-block:: text

         PUT _plugins/_security/api/securityconfig/config
         {
             "dynamic": {
                 "authc": {
                     "basic_internal_auth_domain": {
                         "description": "Authenticate via HTTP Basic against internal users database",
                         "http_enabled": true,
                         "transport_enabled": true,
                         "order": 1,
                         "http_authenticator": {
                             "type": "basic",
                             "challenge": true
                         },
                         "authentication_backend": {
                             "type": "intern"
                         }
                     },
                     "ldap": {
                         "description": "Authenticate via LDAP or Active Directory",
                         "http_enabled": true,
                         "transport_enabled": true,
                         "order": 2,
                         "http_authenticator": {
                             "type": "basic",
                             "challenge": false
                         },
                         "authentication_backend": {
                             "type": "ldap",
                             "config": {
                                 "enable_ssl": false,
                                 "enable_start_tls": false,
                                 "enable_ssl_client_auth": false,
                                 "verify_hostnames": true,
                                 "hosts": ["10.0.XXX.XXX:389"],
                                 "bind_dn": "CN=adminAD,DC=test,DC=ldap,DC=com",
                                 "password": "<password>",
                                 "userbase": "OU=ITDepartment,DC=test,DC=ldap,DC=com",
                                 "usersearch": "(sAMAccountName={0})",
                                 "username_attribute": "uid"
                             }
                         }
                     }
                 },
                 "authz": {
                     "roles_from_myldap": {
                         "description": "Authorize via LDAP or Active Directory",
                         "http_enabled": true,
                         "transport_enabled": true,
                         "authorization_backend": {
                             "type": "ldap",
                             "config": {
                                 "enable_ssl": false,
                                 "enable_start_tls": false,
                                 "enable_ssl_client_auth": false,
                                 "verify_hostnames": true,
                                 "hosts": ["10.0.XXX.XXX:389"],
                                 "bind_dn": "CN=adminAD,DC=test,DC=ldap,DC=com",
                                 "password": "<password>",
                                 "rolebase": "OU=groups,DC=test,DC=ldap,DC=com",
                                 "rolesearch": "(member={0})",
                                 "userroleattribute": null,
                                 "userrolename": "disabled",
                                 "rolename": "CN",
                                 "resolve_nested_roles": true,
                                 "userbase": "OU=ITDepartment,DC=test,DC=ldap,DC=com",
                                 "usersearch": "(uid={0})"
                             }
                         }
                     }
                 }
             }
         }

      The parameters in :ref:`Table 2 <en-us_topic_0000002003441200__en-us_topic_0000001934179690_table111741414338>` need to be modified based on the actual environment.

      .. _en-us_topic_0000002003441200__en-us_topic_0000001934179690_table111741414338:

      .. table:: **Table 2** Parameter description

         +-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter | Description                                                                                                                                                                |
         +===========+============================================================================================================================================================================+
         | hosts     | Address of the LDAP service. The port number is 389. If the LDAP service on the ECS is used, enter the IP address of the ECS.                                              |
         +-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | bind_dn   | It is similar to the LDAP user name (CN - OU - DC) and is used to access the LDAP server. Select a user name from the user data of the LDAP service.                       |
         +-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | password  | Password of the LDAP user configured using **bind_dn**.                                                                                                                    |
         +-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | userbase  | After the LDAP service is connected, the DN that the user belongs to is obtained. In this example, all user information in the **ITDepartment** directory is synchronized. |
         +-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | rolebase  | The collection of permissions that can be configured for the **userbase** user group of the LDAP service.                                                                  |
         +-----------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#. Configure the mapping between LDAP user permissions and OpenSearch permissions in the OpenSearch security-mode cluster to enable fine-grained access control.

   The rolebase permissions group of the LDAP server must be mapped to the roles in the OpenSearch cluster. :ref:`Figure 1 <en-us_topic_0000002003441200__fig196302320392>` illustrates the mapping. For details about the configuration, see :ref:`Creating Users for an OpenSearch Cluster and Granting Cluster Access <css_01_0329>`.

   .. _en-us_topic_0000002003441200__fig196302320392:

   .. figure:: /_static/images/en-us_image_0000002003441216.png
      :alt: **Figure 1** Permissions mapping

      **Figure 1** Permissions mapping

   a. On OpenSearch Dashboards, expand the menu in the upper-left corner, and choose **Security**. The **Security** page is displayed.

   b. .. _en-us_topic_0000002003441200__li12898131717474:

      Click **Roles** to go to the Open Distro Security Roles page. Click **Create Role**, set **Name**, **Cluster Permissions**, **Index Permissions**, and **Tenant Permissions**. Then click **Save Role Definition** to save the role settings. The parameters are as follows:

      -  Name (name of the role)
      -  Cluster Permissions
      -  Index permissions
      -  Tenant permissions

   c. Click the newly created role, select **Mapped users**, enter a permissions group of the LDAP service in **Backend roles**, and click **Map**.

   d. .. _en-us_topic_0000002003441200__li1408144916524:

      Check the configuration result.


      .. figure:: /_static/images/en-us_image_0000002039680337.png
         :alt: **Figure 2** Permissions mapping

         **Figure 2** Permissions mapping

   e. Repeat :ref:`5.b <en-us_topic_0000002003441200__li12898131717474>` to :ref:`5.d <en-us_topic_0000002003441200__li1408144916524>` to map other permissions groups.

#. Log in to OpenSearch Dashboards using the LDAP user to verify the configuration.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch**.

   c. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column. Use the LDAP user to log in to OpenSearch Dashboards.

      If the login is successful, the configuration is successful, and users can access the OpenSearch cluster through LDAP. The specific permissions authorized are controlled by role permissions configured in OpenSearch.
