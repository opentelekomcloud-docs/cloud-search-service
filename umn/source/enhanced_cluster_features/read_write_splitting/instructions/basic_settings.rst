:original_name: en-us_topic_0000001528379313.html

.. _en-us_topic_0000001528379313:

Basic Settings
==============

#. Log in to the CSS management console.

#. Choose **Clusters** in the navigation pane. On the **Clusters** page, locate the target cluster, and click **Access Kibana** in the **Operation** column.

#. Click **Dev Tools** in the navigation tree on the left and perform the following operations:

   **Configure the primary cluster information**.

   .. code-block:: text

      PUT /_cluster/settings
      {
        "persistent" : {
          "cluster" : {
            "remote.rest" : {
              "leader1" : {
                "seeds" : [
                  "http://10.0.0.1:9200",
                  "http://10.0.0.2:9200",
                  "http://10.0.0.3:9200"
                ] ,
                  "username": "elastic",
                  "password": "*****"
              }
            }
          }
        }
      }

   .. note::

      -  Secondary clusters must be able to access the REST API (default port: 9200) of the primary cluster.
      -  The primary cluster name is **leader1** and can be changed.
      -  The value of **seeds** is the REST address of the primary cluster. Multiple values are supported. When HTTPS access is enabled, the URI schema must be changed to HTTPS.
      -  **username** and **password** are required only when the security mode is enabled for the primary cluster.
      -  After the configuration is complete, you can use the **GET \_remote/rest/info** API to obtain the connection status with the primary cluster.
