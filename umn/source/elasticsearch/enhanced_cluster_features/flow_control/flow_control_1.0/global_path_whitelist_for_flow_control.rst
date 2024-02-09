:original_name: css_01_0143.html

.. _css_01_0143:

Global Path Whitelist for Flow Control
======================================

Context
-------

The following table describes the global path whitelist parameters for flow control.

.. table:: **Table 1** Global path whitelist parameters for flow control

   +-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter                   | Type                  | Description                                                                                                                                                                       |
   +=============================+=======================+===================================================================================================================================================================================+
   | flowcontrol.path.white_list | List<String>          | Paths that are not under flow control. These paths are not affected by memory flow control, CPU flow control, or one-click blocking; but are under IP address-based flow control. |
   |                             |                       |                                                                                                                                                                                   |
   |                             |                       | A maximum of 10 paths can be configured. A path can contain up to 32 characters.                                                                                                  |
   |                             |                       |                                                                                                                                                                                   |
   |                             |                       | This parameter is left blank by default.                                                                                                                                          |
   |                             |                       |                                                                                                                                                                                   |
   |                             |                       | .. note::                                                                                                                                                                         |
   |                             |                       |                                                                                                                                                                                   |
   |                             |                       |    You are advised not to configure this parameter, unless required by plug-ins.                                                                                                  |
   +-----------------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

Procedure
---------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. In the navigation tree on the left, choose **Dev Tools**. Run the following command to configure the global path whitelist for flow control:

   .. code-block:: text

      PUT _cluster/settings
      {
        "persistent": {
          "flowcontrol.path.white_list": "xxxx"
        }
      }
