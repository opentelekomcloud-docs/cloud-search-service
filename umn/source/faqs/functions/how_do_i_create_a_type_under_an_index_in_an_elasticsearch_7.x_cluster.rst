:original_name: en-us_topic_0000001528097313.html

.. _en-us_topic_0000001528097313:

How Do I Create a Type Under an Index in an Elasticsearch 7.\ *x* Cluster?
==========================================================================

In Elasticsearch 7.\ *x* and later versions, types cannot be created for indexes.

If you need to use types, add **include_type_name=true** to the command. For example:

.. code-block:: text

   PUT _template/urldialinfo_template?include_type_name=true

After the command is executed, the following information is displayed:

.. code-block::

   "#! Deprecation: [types removal] Specifying include_type_name in put index template requests is deprecated. The parameter will be removed in the next major version. "
