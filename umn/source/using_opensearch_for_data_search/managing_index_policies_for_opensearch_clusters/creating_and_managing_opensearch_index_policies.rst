:original_name: css_01_0319.html

.. _css_01_0319:

Creating and Managing OpenSearch Index Policies
===============================================

This topic describes how to create and manage index lifecycle policies for OpenSearch clusters.

Context
-------

Index State Management (ISM) of OpenSearch is a plugin that allows you to automate periodic, administrative operations on indexes by triggering them based on changes in the index age, index size, or number of documents. With ISM, you can define custom policies to automate index rollovers and deletion, thus optimizing cluster search performance or cutting storage costs. The procedure for using ISM is as follows:

#. :ref:`Creating an Index Lifecycle Policy <en-us_topic_0000001965496865__en-us_topic_0000001477739392_en-us_topic_0000001268154473_section779154094817>`: Create an index lifecycle policy on OpenSearch Dashboards.
#. :ref:`Associating Indexes with a Lifecycle Policy <en-us_topic_0000001965496865__en-us_topic_0000001477739392_en-us_topic_0000001268154473_section11451321182815>`: Associate indexes with a lifecycle policy.
#. :ref:`Managing Index Policies <en-us_topic_0000001965496865__en-us_topic_0000001477739392_en-us_topic_0000001268154473_section87941257192>`: Modify, retry, and change index lifecycle policies.

For more information about ISM, see `Index State Management <https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/>`__.

The OpenSearch Dashboards GUI may vary depending on the software version. OpenSearch Dashboards 1.3.6 is used as an example here.

.. _en-us_topic_0000001965496865__en-us_topic_0000001477739392_en-us_topic_0000001268154473_section779154094817:

Creating an Index Lifecycle Policy
----------------------------------

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.
#. Expand the OpenSearch Dashboards menu in the upper-left corner, and choose **Index Management**.
#. Click **Create policy** to create an index policy. In the **Configuration method** dialog box, select **JSON editor** and click **Continue**. The page for creating an index policy is displayed.

   -  **Policy ID**: use a custom policy name.

   -  **Define policy**: define a custom policy based on the reference example provided.


      .. figure:: /_static/images/en-us_image_0000001999761193.png
         :alt: **Figure 1** Configuring a policy

         **Figure 1** Configuring a policy

#. Click **Create**.

.. _en-us_topic_0000001965496865__en-us_topic_0000001477739392_en-us_topic_0000001268154473_section11451321182815:

Associating Indexes with a Lifecycle Policy
-------------------------------------------

You can bind a policy to one or more indexes, or associate a policy with an index template, so that the policy will be applied to all indexes created using this index template. Use this method when associating existing indexes with a lifecycle policy.

#. On the **Index Management** page of the OpenSearch Dashboards, choose **Indexes**.

#. In the **Indexes** list, select one or more indexes that you want to bind with a policy.

#. Click **Apply policy** in the upper-right corner. In the displayed dialog box, select **Policy ID**.


   .. figure:: /_static/images/en-us_image_0000001938218604.png
      :alt: **Figure 2** Apply policy

      **Figure 2** Apply policy


   .. figure:: /_static/images/en-us_image_0000001963261856.png
      :alt: **Figure 3** Selecting a policy

      **Figure 3** Selecting a policy

#. Click **Apply**.

   After you bind a policy to an index, ISM creates a job that runs every 5 minutes by default to execute the policy, check criteria, and change index states.

.. _en-us_topic_0000001965496865__en-us_topic_0000001477739392_en-us_topic_0000001268154473_section87941257192:

Managing Index Policies
-----------------------

#. On the **Index Management** page of the OpenSearch Dashboards, choose **Managed Indices**.

   The displayed page shows index policies configured for the current cluster.

#. Manage policies in the index policy list.

   -  For a policy whose status is abnormal, click **Retry policy**.
   -  To update a policy for an index, select the associated index, and click **Change policy**. After the policy is updated, click **Change** to apply the new policy.
   -  To remove a policy from an index, select the index, and click **Remove policy**. In the displayed dialog box, click **Remove**.

For details, see `Index State Management <https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/>`__.
