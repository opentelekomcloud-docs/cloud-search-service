:original_name: css_01_0490.html

.. _css_01_0490:

Binding an OpenSearch Cluster to an Enterprise Project
======================================================

You can create enterprise projects based on your organizational structure. Then you can manage resources across different regions by enterprise project, add users and user groups to enterprise projects, and grant different permissions to the users and user groups. This section describes how to bind a CSS cluster to an enterprise project and how to modify an enterprise project.

Prerequisites
-------------

Before binding an enterprise project, you have created an enterprise project.

Binding an Enterprise Project
-----------------------------

When creating a cluster, you can bind an existing enterprise project to the cluster, or click **View Enterprise Project** to go to the enterprise project management console and create a new project or view existing projects.

Modifying an Enterprise Project
-------------------------------

For a cluster that has been created, you can modify its enterprise project based on the site requirements.

#. Log in to the CSS management console.
#. In the navigation pane on the left, select a cluster type. The cluster management page is displayed.
#. In the cluster list on the displayed page, click the target cluster name to switch to the **Cluster Information** page.
#. On the **Cluster Information** page, click the enterprise project name on the right of **Enterprise Project**. The project management page is displayed.
#. On the **Resources** tab page, select the region of the current cluster, and select **CSS** for **Service**. In this case, the corresponding CSS cluster is displayed in the resource list.
#. Select the cluster whose enterprise project you want to modify and click **Remove**.
#. On the **Remove Resource** page, specify **Mode** and select **Destination Enterprise Project**, and click **OK**.
#. After the resource is removed, you can view the modified enterprise project information on the **Clusters** page.
