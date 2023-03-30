:original_name: css_01_0109.html

.. _css_01_0109:

Creating a User and Granting Permissions by Using Kibana
========================================================

Prerequisites
-------------

The security mode has been enabled for the cluster.

Procedure
---------

.. note::

   This section takes Kibana 7.6.2 as an example to describe the procedure.

#. Log in to the CSS management console.

#. Click **Access Kibana** in the **Operation** column of a cluster.


   .. figure:: /_static/images/en-us_image_0000001474725864.png
      :alt: **Figure 1** Logging in to Kibana (1)

      **Figure 1** Logging in to Kibana (1)

#. Log in to Kibana.


   .. figure:: /_static/images/en-us_image_0000001525365849.png
      :alt: **Figure 2** Logging in to Kibana (2)

      **Figure 2** Logging in to Kibana (2)

   -  Username: **admin**
   -  **Password**: Enter the password set during cluster creation.

#. Click the **Security** icon on the Kibana operation page.


   .. figure:: /_static/images/en-us_image_0000001474406052.png
      :alt: **Figure 3** Going to the Security page

      **Figure 3** Going to the Security page

#. Create a user.

   a. Choose **Authentication Backends** >\ **Internal Users Database**.


      .. figure:: /_static/images/en-us_image_0000001525365845.png
         :alt: **Figure 4** Adding a user (1)

         **Figure 4** Adding a user (1)

   b. On the **Internal Users Database** page, choose |image1|. The page for adding user information is displayed.


      .. figure:: /_static/images/en-us_image_0000001474406056.png
         :alt: **Figure 5** Adding a user (2)

         **Figure 5** Adding a user (2)

   c. On the user creation page, configure **Username** and **Password**, and click **Submit**.

      The user will be displayed in the user list.

#. Configure roles and permissions for the user.

   a. Click **Roles**.


      .. figure:: /_static/images/en-us_image_0000001524766313.png
         :alt: **Figure 6** Adding a role

         **Figure 6** Adding a role

   b. On the **Open Distro Security Roles** page, click |image2|.

      #. Enter a role name on the **Overview** page.


         .. figure:: /_static/images/en-us_image_0000001524766321.png
            :alt: **Figure 7** Entering a role name

            **Figure 7** Entering a role name

      #. Configure CSS cluster permissions on the **Cluster Permissions** page. You can skip this step.

      #. Configure index permissions on the **Index Permissions** page.

         **Index patterns**: Set this parameter to the name of the index whose permission needs to be configured. For example, **my_store**.

         .. note::

            Use different names for the index and the user.

         Configure **Permissions: Action Groups** as required, for example, select the read-only permission **Search**.

      #. Retain the default settings on the **Tenant Permissions** page.

         After the configuration is complete, the role will be displayed.

#. Assign a role to the user.

   a. Click **Role Mappings**.


      .. figure:: /_static/images/en-us_image_0000001474246400.png
         :alt: **Figure 8** Role mapping

         **Figure 8** Role mapping

   b. Click |image3| to add the mapping between users and roles.


      .. figure:: /_static/images/en-us_image_0000001474725872.png
         :alt: **Figure 9** Users and roles

         **Figure 9** Users and roles

   c. Click **Submit**.

#. Verify that the configuration takes effect in Kibana.

.. |image1| image:: /_static/images/en-us_image_0000001474566028.png
.. |image2| image:: /_static/images/en-us_image_0000001474566028.png
.. |image3| image:: /_static/images/en-us_image_0000001474566028.png
