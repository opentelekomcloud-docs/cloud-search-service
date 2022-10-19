:original_name: css_01_0044.html

.. _css_01_0044:

Viewing Metrics
===============

Cloud Eye performs daily monitoring on core cluster metrics for CSS. You can log in to the Cloud Eye management console to view cluster metrics.

Cloud Eye only monitors clusters that have been successfully created in real time.

Prerequisites
-------------

-  The cluster status is **Available** or **Processing**.

   .. note::

      You cannot view the metrics for deleted clusters or the metrics for the clusters those whose **Status** is **Abnormal** or **Creating** on the Cloud Eye management console. If the status of a cluster changes from **Abnormal** or **Creating** to **Available**, you can view its metrics in real time after approximately 10 minutes.

-  The cluster has been running for about 10 minutes.
-  You have created alarm rules.

Procedure
---------

#. Log in to the CSS management console.
#. Choose **Clusters**. Select a cluster. In the **Operation** column, choose **More** > **View Metric**.
#. Click the tab for the time range you want to view.
#. View the monitoring data.
