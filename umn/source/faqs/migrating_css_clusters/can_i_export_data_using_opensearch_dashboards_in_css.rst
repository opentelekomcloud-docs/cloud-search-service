:original_name: css_02_0087.html

.. _css_02_0087:

Can I Export Data Using OpenSearch Dashboards in CSS?
=====================================================

Only OpenSearch 2.19.0 clusters allow you to export charts and tables through OpenSearch Dashboards.

.. caution::

   -  A maximum of 10 MB of data can be exported. If the data you want to export exceeds 10 MB, only the first 10 MB is exported.
   -  Any special characters such as **=+-@** in exported CSV files may be identified as part of some formulas, leading to data export failures.

-  **Exporting a dashboard**

   #. Log in to the OpenSearch Dashboards.

   #. Choose **OpenSearch Dashboards > Dashboards**. The **Dashboards** page is displayed.

   #. Find the dashboard you want to export and click its title. The details page is displayed.

   #. Click **Reporting** in the upper right corner, and select a download format. Once the report is generated, select a save location on your local PC to download it.

      Save the data before exporting it, or an error will be returned.


      .. figure:: /_static/images/en-us_image_0000002513250713.png
         :alt: **Figure 1** Selecting an export file format

         **Figure 1** Selecting an export file format

-  **Exporting data**

   #. Log in to the OpenSearch Dashboards.

   #. Choose **OpenSearch Dashboards > Discover**. The **Discover** page is displayed.

   #. Click **Save** in the upper right corner, then click **Reporting**. Select a download format, and once the report is generated, select a save location on your local PC to download it.


      .. figure:: /_static/images/en-us_image_0000002513253505.png
         :alt: **Figure 2** Selecting an export file format

         **Figure 2** Selecting an export file format
