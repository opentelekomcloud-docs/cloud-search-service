:original_name: css_02_0121.html

.. _css_02_0121:

Can I Stop a CSS Cluster?
=========================

To stop a CSS cluster, you delete it. If you want to stop a cluster upon completion of a cluster migration, stop all services in the source cluster, and confirm that all data has been migrated to the destination cluster. Then delete the source cluster. You can stop services in the source cluster in the following ways:

-  If the cluster version in use supports the flow control function, you can enable one-click traffic blocking to block traffic everywhere except the O&M interface, rejecting all requests.

-  If your cluster version in use does not support traffic control, you can disable read and write for all service indexes instead. For example, if all service indexes start with **log**, run the following command on the **Dev Tools** page of Kibana:

   .. code-block:: text

      PUT log*/_settings
      {
        "index.blocks.read": true,
        "index.blocks.write": true,
        "index.blocks.metadata": true
      }
