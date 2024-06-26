:original_name: en-us_topic_0000001528299613.html

.. _en-us_topic_0000001528299613:

Cluster List Overview
=====================

The cluster list displays all CSS clusters. If there are a large number of clusters, these clusters will be displayed on multiple pages. You can view clusters of all statuses from the cluster list.

Clusters are listed in chronological order by default in the cluster list, with the most recent cluster displayed at the top. :ref:`Table 1 <en-us_topic_0000001528299613__en-us_topic_0000001223754404_table163431019544>` shows the cluster parameters.

In the upper right corner of the cluster list, you can enter the cluster name, or cluster ID and click |image1| to search for a cluster. You can also click |image2| in the upper right corner to refresh the cluster list. Click |image3| to download the cluster list.

.. _en-us_topic_0000001528299613__en-us_topic_0000001223754404_table163431019544:

.. table:: **Table 1** Cluster list parameter description

   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter               | Description                                                                                                                                                                                                               |
   +=========================+===========================================================================================================================================================================================================================+
   | Name/ID                 | Name and ID of a cluster. You can click a cluster name to switch to the **Basic Information** page. The cluster ID is automatically generated by the system and uniquely identifies a cluster.                            |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Cluster Status          | Status of a cluster. For details about the cluster status, see :ref:`Viewing the Cluster Runtime Status and Storage Capacity Status <en-us_topic_0000001477579368>`.                                                      |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Task Status             | Status of a task, such as cluster restart, cluster capacity expansion, cluster backup, and cluster restoration.                                                                                                           |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Version                 | Elasticsearch version of the cluster.                                                                                                                                                                                     |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Created                 | Time when the cluster is created.                                                                                                                                                                                         |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Enterprise Project      | Enterprise project that a cluster belongs to.                                                                                                                                                                             |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Private Network Address | Private network address and port number of the cluster. You can use these parameters to access the cluster. If the cluster has multiple nodes, the private network addresses and port numbers of all nodes are displayed. |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Billing Mode            | Billing mode of a cluster.                                                                                                                                                                                                |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Operation               | Operations that can be performed on a cluster, including accessing Kibana, checking metrics, restarting a cluster, and deleting a cluster. If an operation is not allowed, the button is gray.                            |
   +-------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. |image1| image:: /_static/images/en-us_image_0000001575471322.png
.. |image2| image:: /_static/images/en-us_image_0000001625790509.png
.. |image3| image:: /_static/images/en-us_image_0000001625870985.png
