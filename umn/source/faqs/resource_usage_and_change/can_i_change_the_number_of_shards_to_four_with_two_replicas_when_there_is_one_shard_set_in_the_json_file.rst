:original_name: en-us_topic_0000001476977562.html

.. _en-us_topic_0000001476977562:

Can I Change the Number of Shards to Four with Two Replicas When There Is One Shard Set in the JSON File?
=========================================================================================================

Once an index is created, the number of primary shards cannot be changed.

You can run the following command in Kibana to change the number of replicas:

.. code-block:: text

   PUT /indexname/_settings
   {
   "number_of_replicas":1       //Number of replicas
   }

.. note::

   **index** specifies the index name. Set this parameter based on site requirements.
