:original_name: css_02_0034.html

.. _css_02_0034:

What Are Regions and AZs?
=========================

Regions and AZs
---------------

A region and availability zone (AZ) identify the location of a data center. You can create resources in a specific region and AZ.

-  A region is a physical data center. Each region is completely independent, and thereby improves fault tolerance and stability. After a resource is created, its region cannot be changed.
-  An AZ is a physical location using independent power supplies and networks. Faults in an AZ do not affect other AZs. A region can contain multiple AZs that are physically isolated but networked together. This enables low-cost and low-latency network connections.

:ref:`Figure 1 <css_02_0034__fig115516197127>` shows the relationship between regions and AZs.

.. _css_02_0034__fig115516197127:

.. figure:: /_static/images/en-us_image_0000001338716545.png
   :alt: **Figure 1** Regions and AZs

   **Figure 1** Regions and AZs

Region Selection
----------------

You are advised to select a region close to you or your target users. This reduces network latency and improves the access success rate.

AZ Selection
------------

When determining whether to deploy resources in the same AZ, consider your application's requirements for disaster recovery (DR) and network latency.

-  To prioritize DR capabilities, deploy resources in different AZs in the same region.
-  To prioritize network latency, deploy resources in the same AZ.

Regions and Endpoints
---------------------

Before using an API to call resources, you will need to specify the resource region and endpoint. For details about public cloud regions and endpoints, see `Regions and Endpoints <https://docs.otc.t-systems.com/en-us/endpoint/index.html>`__.
