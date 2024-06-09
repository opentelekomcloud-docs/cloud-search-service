:original_name: en-us_topic_0000001641016221.html

.. _en-us_topic_0000001641016221:

Changing an Index Policy
========================

You can change any managed index policy. ISM has constraints to ensure that policy changes do not break indexes.

If an index is stuck in its current status and you want to update its policy immediately, make sure that the new policy includes the same status (same name, action, and order) as the old policy. In this case, ISM applies the new policy even if the old policy is being executed.

If the new policy you use does not include the same status as the old policy, ISM updates the policies only after all actions in the current status are completed. Alternatively, you can select a specific status in the old policy and make the new policy take effect.

Perform the following steps to change a policy in the **OpenSearch Dashboards**:

#. On the **Index Management** page of the **OpenSearch Dashboards**, select the index policy you want to change.

#. Click **Change policy** in the upper right corner. In the **Choose managed indices** and **Choose new policy** areas, select information about the new policy.


   .. figure:: /_static/images/en-us_image_0000001607591784.png
      :alt: **Figure 1** Changing an index policy

      **Figure 1** Changing an index policy

   .. table:: **Table 1** Parameters required for changing a policy

      +-----------------+-----------------------------------------------------------------------------------------------------------+
      | Parameter       | Description                                                                                               |
      +=================+===========================================================================================================+
      | Managed indices | Select the indexes to which you want to attach the new policy. Multiple indexes can be selected.          |
      +-----------------+-----------------------------------------------------------------------------------------------------------+
      | State filters   | Select an index status. When a status is selected, the new policy is attached to an index in this status. |
      +-----------------+-----------------------------------------------------------------------------------------------------------+
      | New policy      | Select a new policy.                                                                                      |
      +-----------------+-----------------------------------------------------------------------------------------------------------+

#. After configuration is complete, click **Change**.
