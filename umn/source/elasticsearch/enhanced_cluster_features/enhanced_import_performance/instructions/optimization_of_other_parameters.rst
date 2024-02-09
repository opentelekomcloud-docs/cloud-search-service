:original_name: css_01_0233.html

.. _css_01_0233:

Optimization of Other Parameters
================================

After the import optimization function is enabled, the number of index merge tasks will increase. You can configure the following parameters to reduce the impact of merge task overhead on the import performance:

You can increase the value of **index.merge.scheduler.max_thread_count** to increase the number of shard merge threads and reduce the traffic limit on data import. The default value is **4**. You are advised to set it to **8**.
