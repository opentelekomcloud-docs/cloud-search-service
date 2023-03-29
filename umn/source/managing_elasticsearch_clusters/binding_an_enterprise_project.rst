:original_name: css_01_0058.html

.. _css_01_0058:

Binding an Enterprise Project
=============================

You must configure an enterprise project for each cluster. If you do not need to distinguish enterprise projects for clusters, you can bind clusters to the **default** project. For clusters created before the binding an enterprise project feature was released, their enterprise projects were bound to the **default** project. You can modify the enterprise project based on the site requirements.


Binding an Enterprise Project
-----------------------------

When creating a cluster, you can bind it to an enterprise project by specifying the **Enterprise Project** parameter. For details, see .

Modifying an Enterprise Project
-------------------------------

For a cluster that has been created, you can modify its enterprise project based on the site requirements.

#. On the CSS management console, click **Clusters**.
#. In the cluster list on the displayed page, click the target cluster name to switch to the **Basic Information** page.
#. On the displayed page, click the parameter value on the right of **Enterprise Project**. The **Project Management** page of the **Resource Management** is displayed.
#. On the **Resources** tab page, select the corresponding **Region** and select **Cloud Search Service** from **Service**. In this case, the corresponding CSS cluster is displayed in the resource list.
#. Select the cluster whose enterprise project you want to modify and click **Remove**.
#. On the **Remove Resource** page, specify **Mode** and select **Destination Enterprise Project**, and click **OK**.
#. After you complete the preceding steps, you can view the enterprise project bound to the cluster in either of the following ways:

   -  Switch to the CSS cluster list, where the value of **Enterprise Project** for the cluster is changed to the new enterprise project.
   -  On the **Resource Management** page, click **Project Management** in the navigation pane on the left. On the displayed page, click **View Migration Event** to obtain the cluster information.
