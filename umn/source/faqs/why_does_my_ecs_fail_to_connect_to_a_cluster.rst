:original_name: css_02_0025.html

.. _css_02_0025:

Why Does My ECS Fail to Connect to a Cluster?
=============================================

Perform the following steps:

#. Check whether the ECS instance and cluster are in the same VPC.

   -  If they are, go to :ref:`2 <css_02_0025__li47021920155415>`.
   -  If they are not, create an ECS instance and ensure that the ECS instance is in the same VPC as the cluster.

#. .. _css_02_0025__li47021920155415:

   View the security group rule setting of the cluster to check whether port **9200** (TCP protocol) is allowed or port **9200** is included in the port range allowed in both the outbound and inbound directions.

   -  If it is allowed, go to :ref:`3 <css_02_0025__li770210445265>`.
   -  If it is not allowed, switch to the VPC management console and configure the security group rule of the cluster to allow port **9200** in both the outbound and inbound directions.

#. .. _css_02_0025__li770210445265:

   Check whether the ECS instance has been added to a security group.

   -  If the instance has been added to a security group, check whether the security group configuration rules meet requirements. For details, see the description of **Security Group** in the cluster information table in **Clusters**. Then go to :ref:`4 <css_02_0025__li12702114432619>`.


      .. figure:: /_static/images/en-us_image_0000001286116622.png
         :alt: **Figure 1** Viewing security group information


         **Figure 1** Viewing security group information

   -  If the instance has not been added to the security group, go to the VPC page from the ECS instance details page, select a security group, and add the ECS to the group.

#. .. _css_02_0025__li12702114432619:

   Check whether the ECS instance can connect to the cluster.

   **ssh** *<Private network address and port number of a node>*

   .. note::

      If the cluster contains multiple nodes, check whether the ECS can be connected to each node in the cluster.

   -  If the connection is normal, the network is running properly.
   -  If the ECS still cannot connect to the DB instance port, contact technical support.
