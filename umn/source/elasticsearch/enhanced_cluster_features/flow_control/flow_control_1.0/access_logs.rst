:original_name: css_01_0146.html

.. _css_01_0146:

Access Logs
===========

Context
-------

You can check access logs in either of the following ways:

-  Enable and check access logs via an independent API. Configure the API parameters to record the access log time and size. The access log content is returned through a REST API.
-  Print access logs. Your access logs are printed as files in backend logs.

Enabling the access log function may affect cluster performance.

The following table describes access log parameters.

.. table:: **Table 1** Access log parameters

   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | Parameter             | Type                  | Description                                                                                                                                                                  |
   +=======================+=======================+==============================================================================================================================================================================+
   | duration_limit        | String                | Duration recorded in an access log.                                                                                                                                          |
   |                       |                       |                                                                                                                                                                              |
   |                       |                       | Value range: 10 to 120                                                                                                                                                       |
   |                       |                       |                                                                                                                                                                              |
   |                       |                       | Unit: s                                                                                                                                                                      |
   |                       |                       |                                                                                                                                                                              |
   |                       |                       | Default value: **30**                                                                                                                                                        |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
   | capacity_limit        | String                | Size of an access log. After access logging is enabled, the size of recorded requests is checked. If the size exceeds the value of this parameter, the access logging stops. |
   |                       |                       |                                                                                                                                                                              |
   |                       |                       | Value range: 1 to 5                                                                                                                                                          |
   |                       |                       |                                                                                                                                                                              |
   |                       |                       | Unit: MB                                                                                                                                                                     |
   |                       |                       |                                                                                                                                                                              |
   |                       |                       | Default value: **1**                                                                                                                                                         |
   +-----------------------+-----------------------+------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

.. note::

   Access logging stops if either **duration_limit** or **capacity_limit** reaches the threshold.

Procedure
---------

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.

#. In the navigation pane on the left, choose **Dev Tools** and run commands to enable or disable access logs.

   -  Enabling access logs for all nodes in a cluster

      .. code-block:: text

         PUT /_access_log?duration_limit=30s&capacity_limit=1mb

   -  Enabling access logs for a node in a cluster

      .. code-block:: text

         PUT /_access_log/{nodeId}?duration_limit=30s&capacity_limit=1mb

      *{nodeId}* indicates the ID of the node where you want to enable access logs.

#. Use APIs to check access logs.

   -  API for checking the access logs of all nodes in a cluster

      .. code-block:: text

         GET /_access_log

   -  API for checking the access logs of a node in a cluster

      .. code-block:: text

         GET /_access_log/{nodeId}

      *{nodeId}* indicates the ID of the node where you want to enable access logs.

   Example response:

   .. code-block::

      {
        "_nodes" : {
          "total" : 1,
          "successful" : 1,
          "failed" : 0
        },
        "cluster_name" : "css-flowcontroller",
        "nodes" : {
          "8x-ZHu-wTemBQwpcGivFKg" : {
            "name" : "css-flowcontroller-ess-esn-1-1",
            "host" : "10.0.0.98",
            "count" : 2,
            "access" : [
              {
                "time" : "2021-02-23 02:09:50",
                "remote_address" : "/10.0.0.98:28191",
                "url" : "/_access/security/log?pretty",
                "method" : "GET",
                "content" : ""
              },
              {
                "time" : "2021-02-23 02:09:52",
                "remote_address" : "/10.0.0.98:28193",
                "url" : "/_access/security/log?pretty",
                "method" : "GET",
                "content" : ""
              }
            ]
          }
        }
      }

   .. table:: **Table 2** Response parameters

      +-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | Parameter | Description                                                                                                                                                |
      +===========+============================================================================================================================================================+
      | name      | Node name                                                                                                                                                  |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | host      | Node IP address                                                                                                                                            |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | count     | Number of node access requests in a statistical period                                                                                                     |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------+
      | access    | Details about node access requests in a statistical period For details, see :ref:`Table 3 <css_01_0146__en-us_topic_0000001272932417_table1631713296470>`. |
      +-----------+------------------------------------------------------------------------------------------------------------------------------------------------------------+

   .. _css_01_0146__en-us_topic_0000001272932417_table1631713296470:

   .. table:: **Table 3** access

      ============== ================================================
      Parameter      Description
      ============== ================================================
      time           Request time
      remote_address Source IP address and port number of the request
      url            Original URL of the request
      method         Method corresponding to the request path
      content        Request content
      ============== ================================================

#. Enable or disable the access log function.

   All user access operation can be logged. By default, logs are recorded in the **acces_log.log** file in the background. The maximum size of a log file is 250 MB, and there can be a maximum of five log files. You can back up access log files to OBS.

   -  Enabling access logs

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.accesslog.enabled": true
            }
         }

   -  Disabling access logs

      .. code-block:: text

         PUT /_cluster/settings
         {
           "persistent": {
             "flowcontrol.accesslog.enabled": false
            }
         }
