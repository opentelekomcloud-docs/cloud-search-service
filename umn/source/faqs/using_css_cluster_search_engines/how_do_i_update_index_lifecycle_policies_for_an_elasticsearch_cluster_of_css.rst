:original_name: css_02_0119.html

.. _css_02_0119:

How Do I Update Index Lifecycle Policies for an Elasticsearch Cluster of CSS?
=============================================================================

The lifecycle of Elasticsearch clusters is implemented using the Index State Management (ISM) of Open Distro. For details about how to configure policies related to the ISM template, see the `Open Distro documentation <https://opendistro.github.io/for-elasticsearch-docs/docs/im/ism/>`__.

#. When a policy is created, the system writes a record to the **.opendistro-ism-config** index. In the record, **\_id** is the policy name, and the content is the policy definition.


   .. figure:: /_static/images/en-us_image_0000001960397693.png
      :alt: **Figure 1** Writing a data record

      **Figure 1** Writing a data record

#. After a policy is bound to an index, the system writes another record to the **.opendistro-ism-config** index. The following figure shows the initial status of a record.


   .. figure:: /_static/images/en-us_image_0000001933159210.png
      :alt: **Figure 2** Initial data status

      **Figure 2** Initial data status

#. Run the **explain** command. Only a policy ID will be returned.

   .. code-block:: text

      GET _opendistro/_ism/explain/data2
      {
        "data2" : {
          "index.opendistro.index_state_management.policy_id" : "policy1"
        }
      }

   Open Distro will execute an initialization process to fill the policy content in the record. The following figure shows the initialized data.


   .. figure:: /_static/images/en-us_image_0000001933318578.png
      :alt: **Figure 3** Initialized data

      **Figure 3** Initialized data

   After the initialization, **min_index_age** in the policy will be copied.

   .. note::

      The initialized index uses a copy of this policy. The policy update will not take effect on the index.

4. After the policy is modified, call the **change_policy** API to update the policy.

   .. code-block:: text

      POST _opendistro/_ism/change_policy/data1
      {
        "policy_id": "policy1"
      }
