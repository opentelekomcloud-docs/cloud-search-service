:original_name: en-us_topic_0000001528659085.html

.. _en-us_topic_0000001528659085:

Changing Policies
=================

You can change any managed index policy. ISM has constraints to ensure that policy changes do not break indexes.

If an index is stuck in its current status, never proceeding, and you want to update its policy immediately, make sure that the new policy includes the same status (same name, action, and order) as the old policy. In this case, ISM applies the new policy even if the policy is being executed.

If you update the policy without including an identical status, ISM updates the policy only after all actions in the current status finish executing. Alternatively, you can select a specific status in the old policy and have the new policy take effect.

To change a policy using Kibana, do the following:

#. Under **Managed Indices**, select the indexes to which you want to attach the new policy.
#. Click **Change policy** in the upper right corner. The **Choose managed indices** page is displayed. Configure parameters required for changing a policy.

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
