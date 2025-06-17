:original_name: css_02_0126.html

.. _css_02_0126:

Why Does the Disk Usage Increase After the delete_by_query Command Was Executed to Delete Data in an Elasticsearch Cluster?
===========================================================================================================================

Running the **delete_by_query** command only add a deletion mark to the target data, instead of really deleting it. When you search for data, all data is searched and the data with the deletion mark is filtered out.

The space occupied by an index with the deletion mark will not be released immediately after you call the disk deletion API. The disk space is released only when the segment merge is performed next time.

Querying the data with deletion mark occupies disk space. In this case, the disk usage increases when you run the disk deletion commands.
