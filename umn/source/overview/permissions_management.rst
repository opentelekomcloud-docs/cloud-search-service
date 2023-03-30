:original_name: css_04_0014.html

.. _css_04_0014:

Permissions Management
======================

If you need to assign different permissions to employees in your enterprise to access your CSS resources, IAM is a good choice for fine-grained permissions management. IAM provides identity authentication, permissions management, and access control, helping you secure access your resources.

With IAM, you can use your account to create IAM users for your employees, and assign permissions to the users to control their access to specific resource types. For example, you may need to grant some software developers in your enterprise access to CSS resources but do not want them to be able to delete them or perform any high-risk operations. To this end, you can create IAM users for the software developers and grant them only the permissions required for using CSS resources.

If you do not need to create IAM users, you can skip this section.

IAM is a free service. You pay only for the resources in your account.


Permissions Management
----------------------

By default, new IAM users do not have any permissions assigned. You need to add the user to one or more groups, and apply permissions policies or roles to these groups. Users inherit permissions from the groups they are added to and can perform specified operations on cloud services based on these permissions.

CSS is a project-level service deployed in specific physical regions. CSS permissions are assigned to users in specific regions and only take effect for these regions. If you want the permissions to take effect for all regions, you need to assign the permissions to the users in each region. When accessing CSS, the users need to switch to a region where they have been authorized to use cloud services.

You can use roles and policies to grant users permissions.

-  Roles are a type of coarse-grained authorization mechanism that defines permissions related to user responsibilities. There are only a limited number of service-level roles for granting permissions to users. When using roles to grant permissions, you need to also assign other roles on which the permissions depend to take effect. Roles are not ideal for fine-grained authorization and secure access control.
-  Policies are a type of fine-grained authorization mechanism that defines the permissions for performing operations on specific cloud resources under certain conditions. This mechanism allows for more flexible authorization. Policies allow you to meet requirements for more secure access control. For example, CSS administrators can grant CSS users only the permissions needed for managing a certain type of CSS.

:ref:`Table 1 <css_04_0014__en-us_topic_0170096704_table5954195822016>` lists all the system roles supported by CSS. For example, some CSS roles are dependent on the roles of other services. When assigning CSS roles to users, you need to also assign dependent roles for the CSS permissions to take effect.

.. _css_04_0014__en-us_topic_0170096704_table5954195822016:

.. table:: **Table 1** System-defined roles and policies supported by CSS

   +-----------------------------+-----------------------+------------------------------------------------------------------------------------------------+
   | Role Name                   | Description           | Dependency                                                                                     |
   +=============================+=======================+================================================================================================+
   | Elasticsearch Administrator | CSS administrator     | Dependent on the **Tenant Guest** and **Server Administrator** roles.                          |
   |                             |                       |                                                                                                |
   |                             |                       | -  **Tenant Guest**: A global role, which must be assigned in the global project.              |
   |                             |                       | -  **Server Administrator**: A project-level role, which must be assigned in the same project. |
   +-----------------------------+-----------------------+------------------------------------------------------------------------------------------------+

.. table:: **Table 2** Relationship between user permissions and roles

   +-----------------+-----------------------------------------------------------+---------------------+-----------------------------------------------------------------+
   | Permission Type | Description                                               | Type                | Required Role                                                   |
   +=================+===========================================================+=====================+=================================================================+
   | Permission 1    | Permissions:                                              | System-defined role | -  Elasticsearch Administrator                                  |
   |                 |                                                           |                     | -  Server Administrator                                         |
   |                 | -  Creating, deleting, and expanding CSS clusters         |                     | -  Tenant Guest                                                 |
   |                 | -  Manually and automatically backing up CSS cluster data |                     | -  VPC Administrator                                            |
   |                 | -  Restoring CSS cluster data                             |                     | -  Security Administrator                                       |
   |                 | -  Creating an IAM agency                                 |                     | -  OBS Administrator                                            |
   |                 | -  Creating an OBS bucket                                 |                     |                                                                 |
   |                 | -  Creating a VPC and security group                      |                     |                                                                 |
   |                 | -  Kibana                                                 |                     |                                                                 |
   |                 | -  Customizing a word dictionary                          |                     |                                                                 |
   +-----------------+-----------------------------------------------------------+---------------------+-----------------------------------------------------------------+
   | Permission 2    | Permissions:                                              | System-defined role | -  Elasticsearch Administrator                                  |
   |                 |                                                           |                     | -  Server Administrator                                         |
   |                 | -  Creating, deleting, and expanding CSS clusters         |                     | -  Tenant Guest                                                 |
   |                 | -  Manually backing up CSS cluster data                   |                     |                                                                 |
   |                 | -  Restoring CSS cluster data                             |                     |                                                                 |
   |                 | -  Kibana                                                 |                     |                                                                 |
   |                 | -  Customizing a word dictionary                          |                     |                                                                 |
   +-----------------+-----------------------------------------------------------+---------------------+-----------------------------------------------------------------+
   | Permission 3    | Permissions:                                              | System-defined role | This permission is dependent on the **Tenant Guest** role,      |
   |                 |                                                           |                     |                                                                 |
   |                 | -  Viewing the cluster list                               |                     | which must be assigned in the same project as **Permission 3**. |
   |                 | -  Viewing the Overview page                              |                     |                                                                 |
   |                 | -  Kibana                                                 |                     |                                                                 |
   +-----------------+-----------------------------------------------------------+---------------------+-----------------------------------------------------------------+

:ref:`Table 3 <css_04_0014__en-us_topic_0170096704_table680913525437>` lists the common operations supported by each system permission of CSS. Please choose proper system policies according to this table.

.. _css_04_0014__en-us_topic_0170096704_table680913525437:

.. table:: **Table 3** Common operations supported by each system-defined policy

   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Operation                                                        | CSS FullAccess | CSS ReadOnlyAccess | Elasticsearch Administrator | Remarks                            |
   +==================================================================+================+====================+=============================+====================================+
   | Creating a cluster                                               | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Querying a cluster list                                          | Y              | Y                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Querying cluster details                                         | Y              | Y                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Deleting a cluster                                               | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Restarting a cluster                                             | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Expanding cluster capacity                                       | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Adding instances and expanding instance storage capacity         | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Querying tags of a specified cluster                             | Y              | Y                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Querying all tags                                                | Y              | Y                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Loading a custom word dictionary                                 | Y              | x                  | Y                           | Depends on OBS and IAM permissions |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Querying the status of a custom word dictionary                  | Y              | Y                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Deleting a custom word dictionary                                | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Automatically setting basic configurations of a cluster snapshot | Y              | x                  | Y                           | Depends on OBS and IAM permissions |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Modifying basic configurations of a cluster snapshot             | Y              | x                  | Y                           | Depends on OBS and IAM permissions |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Setting the automatic snapshot creation policy                   | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Querying the automatic snapshot creation policy                  | Y              | Y                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Manually creating a snapshot                                     | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Querying the snapshot list                                       | Y              | Y                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Restoring a snapshot                                             | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Deleting a snapshot                                              | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
   | Disabling the snapshot function                                  | Y              | x                  | Y                           | ``-``                              |
   +------------------------------------------------------------------+----------------+--------------------+-----------------------------+------------------------------------+
