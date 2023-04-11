:original_name: css_03_0065.html

.. _css_03_0065:

Permissions Policies and Supported Actions
==========================================

This section describes fine-grained permissions management for your CSS. If your account does not need individual IAM users, then you may skip over this chapter.

By default, new IAM users do not have any permissions assigned. You need to add a user to one or more groups, and assign permissions policies to these groups. Users inherit permissions from the groups to which they are added and can perform specified operations on cloud services based on the permissions.

You can grant users permissions by using roles and policies. Roles are a type of coarse-grained authorization mechanism that defines permissions related to user responsibilities. Policies define API-based permissions for operations on specific resources under certain conditions, allowing for more fine-grained, secure access control of cloud resources.

.. note::

   Policy-based authorization is useful if you want to allow or deny the access to an API.

An account has all the permissions required to call all APIs, but IAM users must be assigned the required permissions. The permissions required for calling an API are determined by the actions supported by the API. Only users who have been granted permissions allowing the actions can call the API successfully.

Supported Actions
-----------------

CSS provides system-defined policies that can be directly used in IAM. CSS administrators can create custom policies and use them to supplement system-defined policies, implementing more refined access control. Actions supported by policies are specific to APIs. The following are common concepts related to policies:

-  Permissions: Allow or deny operations on specified resources under specific conditions.
-  APIs: REST APIs that can be called by a custom policy.
-  Actions: added to a custom policy to control permissions for specific operations.
-  Related actions: actions on which a specific action depends to take effect. When assigning permissions for the action to a user, you also need to assign permissions for the dependent actions.
-  IAM or enterprise projects: type of projects for which an action will take effect. Policies that contain actions supporting both IAM and enterprise projects can be assigned to user groups and take effect in both IAM and Enterprise Management. Policies that only contain actions supporting IAM projects can be assigned to user groups and only take effect for IAM.

   .. note::

      The check mark (Y) indicates that an action takes effect. The cross mark (x) indicates that an action does not take effect.

   .. table:: **Table 1** API actions

      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Permission                                                       | API                                                                                | Action                                | IAM Project | Enterprise Project   |
      |                                                                  |                                                                                    |                                       |             |                      |
      |                                                                  |                                                                                    |                                       | (Project)   | (Enterprise Project) |
      +==================================================================+====================================================================================+=======================================+=============+======================+
      | Creating a cluster                                               | POST /v1.0/{project_id}/clusters                                                   | css:cluster:create                    | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Querying a cluster list                                          | GET /v1.0/{project_id}/clusters                                                    | css:cluster:list                      | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Querying cluster details                                         | GET /v1.0/{project_id}/clusters/{cluster_id}                                       | css:cluster:get                       | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Deleting a cluster                                               | DELETE /v1.0/{project_id}/clusters/{cluster_id}                                    | css:cluster:delete                    | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Restarting a cluster                                             | POST /v1.0/{project_id}/clusters/{cluster_id}/restart                              | css:cluster:restart                   | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Scaling out a cluster                                            | POST /v1.0/{project_id}/clusters/{cluster_id}/extend                               | css:cluster:scaleOut                  | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Adding instances and expanding instance storage capacity         | POST /v1.0/{project_id}/clusters/{cluster_id}/role_extend                          | css:cluster:expand                    | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Querying tags of a specified cluster                             | GET /v1.0/{project_id}/css-cluster/{cluster_id}/tags                               | css:tag:get                           | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Automatically setting basic configurations of a cluster snapshot | POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/auto_setting          | css:snapshot:enableAtomaticSnapsot    | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Modifying basic configurations of a cluster snapshot             | POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/setting               | css:snapshot:setSnapshotContiguration | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Setting the automatic snapshot creation policy                   | POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy                | css:snapshot:setSnapshotPolicy        | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Querying the automatic snapshot creation policy                  | GET /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/policy                 | css:snapshot:getSnapshotPolicy        | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Manually creating a snapshot                                     | POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot                       | css:snapshot:create                   | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Querying the snapshot list                                       | GET /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots                       | css:snapshot:list                     | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Restoring a snapshot                                             | POST /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}/restore | css:snapshot:restore                  | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Deleting a snapshot                                              | DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshot/{snapshot_id}       | css:snapshot:delete                   | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
      | Disabling the snapshot function                                  | DELETE /v1.0/{project_id}/clusters/{cluster_id}/index_snapshots                    | css:snapshot:disableSnapshotFuction   | Y           | Y                    |
      +------------------------------------------------------------------+------------------------------------------------------------------------------------+---------------------------------------+-------------+----------------------+
