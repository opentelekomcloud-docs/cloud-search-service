:original_name: css_01_0072.html

.. _css_01_0072:

Creating IAM Users and Granting Them Permissions to Use CSS
===========================================================

You can use `Identity and Access Management (IAM) <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0026.html>`__ for fine-grained permissions control for CSS. With IAM, you can:

-  Create IAM users for employees based on your enterprise's organizational structure. Each IAM user has their own identity credentials for accessing CSS resources.
-  Grant users only the permissions required to perform a given task based on their job responsibilities.
-  Entrust an account or a cloud service to perform efficient O&M on your CSS resources.

If your account does not require individual IAM users, you may skip this section.

This section describes the procedure for granting permissions.

Prerequisites
-------------

You know what permissions to assign to which users. CSS supports administrator permissions and read-only permissions. For details, see Permissions Management.

Process Flow
------------


.. figure:: /_static/images/en-us_image_0000001938218776.png
   :alt: **Figure 1** Process of granting CSS permissions

   **Figure 1** Process of granting CSS permissions

#. .. _css_01_0072__li109582711173:

   `Create a user group and assign permissions <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0030.html>`__.

   Create a user group on the IAM console, and assign the **CSS ReadOnlyAccess** permission to the group.

#. `Create an IAM user and add it to a user group <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0031.html>`__.

   Create a user on the IAM console and add it to the user group created in :ref:`1 <css_01_0072__li109582711173>`.

   By adding a user to a user group, you assign all the permissions that this user group has to that user. All users in a group have the same permissions.

#. `Log in <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0032.html>`__ and verify permissions.

   Log in to the console as the created user, switch to the authorized region, and verify the permissions.

   -  Choose **Service List** > **Cloud Search Service**. Then click **Create Cluster** on the CSS console. If the cluster cannot be purchased (assuming that the current permissions include only **CSS ReadOnlyAccess**), the **CSS ReadOnlyAccess** policy has already taken effect.
   -  Choose any other service from **Service List**. (Assume that the current policy contains only **CSS ReadOnlyAccess**.) If a message appears indicating insufficient permissions to access the service, the **CSS ReadOnlyAccess** policy has already taken effect.

Examples of CSS Custom Policies
-------------------------------

Custom policies can be created to supplement the system-defined policies of CSS. For the actions supported for custom policies, see section "Permissions Policies and Supported Actions" in the *Cloud Search Service API Reference*.

You can create custom policies in either of the following ways:

-  Visual editor: Select cloud services, actions, resources, and request conditions. This does not require knowledge of policy syntax.
-  JSON: Create a JSON policy or edit an existing one.

For details about how to create custom policies, see `Creating a Custom Policy <https://docs.otc.t-systems.com/identity-access-management/umn/user_guide/permissions/creating_a_custom_policy.html>`__. The following provides examples of custom CSS policies.

.. note::

   the IAM permissions and data plane cluster permissions of CSS are managed separately. To enhance data-plane security, you need to use the security mode.

   To let an IAM user access an OBS bucket, you need to grant the **GetBucketStoragePolicy**, **GetBucketLocation**, **ListBucket**, and **ListAllMyBuckets** permissions to the user.

-  Example 1: Allowing users to create CSS clusters

   .. code-block::

      {
          "Version": "1.1",
          "Statement": [
              {
                  "Action": [
                      "css:cluster:create",
                      "vpc:securityGroups:get",
                      "vpc:securityGroups:create",
                      "vpc:securityGroups:delete",
                      "vpc:securityGroupRules:get",
                      "vpc:securityGroupRules:create",
                      "vpc:securityGroupRules:delete",
                      "vpc:vpcs:list",
                      "vpc:privateIps:list",
                      "vpc:ports:get",
                      "vpc:ports:create",
                      "vpc:ports:update",
                      "vpc:ports:delete",
                      "vpc:quotas:list",
                      "vpc:subnets:get",
                      "ecs:cloudServerFlavors:get",
                      "ecs:serverInterfaces:use",
                      "ecs:cloudServers:addNics",
                      "ecs:quotas:get",
                      "evs:types:get",
                      "evs:quotas:get"
                  ],
                  "Effect": "Allow"
              }
          ]
      }

-  Example 2: Denying cluster deletion

   A policy with only **Deny** permissions must be used in conjunction with other policies for it to take effect. If the permissions assigned to a user contain both **Allow** and **Deny**, the **Deny** permissions take precedence over the **Allow** permissions.

   The following method can be used if you need to assign permissions of the **CSS Admin** policy to a user but you want to prevent the user from deleting clusters. Create a custom policy for denying cluster deletion, and attach both policies to the group to which the user belongs. Then, the user can perform all operations on CSS except deleting clusters. The following is an example of a deny policy:

   .. code-block::

      {
            "Version": "1.1",
            "Statement": [
                  {
          "Effect": "Deny",
                        "Action": [
                              "css:cluster:delete"
                        ]
                  }
            ]
      }

-  Example 3: Defining permissions for multiple services in a policy

   A custom policy can contain the actions of multiple services that are of the global or project-level type. Example of a policy containing multiple actions:

   .. code-block::

      {
          "Version": "1.1",
          "Statement": [
              {
                  "Action": [
                      "ecs:cloudServers:resize",
                      "ecs:cloudServers:delete",
                      "ecs:cloudServers:delete",
                      "css:cluster:restart",
                      "css:*:get*",
                      "css:*:list*"
                  ],
                  "Effect": "Allow"
              }
          ]
      }
