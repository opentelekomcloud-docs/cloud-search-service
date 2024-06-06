:original_name: en-us_topic_0000001591298678.html

.. _en-us_topic_0000001591298678:

Creating and Managing Index Policies
====================================

You can manage the indexes of OpenSearch clusters. ISM is a plugin that allows you to automate periodic and administrative operations based on changes on the index age, index size, or number of documents. When using the ISM plug-in, you can define policies that automatically handle index rollovers or deletions based on your needs.

Creating an Index Policy
------------------------

#. Log in to Kibana and choose or **Index Management** on the left. The index management page is displayed.

#. Click **Create policy** to create an index policy.

#. In the **Configuration method** dialog box, select **JSON editor** and click **Continue**. The page for creating an index policy is displayed.

#. Enter a policy ID in the **Policy ID** text box and enter your policy in the **Define policy** text box.


   .. figure:: /_static/images/en-us_image_0000001656290797.png
      :alt: **Figure 1** Configuring a policy

      **Figure 1** Configuring a policy

#. Click **Create**.

Attaching a Policy to an Index
------------------------------

You can attach a policy to one or more indexes and add the policy ID to an index template. When you create indexes using that index template pattern, the policy will be attached to all created indexes.

-  **Method 1: OpenSearch Dashboard CLI**

   On the **Dev Tools** page of the **OpenSearch Dashboards**, run the following command to associate the policy ID with the index template:

   .. code-block:: text

      PUT _template/<template_name>
      {
          "index_patterns": ["index_name-*"],
          "settings": {
              "opendistro.index_state_management.policy_id": "policy_id"
          }
      }

   -  **<template_name>**: Replace it with the name of a created index template.
   -  **policy_id**: Replace it with a custom policy ID.

   For details about how to create an index template, see `Index Templates <https://opendistro.github.io/for-elasticsearch-docs/docs/elasticsearch/index-templates/#create-template>`__.

-  **Method 2: OpenSearch Dashboards Console**

   #. On the **Index Management** page of the **OpenSearch Dashboards**, choose **Indices**.


      .. figure:: /_static/images/en-us_image_0000001607405894.png
         :alt: **Figure 2** Choosing Indices

         **Figure 2** Choosing Indices

   #. In the **Indices** list, select the target index to which you want to attach a policy.

   #. Click **Apply policy** in the upper right corner.


      .. figure:: /_static/images/en-us_image_0000001607890430.png
         :alt: **Figure 3** Adding a policy

         **Figure 3** Adding a policy

   #. Select the policy you created from the **Policy ID** drop-down list.


      .. figure:: /_static/images/en-us_image_0000001606771374.png
         :alt: **Figure 4** Selecting an index policy

         **Figure 4** Selecting an index policy

   #. Click **Apply**.

      After you attach a policy to an index, ISM creates a job that runs every 5 minutes by default, to execute the policy, check conditions, and convert the index to different statuses.

Managing Index Policies
-----------------------

#. On the **Index Management** page of the **OpenSearch Dashboards**, choose **Managed Indices**.

#. If you want to change the policy, click **Change policy**. For details, see :ref:`Changing Policies <en-us_topic_0000001641016221>`.


   .. figure:: /_static/images/en-us_image_0000001657221737.png
      :alt: **Figure 5** Changing policies

      **Figure 5** Changing policies

#. To delete a policy, select your policy, and click **Remove policy**.

#. To retry a policy, select your policy, and click **Retry policy**.

For details, see `Index State Management <https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/>`__.
