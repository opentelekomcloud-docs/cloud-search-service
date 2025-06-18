:original_name: css_01_0015.html

.. _css_01_0015:

Deleting an Elasticsearch Cluster
=================================

You can delete clusters that you no longer need.

Constraints
-----------

-  Deleting a cluster will clear all its data. Exercise caution.
-  A cluster that has no snapshots created for it cannot be restored once it is deleted. The snapshots of the cluster stored in OBS, if any, will not be deleted with the cluster. You can restore a deleted cluster using its snapshots stored in the OBS bucket.
-  For a cluster for which the VPCEP service has been enabled, deleting the cluster may not delete the VPC endpoint associated with the cluster if the current account does not have the necessary VPCEP permissions. For details about the VPCEP permissions, see section "Permissions" in *VPC Endpoint User Guide*.

Deleting a Cluster
------------------

#. Log in to the CSS management console.
#. In the navigation tree on the left, select a cluster type. The cluster list page is displayed.
#. Locate the target cluster and click **More** > **Delete** in the **Operation** column.
#. In the displayed dialog box, manually type in **DELETE**, and click **OK**.
