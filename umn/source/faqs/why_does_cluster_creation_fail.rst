:original_name: css_02_0028.html

.. _css_02_0028:

Why Does Cluster Creation Fail?
===============================

The following reasons may cause cluster creation to fail:

-  Insufficient resource quota. You are advised to increase the resource quotas. For details, see `How Do I Apply for a Higher Quota? <https://docs.otc.t-systems.com/en-us/faq/iaas/en-us_topic_0040259342.html>`__
-  The value of **Port Range/ICMP Type** in **Security Group** does not include port **9200**. Modify the security group information or select another available security group.
-  For cluster version 7.6.2 and later versions, the communication port 9300 is enabled on the subnet of user VPC by default. When you create a cluster, check whether the selected security group allows traffic from communication port 9300 in the subnet. If it does not allow traffic, modify the security group or select another security group.
