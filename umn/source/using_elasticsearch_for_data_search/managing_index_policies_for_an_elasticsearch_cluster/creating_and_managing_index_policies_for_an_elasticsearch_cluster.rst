:original_name: css_01_0419.html

.. _css_01_0419:

Creating and Managing Index Policies for an Elasticsearch Cluster
=================================================================

This topic describes how to create and manage index lifecycle policies for Elasticsearch clusters.

Context
-------

Index State Management (ISM) of Elasticsearch is a plugin that allows you to automate periodic, administrative operations on indexes by triggering them based on changes in the index age, index size, or number of documents. With ISM, you can define custom policies to automate index rollovers and deletion, thus optimizing cluster search performance or cutting storage costs. The procedure for using ISM is as follows:

#. :ref:`Creating an Index Lifecycle Policy <css_01_0419__en-us_topic_0000001268154473_section779154094817>`: Create an index lifecycle policy on OpenSearch Dashboards.
#. :ref:`Associating Indexes with a Lifecycle Policy <css_01_0419__en-us_topic_0000001268154473_section11451321182815>`: Associate indexes with a lifecycle policy.
#. :ref:`Managing Index Policies <css_01_0419__en-us_topic_0000001268154473_section87941257192>`: Modify, retry, and change index lifecycle policies.

For more information about ISM, see `Index State Management <https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/>`__.

Common use cases for index lifecycle policies:

-  :ref:`Automating Index Rollover in an Elasticsearch Cluster Through Index Lifecycle Management <css_01_0420>`
-  :ref:`Decoupling Index Storage and Compute in an Elasticsearch Cluster Through Index Lifecycle Management <css_01_0421>`

Constraints
-----------

-  ISM is available only in Elasticsearch 7.6.2 clusters or later or OpenSearch clusters.
-  You can customize policy names in Kibana.
-  The Kibana GUI varies depending on the Kibana version. Kibana 7.6.2 is used as an example here.

.. _css_01_0419__en-us_topic_0000001268154473_section779154094817:

Creating an Index Lifecycle Policy
----------------------------------

#. Log in to the CSS management console.

#. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column to log in to the Kibana page.

#. Choose **IM** or **Index Management** from the menu bar to go to the index management page.

#. Click **Create policy** to configure an index lifecycle policy.

   -  **Policy ID**: use a custom policy name.
   -  **Define policy**: define a custom policy based on the reference example provided.


   .. figure:: /_static/images/en-us_image_0000001938378248.png
      :alt: **Figure 1** Configuring a policy

      **Figure 1** Configuring a policy

#. Click **Create**.

.. _css_01_0419__en-us_topic_0000001268154473_section11451321182815:

Associating Indexes with a Lifecycle Policy
-------------------------------------------

You can attach a policy to one or more indexes, or associate a policy with an index template, so that the policy will be applied to all indexes created using this index template.

Use either of the following methods to associate a lifecycle policy with an index.

-  **Method 1: Kibana commands**

   On the **Dev Tools** page of Kibana, run the following command to associate a policy ID with an index template:

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

   For details about how to create an index template, see `Index Template <https://opendistro.github.io/for-elasticsearch-docs/docs/elasticsearch/index-templates/#create-template>`__.

-  **Method 2: Kibana console**

   #. On the Kibana console, choose **IM** or **Index Management** from the menu bar to go to the index management page.

   #. Select **Indices** on the left.


      .. figure:: /_static/images/en-us_image_0000001938218884.png
         :alt: **Figure 2** Choosing Indices

         **Figure 2** Choosing Indices

   #. In the **Indices** list, select the target index to which you want to bind a policy.

   #. Click **Apply policy** in the upper right corner. In the displayed dialog box, select a policy ID.


      .. figure:: /_static/images/en-us_image_0000001965417249.png
         :alt: **Figure 3** Adding an index policy

         **Figure 3** Adding an index policy


      .. figure:: /_static/images/en-us_image_0000001965497453.png
         :alt: **Figure 4** Selecting a policy

         **Figure 4** Selecting a policy

   #. Click **Apply**.

      After you bind a policy to an index, ISM creates a job that runs every 5 minutes by default to execute the policy, check criteria, and change index states.

.. _css_01_0419__en-us_topic_0000001268154473_section87941257192:

Managing Index Policies
-----------------------

#. Log in to the CSS management console.

#. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column to log in to the Kibana page.

#. Choose **IM** or **Index Management** from the menu bar to go to the index management page.

#. Choose **Managed Indices** on the left.

   The displayed page shows index policies configured for the current cluster.

#. Manage policies in the index policy list.

   -  For a policy whose status is abnormal, click **Retry policy**.
   -  To update a policy for an index, select the associated index, and click **Change policy**. After the policy is updated, click **Change** to apply the new policy.
   -  To remove a policy from an index, select the index, and click **Remove policy**. In the displayed dialog box, click **Remove**.

For details, see `Index State Management <https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/>`__.
