:original_name: en-us_topic_0000001528299609.html

.. _en-us_topic_0000001528299609:

(Optional) Pre-Building and Registering a Center Point Vector
=============================================================

When you perform operations in :ref:`Creating a Vector Index <en-us_topic_0000001528299557__en-us_topic_0000001309709789_section137344225249>`, if **IVF_GRAPH** and **IVF_GRAPH_PQ** index algorithms are selected, you need to pre-build and register the center point vector.

Context
-------

The vector index acceleration algorithms **IVF_GRAPH** and **IVF_GRAPH_PQ** are suitable for ultra-large-scale computing. These two algorithms allow you to narrow down the query range by dividing a vector space into subspaces through clustering or random sampling. Before pre-build, you need to obtain all center point vectors by clustering or random sampling.

Then, pre-construct and register the center point vectors to create the **GRAPH** or **GRAPH_PQ** index and register them with the Elasticsearch cluster. All nodes in the cluster can share the index file. Reuse of the center index among shards can effectively reduce the training overhead and the number of center index queries, improving the write and query performance.

Procedure
---------

#. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. Click **Dev Tools** in the navigation tree on the left.

#. Create a center point index table.

   -  For example, if the created index is named **my_dict**, **number_of_shards** of the index must be set to **1**. Otherwise, the index cannot be registered.
   -  If you want to use the **IVF_GRAPH** index, set **algorithm** of the center point index to **GRAPH**.
   -  If you want to use the **IVF_GRAPH_PQ** index, set **algorithm** of the center point index to **GRAPH_PQ**.

   .. code-block:: text

      PUT my_dict
       {
         "settings": {
           "index": {
             "vector": true
           },
           "number_of_shards": 1,
           "number_of_replicas": 0
         },
         "mappings": {
           "properties": {
             "my_vector": {
               "type": "vector",
               "dimension": 2,
               "indexing": true,
               "algorithm": "GRAPH",
               "metric": "euclidean"
             }
           }
         }
       }

#. Write the center point vector to the created index.

   Write the center point vector obtained through sampling or clustering into the created **my_dict** index by referring to :ref:`Importing Vector Data <en-us_topic_0000001528299557__en-us_topic_0000001309709789_section137931314240>`.

#. Call the registration API.

   Register the created **my_dict** index with a **Dict** object with a globally unique identifier name (**dict_name**).

   .. code-block:: text

      PUT _vector/register/my_dict
       {
         "dict_name": "my_dict"
       }

#. Create an **IVF_GRAPH** or **IVF_GRAPH_PQ** index.

   You do not need to specify the dimension and metric information. Simply specify the registered dictionary name.

   .. code-block:: text

      PUT my_index
       {
         "settings": {
           "index": {
             "vector": true
           }
         },
         "mappings": {
           "properties": {
             "my_vector": {
               "type": "vector",
               "indexing": true,
               "algorithm": "IVF_GRAPH",
               "dict_name": "my_dict",
               "offload_ivf": false
             }
           }
         }
       }

   .. table:: **Table 1** Field mappings parameters

      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter                         | Description                                                                                                                                                                                                                                                               |
      +===================================+===========================================================================================================================================================================================================================================================================+
      | dict_name                         | Specifies the name of the depended central point index. The vector dimension and measurement metric of the index are the same as those of the Dict index.                                                                                                                 |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | offload_ivf                       | Unloads the IVF inverted index implemented by the underlying index to Elasticsearch. In this way, the use of non-heap memory and the overhead of write and merge operations are reduced. However, the query performance also deteriorates. You can use the default value. |
      |                                   |                                                                                                                                                                                                                                                                           |
      |                                   | Value: **true** or **false**                                                                                                                                                                                                                                              |
      |                                   |                                                                                                                                                                                                                                                                           |
      |                                   | Default value: **false**                                                                                                                                                                                                                                                  |
      +-----------------------------------+---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
