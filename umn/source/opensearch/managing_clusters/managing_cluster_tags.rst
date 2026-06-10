:original_name: css_01_0277.html

.. _css_01_0277:

Managing Cluster Tags
=====================

As business grows, an enterprise may operate hundreds of OpenSearch clusters, and cluster names alone will be insufficient for categorization and identification. For example, tasks such as resource monitoring or automated operations via scripts require the ability to quickly locate clusters based on specific attributes. On CSS, you can use tags (key-value pairs) to label resources, enabling efficient filtering and batch management. When used together with Tag Management Service (TMS), tags help you implement enterprise-grade resource governance.

Constraints
-----------

-  Each cluster can have a maximum of 20 tags.
-  If your organization has configured tag policies for CSS, add tags to clusters based on these policies. If a tag does not comply with existing tag policies, cluster creation may fail. Contact the administrator to learn more about these policies.
-  To use the same tag to identify multiple cloud resources for better resource grouping, predefine tags in Tag Management Service (TMS). For details, see *Tag Management Service User Guide*.

Managing Cluster Tags in Batches
--------------------------------

Manage tags for multiple clusters in batches, including add, modify, and delete. This feature is useful in cases such as environment refactoring and large-scale migrations.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, select one or more clusters.
#. Click **Edit Tag** above the cluster list.

   -  Add

      In the displayed dialog box, click **+Add**, and add new tags in the form of key-value pairs. The tags will be added for all selected clusters.

   -  Modify

      In the displayed dialog box, modify existing tag values. The changes will be applied to all selected clusters, overwriting existing tags. Avoid this operation if you have custom tags that you wish to keep.

   -  Delete

      In the displayed dialog box, click **Delete** next to the tag you want to delete. This deletes the tag for all selected clusters. The deletion cannot be undone.

#. Click **OK** to save the changes.
#. Verify the result: In the cluster list, hover the mouse over the icon in the **Tag** column for each cluster. Check that the tag information has been updated for all selected clusters.

Managing Tags for a Single Cluster
----------------------------------

Add, modify, or delete tags for a single cluster.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > OpenSearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Click the **Tags** tab.
#. Click **Edit Tag**. In the displayed dialog box, modify the cluster's tags.

   -  Add

      In the displayed dialog box, click **+Add**, and add new tags in the form of key-value pairs.

   -  Modify

      In the displayed dialog box, modify existing tag keys and values.

   -  Delete

      In the displayed dialog box, click **Delete** next to the tag you want to delete.

#. Click **OK**.
#. Verify the result: In the tag list, check that the tag keys and values have been updated.

Searching for Clusters by Tag
-----------------------------

Locate clusters by tag from among a large number of resources.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. Click the search box above the cluster list. Select a tag key, operator, and tag value to search.

   -  You can select a tag key and value from the drop-down list. The system returns a list of clusters that exactly match the tag key and value.
   -  In case you use multiple tags to start a search: With the same tag key but different values, the system returns a list of clusters that match any of the tag values; If the tag keys are different, the system returns a list of clusters that match all of these keys and tags.

   The cluster list is filtered in real time to display matching clusters only.
