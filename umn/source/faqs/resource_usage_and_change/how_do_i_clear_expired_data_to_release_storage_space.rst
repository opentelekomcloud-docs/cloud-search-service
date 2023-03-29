:original_name: css_02_0067.html

.. _css_02_0067:

How Do I Clear Expired Data to Release Storage Space?
=====================================================

-  Run the following command to delete a single index data record.

   **curl -XDELETE http://IP:9200/**\ *Index_name*

   .. note::

      **IP**: the IP address of any node in the cluster

-  Run the following command to delete all Logstash data of a day. For example, delete all data on June 19, 2017:

   For a cluster in non-security mode: **curl -XDELETE 'http://IP:9200/logstash-2017.06.19*'**

   For a cluster in security mode: **curl -XDELETE -u username:password 'https://IP:9200/logstash-2017.06.19' -k**

   .. note::

      -  **username**: username of the administrator. The default value is **admin**.
      -  **password**: the password set during cluster creation
      -  **IP**: the IP address of any node in the cluster
