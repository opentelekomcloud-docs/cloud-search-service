:original_name: css_02_0098.html

.. _css_02_0098:

Can I Export Data from Kibana in CSS?
=====================================

-  With Elasticsearch 7.10.2 (with an image version no earlier than 7.10.2_24.3.3_x.x.x), Kibana supports one-click data export in CSV.

   .. important::

      -  A maximum of 10 MB of data can be exported. If the data you want to export exceeds 10 MB, only the first 10 MB is exported.
      -  Any special characters such as **=+-@** in exported CSV files may be identified as part of some formulas, leading to data export failures.

   On the **Discover** page of Kibana, choose **Share > Data Export** in the upper right corner, and select **Export CSV**.


   .. figure:: /_static/images/en-us_image_0000002008857332.png
      :alt: **Figure 1** Exporting data

      **Figure 1** Exporting data

   Wait for a few minutes. Then click **Download csv** in the lower right corner to download the data to the local PC.


   .. figure:: /_static/images/en-us_image_0000002008857464.png
      :alt: **Figure 2** Downloading data

      **Figure 2** Downloading data

-  With Elasticsearch 7.6.2, 7.9.3, and 7.10.2 (the image version is earlier than 24.3.0), the SQL Workbench plug-in is required for exporting data on Kibana.

   In **SQL Workbench** of Kibana, you can run Elasticsearch SQL statements to query data or click **Download** to export data. You can export 1 to 200 records. By default, 200 records are exported.


   .. figure:: /_static/images/en-us_image_0000001960517917.png
      :alt: **Figure 3** SQL Workbench

      **Figure 3** SQL Workbench
