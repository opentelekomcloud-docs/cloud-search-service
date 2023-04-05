:original_name: css_01_0072.html

.. _css_01_0072:

Creating a User and Granting Permissions
========================================

This chapter describes how to use to implement fine-grained permissions control for your CloudSearch Service (CSS) resources. With IAM, you can:

-  Create IAM users for employees based on your enterprise's organizational structure. Each IAM user will have their own security credentials for accessing CSS resources.
-  Grant only the permissions required for users to perform a specific task.
-  Entrust a account or cloud service to perform efficient O&M on your CSS resources.

If your account does not require individual IAM users, skip this chapter.

This section describes the procedure for granting permissions (see :ref:`Figure 1 <css_01_0072__fig342064620244>`).

Prerequisites
-------------

Before assigning permissions to user groups, you should learn about the system policies listed in :ref:`Permissions Management <css_04_0014>`.

Process Flow
------------

.. _css_01_0072__fig342064620244:

.. figure:: /_static/images/en-us_image_0000001554577425.png
   :alt: **Figure 1** Process for granting CSS permissions

   **Figure 1** Process for granting CSS permissions

#. .. _css_01_0072__li8182365323:

   `Create a user group and assign permissions <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0030.html>`__

   Create a user group on the IAM console, and assign the CSS permission to the group.

#. `Create a user and add it to a user group <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0031.html>`__

   Create a user on the IAM console and add the user to the group created in :ref:`1. Create a user group a... <css_01_0072__li8182365323>`.

#. `Log in as an IAM user <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0032.html>`__ and verify permissions.

   Log in to the CSS console as the created user, and verify that it only has read permissions for CSS.
