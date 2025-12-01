:original_name: css_01_0075.html

.. _css_01_0075:

Setting Tags for an Elasticsearch Cluster
=========================================

Tags are cluster identifiers. Adding tags to clusters helps you identify and manage your cluster resources.

Tags can be added during or after cluster creation. If you want to use the same tag to identify multiple cloud resources for better resource grouping, we recommend that you predefine tags in Tag Management Service (TMS). For details, see Tag Management Service User Guide.

Constraints
-----------

-  Each cluster can have a maximum of 20 tags.
-  If your organization has configured tag policies for CSS, add tags to clusters based on these policies. If a tag does not comply with existing tag policies, cluster creation may fail. Contact the administrator to learn more about these policies.

Managing Tags
-------------

In CSS, you can add, delete, modify, and query cluster tags.

#. Log in to the CSS management console.
#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.
#. In the cluster list, click the name of the target cluster. The cluster information page is displayed.
#. Select the **Tags** tab, where you can add, modify, or delete tags for the current cluster.

   -  View

      On the **Tags** page, you can view details about tags of the cluster, including the number of tags and the key and value of each tag.

   -  Add

      Click **Edit Tag** in the upper left corner. In the displayed dialog box, click **Add Tag**, enter the tag key and value, and click **OK**.

   -  Modify

      Click **Edit Tag** in the upper left corner. In the displayed dialog box, modify the key and value of a tag, and click **OK**.

   -  Delete

      Click **Edit Tag** in the upper left corner. In the displayed dialog box, click **Delete** in the row that contains a tag, and click **OK**.

Searching for Clusters by Tag
-----------------------------

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > Elasticsearch**.

#. In the cluster list, click the search box, and select a tag key and value to search for the target cluster.

   You can select a tag key or tag value from their drop-down lists. The system returns a list of clusters that exactly match the tag key or tag value. If you enter multiple tags, the cluster that meets requirements of all the tags will be filtered.

   You can add a maximum of 10 tags at one time.
