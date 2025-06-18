:original_name: css_01_0452.html

.. _css_01_0452:

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

      For how to create an ECS, see .

   b. Log in to the ECS, and enable the Active Directory service. Create a domain, administrator, users, and user groups.

#. Modify the parameter settings of the security-mode OpenSearch cluster on CSS. Configure a static parameter in **elasticsearch.yml** to connect the cluster to the LDAP service.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch** to go to the cluster list.

   c. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster. The cluster information page is displayed.

   d. In the navigation pane on the left, choose **Parameter Configurations**. Click **Edit**, and add the following to the **Custom** module:

      -  **Parameter**: plugins.security.unsupported.restapi.allow_securityconfig_modification
      -  **Value**: true

   e. Click **Submit** above. In the displayed **Submit Configuration** dialog box, select the box that says "I understand that the modification will take effect after the cluster is restarted." and click **Yes**.

      If **Status** is **Succeeded** in the parameter change list, the change has been saved. Up to 20 change records can be displayed.

   f. Return to the cluster list and choose **More** > **Restart** in the **Operation** column to restart the cluster and make the change take effect.

      -  You need to restart the cluster after modification, or **Configuration not updated** will be displayed in the **Task Status** column on the **Clusters** page.
      -  If the cluster is restarted after the change, and **Task Status** still shows **Configuration error**, the parameter configuration file has failed to be modified.

#. Configure a custom route for the cluster on the CSS console to connect the cluster to the LDAP service.

   .. important::

      The permission to configure custom routes for clusters is controlled using a whitelist. If you need this permission, submit a service ticket to apply for it.

   a. Log in to the CSS management console.
   b. In the navigation pane on the left, choose **Clusters**, and click a cluster type to go to the cluster list (Elasticsearch in this example).
   c. Choose **Clusters** in the navigation pane. On the **Clusters** page, click the name of the target cluster. The cluster information page is displayed.
   d. On the Cluster Information page, locate **Cluster Routing**, and click **Modify**.

      -  **IP Address**: Enter the IP address of the LDAP server. If the LDAP service on the ECS is used, enter the IP address of the ECS. **Subnet Mask**: Enter the subnet mask of the LDAP server. If the LDAP service on the ECS is used, enter the subnet mask of the ECS.
      -  **Modification Type**: Select **Add**.

   e. Click **OK**.

#. Configure LDAP authentication for a security-mode OpenSearch cluster.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch** to go to the cluster list.

   c. In the cluster list, locate the target cluster, and click **Kibana** in the **Operation** column.

   d. On the OpenSearch Dashboards console, click **Dev Tools** in the navigation tree on the left.

   e. Run the following commands to configure LDAP authentication.

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

      The parameters in :ref:`Table 1 <css_01_0452__en-us_topic_0000001934179690_table111741414338>` need to be modified based on the actual environment.

      .. _css_01_0452__en-us_topic_0000001934179690_table111741414338:

      .. table:: **Table 1** Parameter description

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

   The rolebase permissions group of the LDAP server must be mapped to the roles in the OpenSearch cluster. :ref:`Figure 1 <css_01_0452__fig196302320392>` illustrates the mapping. For details about the configuration, see :ref:`Creating Users for an OpenSearch Cluster and Granting Cluster Access <css_01_0329>`.

   .. _css_01_0452__fig196302320392:

   .. figure:: /_static/images/en-us_image_0000002003441216.png
      :alt: **Figure 1** Permissions mapping

      **Figure 1** Permissions mapping

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch** to go to the cluster list.

   c. In the cluster list, locate the target cluster, and click **Kibana** in the **Operation** column. Log in to OpenSearch Dashboards as user admin.

   d. Choose **Security** in the navigation tree on the left. The **Security** page is displayed.

   e. .. _css_01_0452__li12898131717474:

      Click **Roles** to go to the Open Distro Security Roles page. Click **Create Role**, set **Name**, **Cluster Permissions**, **Index Permissions**, and **Tenant Permissions**. Then click **Save Role Definition** to save the role settings. The parameters are as follows:

      -  Name (name of the role)
      -  Cluster Permissions
      -  Index permissions
      -  Tenant permissions

   f. Click the newly created role, select **Mapped users**, enter a permissions group of the LDAP service in **Backend roles**, and click **Map**.

   g. .. _css_01_0452__li1408144916524:

      Check the configuration result.


      .. figure:: /_static/images/en-us_image_0000002039680337.png
         :alt: **Figure 2** Permissions mapping

         **Figure 2** Permissions mapping

   h. Repeat :ref:`5.e <css_01_0452__li12898131717474>` to :ref:`5.g <css_01_0452__li1408144916524>` to map other permissions groups.

#. Verify the result.

   a. Log in to the CSS management console.

   b. In the navigation pane on the left, choose **Clusters > OpenSearch** to go to the cluster list.

   c. In the cluster list, locate the target cluster, and click **Kibana** in the **Operation** column. Use an LDAP user to log in to the OpenSearch Dashboards page.

      If the login is successful, the configuration is successful, and users can access the OpenSearch cluster through LDAP. The specific permissions authorized are controlled by role permissions configured in OpenSearch.
