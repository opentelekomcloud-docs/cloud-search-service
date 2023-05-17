:original_name: css_03_0055.html

.. _css_03_0055:

Concepts
========

-  Account

   An account is created after you register with the cloud platform. It has full access permissions on its resources and cloud services, such as resetting password and granting permissions. The account is a payment entity and should not be used to perform routine management. For security purposes, create IAM users and grant them permissions for routine management.

-  User

   An IAM user is created using an account to use cloud services. Each IAM user has their own identity credentials (password and access keys).

   API authentication requires information such as the account name, username, and password.

-  Region

   A region is a geographic area in which cloud resources are deployed. Availability zones (AZs) in the same region can communicate with each other over an intranet, while AZs in different regions are isolated from each other. By creating cloud resources in different regions, you can design applications to better meet customer requirements and comply with local laws and regulations.

-  AZ

   An AZ comprises of one or multiple physical data centers equipped with independent ventilation, fire, water, and electricity facilities. Computing, network, storage, and other resources in an AZ are logically divided into multiple clusters. AZs within a region are interconnected using high-speed optical fibers to allow you to build cross-AZ high-availability systems.

-  Project

   Projects group and isolate resources (including compute, storage, and network resources) across physical regions. A default project is provided for each region, and subprojects can be created under each default project. Users can be granted permissions to access all resources in a specific project. If you need more refined access control, create sub-projects under a default project and purchase resources in sub-projects. Then you can assign users the permissions required to access only the resources in the specific sub-projects.


   .. figure:: /_static/images/en-us_image_0000001504150288.gif
      :alt: **Figure 1** Project isolation model

      **Figure 1** Project isolation model

-  Checkpoint: When an application consumes data, the latest SN of the consumed data is recorded as a checkpoint. When the data is consumed again, the consumption can be continued based on this checkpoint.

-  APP: Multiple applications can access data in the same stream. Checkpoints generated for each application are used to record the consumed data in the stream by each application.
