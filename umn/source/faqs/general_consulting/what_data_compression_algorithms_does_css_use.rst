:original_name: css_02_0041.html

.. _css_02_0041:

What Data Compression Algorithms Does CSS Use?
==============================================

CSS supports two data compression algorithms: LZ4 (by default) and best_compression.

-  **LZ4 algorithm**

   LZ4 is the default compression algorithm of Elasticsearch. This algorithm can compress and decompress data quickly, but its compression ratio is low.

   LZ4 scans data with a 4-byte window, which slides 1 byte forward at a time. Duplicate data is compressed. This algorithm applies to scenarios where a large amount of data to be read while a small amount of data to be written.

-  **best_compression algorithm**

   This algorithm can be used when a large amount of data is written and the index storage cost is high, such as logs and time sequence analysis. This algorithm can greatly reduce the index storage cost.

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

The LZ4 algorithm can quickly compress and decompress data while the best_compression algorithm has a higher compression and decompression ratio.
