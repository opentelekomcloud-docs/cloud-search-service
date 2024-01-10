:original_name: css_01_0122.html

.. _css_01_0122:

Cluster Planning for Vector Retrieval
=====================================

Off-heap memory is used for index construction and query in vector retrieval. Therefore, the required cluster capacity is related to the index type and off-heap memory size. You can estimate the off-heap memory required by full indexing to select proper cluster specifications.

There are different methods for estimating the size of off-heap memory required by different types of indexes. The calculation formulas are as follows:

-  **Graph Index**

   |image1|

   .. note::

      If you need to update indexes in real time, consider the off-heap memory overhead required for vector index construction and automatic merge. The actual size of required **mem_needs** is at least 1.5 to 2 times of the original estimation.

-  **PQ Index**

   |image2|

-  **FALT and IVF Indexes**

   |image3|

.. table:: **Table 1** Parameter description

   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                         | Description                                                                                                                                                                     |
   +===================================+=================================================================================================================================================================================+
   | dim                               | Vector dimensions                                                                                                                                                               |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | neighbors                         | Number of neighbors of a graph node. The default value is **64**.                                                                                                               |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | dim_size                          | Number of bytes required by each dimension. The default value is four bytes in the float type.                                                                                  |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | num                               | Total number of vectors                                                                                                                                                         |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | delta                             | Metadata size. This parameter can be left blank.                                                                                                                                |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | frag_num                          | Number of vector segments during quantization and coding. If this parameter is not specified when an index is created, the value is determined by the vector dimension **dim**. |
   |                                   |                                                                                                                                                                                 |
   |                                   | .. code-block::                                                                                                                                                                 |
   |                                   |                                                                                                                                                                                 |
   |                                   |    if dim <= 256:                                                                                                                                                               |
   |                                   |      frag_num = dim / 4                                                                                                                                                         |
   |                                   |    elif dim <= 512:                                                                                                                                                             |
   |                                   |      frag_num = dim / 8                                                                                                                                                         |
   |                                   |    else :                                                                                                                                                                       |
   |                                   |      frag_num = 64                                                                                                                                                              |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | frag_size                         | Size of the center point during quantization and coding. The default value is **1**. If the value of **frag_num** is greater than **256**, the value of **frag_size** is **2**. |
   +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

These calculation methods can estimate the size of off-heap memory required by a complete vector index. To determine cluster specifications, you also need to consider the heap memory overhead of each node.

Heap memory allocation policy: The size of the heap memory of each node is half of the node physical memory, and the maximum size is **31 GB**.

For example, if you create a Graph index for the SIFT10M dataset, set **dim** to **128**, **dim_size** to **4**, **neighbors** to default value **64**, and **num** to **10 million**, the off-heap memory required by the Graph index is as follows:

|image4|

Considering the overhead of heap memory, a single server with **8 vCPUs** and **16 GB memory** is recommended. If real-time write or update is required, you need to apply for larger memory.

.. |image1| image:: /_static/images/en-us_formulaimage_0000001714802349.png
.. |image2| image:: /_static/images/en-us_formulaimage_0000001667002558.png
.. |image3| image:: /_static/images/en-us_formulaimage_0000001666842858.png
.. |image4| image:: /_static/images/en-us_formulaimage_0000001714802345.png
