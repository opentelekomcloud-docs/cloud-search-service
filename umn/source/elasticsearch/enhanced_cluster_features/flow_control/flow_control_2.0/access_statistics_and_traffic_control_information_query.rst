:original_name: css_01_0198.html

.. _css_01_0198:

Access Statistics and Traffic Control Information Query
=======================================================

Flow control can be implemented via an independent API.

Procedure
---------

#. Log in to the CSS management console.
#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster and click **Access Kibana** in the **Operation** column.
#. In the navigation pane on the left, choose **Dev Tools** and run the commands to query traffic control information.

   -  Check the traffic control status of all nodes.

      .. code-block:: text

         GET /_nodes/stats/filter/v2

   -  View traffic control details of all nodes.

      .. code-block:: text

         GET /_nodes/stats/filter/v2?detail

   -  View the traffic control status of a specific node.

      .. code-block:: text

         GET /_nodes/{nodeId}/stats/filter/v2

      **{nodeId}** indicates the ID of the node you want to check.

      Example response:

      .. code-block::

         {
           "_nodes" : {
             "total" : 1,
             "successful" : 1,
             "failed" : 0
           },
           "cluster_name" : "css-xxxx",
           "nodes" : {
             "d3qnVIpPTtSoadkV0LQEkA" : {
               "name" : "css-xxxx-ess-esn-1-1",
               "host" : "192.168.x.x",
               "timestamp" : 1672236425112,
               "flow_control" : {
                 "http" : {
                   "current_connect" : 52,
                   "rejected_concurrent" : 0,
                   "rejected_rate" : 0,
                   "rejected_black" : 0,
                   "rejected_breaker" : 0
                 },
                 "access_items" : [
                   {
                     "remote_address" : "10.0.0.x",
                     "search_count" : 0,
                     "bulk_count" : 0,
                     "other_count" : 4
                   }
                 ],
                 "holding_requests" : 0
               }
             }
           }
         }

      .. table:: **Table 1** Response parameters

         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | Parameter           | Description                                                                                                                                                                                                                         |
         +=====================+=====================================================================================================================================================================================================================================+
         | current_connect     | Number of HTTP connections of a node, which is recorded even if flow control is disabled. This value is equal to the **current_open** value of **GET /_nodes/stats/http** API. It includes the current client connections of nodes. |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | rejected_concurrent | Number of concurrent connections rejected during HTTP flow control. This value is not cleared when HTTP flow control is disabled.                                                                                                   |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | rejected_rate       | Number of new connections rejected during HTTP flow control. This value is not cleared when HTTP flow control is disabled.                                                                                                          |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | rejected_black      | Number of requests rejected based on the blacklist during HTTP flow control. This value is not cleared when HTTP flow control is disabled.                                                                                          |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | rejected_breaker    | Number of rejected new connections after one-click traffic blocking is enabled.                                                                                                                                                     |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | remote_address      | IP addresses and the number of requests.                                                                                                                                                                                            |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | search_count        | Number of times that a client accessed a database using **\_search** and **\_msearch**.                                                                                                                                             |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | bulk_count          | Number of times that a client accessed a database using **\_bulk**.                                                                                                                                                                 |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
         | other_count         | Number of times that a client accessed a database using other requests.                                                                                                                                                             |
         +---------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
