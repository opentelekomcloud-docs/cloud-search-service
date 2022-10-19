:original_name: css_02_0029.html

.. _css_02_0029:

Why Does Index Backup Fail?
===========================

Index backup is implemented by creating cluster snapshots. If index backup fails, perform the following steps:

Check Whether the Account or IAM User Has the Index Backup Permissions
----------------------------------------------------------------------

#. Log in to the IAM management console.

#. Check the user group that the account or the IAM user belongs to.

   For details, see `Viewing or Modifying User Information <https://docs.otc.t-systems.com/en-us/usermanual/iam/en-us_topic_0046661675.html>`__.

#. Check whether the permissions assigned to the user group include the following two permissions: **Tenant Administrator** for project **OBS** in region **Global service** and **CSS Administrator** for the current region.

   For details, see `Viewing and Modifying User Group Information <https://docs.otc.t-systems.com/en-us/usermanual/iam/en-us_topic_0085605493.html>`__.

   -  If neither of the preceding permissions has been assigned, go to :ref:`4 <css_02_0029__li6702956162617>`.
   -  If both the preceding permissions have been assigned to the group, contact technical support.

#. .. _css_02_0029__li6702956162617:

   Add the following permissions to the user group: **Tenant Administrator** for project **OBS** in region **Global service**, and **CSS Administrator** for the current region.

   For details, see `Viewing and Modifying User Group Information <https://docs.otc.t-systems.com/en-us/usermanual/iam/en-us_topic_0085605493.html>`__.
