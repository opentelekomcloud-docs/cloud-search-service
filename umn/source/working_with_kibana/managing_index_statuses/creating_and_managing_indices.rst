:original_name: css_01_0093.html

.. _css_01_0093:

Creating and Managing Indices
=============================

Clusters of versions 7.6.2, 7.9.3 and 7.10.2 support index status management (ISM). ISM is a plugin that allows you to automate periodic and administrative operations based on changes on the index age, index size, or number of documents. When using the ISM plug-in, you can define policies that automatically handle index rolleovers or deletions based on your needs.

.. note::

   The following procedure uses Kibana 7.6.2 as an example. The Kibana UI varies depending on the Kibana version, but their operations are similar.

Creating an Index Policy
------------------------

#. Log in to Kibana and choose **IM** or **Index Management** on the left. The **Index Management** page is displayed.


   .. figure:: /_static/images/en-us_image_0000001554697221.png
      :alt: **Figure 1** Choosing IM

      **Figure 1** Choosing IM

#. Click **Create policy** to create an index policy.

#. .. _css_01_0093__li66234455115:

   Enter a policy ID in the **Policy ID** text box and enter your policy in the **Define policy** text box.


   .. figure:: /_static/images/en-us_image_0000001503977512.png
      :alt: **Figure 2** Configuring a policy

      **Figure 2** Configuring a policy

#. Click **Create**.

   After you create a policy, attach the policy to one or more indices. You can also include **policy_id** in an index template, so when you create an index that matches the index template pattern, the policy is attached to the index.

   For details about how to create an index template, see `Index Templates <https://opendistro.github.io/for-elasticsearch-docs/docs/elasticsearch/index-templates/#create-template>`__.

   .. code-block:: text

      PUT _template/<template_name>
      {
          "index_patterns": [
              "index_name-*"
          ],
          "settings": {
              "opendistro.index_state_management.policy_id": "policy_id"
          }
      }

   -  *<template_name>*: Replace it with the name of the created index template.
   -  *policy_id*: Replace it with the policy ID created in :ref:`3 <css_01_0093__li66234455115>`.

Attach the policy to an index.
------------------------------

#. Click **Indices**.


   .. figure:: /_static/images/en-us_image_0000001503657716.png
      :alt: **Figure 3** Choosing Indices

      **Figure 3** Choosing Indices

#. In the **Indices** list, select the target index to which you want to attach the policy.

#. Click **Apply policy** in the upper right corner.


   .. figure:: /_static/images/en-us_image_0000001554897281.png
      :alt: **Figure 4** Adding a policy

      **Figure 4** Adding a policy

#. Select the policy you created from the **Policy ID** drop-down list.


   .. figure:: /_static/images/en-us_image_0000001504137400.png
      :alt: **Figure 5** Selecting a policy

      **Figure 5** Selecting a policy

#. Click **Apply**.

   After you attach a policy to an index, ISM creates a job that runs every five minutes by default, to execute the policy, check conditions, and convert the index to different statuses.

Managing Indices
----------------

#. Click **Managed Indices**.
#. If you want to change the policy, click **Change policy**. For details, see :ref:`Changing Policies <css_01_0092>`.
#. To delete a policy, select your policy, and click **Remove policy**.
#. To retry a policy, select your policy, and click **Retry policy**.

For details, see `Index State Management <https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/>`__.
