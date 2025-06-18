:original_name: css_01_0249.html

.. _css_01_0249:

Configuring an Index Recycle Bin for an Elasticsearch Cluster
=============================================================

With Elasticsearch clusters, indexes are deleted without first being put into a recycle bin. To allow users to restore data after misdeletion, CSS provides an index recycle bin. Similar to other recycle bins, the index recycle bin temporarily stores deleted indexes so that users can restore them before they are finally removed from the recycle bin. This helps to improve cluster data reliability.

Constraints
-----------

-  Only Elasticsearch 7.10.2 clusters support the index recycle bin.

-  With the index recycle bin enabled, after you use the DELETE API to move an index to the recycle bin, the cluster status may stay RED for a short period of time. This is because putting the index into the recycle bin causes the index to be closed, and the Elasticsearch cluster status becomes RED when there are closed indexes.
-  When a restoration API is used to restore an index from the recycle bin, the cluster status may also stay RED for a short period of time. This is because restoring an index from the recycle bin causes that index to be reopened, and when it happens, Elasticsearch needs to re-initialize shards. This causes the cluster status to become RED momentarily.
-  Indexes stored in the recycle bin are still part of the cluster metadata. Before they are removed from the recycle bin, same-name indexes cannot be created for the cluster.

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

.. table:: **Table 1** Configuration items

   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Configuration Item          | Description                                                                                                                                                                                                                                                                                                                                           |
   +=============================+=======================================================================================================================================================================================================================================================================================================================================================+
   | **index.trash.enabled**     | Whether to enable the index recycle bin. The default value is **false**. This setting is compatible with the open-source Elasticsearch. Setting this parameter to **true** enables the index recycle bin. After an index is deleted, the index is stored in the recycle bin. You need to delete the index again to permanently delete the index data. |
   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | **indices.trash.keep.time** | Duration for retaining indexes in the recycle bin. The default value is **1d**, meaning indexes will be retained in the recycle bin for one day before they are permanently deleted. The minimum value is **1d**.                                                                                                                                     |
   +-----------------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

.. table:: **Table 2** Parameters

   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Description                                                                                                                                                                                                   |
   +===================================+===============================================================================================================================================================================================================+
   | v                                 | Whether to display the table header when the return format is a table.                                                                                                                                        |
   |                                   |                                                                                                                                                                                                               |
   |                                   | -  true: display the table header.                                                                                                                                                                            |
   |                                   | -  false: not display the table header.                                                                                                                                                                       |
   |                                   |                                                                                                                                                                                                               |
   |                                   | The default value is **false**.                                                                                                                                                                               |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | s                                 | Index sorting fields. Options include **index**, **uuid**, **pri**, **rep**, **trash.ts**, and **delete.time**.                                                                                               |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | format                            | Return format of the command. The default format is table. Other options include json, yaml, cobr, and smile. cobr and smile are binary formats.                                                              |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | h                                 | Set the column names to be displayed. By default, all column names are displayed. To specify the column names you want to display, separate them using commas (,), for example, **h=index,uuid,delete.time**. |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

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

Run the following command to clear the recycle bin:

.. code-block:: text

   POST trash/empty

Emptying the recycle bin will permanently delete all data in it. Please exercise caution.
