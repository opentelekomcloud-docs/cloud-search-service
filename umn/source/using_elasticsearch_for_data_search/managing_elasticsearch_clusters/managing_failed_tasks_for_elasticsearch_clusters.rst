:original_name: css_01_0060.html

.. _css_01_0060:

Managing Failed Tasks for Elasticsearch Clusters
================================================

In the **Failed Tasks** dialog box, you can view the failed tasks related to a cluster, such as failing to create, restart, scale out, back up, or restore a cluster. In addition, you can view the failure cause of each task and choose to delete one or all failed tasks.

Viewing Failed Tasks
--------------------

#. Log in to the CSS management console.

#. Click **Clusters** to switch to the **Clusters** page. Click the digit next to **Failed Tasks** to switch to the **Failed Tasks** dialog box.


   .. figure:: /_static/images/en-us_image_0000001938218564.png
      :alt: **Figure 1** Clicking the digit next to Failed Tasks

      **Figure 1** Clicking the digit next to Failed Tasks

#. In the **Failed Tasks** dialog box, view all failed tasks of the current account. The following information about the failed tasks is displayed: **Name/ID**, **Task Status**, and **Failure Time**.

#. Click the question mark in the **Task Status** column to view the failure cause of a task. You are advised to troubleshoot faults based on failure causes. For details about failure causes, see :ref:`Error Code <css_01_0060__en-us_topic_0000001268594529_section155001521193312>`.


   .. figure:: /_static/images/en-us_image_0000001965416917.png
      :alt: **Figure 2** Viewing the failure cause of a task

      **Figure 2** Viewing the failure cause of a task

Deleting a Failed Task
----------------------

You can delete one or all failed tasks at a time.

-  To delete a failed task, perform the following operations: Locate the row that contains the target task and click **Delete** in the **Operation** column. In the displayed dialog box, confirm the task you want to delete and click **Yes**.
-  To delete all failed tasks, perform the following operations: In the **Failed Tasks** dialog box, click **Delete All**. In the displayed dialog box, confirm the information about all failed tasks and click **Yes**.


.. figure:: /_static/images/en-us_image_0000001938377924.png
   :alt: **Figure 3** Deleting a failed task

   **Figure 3** Deleting a failed task

.. _css_01_0060__en-us_topic_0000001268594529_section155001521193312:

Error Code
----------

.. table:: **Table 1** Failure causes

   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | Error Code            | Failure Cause                                                                                                                                                                                                                   | Solution                                            |
   +=======================+=================================================================================================================================================================================================================================+=====================================================+
   | CSS.6000              | Failed to create the cluster because of an internal error. Please try again later. If the problem persists, contact customer service.                                                                                           | Please try again later or contact customer service. |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6001              | Failed to scale out the cluster because of an internal error. Please try again later. If the problem persists, contact customer service.                                                                                        |                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6002              | Failed to restart the cluster because of an internal error. Please try again later. If the problem persists, contact customer service.                                                                                          |                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6003              | Failed to restore the cluster because of an internal error. Please try again later. If the problem persists, contact customer service.                                                                                          |                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6004              | Failed to create the node because of ECS exceptions (*<ECS error code>*). Please try again later. If the problem persists, contact customer service.                                                                            |                                                     |
   |                       |                                                                                                                                                                                                                                 |                                                     |
   |                       | .. note::                                                                                                                                                                                                                       |                                                     |
   |                       |                                                                                                                                                                                                                                 |                                                     |
   |                       |    *<ECS error code>* indicates the error information reported by ECS. For details about the cause and solution, see `ECS Error Code Description <https://docs.otc.t-systems.com/en-us/api/ecs/en-us_topic_0022067717.html>`__. |                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6005              | Failed to initialize the service because of an internal error. Please try again later. If the problem persists, contact customer service.                                                                                       |                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6007              | Failed to create the snapshot because of an internal error. Please try again later. If the problem persists, contact customer service.                                                                                          |                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6008              | Failed to create the snapshot because the OBS bucket you select does not exist or has been deleted.                                                                                                                             | Modify the OBS bucket.                              |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6009              | Failed to restore the snapshot because the OBS bucket you select does not exist or has been deleted.                                                                                                                            |                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
   | CSS.6010              | Failed to restore the snapshot because the OBS object does not exist or has been deleted.                                                                                                                                       |                                                     |
   +-----------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+-----------------------------------------------------+
