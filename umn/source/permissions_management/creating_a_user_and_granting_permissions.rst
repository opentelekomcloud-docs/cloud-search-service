:original_name: css_01_0072.html

.. _css_01_0072:

Creating a User and Granting Permissions
========================================

This section describes how to use a group to grant permissions to a user. :ref:`Figure 1 <css_01_0072__en-us_topic_0000001223594424_fig342064620244>` shows the process for granting permissions.

CSS has two types of user permissions: CSS administrator permission and read-only permission.

Prerequisites
-------------

Before assigning permissions to user groups, you have learned about the system policies listed in Permissions Management.

Process Flow
------------

.. _css_01_0072__en-us_topic_0000001223594424_fig342064620244:

.. figure:: /_static/images/en-us_image_0000001667002486.png
   :alt: **Figure 1** Process of granting CSS permissions

   **Figure 1** Process of granting CSS permissions

#. .. _css_01_0072__en-us_topic_0000001223594424_li1157731913917:

   `Create a user group and assign permissions <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0030.html>`__.

   Create a user group on the IAM console, and assign the CSS permission to the group.

#. `Create an IAM user and add it to a user group <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0031.html>`__.

   Create a user on the IAM console and add the user to the group created in :ref:`1. Create a user group and assign permissions <css_01_0072__en-us_topic_0000001223594424_li1157731913917>`.

#. `Log in <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0032.html>`__ and verify permissions.

   In the authorized region, perform the following operations:

   -  Choose **Service List** > **Cloud Search Service**. Then click **Create Cluster** on the CSS console. If the cluster cannot be bought (assuming that the current permissions include only **CSS ReadOnlyAccess**), the **CSS ReadOnlyAccess** policy has already taken effect.
   -  Choose another service from **Service List**. If a message appears indicating that you have insufficient permissions to access the service (assuming that the current policy contains only **CSS ReadOnlyAccess**), the **ECS ReadOnlyAccess** policy is in effect.
