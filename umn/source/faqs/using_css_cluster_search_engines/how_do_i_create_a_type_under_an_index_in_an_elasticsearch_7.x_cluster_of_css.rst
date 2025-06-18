:original_name: css_02_0132.html

.. _css_02_0132:

How Do I Create a Type Under an Index in an Elasticsearch 7.\ *x* Cluster of CSS?
=================================================================================

In Elasticsearch 7.\ *x* and later versions, types cannot be created for indexes.

If you need to use types, add **include_type_name=true** to the command. Only a single type is supported.

.. code-block:: text

   PUT index?include_type_name=true
   {
     "mappings": {
       "my_type": {
         "properties": {
           "@timestamp": {
             "type": "date"
           }
         }
       }
     }
   }

After a multi-type index is created, run the following command to write data into it:

.. code-block:: text

   PUT index/my_type/1
   {
     "@timestamp":"2019-02-20"
   }
