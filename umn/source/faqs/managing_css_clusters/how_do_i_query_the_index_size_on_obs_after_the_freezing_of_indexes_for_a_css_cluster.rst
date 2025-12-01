:original_name: css_02_0151.html

.. _css_02_0151:

How Do I Query the Index Size on OBS After the Freezing of Indexes for a CSS Cluster?
=====================================================================================

The size of indexes remains unchanged after freezing. By querying the size of frozen indexes in OBS, you obtain the size of all indexes stored on OBS.

Run the following command to obtain information about all indexes that are being frozen or have already been frozen:

.. code-block:: text

   GET _cat/freeze_indices?stage=$

The output is as follows (as an example only):

.. code-block::

   green open data2 0bNtxWDtRbOSkS4JYaUgMQ 3 0  5 0  7.9kb  7.9kb
   green open data3 oYMLvw31QnyasqUNuyP6RA 3 0 51 0 23.5kb 23.5kb

The last column of the returned result contains the index size information.

**Related Questions**

-  **Billing for index storage on OBS**

   Storing index data in OBS incurs additional charges.

-  **Why are frozen indexes stored in OBS still searchable via commands?**

   Elasticsearch and OpenSearch clusters use local storage by default, and Lucene index files are stored on local disks. Lucene interacts with the underlying storage via the Directory API. Files can be read through the following API:

   .. code-block::

      public abstract IndexInput openInput(String name, IOContext context) throws IOException;

   The storage-compute decoupling feature enables interaction with OBS through the Directory API to read files stored in OBS. This is why information about frozen indexes stored in OBS can be queried using commands.
