:original_name: en-us_topic_0000001564706853.html

.. _en-us_topic_0000001564706853:

(Optional) Authorizing CSS to Use SMN
=====================================

Scenario Description
--------------------

To use the OpenDistro alarm plugin (**opendistro_alerting**), authorize your Elasticsearch cluster to use SMN to send notifications. For details about how to use the OpenDistro alarm plugin, see :ref:`Configuring SMN Alarms <en-us_topic_0000001564906577>`.

Service authorization is to delegate CSS to use other cloud resources. For example, you can authorize CSS to use SMN to send notifications.

Constraints and Limitations
---------------------------

Only the SMN service can be authorized.

Procedure
---------

#. Log in to the CSS management console as an administrator with IAM permissions.
#. In the navigation pane, choose **Service Authorization**.
#. On the **Service Authorization** page, click **Create Agency**. In the dialog box displayed, confirm that the agency is successfully created.

   -  If an agency has been created, "css_smn_agency exist, no need to created." is displayed in the upper right corner.
   -  If you do not have the creation permission, a message indicating that the current user does not have the permission and you need to check the account permission on IAM is displayed in the upper right corner.
