:original_name: en-us_topic_0000001477297358.html

.. _en-us_topic_0000001477297358:

How Do I Set the Numbers of Index Copies to 0 in Batches?
=========================================================

#. Log in to the Kibana page of the cluster. In the navigation pane, choose **Dev Tools**.
#. Modify and run the **PUT /*/_settings{"number_of_replicas":0}** command.

   .. note::

      Do not directly run the preceding command, because the asterisk (``*``) may match security indexes. You are advised to specify the index required for the batch operation. Example: **PUT /test*/_settings{"number_of_replicas":0}**
