:original_name: css_02_0019.html

.. _css_02_0019:

Failed to Open Kibana
=====================

Symptom
-------

After I click **Access Kibana** in the **Operation** column in the row where cluster **Es-event** resides on the **Clusters** page of the CSS management console, the Kibana page fails to be loaded and access to Kibana fails.

Cause
-----

The browser cache is not cleared.

Procedure
---------

#. Log in to the CSS management console.
#. In the left navigation pane, click **Clusters**.
#. On the displayed **Clusters** page, locate the row containing the target cluster **Es-event** and click **Access Kibana** in the **Operation** column.

   .. note::

      If the cluster has the security mode enabled, enter the username and password you for login. Generally, the username is **admin** and the password is the one specified during cluster creation.

      If you forget the password, you can reset it on the cluster details page and then log in. For details, see .

#. On the displayed **Kibana** page, press **F12**.
#. Click **Network**, right-click **data:image**, and choose **clear browser cache** from the shortcut menu. In the displayed dialog box, click **OK**. Close the Kibana window.
#. Switch to the **Clusters** page, locate the row that contains cluster **Es-event** and click **Access Kibana** in the **Operation** column.
