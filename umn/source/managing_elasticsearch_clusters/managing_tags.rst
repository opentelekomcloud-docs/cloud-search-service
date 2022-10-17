:original_name: css_01_0075.html

.. _css_01_0075:

Managing Tags
=============

Tags are cluster identifiers. Adding tags to clusters can help you identify and manage your cluster resources.

You can add tags to a cluster when creating the cluster or add them on the details page of the created cluster.

Managing Tags When Creating a New Cluster
-----------------------------------------

#. Log in to the CSS management console.

#. Click **Create Cluster** in the upper right corner. The **Create Cluster** page is displayed.

#. On the **Create Cluster** page, set **Advanced Settings** to **Custom**. Add tags for a cluster.

   You can select a predefined tag and set **Tag value** for the tag. You can click **View Predefined Tag** to switch to the TMS management console and view existing tags.

   You can also create new tags by specifying **Tag key** and **Tag value**.

   You can add a maximum of 10 tags for a CSS cluster. If the entered tag is incorrect, you can click **Delete** on the right of the tag to delete the tag.

   .. table:: **Table 1** Naming rules for a tag key and value

      +-----------------------------------+------------------------------------------------------------------------+
      | Parameter                         | Description                                                            |
      +===================================+========================================================================+
      | Tag key                           | Cannot be left blank.                                                  |
      |                                   |                                                                        |
      |                                   | Must be unique in a cluster.                                           |
      |                                   |                                                                        |
      |                                   | Can contain a maximum of 36 characters.                                |
      |                                   |                                                                        |
      |                                   | Can only consist of digits, letters, hyphens (-), and underscores (_). |
      +-----------------------------------+------------------------------------------------------------------------+
      | Tag value                         | Can contain a maximum of 43 characters.                                |
      |                                   |                                                                        |
      |                                   | Can only consist of digits, letters, hyphens (-), and underscores (_). |
      |                                   |                                                                        |
      |                                   | Cannot be left blank.                                                  |
      +-----------------------------------+------------------------------------------------------------------------+

Managing Tags of Existing Clusters
----------------------------------

You can modify, delete, or add tags for a cluster.

#. Log in to the CSS management console.

#. On the **Clusters** page, click the name of a cluster for which you want to manage tags.

   The **Basic Information** page is displayed.

#. Select the **Tags** tab, then you can add, modify, or delete tags on the displayed page.

   -  View

      On the **Tags** page, you can view details about tags of the cluster, including the number of tags and the key and value of each tag.

   -  Add

      Click **Add** in the upper left corner. In the displayed **Add Tag** dialog box, enter the key and value of the tag to be added, and click **OK**.

   -  Modify

      You can only change the value of an existing tag.

      In the **Operation** column of a tag, click **Edit**. In the displayed **Edit Tag** page, enter a new tag value and click **OK**.

   -  Delete

      In the **Operation** column of the tag, click **Delete**. After confirmation, click **Yes** on the displayed **Delete Tag** page.

Searching for Clusters by Tag
-----------------------------

#. Log in to the CSS management console.

#. On the **Clusters** page, click **Search by Tag** in the upper right corner of the cluster list.

#. Enter the target tag key and value.

   You can select a tag key or tag value from their drop-down lists. The system returns a list of clusters that exactly match the tag key or tag value. If you enter multiple tags, the cluster that meets requirements of all the tags will be filtered.

   You can add a maximum of 10 tags at one time.

#. Click **Search**.

   The system searches for the target cluster by tag key and value.
