:original_name: en-us_topic_0000001477739376.html

.. _en-us_topic_0000001477739376:

Context
=======

The large query isolation feature allows you to separately manage large queries. You can isolate query requests that consume a large amount of memory or take a long period of time. If the heap memory usage of a node is too high, the interrupt control program will be triggered. The program will interrupt a large query based on the policies you configured and cancel the running query tasks of the query.

You can also configure a global query timeout duration. Long queries will be intercepted.

.. note::

   Currently, only versions 7.6.2 and 7.10.2 support large query isolation.
