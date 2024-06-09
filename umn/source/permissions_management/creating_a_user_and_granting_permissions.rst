:original_name: en-us_topic_0000001477419752.html

.. _en-us_topic_0000001477419752:

Creating a User and Granting Permissions
========================================

This section describes how to use a group to grant permissions to a user. :ref:`Figure 1 <en-us_topic_0000001477419752__en-us_topic_0000001223594424_fig342064620244>` shows the process for granting permissions.

CSS has two types of user permissions: CSS administrator permission and read-only permission.

Prerequisites
-------------

Before assigning permissions to user groups, you have learned about the system policies listed in Permissions Management.

Process Flow
------------

.. _en-us_topic_0000001477419752__en-us_topic_0000001223594424_fig342064620244:

.. figure:: /_static/images/en-us_image_0000001575311218.png
   :alt: **Figure 1** Process of granting CSS permissions

   **Figure 1** Process of granting CSS permissions

#. .. _en-us_topic_0000001477419752__en-us_topic_0000001223594424_li1157731913917:

   `Create a user group and assign permissions <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0030.html>`__.

   Create a user group on the IAM console, and assign the CSS permission to the group.

#. `Create an IAM user and add it to a user group <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0031.html>`__.

   Create a user on the IAM console and add the user to the group created in :ref:`1. Create a user group and assign permissions <en-us_topic_0000001477419752__en-us_topic_0000001223594424_li1157731913917>`.

#. `Log in <https://docs.otc.t-systems.com/usermanual/iam/iam_01_0032.html>`__ and verify permissions.

   Log in to the console as the created user, switch to the authorized region, and verify the permissions.

   -  Choose **Service List** > **Cloud Search Service**. Then click **Create Cluster** on the CSS console. If the cluster cannot be bought (assuming that the current permissions include only **CSS ReadOnlyAccess**), the **CSS ReadOnlyAccess** policy has already taken effect.
   -  Choose any other service from **Service List**. (Assume that the current policy contains only **CSS ReadOnlyAccess**.) If a message appears indicating insufficient permissions to access the service, the **CSS ReadOnlyAccess** policy has already taken effect.
