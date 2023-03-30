:original_name: css_01_0086.html

.. _css_01_0086:

CSS Custom Policies
===================

Custom policies can be created to supplement the system-defined policies of CSS. For the actions supported for custom policies, see Permissions Policies and Supported Actions.

You can create custom policies in either of the following ways:

-  Visual editor: Select cloud services, actions, resources, and request conditions. You do not need to have knowledge of the policy syntax.
-  JSON: Create a JSON policy or edit based on an existing policy.

For details about how to create custom policies, see `Creating a Custom Policy <https://docs.otc.t-systems.com/usermanual/iam/en-us_topic_0274187246.html>`__. The following section contains examples of common CSS custom policies.

.. note::

   IAM permissions and data plane cluster permissions are managed separately. To enable the security capability of the data plane, you need to use the security mode.

Example Custom Policies
-----------------------

Example 1: Allowing users to create a CSS cluster

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

Example 2: Denying cluster deletion

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

Example 3: Defining permissions for multiple services in a policy

A custom policy can contain the actions of multiple services that are of the global or project-level type. The following is an example policy containing actions of multiple services:

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
