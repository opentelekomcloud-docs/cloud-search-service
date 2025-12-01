:original_name: css_01_0047.html

.. _css_01_0047:

Configuring an Index Recycle Bin for an OpenSearch Cluster
==========================================================

By default, when indexes are deleted in an OpenSearch cluster, the index data is deleted permanently. To prevent data loss caused by accidental deletion, CSS provides an index recycle bin. When enabled, deleted indexes are temporarily stored in the recycle bin, allowing for recovery before they are permanently removed. This feature improves data reliability and operational security.

How the Feature Works
---------------------

The index recycle bin works as follows:

-  Data recycling mechanism: When an index is deleted, it is first moved to the recycle bin. From there, it will be automatically cleared when a predefined retention duration expires. Indexes in the recycle bin are still part of the cluster metadata and can be restored using an API.
-  Status management

   -  When the DELETE API is used to delete an index, the index is closed, and the cluster status temporarily changes to Red.
   -  When the restore API is used to restore an index, the index is reopened and shards are initialized, which may also cause the cluster status to temporarily change to Red.

Constraints
-----------

-  Only OpenSearch 2.19.0 supports the index recycle bin.

-  Indexes in the recycle bin are still part of the cluster metadata. Before they are removed from the recycle bin, same-name indexes cannot be created for the cluster.

Logging In to OpenSearch Dashboards
-----------------------------------

Log in to OpenSearch Dashboards and go to the command execution page. OpenSearch clusters support multiple access methods. This topic uses OpenSearch Dashboards as an example to describe the operation procedures.

#. Log in to the CSS management console.

#. In the navigation pane on the left, choose **Clusters > OpenSearch**.

#. In the cluster list, find the target cluster, and click **Dashboards** in the **Operation** column to log in to OpenSearch Dashboards.

#. In the left navigation pane, choose **Dev Tools**.

   The left part of the console is the command input box, and the triangle icon in its upper-right corner is the execution button. The right part shows the execution result.

Enabling the Index Recycle Bin
------------------------------

Run the following command to enable the index recycle bin:

.. code-block:: text

   PUT _cluster/settings
   {
     "persistent": {
       "index.trash.enabled": true
     }
   }

.. table:: **Table 1** Parameters for enabling the index recycle bin

   +-------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter               | Type                  | Description                                                                                                                                                                                                                        |
   +=========================+=======================+====================================================================================================================================================================================================================================+
   | index.trash.enabled     | Boolean               | Whether to enable the index recycle bin. When the index recycle bin is enabled, deleting indexes will first move them to the recycle bin. The indexes will be permanently deleted only when they are cleared from the recycle bin. |
   |                         |                       |                                                                                                                                                                                                                                    |
   |                         |                       | -  **true**: Enable the index recycle bin.                                                                                                                                                                                         |
   |                         |                       | -  **false** (default): Disable the index recycle bin.                                                                                                                                                                             |
   +-------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | indices.trash.keep.time | String                | Index retention duration in the recycle bin. Indexes will be automatically removed from the recycle bin when this duration expires.                                                                                                |
   |                         |                       |                                                                                                                                                                                                                                    |
   |                         |                       | Examples of supported time formats: **1d** (one day), **7d** (seven days), **1w** (one week), **1h** (one hour). The minimum duration is **1d**.                                                                                   |
   |                         |                       |                                                                                                                                                                                                                                    |
   |                         |                       | Default value: **1d**.                                                                                                                                                                                                             |
   +-------------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   The following command deletes an index:

   .. code-block:: text

      DELETE {INDEX_NAME}

   **INDEX_NAME** indicates the name of the index to be deleted. Wildcards can be used to specify indexes.

Viewing Indexes in the Recycle Bin
----------------------------------

Run the following command to view indexes in the index recycle bin:

.. code-block:: text

   GET _cat/trash?v=true&s=index

.. table:: **Table 2** Parameter description

   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Description                                                                                                                                                                                    |
   +===================================+================================================================================================================================================================================================+
   | v                                 | Whether to display the table header when the return format is a table.                                                                                                                         |
   |                                   |                                                                                                                                                                                                |
   |                                   | -  true: display the table header.                                                                                                                                                             |
   |                                   | -  false: not display the table header.                                                                                                                                                        |
   |                                   |                                                                                                                                                                                                |
   |                                   | The default value is **false**.                                                                                                                                                                |
   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | s                                 | Index sorting fields. Options include **index**, **uuid**, **pri**, **rep**, **trash.ts**, and **delete.time**.                                                                                |
   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | format                            | Return format of the command. The default format is table. Other options include json, yaml, cobr, and smile. cobr and smile are binary formats.                                               |
   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | h                                 | Set the column names to be displayed. By default, all column names are displayed. To specify multiple column names, separate them using commas (,), for example, **h=index,uuid,delete.time**. |
   +-----------------------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

The following is an example of the output.

.. code-block::

   index    uuid                   pri rep      trash.ts delete.time
   index1   CMD3FCLzTOyTg4RUekWNNA   1   1 1714465116615       23.6h
   index1   6ATijuu6SfqamVI-WMyOKg   1   1 1714466233898       23.9h

.. table:: **Table 3** Parameters in the output

   +-------------+-----------------------------------------------------------------------------------------------------------------------------+
   | Column      | Description                                                                                                                 |
   +=============+=============================================================================================================================+
   | index       | Index name                                                                                                                  |
   +-------------+-----------------------------------------------------------------------------------------------------------------------------+
   | uuid        | Index UUID                                                                                                                  |
   +-------------+-----------------------------------------------------------------------------------------------------------------------------+
   | pri         | Number of shards of an index                                                                                                |
   +-------------+-----------------------------------------------------------------------------------------------------------------------------+
   | rep         | Number of replicas of an index                                                                                              |
   +-------------+-----------------------------------------------------------------------------------------------------------------------------+
   | trash.ts    | Time when an index was moved to the recycle bin                                                                             |
   +-------------+-----------------------------------------------------------------------------------------------------------------------------+
   | delete.time | Remaining retention duration of an index in the recycle bin. When the value changes to 0, the index is permanently deleted. |
   +-------------+-----------------------------------------------------------------------------------------------------------------------------+

Restoring an Index from the Recycle Bin
---------------------------------------

Run the following command to restore an index from the recycle bin:

.. code-block:: text

   POST /trash/recover/{INDEX_NAME}

**INDEX_NAME** indicates the name of the index to be restored. Wildcards can be used to specify indexes.

Emptying the Recycle Bin
------------------------

Run the following command to empty the recycle bin:

.. code-block:: text

   POST trash/empty

Emptying the recycle bin will permanently delete all data in it. Please exercise caution.
