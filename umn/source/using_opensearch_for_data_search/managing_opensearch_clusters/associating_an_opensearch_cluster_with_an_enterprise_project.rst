:original_name: css_01_0285.html

.. _css_01_0285:

Associating an OpenSearch Cluster with an Enterprise Project
============================================================

In CSS, you can associate your OpenSearch cluster with an enterprise project. You can create enterprise projects based on your organizational structure. Then you can manage resources across different regions by enterprise project, add users and user groups to enterprise projects, and grant different permissions to these users and user groups.

You can associate your cluster with an enterprise project either when creating the cluster or afterward.

Prerequisites
-------------

You have created an enterprise project.

Managing Enterprise Projects
----------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. On the **Overview** tab, find **Enterprise Project** in the **Configuration** area, and click the enterprise project name next to it. The **Project Management** page is displayed.
#. On the **Resources** tab, select the region of the current cluster, and select **CloudSearchService** as **Service**. Then click **Search**. The CSS clusters are displayed in the resource list below.
#. Select the cluster whose enterprise project you want to modify and click **Remove**.
#. In the **Remove Resource** dialog box, specify **Mode** and select **Destination Enterprise Project**. Then click **OK**.
#. After the change is complete, return to the OpenSearch cluster list on the CSS console and check the cluster's new enterprise project.
