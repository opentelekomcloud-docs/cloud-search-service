:original_name: css_02_0043.html

.. _css_02_0043:

How Do I Query Snapshot Information?
====================================

Prerequisites
-------------

The snapshot function has been enabled for the cluster and snapshot information has been configured.

Querying a Snapshot
-------------------

#. Log in to the CSS management console, and click **Clusters** in the navigation pane. On the displayed **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. In the left navigation pane of the Kibana page, click **Dev Tools**. Click **Get to work** to switch to the **Console** page.

   Enter the code as required in the left pane, click |image1| to execute the command, and view the result in the right pane.

#. Run the **GET \_snapshot/_all** command to query information about all repositories.


   .. figure:: /_static/images/en-us_image_0000001527937349.png
      :alt: **Figure 1** Querying information about all repositories

      **Figure 1** Querying information about all repositories

   -  **bucket**: OBS bucket name
   -  **base_path**: Path. It consists of a fixed prefix and a cluster name.
   -  **endpoint**: OBS domain name
   -  **region**: your region

#. Query snapshot information.

   a. Run the **GET \_snapshot/repo_auto/_all** command to query the list of all the snapshots in the current repository.


      .. figure:: /_static/images/en-us_image_0000001476817922.png
         :alt: **Figure 2** Snapshot information

         **Figure 2** Snapshot information

      -  **snapshot**: snapshot name
      -  **state**: snapshot status
      -  **start_time**, **start_time_in_millis**, **end_time**, and **end_time_in_millis**: snapshot time
      -  **shards**: the number of shards. **total** indicates the total number of shards. **failed** indicates the number of failures. **successful** indicates the number of successes.

   b. Run the **GET \_snapshot/repo_auto/$snapshot-xxx** command to query information about a specified snapshot.

      -  Replace **$snapshot-xxx** with the actual snapshot name.
      -  **repo_auto** is followed by a snapshot name or wildcard characters.

#. (Optional) Delete information about a specified snapshot.

   To delete a specific snapshot, run the **DELETE \_snapshot/ repo_auto/$snapshot-xxx** command.

   Replace **$snapshot-xxx** with the actual snapshot name.

.. |image1| image:: /_static/images/en-us_image_0000001477137550.png
