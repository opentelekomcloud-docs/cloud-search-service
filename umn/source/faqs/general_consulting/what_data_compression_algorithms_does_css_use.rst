:original_name: css_02_0041.html

.. _css_02_0041:

What Data Compression Algorithms Does CSS Use?
==============================================

CSS supports two data compression algorithms: LZ4 (by default) and best_compression.

-  **LZ4 algorithm**

   LZ4 is the default compression algorithm for Elasticsearch. This algorithm can compress and decompress data quickly, but its compression ratio is low.

   LZ4 scans data with a 4-byte window, which slides 1 byte forward at a time. Duplicate data is compressed. This algorithm is well-suited where reads far exceed writes in terms of data volumes.

-  **best_compression algorithm**

   This algorithm can be used when a large amount of data is written and the index storage cost is high, such as logs and time series analysis. This algorithm can greatly reduce the index storage cost.

Run the following command to switch the default compression algorithm (LZ4) to best_compression:

.. code-block:: text

   PUT index-1
   {
       "settings": {
           "index": {
               "codec": "best_compression"
           }
       }
   }

The LZ4 algorithm is faster, while the best_compression algorithm provides higher compression and decompression ratios.
